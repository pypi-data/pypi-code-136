'''
# `google_container_aws_node_pool`

Refer to the Terraform Registory for docs: [`google_container_aws_node_pool`](https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool).
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


class GoogleContainerAwsNodePool(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePool",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool google_container_aws_node_pool}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        autoscaling: typing.Union["GoogleContainerAwsNodePoolAutoscaling", typing.Dict[str, typing.Any]],
        cluster: builtins.str,
        config: typing.Union["GoogleContainerAwsNodePoolConfigA", typing.Dict[str, typing.Any]],
        location: builtins.str,
        max_pods_constraint: typing.Union["GoogleContainerAwsNodePoolMaxPodsConstraint", typing.Dict[str, typing.Any]],
        name: builtins.str,
        subnet_id: builtins.str,
        version: builtins.str,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleContainerAwsNodePoolTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool google_container_aws_node_pool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param autoscaling: autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#autoscaling GoogleContainerAwsNodePool#autoscaling}
        :param cluster: The awsCluster for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#cluster GoogleContainerAwsNodePool#cluster}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#config GoogleContainerAwsNodePool#config}
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#location GoogleContainerAwsNodePool#location}
        :param max_pods_constraint: max_pods_constraint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#max_pods_constraint GoogleContainerAwsNodePool#max_pods_constraint}
        :param name: The name of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#name GoogleContainerAwsNodePool#name}
        :param subnet_id: The subnet where the node pool node run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#subnet_id GoogleContainerAwsNodePool#subnet_id}
        :param version: The Kubernetes version to run on this node pool (e.g. ``1.19.10-gke.1000``). You can list all supported versions on a given Google Cloud region by calling GetAwsServerConfig. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#version GoogleContainerAwsNodePool#version}
        :param annotations: Optional. Annotations on the node pool. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#annotations GoogleContainerAwsNodePool#annotations}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#id GoogleContainerAwsNodePool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#project GoogleContainerAwsNodePool#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#timeouts GoogleContainerAwsNodePool#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePool.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config_ = GoogleContainerAwsNodePoolConfig(
            autoscaling=autoscaling,
            cluster=cluster,
            config=config,
            location=location,
            max_pods_constraint=max_pods_constraint,
            name=name,
            subnet_id=subnet_id,
            version=version,
            annotations=annotations,
            id=id,
            project=project,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config_])

    @jsii.member(jsii_name="putAutoscaling")
    def put_autoscaling(
        self,
        *,
        max_node_count: jsii.Number,
        min_node_count: jsii.Number,
    ) -> None:
        '''
        :param max_node_count: Maximum number of nodes in the NodePool. Must be >= min_node_count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#max_node_count GoogleContainerAwsNodePool#max_node_count}
        :param min_node_count: Minimum number of nodes in the NodePool. Must be >= 1 and <= max_node_count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#min_node_count GoogleContainerAwsNodePool#min_node_count}
        '''
        value = GoogleContainerAwsNodePoolAutoscaling(
            max_node_count=max_node_count, min_node_count=min_node_count
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscaling", [value]))

    @jsii.member(jsii_name="putConfig")
    def put_config(
        self,
        *,
        config_encryption: typing.Union["GoogleContainerAwsNodePoolConfigConfigEncryption", typing.Dict[str, typing.Any]],
        iam_instance_profile: builtins.str,
        image_type: typing.Optional[builtins.str] = None,
        instance_placement: typing.Optional[typing.Union["GoogleContainerAwsNodePoolConfigInstancePlacement", typing.Dict[str, typing.Any]]] = None,
        instance_type: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        proxy_config: typing.Optional[typing.Union["GoogleContainerAwsNodePoolConfigProxyConfig", typing.Dict[str, typing.Any]]] = None,
        root_volume: typing.Optional[typing.Union["GoogleContainerAwsNodePoolConfigRootVolume", typing.Dict[str, typing.Any]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ssh_config: typing.Optional[typing.Union["GoogleContainerAwsNodePoolConfigSshConfig", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        taints: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleContainerAwsNodePoolConfigTaints", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param config_encryption: config_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#config_encryption GoogleContainerAwsNodePool#config_encryption}
        :param iam_instance_profile: The name of the AWS IAM role assigned to nodes in the pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#iam_instance_profile GoogleContainerAwsNodePool#iam_instance_profile}
        :param image_type: The OS image type to use on node pool instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#image_type GoogleContainerAwsNodePool#image_type}
        :param instance_placement: instance_placement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#instance_placement GoogleContainerAwsNodePool#instance_placement}
        :param instance_type: Optional. The AWS instance type. When unspecified, it defaults to ``m5.large``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#instance_type GoogleContainerAwsNodePool#instance_type}
        :param labels: Optional. The initial labels assigned to nodes of this node pool. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#labels GoogleContainerAwsNodePool#labels}
        :param proxy_config: proxy_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#proxy_config GoogleContainerAwsNodePool#proxy_config}
        :param root_volume: root_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#root_volume GoogleContainerAwsNodePool#root_volume}
        :param security_group_ids: Optional. The IDs of additional security groups to add to nodes in this pool. The manager will automatically create security groups with minimum rules needed for a functioning cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#security_group_ids GoogleContainerAwsNodePool#security_group_ids}
        :param ssh_config: ssh_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#ssh_config GoogleContainerAwsNodePool#ssh_config}
        :param tags: Optional. Key/value metadata to assign to each underlying AWS resource. Specify at most 50 pairs containing alphanumerics, spaces, and symbols (.+-=_:@/). Keys can be up to 127 Unicode characters. Values can be up to 255 Unicode characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#tags GoogleContainerAwsNodePool#tags}
        :param taints: taints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#taints GoogleContainerAwsNodePool#taints}
        '''
        value = GoogleContainerAwsNodePoolConfigA(
            config_encryption=config_encryption,
            iam_instance_profile=iam_instance_profile,
            image_type=image_type,
            instance_placement=instance_placement,
            instance_type=instance_type,
            labels=labels,
            proxy_config=proxy_config,
            root_volume=root_volume,
            security_group_ids=security_group_ids,
            ssh_config=ssh_config,
            tags=tags,
            taints=taints,
        )

        return typing.cast(None, jsii.invoke(self, "putConfig", [value]))

    @jsii.member(jsii_name="putMaxPodsConstraint")
    def put_max_pods_constraint(self, *, max_pods_per_node: jsii.Number) -> None:
        '''
        :param max_pods_per_node: The maximum number of pods to schedule on a single node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#max_pods_per_node GoogleContainerAwsNodePool#max_pods_per_node}
        '''
        value = GoogleContainerAwsNodePoolMaxPodsConstraint(
            max_pods_per_node=max_pods_per_node
        )

        return typing.cast(None, jsii.invoke(self, "putMaxPodsConstraint", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#create GoogleContainerAwsNodePool#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#delete GoogleContainerAwsNodePool#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#update GoogleContainerAwsNodePool#update}.
        '''
        value = GoogleContainerAwsNodePoolTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

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
    @jsii.member(jsii_name="autoscaling")
    def autoscaling(self) -> "GoogleContainerAwsNodePoolAutoscalingOutputReference":
        return typing.cast("GoogleContainerAwsNodePoolAutoscalingOutputReference", jsii.get(self, "autoscaling"))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(self) -> "GoogleContainerAwsNodePoolConfigAOutputReference":
        return typing.cast("GoogleContainerAwsNodePoolConfigAOutputReference", jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="maxPodsConstraint")
    def max_pods_constraint(
        self,
    ) -> "GoogleContainerAwsNodePoolMaxPodsConstraintOutputReference":
        return typing.cast("GoogleContainerAwsNodePoolMaxPodsConstraintOutputReference", jsii.get(self, "maxPodsConstraint"))

    @builtins.property
    @jsii.member(jsii_name="reconciling")
    def reconciling(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "reconciling"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleContainerAwsNodePoolTimeoutsOutputReference":
        return typing.cast("GoogleContainerAwsNodePoolTimeoutsOutputReference", jsii.get(self, "timeouts"))

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
    @jsii.member(jsii_name="autoscalingInput")
    def autoscaling_input(
        self,
    ) -> typing.Optional["GoogleContainerAwsNodePoolAutoscaling"]:
        return typing.cast(typing.Optional["GoogleContainerAwsNodePoolAutoscaling"], jsii.get(self, "autoscalingInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterInput")
    def cluster_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterInput"))

    @builtins.property
    @jsii.member(jsii_name="configInput")
    def config_input(self) -> typing.Optional["GoogleContainerAwsNodePoolConfigA"]:
        return typing.cast(typing.Optional["GoogleContainerAwsNodePoolConfigA"], jsii.get(self, "configInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPodsConstraintInput")
    def max_pods_constraint_input(
        self,
    ) -> typing.Optional["GoogleContainerAwsNodePoolMaxPodsConstraint"]:
        return typing.cast(typing.Optional["GoogleContainerAwsNodePoolMaxPodsConstraint"], jsii.get(self, "maxPodsConstraintInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleContainerAwsNodePoolTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleContainerAwsNodePoolTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePool, "annotations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cluster"))

    @cluster.setter
    def cluster(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePool, "cluster").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cluster", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePool, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePool, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePool, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePool, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePool, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePool, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolAutoscaling",
    jsii_struct_bases=[],
    name_mapping={"max_node_count": "maxNodeCount", "min_node_count": "minNodeCount"},
)
class GoogleContainerAwsNodePoolAutoscaling:
    def __init__(
        self,
        *,
        max_node_count: jsii.Number,
        min_node_count: jsii.Number,
    ) -> None:
        '''
        :param max_node_count: Maximum number of nodes in the NodePool. Must be >= min_node_count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#max_node_count GoogleContainerAwsNodePool#max_node_count}
        :param min_node_count: Minimum number of nodes in the NodePool. Must be >= 1 and <= max_node_count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#min_node_count GoogleContainerAwsNodePool#min_node_count}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolAutoscaling.__init__)
            check_type(argname="argument max_node_count", value=max_node_count, expected_type=type_hints["max_node_count"])
            check_type(argname="argument min_node_count", value=min_node_count, expected_type=type_hints["min_node_count"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_node_count": max_node_count,
            "min_node_count": min_node_count,
        }

    @builtins.property
    def max_node_count(self) -> jsii.Number:
        '''Maximum number of nodes in the NodePool. Must be >= min_node_count.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#max_node_count GoogleContainerAwsNodePool#max_node_count}
        '''
        result = self._values.get("max_node_count")
        assert result is not None, "Required property 'max_node_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_node_count(self) -> jsii.Number:
        '''Minimum number of nodes in the NodePool. Must be >= 1 and <= max_node_count.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#min_node_count GoogleContainerAwsNodePool#min_node_count}
        '''
        result = self._values.get("min_node_count")
        assert result is not None, "Required property 'min_node_count' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAwsNodePoolAutoscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAwsNodePoolAutoscalingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolAutoscalingOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolAutoscalingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxNodeCountInput")
    def max_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="minNodeCountInput")
    def min_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="maxNodeCount")
    def max_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxNodeCount"))

    @max_node_count.setter
    def max_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolAutoscalingOutputReference, "max_node_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="minNodeCount")
    def min_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNodeCount"))

    @min_node_count.setter
    def min_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolAutoscalingOutputReference, "min_node_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleContainerAwsNodePoolAutoscaling]:
        return typing.cast(typing.Optional[GoogleContainerAwsNodePoolAutoscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerAwsNodePoolAutoscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolAutoscalingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "autoscaling": "autoscaling",
        "cluster": "cluster",
        "config": "config",
        "location": "location",
        "max_pods_constraint": "maxPodsConstraint",
        "name": "name",
        "subnet_id": "subnetId",
        "version": "version",
        "annotations": "annotations",
        "id": "id",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleContainerAwsNodePoolConfig(cdktf.TerraformMetaArguments):
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
        autoscaling: typing.Union[GoogleContainerAwsNodePoolAutoscaling, typing.Dict[str, typing.Any]],
        cluster: builtins.str,
        config: typing.Union["GoogleContainerAwsNodePoolConfigA", typing.Dict[str, typing.Any]],
        location: builtins.str,
        max_pods_constraint: typing.Union["GoogleContainerAwsNodePoolMaxPodsConstraint", typing.Dict[str, typing.Any]],
        name: builtins.str,
        subnet_id: builtins.str,
        version: builtins.str,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleContainerAwsNodePoolTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param autoscaling: autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#autoscaling GoogleContainerAwsNodePool#autoscaling}
        :param cluster: The awsCluster for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#cluster GoogleContainerAwsNodePool#cluster}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#config GoogleContainerAwsNodePool#config}
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#location GoogleContainerAwsNodePool#location}
        :param max_pods_constraint: max_pods_constraint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#max_pods_constraint GoogleContainerAwsNodePool#max_pods_constraint}
        :param name: The name of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#name GoogleContainerAwsNodePool#name}
        :param subnet_id: The subnet where the node pool node run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#subnet_id GoogleContainerAwsNodePool#subnet_id}
        :param version: The Kubernetes version to run on this node pool (e.g. ``1.19.10-gke.1000``). You can list all supported versions on a given Google Cloud region by calling GetAwsServerConfig. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#version GoogleContainerAwsNodePool#version}
        :param annotations: Optional. Annotations on the node pool. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#annotations GoogleContainerAwsNodePool#annotations}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#id GoogleContainerAwsNodePool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#project GoogleContainerAwsNodePool#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#timeouts GoogleContainerAwsNodePool#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(autoscaling, dict):
            autoscaling = GoogleContainerAwsNodePoolAutoscaling(**autoscaling)
        if isinstance(config, dict):
            config = GoogleContainerAwsNodePoolConfigA(**config)
        if isinstance(max_pods_constraint, dict):
            max_pods_constraint = GoogleContainerAwsNodePoolMaxPodsConstraint(**max_pods_constraint)
        if isinstance(timeouts, dict):
            timeouts = GoogleContainerAwsNodePoolTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument autoscaling", value=autoscaling, expected_type=type_hints["autoscaling"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument max_pods_constraint", value=max_pods_constraint, expected_type=type_hints["max_pods_constraint"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "autoscaling": autoscaling,
            "cluster": cluster,
            "config": config,
            "location": location,
            "max_pods_constraint": max_pods_constraint,
            "name": name,
            "subnet_id": subnet_id,
            "version": version,
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
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project
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
    def autoscaling(self) -> GoogleContainerAwsNodePoolAutoscaling:
        '''autoscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#autoscaling GoogleContainerAwsNodePool#autoscaling}
        '''
        result = self._values.get("autoscaling")
        assert result is not None, "Required property 'autoscaling' is missing"
        return typing.cast(GoogleContainerAwsNodePoolAutoscaling, result)

    @builtins.property
    def cluster(self) -> builtins.str:
        '''The awsCluster for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#cluster GoogleContainerAwsNodePool#cluster}
        '''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config(self) -> "GoogleContainerAwsNodePoolConfigA":
        '''config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#config GoogleContainerAwsNodePool#config}
        '''
        result = self._values.get("config")
        assert result is not None, "Required property 'config' is missing"
        return typing.cast("GoogleContainerAwsNodePoolConfigA", result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The location for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#location GoogleContainerAwsNodePool#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_pods_constraint(self) -> "GoogleContainerAwsNodePoolMaxPodsConstraint":
        '''max_pods_constraint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#max_pods_constraint GoogleContainerAwsNodePool#max_pods_constraint}
        '''
        result = self._values.get("max_pods_constraint")
        assert result is not None, "Required property 'max_pods_constraint' is missing"
        return typing.cast("GoogleContainerAwsNodePoolMaxPodsConstraint", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#name GoogleContainerAwsNodePool#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''The subnet where the node pool node run.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#subnet_id GoogleContainerAwsNodePool#subnet_id}
        '''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''The Kubernetes version to run on this node pool (e.g. ``1.19.10-gke.1000``). You can list all supported versions on a given Google Cloud region by calling GetAwsServerConfig.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#version GoogleContainerAwsNodePool#version}
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        Annotations on the node pool. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#annotations GoogleContainerAwsNodePool#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#id GoogleContainerAwsNodePool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#project GoogleContainerAwsNodePool#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleContainerAwsNodePoolTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#timeouts GoogleContainerAwsNodePool#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleContainerAwsNodePoolTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAwsNodePoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfigA",
    jsii_struct_bases=[],
    name_mapping={
        "config_encryption": "configEncryption",
        "iam_instance_profile": "iamInstanceProfile",
        "image_type": "imageType",
        "instance_placement": "instancePlacement",
        "instance_type": "instanceType",
        "labels": "labels",
        "proxy_config": "proxyConfig",
        "root_volume": "rootVolume",
        "security_group_ids": "securityGroupIds",
        "ssh_config": "sshConfig",
        "tags": "tags",
        "taints": "taints",
    },
)
class GoogleContainerAwsNodePoolConfigA:
    def __init__(
        self,
        *,
        config_encryption: typing.Union["GoogleContainerAwsNodePoolConfigConfigEncryption", typing.Dict[str, typing.Any]],
        iam_instance_profile: builtins.str,
        image_type: typing.Optional[builtins.str] = None,
        instance_placement: typing.Optional[typing.Union["GoogleContainerAwsNodePoolConfigInstancePlacement", typing.Dict[str, typing.Any]]] = None,
        instance_type: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        proxy_config: typing.Optional[typing.Union["GoogleContainerAwsNodePoolConfigProxyConfig", typing.Dict[str, typing.Any]]] = None,
        root_volume: typing.Optional[typing.Union["GoogleContainerAwsNodePoolConfigRootVolume", typing.Dict[str, typing.Any]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ssh_config: typing.Optional[typing.Union["GoogleContainerAwsNodePoolConfigSshConfig", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        taints: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleContainerAwsNodePoolConfigTaints", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param config_encryption: config_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#config_encryption GoogleContainerAwsNodePool#config_encryption}
        :param iam_instance_profile: The name of the AWS IAM role assigned to nodes in the pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#iam_instance_profile GoogleContainerAwsNodePool#iam_instance_profile}
        :param image_type: The OS image type to use on node pool instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#image_type GoogleContainerAwsNodePool#image_type}
        :param instance_placement: instance_placement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#instance_placement GoogleContainerAwsNodePool#instance_placement}
        :param instance_type: Optional. The AWS instance type. When unspecified, it defaults to ``m5.large``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#instance_type GoogleContainerAwsNodePool#instance_type}
        :param labels: Optional. The initial labels assigned to nodes of this node pool. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#labels GoogleContainerAwsNodePool#labels}
        :param proxy_config: proxy_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#proxy_config GoogleContainerAwsNodePool#proxy_config}
        :param root_volume: root_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#root_volume GoogleContainerAwsNodePool#root_volume}
        :param security_group_ids: Optional. The IDs of additional security groups to add to nodes in this pool. The manager will automatically create security groups with minimum rules needed for a functioning cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#security_group_ids GoogleContainerAwsNodePool#security_group_ids}
        :param ssh_config: ssh_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#ssh_config GoogleContainerAwsNodePool#ssh_config}
        :param tags: Optional. Key/value metadata to assign to each underlying AWS resource. Specify at most 50 pairs containing alphanumerics, spaces, and symbols (.+-=_:@/). Keys can be up to 127 Unicode characters. Values can be up to 255 Unicode characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#tags GoogleContainerAwsNodePool#tags}
        :param taints: taints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#taints GoogleContainerAwsNodePool#taints}
        '''
        if isinstance(config_encryption, dict):
            config_encryption = GoogleContainerAwsNodePoolConfigConfigEncryption(**config_encryption)
        if isinstance(instance_placement, dict):
            instance_placement = GoogleContainerAwsNodePoolConfigInstancePlacement(**instance_placement)
        if isinstance(proxy_config, dict):
            proxy_config = GoogleContainerAwsNodePoolConfigProxyConfig(**proxy_config)
        if isinstance(root_volume, dict):
            root_volume = GoogleContainerAwsNodePoolConfigRootVolume(**root_volume)
        if isinstance(ssh_config, dict):
            ssh_config = GoogleContainerAwsNodePoolConfigSshConfig(**ssh_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigA.__init__)
            check_type(argname="argument config_encryption", value=config_encryption, expected_type=type_hints["config_encryption"])
            check_type(argname="argument iam_instance_profile", value=iam_instance_profile, expected_type=type_hints["iam_instance_profile"])
            check_type(argname="argument image_type", value=image_type, expected_type=type_hints["image_type"])
            check_type(argname="argument instance_placement", value=instance_placement, expected_type=type_hints["instance_placement"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument proxy_config", value=proxy_config, expected_type=type_hints["proxy_config"])
            check_type(argname="argument root_volume", value=root_volume, expected_type=type_hints["root_volume"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument ssh_config", value=ssh_config, expected_type=type_hints["ssh_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument taints", value=taints, expected_type=type_hints["taints"])
        self._values: typing.Dict[str, typing.Any] = {
            "config_encryption": config_encryption,
            "iam_instance_profile": iam_instance_profile,
        }
        if image_type is not None:
            self._values["image_type"] = image_type
        if instance_placement is not None:
            self._values["instance_placement"] = instance_placement
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if labels is not None:
            self._values["labels"] = labels
        if proxy_config is not None:
            self._values["proxy_config"] = proxy_config
        if root_volume is not None:
            self._values["root_volume"] = root_volume
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if ssh_config is not None:
            self._values["ssh_config"] = ssh_config
        if tags is not None:
            self._values["tags"] = tags
        if taints is not None:
            self._values["taints"] = taints

    @builtins.property
    def config_encryption(self) -> "GoogleContainerAwsNodePoolConfigConfigEncryption":
        '''config_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#config_encryption GoogleContainerAwsNodePool#config_encryption}
        '''
        result = self._values.get("config_encryption")
        assert result is not None, "Required property 'config_encryption' is missing"
        return typing.cast("GoogleContainerAwsNodePoolConfigConfigEncryption", result)

    @builtins.property
    def iam_instance_profile(self) -> builtins.str:
        '''The name of the AWS IAM role assigned to nodes in the pool.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#iam_instance_profile GoogleContainerAwsNodePool#iam_instance_profile}
        '''
        result = self._values.get("iam_instance_profile")
        assert result is not None, "Required property 'iam_instance_profile' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_type(self) -> typing.Optional[builtins.str]:
        '''The OS image type to use on node pool instances.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#image_type GoogleContainerAwsNodePool#image_type}
        '''
        result = self._values.get("image_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_placement(
        self,
    ) -> typing.Optional["GoogleContainerAwsNodePoolConfigInstancePlacement"]:
        '''instance_placement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#instance_placement GoogleContainerAwsNodePool#instance_placement}
        '''
        result = self._values.get("instance_placement")
        return typing.cast(typing.Optional["GoogleContainerAwsNodePoolConfigInstancePlacement"], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Optional. The AWS instance type. When unspecified, it defaults to ``m5.large``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#instance_type GoogleContainerAwsNodePool#instance_type}
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        The initial labels assigned to nodes of this node pool. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#labels GoogleContainerAwsNodePool#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def proxy_config(
        self,
    ) -> typing.Optional["GoogleContainerAwsNodePoolConfigProxyConfig"]:
        '''proxy_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#proxy_config GoogleContainerAwsNodePool#proxy_config}
        '''
        result = self._values.get("proxy_config")
        return typing.cast(typing.Optional["GoogleContainerAwsNodePoolConfigProxyConfig"], result)

    @builtins.property
    def root_volume(
        self,
    ) -> typing.Optional["GoogleContainerAwsNodePoolConfigRootVolume"]:
        '''root_volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#root_volume GoogleContainerAwsNodePool#root_volume}
        '''
        result = self._values.get("root_volume")
        return typing.cast(typing.Optional["GoogleContainerAwsNodePoolConfigRootVolume"], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        The IDs of additional security groups to add to nodes in this pool. The manager will automatically create security groups with minimum rules needed for a functioning cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#security_group_ids GoogleContainerAwsNodePool#security_group_ids}
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ssh_config(
        self,
    ) -> typing.Optional["GoogleContainerAwsNodePoolConfigSshConfig"]:
        '''ssh_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#ssh_config GoogleContainerAwsNodePool#ssh_config}
        '''
        result = self._values.get("ssh_config")
        return typing.cast(typing.Optional["GoogleContainerAwsNodePoolConfigSshConfig"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        Key/value metadata to assign to each underlying AWS resource. Specify at most 50 pairs containing alphanumerics, spaces, and symbols (.+-=_:@/). Keys can be up to 127 Unicode characters. Values can be up to 255 Unicode characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#tags GoogleContainerAwsNodePool#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def taints(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleContainerAwsNodePoolConfigTaints"]]]:
        '''taints block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#taints GoogleContainerAwsNodePool#taints}
        '''
        result = self._values.get("taints")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleContainerAwsNodePoolConfigTaints"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAwsNodePoolConfigA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAwsNodePoolConfigAOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfigAOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigAOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConfigEncryption")
    def put_config_encryption(self, *, kms_key_arn: builtins.str) -> None:
        '''
        :param kms_key_arn: The ARN of the AWS KMS key used to encrypt node pool configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#kms_key_arn GoogleContainerAwsNodePool#kms_key_arn}
        '''
        value = GoogleContainerAwsNodePoolConfigConfigEncryption(
            kms_key_arn=kms_key_arn
        )

        return typing.cast(None, jsii.invoke(self, "putConfigEncryption", [value]))

    @jsii.member(jsii_name="putInstancePlacement")
    def put_instance_placement(
        self,
        *,
        tenancy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param tenancy: The tenancy for the instance. Possible values: TENANCY_UNSPECIFIED, DEFAULT, DEDICATED, HOST. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#tenancy GoogleContainerAwsNodePool#tenancy}
        '''
        value = GoogleContainerAwsNodePoolConfigInstancePlacement(tenancy=tenancy)

        return typing.cast(None, jsii.invoke(self, "putInstancePlacement", [value]))

    @jsii.member(jsii_name="putProxyConfig")
    def put_proxy_config(
        self,
        *,
        secret_arn: builtins.str,
        secret_version: builtins.str,
    ) -> None:
        '''
        :param secret_arn: The ARN of the AWS Secret Manager secret that contains the HTTP(S) proxy configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#secret_arn GoogleContainerAwsNodePool#secret_arn}
        :param secret_version: The version string of the AWS Secret Manager secret that contains the HTTP(S) proxy configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#secret_version GoogleContainerAwsNodePool#secret_version}
        '''
        value = GoogleContainerAwsNodePoolConfigProxyConfig(
            secret_arn=secret_arn, secret_version=secret_version
        )

        return typing.cast(None, jsii.invoke(self, "putProxyConfig", [value]))

    @jsii.member(jsii_name="putRootVolume")
    def put_root_volume(
        self,
        *,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        size_gib: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param iops: Optional. The number of I/O operations per second (IOPS) to provision for GP3 volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#iops GoogleContainerAwsNodePool#iops}
        :param kms_key_arn: Optional. The Amazon Resource Name (ARN) of the Customer Managed Key (CMK) used to encrypt AWS EBS volumes. If not specified, the default Amazon managed key associated to the AWS region where this cluster runs will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#kms_key_arn GoogleContainerAwsNodePool#kms_key_arn}
        :param size_gib: Optional. The size of the volume, in GiBs. When unspecified, a default value is provided. See the specific reference in the parent resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#size_gib GoogleContainerAwsNodePool#size_gib}
        :param volume_type: Optional. Type of the EBS volume. When unspecified, it defaults to GP2 volume. Possible values: VOLUME_TYPE_UNSPECIFIED, GP2, GP3. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#volume_type GoogleContainerAwsNodePool#volume_type}
        '''
        value = GoogleContainerAwsNodePoolConfigRootVolume(
            iops=iops,
            kms_key_arn=kms_key_arn,
            size_gib=size_gib,
            volume_type=volume_type,
        )

        return typing.cast(None, jsii.invoke(self, "putRootVolume", [value]))

    @jsii.member(jsii_name="putSshConfig")
    def put_ssh_config(self, *, ec2_key_pair: builtins.str) -> None:
        '''
        :param ec2_key_pair: The name of the EC2 key pair used to login into cluster machines. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#ec2_key_pair GoogleContainerAwsNodePool#ec2_key_pair}
        '''
        value = GoogleContainerAwsNodePoolConfigSshConfig(ec2_key_pair=ec2_key_pair)

        return typing.cast(None, jsii.invoke(self, "putSshConfig", [value]))

    @jsii.member(jsii_name="putTaints")
    def put_taints(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleContainerAwsNodePoolConfigTaints", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigAOutputReference.put_taints)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTaints", [value]))

    @jsii.member(jsii_name="resetImageType")
    def reset_image_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageType", []))

    @jsii.member(jsii_name="resetInstancePlacement")
    def reset_instance_placement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePlacement", []))

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetProxyConfig")
    def reset_proxy_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyConfig", []))

    @jsii.member(jsii_name="resetRootVolume")
    def reset_root_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootVolume", []))

    @jsii.member(jsii_name="resetSecurityGroupIds")
    def reset_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupIds", []))

    @jsii.member(jsii_name="resetSshConfig")
    def reset_ssh_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshConfig", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTaints")
    def reset_taints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaints", []))

    @builtins.property
    @jsii.member(jsii_name="configEncryption")
    def config_encryption(
        self,
    ) -> "GoogleContainerAwsNodePoolConfigConfigEncryptionOutputReference":
        return typing.cast("GoogleContainerAwsNodePoolConfigConfigEncryptionOutputReference", jsii.get(self, "configEncryption"))

    @builtins.property
    @jsii.member(jsii_name="instancePlacement")
    def instance_placement(
        self,
    ) -> "GoogleContainerAwsNodePoolConfigInstancePlacementOutputReference":
        return typing.cast("GoogleContainerAwsNodePoolConfigInstancePlacementOutputReference", jsii.get(self, "instancePlacement"))

    @builtins.property
    @jsii.member(jsii_name="proxyConfig")
    def proxy_config(
        self,
    ) -> "GoogleContainerAwsNodePoolConfigProxyConfigOutputReference":
        return typing.cast("GoogleContainerAwsNodePoolConfigProxyConfigOutputReference", jsii.get(self, "proxyConfig"))

    @builtins.property
    @jsii.member(jsii_name="rootVolume")
    def root_volume(
        self,
    ) -> "GoogleContainerAwsNodePoolConfigRootVolumeOutputReference":
        return typing.cast("GoogleContainerAwsNodePoolConfigRootVolumeOutputReference", jsii.get(self, "rootVolume"))

    @builtins.property
    @jsii.member(jsii_name="sshConfig")
    def ssh_config(self) -> "GoogleContainerAwsNodePoolConfigSshConfigOutputReference":
        return typing.cast("GoogleContainerAwsNodePoolConfigSshConfigOutputReference", jsii.get(self, "sshConfig"))

    @builtins.property
    @jsii.member(jsii_name="taints")
    def taints(self) -> "GoogleContainerAwsNodePoolConfigTaintsList":
        return typing.cast("GoogleContainerAwsNodePoolConfigTaintsList", jsii.get(self, "taints"))

    @builtins.property
    @jsii.member(jsii_name="configEncryptionInput")
    def config_encryption_input(
        self,
    ) -> typing.Optional["GoogleContainerAwsNodePoolConfigConfigEncryption"]:
        return typing.cast(typing.Optional["GoogleContainerAwsNodePoolConfigConfigEncryption"], jsii.get(self, "configEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfileInput")
    def iam_instance_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamInstanceProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="imageTypeInput")
    def image_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePlacementInput")
    def instance_placement_input(
        self,
    ) -> typing.Optional["GoogleContainerAwsNodePoolConfigInstancePlacement"]:
        return typing.cast(typing.Optional["GoogleContainerAwsNodePoolConfigInstancePlacement"], jsii.get(self, "instancePlacementInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyConfigInput")
    def proxy_config_input(
        self,
    ) -> typing.Optional["GoogleContainerAwsNodePoolConfigProxyConfig"]:
        return typing.cast(typing.Optional["GoogleContainerAwsNodePoolConfigProxyConfig"], jsii.get(self, "proxyConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="rootVolumeInput")
    def root_volume_input(
        self,
    ) -> typing.Optional["GoogleContainerAwsNodePoolConfigRootVolume"]:
        return typing.cast(typing.Optional["GoogleContainerAwsNodePoolConfigRootVolume"], jsii.get(self, "rootVolumeInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="sshConfigInput")
    def ssh_config_input(
        self,
    ) -> typing.Optional["GoogleContainerAwsNodePoolConfigSshConfig"]:
        return typing.cast(typing.Optional["GoogleContainerAwsNodePoolConfigSshConfig"], jsii.get(self, "sshConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="taintsInput")
    def taints_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleContainerAwsNodePoolConfigTaints"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleContainerAwsNodePoolConfigTaints"]]], jsii.get(self, "taintsInput"))

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfile")
    def iam_instance_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamInstanceProfile"))

    @iam_instance_profile.setter
    def iam_instance_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigAOutputReference, "iam_instance_profile").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamInstanceProfile", value)

    @builtins.property
    @jsii.member(jsii_name="imageType")
    def image_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageType"))

    @image_type.setter
    def image_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigAOutputReference, "image_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageType", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigAOutputReference, "instance_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigAOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigAOutputReference, "security_group_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigAOutputReference, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleContainerAwsNodePoolConfigA]:
        return typing.cast(typing.Optional[GoogleContainerAwsNodePoolConfigA], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerAwsNodePoolConfigA],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigAOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfigConfigEncryption",
    jsii_struct_bases=[],
    name_mapping={"kms_key_arn": "kmsKeyArn"},
)
class GoogleContainerAwsNodePoolConfigConfigEncryption:
    def __init__(self, *, kms_key_arn: builtins.str) -> None:
        '''
        :param kms_key_arn: The ARN of the AWS KMS key used to encrypt node pool configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#kms_key_arn GoogleContainerAwsNodePool#kms_key_arn}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigConfigEncryption.__init__)
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "kms_key_arn": kms_key_arn,
        }

    @builtins.property
    def kms_key_arn(self) -> builtins.str:
        '''The ARN of the AWS KMS key used to encrypt node pool configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#kms_key_arn GoogleContainerAwsNodePool#kms_key_arn}
        '''
        result = self._values.get("kms_key_arn")
        assert result is not None, "Required property 'kms_key_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAwsNodePoolConfigConfigEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAwsNodePoolConfigConfigEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfigConfigEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigConfigEncryptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigConfigEncryptionOutputReference, "kms_key_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerAwsNodePoolConfigConfigEncryption]:
        return typing.cast(typing.Optional[GoogleContainerAwsNodePoolConfigConfigEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerAwsNodePoolConfigConfigEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigConfigEncryptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfigInstancePlacement",
    jsii_struct_bases=[],
    name_mapping={"tenancy": "tenancy"},
)
class GoogleContainerAwsNodePoolConfigInstancePlacement:
    def __init__(self, *, tenancy: typing.Optional[builtins.str] = None) -> None:
        '''
        :param tenancy: The tenancy for the instance. Possible values: TENANCY_UNSPECIFIED, DEFAULT, DEDICATED, HOST. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#tenancy GoogleContainerAwsNodePool#tenancy}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigInstancePlacement.__init__)
            check_type(argname="argument tenancy", value=tenancy, expected_type=type_hints["tenancy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if tenancy is not None:
            self._values["tenancy"] = tenancy

    @builtins.property
    def tenancy(self) -> typing.Optional[builtins.str]:
        '''The tenancy for the instance. Possible values: TENANCY_UNSPECIFIED, DEFAULT, DEDICATED, HOST.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#tenancy GoogleContainerAwsNodePool#tenancy}
        '''
        result = self._values.get("tenancy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAwsNodePoolConfigInstancePlacement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAwsNodePoolConfigInstancePlacementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfigInstancePlacementOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigInstancePlacementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTenancy")
    def reset_tenancy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenancy", []))

    @builtins.property
    @jsii.member(jsii_name="tenancyInput")
    def tenancy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenancyInput"))

    @builtins.property
    @jsii.member(jsii_name="tenancy")
    def tenancy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenancy"))

    @tenancy.setter
    def tenancy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigInstancePlacementOutputReference, "tenancy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenancy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerAwsNodePoolConfigInstancePlacement]:
        return typing.cast(typing.Optional[GoogleContainerAwsNodePoolConfigInstancePlacement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerAwsNodePoolConfigInstancePlacement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigInstancePlacementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfigProxyConfig",
    jsii_struct_bases=[],
    name_mapping={"secret_arn": "secretArn", "secret_version": "secretVersion"},
)
class GoogleContainerAwsNodePoolConfigProxyConfig:
    def __init__(
        self,
        *,
        secret_arn: builtins.str,
        secret_version: builtins.str,
    ) -> None:
        '''
        :param secret_arn: The ARN of the AWS Secret Manager secret that contains the HTTP(S) proxy configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#secret_arn GoogleContainerAwsNodePool#secret_arn}
        :param secret_version: The version string of the AWS Secret Manager secret that contains the HTTP(S) proxy configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#secret_version GoogleContainerAwsNodePool#secret_version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigProxyConfig.__init__)
            check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
            check_type(argname="argument secret_version", value=secret_version, expected_type=type_hints["secret_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "secret_arn": secret_arn,
            "secret_version": secret_version,
        }

    @builtins.property
    def secret_arn(self) -> builtins.str:
        '''The ARN of the AWS Secret Manager secret that contains the HTTP(S) proxy configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#secret_arn GoogleContainerAwsNodePool#secret_arn}
        '''
        result = self._values.get("secret_arn")
        assert result is not None, "Required property 'secret_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_version(self) -> builtins.str:
        '''The version string of the AWS Secret Manager secret that contains the HTTP(S) proxy configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#secret_version GoogleContainerAwsNodePool#secret_version}
        '''
        result = self._values.get("secret_version")
        assert result is not None, "Required property 'secret_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAwsNodePoolConfigProxyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAwsNodePoolConfigProxyConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfigProxyConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigProxyConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="secretArnInput")
    def secret_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretArnInput"))

    @builtins.property
    @jsii.member(jsii_name="secretVersionInput")
    def secret_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="secretArn")
    def secret_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretArn"))

    @secret_arn.setter
    def secret_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigProxyConfigOutputReference, "secret_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretArn", value)

    @builtins.property
    @jsii.member(jsii_name="secretVersion")
    def secret_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretVersion"))

    @secret_version.setter
    def secret_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigProxyConfigOutputReference, "secret_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerAwsNodePoolConfigProxyConfig]:
        return typing.cast(typing.Optional[GoogleContainerAwsNodePoolConfigProxyConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerAwsNodePoolConfigProxyConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigProxyConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfigRootVolume",
    jsii_struct_bases=[],
    name_mapping={
        "iops": "iops",
        "kms_key_arn": "kmsKeyArn",
        "size_gib": "sizeGib",
        "volume_type": "volumeType",
    },
)
class GoogleContainerAwsNodePoolConfigRootVolume:
    def __init__(
        self,
        *,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        size_gib: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param iops: Optional. The number of I/O operations per second (IOPS) to provision for GP3 volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#iops GoogleContainerAwsNodePool#iops}
        :param kms_key_arn: Optional. The Amazon Resource Name (ARN) of the Customer Managed Key (CMK) used to encrypt AWS EBS volumes. If not specified, the default Amazon managed key associated to the AWS region where this cluster runs will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#kms_key_arn GoogleContainerAwsNodePool#kms_key_arn}
        :param size_gib: Optional. The size of the volume, in GiBs. When unspecified, a default value is provided. See the specific reference in the parent resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#size_gib GoogleContainerAwsNodePool#size_gib}
        :param volume_type: Optional. Type of the EBS volume. When unspecified, it defaults to GP2 volume. Possible values: VOLUME_TYPE_UNSPECIFIED, GP2, GP3. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#volume_type GoogleContainerAwsNodePool#volume_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigRootVolume.__init__)
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument size_gib", value=size_gib, expected_type=type_hints["size_gib"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if iops is not None:
            self._values["iops"] = iops
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if size_gib is not None:
            self._values["size_gib"] = size_gib
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Optional. The number of I/O operations per second (IOPS) to provision for GP3 volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#iops GoogleContainerAwsNodePool#iops}
        '''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The Amazon Resource Name (ARN) of the Customer Managed Key (CMK) used to encrypt AWS EBS volumes. If not specified, the default Amazon managed key associated to the AWS region where this cluster runs will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#kms_key_arn GoogleContainerAwsNodePool#kms_key_arn}
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size_gib(self) -> typing.Optional[jsii.Number]:
        '''Optional.

        The size of the volume, in GiBs. When unspecified, a default value is provided. See the specific reference in the parent resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#size_gib GoogleContainerAwsNodePool#size_gib}
        '''
        result = self._values.get("size_gib")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Optional. Type of the EBS volume. When unspecified, it defaults to GP2 volume. Possible values: VOLUME_TYPE_UNSPECIFIED, GP2, GP3.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#volume_type GoogleContainerAwsNodePool#volume_type}
        '''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAwsNodePoolConfigRootVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAwsNodePoolConfigRootVolumeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfigRootVolumeOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigRootVolumeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetSizeGib")
    def reset_size_gib(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizeGib", []))

    @jsii.member(jsii_name="resetVolumeType")
    def reset_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeType", []))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeGibInput")
    def size_gib_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeGibInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeTypeInput")
    def volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigRootVolumeOutputReference, "iops").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigRootVolumeOutputReference, "kms_key_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="sizeGib")
    def size_gib(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeGib"))

    @size_gib.setter
    def size_gib(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigRootVolumeOutputReference, "size_gib").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeGib", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigRootVolumeOutputReference, "volume_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerAwsNodePoolConfigRootVolume]:
        return typing.cast(typing.Optional[GoogleContainerAwsNodePoolConfigRootVolume], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerAwsNodePoolConfigRootVolume],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigRootVolumeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfigSshConfig",
    jsii_struct_bases=[],
    name_mapping={"ec2_key_pair": "ec2KeyPair"},
)
class GoogleContainerAwsNodePoolConfigSshConfig:
    def __init__(self, *, ec2_key_pair: builtins.str) -> None:
        '''
        :param ec2_key_pair: The name of the EC2 key pair used to login into cluster machines. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#ec2_key_pair GoogleContainerAwsNodePool#ec2_key_pair}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigSshConfig.__init__)
            check_type(argname="argument ec2_key_pair", value=ec2_key_pair, expected_type=type_hints["ec2_key_pair"])
        self._values: typing.Dict[str, typing.Any] = {
            "ec2_key_pair": ec2_key_pair,
        }

    @builtins.property
    def ec2_key_pair(self) -> builtins.str:
        '''The name of the EC2 key pair used to login into cluster machines.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#ec2_key_pair GoogleContainerAwsNodePool#ec2_key_pair}
        '''
        result = self._values.get("ec2_key_pair")
        assert result is not None, "Required property 'ec2_key_pair' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAwsNodePoolConfigSshConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAwsNodePoolConfigSshConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfigSshConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigSshConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="ec2KeyPairInput")
    def ec2_key_pair_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2KeyPairInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2KeyPair")
    def ec2_key_pair(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ec2KeyPair"))

    @ec2_key_pair.setter
    def ec2_key_pair(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigSshConfigOutputReference, "ec2_key_pair").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2KeyPair", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerAwsNodePoolConfigSshConfig]:
        return typing.cast(typing.Optional[GoogleContainerAwsNodePoolConfigSshConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerAwsNodePoolConfigSshConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigSshConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfigTaints",
    jsii_struct_bases=[],
    name_mapping={"effect": "effect", "key": "key", "value": "value"},
)
class GoogleContainerAwsNodePoolConfigTaints:
    def __init__(
        self,
        *,
        effect: builtins.str,
        key: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param effect: The taint effect. Possible values: EFFECT_UNSPECIFIED, NO_SCHEDULE, PREFER_NO_SCHEDULE, NO_EXECUTE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#effect GoogleContainerAwsNodePool#effect}
        :param key: Key for the taint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#key GoogleContainerAwsNodePool#key}
        :param value: Value for the taint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#value GoogleContainerAwsNodePool#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigTaints.__init__)
            check_type(argname="argument effect", value=effect, expected_type=type_hints["effect"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "effect": effect,
            "key": key,
            "value": value,
        }

    @builtins.property
    def effect(self) -> builtins.str:
        '''The taint effect. Possible values: EFFECT_UNSPECIFIED, NO_SCHEDULE, PREFER_NO_SCHEDULE, NO_EXECUTE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#effect GoogleContainerAwsNodePool#effect}
        '''
        result = self._values.get("effect")
        assert result is not None, "Required property 'effect' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''Key for the taint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#key GoogleContainerAwsNodePool#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value for the taint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#value GoogleContainerAwsNodePool#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAwsNodePoolConfigTaints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAwsNodePoolConfigTaintsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfigTaintsList",
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
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigTaintsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleContainerAwsNodePoolConfigTaintsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigTaintsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleContainerAwsNodePoolConfigTaintsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigTaintsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigTaintsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigTaintsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleContainerAwsNodePoolConfigTaints]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleContainerAwsNodePoolConfigTaints]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleContainerAwsNodePoolConfigTaints]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigTaintsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleContainerAwsNodePoolConfigTaintsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolConfigTaintsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolConfigTaintsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="effectInput")
    def effect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "effectInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="effect")
    def effect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "effect"))

    @effect.setter
    def effect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigTaintsOutputReference, "effect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "effect", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigTaintsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigTaintsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleContainerAwsNodePoolConfigTaints, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleContainerAwsNodePoolConfigTaints, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleContainerAwsNodePoolConfigTaints, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolConfigTaintsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolMaxPodsConstraint",
    jsii_struct_bases=[],
    name_mapping={"max_pods_per_node": "maxPodsPerNode"},
)
class GoogleContainerAwsNodePoolMaxPodsConstraint:
    def __init__(self, *, max_pods_per_node: jsii.Number) -> None:
        '''
        :param max_pods_per_node: The maximum number of pods to schedule on a single node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#max_pods_per_node GoogleContainerAwsNodePool#max_pods_per_node}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolMaxPodsConstraint.__init__)
            check_type(argname="argument max_pods_per_node", value=max_pods_per_node, expected_type=type_hints["max_pods_per_node"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_pods_per_node": max_pods_per_node,
        }

    @builtins.property
    def max_pods_per_node(self) -> jsii.Number:
        '''The maximum number of pods to schedule on a single node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#max_pods_per_node GoogleContainerAwsNodePool#max_pods_per_node}
        '''
        result = self._values.get("max_pods_per_node")
        assert result is not None, "Required property 'max_pods_per_node' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAwsNodePoolMaxPodsConstraint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAwsNodePoolMaxPodsConstraintOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolMaxPodsConstraintOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolMaxPodsConstraintOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxPodsPerNodeInput")
    def max_pods_per_node_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPodsPerNodeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPodsPerNode")
    def max_pods_per_node(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPodsPerNode"))

    @max_pods_per_node.setter
    def max_pods_per_node(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolMaxPodsConstraintOutputReference, "max_pods_per_node").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPodsPerNode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerAwsNodePoolMaxPodsConstraint]:
        return typing.cast(typing.Optional[GoogleContainerAwsNodePoolMaxPodsConstraint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerAwsNodePoolMaxPodsConstraint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolMaxPodsConstraintOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleContainerAwsNodePoolTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#create GoogleContainerAwsNodePool#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#delete GoogleContainerAwsNodePool#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#update GoogleContainerAwsNodePool#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#create GoogleContainerAwsNodePool#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#delete GoogleContainerAwsNodePool#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_aws_node_pool#update GoogleContainerAwsNodePool#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAwsNodePoolTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAwsNodePoolTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAwsNodePool.GoogleContainerAwsNodePoolTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAwsNodePoolTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleContainerAwsNodePoolTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleContainerAwsNodePoolTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleContainerAwsNodePoolTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAwsNodePoolTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleContainerAwsNodePool",
    "GoogleContainerAwsNodePoolAutoscaling",
    "GoogleContainerAwsNodePoolAutoscalingOutputReference",
    "GoogleContainerAwsNodePoolConfig",
    "GoogleContainerAwsNodePoolConfigA",
    "GoogleContainerAwsNodePoolConfigAOutputReference",
    "GoogleContainerAwsNodePoolConfigConfigEncryption",
    "GoogleContainerAwsNodePoolConfigConfigEncryptionOutputReference",
    "GoogleContainerAwsNodePoolConfigInstancePlacement",
    "GoogleContainerAwsNodePoolConfigInstancePlacementOutputReference",
    "GoogleContainerAwsNodePoolConfigProxyConfig",
    "GoogleContainerAwsNodePoolConfigProxyConfigOutputReference",
    "GoogleContainerAwsNodePoolConfigRootVolume",
    "GoogleContainerAwsNodePoolConfigRootVolumeOutputReference",
    "GoogleContainerAwsNodePoolConfigSshConfig",
    "GoogleContainerAwsNodePoolConfigSshConfigOutputReference",
    "GoogleContainerAwsNodePoolConfigTaints",
    "GoogleContainerAwsNodePoolConfigTaintsList",
    "GoogleContainerAwsNodePoolConfigTaintsOutputReference",
    "GoogleContainerAwsNodePoolMaxPodsConstraint",
    "GoogleContainerAwsNodePoolMaxPodsConstraintOutputReference",
    "GoogleContainerAwsNodePoolTimeouts",
    "GoogleContainerAwsNodePoolTimeoutsOutputReference",
]

publication.publish()
