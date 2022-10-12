'''
# `google_dataproc_workflow_template`

Refer to the Terraform Registory for docs: [`google_dataproc_workflow_template`](https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template).
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


class GoogleDataprocWorkflowTemplate(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplate",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template google_dataproc_workflow_template}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        jobs: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataprocWorkflowTemplateJobs", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        placement: typing.Union["GoogleDataprocWorkflowTemplatePlacement", typing.Dict[str, typing.Any]],
        dag_timeout: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        parameters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataprocWorkflowTemplateParameters", typing.Dict[str, typing.Any]]]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateTimeouts", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template google_dataproc_workflow_template} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param jobs: jobs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jobs GoogleDataprocWorkflowTemplate#jobs}
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#location GoogleDataprocWorkflowTemplate#location}
        :param name: Output only. The resource name of the workflow template, as described in https://cloud.google.com/apis/design/resource_names. * For ``projects.regions.workflowTemplates``, the resource name of the template has the following format: ``projects/{project_id}/regions/{region}/workflowTemplates/{template_id}`` * For ``projects.locations.workflowTemplates``, the resource name of the template has the following format: ``projects/{project_id}/locations/{location}/workflowTemplates/{template_id}`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#name GoogleDataprocWorkflowTemplate#name}
        :param placement: placement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#placement GoogleDataprocWorkflowTemplate#placement}
        :param dag_timeout: Optional. Timeout duration for the DAG of jobs, expressed in seconds (see `JSON representation of duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`_). The timeout duration must be from 10 minutes ("600s") to 24 hours ("86400s"). The timer begins when the first job is submitted. If the workflow is running at the end of the timeout period, any remaining jobs are cancelled, the workflow is ended, and if the workflow was running on a `managed cluster </dataproc/docs/concepts/workflows/using-workflows#configuring_or_selecting_a_cluster>`_, the cluster is deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#dag_timeout GoogleDataprocWorkflowTemplate#dag_timeout}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#id GoogleDataprocWorkflowTemplate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Optional. The labels to associate with this template. These labels will be propagated to all jobs and clusters created by the workflow instance. Label **keys** must contain 1 to 63 characters, and must conform to `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`_. Label **values** may be empty, but, if present, must contain 1 to 63 characters, and must conform to `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`_. No more than 32 labels can be associated with a template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#labels GoogleDataprocWorkflowTemplate#labels}
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#parameters GoogleDataprocWorkflowTemplate#parameters}
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#project GoogleDataprocWorkflowTemplate#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#timeouts GoogleDataprocWorkflowTemplate#timeouts}
        :param version: Output only. The current version of this workflow template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#version GoogleDataprocWorkflowTemplate#version}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDataprocWorkflowTemplateConfig(
            jobs=jobs,
            location=location,
            name=name,
            placement=placement,
            dag_timeout=dag_timeout,
            id=id,
            labels=labels,
            parameters=parameters,
            project=project,
            timeouts=timeouts,
            version=version,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putJobs")
    def put_jobs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataprocWorkflowTemplateJobs", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplate.put_jobs)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putJobs", [value]))

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataprocWorkflowTemplateParameters", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplate.put_parameters)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="putPlacement")
    def put_placement(
        self,
        *,
        cluster_selector: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementClusterSelector", typing.Dict[str, typing.Any]]] = None,
        managed_cluster: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedCluster", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cluster_selector: cluster_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cluster_selector GoogleDataprocWorkflowTemplate#cluster_selector}
        :param managed_cluster: managed_cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#managed_cluster GoogleDataprocWorkflowTemplate#managed_cluster}
        '''
        value = GoogleDataprocWorkflowTemplatePlacement(
            cluster_selector=cluster_selector, managed_cluster=managed_cluster
        )

        return typing.cast(None, jsii.invoke(self, "putPlacement", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#create GoogleDataprocWorkflowTemplate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#delete GoogleDataprocWorkflowTemplate#delete}.
        '''
        value = GoogleDataprocWorkflowTemplateTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDagTimeout")
    def reset_dag_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDagTimeout", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="jobs")
    def jobs(self) -> "GoogleDataprocWorkflowTemplateJobsList":
        return typing.cast("GoogleDataprocWorkflowTemplateJobsList", jsii.get(self, "jobs"))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> "GoogleDataprocWorkflowTemplateParametersList":
        return typing.cast("GoogleDataprocWorkflowTemplateParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="placement")
    def placement(self) -> "GoogleDataprocWorkflowTemplatePlacementOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplatePlacementOutputReference", jsii.get(self, "placement"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleDataprocWorkflowTemplateTimeoutsOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplateTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="dagTimeoutInput")
    def dag_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dagTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="jobsInput")
    def jobs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplateJobs"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplateJobs"]]], jsii.get(self, "jobsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplateParameters"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplateParameters"]]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="placementInput")
    def placement_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacement"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacement"], jsii.get(self, "placementInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="dagTimeout")
    def dag_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dagTimeout"))

    @dag_timeout.setter
    def dag_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplate, "dag_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dagTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplate, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplate, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplate, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplate, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplate, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @version.setter
    def version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplate, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "jobs": "jobs",
        "location": "location",
        "name": "name",
        "placement": "placement",
        "dag_timeout": "dagTimeout",
        "id": "id",
        "labels": "labels",
        "parameters": "parameters",
        "project": "project",
        "timeouts": "timeouts",
        "version": "version",
    },
)
class GoogleDataprocWorkflowTemplateConfig(cdktf.TerraformMetaArguments):
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
        jobs: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataprocWorkflowTemplateJobs", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        placement: typing.Union["GoogleDataprocWorkflowTemplatePlacement", typing.Dict[str, typing.Any]],
        dag_timeout: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        parameters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataprocWorkflowTemplateParameters", typing.Dict[str, typing.Any]]]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateTimeouts", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param jobs: jobs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jobs GoogleDataprocWorkflowTemplate#jobs}
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#location GoogleDataprocWorkflowTemplate#location}
        :param name: Output only. The resource name of the workflow template, as described in https://cloud.google.com/apis/design/resource_names. * For ``projects.regions.workflowTemplates``, the resource name of the template has the following format: ``projects/{project_id}/regions/{region}/workflowTemplates/{template_id}`` * For ``projects.locations.workflowTemplates``, the resource name of the template has the following format: ``projects/{project_id}/locations/{location}/workflowTemplates/{template_id}`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#name GoogleDataprocWorkflowTemplate#name}
        :param placement: placement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#placement GoogleDataprocWorkflowTemplate#placement}
        :param dag_timeout: Optional. Timeout duration for the DAG of jobs, expressed in seconds (see `JSON representation of duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`_). The timeout duration must be from 10 minutes ("600s") to 24 hours ("86400s"). The timer begins when the first job is submitted. If the workflow is running at the end of the timeout period, any remaining jobs are cancelled, the workflow is ended, and if the workflow was running on a `managed cluster </dataproc/docs/concepts/workflows/using-workflows#configuring_or_selecting_a_cluster>`_, the cluster is deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#dag_timeout GoogleDataprocWorkflowTemplate#dag_timeout}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#id GoogleDataprocWorkflowTemplate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Optional. The labels to associate with this template. These labels will be propagated to all jobs and clusters created by the workflow instance. Label **keys** must contain 1 to 63 characters, and must conform to `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`_. Label **values** may be empty, but, if present, must contain 1 to 63 characters, and must conform to `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`_. No more than 32 labels can be associated with a template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#labels GoogleDataprocWorkflowTemplate#labels}
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#parameters GoogleDataprocWorkflowTemplate#parameters}
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#project GoogleDataprocWorkflowTemplate#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#timeouts GoogleDataprocWorkflowTemplate#timeouts}
        :param version: Output only. The current version of this workflow template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#version GoogleDataprocWorkflowTemplate#version}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(placement, dict):
            placement = GoogleDataprocWorkflowTemplatePlacement(**placement)
        if isinstance(timeouts, dict):
            timeouts = GoogleDataprocWorkflowTemplateTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument jobs", value=jobs, expected_type=type_hints["jobs"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument placement", value=placement, expected_type=type_hints["placement"])
            check_type(argname="argument dag_timeout", value=dag_timeout, expected_type=type_hints["dag_timeout"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "jobs": jobs,
            "location": location,
            "name": name,
            "placement": placement,
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
        if dag_timeout is not None:
            self._values["dag_timeout"] = dag_timeout
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if parameters is not None:
            self._values["parameters"] = parameters
        if project is not None:
            self._values["project"] = project
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if version is not None:
            self._values["version"] = version

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
    def jobs(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplateJobs"]]:
        '''jobs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jobs GoogleDataprocWorkflowTemplate#jobs}
        '''
        result = self._values.get("jobs")
        assert result is not None, "Required property 'jobs' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplateJobs"]], result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The location for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#location GoogleDataprocWorkflowTemplate#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Output only.

        The resource name of the workflow template, as described in https://cloud.google.com/apis/design/resource_names. * For ``projects.regions.workflowTemplates``, the resource name of the template has the following format: ``projects/{project_id}/regions/{region}/workflowTemplates/{template_id}`` * For ``projects.locations.workflowTemplates``, the resource name of the template has the following format: ``projects/{project_id}/locations/{location}/workflowTemplates/{template_id}``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#name GoogleDataprocWorkflowTemplate#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def placement(self) -> "GoogleDataprocWorkflowTemplatePlacement":
        '''placement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#placement GoogleDataprocWorkflowTemplate#placement}
        '''
        result = self._values.get("placement")
        assert result is not None, "Required property 'placement' is missing"
        return typing.cast("GoogleDataprocWorkflowTemplatePlacement", result)

    @builtins.property
    def dag_timeout(self) -> typing.Optional[builtins.str]:
        '''Optional.

        Timeout duration for the DAG of jobs, expressed in seconds (see `JSON representation of duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`_). The timeout duration must be from 10 minutes ("600s") to 24 hours ("86400s"). The timer begins when the first job is submitted. If the workflow is running at the end of the timeout period, any remaining jobs are cancelled, the workflow is ended, and if the workflow was running on a `managed cluster </dataproc/docs/concepts/workflows/using-workflows#configuring_or_selecting_a_cluster>`_, the cluster is deleted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#dag_timeout GoogleDataprocWorkflowTemplate#dag_timeout}
        '''
        result = self._values.get("dag_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#id GoogleDataprocWorkflowTemplate#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        The labels to associate with this template. These labels will be propagated to all jobs and clusters created by the workflow instance. Label **keys** must contain 1 to 63 characters, and must conform to `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`_. Label **values** may be empty, but, if present, must contain 1 to 63 characters, and must conform to `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`_. No more than 32 labels can be associated with a template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#labels GoogleDataprocWorkflowTemplate#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplateParameters"]]]:
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#parameters GoogleDataprocWorkflowTemplate#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplateParameters"]]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#project GoogleDataprocWorkflowTemplate#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDataprocWorkflowTemplateTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#timeouts GoogleDataprocWorkflowTemplate#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateTimeouts"], result)

    @builtins.property
    def version(self) -> typing.Optional[jsii.Number]:
        '''Output only. The current version of this workflow template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#version GoogleDataprocWorkflowTemplate#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobs",
    jsii_struct_bases=[],
    name_mapping={
        "step_id": "stepId",
        "hadoop_job": "hadoopJob",
        "hive_job": "hiveJob",
        "labels": "labels",
        "pig_job": "pigJob",
        "prerequisite_step_ids": "prerequisiteStepIds",
        "presto_job": "prestoJob",
        "pyspark_job": "pysparkJob",
        "scheduling": "scheduling",
        "spark_job": "sparkJob",
        "spark_r_job": "sparkRJob",
        "spark_sql_job": "sparkSqlJob",
    },
)
class GoogleDataprocWorkflowTemplateJobs:
    def __init__(
        self,
        *,
        step_id: builtins.str,
        hadoop_job: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsHadoopJob", typing.Dict[str, typing.Any]]] = None,
        hive_job: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsHiveJob", typing.Dict[str, typing.Any]]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        pig_job: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsPigJob", typing.Dict[str, typing.Any]]] = None,
        prerequisite_step_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        presto_job: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsPrestoJob", typing.Dict[str, typing.Any]]] = None,
        pyspark_job: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsPysparkJob", typing.Dict[str, typing.Any]]] = None,
        scheduling: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsScheduling", typing.Dict[str, typing.Any]]] = None,
        spark_job: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsSparkJob", typing.Dict[str, typing.Any]]] = None,
        spark_r_job: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsSparkRJob", typing.Dict[str, typing.Any]]] = None,
        spark_sql_job: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsSparkSqlJob", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param step_id: Required. The step id. The id must be unique among all jobs within the template. The step id is used as prefix for job id, as job ``goog-dataproc-workflow-step-id`` label, and in prerequisiteStepIds field from other steps. The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between 3 and 50 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#step_id GoogleDataprocWorkflowTemplate#step_id}
        :param hadoop_job: hadoop_job block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#hadoop_job GoogleDataprocWorkflowTemplate#hadoop_job}
        :param hive_job: hive_job block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#hive_job GoogleDataprocWorkflowTemplate#hive_job}
        :param labels: Optional. The labels to associate with this job. Label keys must be between 1 and 63 characters long, and must conform to the following regular expression: p{Ll}p{Lo}{0,62} Label values must be between 1 and 63 characters long, and must conform to the following regular expression: [p{Ll}p{Lo}p{N}_-]{0,63} No more than 32 labels can be associated with a given job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#labels GoogleDataprocWorkflowTemplate#labels}
        :param pig_job: pig_job block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#pig_job GoogleDataprocWorkflowTemplate#pig_job}
        :param prerequisite_step_ids: Optional. The optional list of prerequisite job step_ids. If not specified, the job will start at the beginning of workflow. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#prerequisite_step_ids GoogleDataprocWorkflowTemplate#prerequisite_step_ids}
        :param presto_job: presto_job block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#presto_job GoogleDataprocWorkflowTemplate#presto_job}
        :param pyspark_job: pyspark_job block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#pyspark_job GoogleDataprocWorkflowTemplate#pyspark_job}
        :param scheduling: scheduling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#scheduling GoogleDataprocWorkflowTemplate#scheduling}
        :param spark_job: spark_job block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#spark_job GoogleDataprocWorkflowTemplate#spark_job}
        :param spark_r_job: spark_r_job block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#spark_r_job GoogleDataprocWorkflowTemplate#spark_r_job}
        :param spark_sql_job: spark_sql_job block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#spark_sql_job GoogleDataprocWorkflowTemplate#spark_sql_job}
        '''
        if isinstance(hadoop_job, dict):
            hadoop_job = GoogleDataprocWorkflowTemplateJobsHadoopJob(**hadoop_job)
        if isinstance(hive_job, dict):
            hive_job = GoogleDataprocWorkflowTemplateJobsHiveJob(**hive_job)
        if isinstance(pig_job, dict):
            pig_job = GoogleDataprocWorkflowTemplateJobsPigJob(**pig_job)
        if isinstance(presto_job, dict):
            presto_job = GoogleDataprocWorkflowTemplateJobsPrestoJob(**presto_job)
        if isinstance(pyspark_job, dict):
            pyspark_job = GoogleDataprocWorkflowTemplateJobsPysparkJob(**pyspark_job)
        if isinstance(scheduling, dict):
            scheduling = GoogleDataprocWorkflowTemplateJobsScheduling(**scheduling)
        if isinstance(spark_job, dict):
            spark_job = GoogleDataprocWorkflowTemplateJobsSparkJob(**spark_job)
        if isinstance(spark_r_job, dict):
            spark_r_job = GoogleDataprocWorkflowTemplateJobsSparkRJob(**spark_r_job)
        if isinstance(spark_sql_job, dict):
            spark_sql_job = GoogleDataprocWorkflowTemplateJobsSparkSqlJob(**spark_sql_job)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobs.__init__)
            check_type(argname="argument step_id", value=step_id, expected_type=type_hints["step_id"])
            check_type(argname="argument hadoop_job", value=hadoop_job, expected_type=type_hints["hadoop_job"])
            check_type(argname="argument hive_job", value=hive_job, expected_type=type_hints["hive_job"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument pig_job", value=pig_job, expected_type=type_hints["pig_job"])
            check_type(argname="argument prerequisite_step_ids", value=prerequisite_step_ids, expected_type=type_hints["prerequisite_step_ids"])
            check_type(argname="argument presto_job", value=presto_job, expected_type=type_hints["presto_job"])
            check_type(argname="argument pyspark_job", value=pyspark_job, expected_type=type_hints["pyspark_job"])
            check_type(argname="argument scheduling", value=scheduling, expected_type=type_hints["scheduling"])
            check_type(argname="argument spark_job", value=spark_job, expected_type=type_hints["spark_job"])
            check_type(argname="argument spark_r_job", value=spark_r_job, expected_type=type_hints["spark_r_job"])
            check_type(argname="argument spark_sql_job", value=spark_sql_job, expected_type=type_hints["spark_sql_job"])
        self._values: typing.Dict[str, typing.Any] = {
            "step_id": step_id,
        }
        if hadoop_job is not None:
            self._values["hadoop_job"] = hadoop_job
        if hive_job is not None:
            self._values["hive_job"] = hive_job
        if labels is not None:
            self._values["labels"] = labels
        if pig_job is not None:
            self._values["pig_job"] = pig_job
        if prerequisite_step_ids is not None:
            self._values["prerequisite_step_ids"] = prerequisite_step_ids
        if presto_job is not None:
            self._values["presto_job"] = presto_job
        if pyspark_job is not None:
            self._values["pyspark_job"] = pyspark_job
        if scheduling is not None:
            self._values["scheduling"] = scheduling
        if spark_job is not None:
            self._values["spark_job"] = spark_job
        if spark_r_job is not None:
            self._values["spark_r_job"] = spark_r_job
        if spark_sql_job is not None:
            self._values["spark_sql_job"] = spark_sql_job

    @builtins.property
    def step_id(self) -> builtins.str:
        '''Required.

        The step id. The id must be unique among all jobs within the template. The step id is used as prefix for job id, as job ``goog-dataproc-workflow-step-id`` label, and in prerequisiteStepIds field from other steps. The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between 3 and 50 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#step_id GoogleDataprocWorkflowTemplate#step_id}
        '''
        result = self._values.get("step_id")
        assert result is not None, "Required property 'step_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hadoop_job(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsHadoopJob"]:
        '''hadoop_job block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#hadoop_job GoogleDataprocWorkflowTemplate#hadoop_job}
        '''
        result = self._values.get("hadoop_job")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsHadoopJob"], result)

    @builtins.property
    def hive_job(self) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsHiveJob"]:
        '''hive_job block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#hive_job GoogleDataprocWorkflowTemplate#hive_job}
        '''
        result = self._values.get("hive_job")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsHiveJob"], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        The labels to associate with this job. Label keys must be between 1 and 63 characters long, and must conform to the following regular expression: p{Ll}p{Lo}{0,62} Label values must be between 1 and 63 characters long, and must conform to the following regular expression: [p{Ll}p{Lo}p{N}_-]{0,63} No more than 32 labels can be associated with a given job.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#labels GoogleDataprocWorkflowTemplate#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def pig_job(self) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsPigJob"]:
        '''pig_job block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#pig_job GoogleDataprocWorkflowTemplate#pig_job}
        '''
        result = self._values.get("pig_job")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsPigJob"], result)

    @builtins.property
    def prerequisite_step_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        The optional list of prerequisite job step_ids. If not specified, the job will start at the beginning of workflow.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#prerequisite_step_ids GoogleDataprocWorkflowTemplate#prerequisite_step_ids}
        '''
        result = self._values.get("prerequisite_step_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def presto_job(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsPrestoJob"]:
        '''presto_job block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#presto_job GoogleDataprocWorkflowTemplate#presto_job}
        '''
        result = self._values.get("presto_job")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsPrestoJob"], result)

    @builtins.property
    def pyspark_job(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsPysparkJob"]:
        '''pyspark_job block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#pyspark_job GoogleDataprocWorkflowTemplate#pyspark_job}
        '''
        result = self._values.get("pyspark_job")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsPysparkJob"], result)

    @builtins.property
    def scheduling(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsScheduling"]:
        '''scheduling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#scheduling GoogleDataprocWorkflowTemplate#scheduling}
        '''
        result = self._values.get("scheduling")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsScheduling"], result)

    @builtins.property
    def spark_job(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkJob"]:
        '''spark_job block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#spark_job GoogleDataprocWorkflowTemplate#spark_job}
        '''
        result = self._values.get("spark_job")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkJob"], result)

    @builtins.property
    def spark_r_job(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkRJob"]:
        '''spark_r_job block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#spark_r_job GoogleDataprocWorkflowTemplate#spark_r_job}
        '''
        result = self._values.get("spark_r_job")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkRJob"], result)

    @builtins.property
    def spark_sql_job(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkSqlJob"]:
        '''spark_sql_job block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#spark_sql_job GoogleDataprocWorkflowTemplate#spark_sql_job}
        '''
        result = self._values.get("spark_sql_job")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkSqlJob"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsHadoopJob",
    jsii_struct_bases=[],
    name_mapping={
        "archive_uris": "archiveUris",
        "args": "args",
        "file_uris": "fileUris",
        "jar_file_uris": "jarFileUris",
        "logging_config": "loggingConfig",
        "main_class": "mainClass",
        "main_jar_file_uri": "mainJarFileUri",
        "properties": "properties",
    },
)
class GoogleDataprocWorkflowTemplateJobsHadoopJob:
    def __init__(
        self,
        *,
        archive_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        main_class: typing.Optional[builtins.str] = None,
        main_jar_file_uri: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param archive_uris: Optional. HCFS URIs of archives to be extracted in the working directory of Hadoop drivers and tasks. Supported file types: .jar, .tar, .tar.gz, .tgz, or .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#archive_uris GoogleDataprocWorkflowTemplate#archive_uris}
        :param args: Optional. The arguments to pass to the driver. Do not include arguments, such as ``-libjars`` or ``-Dfoo=bar``, that can be set as job properties, since a collision may occur that causes an incorrect job submission. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#args GoogleDataprocWorkflowTemplate#args}
        :param file_uris: Optional. HCFS (Hadoop Compatible Filesystem) URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#file_uris GoogleDataprocWorkflowTemplate#file_uris}
        :param jar_file_uris: Optional. Jar file URIs to add to the CLASSPATHs of the Hadoop driver and tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        :param main_class: The name of the driver's main class. The jar file containing the class must be in the default CLASSPATH or specified in ``jar_file_uris``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_class GoogleDataprocWorkflowTemplate#main_class}
        :param main_jar_file_uri: The HCFS URI of the jar file containing the main class. Examples: 'gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar' 'hdfs:/tmp/test-samples/custom-wordcount.jar' 'file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_jar_file_uri GoogleDataprocWorkflowTemplate#main_jar_file_uri}
        :param properties: Optional. A mapping of property names to values, used to configure Hadoop. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/hadoop/conf/*-site and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        if isinstance(logging_config, dict):
            logging_config = GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig(**logging_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsHadoopJob.__init__)
            check_type(argname="argument archive_uris", value=archive_uris, expected_type=type_hints["archive_uris"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument file_uris", value=file_uris, expected_type=type_hints["file_uris"])
            check_type(argname="argument jar_file_uris", value=jar_file_uris, expected_type=type_hints["jar_file_uris"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument main_class", value=main_class, expected_type=type_hints["main_class"])
            check_type(argname="argument main_jar_file_uri", value=main_jar_file_uri, expected_type=type_hints["main_jar_file_uri"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[str, typing.Any] = {}
        if archive_uris is not None:
            self._values["archive_uris"] = archive_uris
        if args is not None:
            self._values["args"] = args
        if file_uris is not None:
            self._values["file_uris"] = file_uris
        if jar_file_uris is not None:
            self._values["jar_file_uris"] = jar_file_uris
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if main_class is not None:
            self._values["main_class"] = main_class
        if main_jar_file_uri is not None:
            self._values["main_jar_file_uri"] = main_jar_file_uri
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def archive_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        HCFS URIs of archives to be extracted in the working directory of Hadoop drivers and tasks. Supported file types: .jar, .tar, .tar.gz, .tgz, or .zip.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#archive_uris GoogleDataprocWorkflowTemplate#archive_uris}
        '''
        result = self._values.get("archive_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        The arguments to pass to the driver. Do not include arguments, such as ``-libjars`` or ``-Dfoo=bar``, that can be set as job properties, since a collision may occur that causes an incorrect job submission.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#args GoogleDataprocWorkflowTemplate#args}
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        HCFS (Hadoop Compatible Filesystem) URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#file_uris GoogleDataprocWorkflowTemplate#file_uris}
        '''
        result = self._values.get("file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def jar_file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional. Jar file URIs to add to the CLASSPATHs of the Hadoop driver and tasks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        '''
        result = self._values.get("jar_file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig"]:
        '''logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig"], result)

    @builtins.property
    def main_class(self) -> typing.Optional[builtins.str]:
        '''The name of the driver's main class.

        The jar file containing the class must be in the default CLASSPATH or specified in ``jar_file_uris``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_class GoogleDataprocWorkflowTemplate#main_class}
        '''
        result = self._values.get("main_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def main_jar_file_uri(self) -> typing.Optional[builtins.str]:
        '''The HCFS URI of the jar file containing the main class. Examples: 'gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar' 'hdfs:/tmp/test-samples/custom-wordcount.jar' 'file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_jar_file_uri GoogleDataprocWorkflowTemplate#main_jar_file_uri}
        '''
        result = self._values.get("main_jar_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        A mapping of property names to values, used to configure Hadoop. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/hadoop/conf/*-site and classes in user code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsHadoopJob(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={"driver_log_levels": "driverLogLevels"},
)
class GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig:
    def __init__(
        self,
        *,
        driver_log_levels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver_log_levels: The per-package log levels for the driver. This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig.__init__)
            check_type(argname="argument driver_log_levels", value=driver_log_levels, expected_type=type_hints["driver_log_levels"])
        self._values: typing.Dict[str, typing.Any] = {}
        if driver_log_levels is not None:
            self._values["driver_log_levels"] = driver_log_levels

    @builtins.property
    def driver_log_levels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The per-package log levels for the driver.

        This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        result = self._values.get("driver_log_levels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDriverLogLevels")
    def reset_driver_log_levels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverLogLevels", []))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevelsInput")
    def driver_log_levels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverLogLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevels")
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverLogLevels"))

    @driver_log_levels.setter
    def driver_log_levels(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfigOutputReference, "driver_log_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverLogLevels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplateJobsHadoopJobOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsHadoopJobOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsHadoopJobOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLoggingConfig")
    def put_logging_config(
        self,
        *,
        driver_log_levels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver_log_levels: The per-package log levels for the driver. This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        value = GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig(
            driver_log_levels=driver_log_levels
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfig", [value]))

    @jsii.member(jsii_name="resetArchiveUris")
    def reset_archive_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchiveUris", []))

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @jsii.member(jsii_name="resetFileUris")
    def reset_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileUris", []))

    @jsii.member(jsii_name="resetJarFileUris")
    def reset_jar_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJarFileUris", []))

    @jsii.member(jsii_name="resetLoggingConfig")
    def reset_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfig", []))

    @jsii.member(jsii_name="resetMainClass")
    def reset_main_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMainClass", []))

    @jsii.member(jsii_name="resetMainJarFileUri")
    def reset_main_jar_file_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMainJarFileUri", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfigOutputReference, jsii.get(self, "loggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="archiveUrisInput")
    def archive_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "archiveUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="fileUrisInput")
    def file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "fileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="jarFileUrisInput")
    def jar_file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jarFileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigInput")
    def logging_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig], jsii.get(self, "loggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="mainClassInput")
    def main_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mainClassInput"))

    @builtins.property
    @jsii.member(jsii_name="mainJarFileUriInput")
    def main_jar_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mainJarFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="archiveUris")
    def archive_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "archiveUris"))

    @archive_uris.setter
    def archive_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHadoopJobOutputReference, "archive_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archiveUris", value)

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHadoopJobOutputReference, "args").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

    @builtins.property
    @jsii.member(jsii_name="fileUris")
    def file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "fileUris"))

    @file_uris.setter
    def file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHadoopJobOutputReference, "file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileUris", value)

    @builtins.property
    @jsii.member(jsii_name="jarFileUris")
    def jar_file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jarFileUris"))

    @jar_file_uris.setter
    def jar_file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHadoopJobOutputReference, "jar_file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jarFileUris", value)

    @builtins.property
    @jsii.member(jsii_name="mainClass")
    def main_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mainClass"))

    @main_class.setter
    def main_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHadoopJobOutputReference, "main_class").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mainClass", value)

    @builtins.property
    @jsii.member(jsii_name="mainJarFileUri")
    def main_jar_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mainJarFileUri"))

    @main_jar_file_uri.setter
    def main_jar_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHadoopJobOutputReference, "main_jar_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mainJarFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHadoopJobOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsHadoopJob]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsHadoopJob], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsHadoopJob],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHadoopJobOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsHiveJob",
    jsii_struct_bases=[],
    name_mapping={
        "continue_on_failure": "continueOnFailure",
        "jar_file_uris": "jarFileUris",
        "properties": "properties",
        "query_file_uri": "queryFileUri",
        "query_list": "queryList",
        "script_variables": "scriptVariables",
    },
)
class GoogleDataprocWorkflowTemplateJobsHiveJob:
    def __init__(
        self,
        *,
        continue_on_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsHiveJobQueryList", typing.Dict[str, typing.Any]]] = None,
        script_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param continue_on_failure: Optional. Whether to continue executing queries if a query fails. The default value is ``false``. Setting to ``true`` can be useful when executing independent parallel queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#continue_on_failure GoogleDataprocWorkflowTemplate#continue_on_failure}
        :param jar_file_uris: Optional. HCFS URIs of jar files to add to the CLASSPATH of the Hive server and Hadoop MapReduce (MR) tasks. Can contain Hive SerDes and UDFs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        :param properties: Optional. A mapping of property names and values, used to configure Hive. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/hadoop/conf/*-site.xml, /etc/hive/conf/hive-site.xml, and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        :param query_file_uri: The HCFS URI of the script that contains Hive queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_file_uri GoogleDataprocWorkflowTemplate#query_file_uri}
        :param query_list: query_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_list GoogleDataprocWorkflowTemplate#query_list}
        :param script_variables: Optional. Mapping of query variable names to values (equivalent to the Hive command: ``SET name="value";``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#script_variables GoogleDataprocWorkflowTemplate#script_variables}
        '''
        if isinstance(query_list, dict):
            query_list = GoogleDataprocWorkflowTemplateJobsHiveJobQueryList(**query_list)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsHiveJob.__init__)
            check_type(argname="argument continue_on_failure", value=continue_on_failure, expected_type=type_hints["continue_on_failure"])
            check_type(argname="argument jar_file_uris", value=jar_file_uris, expected_type=type_hints["jar_file_uris"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument query_file_uri", value=query_file_uri, expected_type=type_hints["query_file_uri"])
            check_type(argname="argument query_list", value=query_list, expected_type=type_hints["query_list"])
            check_type(argname="argument script_variables", value=script_variables, expected_type=type_hints["script_variables"])
        self._values: typing.Dict[str, typing.Any] = {}
        if continue_on_failure is not None:
            self._values["continue_on_failure"] = continue_on_failure
        if jar_file_uris is not None:
            self._values["jar_file_uris"] = jar_file_uris
        if properties is not None:
            self._values["properties"] = properties
        if query_file_uri is not None:
            self._values["query_file_uri"] = query_file_uri
        if query_list is not None:
            self._values["query_list"] = query_list
        if script_variables is not None:
            self._values["script_variables"] = script_variables

    @builtins.property
    def continue_on_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional.

        Whether to continue executing queries if a query fails. The default value is ``false``. Setting to ``true`` can be useful when executing independent parallel queries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#continue_on_failure GoogleDataprocWorkflowTemplate#continue_on_failure}
        '''
        result = self._values.get("continue_on_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def jar_file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        HCFS URIs of jar files to add to the CLASSPATH of the Hive server and Hadoop MapReduce (MR) tasks. Can contain Hive SerDes and UDFs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        '''
        result = self._values.get("jar_file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        A mapping of property names and values, used to configure Hive. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/hadoop/conf/*-site.xml, /etc/hive/conf/hive-site.xml, and classes in user code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def query_file_uri(self) -> typing.Optional[builtins.str]:
        '''The HCFS URI of the script that contains Hive queries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_file_uri GoogleDataprocWorkflowTemplate#query_file_uri}
        '''
        result = self._values.get("query_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_list(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsHiveJobQueryList"]:
        '''query_list block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_list GoogleDataprocWorkflowTemplate#query_list}
        '''
        result = self._values.get("query_list")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsHiveJobQueryList"], result)

    @builtins.property
    def script_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional. Mapping of query variable names to values (equivalent to the Hive command: ``SET name="value";``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#script_variables GoogleDataprocWorkflowTemplate#script_variables}
        '''
        result = self._values.get("script_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsHiveJob(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateJobsHiveJobOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsHiveJobOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsHiveJobOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putQueryList")
    def put_query_list(self, *, queries: typing.Sequence[builtins.str]) -> None:
        '''
        :param queries: Required. The queries to execute. You do not need to end a query expression with a semicolon. Multiple queries can be specified in one string by separating each with a semicolon. Here is an example of a Dataproc API snippet that uses a QueryList to specify a HiveJob: "hiveJob": { "queryList": { "queries": [ "query1", "query2", "query3;query4", ] } } Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#queries GoogleDataprocWorkflowTemplate#queries}
        '''
        value = GoogleDataprocWorkflowTemplateJobsHiveJobQueryList(queries=queries)

        return typing.cast(None, jsii.invoke(self, "putQueryList", [value]))

    @jsii.member(jsii_name="resetContinueOnFailure")
    def reset_continue_on_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContinueOnFailure", []))

    @jsii.member(jsii_name="resetJarFileUris")
    def reset_jar_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJarFileUris", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetQueryFileUri")
    def reset_query_file_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryFileUri", []))

    @jsii.member(jsii_name="resetQueryList")
    def reset_query_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryList", []))

    @jsii.member(jsii_name="resetScriptVariables")
    def reset_script_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScriptVariables", []))

    @builtins.property
    @jsii.member(jsii_name="queryList")
    def query_list(
        self,
    ) -> "GoogleDataprocWorkflowTemplateJobsHiveJobQueryListOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplateJobsHiveJobQueryListOutputReference", jsii.get(self, "queryList"))

    @builtins.property
    @jsii.member(jsii_name="continueOnFailureInput")
    def continue_on_failure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "continueOnFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="jarFileUrisInput")
    def jar_file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jarFileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="queryFileUriInput")
    def query_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="queryListInput")
    def query_list_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsHiveJobQueryList"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsHiveJobQueryList"], jsii.get(self, "queryListInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptVariablesInput")
    def script_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "scriptVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="continueOnFailure")
    def continue_on_failure(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "continueOnFailure"))

    @continue_on_failure.setter
    def continue_on_failure(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHiveJobOutputReference, "continue_on_failure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "continueOnFailure", value)

    @builtins.property
    @jsii.member(jsii_name="jarFileUris")
    def jar_file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jarFileUris"))

    @jar_file_uris.setter
    def jar_file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHiveJobOutputReference, "jar_file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jarFileUris", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHiveJobOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="queryFileUri")
    def query_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryFileUri"))

    @query_file_uri.setter
    def query_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHiveJobOutputReference, "query_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="scriptVariables")
    def script_variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "scriptVariables"))

    @script_variables.setter
    def script_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHiveJobOutputReference, "script_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scriptVariables", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsHiveJob]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsHiveJob], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsHiveJob],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHiveJobOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsHiveJobQueryList",
    jsii_struct_bases=[],
    name_mapping={"queries": "queries"},
)
class GoogleDataprocWorkflowTemplateJobsHiveJobQueryList:
    def __init__(self, *, queries: typing.Sequence[builtins.str]) -> None:
        '''
        :param queries: Required. The queries to execute. You do not need to end a query expression with a semicolon. Multiple queries can be specified in one string by separating each with a semicolon. Here is an example of a Dataproc API snippet that uses a QueryList to specify a HiveJob: "hiveJob": { "queryList": { "queries": [ "query1", "query2", "query3;query4", ] } } Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#queries GoogleDataprocWorkflowTemplate#queries}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsHiveJobQueryList.__init__)
            check_type(argname="argument queries", value=queries, expected_type=type_hints["queries"])
        self._values: typing.Dict[str, typing.Any] = {
            "queries": queries,
        }

    @builtins.property
    def queries(self) -> typing.List[builtins.str]:
        '''Required.

        The queries to execute. You do not need to end a query expression with a semicolon. Multiple queries can be specified in one string by separating each with a semicolon. Here is an example of a Dataproc API snippet that uses a QueryList to specify a HiveJob: "hiveJob": { "queryList": { "queries": [ "query1", "query2", "query3;query4", ] } }

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#queries GoogleDataprocWorkflowTemplate#queries}
        '''
        result = self._values.get("queries")
        assert result is not None, "Required property 'queries' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsHiveJobQueryList(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateJobsHiveJobQueryListOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsHiveJobQueryListOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsHiveJobQueryListOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="queriesInput")
    def queries_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queriesInput"))

    @builtins.property
    @jsii.member(jsii_name="queries")
    def queries(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queries"))

    @queries.setter
    def queries(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHiveJobQueryListOutputReference, "queries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queries", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsHiveJobQueryList]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsHiveJobQueryList], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsHiveJobQueryList],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsHiveJobQueryListOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplateJobsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsList",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDataprocWorkflowTemplateJobsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDataprocWorkflowTemplateJobsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplateJobs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplateJobs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplateJobs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplateJobsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHadoopJob")
    def put_hadoop_job(
        self,
        *,
        archive_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig, typing.Dict[str, typing.Any]]] = None,
        main_class: typing.Optional[builtins.str] = None,
        main_jar_file_uri: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param archive_uris: Optional. HCFS URIs of archives to be extracted in the working directory of Hadoop drivers and tasks. Supported file types: .jar, .tar, .tar.gz, .tgz, or .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#archive_uris GoogleDataprocWorkflowTemplate#archive_uris}
        :param args: Optional. The arguments to pass to the driver. Do not include arguments, such as ``-libjars`` or ``-Dfoo=bar``, that can be set as job properties, since a collision may occur that causes an incorrect job submission. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#args GoogleDataprocWorkflowTemplate#args}
        :param file_uris: Optional. HCFS (Hadoop Compatible Filesystem) URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#file_uris GoogleDataprocWorkflowTemplate#file_uris}
        :param jar_file_uris: Optional. Jar file URIs to add to the CLASSPATHs of the Hadoop driver and tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        :param main_class: The name of the driver's main class. The jar file containing the class must be in the default CLASSPATH or specified in ``jar_file_uris``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_class GoogleDataprocWorkflowTemplate#main_class}
        :param main_jar_file_uri: The HCFS URI of the jar file containing the main class. Examples: 'gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar' 'hdfs:/tmp/test-samples/custom-wordcount.jar' 'file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_jar_file_uri GoogleDataprocWorkflowTemplate#main_jar_file_uri}
        :param properties: Optional. A mapping of property names to values, used to configure Hadoop. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/hadoop/conf/*-site and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        value = GoogleDataprocWorkflowTemplateJobsHadoopJob(
            archive_uris=archive_uris,
            args=args,
            file_uris=file_uris,
            jar_file_uris=jar_file_uris,
            logging_config=logging_config,
            main_class=main_class,
            main_jar_file_uri=main_jar_file_uri,
            properties=properties,
        )

        return typing.cast(None, jsii.invoke(self, "putHadoopJob", [value]))

    @jsii.member(jsii_name="putHiveJob")
    def put_hive_job(
        self,
        *,
        continue_on_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplateJobsHiveJobQueryList, typing.Dict[str, typing.Any]]] = None,
        script_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param continue_on_failure: Optional. Whether to continue executing queries if a query fails. The default value is ``false``. Setting to ``true`` can be useful when executing independent parallel queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#continue_on_failure GoogleDataprocWorkflowTemplate#continue_on_failure}
        :param jar_file_uris: Optional. HCFS URIs of jar files to add to the CLASSPATH of the Hive server and Hadoop MapReduce (MR) tasks. Can contain Hive SerDes and UDFs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        :param properties: Optional. A mapping of property names and values, used to configure Hive. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/hadoop/conf/*-site.xml, /etc/hive/conf/hive-site.xml, and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        :param query_file_uri: The HCFS URI of the script that contains Hive queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_file_uri GoogleDataprocWorkflowTemplate#query_file_uri}
        :param query_list: query_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_list GoogleDataprocWorkflowTemplate#query_list}
        :param script_variables: Optional. Mapping of query variable names to values (equivalent to the Hive command: ``SET name="value";``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#script_variables GoogleDataprocWorkflowTemplate#script_variables}
        '''
        value = GoogleDataprocWorkflowTemplateJobsHiveJob(
            continue_on_failure=continue_on_failure,
            jar_file_uris=jar_file_uris,
            properties=properties,
            query_file_uri=query_file_uri,
            query_list=query_list,
            script_variables=script_variables,
        )

        return typing.cast(None, jsii.invoke(self, "putHiveJob", [value]))

    @jsii.member(jsii_name="putPigJob")
    def put_pig_job(
        self,
        *,
        continue_on_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsPigJobQueryList", typing.Dict[str, typing.Any]]] = None,
        script_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param continue_on_failure: Optional. Whether to continue executing queries if a query fails. The default value is ``false``. Setting to ``true`` can be useful when executing independent parallel queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#continue_on_failure GoogleDataprocWorkflowTemplate#continue_on_failure}
        :param jar_file_uris: Optional. HCFS URIs of jar files to add to the CLASSPATH of the Pig Client and Hadoop MapReduce (MR) tasks. Can contain Pig UDFs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        :param properties: Optional. A mapping of property names to values, used to configure Pig. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/hadoop/conf/*-site.xml, /etc/pig/conf/pig.properties, and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        :param query_file_uri: The HCFS URI of the script that contains the Pig queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_file_uri GoogleDataprocWorkflowTemplate#query_file_uri}
        :param query_list: query_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_list GoogleDataprocWorkflowTemplate#query_list}
        :param script_variables: Optional. Mapping of query variable names to values (equivalent to the Pig command: ``name=[value]``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#script_variables GoogleDataprocWorkflowTemplate#script_variables}
        '''
        value = GoogleDataprocWorkflowTemplateJobsPigJob(
            continue_on_failure=continue_on_failure,
            jar_file_uris=jar_file_uris,
            logging_config=logging_config,
            properties=properties,
            query_file_uri=query_file_uri,
            query_list=query_list,
            script_variables=script_variables,
        )

        return typing.cast(None, jsii.invoke(self, "putPigJob", [value]))

    @jsii.member(jsii_name="putPrestoJob")
    def put_presto_job(
        self,
        *,
        client_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        continue_on_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        output_format: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_tags: Optional. Presto client tags to attach to this query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#client_tags GoogleDataprocWorkflowTemplate#client_tags}
        :param continue_on_failure: Optional. Whether to continue executing queries if a query fails. The default value is ``false``. Setting to ``true`` can be useful when executing independent parallel queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#continue_on_failure GoogleDataprocWorkflowTemplate#continue_on_failure}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        :param output_format: Optional. The format in which query output will be displayed. See the Presto documentation for supported output formats. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#output_format GoogleDataprocWorkflowTemplate#output_format}
        :param properties: Optional. A mapping of property names to values. Used to set Presto `session properties <https://prestodb.io/docs/current/sql/set-session.html>`_ Equivalent to using the --session flag in the Presto CLI Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        :param query_file_uri: The HCFS URI of the script that contains SQL queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_file_uri GoogleDataprocWorkflowTemplate#query_file_uri}
        :param query_list: query_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_list GoogleDataprocWorkflowTemplate#query_list}
        '''
        value = GoogleDataprocWorkflowTemplateJobsPrestoJob(
            client_tags=client_tags,
            continue_on_failure=continue_on_failure,
            logging_config=logging_config,
            output_format=output_format,
            properties=properties,
            query_file_uri=query_file_uri,
            query_list=query_list,
        )

        return typing.cast(None, jsii.invoke(self, "putPrestoJob", [value]))

    @jsii.member(jsii_name="putPysparkJob")
    def put_pyspark_job(
        self,
        *,
        main_python_file_uri: builtins.str,
        archive_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        python_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param main_python_file_uri: Required. The HCFS URI of the main Python file to use as the driver. Must be a .py file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_python_file_uri GoogleDataprocWorkflowTemplate#main_python_file_uri}
        :param archive_uris: Optional. HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#archive_uris GoogleDataprocWorkflowTemplate#archive_uris}
        :param args: Optional. The arguments to pass to the driver. Do not include arguments, such as ``--conf``, that can be set as job properties, since a collision may occur that causes an incorrect job submission. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#args GoogleDataprocWorkflowTemplate#args}
        :param file_uris: Optional. HCFS URIs of files to be placed in the working directory of each executor. Useful for naively parallel tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#file_uris GoogleDataprocWorkflowTemplate#file_uris}
        :param jar_file_uris: Optional. HCFS URIs of jar files to add to the CLASSPATHs of the Python driver and tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        :param properties: Optional. A mapping of property names to values, used to configure PySpark. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        :param python_file_uris: Optional. HCFS file URIs of Python files to pass to the PySpark framework. Supported file types: .py, .egg, and .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#python_file_uris GoogleDataprocWorkflowTemplate#python_file_uris}
        '''
        value = GoogleDataprocWorkflowTemplateJobsPysparkJob(
            main_python_file_uri=main_python_file_uri,
            archive_uris=archive_uris,
            args=args,
            file_uris=file_uris,
            jar_file_uris=jar_file_uris,
            logging_config=logging_config,
            properties=properties,
            python_file_uris=python_file_uris,
        )

        return typing.cast(None, jsii.invoke(self, "putPysparkJob", [value]))

    @jsii.member(jsii_name="putScheduling")
    def put_scheduling(
        self,
        *,
        max_failures_per_hour: typing.Optional[jsii.Number] = None,
        max_failures_total: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_failures_per_hour: Optional. Maximum number of times per hour a driver may be restarted as a result of driver exiting with non-zero code before job is reported failed. A job may be reported as thrashing if driver exits with non-zero code 4 times within 10 minute window. Maximum value is 10. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#max_failures_per_hour GoogleDataprocWorkflowTemplate#max_failures_per_hour}
        :param max_failures_total: Optional. Maximum number of times in total a driver may be restarted as a result of driver exiting with non-zero code before job is reported failed. Maximum value is 240. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#max_failures_total GoogleDataprocWorkflowTemplate#max_failures_total}
        '''
        value = GoogleDataprocWorkflowTemplateJobsScheduling(
            max_failures_per_hour=max_failures_per_hour,
            max_failures_total=max_failures_total,
        )

        return typing.cast(None, jsii.invoke(self, "putScheduling", [value]))

    @jsii.member(jsii_name="putSparkJob")
    def put_spark_job(
        self,
        *,
        archive_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        main_class: typing.Optional[builtins.str] = None,
        main_jar_file_uri: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param archive_uris: Optional. HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#archive_uris GoogleDataprocWorkflowTemplate#archive_uris}
        :param args: Optional. The arguments to pass to the driver. Do not include arguments, such as ``--conf``, that can be set as job properties, since a collision may occur that causes an incorrect job submission. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#args GoogleDataprocWorkflowTemplate#args}
        :param file_uris: Optional. HCFS URIs of files to be placed in the working directory of each executor. Useful for naively parallel tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#file_uris GoogleDataprocWorkflowTemplate#file_uris}
        :param jar_file_uris: Optional. HCFS URIs of jar files to add to the CLASSPATHs of the Spark driver and tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        :param main_class: The name of the driver's main class. The jar file that contains the class must be in the default CLASSPATH or specified in ``jar_file_uris``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_class GoogleDataprocWorkflowTemplate#main_class}
        :param main_jar_file_uri: The HCFS URI of the jar file that contains the main class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_jar_file_uri GoogleDataprocWorkflowTemplate#main_jar_file_uri}
        :param properties: Optional. A mapping of property names to values, used to configure Spark. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        value = GoogleDataprocWorkflowTemplateJobsSparkJob(
            archive_uris=archive_uris,
            args=args,
            file_uris=file_uris,
            jar_file_uris=jar_file_uris,
            logging_config=logging_config,
            main_class=main_class,
            main_jar_file_uri=main_jar_file_uri,
            properties=properties,
        )

        return typing.cast(None, jsii.invoke(self, "putSparkJob", [value]))

    @jsii.member(jsii_name="putSparkRJob")
    def put_spark_r_job(
        self,
        *,
        main_r_file_uri: builtins.str,
        archive_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param main_r_file_uri: Required. The HCFS URI of the main R file to use as the driver. Must be a .R file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_r_file_uri GoogleDataprocWorkflowTemplate#main_r_file_uri}
        :param archive_uris: Optional. HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#archive_uris GoogleDataprocWorkflowTemplate#archive_uris}
        :param args: Optional. The arguments to pass to the driver. Do not include arguments, such as ``--conf``, that can be set as job properties, since a collision may occur that causes an incorrect job submission. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#args GoogleDataprocWorkflowTemplate#args}
        :param file_uris: Optional. HCFS URIs of files to be placed in the working directory of each executor. Useful for naively parallel tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#file_uris GoogleDataprocWorkflowTemplate#file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        :param properties: Optional. A mapping of property names to values, used to configure SparkR. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        value = GoogleDataprocWorkflowTemplateJobsSparkRJob(
            main_r_file_uri=main_r_file_uri,
            archive_uris=archive_uris,
            args=args,
            file_uris=file_uris,
            logging_config=logging_config,
            properties=properties,
        )

        return typing.cast(None, jsii.invoke(self, "putSparkRJob", [value]))

    @jsii.member(jsii_name="putSparkSqlJob")
    def put_spark_sql_job(
        self,
        *,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList", typing.Dict[str, typing.Any]]] = None,
        script_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param jar_file_uris: Optional. HCFS URIs of jar files to be added to the Spark CLASSPATH. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        :param properties: Optional. A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Dataproc API may be overwritten. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        :param query_file_uri: The HCFS URI of the script that contains SQL queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_file_uri GoogleDataprocWorkflowTemplate#query_file_uri}
        :param query_list: query_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_list GoogleDataprocWorkflowTemplate#query_list}
        :param script_variables: Optional. Mapping of query variable names to values (equivalent to the Spark SQL command: SET ``name="value";``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#script_variables GoogleDataprocWorkflowTemplate#script_variables}
        '''
        value = GoogleDataprocWorkflowTemplateJobsSparkSqlJob(
            jar_file_uris=jar_file_uris,
            logging_config=logging_config,
            properties=properties,
            query_file_uri=query_file_uri,
            query_list=query_list,
            script_variables=script_variables,
        )

        return typing.cast(None, jsii.invoke(self, "putSparkSqlJob", [value]))

    @jsii.member(jsii_name="resetHadoopJob")
    def reset_hadoop_job(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHadoopJob", []))

    @jsii.member(jsii_name="resetHiveJob")
    def reset_hive_job(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHiveJob", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetPigJob")
    def reset_pig_job(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPigJob", []))

    @jsii.member(jsii_name="resetPrerequisiteStepIds")
    def reset_prerequisite_step_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrerequisiteStepIds", []))

    @jsii.member(jsii_name="resetPrestoJob")
    def reset_presto_job(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrestoJob", []))

    @jsii.member(jsii_name="resetPysparkJob")
    def reset_pyspark_job(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPysparkJob", []))

    @jsii.member(jsii_name="resetScheduling")
    def reset_scheduling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduling", []))

    @jsii.member(jsii_name="resetSparkJob")
    def reset_spark_job(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkJob", []))

    @jsii.member(jsii_name="resetSparkRJob")
    def reset_spark_r_job(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkRJob", []))

    @jsii.member(jsii_name="resetSparkSqlJob")
    def reset_spark_sql_job(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkSqlJob", []))

    @builtins.property
    @jsii.member(jsii_name="hadoopJob")
    def hadoop_job(self) -> GoogleDataprocWorkflowTemplateJobsHadoopJobOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplateJobsHadoopJobOutputReference, jsii.get(self, "hadoopJob"))

    @builtins.property
    @jsii.member(jsii_name="hiveJob")
    def hive_job(self) -> GoogleDataprocWorkflowTemplateJobsHiveJobOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplateJobsHiveJobOutputReference, jsii.get(self, "hiveJob"))

    @builtins.property
    @jsii.member(jsii_name="pigJob")
    def pig_job(self) -> "GoogleDataprocWorkflowTemplateJobsPigJobOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplateJobsPigJobOutputReference", jsii.get(self, "pigJob"))

    @builtins.property
    @jsii.member(jsii_name="prestoJob")
    def presto_job(
        self,
    ) -> "GoogleDataprocWorkflowTemplateJobsPrestoJobOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplateJobsPrestoJobOutputReference", jsii.get(self, "prestoJob"))

    @builtins.property
    @jsii.member(jsii_name="pysparkJob")
    def pyspark_job(
        self,
    ) -> "GoogleDataprocWorkflowTemplateJobsPysparkJobOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplateJobsPysparkJobOutputReference", jsii.get(self, "pysparkJob"))

    @builtins.property
    @jsii.member(jsii_name="scheduling")
    def scheduling(
        self,
    ) -> "GoogleDataprocWorkflowTemplateJobsSchedulingOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplateJobsSchedulingOutputReference", jsii.get(self, "scheduling"))

    @builtins.property
    @jsii.member(jsii_name="sparkJob")
    def spark_job(self) -> "GoogleDataprocWorkflowTemplateJobsSparkJobOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplateJobsSparkJobOutputReference", jsii.get(self, "sparkJob"))

    @builtins.property
    @jsii.member(jsii_name="sparkRJob")
    def spark_r_job(
        self,
    ) -> "GoogleDataprocWorkflowTemplateJobsSparkRJobOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplateJobsSparkRJobOutputReference", jsii.get(self, "sparkRJob"))

    @builtins.property
    @jsii.member(jsii_name="sparkSqlJob")
    def spark_sql_job(
        self,
    ) -> "GoogleDataprocWorkflowTemplateJobsSparkSqlJobOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplateJobsSparkSqlJobOutputReference", jsii.get(self, "sparkSqlJob"))

    @builtins.property
    @jsii.member(jsii_name="hadoopJobInput")
    def hadoop_job_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsHadoopJob]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsHadoopJob], jsii.get(self, "hadoopJobInput"))

    @builtins.property
    @jsii.member(jsii_name="hiveJobInput")
    def hive_job_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsHiveJob]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsHiveJob], jsii.get(self, "hiveJobInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="pigJobInput")
    def pig_job_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsPigJob"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsPigJob"], jsii.get(self, "pigJobInput"))

    @builtins.property
    @jsii.member(jsii_name="prerequisiteStepIdsInput")
    def prerequisite_step_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "prerequisiteStepIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="prestoJobInput")
    def presto_job_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsPrestoJob"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsPrestoJob"], jsii.get(self, "prestoJobInput"))

    @builtins.property
    @jsii.member(jsii_name="pysparkJobInput")
    def pyspark_job_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsPysparkJob"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsPysparkJob"], jsii.get(self, "pysparkJobInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulingInput")
    def scheduling_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsScheduling"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsScheduling"], jsii.get(self, "schedulingInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkJobInput")
    def spark_job_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkJob"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkJob"], jsii.get(self, "sparkJobInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkRJobInput")
    def spark_r_job_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkRJob"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkRJob"], jsii.get(self, "sparkRJobInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkSqlJobInput")
    def spark_sql_job_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkSqlJob"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkSqlJob"], jsii.get(self, "sparkSqlJobInput"))

    @builtins.property
    @jsii.member(jsii_name="stepIdInput")
    def step_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stepIdInput"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="prerequisiteStepIds")
    def prerequisite_step_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "prerequisiteStepIds"))

    @prerequisite_step_ids.setter
    def prerequisite_step_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsOutputReference, "prerequisite_step_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prerequisiteStepIds", value)

    @builtins.property
    @jsii.member(jsii_name="stepId")
    def step_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stepId"))

    @step_id.setter
    def step_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsOutputReference, "step_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stepId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataprocWorkflowTemplateJobs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataprocWorkflowTemplateJobs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplateJobs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPigJob",
    jsii_struct_bases=[],
    name_mapping={
        "continue_on_failure": "continueOnFailure",
        "jar_file_uris": "jarFileUris",
        "logging_config": "loggingConfig",
        "properties": "properties",
        "query_file_uri": "queryFileUri",
        "query_list": "queryList",
        "script_variables": "scriptVariables",
    },
)
class GoogleDataprocWorkflowTemplateJobsPigJob:
    def __init__(
        self,
        *,
        continue_on_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsPigJobQueryList", typing.Dict[str, typing.Any]]] = None,
        script_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param continue_on_failure: Optional. Whether to continue executing queries if a query fails. The default value is ``false``. Setting to ``true`` can be useful when executing independent parallel queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#continue_on_failure GoogleDataprocWorkflowTemplate#continue_on_failure}
        :param jar_file_uris: Optional. HCFS URIs of jar files to add to the CLASSPATH of the Pig Client and Hadoop MapReduce (MR) tasks. Can contain Pig UDFs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        :param properties: Optional. A mapping of property names to values, used to configure Pig. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/hadoop/conf/*-site.xml, /etc/pig/conf/pig.properties, and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        :param query_file_uri: The HCFS URI of the script that contains the Pig queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_file_uri GoogleDataprocWorkflowTemplate#query_file_uri}
        :param query_list: query_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_list GoogleDataprocWorkflowTemplate#query_list}
        :param script_variables: Optional. Mapping of query variable names to values (equivalent to the Pig command: ``name=[value]``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#script_variables GoogleDataprocWorkflowTemplate#script_variables}
        '''
        if isinstance(logging_config, dict):
            logging_config = GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig(**logging_config)
        if isinstance(query_list, dict):
            query_list = GoogleDataprocWorkflowTemplateJobsPigJobQueryList(**query_list)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPigJob.__init__)
            check_type(argname="argument continue_on_failure", value=continue_on_failure, expected_type=type_hints["continue_on_failure"])
            check_type(argname="argument jar_file_uris", value=jar_file_uris, expected_type=type_hints["jar_file_uris"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument query_file_uri", value=query_file_uri, expected_type=type_hints["query_file_uri"])
            check_type(argname="argument query_list", value=query_list, expected_type=type_hints["query_list"])
            check_type(argname="argument script_variables", value=script_variables, expected_type=type_hints["script_variables"])
        self._values: typing.Dict[str, typing.Any] = {}
        if continue_on_failure is not None:
            self._values["continue_on_failure"] = continue_on_failure
        if jar_file_uris is not None:
            self._values["jar_file_uris"] = jar_file_uris
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if properties is not None:
            self._values["properties"] = properties
        if query_file_uri is not None:
            self._values["query_file_uri"] = query_file_uri
        if query_list is not None:
            self._values["query_list"] = query_list
        if script_variables is not None:
            self._values["script_variables"] = script_variables

    @builtins.property
    def continue_on_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional.

        Whether to continue executing queries if a query fails. The default value is ``false``. Setting to ``true`` can be useful when executing independent parallel queries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#continue_on_failure GoogleDataprocWorkflowTemplate#continue_on_failure}
        '''
        result = self._values.get("continue_on_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def jar_file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        HCFS URIs of jar files to add to the CLASSPATH of the Pig Client and Hadoop MapReduce (MR) tasks. Can contain Pig UDFs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        '''
        result = self._values.get("jar_file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig"]:
        '''logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig"], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        A mapping of property names to values, used to configure Pig. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/hadoop/conf/*-site.xml, /etc/pig/conf/pig.properties, and classes in user code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def query_file_uri(self) -> typing.Optional[builtins.str]:
        '''The HCFS URI of the script that contains the Pig queries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_file_uri GoogleDataprocWorkflowTemplate#query_file_uri}
        '''
        result = self._values.get("query_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_list(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsPigJobQueryList"]:
        '''query_list block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_list GoogleDataprocWorkflowTemplate#query_list}
        '''
        result = self._values.get("query_list")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsPigJobQueryList"], result)

    @builtins.property
    def script_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional. Mapping of query variable names to values (equivalent to the Pig command: ``name=[value]``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#script_variables GoogleDataprocWorkflowTemplate#script_variables}
        '''
        result = self._values.get("script_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsPigJob(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={"driver_log_levels": "driverLogLevels"},
)
class GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig:
    def __init__(
        self,
        *,
        driver_log_levels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver_log_levels: The per-package log levels for the driver. This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig.__init__)
            check_type(argname="argument driver_log_levels", value=driver_log_levels, expected_type=type_hints["driver_log_levels"])
        self._values: typing.Dict[str, typing.Any] = {}
        if driver_log_levels is not None:
            self._values["driver_log_levels"] = driver_log_levels

    @builtins.property
    def driver_log_levels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The per-package log levels for the driver.

        This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        result = self._values.get("driver_log_levels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDriverLogLevels")
    def reset_driver_log_levels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverLogLevels", []))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevelsInput")
    def driver_log_levels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverLogLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevels")
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverLogLevels"))

    @driver_log_levels.setter
    def driver_log_levels(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfigOutputReference, "driver_log_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverLogLevels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplateJobsPigJobOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPigJobOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPigJobOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLoggingConfig")
    def put_logging_config(
        self,
        *,
        driver_log_levels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver_log_levels: The per-package log levels for the driver. This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        value = GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig(
            driver_log_levels=driver_log_levels
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfig", [value]))

    @jsii.member(jsii_name="putQueryList")
    def put_query_list(self, *, queries: typing.Sequence[builtins.str]) -> None:
        '''
        :param queries: Required. The queries to execute. You do not need to end a query expression with a semicolon. Multiple queries can be specified in one string by separating each with a semicolon. Here is an example of a Dataproc API snippet that uses a QueryList to specify a HiveJob: "hiveJob": { "queryList": { "queries": [ "query1", "query2", "query3;query4", ] } } Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#queries GoogleDataprocWorkflowTemplate#queries}
        '''
        value = GoogleDataprocWorkflowTemplateJobsPigJobQueryList(queries=queries)

        return typing.cast(None, jsii.invoke(self, "putQueryList", [value]))

    @jsii.member(jsii_name="resetContinueOnFailure")
    def reset_continue_on_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContinueOnFailure", []))

    @jsii.member(jsii_name="resetJarFileUris")
    def reset_jar_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJarFileUris", []))

    @jsii.member(jsii_name="resetLoggingConfig")
    def reset_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfig", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetQueryFileUri")
    def reset_query_file_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryFileUri", []))

    @jsii.member(jsii_name="resetQueryList")
    def reset_query_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryList", []))

    @jsii.member(jsii_name="resetScriptVariables")
    def reset_script_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScriptVariables", []))

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfigOutputReference, jsii.get(self, "loggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="queryList")
    def query_list(
        self,
    ) -> "GoogleDataprocWorkflowTemplateJobsPigJobQueryListOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplateJobsPigJobQueryListOutputReference", jsii.get(self, "queryList"))

    @builtins.property
    @jsii.member(jsii_name="continueOnFailureInput")
    def continue_on_failure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "continueOnFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="jarFileUrisInput")
    def jar_file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jarFileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigInput")
    def logging_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig], jsii.get(self, "loggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="queryFileUriInput")
    def query_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="queryListInput")
    def query_list_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsPigJobQueryList"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsPigJobQueryList"], jsii.get(self, "queryListInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptVariablesInput")
    def script_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "scriptVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="continueOnFailure")
    def continue_on_failure(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "continueOnFailure"))

    @continue_on_failure.setter
    def continue_on_failure(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPigJobOutputReference, "continue_on_failure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "continueOnFailure", value)

    @builtins.property
    @jsii.member(jsii_name="jarFileUris")
    def jar_file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jarFileUris"))

    @jar_file_uris.setter
    def jar_file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPigJobOutputReference, "jar_file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jarFileUris", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPigJobOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="queryFileUri")
    def query_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryFileUri"))

    @query_file_uri.setter
    def query_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPigJobOutputReference, "query_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="scriptVariables")
    def script_variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "scriptVariables"))

    @script_variables.setter
    def script_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPigJobOutputReference, "script_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scriptVariables", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsPigJob]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsPigJob], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsPigJob],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPigJobOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPigJobQueryList",
    jsii_struct_bases=[],
    name_mapping={"queries": "queries"},
)
class GoogleDataprocWorkflowTemplateJobsPigJobQueryList:
    def __init__(self, *, queries: typing.Sequence[builtins.str]) -> None:
        '''
        :param queries: Required. The queries to execute. You do not need to end a query expression with a semicolon. Multiple queries can be specified in one string by separating each with a semicolon. Here is an example of a Dataproc API snippet that uses a QueryList to specify a HiveJob: "hiveJob": { "queryList": { "queries": [ "query1", "query2", "query3;query4", ] } } Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#queries GoogleDataprocWorkflowTemplate#queries}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPigJobQueryList.__init__)
            check_type(argname="argument queries", value=queries, expected_type=type_hints["queries"])
        self._values: typing.Dict[str, typing.Any] = {
            "queries": queries,
        }

    @builtins.property
    def queries(self) -> typing.List[builtins.str]:
        '''Required.

        The queries to execute. You do not need to end a query expression with a semicolon. Multiple queries can be specified in one string by separating each with a semicolon. Here is an example of a Dataproc API snippet that uses a QueryList to specify a HiveJob: "hiveJob": { "queryList": { "queries": [ "query1", "query2", "query3;query4", ] } }

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#queries GoogleDataprocWorkflowTemplate#queries}
        '''
        result = self._values.get("queries")
        assert result is not None, "Required property 'queries' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsPigJobQueryList(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateJobsPigJobQueryListOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPigJobQueryListOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPigJobQueryListOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="queriesInput")
    def queries_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queriesInput"))

    @builtins.property
    @jsii.member(jsii_name="queries")
    def queries(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queries"))

    @queries.setter
    def queries(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPigJobQueryListOutputReference, "queries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queries", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsPigJobQueryList]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsPigJobQueryList], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsPigJobQueryList],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPigJobQueryListOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPrestoJob",
    jsii_struct_bases=[],
    name_mapping={
        "client_tags": "clientTags",
        "continue_on_failure": "continueOnFailure",
        "logging_config": "loggingConfig",
        "output_format": "outputFormat",
        "properties": "properties",
        "query_file_uri": "queryFileUri",
        "query_list": "queryList",
    },
)
class GoogleDataprocWorkflowTemplateJobsPrestoJob:
    def __init__(
        self,
        *,
        client_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        continue_on_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        output_format: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_tags: Optional. Presto client tags to attach to this query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#client_tags GoogleDataprocWorkflowTemplate#client_tags}
        :param continue_on_failure: Optional. Whether to continue executing queries if a query fails. The default value is ``false``. Setting to ``true`` can be useful when executing independent parallel queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#continue_on_failure GoogleDataprocWorkflowTemplate#continue_on_failure}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        :param output_format: Optional. The format in which query output will be displayed. See the Presto documentation for supported output formats. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#output_format GoogleDataprocWorkflowTemplate#output_format}
        :param properties: Optional. A mapping of property names to values. Used to set Presto `session properties <https://prestodb.io/docs/current/sql/set-session.html>`_ Equivalent to using the --session flag in the Presto CLI Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        :param query_file_uri: The HCFS URI of the script that contains SQL queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_file_uri GoogleDataprocWorkflowTemplate#query_file_uri}
        :param query_list: query_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_list GoogleDataprocWorkflowTemplate#query_list}
        '''
        if isinstance(logging_config, dict):
            logging_config = GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig(**logging_config)
        if isinstance(query_list, dict):
            query_list = GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList(**query_list)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPrestoJob.__init__)
            check_type(argname="argument client_tags", value=client_tags, expected_type=type_hints["client_tags"])
            check_type(argname="argument continue_on_failure", value=continue_on_failure, expected_type=type_hints["continue_on_failure"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument output_format", value=output_format, expected_type=type_hints["output_format"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument query_file_uri", value=query_file_uri, expected_type=type_hints["query_file_uri"])
            check_type(argname="argument query_list", value=query_list, expected_type=type_hints["query_list"])
        self._values: typing.Dict[str, typing.Any] = {}
        if client_tags is not None:
            self._values["client_tags"] = client_tags
        if continue_on_failure is not None:
            self._values["continue_on_failure"] = continue_on_failure
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if output_format is not None:
            self._values["output_format"] = output_format
        if properties is not None:
            self._values["properties"] = properties
        if query_file_uri is not None:
            self._values["query_file_uri"] = query_file_uri
        if query_list is not None:
            self._values["query_list"] = query_list

    @builtins.property
    def client_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional. Presto client tags to attach to this query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#client_tags GoogleDataprocWorkflowTemplate#client_tags}
        '''
        result = self._values.get("client_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def continue_on_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional.

        Whether to continue executing queries if a query fails. The default value is ``false``. Setting to ``true`` can be useful when executing independent parallel queries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#continue_on_failure GoogleDataprocWorkflowTemplate#continue_on_failure}
        '''
        result = self._values.get("continue_on_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig"]:
        '''logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig"], result)

    @builtins.property
    def output_format(self) -> typing.Optional[builtins.str]:
        '''Optional. The format in which query output will be displayed. See the Presto documentation for supported output formats.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#output_format GoogleDataprocWorkflowTemplate#output_format}
        '''
        result = self._values.get("output_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        A mapping of property names to values. Used to set Presto `session properties <https://prestodb.io/docs/current/sql/set-session.html>`_ Equivalent to using the --session flag in the Presto CLI

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def query_file_uri(self) -> typing.Optional[builtins.str]:
        '''The HCFS URI of the script that contains SQL queries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_file_uri GoogleDataprocWorkflowTemplate#query_file_uri}
        '''
        result = self._values.get("query_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_list(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList"]:
        '''query_list block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_list GoogleDataprocWorkflowTemplate#query_list}
        '''
        result = self._values.get("query_list")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsPrestoJob(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={"driver_log_levels": "driverLogLevels"},
)
class GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig:
    def __init__(
        self,
        *,
        driver_log_levels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver_log_levels: The per-package log levels for the driver. This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig.__init__)
            check_type(argname="argument driver_log_levels", value=driver_log_levels, expected_type=type_hints["driver_log_levels"])
        self._values: typing.Dict[str, typing.Any] = {}
        if driver_log_levels is not None:
            self._values["driver_log_levels"] = driver_log_levels

    @builtins.property
    def driver_log_levels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The per-package log levels for the driver.

        This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        result = self._values.get("driver_log_levels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDriverLogLevels")
    def reset_driver_log_levels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverLogLevels", []))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevelsInput")
    def driver_log_levels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverLogLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevels")
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverLogLevels"))

    @driver_log_levels.setter
    def driver_log_levels(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfigOutputReference, "driver_log_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverLogLevels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplateJobsPrestoJobOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPrestoJobOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPrestoJobOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLoggingConfig")
    def put_logging_config(
        self,
        *,
        driver_log_levels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver_log_levels: The per-package log levels for the driver. This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        value = GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig(
            driver_log_levels=driver_log_levels
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfig", [value]))

    @jsii.member(jsii_name="putQueryList")
    def put_query_list(self, *, queries: typing.Sequence[builtins.str]) -> None:
        '''
        :param queries: Required. The queries to execute. You do not need to end a query expression with a semicolon. Multiple queries can be specified in one string by separating each with a semicolon. Here is an example of a Dataproc API snippet that uses a QueryList to specify a HiveJob: "hiveJob": { "queryList": { "queries": [ "query1", "query2", "query3;query4", ] } } Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#queries GoogleDataprocWorkflowTemplate#queries}
        '''
        value = GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList(queries=queries)

        return typing.cast(None, jsii.invoke(self, "putQueryList", [value]))

    @jsii.member(jsii_name="resetClientTags")
    def reset_client_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientTags", []))

    @jsii.member(jsii_name="resetContinueOnFailure")
    def reset_continue_on_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContinueOnFailure", []))

    @jsii.member(jsii_name="resetLoggingConfig")
    def reset_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfig", []))

    @jsii.member(jsii_name="resetOutputFormat")
    def reset_output_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputFormat", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetQueryFileUri")
    def reset_query_file_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryFileUri", []))

    @jsii.member(jsii_name="resetQueryList")
    def reset_query_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryList", []))

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfigOutputReference, jsii.get(self, "loggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="queryList")
    def query_list(
        self,
    ) -> "GoogleDataprocWorkflowTemplateJobsPrestoJobQueryListOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplateJobsPrestoJobQueryListOutputReference", jsii.get(self, "queryList"))

    @builtins.property
    @jsii.member(jsii_name="clientTagsInput")
    def client_tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clientTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="continueOnFailureInput")
    def continue_on_failure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "continueOnFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigInput")
    def logging_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig], jsii.get(self, "loggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="outputFormatInput")
    def output_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="queryFileUriInput")
    def query_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="queryListInput")
    def query_list_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList"], jsii.get(self, "queryListInput"))

    @builtins.property
    @jsii.member(jsii_name="clientTags")
    def client_tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "clientTags"))

    @client_tags.setter
    def client_tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPrestoJobOutputReference, "client_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientTags", value)

    @builtins.property
    @jsii.member(jsii_name="continueOnFailure")
    def continue_on_failure(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "continueOnFailure"))

    @continue_on_failure.setter
    def continue_on_failure(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPrestoJobOutputReference, "continue_on_failure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "continueOnFailure", value)

    @builtins.property
    @jsii.member(jsii_name="outputFormat")
    def output_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputFormat"))

    @output_format.setter
    def output_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPrestoJobOutputReference, "output_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputFormat", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPrestoJobOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="queryFileUri")
    def query_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryFileUri"))

    @query_file_uri.setter
    def query_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPrestoJobOutputReference, "query_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsPrestoJob]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsPrestoJob], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsPrestoJob],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPrestoJobOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList",
    jsii_struct_bases=[],
    name_mapping={"queries": "queries"},
)
class GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList:
    def __init__(self, *, queries: typing.Sequence[builtins.str]) -> None:
        '''
        :param queries: Required. The queries to execute. You do not need to end a query expression with a semicolon. Multiple queries can be specified in one string by separating each with a semicolon. Here is an example of a Dataproc API snippet that uses a QueryList to specify a HiveJob: "hiveJob": { "queryList": { "queries": [ "query1", "query2", "query3;query4", ] } } Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#queries GoogleDataprocWorkflowTemplate#queries}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList.__init__)
            check_type(argname="argument queries", value=queries, expected_type=type_hints["queries"])
        self._values: typing.Dict[str, typing.Any] = {
            "queries": queries,
        }

    @builtins.property
    def queries(self) -> typing.List[builtins.str]:
        '''Required.

        The queries to execute. You do not need to end a query expression with a semicolon. Multiple queries can be specified in one string by separating each with a semicolon. Here is an example of a Dataproc API snippet that uses a QueryList to specify a HiveJob: "hiveJob": { "queryList": { "queries": [ "query1", "query2", "query3;query4", ] } }

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#queries GoogleDataprocWorkflowTemplate#queries}
        '''
        result = self._values.get("queries")
        assert result is not None, "Required property 'queries' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateJobsPrestoJobQueryListOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPrestoJobQueryListOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPrestoJobQueryListOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="queriesInput")
    def queries_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queriesInput"))

    @builtins.property
    @jsii.member(jsii_name="queries")
    def queries(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queries"))

    @queries.setter
    def queries(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPrestoJobQueryListOutputReference, "queries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queries", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPrestoJobQueryListOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPysparkJob",
    jsii_struct_bases=[],
    name_mapping={
        "main_python_file_uri": "mainPythonFileUri",
        "archive_uris": "archiveUris",
        "args": "args",
        "file_uris": "fileUris",
        "jar_file_uris": "jarFileUris",
        "logging_config": "loggingConfig",
        "properties": "properties",
        "python_file_uris": "pythonFileUris",
    },
)
class GoogleDataprocWorkflowTemplateJobsPysparkJob:
    def __init__(
        self,
        *,
        main_python_file_uri: builtins.str,
        archive_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        python_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param main_python_file_uri: Required. The HCFS URI of the main Python file to use as the driver. Must be a .py file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_python_file_uri GoogleDataprocWorkflowTemplate#main_python_file_uri}
        :param archive_uris: Optional. HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#archive_uris GoogleDataprocWorkflowTemplate#archive_uris}
        :param args: Optional. The arguments to pass to the driver. Do not include arguments, such as ``--conf``, that can be set as job properties, since a collision may occur that causes an incorrect job submission. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#args GoogleDataprocWorkflowTemplate#args}
        :param file_uris: Optional. HCFS URIs of files to be placed in the working directory of each executor. Useful for naively parallel tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#file_uris GoogleDataprocWorkflowTemplate#file_uris}
        :param jar_file_uris: Optional. HCFS URIs of jar files to add to the CLASSPATHs of the Python driver and tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        :param properties: Optional. A mapping of property names to values, used to configure PySpark. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        :param python_file_uris: Optional. HCFS file URIs of Python files to pass to the PySpark framework. Supported file types: .py, .egg, and .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#python_file_uris GoogleDataprocWorkflowTemplate#python_file_uris}
        '''
        if isinstance(logging_config, dict):
            logging_config = GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig(**logging_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPysparkJob.__init__)
            check_type(argname="argument main_python_file_uri", value=main_python_file_uri, expected_type=type_hints["main_python_file_uri"])
            check_type(argname="argument archive_uris", value=archive_uris, expected_type=type_hints["archive_uris"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument file_uris", value=file_uris, expected_type=type_hints["file_uris"])
            check_type(argname="argument jar_file_uris", value=jar_file_uris, expected_type=type_hints["jar_file_uris"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument python_file_uris", value=python_file_uris, expected_type=type_hints["python_file_uris"])
        self._values: typing.Dict[str, typing.Any] = {
            "main_python_file_uri": main_python_file_uri,
        }
        if archive_uris is not None:
            self._values["archive_uris"] = archive_uris
        if args is not None:
            self._values["args"] = args
        if file_uris is not None:
            self._values["file_uris"] = file_uris
        if jar_file_uris is not None:
            self._values["jar_file_uris"] = jar_file_uris
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if properties is not None:
            self._values["properties"] = properties
        if python_file_uris is not None:
            self._values["python_file_uris"] = python_file_uris

    @builtins.property
    def main_python_file_uri(self) -> builtins.str:
        '''Required. The HCFS URI of the main Python file to use as the driver. Must be a .py file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_python_file_uri GoogleDataprocWorkflowTemplate#main_python_file_uri}
        '''
        result = self._values.get("main_python_file_uri")
        assert result is not None, "Required property 'main_python_file_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def archive_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#archive_uris GoogleDataprocWorkflowTemplate#archive_uris}
        '''
        result = self._values.get("archive_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        The arguments to pass to the driver. Do not include arguments, such as ``--conf``, that can be set as job properties, since a collision may occur that causes an incorrect job submission.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#args GoogleDataprocWorkflowTemplate#args}
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        HCFS URIs of files to be placed in the working directory of each executor. Useful for naively parallel tasks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#file_uris GoogleDataprocWorkflowTemplate#file_uris}
        '''
        result = self._values.get("file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def jar_file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional. HCFS URIs of jar files to add to the CLASSPATHs of the Python driver and tasks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        '''
        result = self._values.get("jar_file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig"]:
        '''logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig"], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        A mapping of property names to values, used to configure PySpark. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def python_file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        HCFS file URIs of Python files to pass to the PySpark framework. Supported file types: .py, .egg, and .zip.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#python_file_uris GoogleDataprocWorkflowTemplate#python_file_uris}
        '''
        result = self._values.get("python_file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsPysparkJob(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={"driver_log_levels": "driverLogLevels"},
)
class GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig:
    def __init__(
        self,
        *,
        driver_log_levels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver_log_levels: The per-package log levels for the driver. This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig.__init__)
            check_type(argname="argument driver_log_levels", value=driver_log_levels, expected_type=type_hints["driver_log_levels"])
        self._values: typing.Dict[str, typing.Any] = {}
        if driver_log_levels is not None:
            self._values["driver_log_levels"] = driver_log_levels

    @builtins.property
    def driver_log_levels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The per-package log levels for the driver.

        This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        result = self._values.get("driver_log_levels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDriverLogLevels")
    def reset_driver_log_levels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverLogLevels", []))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevelsInput")
    def driver_log_levels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverLogLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevels")
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverLogLevels"))

    @driver_log_levels.setter
    def driver_log_levels(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfigOutputReference, "driver_log_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverLogLevels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplateJobsPysparkJobOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsPysparkJobOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsPysparkJobOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLoggingConfig")
    def put_logging_config(
        self,
        *,
        driver_log_levels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver_log_levels: The per-package log levels for the driver. This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        value = GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig(
            driver_log_levels=driver_log_levels
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfig", [value]))

    @jsii.member(jsii_name="resetArchiveUris")
    def reset_archive_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchiveUris", []))

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @jsii.member(jsii_name="resetFileUris")
    def reset_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileUris", []))

    @jsii.member(jsii_name="resetJarFileUris")
    def reset_jar_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJarFileUris", []))

    @jsii.member(jsii_name="resetLoggingConfig")
    def reset_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfig", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetPythonFileUris")
    def reset_python_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPythonFileUris", []))

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfigOutputReference, jsii.get(self, "loggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="archiveUrisInput")
    def archive_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "archiveUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="fileUrisInput")
    def file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "fileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="jarFileUrisInput")
    def jar_file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jarFileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigInput")
    def logging_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig], jsii.get(self, "loggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="mainPythonFileUriInput")
    def main_python_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mainPythonFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="pythonFileUrisInput")
    def python_file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pythonFileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="archiveUris")
    def archive_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "archiveUris"))

    @archive_uris.setter
    def archive_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPysparkJobOutputReference, "archive_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archiveUris", value)

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPysparkJobOutputReference, "args").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

    @builtins.property
    @jsii.member(jsii_name="fileUris")
    def file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "fileUris"))

    @file_uris.setter
    def file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPysparkJobOutputReference, "file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileUris", value)

    @builtins.property
    @jsii.member(jsii_name="jarFileUris")
    def jar_file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jarFileUris"))

    @jar_file_uris.setter
    def jar_file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPysparkJobOutputReference, "jar_file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jarFileUris", value)

    @builtins.property
    @jsii.member(jsii_name="mainPythonFileUri")
    def main_python_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mainPythonFileUri"))

    @main_python_file_uri.setter
    def main_python_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPysparkJobOutputReference, "main_python_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mainPythonFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPysparkJobOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="pythonFileUris")
    def python_file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pythonFileUris"))

    @python_file_uris.setter
    def python_file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPysparkJobOutputReference, "python_file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pythonFileUris", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsPysparkJob]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsPysparkJob], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsPysparkJob],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsPysparkJobOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsScheduling",
    jsii_struct_bases=[],
    name_mapping={
        "max_failures_per_hour": "maxFailuresPerHour",
        "max_failures_total": "maxFailuresTotal",
    },
)
class GoogleDataprocWorkflowTemplateJobsScheduling:
    def __init__(
        self,
        *,
        max_failures_per_hour: typing.Optional[jsii.Number] = None,
        max_failures_total: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_failures_per_hour: Optional. Maximum number of times per hour a driver may be restarted as a result of driver exiting with non-zero code before job is reported failed. A job may be reported as thrashing if driver exits with non-zero code 4 times within 10 minute window. Maximum value is 10. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#max_failures_per_hour GoogleDataprocWorkflowTemplate#max_failures_per_hour}
        :param max_failures_total: Optional. Maximum number of times in total a driver may be restarted as a result of driver exiting with non-zero code before job is reported failed. Maximum value is 240. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#max_failures_total GoogleDataprocWorkflowTemplate#max_failures_total}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsScheduling.__init__)
            check_type(argname="argument max_failures_per_hour", value=max_failures_per_hour, expected_type=type_hints["max_failures_per_hour"])
            check_type(argname="argument max_failures_total", value=max_failures_total, expected_type=type_hints["max_failures_total"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_failures_per_hour is not None:
            self._values["max_failures_per_hour"] = max_failures_per_hour
        if max_failures_total is not None:
            self._values["max_failures_total"] = max_failures_total

    @builtins.property
    def max_failures_per_hour(self) -> typing.Optional[jsii.Number]:
        '''Optional.

        Maximum number of times per hour a driver may be restarted as a result of driver exiting with non-zero code before job is reported failed. A job may be reported as thrashing if driver exits with non-zero code 4 times within 10 minute window. Maximum value is 10.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#max_failures_per_hour GoogleDataprocWorkflowTemplate#max_failures_per_hour}
        '''
        result = self._values.get("max_failures_per_hour")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_failures_total(self) -> typing.Optional[jsii.Number]:
        '''Optional.

        Maximum number of times in total a driver may be restarted as a result of driver exiting with non-zero code before job is reported failed. Maximum value is 240.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#max_failures_total GoogleDataprocWorkflowTemplate#max_failures_total}
        '''
        result = self._values.get("max_failures_total")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsScheduling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateJobsSchedulingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsSchedulingOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsSchedulingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxFailuresPerHour")
    def reset_max_failures_per_hour(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxFailuresPerHour", []))

    @jsii.member(jsii_name="resetMaxFailuresTotal")
    def reset_max_failures_total(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxFailuresTotal", []))

    @builtins.property
    @jsii.member(jsii_name="maxFailuresPerHourInput")
    def max_failures_per_hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxFailuresPerHourInput"))

    @builtins.property
    @jsii.member(jsii_name="maxFailuresTotalInput")
    def max_failures_total_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxFailuresTotalInput"))

    @builtins.property
    @jsii.member(jsii_name="maxFailuresPerHour")
    def max_failures_per_hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxFailuresPerHour"))

    @max_failures_per_hour.setter
    def max_failures_per_hour(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSchedulingOutputReference, "max_failures_per_hour").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxFailuresPerHour", value)

    @builtins.property
    @jsii.member(jsii_name="maxFailuresTotal")
    def max_failures_total(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxFailuresTotal"))

    @max_failures_total.setter
    def max_failures_total(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSchedulingOutputReference, "max_failures_total").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxFailuresTotal", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsScheduling]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsScheduling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsScheduling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSchedulingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsSparkJob",
    jsii_struct_bases=[],
    name_mapping={
        "archive_uris": "archiveUris",
        "args": "args",
        "file_uris": "fileUris",
        "jar_file_uris": "jarFileUris",
        "logging_config": "loggingConfig",
        "main_class": "mainClass",
        "main_jar_file_uri": "mainJarFileUri",
        "properties": "properties",
    },
)
class GoogleDataprocWorkflowTemplateJobsSparkJob:
    def __init__(
        self,
        *,
        archive_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        main_class: typing.Optional[builtins.str] = None,
        main_jar_file_uri: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param archive_uris: Optional. HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#archive_uris GoogleDataprocWorkflowTemplate#archive_uris}
        :param args: Optional. The arguments to pass to the driver. Do not include arguments, such as ``--conf``, that can be set as job properties, since a collision may occur that causes an incorrect job submission. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#args GoogleDataprocWorkflowTemplate#args}
        :param file_uris: Optional. HCFS URIs of files to be placed in the working directory of each executor. Useful for naively parallel tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#file_uris GoogleDataprocWorkflowTemplate#file_uris}
        :param jar_file_uris: Optional. HCFS URIs of jar files to add to the CLASSPATHs of the Spark driver and tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        :param main_class: The name of the driver's main class. The jar file that contains the class must be in the default CLASSPATH or specified in ``jar_file_uris``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_class GoogleDataprocWorkflowTemplate#main_class}
        :param main_jar_file_uri: The HCFS URI of the jar file that contains the main class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_jar_file_uri GoogleDataprocWorkflowTemplate#main_jar_file_uri}
        :param properties: Optional. A mapping of property names to values, used to configure Spark. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        if isinstance(logging_config, dict):
            logging_config = GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig(**logging_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsSparkJob.__init__)
            check_type(argname="argument archive_uris", value=archive_uris, expected_type=type_hints["archive_uris"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument file_uris", value=file_uris, expected_type=type_hints["file_uris"])
            check_type(argname="argument jar_file_uris", value=jar_file_uris, expected_type=type_hints["jar_file_uris"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument main_class", value=main_class, expected_type=type_hints["main_class"])
            check_type(argname="argument main_jar_file_uri", value=main_jar_file_uri, expected_type=type_hints["main_jar_file_uri"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[str, typing.Any] = {}
        if archive_uris is not None:
            self._values["archive_uris"] = archive_uris
        if args is not None:
            self._values["args"] = args
        if file_uris is not None:
            self._values["file_uris"] = file_uris
        if jar_file_uris is not None:
            self._values["jar_file_uris"] = jar_file_uris
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if main_class is not None:
            self._values["main_class"] = main_class
        if main_jar_file_uri is not None:
            self._values["main_jar_file_uri"] = main_jar_file_uri
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def archive_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#archive_uris GoogleDataprocWorkflowTemplate#archive_uris}
        '''
        result = self._values.get("archive_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        The arguments to pass to the driver. Do not include arguments, such as ``--conf``, that can be set as job properties, since a collision may occur that causes an incorrect job submission.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#args GoogleDataprocWorkflowTemplate#args}
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        HCFS URIs of files to be placed in the working directory of each executor. Useful for naively parallel tasks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#file_uris GoogleDataprocWorkflowTemplate#file_uris}
        '''
        result = self._values.get("file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def jar_file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional. HCFS URIs of jar files to add to the CLASSPATHs of the Spark driver and tasks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        '''
        result = self._values.get("jar_file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig"]:
        '''logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig"], result)

    @builtins.property
    def main_class(self) -> typing.Optional[builtins.str]:
        '''The name of the driver's main class.

        The jar file that contains the class must be in the default CLASSPATH or specified in ``jar_file_uris``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_class GoogleDataprocWorkflowTemplate#main_class}
        '''
        result = self._values.get("main_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def main_jar_file_uri(self) -> typing.Optional[builtins.str]:
        '''The HCFS URI of the jar file that contains the main class.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_jar_file_uri GoogleDataprocWorkflowTemplate#main_jar_file_uri}
        '''
        result = self._values.get("main_jar_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        A mapping of property names to values, used to configure Spark. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsSparkJob(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={"driver_log_levels": "driverLogLevels"},
)
class GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig:
    def __init__(
        self,
        *,
        driver_log_levels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver_log_levels: The per-package log levels for the driver. This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig.__init__)
            check_type(argname="argument driver_log_levels", value=driver_log_levels, expected_type=type_hints["driver_log_levels"])
        self._values: typing.Dict[str, typing.Any] = {}
        if driver_log_levels is not None:
            self._values["driver_log_levels"] = driver_log_levels

    @builtins.property
    def driver_log_levels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The per-package log levels for the driver.

        This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        result = self._values.get("driver_log_levels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDriverLogLevels")
    def reset_driver_log_levels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverLogLevels", []))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevelsInput")
    def driver_log_levels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverLogLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevels")
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverLogLevels"))

    @driver_log_levels.setter
    def driver_log_levels(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfigOutputReference, "driver_log_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverLogLevels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplateJobsSparkJobOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsSparkJobOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsSparkJobOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLoggingConfig")
    def put_logging_config(
        self,
        *,
        driver_log_levels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver_log_levels: The per-package log levels for the driver. This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        value = GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig(
            driver_log_levels=driver_log_levels
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfig", [value]))

    @jsii.member(jsii_name="resetArchiveUris")
    def reset_archive_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchiveUris", []))

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @jsii.member(jsii_name="resetFileUris")
    def reset_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileUris", []))

    @jsii.member(jsii_name="resetJarFileUris")
    def reset_jar_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJarFileUris", []))

    @jsii.member(jsii_name="resetLoggingConfig")
    def reset_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfig", []))

    @jsii.member(jsii_name="resetMainClass")
    def reset_main_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMainClass", []))

    @jsii.member(jsii_name="resetMainJarFileUri")
    def reset_main_jar_file_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMainJarFileUri", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfigOutputReference, jsii.get(self, "loggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="archiveUrisInput")
    def archive_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "archiveUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="fileUrisInput")
    def file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "fileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="jarFileUrisInput")
    def jar_file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jarFileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigInput")
    def logging_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig], jsii.get(self, "loggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="mainClassInput")
    def main_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mainClassInput"))

    @builtins.property
    @jsii.member(jsii_name="mainJarFileUriInput")
    def main_jar_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mainJarFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="archiveUris")
    def archive_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "archiveUris"))

    @archive_uris.setter
    def archive_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkJobOutputReference, "archive_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archiveUris", value)

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkJobOutputReference, "args").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

    @builtins.property
    @jsii.member(jsii_name="fileUris")
    def file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "fileUris"))

    @file_uris.setter
    def file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkJobOutputReference, "file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileUris", value)

    @builtins.property
    @jsii.member(jsii_name="jarFileUris")
    def jar_file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jarFileUris"))

    @jar_file_uris.setter
    def jar_file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkJobOutputReference, "jar_file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jarFileUris", value)

    @builtins.property
    @jsii.member(jsii_name="mainClass")
    def main_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mainClass"))

    @main_class.setter
    def main_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkJobOutputReference, "main_class").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mainClass", value)

    @builtins.property
    @jsii.member(jsii_name="mainJarFileUri")
    def main_jar_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mainJarFileUri"))

    @main_jar_file_uri.setter
    def main_jar_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkJobOutputReference, "main_jar_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mainJarFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkJobOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkJob]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkJob], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkJob],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkJobOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsSparkRJob",
    jsii_struct_bases=[],
    name_mapping={
        "main_r_file_uri": "mainRFileUri",
        "archive_uris": "archiveUris",
        "args": "args",
        "file_uris": "fileUris",
        "logging_config": "loggingConfig",
        "properties": "properties",
    },
)
class GoogleDataprocWorkflowTemplateJobsSparkRJob:
    def __init__(
        self,
        *,
        main_r_file_uri: builtins.str,
        archive_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param main_r_file_uri: Required. The HCFS URI of the main R file to use as the driver. Must be a .R file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_r_file_uri GoogleDataprocWorkflowTemplate#main_r_file_uri}
        :param archive_uris: Optional. HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#archive_uris GoogleDataprocWorkflowTemplate#archive_uris}
        :param args: Optional. The arguments to pass to the driver. Do not include arguments, such as ``--conf``, that can be set as job properties, since a collision may occur that causes an incorrect job submission. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#args GoogleDataprocWorkflowTemplate#args}
        :param file_uris: Optional. HCFS URIs of files to be placed in the working directory of each executor. Useful for naively parallel tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#file_uris GoogleDataprocWorkflowTemplate#file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        :param properties: Optional. A mapping of property names to values, used to configure SparkR. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        if isinstance(logging_config, dict):
            logging_config = GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig(**logging_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsSparkRJob.__init__)
            check_type(argname="argument main_r_file_uri", value=main_r_file_uri, expected_type=type_hints["main_r_file_uri"])
            check_type(argname="argument archive_uris", value=archive_uris, expected_type=type_hints["archive_uris"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument file_uris", value=file_uris, expected_type=type_hints["file_uris"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[str, typing.Any] = {
            "main_r_file_uri": main_r_file_uri,
        }
        if archive_uris is not None:
            self._values["archive_uris"] = archive_uris
        if args is not None:
            self._values["args"] = args
        if file_uris is not None:
            self._values["file_uris"] = file_uris
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def main_r_file_uri(self) -> builtins.str:
        '''Required. The HCFS URI of the main R file to use as the driver. Must be a .R file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#main_r_file_uri GoogleDataprocWorkflowTemplate#main_r_file_uri}
        '''
        result = self._values.get("main_r_file_uri")
        assert result is not None, "Required property 'main_r_file_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def archive_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#archive_uris GoogleDataprocWorkflowTemplate#archive_uris}
        '''
        result = self._values.get("archive_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        The arguments to pass to the driver. Do not include arguments, such as ``--conf``, that can be set as job properties, since a collision may occur that causes an incorrect job submission.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#args GoogleDataprocWorkflowTemplate#args}
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        HCFS URIs of files to be placed in the working directory of each executor. Useful for naively parallel tasks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#file_uris GoogleDataprocWorkflowTemplate#file_uris}
        '''
        result = self._values.get("file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig"]:
        '''logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig"], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        A mapping of property names to values, used to configure SparkR. Properties that conflict with values set by the Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsSparkRJob(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={"driver_log_levels": "driverLogLevels"},
)
class GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig:
    def __init__(
        self,
        *,
        driver_log_levels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver_log_levels: The per-package log levels for the driver. This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig.__init__)
            check_type(argname="argument driver_log_levels", value=driver_log_levels, expected_type=type_hints["driver_log_levels"])
        self._values: typing.Dict[str, typing.Any] = {}
        if driver_log_levels is not None:
            self._values["driver_log_levels"] = driver_log_levels

    @builtins.property
    def driver_log_levels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The per-package log levels for the driver.

        This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        result = self._values.get("driver_log_levels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDriverLogLevels")
    def reset_driver_log_levels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverLogLevels", []))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevelsInput")
    def driver_log_levels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverLogLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevels")
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverLogLevels"))

    @driver_log_levels.setter
    def driver_log_levels(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfigOutputReference, "driver_log_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverLogLevels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplateJobsSparkRJobOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsSparkRJobOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsSparkRJobOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLoggingConfig")
    def put_logging_config(
        self,
        *,
        driver_log_levels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver_log_levels: The per-package log levels for the driver. This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        value = GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig(
            driver_log_levels=driver_log_levels
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfig", [value]))

    @jsii.member(jsii_name="resetArchiveUris")
    def reset_archive_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchiveUris", []))

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @jsii.member(jsii_name="resetFileUris")
    def reset_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileUris", []))

    @jsii.member(jsii_name="resetLoggingConfig")
    def reset_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfig", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfigOutputReference, jsii.get(self, "loggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="archiveUrisInput")
    def archive_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "archiveUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="fileUrisInput")
    def file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "fileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigInput")
    def logging_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig], jsii.get(self, "loggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="mainRFileUriInput")
    def main_r_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mainRFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="archiveUris")
    def archive_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "archiveUris"))

    @archive_uris.setter
    def archive_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkRJobOutputReference, "archive_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archiveUris", value)

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkRJobOutputReference, "args").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

    @builtins.property
    @jsii.member(jsii_name="fileUris")
    def file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "fileUris"))

    @file_uris.setter
    def file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkRJobOutputReference, "file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileUris", value)

    @builtins.property
    @jsii.member(jsii_name="mainRFileUri")
    def main_r_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mainRFileUri"))

    @main_r_file_uri.setter
    def main_r_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkRJobOutputReference, "main_r_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mainRFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkRJobOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkRJob]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkRJob], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkRJob],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkRJobOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsSparkSqlJob",
    jsii_struct_bases=[],
    name_mapping={
        "jar_file_uris": "jarFileUris",
        "logging_config": "loggingConfig",
        "properties": "properties",
        "query_file_uri": "queryFileUri",
        "query_list": "queryList",
        "script_variables": "scriptVariables",
    },
)
class GoogleDataprocWorkflowTemplateJobsSparkSqlJob:
    def __init__(
        self,
        *,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList", typing.Dict[str, typing.Any]]] = None,
        script_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param jar_file_uris: Optional. HCFS URIs of jar files to be added to the Spark CLASSPATH. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        :param properties: Optional. A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Dataproc API may be overwritten. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        :param query_file_uri: The HCFS URI of the script that contains SQL queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_file_uri GoogleDataprocWorkflowTemplate#query_file_uri}
        :param query_list: query_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_list GoogleDataprocWorkflowTemplate#query_list}
        :param script_variables: Optional. Mapping of query variable names to values (equivalent to the Spark SQL command: SET ``name="value";``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#script_variables GoogleDataprocWorkflowTemplate#script_variables}
        '''
        if isinstance(logging_config, dict):
            logging_config = GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig(**logging_config)
        if isinstance(query_list, dict):
            query_list = GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList(**query_list)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsSparkSqlJob.__init__)
            check_type(argname="argument jar_file_uris", value=jar_file_uris, expected_type=type_hints["jar_file_uris"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument query_file_uri", value=query_file_uri, expected_type=type_hints["query_file_uri"])
            check_type(argname="argument query_list", value=query_list, expected_type=type_hints["query_list"])
            check_type(argname="argument script_variables", value=script_variables, expected_type=type_hints["script_variables"])
        self._values: typing.Dict[str, typing.Any] = {}
        if jar_file_uris is not None:
            self._values["jar_file_uris"] = jar_file_uris
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if properties is not None:
            self._values["properties"] = properties
        if query_file_uri is not None:
            self._values["query_file_uri"] = query_file_uri
        if query_list is not None:
            self._values["query_list"] = query_list
        if script_variables is not None:
            self._values["script_variables"] = script_variables

    @builtins.property
    def jar_file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional. HCFS URIs of jar files to be added to the Spark CLASSPATH.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#jar_file_uris GoogleDataprocWorkflowTemplate#jar_file_uris}
        '''
        result = self._values.get("jar_file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig"]:
        '''logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#logging_config GoogleDataprocWorkflowTemplate#logging_config}
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig"], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Dataproc API may be overwritten.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def query_file_uri(self) -> typing.Optional[builtins.str]:
        '''The HCFS URI of the script that contains SQL queries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_file_uri GoogleDataprocWorkflowTemplate#query_file_uri}
        '''
        result = self._values.get("query_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_list(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList"]:
        '''query_list block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#query_list GoogleDataprocWorkflowTemplate#query_list}
        '''
        result = self._values.get("query_list")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList"], result)

    @builtins.property
    def script_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional. Mapping of query variable names to values (equivalent to the Spark SQL command: SET ``name="value";``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#script_variables GoogleDataprocWorkflowTemplate#script_variables}
        '''
        result = self._values.get("script_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsSparkSqlJob(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={"driver_log_levels": "driverLogLevels"},
)
class GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig:
    def __init__(
        self,
        *,
        driver_log_levels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver_log_levels: The per-package log levels for the driver. This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig.__init__)
            check_type(argname="argument driver_log_levels", value=driver_log_levels, expected_type=type_hints["driver_log_levels"])
        self._values: typing.Dict[str, typing.Any] = {}
        if driver_log_levels is not None:
            self._values["driver_log_levels"] = driver_log_levels

    @builtins.property
    def driver_log_levels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The per-package log levels for the driver.

        This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        result = self._values.get("driver_log_levels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDriverLogLevels")
    def reset_driver_log_levels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverLogLevels", []))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevelsInput")
    def driver_log_levels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverLogLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevels")
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverLogLevels"))

    @driver_log_levels.setter
    def driver_log_levels(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfigOutputReference, "driver_log_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverLogLevels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplateJobsSparkSqlJobOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsSparkSqlJobOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsSparkSqlJobOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLoggingConfig")
    def put_logging_config(
        self,
        *,
        driver_log_levels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver_log_levels: The per-package log levels for the driver. This may include "root" package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#driver_log_levels GoogleDataprocWorkflowTemplate#driver_log_levels}
        '''
        value = GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig(
            driver_log_levels=driver_log_levels
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfig", [value]))

    @jsii.member(jsii_name="putQueryList")
    def put_query_list(self, *, queries: typing.Sequence[builtins.str]) -> None:
        '''
        :param queries: Required. The queries to execute. You do not need to end a query expression with a semicolon. Multiple queries can be specified in one string by separating each with a semicolon. Here is an example of a Dataproc API snippet that uses a QueryList to specify a HiveJob: "hiveJob": { "queryList": { "queries": [ "query1", "query2", "query3;query4", ] } } Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#queries GoogleDataprocWorkflowTemplate#queries}
        '''
        value = GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList(queries=queries)

        return typing.cast(None, jsii.invoke(self, "putQueryList", [value]))

    @jsii.member(jsii_name="resetJarFileUris")
    def reset_jar_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJarFileUris", []))

    @jsii.member(jsii_name="resetLoggingConfig")
    def reset_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfig", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetQueryFileUri")
    def reset_query_file_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryFileUri", []))

    @jsii.member(jsii_name="resetQueryList")
    def reset_query_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryList", []))

    @jsii.member(jsii_name="resetScriptVariables")
    def reset_script_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScriptVariables", []))

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfigOutputReference, jsii.get(self, "loggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="queryList")
    def query_list(
        self,
    ) -> "GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryListOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryListOutputReference", jsii.get(self, "queryList"))

    @builtins.property
    @jsii.member(jsii_name="jarFileUrisInput")
    def jar_file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jarFileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigInput")
    def logging_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig], jsii.get(self, "loggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="queryFileUriInput")
    def query_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="queryListInput")
    def query_list_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList"], jsii.get(self, "queryListInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptVariablesInput")
    def script_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "scriptVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="jarFileUris")
    def jar_file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jarFileUris"))

    @jar_file_uris.setter
    def jar_file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkSqlJobOutputReference, "jar_file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jarFileUris", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkSqlJobOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="queryFileUri")
    def query_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryFileUri"))

    @query_file_uri.setter
    def query_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkSqlJobOutputReference, "query_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="scriptVariables")
    def script_variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "scriptVariables"))

    @script_variables.setter
    def script_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkSqlJobOutputReference, "script_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scriptVariables", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkSqlJob]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkSqlJob], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkSqlJob],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkSqlJobOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList",
    jsii_struct_bases=[],
    name_mapping={"queries": "queries"},
)
class GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList:
    def __init__(self, *, queries: typing.Sequence[builtins.str]) -> None:
        '''
        :param queries: Required. The queries to execute. You do not need to end a query expression with a semicolon. Multiple queries can be specified in one string by separating each with a semicolon. Here is an example of a Dataproc API snippet that uses a QueryList to specify a HiveJob: "hiveJob": { "queryList": { "queries": [ "query1", "query2", "query3;query4", ] } } Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#queries GoogleDataprocWorkflowTemplate#queries}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList.__init__)
            check_type(argname="argument queries", value=queries, expected_type=type_hints["queries"])
        self._values: typing.Dict[str, typing.Any] = {
            "queries": queries,
        }

    @builtins.property
    def queries(self) -> typing.List[builtins.str]:
        '''Required.

        The queries to execute. You do not need to end a query expression with a semicolon. Multiple queries can be specified in one string by separating each with a semicolon. Here is an example of a Dataproc API snippet that uses a QueryList to specify a HiveJob: "hiveJob": { "queryList": { "queries": [ "query1", "query2", "query3;query4", ] } }

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#queries GoogleDataprocWorkflowTemplate#queries}
        '''
        result = self._values.get("queries")
        assert result is not None, "Required property 'queries' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryListOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryListOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryListOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="queriesInput")
    def queries_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queriesInput"))

    @builtins.property
    @jsii.member(jsii_name="queries")
    def queries(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queries"))

    @queries.setter
    def queries(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryListOutputReference, "queries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queries", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryListOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateParameters",
    jsii_struct_bases=[],
    name_mapping={
        "fields": "fields",
        "name": "name",
        "description": "description",
        "validation": "validation",
    },
)
class GoogleDataprocWorkflowTemplateParameters:
    def __init__(
        self,
        *,
        fields: typing.Sequence[builtins.str],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        validation: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateParametersValidation", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param fields: Required. Paths to all fields that the parameter replaces. A field is allowed to appear in at most one parameter's list of field paths. A field path is similar in syntax to a google.protobuf.FieldMask. For example, a field path that references the zone field of a workflow template's cluster selector would be specified as ``placement.clusterSelector.zone``. Also, field paths can reference fields using the following syntax: * Values in maps can be referenced by key: * labels['key'] * placement.clusterSelector.clusterLabels['key'] * placement.managedCluster.labels['key'] * placement.clusterSelector.clusterLabels['key'] * jobs['step-id'].labels['key'] * Jobs in the jobs list can be referenced by step-id: * jobs['step-id'].hadoopJob.mainJarFileUri * jobs['step-id'].hiveJob.queryFileUri * jobs['step-id'].pySparkJob.mainPythonFileUri * jobs['step-id'].hadoopJob.jarFileUris[0] * jobs['step-id'].hadoopJob.archiveUris[0] * jobs['step-id'].hadoopJob.fileUris[0] * jobs['step-id'].pySparkJob.pythonFileUris[0] * Items in repeated fields can be referenced by a zero-based index: * jobs['step-id'].sparkJob.args[0] * Other examples: * jobs['step-id'].hadoopJob.properties['key'] * jobs['step-id'].hadoopJob.args[0] * jobs['step-id'].hiveJob.scriptVariables['key'] * jobs['step-id'].hadoopJob.mainJarFileUri * placement.clusterSelector.zone It may not be possible to parameterize maps and repeated fields in their entirety since only individual map values and individual items in repeated fields can be referenced. For example, the following field paths are invalid: - placement.clusterSelector.clusterLabels - jobs['step-id'].sparkJob.args Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#fields GoogleDataprocWorkflowTemplate#fields}
        :param name: Required. Parameter name. The parameter name is used as the key, and paired with the parameter value, which are passed to the template when the template is instantiated. The name must contain only capital letters (A-Z), numbers (0-9), and underscores (_), and must not start with a number. The maximum length is 40 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#name GoogleDataprocWorkflowTemplate#name}
        :param description: Optional. Brief description of the parameter. Must not exceed 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#description GoogleDataprocWorkflowTemplate#description}
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#validation GoogleDataprocWorkflowTemplate#validation}
        '''
        if isinstance(validation, dict):
            validation = GoogleDataprocWorkflowTemplateParametersValidation(**validation)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateParameters.__init__)
            check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument validation", value=validation, expected_type=type_hints["validation"])
        self._values: typing.Dict[str, typing.Any] = {
            "fields": fields,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if validation is not None:
            self._values["validation"] = validation

    @builtins.property
    def fields(self) -> typing.List[builtins.str]:
        '''Required.

        Paths to all fields that the parameter replaces. A field is allowed to appear in at most one parameter's list of field paths. A field path is similar in syntax to a google.protobuf.FieldMask. For example, a field path that references the zone field of a workflow template's cluster selector would be specified as ``placement.clusterSelector.zone``. Also, field paths can reference fields using the following syntax: * Values in maps can be referenced by key: * labels['key'] * placement.clusterSelector.clusterLabels['key'] * placement.managedCluster.labels['key'] * placement.clusterSelector.clusterLabels['key'] * jobs['step-id'].labels['key'] * Jobs in the jobs list can be referenced by step-id: * jobs['step-id'].hadoopJob.mainJarFileUri * jobs['step-id'].hiveJob.queryFileUri * jobs['step-id'].pySparkJob.mainPythonFileUri * jobs['step-id'].hadoopJob.jarFileUris[0] * jobs['step-id'].hadoopJob.archiveUris[0] * jobs['step-id'].hadoopJob.fileUris[0] * jobs['step-id'].pySparkJob.pythonFileUris[0] * Items in repeated fields can be referenced by a zero-based index: * jobs['step-id'].sparkJob.args[0] * Other examples: * jobs['step-id'].hadoopJob.properties['key'] * jobs['step-id'].hadoopJob.args[0] * jobs['step-id'].hiveJob.scriptVariables['key'] * jobs['step-id'].hadoopJob.mainJarFileUri * placement.clusterSelector.zone It may not be possible to parameterize maps and repeated fields in their entirety since only individual map values and individual items in repeated fields can be referenced. For example, the following field paths are invalid: - placement.clusterSelector.clusterLabels - jobs['step-id'].sparkJob.args

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#fields GoogleDataprocWorkflowTemplate#fields}
        '''
        result = self._values.get("fields")
        assert result is not None, "Required property 'fields' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Required.

        Parameter name. The parameter name is used as the key, and paired with the parameter value, which are passed to the template when the template is instantiated. The name must contain only capital letters (A-Z), numbers (0-9), and underscores (_), and must not start with a number. The maximum length is 40 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#name GoogleDataprocWorkflowTemplate#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Optional. Brief description of the parameter. Must not exceed 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#description GoogleDataprocWorkflowTemplate#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validation(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateParametersValidation"]:
        '''validation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#validation GoogleDataprocWorkflowTemplate#validation}
        '''
        result = self._values.get("validation")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateParametersValidation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateParametersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateParametersList",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateParametersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDataprocWorkflowTemplateParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateParametersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDataprocWorkflowTemplateParametersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateParametersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateParametersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateParametersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplateParameters]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplateParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplateParameters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateParametersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplateParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateParametersOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateParametersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putValidation")
    def put_validation(
        self,
        *,
        regex: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateParametersValidationRegex", typing.Dict[str, typing.Any]]] = None,
        values: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateParametersValidationValues", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param regex: regex block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#regex GoogleDataprocWorkflowTemplate#regex}
        :param values: values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#values GoogleDataprocWorkflowTemplate#values}
        '''
        value = GoogleDataprocWorkflowTemplateParametersValidation(
            regex=regex, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putValidation", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetValidation")
    def reset_validation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidation", []))

    @builtins.property
    @jsii.member(jsii_name="validation")
    def validation(
        self,
    ) -> "GoogleDataprocWorkflowTemplateParametersValidationOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplateParametersValidationOutputReference", jsii.get(self, "validation"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldsInput")
    def fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "fieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="validationInput")
    def validation_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateParametersValidation"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateParametersValidation"], jsii.get(self, "validationInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateParametersOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="fields")
    def fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "fields"))

    @fields.setter
    def fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateParametersOutputReference, "fields").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fields", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateParametersOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataprocWorkflowTemplateParameters, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataprocWorkflowTemplateParameters, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplateParameters, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateParametersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateParametersValidation",
    jsii_struct_bases=[],
    name_mapping={"regex": "regex", "values": "values"},
)
class GoogleDataprocWorkflowTemplateParametersValidation:
    def __init__(
        self,
        *,
        regex: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateParametersValidationRegex", typing.Dict[str, typing.Any]]] = None,
        values: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplateParametersValidationValues", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param regex: regex block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#regex GoogleDataprocWorkflowTemplate#regex}
        :param values: values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#values GoogleDataprocWorkflowTemplate#values}
        '''
        if isinstance(regex, dict):
            regex = GoogleDataprocWorkflowTemplateParametersValidationRegex(**regex)
        if isinstance(values, dict):
            values = GoogleDataprocWorkflowTemplateParametersValidationValues(**values)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateParametersValidation.__init__)
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if regex is not None:
            self._values["regex"] = regex
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def regex(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateParametersValidationRegex"]:
        '''regex block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#regex GoogleDataprocWorkflowTemplate#regex}
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateParametersValidationRegex"], result)

    @builtins.property
    def values(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateParametersValidationValues"]:
        '''values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#values GoogleDataprocWorkflowTemplate#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateParametersValidationValues"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateParametersValidation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateParametersValidationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateParametersValidationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateParametersValidationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRegex")
    def put_regex(self, *, regexes: typing.Sequence[builtins.str]) -> None:
        '''
        :param regexes: Required. RE2 regular expressions used to validate the parameter's value. The value must match the regex in its entirety (substring matches are not sufficient). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#regexes GoogleDataprocWorkflowTemplate#regexes}
        '''
        value = GoogleDataprocWorkflowTemplateParametersValidationRegex(
            regexes=regexes
        )

        return typing.cast(None, jsii.invoke(self, "putRegex", [value]))

    @jsii.member(jsii_name="putValues")
    def put_values(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Required. List of allowed values for the parameter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#values GoogleDataprocWorkflowTemplate#values}
        '''
        value = GoogleDataprocWorkflowTemplateParametersValidationValues(values=values)

        return typing.cast(None, jsii.invoke(self, "putValues", [value]))

    @jsii.member(jsii_name="resetRegex")
    def reset_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegex", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="regex")
    def regex(
        self,
    ) -> "GoogleDataprocWorkflowTemplateParametersValidationRegexOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplateParametersValidationRegexOutputReference", jsii.get(self, "regex"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(
        self,
    ) -> "GoogleDataprocWorkflowTemplateParametersValidationValuesOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplateParametersValidationValuesOutputReference", jsii.get(self, "values"))

    @builtins.property
    @jsii.member(jsii_name="regexInput")
    def regex_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateParametersValidationRegex"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateParametersValidationRegex"], jsii.get(self, "regexInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplateParametersValidationValues"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplateParametersValidationValues"], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateParametersValidation]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateParametersValidation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateParametersValidation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateParametersValidationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateParametersValidationRegex",
    jsii_struct_bases=[],
    name_mapping={"regexes": "regexes"},
)
class GoogleDataprocWorkflowTemplateParametersValidationRegex:
    def __init__(self, *, regexes: typing.Sequence[builtins.str]) -> None:
        '''
        :param regexes: Required. RE2 regular expressions used to validate the parameter's value. The value must match the regex in its entirety (substring matches are not sufficient). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#regexes GoogleDataprocWorkflowTemplate#regexes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateParametersValidationRegex.__init__)
            check_type(argname="argument regexes", value=regexes, expected_type=type_hints["regexes"])
        self._values: typing.Dict[str, typing.Any] = {
            "regexes": regexes,
        }

    @builtins.property
    def regexes(self) -> typing.List[builtins.str]:
        '''Required.

        RE2 regular expressions used to validate the parameter's value. The value must match the regex in its entirety (substring matches are not sufficient).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#regexes GoogleDataprocWorkflowTemplate#regexes}
        '''
        result = self._values.get("regexes")
        assert result is not None, "Required property 'regexes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateParametersValidationRegex(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateParametersValidationRegexOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateParametersValidationRegexOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateParametersValidationRegexOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="regexesInput")
    def regexes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "regexesInput"))

    @builtins.property
    @jsii.member(jsii_name="regexes")
    def regexes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regexes"))

    @regexes.setter
    def regexes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateParametersValidationRegexOutputReference, "regexes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regexes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateParametersValidationRegex]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateParametersValidationRegex], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateParametersValidationRegex],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateParametersValidationRegexOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateParametersValidationValues",
    jsii_struct_bases=[],
    name_mapping={"values": "values"},
)
class GoogleDataprocWorkflowTemplateParametersValidationValues:
    def __init__(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Required. List of allowed values for the parameter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#values GoogleDataprocWorkflowTemplate#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateParametersValidationValues.__init__)
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "values": values,
        }

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Required. List of allowed values for the parameter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#values GoogleDataprocWorkflowTemplate#values}
        '''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateParametersValidationValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateParametersValidationValuesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateParametersValidationValuesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateParametersValidationValuesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateParametersValidationValuesOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplateParametersValidationValues]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplateParametersValidationValues], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplateParametersValidationValues],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateParametersValidationValuesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacement",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_selector": "clusterSelector",
        "managed_cluster": "managedCluster",
    },
)
class GoogleDataprocWorkflowTemplatePlacement:
    def __init__(
        self,
        *,
        cluster_selector: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementClusterSelector", typing.Dict[str, typing.Any]]] = None,
        managed_cluster: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedCluster", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cluster_selector: cluster_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cluster_selector GoogleDataprocWorkflowTemplate#cluster_selector}
        :param managed_cluster: managed_cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#managed_cluster GoogleDataprocWorkflowTemplate#managed_cluster}
        '''
        if isinstance(cluster_selector, dict):
            cluster_selector = GoogleDataprocWorkflowTemplatePlacementClusterSelector(**cluster_selector)
        if isinstance(managed_cluster, dict):
            managed_cluster = GoogleDataprocWorkflowTemplatePlacementManagedCluster(**managed_cluster)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacement.__init__)
            check_type(argname="argument cluster_selector", value=cluster_selector, expected_type=type_hints["cluster_selector"])
            check_type(argname="argument managed_cluster", value=managed_cluster, expected_type=type_hints["managed_cluster"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cluster_selector is not None:
            self._values["cluster_selector"] = cluster_selector
        if managed_cluster is not None:
            self._values["managed_cluster"] = managed_cluster

    @builtins.property
    def cluster_selector(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementClusterSelector"]:
        '''cluster_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cluster_selector GoogleDataprocWorkflowTemplate#cluster_selector}
        '''
        result = self._values.get("cluster_selector")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementClusterSelector"], result)

    @builtins.property
    def managed_cluster(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedCluster"]:
        '''managed_cluster block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#managed_cluster GoogleDataprocWorkflowTemplate#managed_cluster}
        '''
        result = self._values.get("managed_cluster")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedCluster"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementClusterSelector",
    jsii_struct_bases=[],
    name_mapping={"cluster_labels": "clusterLabels", "zone": "zone"},
)
class GoogleDataprocWorkflowTemplatePlacementClusterSelector:
    def __init__(
        self,
        *,
        cluster_labels: typing.Mapping[builtins.str, builtins.str],
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_labels: Required. The cluster labels. Cluster must have all labels to match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cluster_labels GoogleDataprocWorkflowTemplate#cluster_labels}
        :param zone: Optional. The zone where workflow process executes. This parameter does not affect the selection of the cluster. If unspecified, the zone of the first cluster matching the selector is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#zone GoogleDataprocWorkflowTemplate#zone}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementClusterSelector.__init__)
            check_type(argname="argument cluster_labels", value=cluster_labels, expected_type=type_hints["cluster_labels"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_labels": cluster_labels,
        }
        if zone is not None:
            self._values["zone"] = zone

    @builtins.property
    def cluster_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Required. The cluster labels. Cluster must have all labels to match.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cluster_labels GoogleDataprocWorkflowTemplate#cluster_labels}
        '''
        result = self._values.get("cluster_labels")
        assert result is not None, "Required property 'cluster_labels' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The zone where workflow process executes. This parameter does not affect the selection of the cluster. If unspecified, the zone of the first cluster matching the selector is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#zone GoogleDataprocWorkflowTemplate#zone}
        '''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementClusterSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementClusterSelectorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementClusterSelectorOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementClusterSelectorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetZone")
    def reset_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZone", []))

    @builtins.property
    @jsii.member(jsii_name="clusterLabelsInput")
    def cluster_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "clusterLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterLabels")
    def cluster_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "clusterLabels"))

    @cluster_labels.setter
    def cluster_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementClusterSelectorOutputReference, "cluster_labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterLabels", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementClusterSelectorOutputReference, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementClusterSelector]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementClusterSelector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementClusterSelector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementClusterSelectorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedCluster",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "config": "config",
        "labels": "labels",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedCluster:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        config: typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig", typing.Dict[str, typing.Any]],
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param cluster_name: Required. The cluster name prefix. A unique cluster name will be formed by appending a random suffix. The name must contain only lower-case letters (a-z), numbers (0-9), and hyphens (-). Must begin with a letter. Cannot begin or end with hyphen. Must consist of between 2 and 35 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cluster_name GoogleDataprocWorkflowTemplate#cluster_name}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#config GoogleDataprocWorkflowTemplate#config}
        :param labels: Optional. The labels to associate with this cluster. Label keys must be between 1 and 63 characters long, and must conform to the following PCRE regular expression: p{Ll}p{Lo}{0,62} Label values must be between 1 and 63 characters long, and must conform to the following PCRE regular expression: [p{Ll}p{Lo}p{N}_-]{0,63} No more than 32 labels can be associated with a given cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#labels GoogleDataprocWorkflowTemplate#labels}
        '''
        if isinstance(config, dict):
            config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig(**config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedCluster.__init__)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_name": cluster_name,
            "config": config,
        }
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''Required.

        The cluster name prefix. A unique cluster name will be formed by appending a random suffix. The name must contain only lower-case letters (a-z), numbers (0-9), and hyphens (-). Must begin with a letter. Cannot begin or end with hyphen. Must consist of between 2 and 35 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cluster_name GoogleDataprocWorkflowTemplate#cluster_name}
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config(self) -> "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig":
        '''config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#config GoogleDataprocWorkflowTemplate#config}
        '''
        result = self._values.get("config")
        assert result is not None, "Required property 'config' is missing"
        return typing.cast("GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig", result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        The labels to associate with this cluster. Label keys must be between 1 and 63 characters long, and must conform to the following PCRE regular expression: p{Ll}p{Lo}{0,62} Label values must be between 1 and 63 characters long, and must conform to the following PCRE regular expression: [p{Ll}p{Lo}p{N}_-]{0,63} No more than 32 labels can be associated with a given cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#labels GoogleDataprocWorkflowTemplate#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedCluster(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig",
    jsii_struct_bases=[],
    name_mapping={
        "autoscaling_config": "autoscalingConfig",
        "encryption_config": "encryptionConfig",
        "endpoint_config": "endpointConfig",
        "gce_cluster_config": "gceClusterConfig",
        "gke_cluster_config": "gkeClusterConfig",
        "initialization_actions": "initializationActions",
        "lifecycle_config": "lifecycleConfig",
        "master_config": "masterConfig",
        "metastore_config": "metastoreConfig",
        "secondary_worker_config": "secondaryWorkerConfig",
        "security_config": "securityConfig",
        "software_config": "softwareConfig",
        "staging_bucket": "stagingBucket",
        "temp_bucket": "tempBucket",
        "worker_config": "workerConfig",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig:
    def __init__(
        self,
        *,
        autoscaling_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig", typing.Dict[str, typing.Any]]] = None,
        encryption_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig", typing.Dict[str, typing.Any]]] = None,
        endpoint_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig", typing.Dict[str, typing.Any]]] = None,
        gce_cluster_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig", typing.Dict[str, typing.Any]]] = None,
        gke_cluster_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig", typing.Dict[str, typing.Any]]] = None,
        initialization_actions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions", typing.Dict[str, typing.Any]]]]] = None,
        lifecycle_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig", typing.Dict[str, typing.Any]]] = None,
        master_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig", typing.Dict[str, typing.Any]]] = None,
        metastore_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig", typing.Dict[str, typing.Any]]] = None,
        secondary_worker_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig", typing.Dict[str, typing.Any]]] = None,
        security_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig", typing.Dict[str, typing.Any]]] = None,
        software_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig", typing.Dict[str, typing.Any]]] = None,
        staging_bucket: typing.Optional[builtins.str] = None,
        temp_bucket: typing.Optional[builtins.str] = None,
        worker_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param autoscaling_config: autoscaling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#autoscaling_config GoogleDataprocWorkflowTemplate#autoscaling_config}
        :param encryption_config: encryption_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#encryption_config GoogleDataprocWorkflowTemplate#encryption_config}
        :param endpoint_config: endpoint_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#endpoint_config GoogleDataprocWorkflowTemplate#endpoint_config}
        :param gce_cluster_config: gce_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#gce_cluster_config GoogleDataprocWorkflowTemplate#gce_cluster_config}
        :param gke_cluster_config: gke_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#gke_cluster_config GoogleDataprocWorkflowTemplate#gke_cluster_config}
        :param initialization_actions: initialization_actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#initialization_actions GoogleDataprocWorkflowTemplate#initialization_actions}
        :param lifecycle_config: lifecycle_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#lifecycle_config GoogleDataprocWorkflowTemplate#lifecycle_config}
        :param master_config: master_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#master_config GoogleDataprocWorkflowTemplate#master_config}
        :param metastore_config: metastore_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#metastore_config GoogleDataprocWorkflowTemplate#metastore_config}
        :param secondary_worker_config: secondary_worker_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#secondary_worker_config GoogleDataprocWorkflowTemplate#secondary_worker_config}
        :param security_config: security_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#security_config GoogleDataprocWorkflowTemplate#security_config}
        :param software_config: software_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#software_config GoogleDataprocWorkflowTemplate#software_config}
        :param staging_bucket: Optional. A Cloud Storage bucket used to stage job dependencies, config files, and job driver console output. If you do not specify a staging bucket, Cloud Dataproc will determine a Cloud Storage location (US, ASIA, or EU) for your cluster's staging bucket according to the Compute Engine zone where your cluster is deployed, and then create and manage this project-level, per-location bucket (see `Dataproc staging bucket <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/staging-bucket>`_). **This field requires a Cloud Storage bucket name, not a URI to a Cloud Storage bucket.** Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#staging_bucket GoogleDataprocWorkflowTemplate#staging_bucket}
        :param temp_bucket: Optional. A Cloud Storage bucket used to store ephemeral cluster and jobs data, such as Spark and MapReduce history files. If you do not specify a temp bucket, Dataproc will determine a Cloud Storage location (US, ASIA, or EU) for your cluster's temp bucket according to the Compute Engine zone where your cluster is deployed, and then create and manage this project-level, per-location bucket. The default bucket has a TTL of 90 days, but you can use any TTL (or none) if you specify a bucket. **This field requires a Cloud Storage bucket name, not a URI to a Cloud Storage bucket.** Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#temp_bucket GoogleDataprocWorkflowTemplate#temp_bucket}
        :param worker_config: worker_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#worker_config GoogleDataprocWorkflowTemplate#worker_config}
        '''
        if isinstance(autoscaling_config, dict):
            autoscaling_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig(**autoscaling_config)
        if isinstance(encryption_config, dict):
            encryption_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig(**encryption_config)
        if isinstance(endpoint_config, dict):
            endpoint_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig(**endpoint_config)
        if isinstance(gce_cluster_config, dict):
            gce_cluster_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig(**gce_cluster_config)
        if isinstance(gke_cluster_config, dict):
            gke_cluster_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig(**gke_cluster_config)
        if isinstance(lifecycle_config, dict):
            lifecycle_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig(**lifecycle_config)
        if isinstance(master_config, dict):
            master_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig(**master_config)
        if isinstance(metastore_config, dict):
            metastore_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig(**metastore_config)
        if isinstance(secondary_worker_config, dict):
            secondary_worker_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig(**secondary_worker_config)
        if isinstance(security_config, dict):
            security_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig(**security_config)
        if isinstance(software_config, dict):
            software_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig(**software_config)
        if isinstance(worker_config, dict):
            worker_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig(**worker_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig.__init__)
            check_type(argname="argument autoscaling_config", value=autoscaling_config, expected_type=type_hints["autoscaling_config"])
            check_type(argname="argument encryption_config", value=encryption_config, expected_type=type_hints["encryption_config"])
            check_type(argname="argument endpoint_config", value=endpoint_config, expected_type=type_hints["endpoint_config"])
            check_type(argname="argument gce_cluster_config", value=gce_cluster_config, expected_type=type_hints["gce_cluster_config"])
            check_type(argname="argument gke_cluster_config", value=gke_cluster_config, expected_type=type_hints["gke_cluster_config"])
            check_type(argname="argument initialization_actions", value=initialization_actions, expected_type=type_hints["initialization_actions"])
            check_type(argname="argument lifecycle_config", value=lifecycle_config, expected_type=type_hints["lifecycle_config"])
            check_type(argname="argument master_config", value=master_config, expected_type=type_hints["master_config"])
            check_type(argname="argument metastore_config", value=metastore_config, expected_type=type_hints["metastore_config"])
            check_type(argname="argument secondary_worker_config", value=secondary_worker_config, expected_type=type_hints["secondary_worker_config"])
            check_type(argname="argument security_config", value=security_config, expected_type=type_hints["security_config"])
            check_type(argname="argument software_config", value=software_config, expected_type=type_hints["software_config"])
            check_type(argname="argument staging_bucket", value=staging_bucket, expected_type=type_hints["staging_bucket"])
            check_type(argname="argument temp_bucket", value=temp_bucket, expected_type=type_hints["temp_bucket"])
            check_type(argname="argument worker_config", value=worker_config, expected_type=type_hints["worker_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if autoscaling_config is not None:
            self._values["autoscaling_config"] = autoscaling_config
        if encryption_config is not None:
            self._values["encryption_config"] = encryption_config
        if endpoint_config is not None:
            self._values["endpoint_config"] = endpoint_config
        if gce_cluster_config is not None:
            self._values["gce_cluster_config"] = gce_cluster_config
        if gke_cluster_config is not None:
            self._values["gke_cluster_config"] = gke_cluster_config
        if initialization_actions is not None:
            self._values["initialization_actions"] = initialization_actions
        if lifecycle_config is not None:
            self._values["lifecycle_config"] = lifecycle_config
        if master_config is not None:
            self._values["master_config"] = master_config
        if metastore_config is not None:
            self._values["metastore_config"] = metastore_config
        if secondary_worker_config is not None:
            self._values["secondary_worker_config"] = secondary_worker_config
        if security_config is not None:
            self._values["security_config"] = security_config
        if software_config is not None:
            self._values["software_config"] = software_config
        if staging_bucket is not None:
            self._values["staging_bucket"] = staging_bucket
        if temp_bucket is not None:
            self._values["temp_bucket"] = temp_bucket
        if worker_config is not None:
            self._values["worker_config"] = worker_config

    @builtins.property
    def autoscaling_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig"]:
        '''autoscaling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#autoscaling_config GoogleDataprocWorkflowTemplate#autoscaling_config}
        '''
        result = self._values.get("autoscaling_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig"], result)

    @builtins.property
    def encryption_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig"]:
        '''encryption_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#encryption_config GoogleDataprocWorkflowTemplate#encryption_config}
        '''
        result = self._values.get("encryption_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig"], result)

    @builtins.property
    def endpoint_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig"]:
        '''endpoint_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#endpoint_config GoogleDataprocWorkflowTemplate#endpoint_config}
        '''
        result = self._values.get("endpoint_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig"], result)

    @builtins.property
    def gce_cluster_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig"]:
        '''gce_cluster_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#gce_cluster_config GoogleDataprocWorkflowTemplate#gce_cluster_config}
        '''
        result = self._values.get("gce_cluster_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig"], result)

    @builtins.property
    def gke_cluster_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig"]:
        '''gke_cluster_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#gke_cluster_config GoogleDataprocWorkflowTemplate#gke_cluster_config}
        '''
        result = self._values.get("gke_cluster_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig"], result)

    @builtins.property
    def initialization_actions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions"]]]:
        '''initialization_actions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#initialization_actions GoogleDataprocWorkflowTemplate#initialization_actions}
        '''
        result = self._values.get("initialization_actions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions"]]], result)

    @builtins.property
    def lifecycle_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig"]:
        '''lifecycle_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#lifecycle_config GoogleDataprocWorkflowTemplate#lifecycle_config}
        '''
        result = self._values.get("lifecycle_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig"], result)

    @builtins.property
    def master_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig"]:
        '''master_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#master_config GoogleDataprocWorkflowTemplate#master_config}
        '''
        result = self._values.get("master_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig"], result)

    @builtins.property
    def metastore_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig"]:
        '''metastore_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#metastore_config GoogleDataprocWorkflowTemplate#metastore_config}
        '''
        result = self._values.get("metastore_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig"], result)

    @builtins.property
    def secondary_worker_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig"]:
        '''secondary_worker_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#secondary_worker_config GoogleDataprocWorkflowTemplate#secondary_worker_config}
        '''
        result = self._values.get("secondary_worker_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig"], result)

    @builtins.property
    def security_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig"]:
        '''security_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#security_config GoogleDataprocWorkflowTemplate#security_config}
        '''
        result = self._values.get("security_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig"], result)

    @builtins.property
    def software_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig"]:
        '''software_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#software_config GoogleDataprocWorkflowTemplate#software_config}
        '''
        result = self._values.get("software_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig"], result)

    @builtins.property
    def staging_bucket(self) -> typing.Optional[builtins.str]:
        '''Optional.

        A Cloud Storage bucket used to stage job dependencies, config files, and job driver console output. If you do not specify a staging bucket, Cloud Dataproc will determine a Cloud Storage location (US, ASIA, or EU) for your cluster's staging bucket according to the Compute Engine zone where your cluster is deployed, and then create and manage this project-level, per-location bucket (see `Dataproc staging bucket <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/staging-bucket>`_). **This field requires a Cloud Storage bucket name, not a URI to a Cloud Storage bucket.**

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#staging_bucket GoogleDataprocWorkflowTemplate#staging_bucket}
        '''
        result = self._values.get("staging_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def temp_bucket(self) -> typing.Optional[builtins.str]:
        '''Optional.

        A Cloud Storage bucket used to store ephemeral cluster and jobs data, such as Spark and MapReduce history files. If you do not specify a temp bucket, Dataproc will determine a Cloud Storage location (US, ASIA, or EU) for your cluster's temp bucket according to the Compute Engine zone where your cluster is deployed, and then create and manage this project-level, per-location bucket. The default bucket has a TTL of 90 days, but you can use any TTL (or none) if you specify a bucket. **This field requires a Cloud Storage bucket name, not a URI to a Cloud Storage bucket.**

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#temp_bucket GoogleDataprocWorkflowTemplate#temp_bucket}
        '''
        result = self._values.get("temp_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def worker_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig"]:
        '''worker_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#worker_config GoogleDataprocWorkflowTemplate#worker_config}
        '''
        result = self._values.get("worker_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig",
    jsii_struct_bases=[],
    name_mapping={"policy": "policy"},
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig:
    def __init__(self, *, policy: typing.Optional[builtins.str] = None) -> None:
        '''
        :param policy: Optional. The autoscaling policy used by the cluster. Only resource names including projectid and location (region) are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/locations/[dataproc_region]/autoscalingPolicies/[policy_id]`` * ``projects/[project_id]/locations/[dataproc_region]/autoscalingPolicies/[policy_id]`` Note that the policy must be in the same project and Dataproc region. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#policy GoogleDataprocWorkflowTemplate#policy}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig.__init__)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if policy is not None:
            self._values["policy"] = policy

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The autoscaling policy used by the cluster. Only resource names including projectid and location (region) are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/locations/[dataproc_region]/autoscalingPolicies/[policy_id]`` * ``projects/[project_id]/locations/[dataproc_region]/autoscalingPolicies/[policy_id]`` Note that the policy must be in the same project and Dataproc region.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#policy GoogleDataprocWorkflowTemplate#policy}
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPolicy")
    def reset_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfigOutputReference, "policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig",
    jsii_struct_bases=[],
    name_mapping={"gce_pd_kms_key_name": "gcePdKmsKeyName"},
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig:
    def __init__(
        self,
        *,
        gce_pd_kms_key_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param gce_pd_kms_key_name: Optional. The Cloud KMS key name to use for PD disk encryption for all instances in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#gce_pd_kms_key_name GoogleDataprocWorkflowTemplate#gce_pd_kms_key_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig.__init__)
            check_type(argname="argument gce_pd_kms_key_name", value=gce_pd_kms_key_name, expected_type=type_hints["gce_pd_kms_key_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if gce_pd_kms_key_name is not None:
            self._values["gce_pd_kms_key_name"] = gce_pd_kms_key_name

    @builtins.property
    def gce_pd_kms_key_name(self) -> typing.Optional[builtins.str]:
        '''Optional. The Cloud KMS key name to use for PD disk encryption for all instances in the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#gce_pd_kms_key_name GoogleDataprocWorkflowTemplate#gce_pd_kms_key_name}
        '''
        result = self._values.get("gce_pd_kms_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGcePdKmsKeyName")
    def reset_gce_pd_kms_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcePdKmsKeyName", []))

    @builtins.property
    @jsii.member(jsii_name="gcePdKmsKeyNameInput")
    def gce_pd_kms_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gcePdKmsKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="gcePdKmsKeyName")
    def gce_pd_kms_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gcePdKmsKeyName"))

    @gce_pd_kms_key_name.setter
    def gce_pd_kms_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfigOutputReference, "gce_pd_kms_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gcePdKmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig",
    jsii_struct_bases=[],
    name_mapping={"enable_http_port_access": "enableHttpPortAccess"},
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig:
    def __init__(
        self,
        *,
        enable_http_port_access: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_http_port_access: Optional. If true, enable http access to specific ports on the cluster from external sources. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#enable_http_port_access GoogleDataprocWorkflowTemplate#enable_http_port_access}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig.__init__)
            check_type(argname="argument enable_http_port_access", value=enable_http_port_access, expected_type=type_hints["enable_http_port_access"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enable_http_port_access is not None:
            self._values["enable_http_port_access"] = enable_http_port_access

    @builtins.property
    def enable_http_port_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional. If true, enable http access to specific ports on the cluster from external sources. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#enable_http_port_access GoogleDataprocWorkflowTemplate#enable_http_port_access}
        '''
        result = self._values.get("enable_http_port_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableHttpPortAccess")
    def reset_enable_http_port_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableHttpPortAccess", []))

    @builtins.property
    @jsii.member(jsii_name="httpPorts")
    def http_ports(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "httpPorts"))

    @builtins.property
    @jsii.member(jsii_name="enableHttpPortAccessInput")
    def enable_http_port_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableHttpPortAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="enableHttpPortAccess")
    def enable_http_port_access(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableHttpPortAccess"))

    @enable_http_port_access.setter
    def enable_http_port_access(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfigOutputReference, "enable_http_port_access").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableHttpPortAccess", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig",
    jsii_struct_bases=[],
    name_mapping={
        "internal_ip_only": "internalIpOnly",
        "metadata": "metadata",
        "network": "network",
        "node_group_affinity": "nodeGroupAffinity",
        "private_ipv6_google_access": "privateIpv6GoogleAccess",
        "reservation_affinity": "reservationAffinity",
        "service_account": "serviceAccount",
        "service_account_scopes": "serviceAccountScopes",
        "shielded_instance_config": "shieldedInstanceConfig",
        "subnetwork": "subnetwork",
        "tags": "tags",
        "zone": "zone",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig:
    def __init__(
        self,
        *,
        internal_ip_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        network: typing.Optional[builtins.str] = None,
        node_group_affinity: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity", typing.Dict[str, typing.Any]]] = None,
        private_ipv6_google_access: typing.Optional[builtins.str] = None,
        reservation_affinity: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity", typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[builtins.str] = None,
        service_account_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        shielded_instance_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig", typing.Dict[str, typing.Any]]] = None,
        subnetwork: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param internal_ip_only: Optional. If true, all instances in the cluster will only have internal IP addresses. By default, clusters are not restricted to internal IP addresses, and will have ephemeral external IP addresses assigned to each instance. This ``internal_ip_only`` restriction can only be enabled for subnetwork enabled networks, and all off-cluster dependencies must be configured to be accessible without external IP addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#internal_ip_only GoogleDataprocWorkflowTemplate#internal_ip_only}
        :param metadata: The Compute Engine metadata entries to add to all instances (see `Project and instance metadata <https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata>`_). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#metadata GoogleDataprocWorkflowTemplate#metadata}
        :param network: Optional. The Compute Engine network to be used for machine communications. Cannot be specified with subnetwork_uri. If neither ``network_uri`` nor ``subnetwork_uri`` is specified, the "default" network of the project is used, if it exists. Cannot be a "Custom Subnet Network" (see `Using Subnetworks <https://cloud.google.com/compute/docs/subnetworks>`_ for more information). A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/regions/global/default`` * ``projects/[project_id]/regions/global/default`` * ``default`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#network GoogleDataprocWorkflowTemplate#network}
        :param node_group_affinity: node_group_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#node_group_affinity GoogleDataprocWorkflowTemplate#node_group_affinity}
        :param private_ipv6_google_access: Optional. The type of IPv6 access for a cluster. Possible values: PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED, INHERIT_FROM_SUBNETWORK, OUTBOUND, BIDIRECTIONAL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#private_ipv6_google_access GoogleDataprocWorkflowTemplate#private_ipv6_google_access}
        :param reservation_affinity: reservation_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#reservation_affinity GoogleDataprocWorkflowTemplate#reservation_affinity}
        :param service_account: Optional. The `Dataproc service account <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#service_accounts_in_dataproc>`_ (also see `VM Data Plane identity <https://cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals#vm_service_account_data_plane_identity>`_) used by Dataproc cluster VM instances to access Google Cloud Platform services. If not specified, the `Compute Engine default service account <https://cloud.google.com/compute/docs/access/service-accounts#default_service_account>`_ is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#service_account GoogleDataprocWorkflowTemplate#service_account}
        :param service_account_scopes: Optional. The URIs of service account scopes to be included in Compute Engine instances. The following base set of scopes is always included: * https://www.googleapis.com/auth/cloud.useraccounts.readonly * https://www.googleapis.com/auth/devstorage.read_write * https://www.googleapis.com/auth/logging.write If no scopes are specified, the following defaults are also provided: * https://www.googleapis.com/auth/bigquery * https://www.googleapis.com/auth/bigtable.admin.table * https://www.googleapis.com/auth/bigtable.data * https://www.googleapis.com/auth/devstorage.full_control Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#service_account_scopes GoogleDataprocWorkflowTemplate#service_account_scopes}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#shielded_instance_config GoogleDataprocWorkflowTemplate#shielded_instance_config}
        :param subnetwork: Optional. The Compute Engine subnetwork to be used for machine communications. Cannot be specified with network_uri. A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/regions/us-east1/subnetworks/sub0`` * ``projects/[project_id]/regions/us-east1/subnetworks/sub0`` * ``sub0`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#subnetwork GoogleDataprocWorkflowTemplate#subnetwork}
        :param tags: The Compute Engine tags to add to all instances (see `Tagging instances <https://cloud.google.com/compute/docs/label-or-tag-resources#tags>`_). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#tags GoogleDataprocWorkflowTemplate#tags}
        :param zone: Optional. The zone where the Compute Engine cluster will be located. On a create request, it is required in the "global" region. If omitted in a non-global Dataproc region, the service will pick a zone in the corresponding Compute Engine region. On a get request, zone will always be present. A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/[zone]`` * ``projects/[project_id]/zones/[zone]`` * ``us-central1-f`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#zone GoogleDataprocWorkflowTemplate#zone}
        '''
        if isinstance(node_group_affinity, dict):
            node_group_affinity = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity(**node_group_affinity)
        if isinstance(reservation_affinity, dict):
            reservation_affinity = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity(**reservation_affinity)
        if isinstance(shielded_instance_config, dict):
            shielded_instance_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig(**shielded_instance_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig.__init__)
            check_type(argname="argument internal_ip_only", value=internal_ip_only, expected_type=type_hints["internal_ip_only"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument node_group_affinity", value=node_group_affinity, expected_type=type_hints["node_group_affinity"])
            check_type(argname="argument private_ipv6_google_access", value=private_ipv6_google_access, expected_type=type_hints["private_ipv6_google_access"])
            check_type(argname="argument reservation_affinity", value=reservation_affinity, expected_type=type_hints["reservation_affinity"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument service_account_scopes", value=service_account_scopes, expected_type=type_hints["service_account_scopes"])
            check_type(argname="argument shielded_instance_config", value=shielded_instance_config, expected_type=type_hints["shielded_instance_config"])
            check_type(argname="argument subnetwork", value=subnetwork, expected_type=type_hints["subnetwork"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[str, typing.Any] = {}
        if internal_ip_only is not None:
            self._values["internal_ip_only"] = internal_ip_only
        if metadata is not None:
            self._values["metadata"] = metadata
        if network is not None:
            self._values["network"] = network
        if node_group_affinity is not None:
            self._values["node_group_affinity"] = node_group_affinity
        if private_ipv6_google_access is not None:
            self._values["private_ipv6_google_access"] = private_ipv6_google_access
        if reservation_affinity is not None:
            self._values["reservation_affinity"] = reservation_affinity
        if service_account is not None:
            self._values["service_account"] = service_account
        if service_account_scopes is not None:
            self._values["service_account_scopes"] = service_account_scopes
        if shielded_instance_config is not None:
            self._values["shielded_instance_config"] = shielded_instance_config
        if subnetwork is not None:
            self._values["subnetwork"] = subnetwork
        if tags is not None:
            self._values["tags"] = tags
        if zone is not None:
            self._values["zone"] = zone

    @builtins.property
    def internal_ip_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional.

        If true, all instances in the cluster will only have internal IP addresses. By default, clusters are not restricted to internal IP addresses, and will have ephemeral external IP addresses assigned to each instance. This ``internal_ip_only`` restriction can only be enabled for subnetwork enabled networks, and all off-cluster dependencies must be configured to be accessible without external IP addresses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#internal_ip_only GoogleDataprocWorkflowTemplate#internal_ip_only}
        '''
        result = self._values.get("internal_ip_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The Compute Engine metadata entries to add to all instances (see `Project and instance metadata <https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata>`_).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#metadata GoogleDataprocWorkflowTemplate#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The Compute Engine network to be used for machine communications. Cannot be specified with subnetwork_uri. If neither ``network_uri`` nor ``subnetwork_uri`` is specified, the "default" network of the project is used, if it exists. Cannot be a "Custom Subnet Network" (see `Using Subnetworks <https://cloud.google.com/compute/docs/subnetworks>`_ for more information). A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/regions/global/default`` * ``projects/[project_id]/regions/global/default`` * ``default``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#network GoogleDataprocWorkflowTemplate#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_group_affinity(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity"]:
        '''node_group_affinity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#node_group_affinity GoogleDataprocWorkflowTemplate#node_group_affinity}
        '''
        result = self._values.get("node_group_affinity")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity"], result)

    @builtins.property
    def private_ipv6_google_access(self) -> typing.Optional[builtins.str]:
        '''Optional. The type of IPv6 access for a cluster. Possible values: PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED, INHERIT_FROM_SUBNETWORK, OUTBOUND, BIDIRECTIONAL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#private_ipv6_google_access GoogleDataprocWorkflowTemplate#private_ipv6_google_access}
        '''
        result = self._values.get("private_ipv6_google_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reservation_affinity(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity"]:
        '''reservation_affinity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#reservation_affinity GoogleDataprocWorkflowTemplate#reservation_affinity}
        '''
        result = self._values.get("reservation_affinity")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity"], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The `Dataproc service account <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#service_accounts_in_dataproc>`_ (also see `VM Data Plane identity <https://cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals#vm_service_account_data_plane_identity>`_) used by Dataproc cluster VM instances to access Google Cloud Platform services. If not specified, the `Compute Engine default service account <https://cloud.google.com/compute/docs/access/service-accounts#default_service_account>`_ is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#service_account GoogleDataprocWorkflowTemplate#service_account}
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_account_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        The URIs of service account scopes to be included in Compute Engine instances. The following base set of scopes is always included: * https://www.googleapis.com/auth/cloud.useraccounts.readonly * https://www.googleapis.com/auth/devstorage.read_write * https://www.googleapis.com/auth/logging.write If no scopes are specified, the following defaults are also provided: * https://www.googleapis.com/auth/bigquery * https://www.googleapis.com/auth/bigtable.admin.table * https://www.googleapis.com/auth/bigtable.data * https://www.googleapis.com/auth/devstorage.full_control

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#service_account_scopes GoogleDataprocWorkflowTemplate#service_account_scopes}
        '''
        result = self._values.get("service_account_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def shielded_instance_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig"]:
        '''shielded_instance_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#shielded_instance_config GoogleDataprocWorkflowTemplate#shielded_instance_config}
        '''
        result = self._values.get("shielded_instance_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig"], result)

    @builtins.property
    def subnetwork(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The Compute Engine subnetwork to be used for machine communications. Cannot be specified with network_uri. A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/regions/us-east1/subnetworks/sub0`` * ``projects/[project_id]/regions/us-east1/subnetworks/sub0`` * ``sub0``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#subnetwork GoogleDataprocWorkflowTemplate#subnetwork}
        '''
        result = self._values.get("subnetwork")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Compute Engine tags to add to all instances (see `Tagging instances <https://cloud.google.com/compute/docs/label-or-tag-resources#tags>`_).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#tags GoogleDataprocWorkflowTemplate#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The zone where the Compute Engine cluster will be located. On a create request, it is required in the "global" region. If omitted in a non-global Dataproc region, the service will pick a zone in the corresponding Compute Engine region. On a get request, zone will always be present. A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/[zone]`` * ``projects/[project_id]/zones/[zone]`` * ``us-central1-f``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#zone GoogleDataprocWorkflowTemplate#zone}
        '''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity",
    jsii_struct_bases=[],
    name_mapping={"node_group": "nodeGroup"},
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity:
    def __init__(self, *, node_group: builtins.str) -> None:
        '''
        :param node_group: Required. The URI of a sole-tenant `node group resource <https://cloud.google.com/compute/docs/reference/rest/v1/nodeGroups>`_ that the cluster will be created on. A full URL, partial URI, or node group name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/us-central1-a/nodeGroups/node-group-1`` * ``projects/[project_id]/zones/us-central1-a/nodeGroups/node-group-1`` * ``node-group-1`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#node_group GoogleDataprocWorkflowTemplate#node_group}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity.__init__)
            check_type(argname="argument node_group", value=node_group, expected_type=type_hints["node_group"])
        self._values: typing.Dict[str, typing.Any] = {
            "node_group": node_group,
        }

    @builtins.property
    def node_group(self) -> builtins.str:
        '''Required.

        The URI of a sole-tenant `node group resource <https://cloud.google.com/compute/docs/reference/rest/v1/nodeGroups>`_ that the cluster will be created on. A full URL, partial URI, or node group name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/us-central1-a/nodeGroups/node-group-1`` * ``projects/[project_id]/zones/us-central1-a/nodeGroups/node-group-1`` * ``node-group-1``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#node_group GoogleDataprocWorkflowTemplate#node_group}
        '''
        result = self._values.get("node_group")
        assert result is not None, "Required property 'node_group' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinityOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nodeGroupInput")
    def node_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeGroup")
    def node_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeGroup"))

    @node_group.setter
    def node_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinityOutputReference, "node_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeGroup", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNodeGroupAffinity")
    def put_node_group_affinity(self, *, node_group: builtins.str) -> None:
        '''
        :param node_group: Required. The URI of a sole-tenant `node group resource <https://cloud.google.com/compute/docs/reference/rest/v1/nodeGroups>`_ that the cluster will be created on. A full URL, partial URI, or node group name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/us-central1-a/nodeGroups/node-group-1`` * ``projects/[project_id]/zones/us-central1-a/nodeGroups/node-group-1`` * ``node-group-1`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#node_group GoogleDataprocWorkflowTemplate#node_group}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity(
            node_group=node_group
        )

        return typing.cast(None, jsii.invoke(self, "putNodeGroupAffinity", [value]))

    @jsii.member(jsii_name="putReservationAffinity")
    def put_reservation_affinity(
        self,
        *,
        consume_reservation_type: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param consume_reservation_type: Optional. Type of reservation to consume Possible values: TYPE_UNSPECIFIED, NO_RESERVATION, ANY_RESERVATION, SPECIFIC_RESERVATION. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#consume_reservation_type GoogleDataprocWorkflowTemplate#consume_reservation_type}
        :param key: Optional. Corresponds to the label key of reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#key GoogleDataprocWorkflowTemplate#key}
        :param values: Optional. Corresponds to the label values of reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#values GoogleDataprocWorkflowTemplate#values}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity(
            consume_reservation_type=consume_reservation_type, key=key, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putReservationAffinity", [value]))

    @jsii.member(jsii_name="putShieldedInstanceConfig")
    def put_shielded_instance_config(
        self,
        *,
        enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_secure_boot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_vtpm: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_integrity_monitoring: Optional. Defines whether instances have integrity monitoring enabled. Integrity monitoring compares the most recent boot measurements to the integrity policy baseline and returns a pair of pass/fail results depending on whether they match or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#enable_integrity_monitoring GoogleDataprocWorkflowTemplate#enable_integrity_monitoring}
        :param enable_secure_boot: Optional. Defines whether the instances have Secure Boot enabled. Secure Boot helps ensure that the system only runs authentic software by verifying the digital signature of all boot components, and halting the boot process if signature verification fails. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#enable_secure_boot GoogleDataprocWorkflowTemplate#enable_secure_boot}
        :param enable_vtpm: Optional. Defines whether the instance have the vTPM enabled. Virtual Trusted Platform Module protects objects like keys, certificates and enables Measured Boot by performing the measurements needed to create a known good boot baseline, called the integrity policy baseline. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#enable_vtpm GoogleDataprocWorkflowTemplate#enable_vtpm}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig(
            enable_integrity_monitoring=enable_integrity_monitoring,
            enable_secure_boot=enable_secure_boot,
            enable_vtpm=enable_vtpm,
        )

        return typing.cast(None, jsii.invoke(self, "putShieldedInstanceConfig", [value]))

    @jsii.member(jsii_name="resetInternalIpOnly")
    def reset_internal_ip_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternalIpOnly", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetNodeGroupAffinity")
    def reset_node_group_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeGroupAffinity", []))

    @jsii.member(jsii_name="resetPrivateIpv6GoogleAccess")
    def reset_private_ipv6_google_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpv6GoogleAccess", []))

    @jsii.member(jsii_name="resetReservationAffinity")
    def reset_reservation_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReservationAffinity", []))

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @jsii.member(jsii_name="resetServiceAccountScopes")
    def reset_service_account_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccountScopes", []))

    @jsii.member(jsii_name="resetShieldedInstanceConfig")
    def reset_shielded_instance_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShieldedInstanceConfig", []))

    @jsii.member(jsii_name="resetSubnetwork")
    def reset_subnetwork(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetwork", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetZone")
    def reset_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZone", []))

    @builtins.property
    @jsii.member(jsii_name="nodeGroupAffinity")
    def node_group_affinity(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinityOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinityOutputReference, jsii.get(self, "nodeGroupAffinity"))

    @builtins.property
    @jsii.member(jsii_name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityOutputReference", jsii.get(self, "reservationAffinity"))

    @builtins.property
    @jsii.member(jsii_name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference", jsii.get(self, "shieldedInstanceConfig"))

    @builtins.property
    @jsii.member(jsii_name="internalIpOnlyInput")
    def internal_ip_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "internalIpOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeGroupAffinityInput")
    def node_group_affinity_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity], jsii.get(self, "nodeGroupAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpv6GoogleAccessInput")
    def private_ipv6_google_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpv6GoogleAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="reservationAffinityInput")
    def reservation_affinity_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity"], jsii.get(self, "reservationAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountScopesInput")
    def service_account_scopes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serviceAccountScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="shieldedInstanceConfigInput")
    def shielded_instance_config_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig"], jsii.get(self, "shieldedInstanceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetworkInput")
    def subnetwork_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="internalIpOnly")
    def internal_ip_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "internalIpOnly"))

    @internal_ip_only.setter
    def internal_ip_only(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference, "internal_ip_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalIpOnly", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference, "metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpv6GoogleAccess"))

    @private_ipv6_google_access.setter
    def private_ipv6_google_access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference, "private_ipv6_google_access").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpv6GoogleAccess", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccount"))

    @service_account.setter
    def service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference, "service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccountScopes")
    def service_account_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serviceAccountScopes"))

    @service_account_scopes.setter
    def service_account_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference, "service_account_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccountScopes", value)

    @builtins.property
    @jsii.member(jsii_name="subnetwork")
    def subnetwork(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetwork"))

    @subnetwork.setter
    def subnetwork(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference, "subnetwork").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetwork", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity",
    jsii_struct_bases=[],
    name_mapping={
        "consume_reservation_type": "consumeReservationType",
        "key": "key",
        "values": "values",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity:
    def __init__(
        self,
        *,
        consume_reservation_type: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param consume_reservation_type: Optional. Type of reservation to consume Possible values: TYPE_UNSPECIFIED, NO_RESERVATION, ANY_RESERVATION, SPECIFIC_RESERVATION. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#consume_reservation_type GoogleDataprocWorkflowTemplate#consume_reservation_type}
        :param key: Optional. Corresponds to the label key of reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#key GoogleDataprocWorkflowTemplate#key}
        :param values: Optional. Corresponds to the label values of reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#values GoogleDataprocWorkflowTemplate#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity.__init__)
            check_type(argname="argument consume_reservation_type", value=consume_reservation_type, expected_type=type_hints["consume_reservation_type"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if consume_reservation_type is not None:
            self._values["consume_reservation_type"] = consume_reservation_type
        if key is not None:
            self._values["key"] = key
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def consume_reservation_type(self) -> typing.Optional[builtins.str]:
        '''Optional. Type of reservation to consume Possible values: TYPE_UNSPECIFIED, NO_RESERVATION, ANY_RESERVATION, SPECIFIC_RESERVATION.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#consume_reservation_type GoogleDataprocWorkflowTemplate#consume_reservation_type}
        '''
        result = self._values.get("consume_reservation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Optional. Corresponds to the label key of reservation resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#key GoogleDataprocWorkflowTemplate#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional. Corresponds to the label values of reservation resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#values GoogleDataprocWorkflowTemplate#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConsumeReservationType")
    def reset_consume_reservation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsumeReservationType", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="consumeReservationTypeInput")
    def consume_reservation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumeReservationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="consumeReservationType")
    def consume_reservation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumeReservationType"))

    @consume_reservation_type.setter
    def consume_reservation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityOutputReference, "consume_reservation_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumeReservationType", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "enable_integrity_monitoring": "enableIntegrityMonitoring",
        "enable_secure_boot": "enableSecureBoot",
        "enable_vtpm": "enableVtpm",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig:
    def __init__(
        self,
        *,
        enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_secure_boot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_vtpm: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_integrity_monitoring: Optional. Defines whether instances have integrity monitoring enabled. Integrity monitoring compares the most recent boot measurements to the integrity policy baseline and returns a pair of pass/fail results depending on whether they match or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#enable_integrity_monitoring GoogleDataprocWorkflowTemplate#enable_integrity_monitoring}
        :param enable_secure_boot: Optional. Defines whether the instances have Secure Boot enabled. Secure Boot helps ensure that the system only runs authentic software by verifying the digital signature of all boot components, and halting the boot process if signature verification fails. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#enable_secure_boot GoogleDataprocWorkflowTemplate#enable_secure_boot}
        :param enable_vtpm: Optional. Defines whether the instance have the vTPM enabled. Virtual Trusted Platform Module protects objects like keys, certificates and enables Measured Boot by performing the measurements needed to create a known good boot baseline, called the integrity policy baseline. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#enable_vtpm GoogleDataprocWorkflowTemplate#enable_vtpm}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig.__init__)
            check_type(argname="argument enable_integrity_monitoring", value=enable_integrity_monitoring, expected_type=type_hints["enable_integrity_monitoring"])
            check_type(argname="argument enable_secure_boot", value=enable_secure_boot, expected_type=type_hints["enable_secure_boot"])
            check_type(argname="argument enable_vtpm", value=enable_vtpm, expected_type=type_hints["enable_vtpm"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enable_integrity_monitoring is not None:
            self._values["enable_integrity_monitoring"] = enable_integrity_monitoring
        if enable_secure_boot is not None:
            self._values["enable_secure_boot"] = enable_secure_boot
        if enable_vtpm is not None:
            self._values["enable_vtpm"] = enable_vtpm

    @builtins.property
    def enable_integrity_monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional.

        Defines whether instances have integrity monitoring enabled. Integrity monitoring compares the most recent boot measurements to the integrity policy baseline and returns a pair of pass/fail results depending on whether they match or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#enable_integrity_monitoring GoogleDataprocWorkflowTemplate#enable_integrity_monitoring}
        '''
        result = self._values.get("enable_integrity_monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_secure_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional.

        Defines whether the instances have Secure Boot enabled. Secure Boot helps ensure that the system only runs authentic software by verifying the digital signature of all boot components, and halting the boot process if signature verification fails.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#enable_secure_boot GoogleDataprocWorkflowTemplate#enable_secure_boot}
        '''
        result = self._values.get("enable_secure_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_vtpm(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional.

        Defines whether the instance have the vTPM enabled. Virtual Trusted Platform Module protects objects like keys, certificates and enables Measured Boot by performing the measurements needed to create a known good boot baseline, called the integrity policy baseline.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#enable_vtpm GoogleDataprocWorkflowTemplate#enable_vtpm}
        '''
        result = self._values.get("enable_vtpm")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableIntegrityMonitoring")
    def reset_enable_integrity_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableIntegrityMonitoring", []))

    @jsii.member(jsii_name="resetEnableSecureBoot")
    def reset_enable_secure_boot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableSecureBoot", []))

    @jsii.member(jsii_name="resetEnableVtpm")
    def reset_enable_vtpm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableVtpm", []))

    @builtins.property
    @jsii.member(jsii_name="enableIntegrityMonitoringInput")
    def enable_integrity_monitoring_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableIntegrityMonitoringInput"))

    @builtins.property
    @jsii.member(jsii_name="enableSecureBootInput")
    def enable_secure_boot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableSecureBootInput"))

    @builtins.property
    @jsii.member(jsii_name="enableVtpmInput")
    def enable_vtpm_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableVtpmInput"))

    @builtins.property
    @jsii.member(jsii_name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableIntegrityMonitoring"))

    @enable_integrity_monitoring.setter
    def enable_integrity_monitoring(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference, "enable_integrity_monitoring").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIntegrityMonitoring", value)

    @builtins.property
    @jsii.member(jsii_name="enableSecureBoot")
    def enable_secure_boot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableSecureBoot"))

    @enable_secure_boot.setter
    def enable_secure_boot(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference, "enable_secure_boot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSecureBoot", value)

    @builtins.property
    @jsii.member(jsii_name="enableVtpm")
    def enable_vtpm(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableVtpm"))

    @enable_vtpm.setter
    def enable_vtpm(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference, "enable_vtpm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableVtpm", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig",
    jsii_struct_bases=[],
    name_mapping={"namespaced_gke_deployment_target": "namespacedGkeDeploymentTarget"},
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig:
    def __init__(
        self,
        *,
        namespaced_gke_deployment_target: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param namespaced_gke_deployment_target: namespaced_gke_deployment_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#namespaced_gke_deployment_target GoogleDataprocWorkflowTemplate#namespaced_gke_deployment_target}
        '''
        if isinstance(namespaced_gke_deployment_target, dict):
            namespaced_gke_deployment_target = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget(**namespaced_gke_deployment_target)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig.__init__)
            check_type(argname="argument namespaced_gke_deployment_target", value=namespaced_gke_deployment_target, expected_type=type_hints["namespaced_gke_deployment_target"])
        self._values: typing.Dict[str, typing.Any] = {}
        if namespaced_gke_deployment_target is not None:
            self._values["namespaced_gke_deployment_target"] = namespaced_gke_deployment_target

    @builtins.property
    def namespaced_gke_deployment_target(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget"]:
        '''namespaced_gke_deployment_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#namespaced_gke_deployment_target GoogleDataprocWorkflowTemplate#namespaced_gke_deployment_target}
        '''
        result = self._values.get("namespaced_gke_deployment_target")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_namespace": "clusterNamespace",
        "target_gke_cluster": "targetGkeCluster",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget:
    def __init__(
        self,
        *,
        cluster_namespace: typing.Optional[builtins.str] = None,
        target_gke_cluster: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_namespace: Optional. A namespace within the GKE cluster to deploy into. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cluster_namespace GoogleDataprocWorkflowTemplate#cluster_namespace}
        :param target_gke_cluster: Optional. The target GKE cluster to deploy to. Format: 'projects/{project}/locations/{location}/clusters/{cluster_id}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#target_gke_cluster GoogleDataprocWorkflowTemplate#target_gke_cluster}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget.__init__)
            check_type(argname="argument cluster_namespace", value=cluster_namespace, expected_type=type_hints["cluster_namespace"])
            check_type(argname="argument target_gke_cluster", value=target_gke_cluster, expected_type=type_hints["target_gke_cluster"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cluster_namespace is not None:
            self._values["cluster_namespace"] = cluster_namespace
        if target_gke_cluster is not None:
            self._values["target_gke_cluster"] = target_gke_cluster

    @builtins.property
    def cluster_namespace(self) -> typing.Optional[builtins.str]:
        '''Optional. A namespace within the GKE cluster to deploy into.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cluster_namespace GoogleDataprocWorkflowTemplate#cluster_namespace}
        '''
        result = self._values.get("cluster_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_gke_cluster(self) -> typing.Optional[builtins.str]:
        '''Optional. The target GKE cluster to deploy to. Format: 'projects/{project}/locations/{location}/clusters/{cluster_id}'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#target_gke_cluster GoogleDataprocWorkflowTemplate#target_gke_cluster}
        '''
        result = self._values.get("target_gke_cluster")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTargetOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClusterNamespace")
    def reset_cluster_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterNamespace", []))

    @jsii.member(jsii_name="resetTargetGkeCluster")
    def reset_target_gke_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetGkeCluster", []))

    @builtins.property
    @jsii.member(jsii_name="clusterNamespaceInput")
    def cluster_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGkeClusterInput")
    def target_gke_cluster_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetGkeClusterInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterNamespace")
    def cluster_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterNamespace"))

    @cluster_namespace.setter
    def cluster_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTargetOutputReference, "cluster_namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="targetGkeCluster")
    def target_gke_cluster(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetGkeCluster"))

    @target_gke_cluster.setter
    def target_gke_cluster(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTargetOutputReference, "target_gke_cluster").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetGkeCluster", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNamespacedGkeDeploymentTarget")
    def put_namespaced_gke_deployment_target(
        self,
        *,
        cluster_namespace: typing.Optional[builtins.str] = None,
        target_gke_cluster: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_namespace: Optional. A namespace within the GKE cluster to deploy into. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cluster_namespace GoogleDataprocWorkflowTemplate#cluster_namespace}
        :param target_gke_cluster: Optional. The target GKE cluster to deploy to. Format: 'projects/{project}/locations/{location}/clusters/{cluster_id}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#target_gke_cluster GoogleDataprocWorkflowTemplate#target_gke_cluster}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget(
            cluster_namespace=cluster_namespace, target_gke_cluster=target_gke_cluster
        )

        return typing.cast(None, jsii.invoke(self, "putNamespacedGkeDeploymentTarget", [value]))

    @jsii.member(jsii_name="resetNamespacedGkeDeploymentTarget")
    def reset_namespaced_gke_deployment_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespacedGkeDeploymentTarget", []))

    @builtins.property
    @jsii.member(jsii_name="namespacedGkeDeploymentTarget")
    def namespaced_gke_deployment_target(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTargetOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTargetOutputReference, jsii.get(self, "namespacedGkeDeploymentTarget"))

    @builtins.property
    @jsii.member(jsii_name="namespacedGkeDeploymentTargetInput")
    def namespaced_gke_deployment_target_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget], jsii.get(self, "namespacedGkeDeploymentTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions",
    jsii_struct_bases=[],
    name_mapping={
        "executable_file": "executableFile",
        "execution_timeout": "executionTimeout",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions:
    def __init__(
        self,
        *,
        executable_file: typing.Optional[builtins.str] = None,
        execution_timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param executable_file: Required. Cloud Storage URI of executable file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#executable_file GoogleDataprocWorkflowTemplate#executable_file}
        :param execution_timeout: Optional. Amount of time executable has to complete. Default is 10 minutes (see JSON representation of `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`_). Cluster creation fails with an explanatory error message (the name of the executable that caused the error and the exceeded timeout period) if the executable is not completed at end of the timeout period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#execution_timeout GoogleDataprocWorkflowTemplate#execution_timeout}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions.__init__)
            check_type(argname="argument executable_file", value=executable_file, expected_type=type_hints["executable_file"])
            check_type(argname="argument execution_timeout", value=execution_timeout, expected_type=type_hints["execution_timeout"])
        self._values: typing.Dict[str, typing.Any] = {}
        if executable_file is not None:
            self._values["executable_file"] = executable_file
        if execution_timeout is not None:
            self._values["execution_timeout"] = execution_timeout

    @builtins.property
    def executable_file(self) -> typing.Optional[builtins.str]:
        '''Required. Cloud Storage URI of executable file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#executable_file GoogleDataprocWorkflowTemplate#executable_file}
        '''
        result = self._values.get("executable_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_timeout(self) -> typing.Optional[builtins.str]:
        '''Optional.

        Amount of time executable has to complete. Default is 10 minutes (see JSON representation of `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`_). Cluster creation fails with an explanatory error message (the name of the executable that caused the error and the exceeded timeout period) if the executable is not completed at end of the timeout period.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#execution_timeout GoogleDataprocWorkflowTemplate#execution_timeout}
        '''
        result = self._values.get("execution_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsList",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExecutableFile")
    def reset_executable_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutableFile", []))

    @jsii.member(jsii_name="resetExecutionTimeout")
    def reset_execution_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="executableFileInput")
    def executable_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executableFileInput"))

    @builtins.property
    @jsii.member(jsii_name="executionTimeoutInput")
    def execution_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="executableFile")
    def executable_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executableFile"))

    @executable_file.setter
    def executable_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsOutputReference, "executable_file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executableFile", value)

    @builtins.property
    @jsii.member(jsii_name="executionTimeout")
    def execution_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionTimeout"))

    @execution_timeout.setter
    def execution_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsOutputReference, "execution_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig",
    jsii_struct_bases=[],
    name_mapping={
        "auto_delete_time": "autoDeleteTime",
        "auto_delete_ttl": "autoDeleteTtl",
        "idle_delete_ttl": "idleDeleteTtl",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig:
    def __init__(
        self,
        *,
        auto_delete_time: typing.Optional[builtins.str] = None,
        auto_delete_ttl: typing.Optional[builtins.str] = None,
        idle_delete_ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_delete_time: Optional. The time when cluster will be auto-deleted (see JSON representation of `Timestamp <https://developers.google.com/protocol-buffers/docs/proto3#json>`_). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#auto_delete_time GoogleDataprocWorkflowTemplate#auto_delete_time}
        :param auto_delete_ttl: Optional. The lifetime duration of cluster. The cluster will be auto-deleted at the end of this period. Minimum value is 10 minutes; maximum value is 14 days (see JSON representation of `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`_). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#auto_delete_ttl GoogleDataprocWorkflowTemplate#auto_delete_ttl}
        :param idle_delete_ttl: Optional. The duration to keep the cluster alive while idling (when no jobs are running). Passing this threshold will cause the cluster to be deleted. Minimum value is 5 minutes; maximum value is 14 days (see JSON representation of `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`_). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#idle_delete_ttl GoogleDataprocWorkflowTemplate#idle_delete_ttl}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig.__init__)
            check_type(argname="argument auto_delete_time", value=auto_delete_time, expected_type=type_hints["auto_delete_time"])
            check_type(argname="argument auto_delete_ttl", value=auto_delete_ttl, expected_type=type_hints["auto_delete_ttl"])
            check_type(argname="argument idle_delete_ttl", value=idle_delete_ttl, expected_type=type_hints["idle_delete_ttl"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_delete_time is not None:
            self._values["auto_delete_time"] = auto_delete_time
        if auto_delete_ttl is not None:
            self._values["auto_delete_ttl"] = auto_delete_ttl
        if idle_delete_ttl is not None:
            self._values["idle_delete_ttl"] = idle_delete_ttl

    @builtins.property
    def auto_delete_time(self) -> typing.Optional[builtins.str]:
        '''Optional. The time when cluster will be auto-deleted (see JSON representation of `Timestamp <https://developers.google.com/protocol-buffers/docs/proto3#json>`_).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#auto_delete_time GoogleDataprocWorkflowTemplate#auto_delete_time}
        '''
        result = self._values.get("auto_delete_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_delete_ttl(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The lifetime duration of cluster. The cluster will be auto-deleted at the end of this period. Minimum value is 10 minutes; maximum value is 14 days (see JSON representation of `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`_).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#auto_delete_ttl GoogleDataprocWorkflowTemplate#auto_delete_ttl}
        '''
        result = self._values.get("auto_delete_ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idle_delete_ttl(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The duration to keep the cluster alive while idling (when no jobs are running). Passing this threshold will cause the cluster to be deleted. Minimum value is 5 minutes; maximum value is 14 days (see JSON representation of `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`_).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#idle_delete_ttl GoogleDataprocWorkflowTemplate#idle_delete_ttl}
        '''
        result = self._values.get("idle_delete_ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAutoDeleteTime")
    def reset_auto_delete_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoDeleteTime", []))

    @jsii.member(jsii_name="resetAutoDeleteTtl")
    def reset_auto_delete_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoDeleteTtl", []))

    @jsii.member(jsii_name="resetIdleDeleteTtl")
    def reset_idle_delete_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleDeleteTtl", []))

    @builtins.property
    @jsii.member(jsii_name="idleStartTime")
    def idle_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idleStartTime"))

    @builtins.property
    @jsii.member(jsii_name="autoDeleteTimeInput")
    def auto_delete_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoDeleteTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="autoDeleteTtlInput")
    def auto_delete_ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoDeleteTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="idleDeleteTtlInput")
    def idle_delete_ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idleDeleteTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="autoDeleteTime")
    def auto_delete_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoDeleteTime"))

    @auto_delete_time.setter
    def auto_delete_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfigOutputReference, "auto_delete_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoDeleteTime", value)

    @builtins.property
    @jsii.member(jsii_name="autoDeleteTtl")
    def auto_delete_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoDeleteTtl"))

    @auto_delete_ttl.setter
    def auto_delete_ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfigOutputReference, "auto_delete_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoDeleteTtl", value)

    @builtins.property
    @jsii.member(jsii_name="idleDeleteTtl")
    def idle_delete_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idleDeleteTtl"))

    @idle_delete_ttl.setter
    def idle_delete_ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfigOutputReference, "idle_delete_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleDeleteTtl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig",
    jsii_struct_bases=[],
    name_mapping={
        "accelerators": "accelerators",
        "disk_config": "diskConfig",
        "image": "image",
        "machine_type": "machineType",
        "min_cpu_platform": "minCpuPlatform",
        "num_instances": "numInstances",
        "preemptibility": "preemptibility",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig:
    def __init__(
        self,
        *,
        accelerators: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators", typing.Dict[str, typing.Any]]]]] = None,
        disk_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig", typing.Dict[str, typing.Any]]] = None,
        image: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        num_instances: typing.Optional[jsii.Number] = None,
        preemptibility: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param accelerators: accelerators block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerators GoogleDataprocWorkflowTemplate#accelerators}
        :param disk_config: disk_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#disk_config GoogleDataprocWorkflowTemplate#disk_config}
        :param image: Optional. The Compute Engine image resource used for cluster instances. The URI can represent an image or image family. Image examples: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/[image-id]`` * ``projects/[project_id]/global/images/[image-id]`` * ``image-id`` Image family examples. Dataproc will use the most recent image from the family: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/family/[custom-image-family-name]`` * ``projects/[project_id]/global/images/family/[custom-image-family-name]`` If the URI is unspecified, it will be inferred from ``SoftwareConfig.image_version`` or the system default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#image GoogleDataprocWorkflowTemplate#image}
        :param machine_type: Optional. The Compute Engine machine type used for cluster instances. A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``n1-standard-2`` **Auto Zone Exception**: If you are using the Dataproc `Auto Zone Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`_ feature, you must use the short name of the machine type resource, for example, ``n1-standard-2``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#machine_type GoogleDataprocWorkflowTemplate#machine_type}
        :param min_cpu_platform: Optional. Specifies the minimum cpu platform for the Instance Group. See `Dataproc -> Minimum CPU Platform <https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-min-cpu>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#min_cpu_platform GoogleDataprocWorkflowTemplate#min_cpu_platform}
        :param num_instances: Optional. The number of VM instances in the instance group. For `HA cluster </dataproc/docs/concepts/configuring-clusters/high-availability>`_ `master_config <#FIELDS.master_config>`_ groups, **must be set to 3**. For standard cluster `master_config <#FIELDS.master_config>`_ groups, **must be set to 1**. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_instances GoogleDataprocWorkflowTemplate#num_instances}
        :param preemptibility: Optional. Specifies the preemptibility of the instance group. The default value for master and worker groups is ``NON_PREEMPTIBLE``. This default cannot be changed. The default value for secondary instances is ``PREEMPTIBLE``. Possible values: PREEMPTIBILITY_UNSPECIFIED, NON_PREEMPTIBLE, PREEMPTIBLE Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#preemptibility GoogleDataprocWorkflowTemplate#preemptibility}
        '''
        if isinstance(disk_config, dict):
            disk_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig(**disk_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig.__init__)
            check_type(argname="argument accelerators", value=accelerators, expected_type=type_hints["accelerators"])
            check_type(argname="argument disk_config", value=disk_config, expected_type=type_hints["disk_config"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            check_type(argname="argument min_cpu_platform", value=min_cpu_platform, expected_type=type_hints["min_cpu_platform"])
            check_type(argname="argument num_instances", value=num_instances, expected_type=type_hints["num_instances"])
            check_type(argname="argument preemptibility", value=preemptibility, expected_type=type_hints["preemptibility"])
        self._values: typing.Dict[str, typing.Any] = {}
        if accelerators is not None:
            self._values["accelerators"] = accelerators
        if disk_config is not None:
            self._values["disk_config"] = disk_config
        if image is not None:
            self._values["image"] = image
        if machine_type is not None:
            self._values["machine_type"] = machine_type
        if min_cpu_platform is not None:
            self._values["min_cpu_platform"] = min_cpu_platform
        if num_instances is not None:
            self._values["num_instances"] = num_instances
        if preemptibility is not None:
            self._values["preemptibility"] = preemptibility

    @builtins.property
    def accelerators(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators"]]]:
        '''accelerators block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerators GoogleDataprocWorkflowTemplate#accelerators}
        '''
        result = self._values.get("accelerators")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators"]]], result)

    @builtins.property
    def disk_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig"]:
        '''disk_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#disk_config GoogleDataprocWorkflowTemplate#disk_config}
        '''
        result = self._values.get("disk_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig"], result)

    @builtins.property
    def image(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The Compute Engine image resource used for cluster instances. The URI can represent an image or image family. Image examples: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/[image-id]`` * ``projects/[project_id]/global/images/[image-id]`` * ``image-id`` Image family examples. Dataproc will use the most recent image from the family: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/family/[custom-image-family-name]`` * ``projects/[project_id]/global/images/family/[custom-image-family-name]`` If the URI is unspecified, it will be inferred from ``SoftwareConfig.image_version`` or the system default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#image GoogleDataprocWorkflowTemplate#image}
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def machine_type(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The Compute Engine machine type used for cluster instances. A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``n1-standard-2`` **Auto Zone Exception**: If you are using the Dataproc `Auto Zone Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`_ feature, you must use the short name of the machine type resource, for example, ``n1-standard-2``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#machine_type GoogleDataprocWorkflowTemplate#machine_type}
        '''
        result = self._values.get("machine_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_cpu_platform(self) -> typing.Optional[builtins.str]:
        '''Optional. Specifies the minimum cpu platform for the Instance Group. See `Dataproc -> Minimum CPU Platform <https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-min-cpu>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#min_cpu_platform GoogleDataprocWorkflowTemplate#min_cpu_platform}
        '''
        result = self._values.get("min_cpu_platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_instances(self) -> typing.Optional[jsii.Number]:
        '''Optional.

        The number of VM instances in the instance group. For `HA cluster </dataproc/docs/concepts/configuring-clusters/high-availability>`_ `master_config <#FIELDS.master_config>`_ groups, **must be set to 3**. For standard cluster `master_config <#FIELDS.master_config>`_ groups, **must be set to 1**.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_instances GoogleDataprocWorkflowTemplate#num_instances}
        '''
        result = self._values.get("num_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preemptibility(self) -> typing.Optional[builtins.str]:
        '''Optional.

        Specifies the preemptibility of the instance group. The default value for master and worker groups is ``NON_PREEMPTIBLE``. This default cannot be changed. The default value for secondary instances is ``PREEMPTIBLE``. Possible values: PREEMPTIBILITY_UNSPECIFIED, NON_PREEMPTIBLE, PREEMPTIBLE

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#preemptibility GoogleDataprocWorkflowTemplate#preemptibility}
        '''
        result = self._values.get("preemptibility")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators",
    jsii_struct_bases=[],
    name_mapping={
        "accelerator_count": "acceleratorCount",
        "accelerator_type": "acceleratorType",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators:
    def __init__(
        self,
        *,
        accelerator_count: typing.Optional[jsii.Number] = None,
        accelerator_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param accelerator_count: The number of the accelerator cards of this type exposed to this instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerator_count GoogleDataprocWorkflowTemplate#accelerator_count}
        :param accelerator_type: Full URL, partial URI, or short name of the accelerator type resource to expose to this instance. See `Compute Engine AcceleratorTypes <https://cloud.google.com/compute/docs/reference/beta/acceleratorTypes>`_. Examples: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/zones/us-east1-a/acceleratorTypes/nvidia-tesla-k80`` * ``projects/[project_id]/zones/us-east1-a/acceleratorTypes/nvidia-tesla-k80`` * ``nvidia-tesla-k80`` **Auto Zone Exception**: If you are using the Dataproc `Auto Zone Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`_ feature, you must use the short name of the accelerator type resource, for example, ``nvidia-tesla-k80``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerator_type GoogleDataprocWorkflowTemplate#accelerator_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators.__init__)
            check_type(argname="argument accelerator_count", value=accelerator_count, expected_type=type_hints["accelerator_count"])
            check_type(argname="argument accelerator_type", value=accelerator_type, expected_type=type_hints["accelerator_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if accelerator_count is not None:
            self._values["accelerator_count"] = accelerator_count
        if accelerator_type is not None:
            self._values["accelerator_type"] = accelerator_type

    @builtins.property
    def accelerator_count(self) -> typing.Optional[jsii.Number]:
        '''The number of the accelerator cards of this type exposed to this instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerator_count GoogleDataprocWorkflowTemplate#accelerator_count}
        '''
        result = self._values.get("accelerator_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def accelerator_type(self) -> typing.Optional[builtins.str]:
        '''Full URL, partial URI, or short name of the accelerator type resource to expose to this instance.

        See `Compute Engine AcceleratorTypes <https://cloud.google.com/compute/docs/reference/beta/acceleratorTypes>`_. Examples: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/zones/us-east1-a/acceleratorTypes/nvidia-tesla-k80`` * ``projects/[project_id]/zones/us-east1-a/acceleratorTypes/nvidia-tesla-k80`` * ``nvidia-tesla-k80`` **Auto Zone Exception**: If you are using the Dataproc `Auto Zone Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`_ feature, you must use the short name of the accelerator type resource, for example, ``nvidia-tesla-k80``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerator_type GoogleDataprocWorkflowTemplate#accelerator_type}
        '''
        result = self._values.get("accelerator_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsList",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAcceleratorCount")
    def reset_accelerator_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorCount", []))

    @jsii.member(jsii_name="resetAcceleratorType")
    def reset_accelerator_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorType", []))

    @builtins.property
    @jsii.member(jsii_name="acceleratorCountInput")
    def accelerator_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "acceleratorCountInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTypeInput")
    def accelerator_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceleratorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorCount")
    def accelerator_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "acceleratorCount"))

    @accelerator_count.setter
    def accelerator_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsOutputReference, "accelerator_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorCount", value)

    @builtins.property
    @jsii.member(jsii_name="acceleratorType")
    def accelerator_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acceleratorType"))

    @accelerator_type.setter
    def accelerator_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsOutputReference, "accelerator_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig",
    jsii_struct_bases=[],
    name_mapping={
        "boot_disk_size_gb": "bootDiskSizeGb",
        "boot_disk_type": "bootDiskType",
        "num_local_ssds": "numLocalSsds",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig:
    def __init__(
        self,
        *,
        boot_disk_size_gb: typing.Optional[jsii.Number] = None,
        boot_disk_type: typing.Optional[builtins.str] = None,
        num_local_ssds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param boot_disk_size_gb: Optional. Size in GB of the boot disk (default is 500GB). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_size_gb GoogleDataprocWorkflowTemplate#boot_disk_size_gb}
        :param boot_disk_type: Optional. Type of the boot disk (default is "pd-standard"). Valid values: "pd-balanced" (Persistent Disk Balanced Solid State Drive), "pd-ssd" (Persistent Disk Solid State Drive), or "pd-standard" (Persistent Disk Hard Disk Drive). See `Disk types <https://cloud.google.com/compute/docs/disks#disk-types>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_type GoogleDataprocWorkflowTemplate#boot_disk_type}
        :param num_local_ssds: Optional. Number of attached SSDs, from 0 to 4 (default is 0). If SSDs are not attached, the boot disk is used to store runtime logs and `HDFS <https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html>`_ data. If one or more SSDs are attached, this runtime bulk data is spread across them, and the boot disk contains only basic config and installed binaries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_local_ssds GoogleDataprocWorkflowTemplate#num_local_ssds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig.__init__)
            check_type(argname="argument boot_disk_size_gb", value=boot_disk_size_gb, expected_type=type_hints["boot_disk_size_gb"])
            check_type(argname="argument boot_disk_type", value=boot_disk_type, expected_type=type_hints["boot_disk_type"])
            check_type(argname="argument num_local_ssds", value=num_local_ssds, expected_type=type_hints["num_local_ssds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if boot_disk_size_gb is not None:
            self._values["boot_disk_size_gb"] = boot_disk_size_gb
        if boot_disk_type is not None:
            self._values["boot_disk_type"] = boot_disk_type
        if num_local_ssds is not None:
            self._values["num_local_ssds"] = num_local_ssds

    @builtins.property
    def boot_disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Optional. Size in GB of the boot disk (default is 500GB).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_size_gb GoogleDataprocWorkflowTemplate#boot_disk_size_gb}
        '''
        result = self._values.get("boot_disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def boot_disk_type(self) -> typing.Optional[builtins.str]:
        '''Optional.

        Type of the boot disk (default is "pd-standard"). Valid values: "pd-balanced" (Persistent Disk Balanced Solid State Drive), "pd-ssd" (Persistent Disk Solid State Drive), or "pd-standard" (Persistent Disk Hard Disk Drive). See `Disk types <https://cloud.google.com/compute/docs/disks#disk-types>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_type GoogleDataprocWorkflowTemplate#boot_disk_type}
        '''
        result = self._values.get("boot_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_local_ssds(self) -> typing.Optional[jsii.Number]:
        '''Optional.

        Number of attached SSDs, from 0 to 4 (default is 0). If SSDs are not attached, the boot disk is used to store runtime logs and `HDFS <https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html>`_ data. If one or more SSDs are attached, this runtime bulk data is spread across them, and the boot disk contains only basic config and installed binaries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_local_ssds GoogleDataprocWorkflowTemplate#num_local_ssds}
        '''
        result = self._values.get("num_local_ssds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBootDiskSizeGb")
    def reset_boot_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskSizeGb", []))

    @jsii.member(jsii_name="resetBootDiskType")
    def reset_boot_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskType", []))

    @jsii.member(jsii_name="resetNumLocalSsds")
    def reset_num_local_ssds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumLocalSsds", []))

    @builtins.property
    @jsii.member(jsii_name="bootDiskSizeGbInput")
    def boot_disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bootDiskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskTypeInput")
    def boot_disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootDiskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="numLocalSsdsInput")
    def num_local_ssds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numLocalSsdsInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bootDiskSizeGb"))

    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigOutputReference, "boot_disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="bootDiskType")
    def boot_disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootDiskType"))

    @boot_disk_type.setter
    def boot_disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigOutputReference, "boot_disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskType", value)

    @builtins.property
    @jsii.member(jsii_name="numLocalSsds")
    def num_local_ssds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numLocalSsds"))

    @num_local_ssds.setter
    def num_local_ssds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigOutputReference, "num_local_ssds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numLocalSsds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfig",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfig:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigList",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="instanceGroupManagerName")
    def instance_group_manager_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceGroupManagerName"))

    @builtins.property
    @jsii.member(jsii_name="instanceTemplateName")
    def instance_template_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceTemplateName"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAccelerators")
    def put_accelerators(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigOutputReference.put_accelerators)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccelerators", [value]))

    @jsii.member(jsii_name="putDiskConfig")
    def put_disk_config(
        self,
        *,
        boot_disk_size_gb: typing.Optional[jsii.Number] = None,
        boot_disk_type: typing.Optional[builtins.str] = None,
        num_local_ssds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param boot_disk_size_gb: Optional. Size in GB of the boot disk (default is 500GB). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_size_gb GoogleDataprocWorkflowTemplate#boot_disk_size_gb}
        :param boot_disk_type: Optional. Type of the boot disk (default is "pd-standard"). Valid values: "pd-balanced" (Persistent Disk Balanced Solid State Drive), "pd-ssd" (Persistent Disk Solid State Drive), or "pd-standard" (Persistent Disk Hard Disk Drive). See `Disk types <https://cloud.google.com/compute/docs/disks#disk-types>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_type GoogleDataprocWorkflowTemplate#boot_disk_type}
        :param num_local_ssds: Optional. Number of attached SSDs, from 0 to 4 (default is 0). If SSDs are not attached, the boot disk is used to store runtime logs and `HDFS <https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html>`_ data. If one or more SSDs are attached, this runtime bulk data is spread across them, and the boot disk contains only basic config and installed binaries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_local_ssds GoogleDataprocWorkflowTemplate#num_local_ssds}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig(
            boot_disk_size_gb=boot_disk_size_gb,
            boot_disk_type=boot_disk_type,
            num_local_ssds=num_local_ssds,
        )

        return typing.cast(None, jsii.invoke(self, "putDiskConfig", [value]))

    @jsii.member(jsii_name="resetAccelerators")
    def reset_accelerators(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccelerators", []))

    @jsii.member(jsii_name="resetDiskConfig")
    def reset_disk_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskConfig", []))

    @jsii.member(jsii_name="resetImage")
    def reset_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImage", []))

    @jsii.member(jsii_name="resetMachineType")
    def reset_machine_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineType", []))

    @jsii.member(jsii_name="resetMinCpuPlatform")
    def reset_min_cpu_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCpuPlatform", []))

    @jsii.member(jsii_name="resetNumInstances")
    def reset_num_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumInstances", []))

    @jsii.member(jsii_name="resetPreemptibility")
    def reset_preemptibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreemptibility", []))

    @builtins.property
    @jsii.member(jsii_name="accelerators")
    def accelerators(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsList:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsList, jsii.get(self, "accelerators"))

    @builtins.property
    @jsii.member(jsii_name="diskConfig")
    def disk_config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigOutputReference, jsii.get(self, "diskConfig"))

    @builtins.property
    @jsii.member(jsii_name="instanceNames")
    def instance_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceNames"))

    @builtins.property
    @jsii.member(jsii_name="isPreemptible")
    def is_preemptible(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "isPreemptible"))

    @builtins.property
    @jsii.member(jsii_name="managedGroupConfig")
    def managed_group_config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigList:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigList, jsii.get(self, "managedGroupConfig"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorsInput")
    def accelerators_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators]]], jsii.get(self, "acceleratorsInput"))

    @builtins.property
    @jsii.member(jsii_name="diskConfigInput")
    def disk_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig], jsii.get(self, "diskConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatformInput")
    def min_cpu_platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minCpuPlatformInput"))

    @builtins.property
    @jsii.member(jsii_name="numInstancesInput")
    def num_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="preemptibilityInput")
    def preemptibility_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preemptibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigOutputReference, "image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "image", value)

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigOutputReference, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatform")
    def min_cpu_platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minCpuPlatform"))

    @min_cpu_platform.setter
    def min_cpu_platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigOutputReference, "min_cpu_platform").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCpuPlatform", value)

    @builtins.property
    @jsii.member(jsii_name="numInstances")
    def num_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numInstances"))

    @num_instances.setter
    def num_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigOutputReference, "num_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numInstances", value)

    @builtins.property
    @jsii.member(jsii_name="preemptibility")
    def preemptibility(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preemptibility"))

    @preemptibility.setter
    def preemptibility(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigOutputReference, "preemptibility").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preemptibility", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig",
    jsii_struct_bases=[],
    name_mapping={"dataproc_metastore_service": "dataprocMetastoreService"},
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig:
    def __init__(self, *, dataproc_metastore_service: builtins.str) -> None:
        '''
        :param dataproc_metastore_service: Required. Resource name of an existing Dataproc Metastore service. Example: * ``projects/[project_id]/locations/[dataproc_region]/services/[service-name]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#dataproc_metastore_service GoogleDataprocWorkflowTemplate#dataproc_metastore_service}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig.__init__)
            check_type(argname="argument dataproc_metastore_service", value=dataproc_metastore_service, expected_type=type_hints["dataproc_metastore_service"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataproc_metastore_service": dataproc_metastore_service,
        }

    @builtins.property
    def dataproc_metastore_service(self) -> builtins.str:
        '''Required. Resource name of an existing Dataproc Metastore service. Example: * ``projects/[project_id]/locations/[dataproc_region]/services/[service-name]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#dataproc_metastore_service GoogleDataprocWorkflowTemplate#dataproc_metastore_service}
        '''
        result = self._values.get("dataproc_metastore_service")
        assert result is not None, "Required property 'dataproc_metastore_service' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dataprocMetastoreServiceInput")
    def dataproc_metastore_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataprocMetastoreServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="dataprocMetastoreService")
    def dataproc_metastore_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataprocMetastoreService"))

    @dataproc_metastore_service.setter
    def dataproc_metastore_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfigOutputReference, "dataproc_metastore_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataprocMetastoreService", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutoscalingConfig")
    def put_autoscaling_config(
        self,
        *,
        policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param policy: Optional. The autoscaling policy used by the cluster. Only resource names including projectid and location (region) are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/locations/[dataproc_region]/autoscalingPolicies/[policy_id]`` * ``projects/[project_id]/locations/[dataproc_region]/autoscalingPolicies/[policy_id]`` Note that the policy must be in the same project and Dataproc region. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#policy GoogleDataprocWorkflowTemplate#policy}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig(
            policy=policy
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscalingConfig", [value]))

    @jsii.member(jsii_name="putEncryptionConfig")
    def put_encryption_config(
        self,
        *,
        gce_pd_kms_key_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param gce_pd_kms_key_name: Optional. The Cloud KMS key name to use for PD disk encryption for all instances in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#gce_pd_kms_key_name GoogleDataprocWorkflowTemplate#gce_pd_kms_key_name}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig(
            gce_pd_kms_key_name=gce_pd_kms_key_name
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptionConfig", [value]))

    @jsii.member(jsii_name="putEndpointConfig")
    def put_endpoint_config(
        self,
        *,
        enable_http_port_access: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_http_port_access: Optional. If true, enable http access to specific ports on the cluster from external sources. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#enable_http_port_access GoogleDataprocWorkflowTemplate#enable_http_port_access}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig(
            enable_http_port_access=enable_http_port_access
        )

        return typing.cast(None, jsii.invoke(self, "putEndpointConfig", [value]))

    @jsii.member(jsii_name="putGceClusterConfig")
    def put_gce_cluster_config(
        self,
        *,
        internal_ip_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        network: typing.Optional[builtins.str] = None,
        node_group_affinity: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity, typing.Dict[str, typing.Any]]] = None,
        private_ipv6_google_access: typing.Optional[builtins.str] = None,
        reservation_affinity: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity, typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[builtins.str] = None,
        service_account_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        shielded_instance_config: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig, typing.Dict[str, typing.Any]]] = None,
        subnetwork: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param internal_ip_only: Optional. If true, all instances in the cluster will only have internal IP addresses. By default, clusters are not restricted to internal IP addresses, and will have ephemeral external IP addresses assigned to each instance. This ``internal_ip_only`` restriction can only be enabled for subnetwork enabled networks, and all off-cluster dependencies must be configured to be accessible without external IP addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#internal_ip_only GoogleDataprocWorkflowTemplate#internal_ip_only}
        :param metadata: The Compute Engine metadata entries to add to all instances (see `Project and instance metadata <https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata>`_). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#metadata GoogleDataprocWorkflowTemplate#metadata}
        :param network: Optional. The Compute Engine network to be used for machine communications. Cannot be specified with subnetwork_uri. If neither ``network_uri`` nor ``subnetwork_uri`` is specified, the "default" network of the project is used, if it exists. Cannot be a "Custom Subnet Network" (see `Using Subnetworks <https://cloud.google.com/compute/docs/subnetworks>`_ for more information). A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/regions/global/default`` * ``projects/[project_id]/regions/global/default`` * ``default`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#network GoogleDataprocWorkflowTemplate#network}
        :param node_group_affinity: node_group_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#node_group_affinity GoogleDataprocWorkflowTemplate#node_group_affinity}
        :param private_ipv6_google_access: Optional. The type of IPv6 access for a cluster. Possible values: PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED, INHERIT_FROM_SUBNETWORK, OUTBOUND, BIDIRECTIONAL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#private_ipv6_google_access GoogleDataprocWorkflowTemplate#private_ipv6_google_access}
        :param reservation_affinity: reservation_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#reservation_affinity GoogleDataprocWorkflowTemplate#reservation_affinity}
        :param service_account: Optional. The `Dataproc service account <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#service_accounts_in_dataproc>`_ (also see `VM Data Plane identity <https://cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals#vm_service_account_data_plane_identity>`_) used by Dataproc cluster VM instances to access Google Cloud Platform services. If not specified, the `Compute Engine default service account <https://cloud.google.com/compute/docs/access/service-accounts#default_service_account>`_ is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#service_account GoogleDataprocWorkflowTemplate#service_account}
        :param service_account_scopes: Optional. The URIs of service account scopes to be included in Compute Engine instances. The following base set of scopes is always included: * https://www.googleapis.com/auth/cloud.useraccounts.readonly * https://www.googleapis.com/auth/devstorage.read_write * https://www.googleapis.com/auth/logging.write If no scopes are specified, the following defaults are also provided: * https://www.googleapis.com/auth/bigquery * https://www.googleapis.com/auth/bigtable.admin.table * https://www.googleapis.com/auth/bigtable.data * https://www.googleapis.com/auth/devstorage.full_control Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#service_account_scopes GoogleDataprocWorkflowTemplate#service_account_scopes}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#shielded_instance_config GoogleDataprocWorkflowTemplate#shielded_instance_config}
        :param subnetwork: Optional. The Compute Engine subnetwork to be used for machine communications. Cannot be specified with network_uri. A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/regions/us-east1/subnetworks/sub0`` * ``projects/[project_id]/regions/us-east1/subnetworks/sub0`` * ``sub0`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#subnetwork GoogleDataprocWorkflowTemplate#subnetwork}
        :param tags: The Compute Engine tags to add to all instances (see `Tagging instances <https://cloud.google.com/compute/docs/label-or-tag-resources#tags>`_). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#tags GoogleDataprocWorkflowTemplate#tags}
        :param zone: Optional. The zone where the Compute Engine cluster will be located. On a create request, it is required in the "global" region. If omitted in a non-global Dataproc region, the service will pick a zone in the corresponding Compute Engine region. On a get request, zone will always be present. A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/[zone]`` * ``projects/[project_id]/zones/[zone]`` * ``us-central1-f`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#zone GoogleDataprocWorkflowTemplate#zone}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig(
            internal_ip_only=internal_ip_only,
            metadata=metadata,
            network=network,
            node_group_affinity=node_group_affinity,
            private_ipv6_google_access=private_ipv6_google_access,
            reservation_affinity=reservation_affinity,
            service_account=service_account,
            service_account_scopes=service_account_scopes,
            shielded_instance_config=shielded_instance_config,
            subnetwork=subnetwork,
            tags=tags,
            zone=zone,
        )

        return typing.cast(None, jsii.invoke(self, "putGceClusterConfig", [value]))

    @jsii.member(jsii_name="putGkeClusterConfig")
    def put_gke_cluster_config(
        self,
        *,
        namespaced_gke_deployment_target: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param namespaced_gke_deployment_target: namespaced_gke_deployment_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#namespaced_gke_deployment_target GoogleDataprocWorkflowTemplate#namespaced_gke_deployment_target}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig(
            namespaced_gke_deployment_target=namespaced_gke_deployment_target
        )

        return typing.cast(None, jsii.invoke(self, "putGkeClusterConfig", [value]))

    @jsii.member(jsii_name="putInitializationActions")
    def put_initialization_actions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigOutputReference.put_initialization_actions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInitializationActions", [value]))

    @jsii.member(jsii_name="putLifecycleConfig")
    def put_lifecycle_config(
        self,
        *,
        auto_delete_time: typing.Optional[builtins.str] = None,
        auto_delete_ttl: typing.Optional[builtins.str] = None,
        idle_delete_ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_delete_time: Optional. The time when cluster will be auto-deleted (see JSON representation of `Timestamp <https://developers.google.com/protocol-buffers/docs/proto3#json>`_). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#auto_delete_time GoogleDataprocWorkflowTemplate#auto_delete_time}
        :param auto_delete_ttl: Optional. The lifetime duration of cluster. The cluster will be auto-deleted at the end of this period. Minimum value is 10 minutes; maximum value is 14 days (see JSON representation of `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`_). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#auto_delete_ttl GoogleDataprocWorkflowTemplate#auto_delete_ttl}
        :param idle_delete_ttl: Optional. The duration to keep the cluster alive while idling (when no jobs are running). Passing this threshold will cause the cluster to be deleted. Minimum value is 5 minutes; maximum value is 14 days (see JSON representation of `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`_). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#idle_delete_ttl GoogleDataprocWorkflowTemplate#idle_delete_ttl}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig(
            auto_delete_time=auto_delete_time,
            auto_delete_ttl=auto_delete_ttl,
            idle_delete_ttl=idle_delete_ttl,
        )

        return typing.cast(None, jsii.invoke(self, "putLifecycleConfig", [value]))

    @jsii.member(jsii_name="putMasterConfig")
    def put_master_config(
        self,
        *,
        accelerators: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators, typing.Dict[str, typing.Any]]]]] = None,
        disk_config: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig, typing.Dict[str, typing.Any]]] = None,
        image: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        num_instances: typing.Optional[jsii.Number] = None,
        preemptibility: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param accelerators: accelerators block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerators GoogleDataprocWorkflowTemplate#accelerators}
        :param disk_config: disk_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#disk_config GoogleDataprocWorkflowTemplate#disk_config}
        :param image: Optional. The Compute Engine image resource used for cluster instances. The URI can represent an image or image family. Image examples: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/[image-id]`` * ``projects/[project_id]/global/images/[image-id]`` * ``image-id`` Image family examples. Dataproc will use the most recent image from the family: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/family/[custom-image-family-name]`` * ``projects/[project_id]/global/images/family/[custom-image-family-name]`` If the URI is unspecified, it will be inferred from ``SoftwareConfig.image_version`` or the system default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#image GoogleDataprocWorkflowTemplate#image}
        :param machine_type: Optional. The Compute Engine machine type used for cluster instances. A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``n1-standard-2`` **Auto Zone Exception**: If you are using the Dataproc `Auto Zone Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`_ feature, you must use the short name of the machine type resource, for example, ``n1-standard-2``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#machine_type GoogleDataprocWorkflowTemplate#machine_type}
        :param min_cpu_platform: Optional. Specifies the minimum cpu platform for the Instance Group. See `Dataproc -> Minimum CPU Platform <https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-min-cpu>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#min_cpu_platform GoogleDataprocWorkflowTemplate#min_cpu_platform}
        :param num_instances: Optional. The number of VM instances in the instance group. For `HA cluster </dataproc/docs/concepts/configuring-clusters/high-availability>`_ `master_config <#FIELDS.master_config>`_ groups, **must be set to 3**. For standard cluster `master_config <#FIELDS.master_config>`_ groups, **must be set to 1**. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_instances GoogleDataprocWorkflowTemplate#num_instances}
        :param preemptibility: Optional. Specifies the preemptibility of the instance group. The default value for master and worker groups is ``NON_PREEMPTIBLE``. This default cannot be changed. The default value for secondary instances is ``PREEMPTIBLE``. Possible values: PREEMPTIBILITY_UNSPECIFIED, NON_PREEMPTIBLE, PREEMPTIBLE Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#preemptibility GoogleDataprocWorkflowTemplate#preemptibility}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig(
            accelerators=accelerators,
            disk_config=disk_config,
            image=image,
            machine_type=machine_type,
            min_cpu_platform=min_cpu_platform,
            num_instances=num_instances,
            preemptibility=preemptibility,
        )

        return typing.cast(None, jsii.invoke(self, "putMasterConfig", [value]))

    @jsii.member(jsii_name="putMetastoreConfig")
    def put_metastore_config(self, *, dataproc_metastore_service: builtins.str) -> None:
        '''
        :param dataproc_metastore_service: Required. Resource name of an existing Dataproc Metastore service. Example: * ``projects/[project_id]/locations/[dataproc_region]/services/[service-name]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#dataproc_metastore_service GoogleDataprocWorkflowTemplate#dataproc_metastore_service}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig(
            dataproc_metastore_service=dataproc_metastore_service
        )

        return typing.cast(None, jsii.invoke(self, "putMetastoreConfig", [value]))

    @jsii.member(jsii_name="putSecondaryWorkerConfig")
    def put_secondary_worker_config(
        self,
        *,
        accelerators: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators", typing.Dict[str, typing.Any]]]]] = None,
        disk_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig", typing.Dict[str, typing.Any]]] = None,
        image: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        num_instances: typing.Optional[jsii.Number] = None,
        preemptibility: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param accelerators: accelerators block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerators GoogleDataprocWorkflowTemplate#accelerators}
        :param disk_config: disk_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#disk_config GoogleDataprocWorkflowTemplate#disk_config}
        :param image: Optional. The Compute Engine image resource used for cluster instances. The URI can represent an image or image family. Image examples: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/[image-id]`` * ``projects/[project_id]/global/images/[image-id]`` * ``image-id`` Image family examples. Dataproc will use the most recent image from the family: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/family/[custom-image-family-name]`` * ``projects/[project_id]/global/images/family/[custom-image-family-name]`` If the URI is unspecified, it will be inferred from ``SoftwareConfig.image_version`` or the system default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#image GoogleDataprocWorkflowTemplate#image}
        :param machine_type: Optional. The Compute Engine machine type used for cluster instances. A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``n1-standard-2`` **Auto Zone Exception**: If you are using the Dataproc `Auto Zone Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`_ feature, you must use the short name of the machine type resource, for example, ``n1-standard-2``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#machine_type GoogleDataprocWorkflowTemplate#machine_type}
        :param min_cpu_platform: Optional. Specifies the minimum cpu platform for the Instance Group. See `Dataproc -> Minimum CPU Platform <https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-min-cpu>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#min_cpu_platform GoogleDataprocWorkflowTemplate#min_cpu_platform}
        :param num_instances: Optional. The number of VM instances in the instance group. For `HA cluster </dataproc/docs/concepts/configuring-clusters/high-availability>`_ `master_config <#FIELDS.master_config>`_ groups, **must be set to 3**. For standard cluster `master_config <#FIELDS.master_config>`_ groups, **must be set to 1**. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_instances GoogleDataprocWorkflowTemplate#num_instances}
        :param preemptibility: Optional. Specifies the preemptibility of the instance group. The default value for master and worker groups is ``NON_PREEMPTIBLE``. This default cannot be changed. The default value for secondary instances is ``PREEMPTIBLE``. Possible values: PREEMPTIBILITY_UNSPECIFIED, NON_PREEMPTIBLE, PREEMPTIBLE Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#preemptibility GoogleDataprocWorkflowTemplate#preemptibility}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig(
            accelerators=accelerators,
            disk_config=disk_config,
            image=image,
            machine_type=machine_type,
            min_cpu_platform=min_cpu_platform,
            num_instances=num_instances,
            preemptibility=preemptibility,
        )

        return typing.cast(None, jsii.invoke(self, "putSecondaryWorkerConfig", [value]))

    @jsii.member(jsii_name="putSecurityConfig")
    def put_security_config(
        self,
        *,
        kerberos_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param kerberos_config: kerberos_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#kerberos_config GoogleDataprocWorkflowTemplate#kerberos_config}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig(
            kerberos_config=kerberos_config
        )

        return typing.cast(None, jsii.invoke(self, "putSecurityConfig", [value]))

    @jsii.member(jsii_name="putSoftwareConfig")
    def put_software_config(
        self,
        *,
        image_version: typing.Optional[builtins.str] = None,
        optional_components: typing.Optional[typing.Sequence[builtins.str]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param image_version: Optional. The version of software inside the cluster. It must be one of the supported `Dataproc Versions <https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#supported_dataproc_versions>`_, such as "1.2" (including a subminor version, such as "1.2.29"), or the `"preview" version <https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#other_versions>`_. If unspecified, it defaults to the latest Debian version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#image_version GoogleDataprocWorkflowTemplate#image_version}
        :param optional_components: Optional. The set of components to activate on the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#optional_components GoogleDataprocWorkflowTemplate#optional_components}
        :param properties: Optional. The properties to set on daemon config files. Property keys are specified in ``prefix:property`` format, for example ``core:hadoop.tmp.dir``. The following are supported prefixes and their mappings: * capacity-scheduler: ``capacity-scheduler.xml`` * core: ``core-site.xml`` * distcp: ``distcp-default.xml`` * hdfs: ``hdfs-site.xml`` * hive: ``hive-site.xml`` * mapred: ``mapred-site.xml`` * pig: ``pig.properties`` * spark: ``spark-defaults.conf`` * yarn: ``yarn-site.xml`` For more information, see `Cluster properties <https://cloud.google.com/dataproc/docs/concepts/cluster-properties>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig(
            image_version=image_version,
            optional_components=optional_components,
            properties=properties,
        )

        return typing.cast(None, jsii.invoke(self, "putSoftwareConfig", [value]))

    @jsii.member(jsii_name="putWorkerConfig")
    def put_worker_config(
        self,
        *,
        accelerators: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators", typing.Dict[str, typing.Any]]]]] = None,
        disk_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig", typing.Dict[str, typing.Any]]] = None,
        image: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        num_instances: typing.Optional[jsii.Number] = None,
        preemptibility: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param accelerators: accelerators block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerators GoogleDataprocWorkflowTemplate#accelerators}
        :param disk_config: disk_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#disk_config GoogleDataprocWorkflowTemplate#disk_config}
        :param image: Optional. The Compute Engine image resource used for cluster instances. The URI can represent an image or image family. Image examples: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/[image-id]`` * ``projects/[project_id]/global/images/[image-id]`` * ``image-id`` Image family examples. Dataproc will use the most recent image from the family: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/family/[custom-image-family-name]`` * ``projects/[project_id]/global/images/family/[custom-image-family-name]`` If the URI is unspecified, it will be inferred from ``SoftwareConfig.image_version`` or the system default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#image GoogleDataprocWorkflowTemplate#image}
        :param machine_type: Optional. The Compute Engine machine type used for cluster instances. A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``n1-standard-2`` **Auto Zone Exception**: If you are using the Dataproc `Auto Zone Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`_ feature, you must use the short name of the machine type resource, for example, ``n1-standard-2``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#machine_type GoogleDataprocWorkflowTemplate#machine_type}
        :param min_cpu_platform: Optional. Specifies the minimum cpu platform for the Instance Group. See `Dataproc -> Minimum CPU Platform <https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-min-cpu>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#min_cpu_platform GoogleDataprocWorkflowTemplate#min_cpu_platform}
        :param num_instances: Optional. The number of VM instances in the instance group. For `HA cluster </dataproc/docs/concepts/configuring-clusters/high-availability>`_ `master_config <#FIELDS.master_config>`_ groups, **must be set to 3**. For standard cluster `master_config <#FIELDS.master_config>`_ groups, **must be set to 1**. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_instances GoogleDataprocWorkflowTemplate#num_instances}
        :param preemptibility: Optional. Specifies the preemptibility of the instance group. The default value for master and worker groups is ``NON_PREEMPTIBLE``. This default cannot be changed. The default value for secondary instances is ``PREEMPTIBLE``. Possible values: PREEMPTIBILITY_UNSPECIFIED, NON_PREEMPTIBLE, PREEMPTIBLE Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#preemptibility GoogleDataprocWorkflowTemplate#preemptibility}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig(
            accelerators=accelerators,
            disk_config=disk_config,
            image=image,
            machine_type=machine_type,
            min_cpu_platform=min_cpu_platform,
            num_instances=num_instances,
            preemptibility=preemptibility,
        )

        return typing.cast(None, jsii.invoke(self, "putWorkerConfig", [value]))

    @jsii.member(jsii_name="resetAutoscalingConfig")
    def reset_autoscaling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscalingConfig", []))

    @jsii.member(jsii_name="resetEncryptionConfig")
    def reset_encryption_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionConfig", []))

    @jsii.member(jsii_name="resetEndpointConfig")
    def reset_endpoint_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointConfig", []))

    @jsii.member(jsii_name="resetGceClusterConfig")
    def reset_gce_cluster_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGceClusterConfig", []))

    @jsii.member(jsii_name="resetGkeClusterConfig")
    def reset_gke_cluster_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGkeClusterConfig", []))

    @jsii.member(jsii_name="resetInitializationActions")
    def reset_initialization_actions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitializationActions", []))

    @jsii.member(jsii_name="resetLifecycleConfig")
    def reset_lifecycle_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfig", []))

    @jsii.member(jsii_name="resetMasterConfig")
    def reset_master_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterConfig", []))

    @jsii.member(jsii_name="resetMetastoreConfig")
    def reset_metastore_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetastoreConfig", []))

    @jsii.member(jsii_name="resetSecondaryWorkerConfig")
    def reset_secondary_worker_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondaryWorkerConfig", []))

    @jsii.member(jsii_name="resetSecurityConfig")
    def reset_security_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityConfig", []))

    @jsii.member(jsii_name="resetSoftwareConfig")
    def reset_software_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSoftwareConfig", []))

    @jsii.member(jsii_name="resetStagingBucket")
    def reset_staging_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStagingBucket", []))

    @jsii.member(jsii_name="resetTempBucket")
    def reset_temp_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTempBucket", []))

    @jsii.member(jsii_name="resetWorkerConfig")
    def reset_worker_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkerConfig", []))

    @builtins.property
    @jsii.member(jsii_name="autoscalingConfig")
    def autoscaling_config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfigOutputReference, jsii.get(self, "autoscalingConfig"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfig")
    def encryption_config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfigOutputReference, jsii.get(self, "encryptionConfig"))

    @builtins.property
    @jsii.member(jsii_name="endpointConfig")
    def endpoint_config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfigOutputReference, jsii.get(self, "endpointConfig"))

    @builtins.property
    @jsii.member(jsii_name="gceClusterConfig")
    def gce_cluster_config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference, jsii.get(self, "gceClusterConfig"))

    @builtins.property
    @jsii.member(jsii_name="gkeClusterConfig")
    def gke_cluster_config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigOutputReference, jsii.get(self, "gkeClusterConfig"))

    @builtins.property
    @jsii.member(jsii_name="initializationActions")
    def initialization_actions(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsList:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsList, jsii.get(self, "initializationActions"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfig")
    def lifecycle_config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfigOutputReference, jsii.get(self, "lifecycleConfig"))

    @builtins.property
    @jsii.member(jsii_name="masterConfig")
    def master_config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigOutputReference, jsii.get(self, "masterConfig"))

    @builtins.property
    @jsii.member(jsii_name="metastoreConfig")
    def metastore_config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfigOutputReference, jsii.get(self, "metastoreConfig"))

    @builtins.property
    @jsii.member(jsii_name="secondaryWorkerConfig")
    def secondary_worker_config(
        self,
    ) -> "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigOutputReference", jsii.get(self, "secondaryWorkerConfig"))

    @builtins.property
    @jsii.member(jsii_name="securityConfig")
    def security_config(
        self,
    ) -> "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigOutputReference", jsii.get(self, "securityConfig"))

    @builtins.property
    @jsii.member(jsii_name="softwareConfig")
    def software_config(
        self,
    ) -> "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfigOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfigOutputReference", jsii.get(self, "softwareConfig"))

    @builtins.property
    @jsii.member(jsii_name="workerConfig")
    def worker_config(
        self,
    ) -> "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigOutputReference":
        return typing.cast("GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigOutputReference", jsii.get(self, "workerConfig"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingConfigInput")
    def autoscaling_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig], jsii.get(self, "autoscalingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfigInput")
    def encryption_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig], jsii.get(self, "encryptionConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointConfigInput")
    def endpoint_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig], jsii.get(self, "endpointConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="gceClusterConfigInput")
    def gce_cluster_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig], jsii.get(self, "gceClusterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="gkeClusterConfigInput")
    def gke_cluster_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig], jsii.get(self, "gkeClusterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="initializationActionsInput")
    def initialization_actions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions]]], jsii.get(self, "initializationActionsInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigInput")
    def lifecycle_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig], jsii.get(self, "lifecycleConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="masterConfigInput")
    def master_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig], jsii.get(self, "masterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="metastoreConfigInput")
    def metastore_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig], jsii.get(self, "metastoreConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryWorkerConfigInput")
    def secondary_worker_config_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig"], jsii.get(self, "secondaryWorkerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="securityConfigInput")
    def security_config_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig"], jsii.get(self, "securityConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="softwareConfigInput")
    def software_config_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig"], jsii.get(self, "softwareConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="stagingBucketInput")
    def staging_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stagingBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="tempBucketInput")
    def temp_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tempBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="workerConfigInput")
    def worker_config_input(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig"]:
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig"], jsii.get(self, "workerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="stagingBucket")
    def staging_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stagingBucket"))

    @staging_bucket.setter
    def staging_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigOutputReference, "staging_bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stagingBucket", value)

    @builtins.property
    @jsii.member(jsii_name="tempBucket")
    def temp_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tempBucket"))

    @temp_bucket.setter
    def temp_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigOutputReference, "temp_bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tempBucket", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig",
    jsii_struct_bases=[],
    name_mapping={
        "accelerators": "accelerators",
        "disk_config": "diskConfig",
        "image": "image",
        "machine_type": "machineType",
        "min_cpu_platform": "minCpuPlatform",
        "num_instances": "numInstances",
        "preemptibility": "preemptibility",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig:
    def __init__(
        self,
        *,
        accelerators: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators", typing.Dict[str, typing.Any]]]]] = None,
        disk_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig", typing.Dict[str, typing.Any]]] = None,
        image: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        num_instances: typing.Optional[jsii.Number] = None,
        preemptibility: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param accelerators: accelerators block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerators GoogleDataprocWorkflowTemplate#accelerators}
        :param disk_config: disk_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#disk_config GoogleDataprocWorkflowTemplate#disk_config}
        :param image: Optional. The Compute Engine image resource used for cluster instances. The URI can represent an image or image family. Image examples: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/[image-id]`` * ``projects/[project_id]/global/images/[image-id]`` * ``image-id`` Image family examples. Dataproc will use the most recent image from the family: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/family/[custom-image-family-name]`` * ``projects/[project_id]/global/images/family/[custom-image-family-name]`` If the URI is unspecified, it will be inferred from ``SoftwareConfig.image_version`` or the system default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#image GoogleDataprocWorkflowTemplate#image}
        :param machine_type: Optional. The Compute Engine machine type used for cluster instances. A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``n1-standard-2`` **Auto Zone Exception**: If you are using the Dataproc `Auto Zone Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`_ feature, you must use the short name of the machine type resource, for example, ``n1-standard-2``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#machine_type GoogleDataprocWorkflowTemplate#machine_type}
        :param min_cpu_platform: Optional. Specifies the minimum cpu platform for the Instance Group. See `Dataproc -> Minimum CPU Platform <https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-min-cpu>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#min_cpu_platform GoogleDataprocWorkflowTemplate#min_cpu_platform}
        :param num_instances: Optional. The number of VM instances in the instance group. For `HA cluster </dataproc/docs/concepts/configuring-clusters/high-availability>`_ `master_config <#FIELDS.master_config>`_ groups, **must be set to 3**. For standard cluster `master_config <#FIELDS.master_config>`_ groups, **must be set to 1**. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_instances GoogleDataprocWorkflowTemplate#num_instances}
        :param preemptibility: Optional. Specifies the preemptibility of the instance group. The default value for master and worker groups is ``NON_PREEMPTIBLE``. This default cannot be changed. The default value for secondary instances is ``PREEMPTIBLE``. Possible values: PREEMPTIBILITY_UNSPECIFIED, NON_PREEMPTIBLE, PREEMPTIBLE Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#preemptibility GoogleDataprocWorkflowTemplate#preemptibility}
        '''
        if isinstance(disk_config, dict):
            disk_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig(**disk_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig.__init__)
            check_type(argname="argument accelerators", value=accelerators, expected_type=type_hints["accelerators"])
            check_type(argname="argument disk_config", value=disk_config, expected_type=type_hints["disk_config"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            check_type(argname="argument min_cpu_platform", value=min_cpu_platform, expected_type=type_hints["min_cpu_platform"])
            check_type(argname="argument num_instances", value=num_instances, expected_type=type_hints["num_instances"])
            check_type(argname="argument preemptibility", value=preemptibility, expected_type=type_hints["preemptibility"])
        self._values: typing.Dict[str, typing.Any] = {}
        if accelerators is not None:
            self._values["accelerators"] = accelerators
        if disk_config is not None:
            self._values["disk_config"] = disk_config
        if image is not None:
            self._values["image"] = image
        if machine_type is not None:
            self._values["machine_type"] = machine_type
        if min_cpu_platform is not None:
            self._values["min_cpu_platform"] = min_cpu_platform
        if num_instances is not None:
            self._values["num_instances"] = num_instances
        if preemptibility is not None:
            self._values["preemptibility"] = preemptibility

    @builtins.property
    def accelerators(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators"]]]:
        '''accelerators block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerators GoogleDataprocWorkflowTemplate#accelerators}
        '''
        result = self._values.get("accelerators")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators"]]], result)

    @builtins.property
    def disk_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig"]:
        '''disk_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#disk_config GoogleDataprocWorkflowTemplate#disk_config}
        '''
        result = self._values.get("disk_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig"], result)

    @builtins.property
    def image(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The Compute Engine image resource used for cluster instances. The URI can represent an image or image family. Image examples: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/[image-id]`` * ``projects/[project_id]/global/images/[image-id]`` * ``image-id`` Image family examples. Dataproc will use the most recent image from the family: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/family/[custom-image-family-name]`` * ``projects/[project_id]/global/images/family/[custom-image-family-name]`` If the URI is unspecified, it will be inferred from ``SoftwareConfig.image_version`` or the system default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#image GoogleDataprocWorkflowTemplate#image}
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def machine_type(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The Compute Engine machine type used for cluster instances. A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``n1-standard-2`` **Auto Zone Exception**: If you are using the Dataproc `Auto Zone Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`_ feature, you must use the short name of the machine type resource, for example, ``n1-standard-2``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#machine_type GoogleDataprocWorkflowTemplate#machine_type}
        '''
        result = self._values.get("machine_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_cpu_platform(self) -> typing.Optional[builtins.str]:
        '''Optional. Specifies the minimum cpu platform for the Instance Group. See `Dataproc -> Minimum CPU Platform <https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-min-cpu>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#min_cpu_platform GoogleDataprocWorkflowTemplate#min_cpu_platform}
        '''
        result = self._values.get("min_cpu_platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_instances(self) -> typing.Optional[jsii.Number]:
        '''Optional.

        The number of VM instances in the instance group. For `HA cluster </dataproc/docs/concepts/configuring-clusters/high-availability>`_ `master_config <#FIELDS.master_config>`_ groups, **must be set to 3**. For standard cluster `master_config <#FIELDS.master_config>`_ groups, **must be set to 1**.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_instances GoogleDataprocWorkflowTemplate#num_instances}
        '''
        result = self._values.get("num_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preemptibility(self) -> typing.Optional[builtins.str]:
        '''Optional.

        Specifies the preemptibility of the instance group. The default value for master and worker groups is ``NON_PREEMPTIBLE``. This default cannot be changed. The default value for secondary instances is ``PREEMPTIBLE``. Possible values: PREEMPTIBILITY_UNSPECIFIED, NON_PREEMPTIBLE, PREEMPTIBLE

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#preemptibility GoogleDataprocWorkflowTemplate#preemptibility}
        '''
        result = self._values.get("preemptibility")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators",
    jsii_struct_bases=[],
    name_mapping={
        "accelerator_count": "acceleratorCount",
        "accelerator_type": "acceleratorType",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators:
    def __init__(
        self,
        *,
        accelerator_count: typing.Optional[jsii.Number] = None,
        accelerator_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param accelerator_count: The number of the accelerator cards of this type exposed to this instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerator_count GoogleDataprocWorkflowTemplate#accelerator_count}
        :param accelerator_type: Full URL, partial URI, or short name of the accelerator type resource to expose to this instance. See `Compute Engine AcceleratorTypes <https://cloud.google.com/compute/docs/reference/beta/acceleratorTypes>`_. Examples: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/zones/us-east1-a/acceleratorTypes/nvidia-tesla-k80`` * ``projects/[project_id]/zones/us-east1-a/acceleratorTypes/nvidia-tesla-k80`` * ``nvidia-tesla-k80`` **Auto Zone Exception**: If you are using the Dataproc `Auto Zone Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`_ feature, you must use the short name of the accelerator type resource, for example, ``nvidia-tesla-k80``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerator_type GoogleDataprocWorkflowTemplate#accelerator_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators.__init__)
            check_type(argname="argument accelerator_count", value=accelerator_count, expected_type=type_hints["accelerator_count"])
            check_type(argname="argument accelerator_type", value=accelerator_type, expected_type=type_hints["accelerator_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if accelerator_count is not None:
            self._values["accelerator_count"] = accelerator_count
        if accelerator_type is not None:
            self._values["accelerator_type"] = accelerator_type

    @builtins.property
    def accelerator_count(self) -> typing.Optional[jsii.Number]:
        '''The number of the accelerator cards of this type exposed to this instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerator_count GoogleDataprocWorkflowTemplate#accelerator_count}
        '''
        result = self._values.get("accelerator_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def accelerator_type(self) -> typing.Optional[builtins.str]:
        '''Full URL, partial URI, or short name of the accelerator type resource to expose to this instance.

        See `Compute Engine AcceleratorTypes <https://cloud.google.com/compute/docs/reference/beta/acceleratorTypes>`_. Examples: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/zones/us-east1-a/acceleratorTypes/nvidia-tesla-k80`` * ``projects/[project_id]/zones/us-east1-a/acceleratorTypes/nvidia-tesla-k80`` * ``nvidia-tesla-k80`` **Auto Zone Exception**: If you are using the Dataproc `Auto Zone Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`_ feature, you must use the short name of the accelerator type resource, for example, ``nvidia-tesla-k80``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerator_type GoogleDataprocWorkflowTemplate#accelerator_type}
        '''
        result = self._values.get("accelerator_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsList",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAcceleratorCount")
    def reset_accelerator_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorCount", []))

    @jsii.member(jsii_name="resetAcceleratorType")
    def reset_accelerator_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorType", []))

    @builtins.property
    @jsii.member(jsii_name="acceleratorCountInput")
    def accelerator_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "acceleratorCountInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTypeInput")
    def accelerator_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceleratorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorCount")
    def accelerator_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "acceleratorCount"))

    @accelerator_count.setter
    def accelerator_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsOutputReference, "accelerator_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorCount", value)

    @builtins.property
    @jsii.member(jsii_name="acceleratorType")
    def accelerator_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acceleratorType"))

    @accelerator_type.setter
    def accelerator_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsOutputReference, "accelerator_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig",
    jsii_struct_bases=[],
    name_mapping={
        "boot_disk_size_gb": "bootDiskSizeGb",
        "boot_disk_type": "bootDiskType",
        "num_local_ssds": "numLocalSsds",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig:
    def __init__(
        self,
        *,
        boot_disk_size_gb: typing.Optional[jsii.Number] = None,
        boot_disk_type: typing.Optional[builtins.str] = None,
        num_local_ssds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param boot_disk_size_gb: Optional. Size in GB of the boot disk (default is 500GB). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_size_gb GoogleDataprocWorkflowTemplate#boot_disk_size_gb}
        :param boot_disk_type: Optional. Type of the boot disk (default is "pd-standard"). Valid values: "pd-balanced" (Persistent Disk Balanced Solid State Drive), "pd-ssd" (Persistent Disk Solid State Drive), or "pd-standard" (Persistent Disk Hard Disk Drive). See `Disk types <https://cloud.google.com/compute/docs/disks#disk-types>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_type GoogleDataprocWorkflowTemplate#boot_disk_type}
        :param num_local_ssds: Optional. Number of attached SSDs, from 0 to 4 (default is 0). If SSDs are not attached, the boot disk is used to store runtime logs and `HDFS <https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html>`_ data. If one or more SSDs are attached, this runtime bulk data is spread across them, and the boot disk contains only basic config and installed binaries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_local_ssds GoogleDataprocWorkflowTemplate#num_local_ssds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig.__init__)
            check_type(argname="argument boot_disk_size_gb", value=boot_disk_size_gb, expected_type=type_hints["boot_disk_size_gb"])
            check_type(argname="argument boot_disk_type", value=boot_disk_type, expected_type=type_hints["boot_disk_type"])
            check_type(argname="argument num_local_ssds", value=num_local_ssds, expected_type=type_hints["num_local_ssds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if boot_disk_size_gb is not None:
            self._values["boot_disk_size_gb"] = boot_disk_size_gb
        if boot_disk_type is not None:
            self._values["boot_disk_type"] = boot_disk_type
        if num_local_ssds is not None:
            self._values["num_local_ssds"] = num_local_ssds

    @builtins.property
    def boot_disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Optional. Size in GB of the boot disk (default is 500GB).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_size_gb GoogleDataprocWorkflowTemplate#boot_disk_size_gb}
        '''
        result = self._values.get("boot_disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def boot_disk_type(self) -> typing.Optional[builtins.str]:
        '''Optional.

        Type of the boot disk (default is "pd-standard"). Valid values: "pd-balanced" (Persistent Disk Balanced Solid State Drive), "pd-ssd" (Persistent Disk Solid State Drive), or "pd-standard" (Persistent Disk Hard Disk Drive). See `Disk types <https://cloud.google.com/compute/docs/disks#disk-types>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_type GoogleDataprocWorkflowTemplate#boot_disk_type}
        '''
        result = self._values.get("boot_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_local_ssds(self) -> typing.Optional[jsii.Number]:
        '''Optional.

        Number of attached SSDs, from 0 to 4 (default is 0). If SSDs are not attached, the boot disk is used to store runtime logs and `HDFS <https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html>`_ data. If one or more SSDs are attached, this runtime bulk data is spread across them, and the boot disk contains only basic config and installed binaries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_local_ssds GoogleDataprocWorkflowTemplate#num_local_ssds}
        '''
        result = self._values.get("num_local_ssds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBootDiskSizeGb")
    def reset_boot_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskSizeGb", []))

    @jsii.member(jsii_name="resetBootDiskType")
    def reset_boot_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskType", []))

    @jsii.member(jsii_name="resetNumLocalSsds")
    def reset_num_local_ssds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumLocalSsds", []))

    @builtins.property
    @jsii.member(jsii_name="bootDiskSizeGbInput")
    def boot_disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bootDiskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskTypeInput")
    def boot_disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootDiskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="numLocalSsdsInput")
    def num_local_ssds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numLocalSsdsInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bootDiskSizeGb"))

    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigOutputReference, "boot_disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="bootDiskType")
    def boot_disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootDiskType"))

    @boot_disk_type.setter
    def boot_disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigOutputReference, "boot_disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskType", value)

    @builtins.property
    @jsii.member(jsii_name="numLocalSsds")
    def num_local_ssds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numLocalSsds"))

    @num_local_ssds.setter
    def num_local_ssds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigOutputReference, "num_local_ssds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numLocalSsds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfig",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfig:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigList",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="instanceGroupManagerName")
    def instance_group_manager_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceGroupManagerName"))

    @builtins.property
    @jsii.member(jsii_name="instanceTemplateName")
    def instance_template_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceTemplateName"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAccelerators")
    def put_accelerators(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigOutputReference.put_accelerators)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccelerators", [value]))

    @jsii.member(jsii_name="putDiskConfig")
    def put_disk_config(
        self,
        *,
        boot_disk_size_gb: typing.Optional[jsii.Number] = None,
        boot_disk_type: typing.Optional[builtins.str] = None,
        num_local_ssds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param boot_disk_size_gb: Optional. Size in GB of the boot disk (default is 500GB). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_size_gb GoogleDataprocWorkflowTemplate#boot_disk_size_gb}
        :param boot_disk_type: Optional. Type of the boot disk (default is "pd-standard"). Valid values: "pd-balanced" (Persistent Disk Balanced Solid State Drive), "pd-ssd" (Persistent Disk Solid State Drive), or "pd-standard" (Persistent Disk Hard Disk Drive). See `Disk types <https://cloud.google.com/compute/docs/disks#disk-types>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_type GoogleDataprocWorkflowTemplate#boot_disk_type}
        :param num_local_ssds: Optional. Number of attached SSDs, from 0 to 4 (default is 0). If SSDs are not attached, the boot disk is used to store runtime logs and `HDFS <https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html>`_ data. If one or more SSDs are attached, this runtime bulk data is spread across them, and the boot disk contains only basic config and installed binaries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_local_ssds GoogleDataprocWorkflowTemplate#num_local_ssds}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig(
            boot_disk_size_gb=boot_disk_size_gb,
            boot_disk_type=boot_disk_type,
            num_local_ssds=num_local_ssds,
        )

        return typing.cast(None, jsii.invoke(self, "putDiskConfig", [value]))

    @jsii.member(jsii_name="resetAccelerators")
    def reset_accelerators(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccelerators", []))

    @jsii.member(jsii_name="resetDiskConfig")
    def reset_disk_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskConfig", []))

    @jsii.member(jsii_name="resetImage")
    def reset_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImage", []))

    @jsii.member(jsii_name="resetMachineType")
    def reset_machine_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineType", []))

    @jsii.member(jsii_name="resetMinCpuPlatform")
    def reset_min_cpu_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCpuPlatform", []))

    @jsii.member(jsii_name="resetNumInstances")
    def reset_num_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumInstances", []))

    @jsii.member(jsii_name="resetPreemptibility")
    def reset_preemptibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreemptibility", []))

    @builtins.property
    @jsii.member(jsii_name="accelerators")
    def accelerators(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsList:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsList, jsii.get(self, "accelerators"))

    @builtins.property
    @jsii.member(jsii_name="diskConfig")
    def disk_config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigOutputReference, jsii.get(self, "diskConfig"))

    @builtins.property
    @jsii.member(jsii_name="instanceNames")
    def instance_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceNames"))

    @builtins.property
    @jsii.member(jsii_name="isPreemptible")
    def is_preemptible(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "isPreemptible"))

    @builtins.property
    @jsii.member(jsii_name="managedGroupConfig")
    def managed_group_config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigList:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigList, jsii.get(self, "managedGroupConfig"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorsInput")
    def accelerators_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators]]], jsii.get(self, "acceleratorsInput"))

    @builtins.property
    @jsii.member(jsii_name="diskConfigInput")
    def disk_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig], jsii.get(self, "diskConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatformInput")
    def min_cpu_platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minCpuPlatformInput"))

    @builtins.property
    @jsii.member(jsii_name="numInstancesInput")
    def num_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="preemptibilityInput")
    def preemptibility_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preemptibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigOutputReference, "image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "image", value)

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigOutputReference, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatform")
    def min_cpu_platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minCpuPlatform"))

    @min_cpu_platform.setter
    def min_cpu_platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigOutputReference, "min_cpu_platform").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCpuPlatform", value)

    @builtins.property
    @jsii.member(jsii_name="numInstances")
    def num_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numInstances"))

    @num_instances.setter
    def num_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigOutputReference, "num_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numInstances", value)

    @builtins.property
    @jsii.member(jsii_name="preemptibility")
    def preemptibility(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preemptibility"))

    @preemptibility.setter
    def preemptibility(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigOutputReference, "preemptibility").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preemptibility", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig",
    jsii_struct_bases=[],
    name_mapping={"kerberos_config": "kerberosConfig"},
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig:
    def __init__(
        self,
        *,
        kerberos_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param kerberos_config: kerberos_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#kerberos_config GoogleDataprocWorkflowTemplate#kerberos_config}
        '''
        if isinstance(kerberos_config, dict):
            kerberos_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig(**kerberos_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig.__init__)
            check_type(argname="argument kerberos_config", value=kerberos_config, expected_type=type_hints["kerberos_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if kerberos_config is not None:
            self._values["kerberos_config"] = kerberos_config

    @builtins.property
    def kerberos_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig"]:
        '''kerberos_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#kerberos_config GoogleDataprocWorkflowTemplate#kerberos_config}
        '''
        result = self._values.get("kerberos_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig",
    jsii_struct_bases=[],
    name_mapping={
        "cross_realm_trust_admin_server": "crossRealmTrustAdminServer",
        "cross_realm_trust_kdc": "crossRealmTrustKdc",
        "cross_realm_trust_realm": "crossRealmTrustRealm",
        "cross_realm_trust_shared_password": "crossRealmTrustSharedPassword",
        "enable_kerberos": "enableKerberos",
        "kdc_db_key": "kdcDbKey",
        "key_password": "keyPassword",
        "keystore": "keystore",
        "keystore_password": "keystorePassword",
        "kms_key": "kmsKey",
        "realm": "realm",
        "root_principal_password": "rootPrincipalPassword",
        "tgt_lifetime_hours": "tgtLifetimeHours",
        "truststore": "truststore",
        "truststore_password": "truststorePassword",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig:
    def __init__(
        self,
        *,
        cross_realm_trust_admin_server: typing.Optional[builtins.str] = None,
        cross_realm_trust_kdc: typing.Optional[builtins.str] = None,
        cross_realm_trust_realm: typing.Optional[builtins.str] = None,
        cross_realm_trust_shared_password: typing.Optional[builtins.str] = None,
        enable_kerberos: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        kdc_db_key: typing.Optional[builtins.str] = None,
        key_password: typing.Optional[builtins.str] = None,
        keystore: typing.Optional[builtins.str] = None,
        keystore_password: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        realm: typing.Optional[builtins.str] = None,
        root_principal_password: typing.Optional[builtins.str] = None,
        tgt_lifetime_hours: typing.Optional[jsii.Number] = None,
        truststore: typing.Optional[builtins.str] = None,
        truststore_password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cross_realm_trust_admin_server: Optional. The admin server (IP or hostname) for the remote trusted realm in a cross realm trust relationship. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cross_realm_trust_admin_server GoogleDataprocWorkflowTemplate#cross_realm_trust_admin_server}
        :param cross_realm_trust_kdc: Optional. The KDC (IP or hostname) for the remote trusted realm in a cross realm trust relationship. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cross_realm_trust_kdc GoogleDataprocWorkflowTemplate#cross_realm_trust_kdc}
        :param cross_realm_trust_realm: Optional. The remote realm the Dataproc on-cluster KDC will trust, should the user enable cross realm trust. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cross_realm_trust_realm GoogleDataprocWorkflowTemplate#cross_realm_trust_realm}
        :param cross_realm_trust_shared_password: Optional. The Cloud Storage URI of a KMS encrypted file containing the shared password between the on-cluster Kerberos realm and the remote trusted realm, in a cross realm trust relationship. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cross_realm_trust_shared_password GoogleDataprocWorkflowTemplate#cross_realm_trust_shared_password}
        :param enable_kerberos: Optional. Flag to indicate whether to Kerberize the cluster (default: false). Set this field to true to enable Kerberos on a cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#enable_kerberos GoogleDataprocWorkflowTemplate#enable_kerberos}
        :param kdc_db_key: Optional. The Cloud Storage URI of a KMS encrypted file containing the master key of the KDC database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#kdc_db_key GoogleDataprocWorkflowTemplate#kdc_db_key}
        :param key_password: Optional. The Cloud Storage URI of a KMS encrypted file containing the password to the user provided key. For the self-signed certificate, this password is generated by Dataproc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#key_password GoogleDataprocWorkflowTemplate#key_password}
        :param keystore: Optional. The Cloud Storage URI of the keystore file used for SSL encryption. If not provided, Dataproc will provide a self-signed certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#keystore GoogleDataprocWorkflowTemplate#keystore}
        :param keystore_password: Optional. The Cloud Storage URI of a KMS encrypted file containing the password to the user provided keystore. For the self-signed certificate, this password is generated by Dataproc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#keystore_password GoogleDataprocWorkflowTemplate#keystore_password}
        :param kms_key: Optional. The uri of the KMS key used to encrypt various sensitive files. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#kms_key GoogleDataprocWorkflowTemplate#kms_key}
        :param realm: Optional. The name of the on-cluster Kerberos realm. If not specified, the uppercased domain of hostnames will be the realm. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#realm GoogleDataprocWorkflowTemplate#realm}
        :param root_principal_password: Optional. The Cloud Storage URI of a KMS encrypted file containing the root principal password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#root_principal_password GoogleDataprocWorkflowTemplate#root_principal_password}
        :param tgt_lifetime_hours: Optional. The lifetime of the ticket granting ticket, in hours. If not specified, or user specifies 0, then default value 10 will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#tgt_lifetime_hours GoogleDataprocWorkflowTemplate#tgt_lifetime_hours}
        :param truststore: Optional. The Cloud Storage URI of the truststore file used for SSL encryption. If not provided, Dataproc will provide a self-signed certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#truststore GoogleDataprocWorkflowTemplate#truststore}
        :param truststore_password: Optional. The Cloud Storage URI of a KMS encrypted file containing the password to the user provided truststore. For the self-signed certificate, this password is generated by Dataproc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#truststore_password GoogleDataprocWorkflowTemplate#truststore_password}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig.__init__)
            check_type(argname="argument cross_realm_trust_admin_server", value=cross_realm_trust_admin_server, expected_type=type_hints["cross_realm_trust_admin_server"])
            check_type(argname="argument cross_realm_trust_kdc", value=cross_realm_trust_kdc, expected_type=type_hints["cross_realm_trust_kdc"])
            check_type(argname="argument cross_realm_trust_realm", value=cross_realm_trust_realm, expected_type=type_hints["cross_realm_trust_realm"])
            check_type(argname="argument cross_realm_trust_shared_password", value=cross_realm_trust_shared_password, expected_type=type_hints["cross_realm_trust_shared_password"])
            check_type(argname="argument enable_kerberos", value=enable_kerberos, expected_type=type_hints["enable_kerberos"])
            check_type(argname="argument kdc_db_key", value=kdc_db_key, expected_type=type_hints["kdc_db_key"])
            check_type(argname="argument key_password", value=key_password, expected_type=type_hints["key_password"])
            check_type(argname="argument keystore", value=keystore, expected_type=type_hints["keystore"])
            check_type(argname="argument keystore_password", value=keystore_password, expected_type=type_hints["keystore_password"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument realm", value=realm, expected_type=type_hints["realm"])
            check_type(argname="argument root_principal_password", value=root_principal_password, expected_type=type_hints["root_principal_password"])
            check_type(argname="argument tgt_lifetime_hours", value=tgt_lifetime_hours, expected_type=type_hints["tgt_lifetime_hours"])
            check_type(argname="argument truststore", value=truststore, expected_type=type_hints["truststore"])
            check_type(argname="argument truststore_password", value=truststore_password, expected_type=type_hints["truststore_password"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cross_realm_trust_admin_server is not None:
            self._values["cross_realm_trust_admin_server"] = cross_realm_trust_admin_server
        if cross_realm_trust_kdc is not None:
            self._values["cross_realm_trust_kdc"] = cross_realm_trust_kdc
        if cross_realm_trust_realm is not None:
            self._values["cross_realm_trust_realm"] = cross_realm_trust_realm
        if cross_realm_trust_shared_password is not None:
            self._values["cross_realm_trust_shared_password"] = cross_realm_trust_shared_password
        if enable_kerberos is not None:
            self._values["enable_kerberos"] = enable_kerberos
        if kdc_db_key is not None:
            self._values["kdc_db_key"] = kdc_db_key
        if key_password is not None:
            self._values["key_password"] = key_password
        if keystore is not None:
            self._values["keystore"] = keystore
        if keystore_password is not None:
            self._values["keystore_password"] = keystore_password
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if realm is not None:
            self._values["realm"] = realm
        if root_principal_password is not None:
            self._values["root_principal_password"] = root_principal_password
        if tgt_lifetime_hours is not None:
            self._values["tgt_lifetime_hours"] = tgt_lifetime_hours
        if truststore is not None:
            self._values["truststore"] = truststore
        if truststore_password is not None:
            self._values["truststore_password"] = truststore_password

    @builtins.property
    def cross_realm_trust_admin_server(self) -> typing.Optional[builtins.str]:
        '''Optional. The admin server (IP or hostname) for the remote trusted realm in a cross realm trust relationship.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cross_realm_trust_admin_server GoogleDataprocWorkflowTemplate#cross_realm_trust_admin_server}
        '''
        result = self._values.get("cross_realm_trust_admin_server")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cross_realm_trust_kdc(self) -> typing.Optional[builtins.str]:
        '''Optional. The KDC (IP or hostname) for the remote trusted realm in a cross realm trust relationship.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cross_realm_trust_kdc GoogleDataprocWorkflowTemplate#cross_realm_trust_kdc}
        '''
        result = self._values.get("cross_realm_trust_kdc")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cross_realm_trust_realm(self) -> typing.Optional[builtins.str]:
        '''Optional. The remote realm the Dataproc on-cluster KDC will trust, should the user enable cross realm trust.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cross_realm_trust_realm GoogleDataprocWorkflowTemplate#cross_realm_trust_realm}
        '''
        result = self._values.get("cross_realm_trust_realm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cross_realm_trust_shared_password(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The Cloud Storage URI of a KMS encrypted file containing the shared password between the on-cluster Kerberos realm and the remote trusted realm, in a cross realm trust relationship.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cross_realm_trust_shared_password GoogleDataprocWorkflowTemplate#cross_realm_trust_shared_password}
        '''
        result = self._values.get("cross_realm_trust_shared_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_kerberos(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional.

        Flag to indicate whether to Kerberize the cluster (default: false). Set this field to true to enable Kerberos on a cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#enable_kerberos GoogleDataprocWorkflowTemplate#enable_kerberos}
        '''
        result = self._values.get("enable_kerberos")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def kdc_db_key(self) -> typing.Optional[builtins.str]:
        '''Optional. The Cloud Storage URI of a KMS encrypted file containing the master key of the KDC database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#kdc_db_key GoogleDataprocWorkflowTemplate#kdc_db_key}
        '''
        result = self._values.get("kdc_db_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_password(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The Cloud Storage URI of a KMS encrypted file containing the password to the user provided key. For the self-signed certificate, this password is generated by Dataproc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#key_password GoogleDataprocWorkflowTemplate#key_password}
        '''
        result = self._values.get("key_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keystore(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The Cloud Storage URI of the keystore file used for SSL encryption. If not provided, Dataproc will provide a self-signed certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#keystore GoogleDataprocWorkflowTemplate#keystore}
        '''
        result = self._values.get("keystore")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keystore_password(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The Cloud Storage URI of a KMS encrypted file containing the password to the user provided keystore. For the self-signed certificate, this password is generated by Dataproc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#keystore_password GoogleDataprocWorkflowTemplate#keystore_password}
        '''
        result = self._values.get("keystore_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''Optional. The uri of the KMS key used to encrypt various sensitive files.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#kms_key GoogleDataprocWorkflowTemplate#kms_key}
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def realm(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The name of the on-cluster Kerberos realm. If not specified, the uppercased domain of hostnames will be the realm.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#realm GoogleDataprocWorkflowTemplate#realm}
        '''
        result = self._values.get("realm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_principal_password(self) -> typing.Optional[builtins.str]:
        '''Optional. The Cloud Storage URI of a KMS encrypted file containing the root principal password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#root_principal_password GoogleDataprocWorkflowTemplate#root_principal_password}
        '''
        result = self._values.get("root_principal_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tgt_lifetime_hours(self) -> typing.Optional[jsii.Number]:
        '''Optional.

        The lifetime of the ticket granting ticket, in hours. If not specified, or user specifies 0, then default value 10 will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#tgt_lifetime_hours GoogleDataprocWorkflowTemplate#tgt_lifetime_hours}
        '''
        result = self._values.get("tgt_lifetime_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def truststore(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The Cloud Storage URI of the truststore file used for SSL encryption. If not provided, Dataproc will provide a self-signed certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#truststore GoogleDataprocWorkflowTemplate#truststore}
        '''
        result = self._values.get("truststore")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def truststore_password(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The Cloud Storage URI of a KMS encrypted file containing the password to the user provided truststore. For the self-signed certificate, this password is generated by Dataproc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#truststore_password GoogleDataprocWorkflowTemplate#truststore_password}
        '''
        result = self._values.get("truststore_password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCrossRealmTrustAdminServer")
    def reset_cross_realm_trust_admin_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossRealmTrustAdminServer", []))

    @jsii.member(jsii_name="resetCrossRealmTrustKdc")
    def reset_cross_realm_trust_kdc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossRealmTrustKdc", []))

    @jsii.member(jsii_name="resetCrossRealmTrustRealm")
    def reset_cross_realm_trust_realm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossRealmTrustRealm", []))

    @jsii.member(jsii_name="resetCrossRealmTrustSharedPassword")
    def reset_cross_realm_trust_shared_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossRealmTrustSharedPassword", []))

    @jsii.member(jsii_name="resetEnableKerberos")
    def reset_enable_kerberos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableKerberos", []))

    @jsii.member(jsii_name="resetKdcDbKey")
    def reset_kdc_db_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKdcDbKey", []))

    @jsii.member(jsii_name="resetKeyPassword")
    def reset_key_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyPassword", []))

    @jsii.member(jsii_name="resetKeystore")
    def reset_keystore(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeystore", []))

    @jsii.member(jsii_name="resetKeystorePassword")
    def reset_keystore_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeystorePassword", []))

    @jsii.member(jsii_name="resetKmsKey")
    def reset_kms_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKey", []))

    @jsii.member(jsii_name="resetRealm")
    def reset_realm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRealm", []))

    @jsii.member(jsii_name="resetRootPrincipalPassword")
    def reset_root_principal_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootPrincipalPassword", []))

    @jsii.member(jsii_name="resetTgtLifetimeHours")
    def reset_tgt_lifetime_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTgtLifetimeHours", []))

    @jsii.member(jsii_name="resetTruststore")
    def reset_truststore(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTruststore", []))

    @jsii.member(jsii_name="resetTruststorePassword")
    def reset_truststore_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTruststorePassword", []))

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustAdminServerInput")
    def cross_realm_trust_admin_server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossRealmTrustAdminServerInput"))

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustKdcInput")
    def cross_realm_trust_kdc_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossRealmTrustKdcInput"))

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustRealmInput")
    def cross_realm_trust_realm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossRealmTrustRealmInput"))

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustSharedPasswordInput")
    def cross_realm_trust_shared_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossRealmTrustSharedPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="enableKerberosInput")
    def enable_kerberos_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableKerberosInput"))

    @builtins.property
    @jsii.member(jsii_name="kdcDbKeyInput")
    def kdc_db_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kdcDbKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="keyPasswordInput")
    def key_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="keystoreInput")
    def keystore_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keystoreInput"))

    @builtins.property
    @jsii.member(jsii_name="keystorePasswordInput")
    def keystore_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keystorePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyInput")
    def kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="realmInput")
    def realm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "realmInput"))

    @builtins.property
    @jsii.member(jsii_name="rootPrincipalPasswordInput")
    def root_principal_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootPrincipalPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="tgtLifetimeHoursInput")
    def tgt_lifetime_hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tgtLifetimeHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="truststoreInput")
    def truststore_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "truststoreInput"))

    @builtins.property
    @jsii.member(jsii_name="truststorePasswordInput")
    def truststore_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "truststorePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustAdminServer")
    def cross_realm_trust_admin_server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossRealmTrustAdminServer"))

    @cross_realm_trust_admin_server.setter
    def cross_realm_trust_admin_server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "cross_realm_trust_admin_server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossRealmTrustAdminServer", value)

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustKdc")
    def cross_realm_trust_kdc(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossRealmTrustKdc"))

    @cross_realm_trust_kdc.setter
    def cross_realm_trust_kdc(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "cross_realm_trust_kdc").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossRealmTrustKdc", value)

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustRealm")
    def cross_realm_trust_realm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossRealmTrustRealm"))

    @cross_realm_trust_realm.setter
    def cross_realm_trust_realm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "cross_realm_trust_realm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossRealmTrustRealm", value)

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustSharedPassword")
    def cross_realm_trust_shared_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossRealmTrustSharedPassword"))

    @cross_realm_trust_shared_password.setter
    def cross_realm_trust_shared_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "cross_realm_trust_shared_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossRealmTrustSharedPassword", value)

    @builtins.property
    @jsii.member(jsii_name="enableKerberos")
    def enable_kerberos(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableKerberos"))

    @enable_kerberos.setter
    def enable_kerberos(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "enable_kerberos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableKerberos", value)

    @builtins.property
    @jsii.member(jsii_name="kdcDbKey")
    def kdc_db_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kdcDbKey"))

    @kdc_db_key.setter
    def kdc_db_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "kdc_db_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kdcDbKey", value)

    @builtins.property
    @jsii.member(jsii_name="keyPassword")
    def key_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyPassword"))

    @key_password.setter
    def key_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "key_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPassword", value)

    @builtins.property
    @jsii.member(jsii_name="keystore")
    def keystore(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keystore"))

    @keystore.setter
    def keystore(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "keystore").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keystore", value)

    @builtins.property
    @jsii.member(jsii_name="keystorePassword")
    def keystore_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keystorePassword"))

    @keystore_password.setter
    def keystore_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "keystore_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keystorePassword", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "kms_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="realm")
    def realm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realm"))

    @realm.setter
    def realm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "realm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "realm", value)

    @builtins.property
    @jsii.member(jsii_name="rootPrincipalPassword")
    def root_principal_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootPrincipalPassword"))

    @root_principal_password.setter
    def root_principal_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "root_principal_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootPrincipalPassword", value)

    @builtins.property
    @jsii.member(jsii_name="tgtLifetimeHours")
    def tgt_lifetime_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tgtLifetimeHours"))

    @tgt_lifetime_hours.setter
    def tgt_lifetime_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "tgt_lifetime_hours").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tgtLifetimeHours", value)

    @builtins.property
    @jsii.member(jsii_name="truststore")
    def truststore(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "truststore"))

    @truststore.setter
    def truststore(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "truststore").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "truststore", value)

    @builtins.property
    @jsii.member(jsii_name="truststorePassword")
    def truststore_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "truststorePassword"))

    @truststore_password.setter
    def truststore_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "truststore_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "truststorePassword", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putKerberosConfig")
    def put_kerberos_config(
        self,
        *,
        cross_realm_trust_admin_server: typing.Optional[builtins.str] = None,
        cross_realm_trust_kdc: typing.Optional[builtins.str] = None,
        cross_realm_trust_realm: typing.Optional[builtins.str] = None,
        cross_realm_trust_shared_password: typing.Optional[builtins.str] = None,
        enable_kerberos: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        kdc_db_key: typing.Optional[builtins.str] = None,
        key_password: typing.Optional[builtins.str] = None,
        keystore: typing.Optional[builtins.str] = None,
        keystore_password: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        realm: typing.Optional[builtins.str] = None,
        root_principal_password: typing.Optional[builtins.str] = None,
        tgt_lifetime_hours: typing.Optional[jsii.Number] = None,
        truststore: typing.Optional[builtins.str] = None,
        truststore_password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cross_realm_trust_admin_server: Optional. The admin server (IP or hostname) for the remote trusted realm in a cross realm trust relationship. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cross_realm_trust_admin_server GoogleDataprocWorkflowTemplate#cross_realm_trust_admin_server}
        :param cross_realm_trust_kdc: Optional. The KDC (IP or hostname) for the remote trusted realm in a cross realm trust relationship. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cross_realm_trust_kdc GoogleDataprocWorkflowTemplate#cross_realm_trust_kdc}
        :param cross_realm_trust_realm: Optional. The remote realm the Dataproc on-cluster KDC will trust, should the user enable cross realm trust. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cross_realm_trust_realm GoogleDataprocWorkflowTemplate#cross_realm_trust_realm}
        :param cross_realm_trust_shared_password: Optional. The Cloud Storage URI of a KMS encrypted file containing the shared password between the on-cluster Kerberos realm and the remote trusted realm, in a cross realm trust relationship. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cross_realm_trust_shared_password GoogleDataprocWorkflowTemplate#cross_realm_trust_shared_password}
        :param enable_kerberos: Optional. Flag to indicate whether to Kerberize the cluster (default: false). Set this field to true to enable Kerberos on a cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#enable_kerberos GoogleDataprocWorkflowTemplate#enable_kerberos}
        :param kdc_db_key: Optional. The Cloud Storage URI of a KMS encrypted file containing the master key of the KDC database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#kdc_db_key GoogleDataprocWorkflowTemplate#kdc_db_key}
        :param key_password: Optional. The Cloud Storage URI of a KMS encrypted file containing the password to the user provided key. For the self-signed certificate, this password is generated by Dataproc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#key_password GoogleDataprocWorkflowTemplate#key_password}
        :param keystore: Optional. The Cloud Storage URI of the keystore file used for SSL encryption. If not provided, Dataproc will provide a self-signed certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#keystore GoogleDataprocWorkflowTemplate#keystore}
        :param keystore_password: Optional. The Cloud Storage URI of a KMS encrypted file containing the password to the user provided keystore. For the self-signed certificate, this password is generated by Dataproc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#keystore_password GoogleDataprocWorkflowTemplate#keystore_password}
        :param kms_key: Optional. The uri of the KMS key used to encrypt various sensitive files. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#kms_key GoogleDataprocWorkflowTemplate#kms_key}
        :param realm: Optional. The name of the on-cluster Kerberos realm. If not specified, the uppercased domain of hostnames will be the realm. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#realm GoogleDataprocWorkflowTemplate#realm}
        :param root_principal_password: Optional. The Cloud Storage URI of a KMS encrypted file containing the root principal password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#root_principal_password GoogleDataprocWorkflowTemplate#root_principal_password}
        :param tgt_lifetime_hours: Optional. The lifetime of the ticket granting ticket, in hours. If not specified, or user specifies 0, then default value 10 will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#tgt_lifetime_hours GoogleDataprocWorkflowTemplate#tgt_lifetime_hours}
        :param truststore: Optional. The Cloud Storage URI of the truststore file used for SSL encryption. If not provided, Dataproc will provide a self-signed certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#truststore GoogleDataprocWorkflowTemplate#truststore}
        :param truststore_password: Optional. The Cloud Storage URI of a KMS encrypted file containing the password to the user provided truststore. For the self-signed certificate, this password is generated by Dataproc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#truststore_password GoogleDataprocWorkflowTemplate#truststore_password}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig(
            cross_realm_trust_admin_server=cross_realm_trust_admin_server,
            cross_realm_trust_kdc=cross_realm_trust_kdc,
            cross_realm_trust_realm=cross_realm_trust_realm,
            cross_realm_trust_shared_password=cross_realm_trust_shared_password,
            enable_kerberos=enable_kerberos,
            kdc_db_key=kdc_db_key,
            key_password=key_password,
            keystore=keystore,
            keystore_password=keystore_password,
            kms_key=kms_key,
            realm=realm,
            root_principal_password=root_principal_password,
            tgt_lifetime_hours=tgt_lifetime_hours,
            truststore=truststore,
            truststore_password=truststore_password,
        )

        return typing.cast(None, jsii.invoke(self, "putKerberosConfig", [value]))

    @jsii.member(jsii_name="resetKerberosConfig")
    def reset_kerberos_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKerberosConfig", []))

    @builtins.property
    @jsii.member(jsii_name="kerberosConfig")
    def kerberos_config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference, jsii.get(self, "kerberosConfig"))

    @builtins.property
    @jsii.member(jsii_name="kerberosConfigInput")
    def kerberos_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig], jsii.get(self, "kerberosConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig",
    jsii_struct_bases=[],
    name_mapping={
        "image_version": "imageVersion",
        "optional_components": "optionalComponents",
        "properties": "properties",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig:
    def __init__(
        self,
        *,
        image_version: typing.Optional[builtins.str] = None,
        optional_components: typing.Optional[typing.Sequence[builtins.str]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param image_version: Optional. The version of software inside the cluster. It must be one of the supported `Dataproc Versions <https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#supported_dataproc_versions>`_, such as "1.2" (including a subminor version, such as "1.2.29"), or the `"preview" version <https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#other_versions>`_. If unspecified, it defaults to the latest Debian version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#image_version GoogleDataprocWorkflowTemplate#image_version}
        :param optional_components: Optional. The set of components to activate on the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#optional_components GoogleDataprocWorkflowTemplate#optional_components}
        :param properties: Optional. The properties to set on daemon config files. Property keys are specified in ``prefix:property`` format, for example ``core:hadoop.tmp.dir``. The following are supported prefixes and their mappings: * capacity-scheduler: ``capacity-scheduler.xml`` * core: ``core-site.xml`` * distcp: ``distcp-default.xml`` * hdfs: ``hdfs-site.xml`` * hive: ``hive-site.xml`` * mapred: ``mapred-site.xml`` * pig: ``pig.properties`` * spark: ``spark-defaults.conf`` * yarn: ``yarn-site.xml`` For more information, see `Cluster properties <https://cloud.google.com/dataproc/docs/concepts/cluster-properties>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig.__init__)
            check_type(argname="argument image_version", value=image_version, expected_type=type_hints["image_version"])
            check_type(argname="argument optional_components", value=optional_components, expected_type=type_hints["optional_components"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[str, typing.Any] = {}
        if image_version is not None:
            self._values["image_version"] = image_version
        if optional_components is not None:
            self._values["optional_components"] = optional_components
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def image_version(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The version of software inside the cluster. It must be one of the supported `Dataproc Versions <https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#supported_dataproc_versions>`_, such as "1.2" (including a subminor version, such as "1.2.29"), or the `"preview" version <https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#other_versions>`_. If unspecified, it defaults to the latest Debian version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#image_version GoogleDataprocWorkflowTemplate#image_version}
        '''
        result = self._values.get("image_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional_components(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional. The set of components to activate on the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#optional_components GoogleDataprocWorkflowTemplate#optional_components}
        '''
        result = self._values.get("optional_components")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        The properties to set on daemon config files. Property keys are specified in ``prefix:property`` format, for example ``core:hadoop.tmp.dir``. The following are supported prefixes and their mappings: * capacity-scheduler: ``capacity-scheduler.xml`` * core: ``core-site.xml`` * distcp: ``distcp-default.xml`` * hdfs: ``hdfs-site.xml`` * hive: ``hive-site.xml`` * mapred: ``mapred-site.xml`` * pig: ``pig.properties`` * spark: ``spark-defaults.conf`` * yarn: ``yarn-site.xml`` For more information, see `Cluster properties <https://cloud.google.com/dataproc/docs/concepts/cluster-properties>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#properties GoogleDataprocWorkflowTemplate#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetImageVersion")
    def reset_image_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageVersion", []))

    @jsii.member(jsii_name="resetOptionalComponents")
    def reset_optional_components(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptionalComponents", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @builtins.property
    @jsii.member(jsii_name="imageVersionInput")
    def image_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="optionalComponentsInput")
    def optional_components_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "optionalComponentsInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="imageVersion")
    def image_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageVersion"))

    @image_version.setter
    def image_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfigOutputReference, "image_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageVersion", value)

    @builtins.property
    @jsii.member(jsii_name="optionalComponents")
    def optional_components(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "optionalComponents"))

    @optional_components.setter
    def optional_components(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfigOutputReference, "optional_components").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optionalComponents", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfigOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig",
    jsii_struct_bases=[],
    name_mapping={
        "accelerators": "accelerators",
        "disk_config": "diskConfig",
        "image": "image",
        "machine_type": "machineType",
        "min_cpu_platform": "minCpuPlatform",
        "num_instances": "numInstances",
        "preemptibility": "preemptibility",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig:
    def __init__(
        self,
        *,
        accelerators: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators", typing.Dict[str, typing.Any]]]]] = None,
        disk_config: typing.Optional[typing.Union["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig", typing.Dict[str, typing.Any]]] = None,
        image: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        num_instances: typing.Optional[jsii.Number] = None,
        preemptibility: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param accelerators: accelerators block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerators GoogleDataprocWorkflowTemplate#accelerators}
        :param disk_config: disk_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#disk_config GoogleDataprocWorkflowTemplate#disk_config}
        :param image: Optional. The Compute Engine image resource used for cluster instances. The URI can represent an image or image family. Image examples: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/[image-id]`` * ``projects/[project_id]/global/images/[image-id]`` * ``image-id`` Image family examples. Dataproc will use the most recent image from the family: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/family/[custom-image-family-name]`` * ``projects/[project_id]/global/images/family/[custom-image-family-name]`` If the URI is unspecified, it will be inferred from ``SoftwareConfig.image_version`` or the system default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#image GoogleDataprocWorkflowTemplate#image}
        :param machine_type: Optional. The Compute Engine machine type used for cluster instances. A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``n1-standard-2`` **Auto Zone Exception**: If you are using the Dataproc `Auto Zone Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`_ feature, you must use the short name of the machine type resource, for example, ``n1-standard-2``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#machine_type GoogleDataprocWorkflowTemplate#machine_type}
        :param min_cpu_platform: Optional. Specifies the minimum cpu platform for the Instance Group. See `Dataproc -> Minimum CPU Platform <https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-min-cpu>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#min_cpu_platform GoogleDataprocWorkflowTemplate#min_cpu_platform}
        :param num_instances: Optional. The number of VM instances in the instance group. For `HA cluster </dataproc/docs/concepts/configuring-clusters/high-availability>`_ `master_config <#FIELDS.master_config>`_ groups, **must be set to 3**. For standard cluster `master_config <#FIELDS.master_config>`_ groups, **must be set to 1**. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_instances GoogleDataprocWorkflowTemplate#num_instances}
        :param preemptibility: Optional. Specifies the preemptibility of the instance group. The default value for master and worker groups is ``NON_PREEMPTIBLE``. This default cannot be changed. The default value for secondary instances is ``PREEMPTIBLE``. Possible values: PREEMPTIBILITY_UNSPECIFIED, NON_PREEMPTIBLE, PREEMPTIBLE Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#preemptibility GoogleDataprocWorkflowTemplate#preemptibility}
        '''
        if isinstance(disk_config, dict):
            disk_config = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig(**disk_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig.__init__)
            check_type(argname="argument accelerators", value=accelerators, expected_type=type_hints["accelerators"])
            check_type(argname="argument disk_config", value=disk_config, expected_type=type_hints["disk_config"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            check_type(argname="argument min_cpu_platform", value=min_cpu_platform, expected_type=type_hints["min_cpu_platform"])
            check_type(argname="argument num_instances", value=num_instances, expected_type=type_hints["num_instances"])
            check_type(argname="argument preemptibility", value=preemptibility, expected_type=type_hints["preemptibility"])
        self._values: typing.Dict[str, typing.Any] = {}
        if accelerators is not None:
            self._values["accelerators"] = accelerators
        if disk_config is not None:
            self._values["disk_config"] = disk_config
        if image is not None:
            self._values["image"] = image
        if machine_type is not None:
            self._values["machine_type"] = machine_type
        if min_cpu_platform is not None:
            self._values["min_cpu_platform"] = min_cpu_platform
        if num_instances is not None:
            self._values["num_instances"] = num_instances
        if preemptibility is not None:
            self._values["preemptibility"] = preemptibility

    @builtins.property
    def accelerators(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators"]]]:
        '''accelerators block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerators GoogleDataprocWorkflowTemplate#accelerators}
        '''
        result = self._values.get("accelerators")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators"]]], result)

    @builtins.property
    def disk_config(
        self,
    ) -> typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig"]:
        '''disk_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#disk_config GoogleDataprocWorkflowTemplate#disk_config}
        '''
        result = self._values.get("disk_config")
        return typing.cast(typing.Optional["GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig"], result)

    @builtins.property
    def image(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The Compute Engine image resource used for cluster instances. The URI can represent an image or image family. Image examples: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/[image-id]`` * ``projects/[project_id]/global/images/[image-id]`` * ``image-id`` Image family examples. Dataproc will use the most recent image from the family: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/family/[custom-image-family-name]`` * ``projects/[project_id]/global/images/family/[custom-image-family-name]`` If the URI is unspecified, it will be inferred from ``SoftwareConfig.image_version`` or the system default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#image GoogleDataprocWorkflowTemplate#image}
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def machine_type(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The Compute Engine machine type used for cluster instances. A full URL, partial URI, or short name are valid. Examples: * ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2`` * ``n1-standard-2`` **Auto Zone Exception**: If you are using the Dataproc `Auto Zone Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`_ feature, you must use the short name of the machine type resource, for example, ``n1-standard-2``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#machine_type GoogleDataprocWorkflowTemplate#machine_type}
        '''
        result = self._values.get("machine_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_cpu_platform(self) -> typing.Optional[builtins.str]:
        '''Optional. Specifies the minimum cpu platform for the Instance Group. See `Dataproc -> Minimum CPU Platform <https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-min-cpu>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#min_cpu_platform GoogleDataprocWorkflowTemplate#min_cpu_platform}
        '''
        result = self._values.get("min_cpu_platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_instances(self) -> typing.Optional[jsii.Number]:
        '''Optional.

        The number of VM instances in the instance group. For `HA cluster </dataproc/docs/concepts/configuring-clusters/high-availability>`_ `master_config <#FIELDS.master_config>`_ groups, **must be set to 3**. For standard cluster `master_config <#FIELDS.master_config>`_ groups, **must be set to 1**.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_instances GoogleDataprocWorkflowTemplate#num_instances}
        '''
        result = self._values.get("num_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preemptibility(self) -> typing.Optional[builtins.str]:
        '''Optional.

        Specifies the preemptibility of the instance group. The default value for master and worker groups is ``NON_PREEMPTIBLE``. This default cannot be changed. The default value for secondary instances is ``PREEMPTIBLE``. Possible values: PREEMPTIBILITY_UNSPECIFIED, NON_PREEMPTIBLE, PREEMPTIBLE

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#preemptibility GoogleDataprocWorkflowTemplate#preemptibility}
        '''
        result = self._values.get("preemptibility")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators",
    jsii_struct_bases=[],
    name_mapping={
        "accelerator_count": "acceleratorCount",
        "accelerator_type": "acceleratorType",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators:
    def __init__(
        self,
        *,
        accelerator_count: typing.Optional[jsii.Number] = None,
        accelerator_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param accelerator_count: The number of the accelerator cards of this type exposed to this instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerator_count GoogleDataprocWorkflowTemplate#accelerator_count}
        :param accelerator_type: Full URL, partial URI, or short name of the accelerator type resource to expose to this instance. See `Compute Engine AcceleratorTypes <https://cloud.google.com/compute/docs/reference/beta/acceleratorTypes>`_. Examples: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/zones/us-east1-a/acceleratorTypes/nvidia-tesla-k80`` * ``projects/[project_id]/zones/us-east1-a/acceleratorTypes/nvidia-tesla-k80`` * ``nvidia-tesla-k80`` **Auto Zone Exception**: If you are using the Dataproc `Auto Zone Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`_ feature, you must use the short name of the accelerator type resource, for example, ``nvidia-tesla-k80``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerator_type GoogleDataprocWorkflowTemplate#accelerator_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators.__init__)
            check_type(argname="argument accelerator_count", value=accelerator_count, expected_type=type_hints["accelerator_count"])
            check_type(argname="argument accelerator_type", value=accelerator_type, expected_type=type_hints["accelerator_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if accelerator_count is not None:
            self._values["accelerator_count"] = accelerator_count
        if accelerator_type is not None:
            self._values["accelerator_type"] = accelerator_type

    @builtins.property
    def accelerator_count(self) -> typing.Optional[jsii.Number]:
        '''The number of the accelerator cards of this type exposed to this instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerator_count GoogleDataprocWorkflowTemplate#accelerator_count}
        '''
        result = self._values.get("accelerator_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def accelerator_type(self) -> typing.Optional[builtins.str]:
        '''Full URL, partial URI, or short name of the accelerator type resource to expose to this instance.

        See `Compute Engine AcceleratorTypes <https://cloud.google.com/compute/docs/reference/beta/acceleratorTypes>`_. Examples: * ``https://www.googleapis.com/compute/beta/projects/[project_id]/zones/us-east1-a/acceleratorTypes/nvidia-tesla-k80`` * ``projects/[project_id]/zones/us-east1-a/acceleratorTypes/nvidia-tesla-k80`` * ``nvidia-tesla-k80`` **Auto Zone Exception**: If you are using the Dataproc `Auto Zone Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`_ feature, you must use the short name of the accelerator type resource, for example, ``nvidia-tesla-k80``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#accelerator_type GoogleDataprocWorkflowTemplate#accelerator_type}
        '''
        result = self._values.get("accelerator_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsList",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAcceleratorCount")
    def reset_accelerator_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorCount", []))

    @jsii.member(jsii_name="resetAcceleratorType")
    def reset_accelerator_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorType", []))

    @builtins.property
    @jsii.member(jsii_name="acceleratorCountInput")
    def accelerator_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "acceleratorCountInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTypeInput")
    def accelerator_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceleratorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorCount")
    def accelerator_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "acceleratorCount"))

    @accelerator_count.setter
    def accelerator_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsOutputReference, "accelerator_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorCount", value)

    @builtins.property
    @jsii.member(jsii_name="acceleratorType")
    def accelerator_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acceleratorType"))

    @accelerator_type.setter
    def accelerator_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsOutputReference, "accelerator_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig",
    jsii_struct_bases=[],
    name_mapping={
        "boot_disk_size_gb": "bootDiskSizeGb",
        "boot_disk_type": "bootDiskType",
        "num_local_ssds": "numLocalSsds",
    },
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig:
    def __init__(
        self,
        *,
        boot_disk_size_gb: typing.Optional[jsii.Number] = None,
        boot_disk_type: typing.Optional[builtins.str] = None,
        num_local_ssds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param boot_disk_size_gb: Optional. Size in GB of the boot disk (default is 500GB). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_size_gb GoogleDataprocWorkflowTemplate#boot_disk_size_gb}
        :param boot_disk_type: Optional. Type of the boot disk (default is "pd-standard"). Valid values: "pd-balanced" (Persistent Disk Balanced Solid State Drive), "pd-ssd" (Persistent Disk Solid State Drive), or "pd-standard" (Persistent Disk Hard Disk Drive). See `Disk types <https://cloud.google.com/compute/docs/disks#disk-types>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_type GoogleDataprocWorkflowTemplate#boot_disk_type}
        :param num_local_ssds: Optional. Number of attached SSDs, from 0 to 4 (default is 0). If SSDs are not attached, the boot disk is used to store runtime logs and `HDFS <https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html>`_ data. If one or more SSDs are attached, this runtime bulk data is spread across them, and the boot disk contains only basic config and installed binaries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_local_ssds GoogleDataprocWorkflowTemplate#num_local_ssds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig.__init__)
            check_type(argname="argument boot_disk_size_gb", value=boot_disk_size_gb, expected_type=type_hints["boot_disk_size_gb"])
            check_type(argname="argument boot_disk_type", value=boot_disk_type, expected_type=type_hints["boot_disk_type"])
            check_type(argname="argument num_local_ssds", value=num_local_ssds, expected_type=type_hints["num_local_ssds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if boot_disk_size_gb is not None:
            self._values["boot_disk_size_gb"] = boot_disk_size_gb
        if boot_disk_type is not None:
            self._values["boot_disk_type"] = boot_disk_type
        if num_local_ssds is not None:
            self._values["num_local_ssds"] = num_local_ssds

    @builtins.property
    def boot_disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Optional. Size in GB of the boot disk (default is 500GB).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_size_gb GoogleDataprocWorkflowTemplate#boot_disk_size_gb}
        '''
        result = self._values.get("boot_disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def boot_disk_type(self) -> typing.Optional[builtins.str]:
        '''Optional.

        Type of the boot disk (default is "pd-standard"). Valid values: "pd-balanced" (Persistent Disk Balanced Solid State Drive), "pd-ssd" (Persistent Disk Solid State Drive), or "pd-standard" (Persistent Disk Hard Disk Drive). See `Disk types <https://cloud.google.com/compute/docs/disks#disk-types>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_type GoogleDataprocWorkflowTemplate#boot_disk_type}
        '''
        result = self._values.get("boot_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_local_ssds(self) -> typing.Optional[jsii.Number]:
        '''Optional.

        Number of attached SSDs, from 0 to 4 (default is 0). If SSDs are not attached, the boot disk is used to store runtime logs and `HDFS <https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html>`_ data. If one or more SSDs are attached, this runtime bulk data is spread across them, and the boot disk contains only basic config and installed binaries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_local_ssds GoogleDataprocWorkflowTemplate#num_local_ssds}
        '''
        result = self._values.get("num_local_ssds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBootDiskSizeGb")
    def reset_boot_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskSizeGb", []))

    @jsii.member(jsii_name="resetBootDiskType")
    def reset_boot_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskType", []))

    @jsii.member(jsii_name="resetNumLocalSsds")
    def reset_num_local_ssds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumLocalSsds", []))

    @builtins.property
    @jsii.member(jsii_name="bootDiskSizeGbInput")
    def boot_disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bootDiskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskTypeInput")
    def boot_disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootDiskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="numLocalSsdsInput")
    def num_local_ssds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numLocalSsdsInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bootDiskSizeGb"))

    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigOutputReference, "boot_disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="bootDiskType")
    def boot_disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootDiskType"))

    @boot_disk_type.setter
    def boot_disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigOutputReference, "boot_disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskType", value)

    @builtins.property
    @jsii.member(jsii_name="numLocalSsds")
    def num_local_ssds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numLocalSsds"))

    @num_local_ssds.setter
    def num_local_ssds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigOutputReference, "num_local_ssds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numLocalSsds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfig",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfig:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigList",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="instanceGroupManagerName")
    def instance_group_manager_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceGroupManagerName"))

    @builtins.property
    @jsii.member(jsii_name="instanceTemplateName")
    def instance_template_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceTemplateName"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAccelerators")
    def put_accelerators(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigOutputReference.put_accelerators)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccelerators", [value]))

    @jsii.member(jsii_name="putDiskConfig")
    def put_disk_config(
        self,
        *,
        boot_disk_size_gb: typing.Optional[jsii.Number] = None,
        boot_disk_type: typing.Optional[builtins.str] = None,
        num_local_ssds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param boot_disk_size_gb: Optional. Size in GB of the boot disk (default is 500GB). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_size_gb GoogleDataprocWorkflowTemplate#boot_disk_size_gb}
        :param boot_disk_type: Optional. Type of the boot disk (default is "pd-standard"). Valid values: "pd-balanced" (Persistent Disk Balanced Solid State Drive), "pd-ssd" (Persistent Disk Solid State Drive), or "pd-standard" (Persistent Disk Hard Disk Drive). See `Disk types <https://cloud.google.com/compute/docs/disks#disk-types>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#boot_disk_type GoogleDataprocWorkflowTemplate#boot_disk_type}
        :param num_local_ssds: Optional. Number of attached SSDs, from 0 to 4 (default is 0). If SSDs are not attached, the boot disk is used to store runtime logs and `HDFS <https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html>`_ data. If one or more SSDs are attached, this runtime bulk data is spread across them, and the boot disk contains only basic config and installed binaries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#num_local_ssds GoogleDataprocWorkflowTemplate#num_local_ssds}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig(
            boot_disk_size_gb=boot_disk_size_gb,
            boot_disk_type=boot_disk_type,
            num_local_ssds=num_local_ssds,
        )

        return typing.cast(None, jsii.invoke(self, "putDiskConfig", [value]))

    @jsii.member(jsii_name="resetAccelerators")
    def reset_accelerators(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccelerators", []))

    @jsii.member(jsii_name="resetDiskConfig")
    def reset_disk_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskConfig", []))

    @jsii.member(jsii_name="resetImage")
    def reset_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImage", []))

    @jsii.member(jsii_name="resetMachineType")
    def reset_machine_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineType", []))

    @jsii.member(jsii_name="resetMinCpuPlatform")
    def reset_min_cpu_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCpuPlatform", []))

    @jsii.member(jsii_name="resetNumInstances")
    def reset_num_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumInstances", []))

    @jsii.member(jsii_name="resetPreemptibility")
    def reset_preemptibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreemptibility", []))

    @builtins.property
    @jsii.member(jsii_name="accelerators")
    def accelerators(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsList:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsList, jsii.get(self, "accelerators"))

    @builtins.property
    @jsii.member(jsii_name="diskConfig")
    def disk_config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigOutputReference, jsii.get(self, "diskConfig"))

    @builtins.property
    @jsii.member(jsii_name="instanceNames")
    def instance_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceNames"))

    @builtins.property
    @jsii.member(jsii_name="isPreemptible")
    def is_preemptible(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "isPreemptible"))

    @builtins.property
    @jsii.member(jsii_name="managedGroupConfig")
    def managed_group_config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigList:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigList, jsii.get(self, "managedGroupConfig"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorsInput")
    def accelerators_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators]]], jsii.get(self, "acceleratorsInput"))

    @builtins.property
    @jsii.member(jsii_name="diskConfigInput")
    def disk_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig], jsii.get(self, "diskConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatformInput")
    def min_cpu_platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minCpuPlatformInput"))

    @builtins.property
    @jsii.member(jsii_name="numInstancesInput")
    def num_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="preemptibilityInput")
    def preemptibility_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preemptibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigOutputReference, "image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "image", value)

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigOutputReference, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatform")
    def min_cpu_platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minCpuPlatform"))

    @min_cpu_platform.setter
    def min_cpu_platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigOutputReference, "min_cpu_platform").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCpuPlatform", value)

    @builtins.property
    @jsii.member(jsii_name="numInstances")
    def num_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numInstances"))

    @num_instances.setter
    def num_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigOutputReference, "num_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numInstances", value)

    @builtins.property
    @jsii.member(jsii_name="preemptibility")
    def preemptibility(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preemptibility"))

    @preemptibility.setter
    def preemptibility(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigOutputReference, "preemptibility").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preemptibility", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplatePlacementManagedClusterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementManagedClusterOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementManagedClusterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConfig")
    def put_config(
        self,
        *,
        autoscaling_config: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig, typing.Dict[str, typing.Any]]] = None,
        encryption_config: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig, typing.Dict[str, typing.Any]]] = None,
        endpoint_config: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig, typing.Dict[str, typing.Any]]] = None,
        gce_cluster_config: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig, typing.Dict[str, typing.Any]]] = None,
        gke_cluster_config: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig, typing.Dict[str, typing.Any]]] = None,
        initialization_actions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions, typing.Dict[str, typing.Any]]]]] = None,
        lifecycle_config: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig, typing.Dict[str, typing.Any]]] = None,
        master_config: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig, typing.Dict[str, typing.Any]]] = None,
        metastore_config: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig, typing.Dict[str, typing.Any]]] = None,
        secondary_worker_config: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig, typing.Dict[str, typing.Any]]] = None,
        security_config: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig, typing.Dict[str, typing.Any]]] = None,
        software_config: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig, typing.Dict[str, typing.Any]]] = None,
        staging_bucket: typing.Optional[builtins.str] = None,
        temp_bucket: typing.Optional[builtins.str] = None,
        worker_config: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param autoscaling_config: autoscaling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#autoscaling_config GoogleDataprocWorkflowTemplate#autoscaling_config}
        :param encryption_config: encryption_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#encryption_config GoogleDataprocWorkflowTemplate#encryption_config}
        :param endpoint_config: endpoint_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#endpoint_config GoogleDataprocWorkflowTemplate#endpoint_config}
        :param gce_cluster_config: gce_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#gce_cluster_config GoogleDataprocWorkflowTemplate#gce_cluster_config}
        :param gke_cluster_config: gke_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#gke_cluster_config GoogleDataprocWorkflowTemplate#gke_cluster_config}
        :param initialization_actions: initialization_actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#initialization_actions GoogleDataprocWorkflowTemplate#initialization_actions}
        :param lifecycle_config: lifecycle_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#lifecycle_config GoogleDataprocWorkflowTemplate#lifecycle_config}
        :param master_config: master_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#master_config GoogleDataprocWorkflowTemplate#master_config}
        :param metastore_config: metastore_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#metastore_config GoogleDataprocWorkflowTemplate#metastore_config}
        :param secondary_worker_config: secondary_worker_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#secondary_worker_config GoogleDataprocWorkflowTemplate#secondary_worker_config}
        :param security_config: security_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#security_config GoogleDataprocWorkflowTemplate#security_config}
        :param software_config: software_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#software_config GoogleDataprocWorkflowTemplate#software_config}
        :param staging_bucket: Optional. A Cloud Storage bucket used to stage job dependencies, config files, and job driver console output. If you do not specify a staging bucket, Cloud Dataproc will determine a Cloud Storage location (US, ASIA, or EU) for your cluster's staging bucket according to the Compute Engine zone where your cluster is deployed, and then create and manage this project-level, per-location bucket (see `Dataproc staging bucket <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/staging-bucket>`_). **This field requires a Cloud Storage bucket name, not a URI to a Cloud Storage bucket.** Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#staging_bucket GoogleDataprocWorkflowTemplate#staging_bucket}
        :param temp_bucket: Optional. A Cloud Storage bucket used to store ephemeral cluster and jobs data, such as Spark and MapReduce history files. If you do not specify a temp bucket, Dataproc will determine a Cloud Storage location (US, ASIA, or EU) for your cluster's temp bucket according to the Compute Engine zone where your cluster is deployed, and then create and manage this project-level, per-location bucket. The default bucket has a TTL of 90 days, but you can use any TTL (or none) if you specify a bucket. **This field requires a Cloud Storage bucket name, not a URI to a Cloud Storage bucket.** Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#temp_bucket GoogleDataprocWorkflowTemplate#temp_bucket}
        :param worker_config: worker_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#worker_config GoogleDataprocWorkflowTemplate#worker_config}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig(
            autoscaling_config=autoscaling_config,
            encryption_config=encryption_config,
            endpoint_config=endpoint_config,
            gce_cluster_config=gce_cluster_config,
            gke_cluster_config=gke_cluster_config,
            initialization_actions=initialization_actions,
            lifecycle_config=lifecycle_config,
            master_config=master_config,
            metastore_config=metastore_config,
            secondary_worker_config=secondary_worker_config,
            security_config=security_config,
            software_config=software_config,
            staging_bucket=staging_bucket,
            temp_bucket=temp_bucket,
            worker_config=worker_config,
        )

        return typing.cast(None, jsii.invoke(self, "putConfig", [value]))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigOutputReference, jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="configInput")
    def config_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig], jsii.get(self, "configInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterOutputReference, "cluster_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedCluster]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedCluster], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedCluster],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementManagedClusterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocWorkflowTemplatePlacementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplatePlacementOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplatePlacementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClusterSelector")
    def put_cluster_selector(
        self,
        *,
        cluster_labels: typing.Mapping[builtins.str, builtins.str],
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_labels: Required. The cluster labels. Cluster must have all labels to match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cluster_labels GoogleDataprocWorkflowTemplate#cluster_labels}
        :param zone: Optional. The zone where workflow process executes. This parameter does not affect the selection of the cluster. If unspecified, the zone of the first cluster matching the selector is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#zone GoogleDataprocWorkflowTemplate#zone}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementClusterSelector(
            cluster_labels=cluster_labels, zone=zone
        )

        return typing.cast(None, jsii.invoke(self, "putClusterSelector", [value]))

    @jsii.member(jsii_name="putManagedCluster")
    def put_managed_cluster(
        self,
        *,
        cluster_name: builtins.str,
        config: typing.Union[GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig, typing.Dict[str, typing.Any]],
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param cluster_name: Required. The cluster name prefix. A unique cluster name will be formed by appending a random suffix. The name must contain only lower-case letters (a-z), numbers (0-9), and hyphens (-). Must begin with a letter. Cannot begin or end with hyphen. Must consist of between 2 and 35 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#cluster_name GoogleDataprocWorkflowTemplate#cluster_name}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#config GoogleDataprocWorkflowTemplate#config}
        :param labels: Optional. The labels to associate with this cluster. Label keys must be between 1 and 63 characters long, and must conform to the following PCRE regular expression: p{Ll}p{Lo}{0,62} Label values must be between 1 and 63 characters long, and must conform to the following PCRE regular expression: [p{Ll}p{Lo}p{N}_-]{0,63} No more than 32 labels can be associated with a given cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#labels GoogleDataprocWorkflowTemplate#labels}
        '''
        value = GoogleDataprocWorkflowTemplatePlacementManagedCluster(
            cluster_name=cluster_name, config=config, labels=labels
        )

        return typing.cast(None, jsii.invoke(self, "putManagedCluster", [value]))

    @jsii.member(jsii_name="resetClusterSelector")
    def reset_cluster_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterSelector", []))

    @jsii.member(jsii_name="resetManagedCluster")
    def reset_managed_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedCluster", []))

    @builtins.property
    @jsii.member(jsii_name="clusterSelector")
    def cluster_selector(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementClusterSelectorOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementClusterSelectorOutputReference, jsii.get(self, "clusterSelector"))

    @builtins.property
    @jsii.member(jsii_name="managedCluster")
    def managed_cluster(
        self,
    ) -> GoogleDataprocWorkflowTemplatePlacementManagedClusterOutputReference:
        return typing.cast(GoogleDataprocWorkflowTemplatePlacementManagedClusterOutputReference, jsii.get(self, "managedCluster"))

    @builtins.property
    @jsii.member(jsii_name="clusterSelectorInput")
    def cluster_selector_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementClusterSelector]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementClusterSelector], jsii.get(self, "clusterSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="managedClusterInput")
    def managed_cluster_input(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedCluster]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacementManagedCluster], jsii.get(self, "managedClusterInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocWorkflowTemplatePlacement]:
        return typing.cast(typing.Optional[GoogleDataprocWorkflowTemplatePlacement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocWorkflowTemplatePlacement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplatePlacementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GoogleDataprocWorkflowTemplateTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#create GoogleDataprocWorkflowTemplate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#delete GoogleDataprocWorkflowTemplate#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#create GoogleDataprocWorkflowTemplate#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_workflow_template#delete GoogleDataprocWorkflowTemplate#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocWorkflowTemplateTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocWorkflowTemplateTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocWorkflowTemplate.GoogleDataprocWorkflowTemplateTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocWorkflowTemplateTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataprocWorkflowTemplateTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataprocWorkflowTemplateTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataprocWorkflowTemplateTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocWorkflowTemplateTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDataprocWorkflowTemplate",
    "GoogleDataprocWorkflowTemplateConfig",
    "GoogleDataprocWorkflowTemplateJobs",
    "GoogleDataprocWorkflowTemplateJobsHadoopJob",
    "GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfig",
    "GoogleDataprocWorkflowTemplateJobsHadoopJobLoggingConfigOutputReference",
    "GoogleDataprocWorkflowTemplateJobsHadoopJobOutputReference",
    "GoogleDataprocWorkflowTemplateJobsHiveJob",
    "GoogleDataprocWorkflowTemplateJobsHiveJobOutputReference",
    "GoogleDataprocWorkflowTemplateJobsHiveJobQueryList",
    "GoogleDataprocWorkflowTemplateJobsHiveJobQueryListOutputReference",
    "GoogleDataprocWorkflowTemplateJobsList",
    "GoogleDataprocWorkflowTemplateJobsOutputReference",
    "GoogleDataprocWorkflowTemplateJobsPigJob",
    "GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfig",
    "GoogleDataprocWorkflowTemplateJobsPigJobLoggingConfigOutputReference",
    "GoogleDataprocWorkflowTemplateJobsPigJobOutputReference",
    "GoogleDataprocWorkflowTemplateJobsPigJobQueryList",
    "GoogleDataprocWorkflowTemplateJobsPigJobQueryListOutputReference",
    "GoogleDataprocWorkflowTemplateJobsPrestoJob",
    "GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfig",
    "GoogleDataprocWorkflowTemplateJobsPrestoJobLoggingConfigOutputReference",
    "GoogleDataprocWorkflowTemplateJobsPrestoJobOutputReference",
    "GoogleDataprocWorkflowTemplateJobsPrestoJobQueryList",
    "GoogleDataprocWorkflowTemplateJobsPrestoJobQueryListOutputReference",
    "GoogleDataprocWorkflowTemplateJobsPysparkJob",
    "GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfig",
    "GoogleDataprocWorkflowTemplateJobsPysparkJobLoggingConfigOutputReference",
    "GoogleDataprocWorkflowTemplateJobsPysparkJobOutputReference",
    "GoogleDataprocWorkflowTemplateJobsScheduling",
    "GoogleDataprocWorkflowTemplateJobsSchedulingOutputReference",
    "GoogleDataprocWorkflowTemplateJobsSparkJob",
    "GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfig",
    "GoogleDataprocWorkflowTemplateJobsSparkJobLoggingConfigOutputReference",
    "GoogleDataprocWorkflowTemplateJobsSparkJobOutputReference",
    "GoogleDataprocWorkflowTemplateJobsSparkRJob",
    "GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfig",
    "GoogleDataprocWorkflowTemplateJobsSparkRJobLoggingConfigOutputReference",
    "GoogleDataprocWorkflowTemplateJobsSparkRJobOutputReference",
    "GoogleDataprocWorkflowTemplateJobsSparkSqlJob",
    "GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfig",
    "GoogleDataprocWorkflowTemplateJobsSparkSqlJobLoggingConfigOutputReference",
    "GoogleDataprocWorkflowTemplateJobsSparkSqlJobOutputReference",
    "GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryList",
    "GoogleDataprocWorkflowTemplateJobsSparkSqlJobQueryListOutputReference",
    "GoogleDataprocWorkflowTemplateParameters",
    "GoogleDataprocWorkflowTemplateParametersList",
    "GoogleDataprocWorkflowTemplateParametersOutputReference",
    "GoogleDataprocWorkflowTemplateParametersValidation",
    "GoogleDataprocWorkflowTemplateParametersValidationOutputReference",
    "GoogleDataprocWorkflowTemplateParametersValidationRegex",
    "GoogleDataprocWorkflowTemplateParametersValidationRegexOutputReference",
    "GoogleDataprocWorkflowTemplateParametersValidationValues",
    "GoogleDataprocWorkflowTemplateParametersValidationValuesOutputReference",
    "GoogleDataprocWorkflowTemplatePlacement",
    "GoogleDataprocWorkflowTemplatePlacementClusterSelector",
    "GoogleDataprocWorkflowTemplatePlacementClusterSelectorOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedCluster",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigAutoscalingConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEncryptionConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigEndpointConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinityOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTargetOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActions",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsList",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigInitializationActionsOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigLifecycleConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerators",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsList",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorsOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigList",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMasterConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigMetastoreConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerators",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsList",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorsOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigList",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSecurityConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigSoftwareConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerators",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsList",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorsOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfig",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigList",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterConfigWorkerConfigOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementManagedClusterOutputReference",
    "GoogleDataprocWorkflowTemplatePlacementOutputReference",
    "GoogleDataprocWorkflowTemplateTimeouts",
    "GoogleDataprocWorkflowTemplateTimeoutsOutputReference",
]

publication.publish()
