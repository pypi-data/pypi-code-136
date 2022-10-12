'''
# `google_clouddeploy_target`

Refer to the Terraform Registory for docs: [`google_clouddeploy_target`](https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target).
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


class GoogleClouddeployTarget(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleClouddeployTarget.GoogleClouddeployTarget",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target google_clouddeploy_target}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        anthos_cluster: typing.Optional[typing.Union["GoogleClouddeployTargetAnthosCluster", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleClouddeployTargetExecutionConfigs", typing.Dict[str, typing.Any]]]]] = None,
        gke: typing.Optional[typing.Union["GoogleClouddeployTargetGke", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        require_approval: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleClouddeployTargetTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target google_clouddeploy_target} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#location GoogleClouddeployTarget#location}
        :param name: Name of the ``Target``. Format is [a-z][a-z0-9-]{0,62}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#name GoogleClouddeployTarget#name}
        :param annotations: Optional. User annotations. These attributes can only be set and used by the user, and not by Google Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#annotations GoogleClouddeployTarget#annotations}
        :param anthos_cluster: anthos_cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#anthos_cluster GoogleClouddeployTarget#anthos_cluster}
        :param description: Optional. Description of the ``Target``. Max length is 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#description GoogleClouddeployTarget#description}
        :param execution_configs: execution_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#execution_configs GoogleClouddeployTarget#execution_configs}
        :param gke: gke block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#gke GoogleClouddeployTarget#gke}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#id GoogleClouddeployTarget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Optional. Labels are attributes that can be set and used by both the user and by Google Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128 bytes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#labels GoogleClouddeployTarget#labels}
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#project GoogleClouddeployTarget#project}
        :param require_approval: Optional. Whether or not the ``Target`` requires approval. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#require_approval GoogleClouddeployTarget#require_approval}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#timeouts GoogleClouddeployTarget#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleClouddeployTarget.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleClouddeployTargetConfig(
            location=location,
            name=name,
            annotations=annotations,
            anthos_cluster=anthos_cluster,
            description=description,
            execution_configs=execution_configs,
            gke=gke,
            id=id,
            labels=labels,
            project=project,
            require_approval=require_approval,
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

    @jsii.member(jsii_name="putAnthosCluster")
    def put_anthos_cluster(
        self,
        *,
        membership: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param membership: Membership of the GKE Hub-registered cluster to which to apply the Skaffold configuration. Format is ``projects/{project}/locations/{location}/memberships/{membership_name}``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#membership GoogleClouddeployTarget#membership}
        '''
        value = GoogleClouddeployTargetAnthosCluster(membership=membership)

        return typing.cast(None, jsii.invoke(self, "putAnthosCluster", [value]))

    @jsii.member(jsii_name="putExecutionConfigs")
    def put_execution_configs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleClouddeployTargetExecutionConfigs", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleClouddeployTarget.put_execution_configs)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExecutionConfigs", [value]))

    @jsii.member(jsii_name="putGke")
    def put_gke(
        self,
        *,
        cluster: typing.Optional[builtins.str] = None,
        internal_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cluster: Information specifying a GKE Cluster. Format is `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#cluster GoogleClouddeployTarget#cluster}
        :param internal_ip: Optional. If true, ``cluster`` is accessed using the private IP address of the control plane endpoint. Otherwise, the default IP address of the control plane endpoint is used. The default IP address is the private IP address for clusters with private control-plane endpoints and the public IP address otherwise. Only specify this option when ``cluster`` is a `private GKE cluster <https://cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#internal_ip GoogleClouddeployTarget#internal_ip}
        '''
        value = GoogleClouddeployTargetGke(cluster=cluster, internal_ip=internal_ip)

        return typing.cast(None, jsii.invoke(self, "putGke", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#create GoogleClouddeployTarget#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#delete GoogleClouddeployTarget#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#update GoogleClouddeployTarget#update}.
        '''
        value = GoogleClouddeployTargetTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetAnthosCluster")
    def reset_anthos_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnthosCluster", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExecutionConfigs")
    def reset_execution_configs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionConfigs", []))

    @jsii.member(jsii_name="resetGke")
    def reset_gke(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGke", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRequireApproval")
    def reset_require_approval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireApproval", []))

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
    @jsii.member(jsii_name="anthosCluster")
    def anthos_cluster(self) -> "GoogleClouddeployTargetAnthosClusterOutputReference":
        return typing.cast("GoogleClouddeployTargetAnthosClusterOutputReference", jsii.get(self, "anthosCluster"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="executionConfigs")
    def execution_configs(self) -> "GoogleClouddeployTargetExecutionConfigsList":
        return typing.cast("GoogleClouddeployTargetExecutionConfigsList", jsii.get(self, "executionConfigs"))

    @builtins.property
    @jsii.member(jsii_name="gke")
    def gke(self) -> "GoogleClouddeployTargetGkeOutputReference":
        return typing.cast("GoogleClouddeployTargetGkeOutputReference", jsii.get(self, "gke"))

    @builtins.property
    @jsii.member(jsii_name="targetId")
    def target_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleClouddeployTargetTimeoutsOutputReference":
        return typing.cast("GoogleClouddeployTargetTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "annotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="anthosClusterInput")
    def anthos_cluster_input(
        self,
    ) -> typing.Optional["GoogleClouddeployTargetAnthosCluster"]:
        return typing.cast(typing.Optional["GoogleClouddeployTargetAnthosCluster"], jsii.get(self, "anthosClusterInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="executionConfigsInput")
    def execution_configs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleClouddeployTargetExecutionConfigs"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleClouddeployTargetExecutionConfigs"]]], jsii.get(self, "executionConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="gkeInput")
    def gke_input(self) -> typing.Optional["GoogleClouddeployTargetGke"]:
        return typing.cast(typing.Optional["GoogleClouddeployTargetGke"], jsii.get(self, "gkeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

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
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="requireApprovalInput")
    def require_approval_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireApprovalInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleClouddeployTargetTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleClouddeployTargetTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTarget, "annotations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTarget, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTarget, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTarget, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTarget, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTarget, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTarget, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="requireApproval")
    def require_approval(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireApproval"))

    @require_approval.setter
    def require_approval(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTarget, "require_approval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireApproval", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleClouddeployTarget.GoogleClouddeployTargetAnthosCluster",
    jsii_struct_bases=[],
    name_mapping={"membership": "membership"},
)
class GoogleClouddeployTargetAnthosCluster:
    def __init__(self, *, membership: typing.Optional[builtins.str] = None) -> None:
        '''
        :param membership: Membership of the GKE Hub-registered cluster to which to apply the Skaffold configuration. Format is ``projects/{project}/locations/{location}/memberships/{membership_name}``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#membership GoogleClouddeployTarget#membership}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleClouddeployTargetAnthosCluster.__init__)
            check_type(argname="argument membership", value=membership, expected_type=type_hints["membership"])
        self._values: typing.Dict[str, typing.Any] = {}
        if membership is not None:
            self._values["membership"] = membership

    @builtins.property
    def membership(self) -> typing.Optional[builtins.str]:
        '''Membership of the GKE Hub-registered cluster to which to apply the Skaffold configuration. Format is ``projects/{project}/locations/{location}/memberships/{membership_name}``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#membership GoogleClouddeployTarget#membership}
        '''
        result = self._values.get("membership")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleClouddeployTargetAnthosCluster(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleClouddeployTargetAnthosClusterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleClouddeployTarget.GoogleClouddeployTargetAnthosClusterOutputReference",
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
            type_hints = typing.get_type_hints(GoogleClouddeployTargetAnthosClusterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMembership")
    def reset_membership(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMembership", []))

    @builtins.property
    @jsii.member(jsii_name="membershipInput")
    def membership_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "membershipInput"))

    @builtins.property
    @jsii.member(jsii_name="membership")
    def membership(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "membership"))

    @membership.setter
    def membership(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetAnthosClusterOutputReference, "membership").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "membership", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleClouddeployTargetAnthosCluster]:
        return typing.cast(typing.Optional[GoogleClouddeployTargetAnthosCluster], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleClouddeployTargetAnthosCluster],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetAnthosClusterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleClouddeployTarget.GoogleClouddeployTargetConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "annotations": "annotations",
        "anthos_cluster": "anthosCluster",
        "description": "description",
        "execution_configs": "executionConfigs",
        "gke": "gke",
        "id": "id",
        "labels": "labels",
        "project": "project",
        "require_approval": "requireApproval",
        "timeouts": "timeouts",
    },
)
class GoogleClouddeployTargetConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        anthos_cluster: typing.Optional[typing.Union[GoogleClouddeployTargetAnthosCluster, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleClouddeployTargetExecutionConfigs", typing.Dict[str, typing.Any]]]]] = None,
        gke: typing.Optional[typing.Union["GoogleClouddeployTargetGke", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        require_approval: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleClouddeployTargetTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#location GoogleClouddeployTarget#location}
        :param name: Name of the ``Target``. Format is [a-z][a-z0-9-]{0,62}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#name GoogleClouddeployTarget#name}
        :param annotations: Optional. User annotations. These attributes can only be set and used by the user, and not by Google Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#annotations GoogleClouddeployTarget#annotations}
        :param anthos_cluster: anthos_cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#anthos_cluster GoogleClouddeployTarget#anthos_cluster}
        :param description: Optional. Description of the ``Target``. Max length is 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#description GoogleClouddeployTarget#description}
        :param execution_configs: execution_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#execution_configs GoogleClouddeployTarget#execution_configs}
        :param gke: gke block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#gke GoogleClouddeployTarget#gke}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#id GoogleClouddeployTarget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Optional. Labels are attributes that can be set and used by both the user and by Google Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128 bytes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#labels GoogleClouddeployTarget#labels}
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#project GoogleClouddeployTarget#project}
        :param require_approval: Optional. Whether or not the ``Target`` requires approval. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#require_approval GoogleClouddeployTarget#require_approval}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#timeouts GoogleClouddeployTarget#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(anthos_cluster, dict):
            anthos_cluster = GoogleClouddeployTargetAnthosCluster(**anthos_cluster)
        if isinstance(gke, dict):
            gke = GoogleClouddeployTargetGke(**gke)
        if isinstance(timeouts, dict):
            timeouts = GoogleClouddeployTargetTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleClouddeployTargetConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument anthos_cluster", value=anthos_cluster, expected_type=type_hints["anthos_cluster"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_configs", value=execution_configs, expected_type=type_hints["execution_configs"])
            check_type(argname="argument gke", value=gke, expected_type=type_hints["gke"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument require_approval", value=require_approval, expected_type=type_hints["require_approval"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
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
        if annotations is not None:
            self._values["annotations"] = annotations
        if anthos_cluster is not None:
            self._values["anthos_cluster"] = anthos_cluster
        if description is not None:
            self._values["description"] = description
        if execution_configs is not None:
            self._values["execution_configs"] = execution_configs
        if gke is not None:
            self._values["gke"] = gke
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if project is not None:
            self._values["project"] = project
        if require_approval is not None:
            self._values["require_approval"] = require_approval
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
    def location(self) -> builtins.str:
        '''The location for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#location GoogleClouddeployTarget#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the ``Target``. Format is [a-z][a-z0-9-]{0,62}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#name GoogleClouddeployTarget#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        User annotations. These attributes can only be set and used by the user, and not by Google Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#annotations GoogleClouddeployTarget#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def anthos_cluster(self) -> typing.Optional[GoogleClouddeployTargetAnthosCluster]:
        '''anthos_cluster block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#anthos_cluster GoogleClouddeployTarget#anthos_cluster}
        '''
        result = self._values.get("anthos_cluster")
        return typing.cast(typing.Optional[GoogleClouddeployTargetAnthosCluster], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Optional. Description of the ``Target``. Max length is 255 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#description GoogleClouddeployTarget#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_configs(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleClouddeployTargetExecutionConfigs"]]]:
        '''execution_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#execution_configs GoogleClouddeployTarget#execution_configs}
        '''
        result = self._values.get("execution_configs")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleClouddeployTargetExecutionConfigs"]]], result)

    @builtins.property
    def gke(self) -> typing.Optional["GoogleClouddeployTargetGke"]:
        '''gke block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#gke GoogleClouddeployTarget#gke}
        '''
        result = self._values.get("gke")
        return typing.cast(typing.Optional["GoogleClouddeployTargetGke"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#id GoogleClouddeployTarget#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        Labels are attributes that can be set and used by both the user and by Google Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128 bytes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#labels GoogleClouddeployTarget#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#project GoogleClouddeployTarget#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def require_approval(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional. Whether or not the ``Target`` requires approval.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#require_approval GoogleClouddeployTarget#require_approval}
        '''
        result = self._values.get("require_approval")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleClouddeployTargetTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#timeouts GoogleClouddeployTarget#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleClouddeployTargetTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleClouddeployTargetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleClouddeployTarget.GoogleClouddeployTargetExecutionConfigs",
    jsii_struct_bases=[],
    name_mapping={
        "usages": "usages",
        "artifact_storage": "artifactStorage",
        "service_account": "serviceAccount",
        "worker_pool": "workerPool",
    },
)
class GoogleClouddeployTargetExecutionConfigs:
    def __init__(
        self,
        *,
        usages: typing.Sequence[builtins.str],
        artifact_storage: typing.Optional[builtins.str] = None,
        service_account: typing.Optional[builtins.str] = None,
        worker_pool: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param usages: Required. Usages when this configuration should be applied. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#usages GoogleClouddeployTarget#usages}
        :param artifact_storage: Optional. Cloud Storage location in which to store execution outputs. This can either be a bucket ("gs://my-bucket") or a path within a bucket ("gs://my-bucket/my-dir"). If unspecified, a default bucket located in the same region will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#artifact_storage GoogleClouddeployTarget#artifact_storage}
        :param service_account: Optional. Google service account to use for execution. If unspecified, the project execution service account (-compute@developer.gserviceaccount.com) is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#service_account GoogleClouddeployTarget#service_account}
        :param worker_pool: Optional. The resource name of the ``WorkerPool``, with the format ``projects/{project}/locations/{location}/workerPools/{worker_pool}``. If this optional field is unspecified, the default Cloud Build pool will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#worker_pool GoogleClouddeployTarget#worker_pool}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleClouddeployTargetExecutionConfigs.__init__)
            check_type(argname="argument usages", value=usages, expected_type=type_hints["usages"])
            check_type(argname="argument artifact_storage", value=artifact_storage, expected_type=type_hints["artifact_storage"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument worker_pool", value=worker_pool, expected_type=type_hints["worker_pool"])
        self._values: typing.Dict[str, typing.Any] = {
            "usages": usages,
        }
        if artifact_storage is not None:
            self._values["artifact_storage"] = artifact_storage
        if service_account is not None:
            self._values["service_account"] = service_account
        if worker_pool is not None:
            self._values["worker_pool"] = worker_pool

    @builtins.property
    def usages(self) -> typing.List[builtins.str]:
        '''Required. Usages when this configuration should be applied.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#usages GoogleClouddeployTarget#usages}
        '''
        result = self._values.get("usages")
        assert result is not None, "Required property 'usages' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def artifact_storage(self) -> typing.Optional[builtins.str]:
        '''Optional.

        Cloud Storage location in which to store execution outputs. This can either be a bucket ("gs://my-bucket") or a path within a bucket ("gs://my-bucket/my-dir"). If unspecified, a default bucket located in the same region will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#artifact_storage GoogleClouddeployTarget#artifact_storage}
        '''
        result = self._values.get("artifact_storage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''Optional. Google service account to use for execution. If unspecified, the project execution service account (-compute@developer.gserviceaccount.com) is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#service_account GoogleClouddeployTarget#service_account}
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def worker_pool(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The resource name of the ``WorkerPool``, with the format ``projects/{project}/locations/{location}/workerPools/{worker_pool}``. If this optional field is unspecified, the default Cloud Build pool will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#worker_pool GoogleClouddeployTarget#worker_pool}
        '''
        result = self._values.get("worker_pool")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleClouddeployTargetExecutionConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleClouddeployTargetExecutionConfigsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleClouddeployTarget.GoogleClouddeployTargetExecutionConfigsList",
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
            type_hints = typing.get_type_hints(GoogleClouddeployTargetExecutionConfigsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleClouddeployTargetExecutionConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleClouddeployTargetExecutionConfigsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleClouddeployTargetExecutionConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetExecutionConfigsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetExecutionConfigsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetExecutionConfigsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleClouddeployTargetExecutionConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleClouddeployTargetExecutionConfigs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleClouddeployTargetExecutionConfigs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetExecutionConfigsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleClouddeployTargetExecutionConfigsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleClouddeployTarget.GoogleClouddeployTargetExecutionConfigsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleClouddeployTargetExecutionConfigsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetArtifactStorage")
    def reset_artifact_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArtifactStorage", []))

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @jsii.member(jsii_name="resetWorkerPool")
    def reset_worker_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkerPool", []))

    @builtins.property
    @jsii.member(jsii_name="artifactStorageInput")
    def artifact_storage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="usagesInput")
    def usages_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "usagesInput"))

    @builtins.property
    @jsii.member(jsii_name="workerPoolInput")
    def worker_pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workerPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactStorage")
    def artifact_storage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactStorage"))

    @artifact_storage.setter
    def artifact_storage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetExecutionConfigsOutputReference, "artifact_storage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactStorage", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccount"))

    @service_account.setter
    def service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetExecutionConfigsOutputReference, "service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="usages")
    def usages(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "usages"))

    @usages.setter
    def usages(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetExecutionConfigsOutputReference, "usages").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usages", value)

    @builtins.property
    @jsii.member(jsii_name="workerPool")
    def worker_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workerPool"))

    @worker_pool.setter
    def worker_pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetExecutionConfigsOutputReference, "worker_pool").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerPool", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleClouddeployTargetExecutionConfigs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleClouddeployTargetExecutionConfigs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleClouddeployTargetExecutionConfigs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetExecutionConfigsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleClouddeployTarget.GoogleClouddeployTargetGke",
    jsii_struct_bases=[],
    name_mapping={"cluster": "cluster", "internal_ip": "internalIp"},
)
class GoogleClouddeployTargetGke:
    def __init__(
        self,
        *,
        cluster: typing.Optional[builtins.str] = None,
        internal_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cluster: Information specifying a GKE Cluster. Format is `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#cluster GoogleClouddeployTarget#cluster}
        :param internal_ip: Optional. If true, ``cluster`` is accessed using the private IP address of the control plane endpoint. Otherwise, the default IP address of the control plane endpoint is used. The default IP address is the private IP address for clusters with private control-plane endpoints and the public IP address otherwise. Only specify this option when ``cluster`` is a `private GKE cluster <https://cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#internal_ip GoogleClouddeployTarget#internal_ip}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleClouddeployTargetGke.__init__)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument internal_ip", value=internal_ip, expected_type=type_hints["internal_ip"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cluster is not None:
            self._values["cluster"] = cluster
        if internal_ip is not None:
            self._values["internal_ip"] = internal_ip

    @builtins.property
    def cluster(self) -> typing.Optional[builtins.str]:
        '''Information specifying a GKE Cluster. Format is `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#cluster GoogleClouddeployTarget#cluster}
        '''
        result = self._values.get("cluster")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def internal_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional.

        If true, ``cluster`` is accessed using the private IP address of the control plane endpoint. Otherwise, the default IP address of the control plane endpoint is used. The default IP address is the private IP address for clusters with private control-plane endpoints and the public IP address otherwise. Only specify this option when ``cluster`` is a `private GKE cluster <https://cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#internal_ip GoogleClouddeployTarget#internal_ip}
        '''
        result = self._values.get("internal_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleClouddeployTargetGke(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleClouddeployTargetGkeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleClouddeployTarget.GoogleClouddeployTargetGkeOutputReference",
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
            type_hints = typing.get_type_hints(GoogleClouddeployTargetGkeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCluster")
    def reset_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCluster", []))

    @jsii.member(jsii_name="resetInternalIp")
    def reset_internal_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternalIp", []))

    @builtins.property
    @jsii.member(jsii_name="clusterInput")
    def cluster_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterInput"))

    @builtins.property
    @jsii.member(jsii_name="internalIpInput")
    def internal_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "internalIpInput"))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cluster"))

    @cluster.setter
    def cluster(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetGkeOutputReference, "cluster").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cluster", value)

    @builtins.property
    @jsii.member(jsii_name="internalIp")
    def internal_ip(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "internalIp"))

    @internal_ip.setter
    def internal_ip(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetGkeOutputReference, "internal_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalIp", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleClouddeployTargetGke]:
        return typing.cast(typing.Optional[GoogleClouddeployTargetGke], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleClouddeployTargetGke],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetGkeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleClouddeployTarget.GoogleClouddeployTargetTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleClouddeployTargetTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#create GoogleClouddeployTarget#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#delete GoogleClouddeployTarget#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#update GoogleClouddeployTarget#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleClouddeployTargetTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#create GoogleClouddeployTarget#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#delete GoogleClouddeployTarget#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_clouddeploy_target#update GoogleClouddeployTarget#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleClouddeployTargetTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleClouddeployTargetTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleClouddeployTarget.GoogleClouddeployTargetTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleClouddeployTargetTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

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
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleClouddeployTargetTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleClouddeployTargetTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleClouddeployTargetTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleClouddeployTargetTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleClouddeployTarget",
    "GoogleClouddeployTargetAnthosCluster",
    "GoogleClouddeployTargetAnthosClusterOutputReference",
    "GoogleClouddeployTargetConfig",
    "GoogleClouddeployTargetExecutionConfigs",
    "GoogleClouddeployTargetExecutionConfigsList",
    "GoogleClouddeployTargetExecutionConfigsOutputReference",
    "GoogleClouddeployTargetGke",
    "GoogleClouddeployTargetGkeOutputReference",
    "GoogleClouddeployTargetTimeouts",
    "GoogleClouddeployTargetTimeoutsOutputReference",
]

publication.publish()
