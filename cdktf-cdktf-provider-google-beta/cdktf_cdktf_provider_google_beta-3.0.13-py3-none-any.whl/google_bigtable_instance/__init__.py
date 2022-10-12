'''
# `google_bigtable_instance`

Refer to the Terraform Registory for docs: [`google_bigtable_instance`](https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance).
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


class GoogleBigtableInstance(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigtableInstance.GoogleBigtableInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance google_bigtable_instance}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        cluster: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleBigtableInstanceCluster", typing.Dict[str, typing.Any]]]]] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_type: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance google_bigtable_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name (also called Instance Id in the Cloud Console) of the Cloud Bigtable instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#name GoogleBigtableInstance#name}
        :param cluster: cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#cluster GoogleBigtableInstance#cluster}
        :param deletion_protection: Whether or not to allow Terraform to destroy the instance. Unless this field is set to false in Terraform state, a terraform destroy or terraform apply that would delete the instance will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#deletion_protection GoogleBigtableInstance#deletion_protection}
        :param display_name: The human-readable display name of the Bigtable instance. Defaults to the instance name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#display_name GoogleBigtableInstance#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#id GoogleBigtableInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_type: The instance type to create. One of "DEVELOPMENT" or "PRODUCTION". Defaults to "PRODUCTION". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#instance_type GoogleBigtableInstance#instance_type}
        :param labels: A mapping of labels to assign to the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#labels GoogleBigtableInstance#labels}
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#project GoogleBigtableInstance#project}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigtableInstance.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleBigtableInstanceConfig(
            name=name,
            cluster=cluster,
            deletion_protection=deletion_protection,
            display_name=display_name,
            id=id,
            instance_type=instance_type,
            labels=labels,
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

    @jsii.member(jsii_name="putCluster")
    def put_cluster(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleBigtableInstanceCluster", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigtableInstance.put_cluster)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCluster", [value]))

    @jsii.member(jsii_name="resetCluster")
    def reset_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCluster", []))

    @jsii.member(jsii_name="resetDeletionProtection")
    def reset_deletion_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeletionProtection", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

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
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> "GoogleBigtableInstanceClusterList":
        return typing.cast("GoogleBigtableInstanceClusterList", jsii.get(self, "cluster"))

    @builtins.property
    @jsii.member(jsii_name="clusterInput")
    def cluster_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleBigtableInstanceCluster"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleBigtableInstanceCluster"]]], jsii.get(self, "clusterInput"))

    @builtins.property
    @jsii.member(jsii_name="deletionProtectionInput")
    def deletion_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deletionProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

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
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deletionProtection"))

    @deletion_protection.setter
    def deletion_protection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstance, "deletion_protection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtection", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstance, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstance, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstance, "instance_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstance, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstance, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstance, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigtableInstance.GoogleBigtableInstanceCluster",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_id": "clusterId",
        "autoscaling_config": "autoscalingConfig",
        "kms_key_name": "kmsKeyName",
        "num_nodes": "numNodes",
        "storage_type": "storageType",
        "zone": "zone",
    },
)
class GoogleBigtableInstanceCluster:
    def __init__(
        self,
        *,
        cluster_id: builtins.str,
        autoscaling_config: typing.Optional[typing.Union["GoogleBigtableInstanceClusterAutoscalingConfig", typing.Dict[str, typing.Any]]] = None,
        kms_key_name: typing.Optional[builtins.str] = None,
        num_nodes: typing.Optional[jsii.Number] = None,
        storage_type: typing.Optional[builtins.str] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_id: The ID of the Cloud Bigtable cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#cluster_id GoogleBigtableInstance#cluster_id}
        :param autoscaling_config: autoscaling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#autoscaling_config GoogleBigtableInstance#autoscaling_config}
        :param kms_key_name: Describes the Cloud KMS encryption key that will be used to protect the destination Bigtable cluster. The requirements for this key are: 1) The Cloud Bigtable service account associated with the project that contains this cluster must be granted the cloudkms.cryptoKeyEncrypterDecrypter role on the CMEK key. 2) Only regional keys can be used and the region of the CMEK key must match the region of the cluster. 3) All clusters within an instance must use the same CMEK key. Values are of the form projects/{project}/locations/{location}/keyRings/{keyring}/cryptoKeys/{key} Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#kms_key_name GoogleBigtableInstance#kms_key_name}
        :param num_nodes: The number of nodes in your Cloud Bigtable cluster. Required, with a minimum of 1 for a PRODUCTION instance. Must be left unset for a DEVELOPMENT instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#num_nodes GoogleBigtableInstance#num_nodes}
        :param storage_type: The storage type to use. One of "SSD" or "HDD". Defaults to "SSD". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#storage_type GoogleBigtableInstance#storage_type}
        :param zone: The zone to create the Cloud Bigtable cluster in. Each cluster must have a different zone in the same region. Zones that support Bigtable instances are noted on the Cloud Bigtable locations page. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#zone GoogleBigtableInstance#zone}
        '''
        if isinstance(autoscaling_config, dict):
            autoscaling_config = GoogleBigtableInstanceClusterAutoscalingConfig(**autoscaling_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigtableInstanceCluster.__init__)
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument autoscaling_config", value=autoscaling_config, expected_type=type_hints["autoscaling_config"])
            check_type(argname="argument kms_key_name", value=kms_key_name, expected_type=type_hints["kms_key_name"])
            check_type(argname="argument num_nodes", value=num_nodes, expected_type=type_hints["num_nodes"])
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_id": cluster_id,
        }
        if autoscaling_config is not None:
            self._values["autoscaling_config"] = autoscaling_config
        if kms_key_name is not None:
            self._values["kms_key_name"] = kms_key_name
        if num_nodes is not None:
            self._values["num_nodes"] = num_nodes
        if storage_type is not None:
            self._values["storage_type"] = storage_type
        if zone is not None:
            self._values["zone"] = zone

    @builtins.property
    def cluster_id(self) -> builtins.str:
        '''The ID of the Cloud Bigtable cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#cluster_id GoogleBigtableInstance#cluster_id}
        '''
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def autoscaling_config(
        self,
    ) -> typing.Optional["GoogleBigtableInstanceClusterAutoscalingConfig"]:
        '''autoscaling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#autoscaling_config GoogleBigtableInstance#autoscaling_config}
        '''
        result = self._values.get("autoscaling_config")
        return typing.cast(typing.Optional["GoogleBigtableInstanceClusterAutoscalingConfig"], result)

    @builtins.property
    def kms_key_name(self) -> typing.Optional[builtins.str]:
        '''Describes the Cloud KMS encryption key that will be used to protect the destination Bigtable cluster.

        The requirements for this key are: 1) The Cloud Bigtable service account associated with the project that contains this cluster must be granted the cloudkms.cryptoKeyEncrypterDecrypter role on the CMEK key. 2) Only regional keys can be used and the region of the CMEK key must match the region of the cluster. 3) All clusters within an instance must use the same CMEK key. Values are of the form projects/{project}/locations/{location}/keyRings/{keyring}/cryptoKeys/{key}

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#kms_key_name GoogleBigtableInstance#kms_key_name}
        '''
        result = self._values.get("kms_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_nodes(self) -> typing.Optional[jsii.Number]:
        '''The number of nodes in your Cloud Bigtable cluster.

        Required, with a minimum of 1 for a PRODUCTION instance. Must be left unset for a DEVELOPMENT instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#num_nodes GoogleBigtableInstance#num_nodes}
        '''
        result = self._values.get("num_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_type(self) -> typing.Optional[builtins.str]:
        '''The storage type to use. One of "SSD" or "HDD". Defaults to "SSD".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#storage_type GoogleBigtableInstance#storage_type}
        '''
        result = self._values.get("storage_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''The zone to create the Cloud Bigtable cluster in.

        Each cluster must have a different zone in the same region. Zones that support Bigtable instances are noted on the Cloud Bigtable locations page.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#zone GoogleBigtableInstance#zone}
        '''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigtableInstanceCluster(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigtableInstance.GoogleBigtableInstanceClusterAutoscalingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "cpu_target": "cpuTarget",
        "max_nodes": "maxNodes",
        "min_nodes": "minNodes",
        "storage_target": "storageTarget",
    },
)
class GoogleBigtableInstanceClusterAutoscalingConfig:
    def __init__(
        self,
        *,
        cpu_target: jsii.Number,
        max_nodes: jsii.Number,
        min_nodes: jsii.Number,
        storage_target: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_target: The target CPU utilization for autoscaling. Value must be between 10 and 80. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#cpu_target GoogleBigtableInstance#cpu_target}
        :param max_nodes: The maximum number of nodes for autoscaling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#max_nodes GoogleBigtableInstance#max_nodes}
        :param min_nodes: The minimum number of nodes for autoscaling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#min_nodes GoogleBigtableInstance#min_nodes}
        :param storage_target: The target storage utilization for autoscaling, in GB, for each node in a cluster. This number is limited between 2560 (2.5TiB) and 5120 (5TiB) for a SSD cluster and between 8192 (8TiB) and 16384 (16 TiB) for an HDD cluster. If not set, whatever is already set for the cluster will not change, or if the cluster is just being created, it will use the default value of 2560 for SSD clusters and 8192 for HDD clusters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#storage_target GoogleBigtableInstance#storage_target}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigtableInstanceClusterAutoscalingConfig.__init__)
            check_type(argname="argument cpu_target", value=cpu_target, expected_type=type_hints["cpu_target"])
            check_type(argname="argument max_nodes", value=max_nodes, expected_type=type_hints["max_nodes"])
            check_type(argname="argument min_nodes", value=min_nodes, expected_type=type_hints["min_nodes"])
            check_type(argname="argument storage_target", value=storage_target, expected_type=type_hints["storage_target"])
        self._values: typing.Dict[str, typing.Any] = {
            "cpu_target": cpu_target,
            "max_nodes": max_nodes,
            "min_nodes": min_nodes,
        }
        if storage_target is not None:
            self._values["storage_target"] = storage_target

    @builtins.property
    def cpu_target(self) -> jsii.Number:
        '''The target CPU utilization for autoscaling. Value must be between 10 and 80.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#cpu_target GoogleBigtableInstance#cpu_target}
        '''
        result = self._values.get("cpu_target")
        assert result is not None, "Required property 'cpu_target' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_nodes(self) -> jsii.Number:
        '''The maximum number of nodes for autoscaling.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#max_nodes GoogleBigtableInstance#max_nodes}
        '''
        result = self._values.get("max_nodes")
        assert result is not None, "Required property 'max_nodes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_nodes(self) -> jsii.Number:
        '''The minimum number of nodes for autoscaling.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#min_nodes GoogleBigtableInstance#min_nodes}
        '''
        result = self._values.get("min_nodes")
        assert result is not None, "Required property 'min_nodes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def storage_target(self) -> typing.Optional[jsii.Number]:
        '''The target storage utilization for autoscaling, in GB, for each node in a cluster.

        This number is limited between 2560 (2.5TiB) and 5120 (5TiB) for a SSD cluster and between 8192 (8TiB) and 16384 (16 TiB) for an HDD cluster. If not set, whatever is already set for the cluster will not change, or if the cluster is just being created, it will use the default value of 2560 for SSD clusters and 8192 for HDD clusters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#storage_target GoogleBigtableInstance#storage_target}
        '''
        result = self._values.get("storage_target")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigtableInstanceClusterAutoscalingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigtableInstanceClusterAutoscalingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigtableInstance.GoogleBigtableInstanceClusterAutoscalingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigtableInstanceClusterAutoscalingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetStorageTarget")
    def reset_storage_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageTarget", []))

    @builtins.property
    @jsii.member(jsii_name="cpuTargetInput")
    def cpu_target_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="maxNodesInput")
    def max_nodes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxNodesInput"))

    @builtins.property
    @jsii.member(jsii_name="minNodesInput")
    def min_nodes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minNodesInput"))

    @builtins.property
    @jsii.member(jsii_name="storageTargetInput")
    def storage_target_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuTarget")
    def cpu_target(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuTarget"))

    @cpu_target.setter
    def cpu_target(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstanceClusterAutoscalingConfigOutputReference, "cpu_target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuTarget", value)

    @builtins.property
    @jsii.member(jsii_name="maxNodes")
    def max_nodes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxNodes"))

    @max_nodes.setter
    def max_nodes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstanceClusterAutoscalingConfigOutputReference, "max_nodes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxNodes", value)

    @builtins.property
    @jsii.member(jsii_name="minNodes")
    def min_nodes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNodes"))

    @min_nodes.setter
    def min_nodes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstanceClusterAutoscalingConfigOutputReference, "min_nodes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minNodes", value)

    @builtins.property
    @jsii.member(jsii_name="storageTarget")
    def storage_target(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageTarget"))

    @storage_target.setter
    def storage_target(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstanceClusterAutoscalingConfigOutputReference, "storage_target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageTarget", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigtableInstanceClusterAutoscalingConfig]:
        return typing.cast(typing.Optional[GoogleBigtableInstanceClusterAutoscalingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigtableInstanceClusterAutoscalingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstanceClusterAutoscalingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigtableInstanceClusterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigtableInstance.GoogleBigtableInstanceClusterList",
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
            type_hints = typing.get_type_hints(GoogleBigtableInstanceClusterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GoogleBigtableInstanceClusterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigtableInstanceClusterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleBigtableInstanceClusterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstanceClusterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstanceClusterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstanceClusterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleBigtableInstanceCluster]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleBigtableInstanceCluster]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleBigtableInstanceCluster]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstanceClusterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigtableInstanceClusterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigtableInstance.GoogleBigtableInstanceClusterOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigtableInstanceClusterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAutoscalingConfig")
    def put_autoscaling_config(
        self,
        *,
        cpu_target: jsii.Number,
        max_nodes: jsii.Number,
        min_nodes: jsii.Number,
        storage_target: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_target: The target CPU utilization for autoscaling. Value must be between 10 and 80. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#cpu_target GoogleBigtableInstance#cpu_target}
        :param max_nodes: The maximum number of nodes for autoscaling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#max_nodes GoogleBigtableInstance#max_nodes}
        :param min_nodes: The minimum number of nodes for autoscaling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#min_nodes GoogleBigtableInstance#min_nodes}
        :param storage_target: The target storage utilization for autoscaling, in GB, for each node in a cluster. This number is limited between 2560 (2.5TiB) and 5120 (5TiB) for a SSD cluster and between 8192 (8TiB) and 16384 (16 TiB) for an HDD cluster. If not set, whatever is already set for the cluster will not change, or if the cluster is just being created, it will use the default value of 2560 for SSD clusters and 8192 for HDD clusters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#storage_target GoogleBigtableInstance#storage_target}
        '''
        value = GoogleBigtableInstanceClusterAutoscalingConfig(
            cpu_target=cpu_target,
            max_nodes=max_nodes,
            min_nodes=min_nodes,
            storage_target=storage_target,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscalingConfig", [value]))

    @jsii.member(jsii_name="resetAutoscalingConfig")
    def reset_autoscaling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscalingConfig", []))

    @jsii.member(jsii_name="resetKmsKeyName")
    def reset_kms_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyName", []))

    @jsii.member(jsii_name="resetNumNodes")
    def reset_num_nodes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumNodes", []))

    @jsii.member(jsii_name="resetStorageType")
    def reset_storage_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageType", []))

    @jsii.member(jsii_name="resetZone")
    def reset_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZone", []))

    @builtins.property
    @jsii.member(jsii_name="autoscalingConfig")
    def autoscaling_config(
        self,
    ) -> GoogleBigtableInstanceClusterAutoscalingConfigOutputReference:
        return typing.cast(GoogleBigtableInstanceClusterAutoscalingConfigOutputReference, jsii.get(self, "autoscalingConfig"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingConfigInput")
    def autoscaling_config_input(
        self,
    ) -> typing.Optional[GoogleBigtableInstanceClusterAutoscalingConfig]:
        return typing.cast(typing.Optional[GoogleBigtableInstanceClusterAutoscalingConfig], jsii.get(self, "autoscalingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyNameInput")
    def kms_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="numNodesInput")
    def num_nodes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numNodesInput"))

    @builtins.property
    @jsii.member(jsii_name="storageTypeInput")
    def storage_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstanceClusterOutputReference, "cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyName")
    def kms_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyName"))

    @kms_key_name.setter
    def kms_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstanceClusterOutputReference, "kms_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="numNodes")
    def num_nodes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numNodes"))

    @num_nodes.setter
    def num_nodes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstanceClusterOutputReference, "num_nodes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numNodes", value)

    @builtins.property
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstanceClusterOutputReference, "storage_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstanceClusterOutputReference, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleBigtableInstanceCluster, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleBigtableInstanceCluster, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleBigtableInstanceCluster, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigtableInstanceClusterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigtableInstance.GoogleBigtableInstanceConfig",
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
        "cluster": "cluster",
        "deletion_protection": "deletionProtection",
        "display_name": "displayName",
        "id": "id",
        "instance_type": "instanceType",
        "labels": "labels",
        "project": "project",
    },
)
class GoogleBigtableInstanceConfig(cdktf.TerraformMetaArguments):
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
        cluster: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleBigtableInstanceCluster, typing.Dict[str, typing.Any]]]]] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_type: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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
        :param name: The name (also called Instance Id in the Cloud Console) of the Cloud Bigtable instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#name GoogleBigtableInstance#name}
        :param cluster: cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#cluster GoogleBigtableInstance#cluster}
        :param deletion_protection: Whether or not to allow Terraform to destroy the instance. Unless this field is set to false in Terraform state, a terraform destroy or terraform apply that would delete the instance will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#deletion_protection GoogleBigtableInstance#deletion_protection}
        :param display_name: The human-readable display name of the Bigtable instance. Defaults to the instance name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#display_name GoogleBigtableInstance#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#id GoogleBigtableInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_type: The instance type to create. One of "DEVELOPMENT" or "PRODUCTION". Defaults to "PRODUCTION". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#instance_type GoogleBigtableInstance#instance_type}
        :param labels: A mapping of labels to assign to the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#labels GoogleBigtableInstance#labels}
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#project GoogleBigtableInstance#project}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigtableInstanceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
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
        if cluster is not None:
            self._values["cluster"] = cluster
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if display_name is not None:
            self._values["display_name"] = display_name
        if id is not None:
            self._values["id"] = id
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if labels is not None:
            self._values["labels"] = labels
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
        '''The name (also called Instance Id in the Cloud Console) of the Cloud Bigtable instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#name GoogleBigtableInstance#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleBigtableInstanceCluster]]]:
        '''cluster block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#cluster GoogleBigtableInstance#cluster}
        '''
        result = self._values.get("cluster")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleBigtableInstanceCluster]]], result)

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not to allow Terraform to destroy the instance.

        Unless this field is set to false in Terraform state, a terraform destroy or terraform apply that would delete the instance will fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#deletion_protection GoogleBigtableInstance#deletion_protection}
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The human-readable display name of the Bigtable instance. Defaults to the instance name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#display_name GoogleBigtableInstance#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#id GoogleBigtableInstance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''The instance type to create. One of "DEVELOPMENT" or "PRODUCTION". Defaults to "PRODUCTION".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#instance_type GoogleBigtableInstance#instance_type}
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A mapping of labels to assign to the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#labels GoogleBigtableInstance#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which the resource belongs.

        If it is not provided, the provider project is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigtable_instance#project GoogleBigtableInstance#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigtableInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GoogleBigtableInstance",
    "GoogleBigtableInstanceCluster",
    "GoogleBigtableInstanceClusterAutoscalingConfig",
    "GoogleBigtableInstanceClusterAutoscalingConfigOutputReference",
    "GoogleBigtableInstanceClusterList",
    "GoogleBigtableInstanceClusterOutputReference",
    "GoogleBigtableInstanceConfig",
]

publication.publish()
