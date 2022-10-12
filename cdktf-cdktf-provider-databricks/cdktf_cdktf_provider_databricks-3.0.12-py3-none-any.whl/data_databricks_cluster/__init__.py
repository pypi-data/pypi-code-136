'''
# `data_databricks_cluster`

Refer to the Terraform Registory for docs: [`data_databricks_cluster`](https://www.terraform.io/docs/providers/databricks/d/cluster).
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


class DataDatabricksCluster(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/d/cluster databricks_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cluster_id: builtins.str,
        cluster_info: typing.Optional[typing.Union["DataDatabricksClusterClusterInfo", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/d/cluster databricks_cluster} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_id DataDatabricksCluster#cluster_id}.
        :param cluster_info: cluster_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_info DataDatabricksCluster#cluster_info}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#id DataDatabricksCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataDatabricksClusterConfig(
            cluster_id=cluster_id,
            cluster_info=cluster_info,
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

    @jsii.member(jsii_name="putClusterInfo")
    def put_cluster_info(
        self,
        *,
        default_tags: typing.Mapping[builtins.str, builtins.str],
        spark_version: builtins.str,
        state: builtins.str,
        autoscale: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoAutoscale", typing.Dict[str, typing.Any]]] = None,
        autotermination_minutes: typing.Optional[jsii.Number] = None,
        aws_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoAwsAttributes", typing.Dict[str, typing.Any]]] = None,
        azure_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoAzureAttributes", typing.Dict[str, typing.Any]]] = None,
        cluster_cores: typing.Optional[jsii.Number] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        cluster_log_conf: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoClusterLogConf", typing.Dict[str, typing.Any]]] = None,
        cluster_log_status: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoClusterLogStatus", typing.Dict[str, typing.Any]]] = None,
        cluster_memory_mb: typing.Optional[jsii.Number] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        cluster_source: typing.Optional[builtins.str] = None,
        creator_user_name: typing.Optional[builtins.str] = None,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        data_security_mode: typing.Optional[builtins.str] = None,
        docker_image: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoDockerImage", typing.Dict[str, typing.Any]]] = None,
        driver: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoDriver", typing.Dict[str, typing.Any]]] = None,
        driver_instance_pool_id: typing.Optional[builtins.str] = None,
        driver_node_type_id: typing.Optional[builtins.str] = None,
        enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_local_disk_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        executors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataDatabricksClusterClusterInfoExecutors", typing.Dict[str, typing.Any]]]]] = None,
        gcp_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoGcpAttributes", typing.Dict[str, typing.Any]]] = None,
        init_scripts: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataDatabricksClusterClusterInfoInitScripts", typing.Dict[str, typing.Any]]]]] = None,
        instance_pool_id: typing.Optional[builtins.str] = None,
        jdbc_port: typing.Optional[jsii.Number] = None,
        last_activity_time: typing.Optional[jsii.Number] = None,
        last_state_loss_time: typing.Optional[jsii.Number] = None,
        node_type_id: typing.Optional[builtins.str] = None,
        num_workers: typing.Optional[jsii.Number] = None,
        policy_id: typing.Optional[builtins.str] = None,
        single_user_name: typing.Optional[builtins.str] = None,
        spark_conf: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        spark_context_id: typing.Optional[jsii.Number] = None,
        spark_env_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        start_time: typing.Optional[jsii.Number] = None,
        state_message: typing.Optional[builtins.str] = None,
        terminate_time: typing.Optional[jsii.Number] = None,
        termination_reason: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoTerminationReason", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#default_tags DataDatabricksCluster#default_tags}.
        :param spark_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_version DataDatabricksCluster#spark_version}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#state DataDatabricksCluster#state}.
        :param autoscale: autoscale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#autoscale DataDatabricksCluster#autoscale}
        :param autotermination_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#autotermination_minutes DataDatabricksCluster#autotermination_minutes}.
        :param aws_attributes: aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#aws_attributes DataDatabricksCluster#aws_attributes}
        :param azure_attributes: azure_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#azure_attributes DataDatabricksCluster#azure_attributes}
        :param cluster_cores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_cores DataDatabricksCluster#cluster_cores}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_id DataDatabricksCluster#cluster_id}.
        :param cluster_log_conf: cluster_log_conf block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_log_conf DataDatabricksCluster#cluster_log_conf}
        :param cluster_log_status: cluster_log_status block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_log_status DataDatabricksCluster#cluster_log_status}
        :param cluster_memory_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_memory_mb DataDatabricksCluster#cluster_memory_mb}.
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_name DataDatabricksCluster#cluster_name}.
        :param cluster_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_source DataDatabricksCluster#cluster_source}.
        :param creator_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#creator_user_name DataDatabricksCluster#creator_user_name}.
        :param custom_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#custom_tags DataDatabricksCluster#custom_tags}.
        :param data_security_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#data_security_mode DataDatabricksCluster#data_security_mode}.
        :param docker_image: docker_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#docker_image DataDatabricksCluster#docker_image}
        :param driver: driver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver DataDatabricksCluster#driver}
        :param driver_instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver_instance_pool_id DataDatabricksCluster#driver_instance_pool_id}.
        :param driver_node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver_node_type_id DataDatabricksCluster#driver_node_type_id}.
        :param enable_elastic_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_elastic_disk DataDatabricksCluster#enable_elastic_disk}.
        :param enable_local_disk_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_local_disk_encryption DataDatabricksCluster#enable_local_disk_encryption}.
        :param executors: executors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#executors DataDatabricksCluster#executors}
        :param gcp_attributes: gcp_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#gcp_attributes DataDatabricksCluster#gcp_attributes}
        :param init_scripts: init_scripts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#init_scripts DataDatabricksCluster#init_scripts}
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_pool_id DataDatabricksCluster#instance_pool_id}.
        :param jdbc_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#jdbc_port DataDatabricksCluster#jdbc_port}.
        :param last_activity_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_activity_time DataDatabricksCluster#last_activity_time}.
        :param last_state_loss_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_state_loss_time DataDatabricksCluster#last_state_loss_time}.
        :param node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_type_id DataDatabricksCluster#node_type_id}.
        :param num_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#num_workers DataDatabricksCluster#num_workers}.
        :param policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#policy_id DataDatabricksCluster#policy_id}.
        :param single_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#single_user_name DataDatabricksCluster#single_user_name}.
        :param spark_conf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_conf DataDatabricksCluster#spark_conf}.
        :param spark_context_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_context_id DataDatabricksCluster#spark_context_id}.
        :param spark_env_vars: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_env_vars DataDatabricksCluster#spark_env_vars}.
        :param ssh_public_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ssh_public_keys DataDatabricksCluster#ssh_public_keys}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_time DataDatabricksCluster#start_time}.
        :param state_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#state_message DataDatabricksCluster#state_message}.
        :param terminate_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#terminate_time DataDatabricksCluster#terminate_time}.
        :param termination_reason: termination_reason block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#termination_reason DataDatabricksCluster#termination_reason}
        '''
        value = DataDatabricksClusterClusterInfo(
            default_tags=default_tags,
            spark_version=spark_version,
            state=state,
            autoscale=autoscale,
            autotermination_minutes=autotermination_minutes,
            aws_attributes=aws_attributes,
            azure_attributes=azure_attributes,
            cluster_cores=cluster_cores,
            cluster_id=cluster_id,
            cluster_log_conf=cluster_log_conf,
            cluster_log_status=cluster_log_status,
            cluster_memory_mb=cluster_memory_mb,
            cluster_name=cluster_name,
            cluster_source=cluster_source,
            creator_user_name=creator_user_name,
            custom_tags=custom_tags,
            data_security_mode=data_security_mode,
            docker_image=docker_image,
            driver=driver,
            driver_instance_pool_id=driver_instance_pool_id,
            driver_node_type_id=driver_node_type_id,
            enable_elastic_disk=enable_elastic_disk,
            enable_local_disk_encryption=enable_local_disk_encryption,
            executors=executors,
            gcp_attributes=gcp_attributes,
            init_scripts=init_scripts,
            instance_pool_id=instance_pool_id,
            jdbc_port=jdbc_port,
            last_activity_time=last_activity_time,
            last_state_loss_time=last_state_loss_time,
            node_type_id=node_type_id,
            num_workers=num_workers,
            policy_id=policy_id,
            single_user_name=single_user_name,
            spark_conf=spark_conf,
            spark_context_id=spark_context_id,
            spark_env_vars=spark_env_vars,
            ssh_public_keys=ssh_public_keys,
            start_time=start_time,
            state_message=state_message,
            terminate_time=terminate_time,
            termination_reason=termination_reason,
        )

        return typing.cast(None, jsii.invoke(self, "putClusterInfo", [value]))

    @jsii.member(jsii_name="resetClusterInfo")
    def reset_cluster_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterInfo", []))

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
    @jsii.member(jsii_name="clusterInfo")
    def cluster_info(self) -> "DataDatabricksClusterClusterInfoOutputReference":
        return typing.cast("DataDatabricksClusterClusterInfoOutputReference", jsii.get(self, "clusterInfo"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterInfoInput")
    def cluster_info_input(self) -> typing.Optional["DataDatabricksClusterClusterInfo"]:
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfo"], jsii.get(self, "clusterInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksCluster, "cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfo",
    jsii_struct_bases=[],
    name_mapping={
        "default_tags": "defaultTags",
        "spark_version": "sparkVersion",
        "state": "state",
        "autoscale": "autoscale",
        "autotermination_minutes": "autoterminationMinutes",
        "aws_attributes": "awsAttributes",
        "azure_attributes": "azureAttributes",
        "cluster_cores": "clusterCores",
        "cluster_id": "clusterId",
        "cluster_log_conf": "clusterLogConf",
        "cluster_log_status": "clusterLogStatus",
        "cluster_memory_mb": "clusterMemoryMb",
        "cluster_name": "clusterName",
        "cluster_source": "clusterSource",
        "creator_user_name": "creatorUserName",
        "custom_tags": "customTags",
        "data_security_mode": "dataSecurityMode",
        "docker_image": "dockerImage",
        "driver": "driver",
        "driver_instance_pool_id": "driverInstancePoolId",
        "driver_node_type_id": "driverNodeTypeId",
        "enable_elastic_disk": "enableElasticDisk",
        "enable_local_disk_encryption": "enableLocalDiskEncryption",
        "executors": "executors",
        "gcp_attributes": "gcpAttributes",
        "init_scripts": "initScripts",
        "instance_pool_id": "instancePoolId",
        "jdbc_port": "jdbcPort",
        "last_activity_time": "lastActivityTime",
        "last_state_loss_time": "lastStateLossTime",
        "node_type_id": "nodeTypeId",
        "num_workers": "numWorkers",
        "policy_id": "policyId",
        "single_user_name": "singleUserName",
        "spark_conf": "sparkConf",
        "spark_context_id": "sparkContextId",
        "spark_env_vars": "sparkEnvVars",
        "ssh_public_keys": "sshPublicKeys",
        "start_time": "startTime",
        "state_message": "stateMessage",
        "terminate_time": "terminateTime",
        "termination_reason": "terminationReason",
    },
)
class DataDatabricksClusterClusterInfo:
    def __init__(
        self,
        *,
        default_tags: typing.Mapping[builtins.str, builtins.str],
        spark_version: builtins.str,
        state: builtins.str,
        autoscale: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoAutoscale", typing.Dict[str, typing.Any]]] = None,
        autotermination_minutes: typing.Optional[jsii.Number] = None,
        aws_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoAwsAttributes", typing.Dict[str, typing.Any]]] = None,
        azure_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoAzureAttributes", typing.Dict[str, typing.Any]]] = None,
        cluster_cores: typing.Optional[jsii.Number] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        cluster_log_conf: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoClusterLogConf", typing.Dict[str, typing.Any]]] = None,
        cluster_log_status: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoClusterLogStatus", typing.Dict[str, typing.Any]]] = None,
        cluster_memory_mb: typing.Optional[jsii.Number] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        cluster_source: typing.Optional[builtins.str] = None,
        creator_user_name: typing.Optional[builtins.str] = None,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        data_security_mode: typing.Optional[builtins.str] = None,
        docker_image: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoDockerImage", typing.Dict[str, typing.Any]]] = None,
        driver: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoDriver", typing.Dict[str, typing.Any]]] = None,
        driver_instance_pool_id: typing.Optional[builtins.str] = None,
        driver_node_type_id: typing.Optional[builtins.str] = None,
        enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_local_disk_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        executors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataDatabricksClusterClusterInfoExecutors", typing.Dict[str, typing.Any]]]]] = None,
        gcp_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoGcpAttributes", typing.Dict[str, typing.Any]]] = None,
        init_scripts: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataDatabricksClusterClusterInfoInitScripts", typing.Dict[str, typing.Any]]]]] = None,
        instance_pool_id: typing.Optional[builtins.str] = None,
        jdbc_port: typing.Optional[jsii.Number] = None,
        last_activity_time: typing.Optional[jsii.Number] = None,
        last_state_loss_time: typing.Optional[jsii.Number] = None,
        node_type_id: typing.Optional[builtins.str] = None,
        num_workers: typing.Optional[jsii.Number] = None,
        policy_id: typing.Optional[builtins.str] = None,
        single_user_name: typing.Optional[builtins.str] = None,
        spark_conf: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        spark_context_id: typing.Optional[jsii.Number] = None,
        spark_env_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        start_time: typing.Optional[jsii.Number] = None,
        state_message: typing.Optional[builtins.str] = None,
        terminate_time: typing.Optional[jsii.Number] = None,
        termination_reason: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoTerminationReason", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#default_tags DataDatabricksCluster#default_tags}.
        :param spark_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_version DataDatabricksCluster#spark_version}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#state DataDatabricksCluster#state}.
        :param autoscale: autoscale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#autoscale DataDatabricksCluster#autoscale}
        :param autotermination_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#autotermination_minutes DataDatabricksCluster#autotermination_minutes}.
        :param aws_attributes: aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#aws_attributes DataDatabricksCluster#aws_attributes}
        :param azure_attributes: azure_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#azure_attributes DataDatabricksCluster#azure_attributes}
        :param cluster_cores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_cores DataDatabricksCluster#cluster_cores}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_id DataDatabricksCluster#cluster_id}.
        :param cluster_log_conf: cluster_log_conf block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_log_conf DataDatabricksCluster#cluster_log_conf}
        :param cluster_log_status: cluster_log_status block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_log_status DataDatabricksCluster#cluster_log_status}
        :param cluster_memory_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_memory_mb DataDatabricksCluster#cluster_memory_mb}.
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_name DataDatabricksCluster#cluster_name}.
        :param cluster_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_source DataDatabricksCluster#cluster_source}.
        :param creator_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#creator_user_name DataDatabricksCluster#creator_user_name}.
        :param custom_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#custom_tags DataDatabricksCluster#custom_tags}.
        :param data_security_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#data_security_mode DataDatabricksCluster#data_security_mode}.
        :param docker_image: docker_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#docker_image DataDatabricksCluster#docker_image}
        :param driver: driver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver DataDatabricksCluster#driver}
        :param driver_instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver_instance_pool_id DataDatabricksCluster#driver_instance_pool_id}.
        :param driver_node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver_node_type_id DataDatabricksCluster#driver_node_type_id}.
        :param enable_elastic_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_elastic_disk DataDatabricksCluster#enable_elastic_disk}.
        :param enable_local_disk_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_local_disk_encryption DataDatabricksCluster#enable_local_disk_encryption}.
        :param executors: executors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#executors DataDatabricksCluster#executors}
        :param gcp_attributes: gcp_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#gcp_attributes DataDatabricksCluster#gcp_attributes}
        :param init_scripts: init_scripts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#init_scripts DataDatabricksCluster#init_scripts}
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_pool_id DataDatabricksCluster#instance_pool_id}.
        :param jdbc_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#jdbc_port DataDatabricksCluster#jdbc_port}.
        :param last_activity_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_activity_time DataDatabricksCluster#last_activity_time}.
        :param last_state_loss_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_state_loss_time DataDatabricksCluster#last_state_loss_time}.
        :param node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_type_id DataDatabricksCluster#node_type_id}.
        :param num_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#num_workers DataDatabricksCluster#num_workers}.
        :param policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#policy_id DataDatabricksCluster#policy_id}.
        :param single_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#single_user_name DataDatabricksCluster#single_user_name}.
        :param spark_conf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_conf DataDatabricksCluster#spark_conf}.
        :param spark_context_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_context_id DataDatabricksCluster#spark_context_id}.
        :param spark_env_vars: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_env_vars DataDatabricksCluster#spark_env_vars}.
        :param ssh_public_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ssh_public_keys DataDatabricksCluster#ssh_public_keys}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_time DataDatabricksCluster#start_time}.
        :param state_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#state_message DataDatabricksCluster#state_message}.
        :param terminate_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#terminate_time DataDatabricksCluster#terminate_time}.
        :param termination_reason: termination_reason block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#termination_reason DataDatabricksCluster#termination_reason}
        '''
        if isinstance(autoscale, dict):
            autoscale = DataDatabricksClusterClusterInfoAutoscale(**autoscale)
        if isinstance(aws_attributes, dict):
            aws_attributes = DataDatabricksClusterClusterInfoAwsAttributes(**aws_attributes)
        if isinstance(azure_attributes, dict):
            azure_attributes = DataDatabricksClusterClusterInfoAzureAttributes(**azure_attributes)
        if isinstance(cluster_log_conf, dict):
            cluster_log_conf = DataDatabricksClusterClusterInfoClusterLogConf(**cluster_log_conf)
        if isinstance(cluster_log_status, dict):
            cluster_log_status = DataDatabricksClusterClusterInfoClusterLogStatus(**cluster_log_status)
        if isinstance(docker_image, dict):
            docker_image = DataDatabricksClusterClusterInfoDockerImage(**docker_image)
        if isinstance(driver, dict):
            driver = DataDatabricksClusterClusterInfoDriver(**driver)
        if isinstance(gcp_attributes, dict):
            gcp_attributes = DataDatabricksClusterClusterInfoGcpAttributes(**gcp_attributes)
        if isinstance(termination_reason, dict):
            termination_reason = DataDatabricksClusterClusterInfoTerminationReason(**termination_reason)
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfo.__init__)
            check_type(argname="argument default_tags", value=default_tags, expected_type=type_hints["default_tags"])
            check_type(argname="argument spark_version", value=spark_version, expected_type=type_hints["spark_version"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument autoscale", value=autoscale, expected_type=type_hints["autoscale"])
            check_type(argname="argument autotermination_minutes", value=autotermination_minutes, expected_type=type_hints["autotermination_minutes"])
            check_type(argname="argument aws_attributes", value=aws_attributes, expected_type=type_hints["aws_attributes"])
            check_type(argname="argument azure_attributes", value=azure_attributes, expected_type=type_hints["azure_attributes"])
            check_type(argname="argument cluster_cores", value=cluster_cores, expected_type=type_hints["cluster_cores"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument cluster_log_conf", value=cluster_log_conf, expected_type=type_hints["cluster_log_conf"])
            check_type(argname="argument cluster_log_status", value=cluster_log_status, expected_type=type_hints["cluster_log_status"])
            check_type(argname="argument cluster_memory_mb", value=cluster_memory_mb, expected_type=type_hints["cluster_memory_mb"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument cluster_source", value=cluster_source, expected_type=type_hints["cluster_source"])
            check_type(argname="argument creator_user_name", value=creator_user_name, expected_type=type_hints["creator_user_name"])
            check_type(argname="argument custom_tags", value=custom_tags, expected_type=type_hints["custom_tags"])
            check_type(argname="argument data_security_mode", value=data_security_mode, expected_type=type_hints["data_security_mode"])
            check_type(argname="argument docker_image", value=docker_image, expected_type=type_hints["docker_image"])
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
            check_type(argname="argument driver_instance_pool_id", value=driver_instance_pool_id, expected_type=type_hints["driver_instance_pool_id"])
            check_type(argname="argument driver_node_type_id", value=driver_node_type_id, expected_type=type_hints["driver_node_type_id"])
            check_type(argname="argument enable_elastic_disk", value=enable_elastic_disk, expected_type=type_hints["enable_elastic_disk"])
            check_type(argname="argument enable_local_disk_encryption", value=enable_local_disk_encryption, expected_type=type_hints["enable_local_disk_encryption"])
            check_type(argname="argument executors", value=executors, expected_type=type_hints["executors"])
            check_type(argname="argument gcp_attributes", value=gcp_attributes, expected_type=type_hints["gcp_attributes"])
            check_type(argname="argument init_scripts", value=init_scripts, expected_type=type_hints["init_scripts"])
            check_type(argname="argument instance_pool_id", value=instance_pool_id, expected_type=type_hints["instance_pool_id"])
            check_type(argname="argument jdbc_port", value=jdbc_port, expected_type=type_hints["jdbc_port"])
            check_type(argname="argument last_activity_time", value=last_activity_time, expected_type=type_hints["last_activity_time"])
            check_type(argname="argument last_state_loss_time", value=last_state_loss_time, expected_type=type_hints["last_state_loss_time"])
            check_type(argname="argument node_type_id", value=node_type_id, expected_type=type_hints["node_type_id"])
            check_type(argname="argument num_workers", value=num_workers, expected_type=type_hints["num_workers"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument single_user_name", value=single_user_name, expected_type=type_hints["single_user_name"])
            check_type(argname="argument spark_conf", value=spark_conf, expected_type=type_hints["spark_conf"])
            check_type(argname="argument spark_context_id", value=spark_context_id, expected_type=type_hints["spark_context_id"])
            check_type(argname="argument spark_env_vars", value=spark_env_vars, expected_type=type_hints["spark_env_vars"])
            check_type(argname="argument ssh_public_keys", value=ssh_public_keys, expected_type=type_hints["ssh_public_keys"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument state_message", value=state_message, expected_type=type_hints["state_message"])
            check_type(argname="argument terminate_time", value=terminate_time, expected_type=type_hints["terminate_time"])
            check_type(argname="argument termination_reason", value=termination_reason, expected_type=type_hints["termination_reason"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_tags": default_tags,
            "spark_version": spark_version,
            "state": state,
        }
        if autoscale is not None:
            self._values["autoscale"] = autoscale
        if autotermination_minutes is not None:
            self._values["autotermination_minutes"] = autotermination_minutes
        if aws_attributes is not None:
            self._values["aws_attributes"] = aws_attributes
        if azure_attributes is not None:
            self._values["azure_attributes"] = azure_attributes
        if cluster_cores is not None:
            self._values["cluster_cores"] = cluster_cores
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if cluster_log_conf is not None:
            self._values["cluster_log_conf"] = cluster_log_conf
        if cluster_log_status is not None:
            self._values["cluster_log_status"] = cluster_log_status
        if cluster_memory_mb is not None:
            self._values["cluster_memory_mb"] = cluster_memory_mb
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if cluster_source is not None:
            self._values["cluster_source"] = cluster_source
        if creator_user_name is not None:
            self._values["creator_user_name"] = creator_user_name
        if custom_tags is not None:
            self._values["custom_tags"] = custom_tags
        if data_security_mode is not None:
            self._values["data_security_mode"] = data_security_mode
        if docker_image is not None:
            self._values["docker_image"] = docker_image
        if driver is not None:
            self._values["driver"] = driver
        if driver_instance_pool_id is not None:
            self._values["driver_instance_pool_id"] = driver_instance_pool_id
        if driver_node_type_id is not None:
            self._values["driver_node_type_id"] = driver_node_type_id
        if enable_elastic_disk is not None:
            self._values["enable_elastic_disk"] = enable_elastic_disk
        if enable_local_disk_encryption is not None:
            self._values["enable_local_disk_encryption"] = enable_local_disk_encryption
        if executors is not None:
            self._values["executors"] = executors
        if gcp_attributes is not None:
            self._values["gcp_attributes"] = gcp_attributes
        if init_scripts is not None:
            self._values["init_scripts"] = init_scripts
        if instance_pool_id is not None:
            self._values["instance_pool_id"] = instance_pool_id
        if jdbc_port is not None:
            self._values["jdbc_port"] = jdbc_port
        if last_activity_time is not None:
            self._values["last_activity_time"] = last_activity_time
        if last_state_loss_time is not None:
            self._values["last_state_loss_time"] = last_state_loss_time
        if node_type_id is not None:
            self._values["node_type_id"] = node_type_id
        if num_workers is not None:
            self._values["num_workers"] = num_workers
        if policy_id is not None:
            self._values["policy_id"] = policy_id
        if single_user_name is not None:
            self._values["single_user_name"] = single_user_name
        if spark_conf is not None:
            self._values["spark_conf"] = spark_conf
        if spark_context_id is not None:
            self._values["spark_context_id"] = spark_context_id
        if spark_env_vars is not None:
            self._values["spark_env_vars"] = spark_env_vars
        if ssh_public_keys is not None:
            self._values["ssh_public_keys"] = ssh_public_keys
        if start_time is not None:
            self._values["start_time"] = start_time
        if state_message is not None:
            self._values["state_message"] = state_message
        if terminate_time is not None:
            self._values["terminate_time"] = terminate_time
        if termination_reason is not None:
            self._values["termination_reason"] = termination_reason

    @builtins.property
    def default_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#default_tags DataDatabricksCluster#default_tags}.'''
        result = self._values.get("default_tags")
        assert result is not None, "Required property 'default_tags' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def spark_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_version DataDatabricksCluster#spark_version}.'''
        result = self._values.get("spark_version")
        assert result is not None, "Required property 'spark_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def state(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#state DataDatabricksCluster#state}.'''
        result = self._values.get("state")
        assert result is not None, "Required property 'state' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def autoscale(self) -> typing.Optional["DataDatabricksClusterClusterInfoAutoscale"]:
        '''autoscale block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#autoscale DataDatabricksCluster#autoscale}
        '''
        result = self._values.get("autoscale")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoAutoscale"], result)

    @builtins.property
    def autotermination_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#autotermination_minutes DataDatabricksCluster#autotermination_minutes}.'''
        result = self._values.get("autotermination_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def aws_attributes(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoAwsAttributes"]:
        '''aws_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#aws_attributes DataDatabricksCluster#aws_attributes}
        '''
        result = self._values.get("aws_attributes")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoAwsAttributes"], result)

    @builtins.property
    def azure_attributes(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoAzureAttributes"]:
        '''azure_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#azure_attributes DataDatabricksCluster#azure_attributes}
        '''
        result = self._values.get("azure_attributes")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoAzureAttributes"], result)

    @builtins.property
    def cluster_cores(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_cores DataDatabricksCluster#cluster_cores}.'''
        result = self._values.get("cluster_cores")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_id DataDatabricksCluster#cluster_id}.'''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_log_conf(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoClusterLogConf"]:
        '''cluster_log_conf block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_log_conf DataDatabricksCluster#cluster_log_conf}
        '''
        result = self._values.get("cluster_log_conf")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoClusterLogConf"], result)

    @builtins.property
    def cluster_log_status(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoClusterLogStatus"]:
        '''cluster_log_status block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_log_status DataDatabricksCluster#cluster_log_status}
        '''
        result = self._values.get("cluster_log_status")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoClusterLogStatus"], result)

    @builtins.property
    def cluster_memory_mb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_memory_mb DataDatabricksCluster#cluster_memory_mb}.'''
        result = self._values.get("cluster_memory_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_name DataDatabricksCluster#cluster_name}.'''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_source DataDatabricksCluster#cluster_source}.'''
        result = self._values.get("cluster_source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creator_user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#creator_user_name DataDatabricksCluster#creator_user_name}.'''
        result = self._values.get("creator_user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#custom_tags DataDatabricksCluster#custom_tags}.'''
        result = self._values.get("custom_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def data_security_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#data_security_mode DataDatabricksCluster#data_security_mode}.'''
        result = self._values.get("data_security_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_image(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoDockerImage"]:
        '''docker_image block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#docker_image DataDatabricksCluster#docker_image}
        '''
        result = self._values.get("docker_image")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoDockerImage"], result)

    @builtins.property
    def driver(self) -> typing.Optional["DataDatabricksClusterClusterInfoDriver"]:
        '''driver block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver DataDatabricksCluster#driver}
        '''
        result = self._values.get("driver")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoDriver"], result)

    @builtins.property
    def driver_instance_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver_instance_pool_id DataDatabricksCluster#driver_instance_pool_id}.'''
        result = self._values.get("driver_instance_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def driver_node_type_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver_node_type_id DataDatabricksCluster#driver_node_type_id}.'''
        result = self._values.get("driver_node_type_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_elastic_disk(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_elastic_disk DataDatabricksCluster#enable_elastic_disk}.'''
        result = self._values.get("enable_elastic_disk")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_local_disk_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_local_disk_encryption DataDatabricksCluster#enable_local_disk_encryption}.'''
        result = self._values.get("enable_local_disk_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def executors(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataDatabricksClusterClusterInfoExecutors"]]]:
        '''executors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#executors DataDatabricksCluster#executors}
        '''
        result = self._values.get("executors")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataDatabricksClusterClusterInfoExecutors"]]], result)

    @builtins.property
    def gcp_attributes(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoGcpAttributes"]:
        '''gcp_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#gcp_attributes DataDatabricksCluster#gcp_attributes}
        '''
        result = self._values.get("gcp_attributes")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoGcpAttributes"], result)

    @builtins.property
    def init_scripts(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataDatabricksClusterClusterInfoInitScripts"]]]:
        '''init_scripts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#init_scripts DataDatabricksCluster#init_scripts}
        '''
        result = self._values.get("init_scripts")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataDatabricksClusterClusterInfoInitScripts"]]], result)

    @builtins.property
    def instance_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_pool_id DataDatabricksCluster#instance_pool_id}.'''
        result = self._values.get("instance_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jdbc_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#jdbc_port DataDatabricksCluster#jdbc_port}.'''
        result = self._values.get("jdbc_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def last_activity_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_activity_time DataDatabricksCluster#last_activity_time}.'''
        result = self._values.get("last_activity_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def last_state_loss_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_state_loss_time DataDatabricksCluster#last_state_loss_time}.'''
        result = self._values.get("last_state_loss_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def node_type_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_type_id DataDatabricksCluster#node_type_id}.'''
        result = self._values.get("node_type_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#num_workers DataDatabricksCluster#num_workers}.'''
        result = self._values.get("num_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#policy_id DataDatabricksCluster#policy_id}.'''
        result = self._values.get("policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#single_user_name DataDatabricksCluster#single_user_name}.'''
        result = self._values.get("single_user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spark_conf(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_conf DataDatabricksCluster#spark_conf}.'''
        result = self._values.get("spark_conf")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def spark_context_id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_context_id DataDatabricksCluster#spark_context_id}.'''
        result = self._values.get("spark_context_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spark_env_vars(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_env_vars DataDatabricksCluster#spark_env_vars}.'''
        result = self._values.get("spark_env_vars")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def ssh_public_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ssh_public_keys DataDatabricksCluster#ssh_public_keys}.'''
        result = self._values.get("ssh_public_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def start_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_time DataDatabricksCluster#start_time}.'''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def state_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#state_message DataDatabricksCluster#state_message}.'''
        result = self._values.get("state_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def terminate_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#terminate_time DataDatabricksCluster#terminate_time}.'''
        result = self._values.get("terminate_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def termination_reason(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoTerminationReason"]:
        '''termination_reason block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#termination_reason DataDatabricksCluster#termination_reason}
        '''
        result = self._values.get("termination_reason")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoTerminationReason"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoAutoscale",
    jsii_struct_bases=[],
    name_mapping={"max_workers": "maxWorkers", "min_workers": "minWorkers"},
)
class DataDatabricksClusterClusterInfoAutoscale:
    def __init__(
        self,
        *,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#max_workers DataDatabricksCluster#max_workers}.
        :param min_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#min_workers DataDatabricksCluster#min_workers}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoAutoscale.__init__)
            check_type(argname="argument max_workers", value=max_workers, expected_type=type_hints["max_workers"])
            check_type(argname="argument min_workers", value=min_workers, expected_type=type_hints["min_workers"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_workers is not None:
            self._values["max_workers"] = max_workers
        if min_workers is not None:
            self._values["min_workers"] = min_workers

    @builtins.property
    def max_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#max_workers DataDatabricksCluster#max_workers}.'''
        result = self._values.get("max_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#min_workers DataDatabricksCluster#min_workers}.'''
        result = self._values.get("min_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoAutoscale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoAutoscaleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoAutoscaleOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoAutoscaleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxWorkers")
    def reset_max_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWorkers", []))

    @jsii.member(jsii_name="resetMinWorkers")
    def reset_min_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinWorkers", []))

    @builtins.property
    @jsii.member(jsii_name="maxWorkersInput")
    def max_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="minWorkersInput")
    def min_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWorkers")
    def max_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxWorkers"))

    @max_workers.setter
    def max_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAutoscaleOutputReference, "max_workers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="minWorkers")
    def min_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minWorkers"))

    @min_workers.setter
    def min_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAutoscaleOutputReference, "min_workers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoAutoscale]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoAutoscale], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoAutoscale],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAutoscaleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoAwsAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "ebs_volume_count": "ebsVolumeCount",
        "ebs_volume_size": "ebsVolumeSize",
        "ebs_volume_type": "ebsVolumeType",
        "first_on_demand": "firstOnDemand",
        "instance_profile_arn": "instanceProfileArn",
        "spot_bid_price_percent": "spotBidPricePercent",
        "zone_id": "zoneId",
    },
)
class DataDatabricksClusterClusterInfoAwsAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        ebs_volume_count: typing.Optional[jsii.Number] = None,
        ebs_volume_size: typing.Optional[jsii.Number] = None,
        ebs_volume_type: typing.Optional[builtins.str] = None,
        first_on_demand: typing.Optional[jsii.Number] = None,
        instance_profile_arn: typing.Optional[builtins.str] = None,
        spot_bid_price_percent: typing.Optional[jsii.Number] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.
        :param ebs_volume_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_count DataDatabricksCluster#ebs_volume_count}.
        :param ebs_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_size DataDatabricksCluster#ebs_volume_size}.
        :param ebs_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_type DataDatabricksCluster#ebs_volume_type}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#first_on_demand DataDatabricksCluster#first_on_demand}.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_profile_arn DataDatabricksCluster#instance_profile_arn}.
        :param spot_bid_price_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spot_bid_price_percent DataDatabricksCluster#spot_bid_price_percent}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#zone_id DataDatabricksCluster#zone_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoAwsAttributes.__init__)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument ebs_volume_count", value=ebs_volume_count, expected_type=type_hints["ebs_volume_count"])
            check_type(argname="argument ebs_volume_size", value=ebs_volume_size, expected_type=type_hints["ebs_volume_size"])
            check_type(argname="argument ebs_volume_type", value=ebs_volume_type, expected_type=type_hints["ebs_volume_type"])
            check_type(argname="argument first_on_demand", value=first_on_demand, expected_type=type_hints["first_on_demand"])
            check_type(argname="argument instance_profile_arn", value=instance_profile_arn, expected_type=type_hints["instance_profile_arn"])
            check_type(argname="argument spot_bid_price_percent", value=spot_bid_price_percent, expected_type=type_hints["spot_bid_price_percent"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if ebs_volume_count is not None:
            self._values["ebs_volume_count"] = ebs_volume_count
        if ebs_volume_size is not None:
            self._values["ebs_volume_size"] = ebs_volume_size
        if ebs_volume_type is not None:
            self._values["ebs_volume_type"] = ebs_volume_type
        if first_on_demand is not None:
            self._values["first_on_demand"] = first_on_demand
        if instance_profile_arn is not None:
            self._values["instance_profile_arn"] = instance_profile_arn
        if spot_bid_price_percent is not None:
            self._values["spot_bid_price_percent"] = spot_bid_price_percent
        if zone_id is not None:
            self._values["zone_id"] = zone_id

    @builtins.property
    def availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_volume_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_count DataDatabricksCluster#ebs_volume_count}.'''
        result = self._values.get("ebs_volume_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ebs_volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_size DataDatabricksCluster#ebs_volume_size}.'''
        result = self._values.get("ebs_volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ebs_volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_type DataDatabricksCluster#ebs_volume_type}.'''
        result = self._values.get("ebs_volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_on_demand(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#first_on_demand DataDatabricksCluster#first_on_demand}.'''
        result = self._values.get("first_on_demand")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_profile_arn DataDatabricksCluster#instance_profile_arn}.'''
        result = self._values.get("instance_profile_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_bid_price_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spot_bid_price_percent DataDatabricksCluster#spot_bid_price_percent}.'''
        result = self._values.get("spot_bid_price_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#zone_id DataDatabricksCluster#zone_id}.'''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoAwsAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoAwsAttributesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoAwsAttributesOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoAwsAttributesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

    @jsii.member(jsii_name="resetEbsVolumeCount")
    def reset_ebs_volume_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsVolumeCount", []))

    @jsii.member(jsii_name="resetEbsVolumeSize")
    def reset_ebs_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsVolumeSize", []))

    @jsii.member(jsii_name="resetEbsVolumeType")
    def reset_ebs_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsVolumeType", []))

    @jsii.member(jsii_name="resetFirstOnDemand")
    def reset_first_on_demand(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstOnDemand", []))

    @jsii.member(jsii_name="resetInstanceProfileArn")
    def reset_instance_profile_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceProfileArn", []))

    @jsii.member(jsii_name="resetSpotBidPricePercent")
    def reset_spot_bid_price_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotBidPricePercent", []))

    @jsii.member(jsii_name="resetZoneId")
    def reset_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneId", []))

    @builtins.property
    @jsii.member(jsii_name="availabilityInput")
    def availability_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeCountInput")
    def ebs_volume_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ebsVolumeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeSizeInput")
    def ebs_volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ebsVolumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeTypeInput")
    def ebs_volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ebsVolumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="firstOnDemandInput")
    def first_on_demand_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "firstOnDemandInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArnInput")
    def instance_profile_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProfileArnInput"))

    @builtins.property
    @jsii.member(jsii_name="spotBidPricePercentInput")
    def spot_bid_price_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "spotBidPricePercentInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="availability")
    def availability(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availability"))

    @availability.setter
    def availability(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAwsAttributesOutputReference, "availability").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeCount")
    def ebs_volume_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsVolumeCount"))

    @ebs_volume_count.setter
    def ebs_volume_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAwsAttributesOutputReference, "ebs_volume_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeCount", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeSize")
    def ebs_volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsVolumeSize"))

    @ebs_volume_size.setter
    def ebs_volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAwsAttributesOutputReference, "ebs_volume_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeType")
    def ebs_volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ebsVolumeType"))

    @ebs_volume_type.setter
    def ebs_volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAwsAttributesOutputReference, "ebs_volume_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeType", value)

    @builtins.property
    @jsii.member(jsii_name="firstOnDemand")
    def first_on_demand(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "firstOnDemand"))

    @first_on_demand.setter
    def first_on_demand(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAwsAttributesOutputReference, "first_on_demand").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstOnDemand", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArn")
    def instance_profile_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileArn"))

    @instance_profile_arn.setter
    def instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAwsAttributesOutputReference, "instance_profile_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="spotBidPricePercent")
    def spot_bid_price_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotBidPricePercent"))

    @spot_bid_price_percent.setter
    def spot_bid_price_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAwsAttributesOutputReference, "spot_bid_price_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotBidPricePercent", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAwsAttributesOutputReference, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoAwsAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoAwsAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoAwsAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAwsAttributesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoAzureAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "first_on_demand": "firstOnDemand",
        "spot_bid_max_price": "spotBidMaxPrice",
    },
)
class DataDatabricksClusterClusterInfoAzureAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        first_on_demand: typing.Optional[jsii.Number] = None,
        spot_bid_max_price: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#first_on_demand DataDatabricksCluster#first_on_demand}.
        :param spot_bid_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spot_bid_max_price DataDatabricksCluster#spot_bid_max_price}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoAzureAttributes.__init__)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument first_on_demand", value=first_on_demand, expected_type=type_hints["first_on_demand"])
            check_type(argname="argument spot_bid_max_price", value=spot_bid_max_price, expected_type=type_hints["spot_bid_max_price"])
        self._values: typing.Dict[str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if first_on_demand is not None:
            self._values["first_on_demand"] = first_on_demand
        if spot_bid_max_price is not None:
            self._values["spot_bid_max_price"] = spot_bid_max_price

    @builtins.property
    def availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_on_demand(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#first_on_demand DataDatabricksCluster#first_on_demand}.'''
        result = self._values.get("first_on_demand")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spot_bid_max_price(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spot_bid_max_price DataDatabricksCluster#spot_bid_max_price}.'''
        result = self._values.get("spot_bid_max_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoAzureAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoAzureAttributesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoAzureAttributesOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoAzureAttributesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

    @jsii.member(jsii_name="resetFirstOnDemand")
    def reset_first_on_demand(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstOnDemand", []))

    @jsii.member(jsii_name="resetSpotBidMaxPrice")
    def reset_spot_bid_max_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotBidMaxPrice", []))

    @builtins.property
    @jsii.member(jsii_name="availabilityInput")
    def availability_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="firstOnDemandInput")
    def first_on_demand_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "firstOnDemandInput"))

    @builtins.property
    @jsii.member(jsii_name="spotBidMaxPriceInput")
    def spot_bid_max_price_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "spotBidMaxPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="availability")
    def availability(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availability"))

    @availability.setter
    def availability(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAzureAttributesOutputReference, "availability").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="firstOnDemand")
    def first_on_demand(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "firstOnDemand"))

    @first_on_demand.setter
    def first_on_demand(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAzureAttributesOutputReference, "first_on_demand").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstOnDemand", value)

    @builtins.property
    @jsii.member(jsii_name="spotBidMaxPrice")
    def spot_bid_max_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotBidMaxPrice"))

    @spot_bid_max_price.setter
    def spot_bid_max_price(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAzureAttributesOutputReference, "spot_bid_max_price").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotBidMaxPrice", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoAzureAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoAzureAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoAzureAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoAzureAttributesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogConf",
    jsii_struct_bases=[],
    name_mapping={"dbfs": "dbfs", "s3": "s3"},
)
class DataDatabricksClusterClusterInfoClusterLogConf:
    def __init__(
        self,
        *,
        dbfs: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoClusterLogConfDbfs", typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoClusterLogConfS3", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dbfs: dbfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#dbfs DataDatabricksCluster#dbfs}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#s3 DataDatabricksCluster#s3}
        '''
        if isinstance(dbfs, dict):
            dbfs = DataDatabricksClusterClusterInfoClusterLogConfDbfs(**dbfs)
        if isinstance(s3, dict):
            s3 = DataDatabricksClusterClusterInfoClusterLogConfS3(**s3)
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoClusterLogConf.__init__)
            check_type(argname="argument dbfs", value=dbfs, expected_type=type_hints["dbfs"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dbfs is not None:
            self._values["dbfs"] = dbfs
        if s3 is not None:
            self._values["s3"] = s3

    @builtins.property
    def dbfs(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoClusterLogConfDbfs"]:
        '''dbfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#dbfs DataDatabricksCluster#dbfs}
        '''
        result = self._values.get("dbfs")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoClusterLogConfDbfs"], result)

    @builtins.property
    def s3(self) -> typing.Optional["DataDatabricksClusterClusterInfoClusterLogConfS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#s3 DataDatabricksCluster#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoClusterLogConfS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoClusterLogConf(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogConfDbfs",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class DataDatabricksClusterClusterInfoClusterLogConfDbfs:
    def __init__(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoClusterLogConfDbfs.__init__)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoClusterLogConfDbfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoClusterLogConfDbfsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogConfDbfsOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoClusterLogConfDbfsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoClusterLogConfDbfsOutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfDbfs]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfDbfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfDbfs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoClusterLogConfDbfsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksClusterClusterInfoClusterLogConfOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogConfOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoClusterLogConfOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDbfs")
    def put_dbfs(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        '''
        value = DataDatabricksClusterClusterInfoClusterLogConfDbfs(
            destination=destination
        )

        return typing.cast(None, jsii.invoke(self, "putDbfs", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        destination: builtins.str,
        canned_acl: typing.Optional[builtins.str] = None,
        enable_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#canned_acl DataDatabricksCluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_encryption DataDatabricksCluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#encryption_type DataDatabricksCluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#endpoint DataDatabricksCluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#kms_key DataDatabricksCluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#region DataDatabricksCluster#region}.
        '''
        value = DataDatabricksClusterClusterInfoClusterLogConfS3(
            destination=destination,
            canned_acl=canned_acl,
            enable_encryption=enable_encryption,
            encryption_type=encryption_type,
            endpoint=endpoint,
            kms_key=kms_key,
            region=region,
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="resetDbfs")
    def reset_dbfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbfs", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @builtins.property
    @jsii.member(jsii_name="dbfs")
    def dbfs(self) -> DataDatabricksClusterClusterInfoClusterLogConfDbfsOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoClusterLogConfDbfsOutputReference, jsii.get(self, "dbfs"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference":
        return typing.cast("DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="dbfsInput")
    def dbfs_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfDbfs]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfDbfs], jsii.get(self, "dbfsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoClusterLogConfS3"]:
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoClusterLogConfS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoClusterLogConf]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoClusterLogConf], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoClusterLogConf],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoClusterLogConfOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogConfS3",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "canned_acl": "cannedAcl",
        "enable_encryption": "enableEncryption",
        "encryption_type": "encryptionType",
        "endpoint": "endpoint",
        "kms_key": "kmsKey",
        "region": "region",
    },
)
class DataDatabricksClusterClusterInfoClusterLogConfS3:
    def __init__(
        self,
        *,
        destination: builtins.str,
        canned_acl: typing.Optional[builtins.str] = None,
        enable_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#canned_acl DataDatabricksCluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_encryption DataDatabricksCluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#encryption_type DataDatabricksCluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#endpoint DataDatabricksCluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#kms_key DataDatabricksCluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#region DataDatabricksCluster#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoClusterLogConfS3.__init__)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument canned_acl", value=canned_acl, expected_type=type_hints["canned_acl"])
            check_type(argname="argument enable_encryption", value=enable_encryption, expected_type=type_hints["enable_encryption"])
            check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
        }
        if canned_acl is not None:
            self._values["canned_acl"] = canned_acl
        if enable_encryption is not None:
            self._values["enable_encryption"] = enable_encryption
        if encryption_type is not None:
            self._values["encryption_type"] = encryption_type
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def canned_acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#canned_acl DataDatabricksCluster#canned_acl}.'''
        result = self._values.get("canned_acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_encryption DataDatabricksCluster#enable_encryption}.'''
        result = self._values.get("enable_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encryption_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#encryption_type DataDatabricksCluster#encryption_type}.'''
        result = self._values.get("encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#endpoint DataDatabricksCluster#endpoint}.'''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#kms_key DataDatabricksCluster#kms_key}.'''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#region DataDatabricksCluster#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoClusterLogConfS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCannedAcl")
    def reset_canned_acl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCannedAcl", []))

    @jsii.member(jsii_name="resetEnableEncryption")
    def reset_enable_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableEncryption", []))

    @jsii.member(jsii_name="resetEncryptionType")
    def reset_encryption_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionType", []))

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @jsii.member(jsii_name="resetKmsKey")
    def reset_kms_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKey", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @builtins.property
    @jsii.member(jsii_name="cannedAclInput")
    def canned_acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cannedAclInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="enableEncryptionInput")
    def enable_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionTypeInput")
    def encryption_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyInput")
    def kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="cannedAcl")
    def canned_acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cannedAcl"))

    @canned_acl.setter
    def canned_acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference, "canned_acl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cannedAcl", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="enableEncryption")
    def enable_encryption(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableEncryption"))

    @enable_encryption.setter
    def enable_encryption(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference, "enable_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference, "encryption_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference, "kms_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfS3]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogStatus",
    jsii_struct_bases=[],
    name_mapping={
        "last_attempted": "lastAttempted",
        "last_exception": "lastException",
    },
)
class DataDatabricksClusterClusterInfoClusterLogStatus:
    def __init__(
        self,
        *,
        last_attempted: typing.Optional[jsii.Number] = None,
        last_exception: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param last_attempted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_attempted DataDatabricksCluster#last_attempted}.
        :param last_exception: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_exception DataDatabricksCluster#last_exception}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoClusterLogStatus.__init__)
            check_type(argname="argument last_attempted", value=last_attempted, expected_type=type_hints["last_attempted"])
            check_type(argname="argument last_exception", value=last_exception, expected_type=type_hints["last_exception"])
        self._values: typing.Dict[str, typing.Any] = {}
        if last_attempted is not None:
            self._values["last_attempted"] = last_attempted
        if last_exception is not None:
            self._values["last_exception"] = last_exception

    @builtins.property
    def last_attempted(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_attempted DataDatabricksCluster#last_attempted}.'''
        result = self._values.get("last_attempted")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def last_exception(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_exception DataDatabricksCluster#last_exception}.'''
        result = self._values.get("last_exception")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoClusterLogStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoClusterLogStatusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogStatusOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoClusterLogStatusOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLastAttempted")
    def reset_last_attempted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastAttempted", []))

    @jsii.member(jsii_name="resetLastException")
    def reset_last_exception(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastException", []))

    @builtins.property
    @jsii.member(jsii_name="lastAttemptedInput")
    def last_attempted_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lastAttemptedInput"))

    @builtins.property
    @jsii.member(jsii_name="lastExceptionInput")
    def last_exception_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastExceptionInput"))

    @builtins.property
    @jsii.member(jsii_name="lastAttempted")
    def last_attempted(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lastAttempted"))

    @last_attempted.setter
    def last_attempted(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoClusterLogStatusOutputReference, "last_attempted").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastAttempted", value)

    @builtins.property
    @jsii.member(jsii_name="lastException")
    def last_exception(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastException"))

    @last_exception.setter
    def last_exception(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoClusterLogStatusOutputReference, "last_exception").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastException", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoClusterLogStatus]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoClusterLogStatus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoClusterLogStatus],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoClusterLogStatusOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDockerImage",
    jsii_struct_bases=[],
    name_mapping={"url": "url", "basic_auth": "basicAuth"},
)
class DataDatabricksClusterClusterInfoDockerImage:
    def __init__(
        self,
        *,
        url: builtins.str,
        basic_auth: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoDockerImageBasicAuth", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#url DataDatabricksCluster#url}.
        :param basic_auth: basic_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#basic_auth DataDatabricksCluster#basic_auth}
        '''
        if isinstance(basic_auth, dict):
            basic_auth = DataDatabricksClusterClusterInfoDockerImageBasicAuth(**basic_auth)
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoDockerImage.__init__)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument basic_auth", value=basic_auth, expected_type=type_hints["basic_auth"])
        self._values: typing.Dict[str, typing.Any] = {
            "url": url,
        }
        if basic_auth is not None:
            self._values["basic_auth"] = basic_auth

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#url DataDatabricksCluster#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def basic_auth(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoDockerImageBasicAuth"]:
        '''basic_auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#basic_auth DataDatabricksCluster#basic_auth}
        '''
        result = self._values.get("basic_auth")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoDockerImageBasicAuth"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoDockerImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDockerImageBasicAuth",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class DataDatabricksClusterClusterInfoDockerImageBasicAuth:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#password DataDatabricksCluster#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#username DataDatabricksCluster#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoDockerImageBasicAuth.__init__)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#password DataDatabricksCluster#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#username DataDatabricksCluster#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoDockerImageBasicAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoDockerImageBasicAuthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDockerImageBasicAuthOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoDockerImageBasicAuthOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoDockerImageBasicAuthOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoDockerImageBasicAuthOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoDockerImageBasicAuth]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDockerImageBasicAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoDockerImageBasicAuth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoDockerImageBasicAuthOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksClusterClusterInfoDockerImageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDockerImageOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoDockerImageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBasicAuth")
    def put_basic_auth(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#password DataDatabricksCluster#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#username DataDatabricksCluster#username}.
        '''
        value = DataDatabricksClusterClusterInfoDockerImageBasicAuth(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putBasicAuth", [value]))

    @jsii.member(jsii_name="resetBasicAuth")
    def reset_basic_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuth", []))

    @builtins.property
    @jsii.member(jsii_name="basicAuth")
    def basic_auth(
        self,
    ) -> DataDatabricksClusterClusterInfoDockerImageBasicAuthOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoDockerImageBasicAuthOutputReference, jsii.get(self, "basicAuth"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthInput")
    def basic_auth_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoDockerImageBasicAuth]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDockerImageBasicAuth], jsii.get(self, "basicAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoDockerImageOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoDockerImage]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDockerImage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoDockerImage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoDockerImageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDriver",
    jsii_struct_bases=[],
    name_mapping={
        "host_private_ip": "hostPrivateIp",
        "instance_id": "instanceId",
        "node_aws_attributes": "nodeAwsAttributes",
        "node_id": "nodeId",
        "private_ip": "privateIp",
        "public_dns": "publicDns",
        "start_timestamp": "startTimestamp",
    },
)
class DataDatabricksClusterClusterInfoDriver:
    def __init__(
        self,
        *,
        host_private_ip: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
        node_aws_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoDriverNodeAwsAttributes", typing.Dict[str, typing.Any]]] = None,
        node_id: typing.Optional[builtins.str] = None,
        private_ip: typing.Optional[builtins.str] = None,
        public_dns: typing.Optional[builtins.str] = None,
        start_timestamp: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param host_private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#host_private_ip DataDatabricksCluster#host_private_ip}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_id DataDatabricksCluster#instance_id}.
        :param node_aws_attributes: node_aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_aws_attributes DataDatabricksCluster#node_aws_attributes}
        :param node_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_id DataDatabricksCluster#node_id}.
        :param private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#private_ip DataDatabricksCluster#private_ip}.
        :param public_dns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#public_dns DataDatabricksCluster#public_dns}.
        :param start_timestamp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_timestamp DataDatabricksCluster#start_timestamp}.
        '''
        if isinstance(node_aws_attributes, dict):
            node_aws_attributes = DataDatabricksClusterClusterInfoDriverNodeAwsAttributes(**node_aws_attributes)
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoDriver.__init__)
            check_type(argname="argument host_private_ip", value=host_private_ip, expected_type=type_hints["host_private_ip"])
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument node_aws_attributes", value=node_aws_attributes, expected_type=type_hints["node_aws_attributes"])
            check_type(argname="argument node_id", value=node_id, expected_type=type_hints["node_id"])
            check_type(argname="argument private_ip", value=private_ip, expected_type=type_hints["private_ip"])
            check_type(argname="argument public_dns", value=public_dns, expected_type=type_hints["public_dns"])
            check_type(argname="argument start_timestamp", value=start_timestamp, expected_type=type_hints["start_timestamp"])
        self._values: typing.Dict[str, typing.Any] = {}
        if host_private_ip is not None:
            self._values["host_private_ip"] = host_private_ip
        if instance_id is not None:
            self._values["instance_id"] = instance_id
        if node_aws_attributes is not None:
            self._values["node_aws_attributes"] = node_aws_attributes
        if node_id is not None:
            self._values["node_id"] = node_id
        if private_ip is not None:
            self._values["private_ip"] = private_ip
        if public_dns is not None:
            self._values["public_dns"] = public_dns
        if start_timestamp is not None:
            self._values["start_timestamp"] = start_timestamp

    @builtins.property
    def host_private_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#host_private_ip DataDatabricksCluster#host_private_ip}.'''
        result = self._values.get("host_private_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_id DataDatabricksCluster#instance_id}.'''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_aws_attributes(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoDriverNodeAwsAttributes"]:
        '''node_aws_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_aws_attributes DataDatabricksCluster#node_aws_attributes}
        '''
        result = self._values.get("node_aws_attributes")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoDriverNodeAwsAttributes"], result)

    @builtins.property
    def node_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_id DataDatabricksCluster#node_id}.'''
        result = self._values.get("node_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#private_ip DataDatabricksCluster#private_ip}.'''
        result = self._values.get("private_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_dns(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#public_dns DataDatabricksCluster#public_dns}.'''
        result = self._values.get("public_dns")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_timestamp(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_timestamp DataDatabricksCluster#start_timestamp}.'''
        result = self._values.get("start_timestamp")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoDriver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDriverNodeAwsAttributes",
    jsii_struct_bases=[],
    name_mapping={"is_spot": "isSpot"},
)
class DataDatabricksClusterClusterInfoDriverNodeAwsAttributes:
    def __init__(
        self,
        *,
        is_spot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param is_spot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#is_spot DataDatabricksCluster#is_spot}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoDriverNodeAwsAttributes.__init__)
            check_type(argname="argument is_spot", value=is_spot, expected_type=type_hints["is_spot"])
        self._values: typing.Dict[str, typing.Any] = {}
        if is_spot is not None:
            self._values["is_spot"] = is_spot

    @builtins.property
    def is_spot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#is_spot DataDatabricksCluster#is_spot}.'''
        result = self._values.get("is_spot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoDriverNodeAwsAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoDriverNodeAwsAttributesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDriverNodeAwsAttributesOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoDriverNodeAwsAttributesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsSpot")
    def reset_is_spot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsSpot", []))

    @builtins.property
    @jsii.member(jsii_name="isSpotInput")
    def is_spot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isSpotInput"))

    @builtins.property
    @jsii.member(jsii_name="isSpot")
    def is_spot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isSpot"))

    @is_spot.setter
    def is_spot(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoDriverNodeAwsAttributesOutputReference, "is_spot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isSpot", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoDriverNodeAwsAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDriverNodeAwsAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoDriverNodeAwsAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoDriverNodeAwsAttributesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksClusterClusterInfoDriverOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDriverOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoDriverOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNodeAwsAttributes")
    def put_node_aws_attributes(
        self,
        *,
        is_spot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param is_spot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#is_spot DataDatabricksCluster#is_spot}.
        '''
        value = DataDatabricksClusterClusterInfoDriverNodeAwsAttributes(
            is_spot=is_spot
        )

        return typing.cast(None, jsii.invoke(self, "putNodeAwsAttributes", [value]))

    @jsii.member(jsii_name="resetHostPrivateIp")
    def reset_host_private_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPrivateIp", []))

    @jsii.member(jsii_name="resetInstanceId")
    def reset_instance_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceId", []))

    @jsii.member(jsii_name="resetNodeAwsAttributes")
    def reset_node_aws_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeAwsAttributes", []))

    @jsii.member(jsii_name="resetNodeId")
    def reset_node_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeId", []))

    @jsii.member(jsii_name="resetPrivateIp")
    def reset_private_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIp", []))

    @jsii.member(jsii_name="resetPublicDns")
    def reset_public_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicDns", []))

    @jsii.member(jsii_name="resetStartTimestamp")
    def reset_start_timestamp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTimestamp", []))

    @builtins.property
    @jsii.member(jsii_name="nodeAwsAttributes")
    def node_aws_attributes(
        self,
    ) -> DataDatabricksClusterClusterInfoDriverNodeAwsAttributesOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoDriverNodeAwsAttributesOutputReference, jsii.get(self, "nodeAwsAttributes"))

    @builtins.property
    @jsii.member(jsii_name="hostPrivateIpInput")
    def host_private_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostPrivateIpInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeAwsAttributesInput")
    def node_aws_attributes_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoDriverNodeAwsAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDriverNodeAwsAttributes], jsii.get(self, "nodeAwsAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeIdInput")
    def node_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpInput")
    def private_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpInput"))

    @builtins.property
    @jsii.member(jsii_name="publicDnsInput")
    def public_dns_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicDnsInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimestampInput")
    def start_timestamp_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startTimestampInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPrivateIp")
    def host_private_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostPrivateIp"))

    @host_private_ip.setter
    def host_private_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoDriverOutputReference, "host_private_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostPrivateIp", value)

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoDriverOutputReference, "instance_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value)

    @builtins.property
    @jsii.member(jsii_name="nodeId")
    def node_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeId"))

    @node_id.setter
    def node_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoDriverOutputReference, "node_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeId", value)

    @builtins.property
    @jsii.member(jsii_name="privateIp")
    def private_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIp"))

    @private_ip.setter
    def private_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoDriverOutputReference, "private_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIp", value)

    @builtins.property
    @jsii.member(jsii_name="publicDns")
    def public_dns(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicDns"))

    @public_dns.setter
    def public_dns(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoDriverOutputReference, "public_dns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicDns", value)

    @builtins.property
    @jsii.member(jsii_name="startTimestamp")
    def start_timestamp(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startTimestamp"))

    @start_timestamp.setter
    def start_timestamp(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoDriverOutputReference, "start_timestamp").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTimestamp", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataDatabricksClusterClusterInfoDriver]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDriver], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoDriver],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoDriverOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoExecutors",
    jsii_struct_bases=[],
    name_mapping={
        "host_private_ip": "hostPrivateIp",
        "instance_id": "instanceId",
        "node_aws_attributes": "nodeAwsAttributes",
        "node_id": "nodeId",
        "private_ip": "privateIp",
        "public_dns": "publicDns",
        "start_timestamp": "startTimestamp",
    },
)
class DataDatabricksClusterClusterInfoExecutors:
    def __init__(
        self,
        *,
        host_private_ip: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
        node_aws_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes", typing.Dict[str, typing.Any]]] = None,
        node_id: typing.Optional[builtins.str] = None,
        private_ip: typing.Optional[builtins.str] = None,
        public_dns: typing.Optional[builtins.str] = None,
        start_timestamp: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param host_private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#host_private_ip DataDatabricksCluster#host_private_ip}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_id DataDatabricksCluster#instance_id}.
        :param node_aws_attributes: node_aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_aws_attributes DataDatabricksCluster#node_aws_attributes}
        :param node_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_id DataDatabricksCluster#node_id}.
        :param private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#private_ip DataDatabricksCluster#private_ip}.
        :param public_dns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#public_dns DataDatabricksCluster#public_dns}.
        :param start_timestamp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_timestamp DataDatabricksCluster#start_timestamp}.
        '''
        if isinstance(node_aws_attributes, dict):
            node_aws_attributes = DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes(**node_aws_attributes)
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoExecutors.__init__)
            check_type(argname="argument host_private_ip", value=host_private_ip, expected_type=type_hints["host_private_ip"])
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument node_aws_attributes", value=node_aws_attributes, expected_type=type_hints["node_aws_attributes"])
            check_type(argname="argument node_id", value=node_id, expected_type=type_hints["node_id"])
            check_type(argname="argument private_ip", value=private_ip, expected_type=type_hints["private_ip"])
            check_type(argname="argument public_dns", value=public_dns, expected_type=type_hints["public_dns"])
            check_type(argname="argument start_timestamp", value=start_timestamp, expected_type=type_hints["start_timestamp"])
        self._values: typing.Dict[str, typing.Any] = {}
        if host_private_ip is not None:
            self._values["host_private_ip"] = host_private_ip
        if instance_id is not None:
            self._values["instance_id"] = instance_id
        if node_aws_attributes is not None:
            self._values["node_aws_attributes"] = node_aws_attributes
        if node_id is not None:
            self._values["node_id"] = node_id
        if private_ip is not None:
            self._values["private_ip"] = private_ip
        if public_dns is not None:
            self._values["public_dns"] = public_dns
        if start_timestamp is not None:
            self._values["start_timestamp"] = start_timestamp

    @builtins.property
    def host_private_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#host_private_ip DataDatabricksCluster#host_private_ip}.'''
        result = self._values.get("host_private_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_id DataDatabricksCluster#instance_id}.'''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_aws_attributes(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes"]:
        '''node_aws_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_aws_attributes DataDatabricksCluster#node_aws_attributes}
        '''
        result = self._values.get("node_aws_attributes")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes"], result)

    @builtins.property
    def node_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_id DataDatabricksCluster#node_id}.'''
        result = self._values.get("node_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#private_ip DataDatabricksCluster#private_ip}.'''
        result = self._values.get("private_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_dns(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#public_dns DataDatabricksCluster#public_dns}.'''
        result = self._values.get("public_dns")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_timestamp(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_timestamp DataDatabricksCluster#start_timestamp}.'''
        result = self._values.get("start_timestamp")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoExecutors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoExecutorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoExecutorsList",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoExecutorsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDatabricksClusterClusterInfoExecutorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoExecutorsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataDatabricksClusterClusterInfoExecutorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoExecutorsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoExecutorsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoExecutorsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDatabricksClusterClusterInfoExecutors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDatabricksClusterClusterInfoExecutors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDatabricksClusterClusterInfoExecutors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoExecutorsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes",
    jsii_struct_bases=[],
    name_mapping={"is_spot": "isSpot"},
)
class DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes:
    def __init__(
        self,
        *,
        is_spot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param is_spot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#is_spot DataDatabricksCluster#is_spot}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes.__init__)
            check_type(argname="argument is_spot", value=is_spot, expected_type=type_hints["is_spot"])
        self._values: typing.Dict[str, typing.Any] = {}
        if is_spot is not None:
            self._values["is_spot"] = is_spot

    @builtins.property
    def is_spot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#is_spot DataDatabricksCluster#is_spot}.'''
        result = self._values.get("is_spot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributesOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsSpot")
    def reset_is_spot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsSpot", []))

    @builtins.property
    @jsii.member(jsii_name="isSpotInput")
    def is_spot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isSpotInput"))

    @builtins.property
    @jsii.member(jsii_name="isSpot")
    def is_spot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isSpot"))

    @is_spot.setter
    def is_spot(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributesOutputReference, "is_spot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isSpot", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksClusterClusterInfoExecutorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoExecutorsOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoExecutorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNodeAwsAttributes")
    def put_node_aws_attributes(
        self,
        *,
        is_spot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param is_spot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#is_spot DataDatabricksCluster#is_spot}.
        '''
        value = DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes(
            is_spot=is_spot
        )

        return typing.cast(None, jsii.invoke(self, "putNodeAwsAttributes", [value]))

    @jsii.member(jsii_name="resetHostPrivateIp")
    def reset_host_private_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPrivateIp", []))

    @jsii.member(jsii_name="resetInstanceId")
    def reset_instance_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceId", []))

    @jsii.member(jsii_name="resetNodeAwsAttributes")
    def reset_node_aws_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeAwsAttributes", []))

    @jsii.member(jsii_name="resetNodeId")
    def reset_node_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeId", []))

    @jsii.member(jsii_name="resetPrivateIp")
    def reset_private_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIp", []))

    @jsii.member(jsii_name="resetPublicDns")
    def reset_public_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicDns", []))

    @jsii.member(jsii_name="resetStartTimestamp")
    def reset_start_timestamp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTimestamp", []))

    @builtins.property
    @jsii.member(jsii_name="nodeAwsAttributes")
    def node_aws_attributes(
        self,
    ) -> DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributesOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributesOutputReference, jsii.get(self, "nodeAwsAttributes"))

    @builtins.property
    @jsii.member(jsii_name="hostPrivateIpInput")
    def host_private_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostPrivateIpInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeAwsAttributesInput")
    def node_aws_attributes_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes], jsii.get(self, "nodeAwsAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeIdInput")
    def node_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpInput")
    def private_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpInput"))

    @builtins.property
    @jsii.member(jsii_name="publicDnsInput")
    def public_dns_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicDnsInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimestampInput")
    def start_timestamp_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startTimestampInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPrivateIp")
    def host_private_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostPrivateIp"))

    @host_private_ip.setter
    def host_private_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoExecutorsOutputReference, "host_private_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostPrivateIp", value)

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoExecutorsOutputReference, "instance_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value)

    @builtins.property
    @jsii.member(jsii_name="nodeId")
    def node_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeId"))

    @node_id.setter
    def node_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoExecutorsOutputReference, "node_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeId", value)

    @builtins.property
    @jsii.member(jsii_name="privateIp")
    def private_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIp"))

    @private_ip.setter
    def private_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoExecutorsOutputReference, "private_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIp", value)

    @builtins.property
    @jsii.member(jsii_name="publicDns")
    def public_dns(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicDns"))

    @public_dns.setter
    def public_dns(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoExecutorsOutputReference, "public_dns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicDns", value)

    @builtins.property
    @jsii.member(jsii_name="startTimestamp")
    def start_timestamp(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startTimestamp"))

    @start_timestamp.setter
    def start_timestamp(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoExecutorsOutputReference, "start_timestamp").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTimestamp", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataDatabricksClusterClusterInfoExecutors, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataDatabricksClusterClusterInfoExecutors, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoExecutors, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoExecutorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoGcpAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "boot_disk_size": "bootDiskSize",
        "google_service_account": "googleServiceAccount",
        "use_preemptible_executors": "usePreemptibleExecutors",
        "zone_id": "zoneId",
    },
)
class DataDatabricksClusterClusterInfoGcpAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        boot_disk_size: typing.Optional[jsii.Number] = None,
        google_service_account: typing.Optional[builtins.str] = None,
        use_preemptible_executors: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.
        :param boot_disk_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#boot_disk_size DataDatabricksCluster#boot_disk_size}.
        :param google_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#google_service_account DataDatabricksCluster#google_service_account}.
        :param use_preemptible_executors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#use_preemptible_executors DataDatabricksCluster#use_preemptible_executors}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#zone_id DataDatabricksCluster#zone_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoGcpAttributes.__init__)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument boot_disk_size", value=boot_disk_size, expected_type=type_hints["boot_disk_size"])
            check_type(argname="argument google_service_account", value=google_service_account, expected_type=type_hints["google_service_account"])
            check_type(argname="argument use_preemptible_executors", value=use_preemptible_executors, expected_type=type_hints["use_preemptible_executors"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if boot_disk_size is not None:
            self._values["boot_disk_size"] = boot_disk_size
        if google_service_account is not None:
            self._values["google_service_account"] = google_service_account
        if use_preemptible_executors is not None:
            self._values["use_preemptible_executors"] = use_preemptible_executors
        if zone_id is not None:
            self._values["zone_id"] = zone_id

    @builtins.property
    def availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def boot_disk_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#boot_disk_size DataDatabricksCluster#boot_disk_size}.'''
        result = self._values.get("boot_disk_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def google_service_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#google_service_account DataDatabricksCluster#google_service_account}.'''
        result = self._values.get("google_service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_preemptible_executors(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#use_preemptible_executors DataDatabricksCluster#use_preemptible_executors}.'''
        result = self._values.get("use_preemptible_executors")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#zone_id DataDatabricksCluster#zone_id}.'''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoGcpAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoGcpAttributesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoGcpAttributesOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoGcpAttributesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

    @jsii.member(jsii_name="resetBootDiskSize")
    def reset_boot_disk_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskSize", []))

    @jsii.member(jsii_name="resetGoogleServiceAccount")
    def reset_google_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleServiceAccount", []))

    @jsii.member(jsii_name="resetUsePreemptibleExecutors")
    def reset_use_preemptible_executors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsePreemptibleExecutors", []))

    @jsii.member(jsii_name="resetZoneId")
    def reset_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneId", []))

    @builtins.property
    @jsii.member(jsii_name="availabilityInput")
    def availability_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskSizeInput")
    def boot_disk_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bootDiskSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccountInput")
    def google_service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleServiceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="usePreemptibleExecutorsInput")
    def use_preemptible_executors_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "usePreemptibleExecutorsInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="availability")
    def availability(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availability"))

    @availability.setter
    def availability(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoGcpAttributesOutputReference, "availability").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="bootDiskSize")
    def boot_disk_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bootDiskSize"))

    @boot_disk_size.setter
    def boot_disk_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoGcpAttributesOutputReference, "boot_disk_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskSize", value)

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccount")
    def google_service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "googleServiceAccount"))

    @google_service_account.setter
    def google_service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoGcpAttributesOutputReference, "google_service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "googleServiceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="usePreemptibleExecutors")
    def use_preemptible_executors(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "usePreemptibleExecutors"))

    @use_preemptible_executors.setter
    def use_preemptible_executors(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoGcpAttributesOutputReference, "use_preemptible_executors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usePreemptibleExecutors", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoGcpAttributesOutputReference, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoGcpAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoGcpAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoGcpAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoGcpAttributesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScripts",
    jsii_struct_bases=[],
    name_mapping={"dbfs": "dbfs", "s3": "s3"},
)
class DataDatabricksClusterClusterInfoInitScripts:
    def __init__(
        self,
        *,
        dbfs: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoInitScriptsDbfs", typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoInitScriptsS3", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dbfs: dbfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#dbfs DataDatabricksCluster#dbfs}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#s3 DataDatabricksCluster#s3}
        '''
        if isinstance(dbfs, dict):
            dbfs = DataDatabricksClusterClusterInfoInitScriptsDbfs(**dbfs)
        if isinstance(s3, dict):
            s3 = DataDatabricksClusterClusterInfoInitScriptsS3(**s3)
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoInitScripts.__init__)
            check_type(argname="argument dbfs", value=dbfs, expected_type=type_hints["dbfs"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dbfs is not None:
            self._values["dbfs"] = dbfs
        if s3 is not None:
            self._values["s3"] = s3

    @builtins.property
    def dbfs(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoInitScriptsDbfs"]:
        '''dbfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#dbfs DataDatabricksCluster#dbfs}
        '''
        result = self._values.get("dbfs")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoInitScriptsDbfs"], result)

    @builtins.property
    def s3(self) -> typing.Optional["DataDatabricksClusterClusterInfoInitScriptsS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#s3 DataDatabricksCluster#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoInitScriptsS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoInitScripts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsDbfs",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class DataDatabricksClusterClusterInfoInitScriptsDbfs:
    def __init__(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoInitScriptsDbfs.__init__)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoInitScriptsDbfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoInitScriptsDbfsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsDbfsOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoInitScriptsDbfsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoInitScriptsDbfsOutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoInitScriptsDbfs]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoInitScriptsDbfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoInitScriptsDbfs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoInitScriptsDbfsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksClusterClusterInfoInitScriptsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsList",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoInitScriptsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDatabricksClusterClusterInfoInitScriptsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoInitScriptsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataDatabricksClusterClusterInfoInitScriptsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoInitScriptsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoInitScriptsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoInitScriptsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDatabricksClusterClusterInfoInitScripts]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDatabricksClusterClusterInfoInitScripts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDatabricksClusterClusterInfoInitScripts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoInitScriptsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksClusterClusterInfoInitScriptsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoInitScriptsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDbfs")
    def put_dbfs(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        '''
        value = DataDatabricksClusterClusterInfoInitScriptsDbfs(
            destination=destination
        )

        return typing.cast(None, jsii.invoke(self, "putDbfs", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        destination: builtins.str,
        canned_acl: typing.Optional[builtins.str] = None,
        enable_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#canned_acl DataDatabricksCluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_encryption DataDatabricksCluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#encryption_type DataDatabricksCluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#endpoint DataDatabricksCluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#kms_key DataDatabricksCluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#region DataDatabricksCluster#region}.
        '''
        value = DataDatabricksClusterClusterInfoInitScriptsS3(
            destination=destination,
            canned_acl=canned_acl,
            enable_encryption=enable_encryption,
            encryption_type=encryption_type,
            endpoint=endpoint,
            kms_key=kms_key,
            region=region,
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="resetDbfs")
    def reset_dbfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbfs", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @builtins.property
    @jsii.member(jsii_name="dbfs")
    def dbfs(self) -> DataDatabricksClusterClusterInfoInitScriptsDbfsOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoInitScriptsDbfsOutputReference, jsii.get(self, "dbfs"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "DataDatabricksClusterClusterInfoInitScriptsS3OutputReference":
        return typing.cast("DataDatabricksClusterClusterInfoInitScriptsS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="dbfsInput")
    def dbfs_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoInitScriptsDbfs]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoInitScriptsDbfs], jsii.get(self, "dbfsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoInitScriptsS3"]:
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoInitScriptsS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataDatabricksClusterClusterInfoInitScripts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataDatabricksClusterClusterInfoInitScripts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoInitScripts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoInitScriptsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsS3",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "canned_acl": "cannedAcl",
        "enable_encryption": "enableEncryption",
        "encryption_type": "encryptionType",
        "endpoint": "endpoint",
        "kms_key": "kmsKey",
        "region": "region",
    },
)
class DataDatabricksClusterClusterInfoInitScriptsS3:
    def __init__(
        self,
        *,
        destination: builtins.str,
        canned_acl: typing.Optional[builtins.str] = None,
        enable_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#canned_acl DataDatabricksCluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_encryption DataDatabricksCluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#encryption_type DataDatabricksCluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#endpoint DataDatabricksCluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#kms_key DataDatabricksCluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#region DataDatabricksCluster#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoInitScriptsS3.__init__)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument canned_acl", value=canned_acl, expected_type=type_hints["canned_acl"])
            check_type(argname="argument enable_encryption", value=enable_encryption, expected_type=type_hints["enable_encryption"])
            check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
        }
        if canned_acl is not None:
            self._values["canned_acl"] = canned_acl
        if enable_encryption is not None:
            self._values["enable_encryption"] = enable_encryption
        if encryption_type is not None:
            self._values["encryption_type"] = encryption_type
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def canned_acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#canned_acl DataDatabricksCluster#canned_acl}.'''
        result = self._values.get("canned_acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_encryption DataDatabricksCluster#enable_encryption}.'''
        result = self._values.get("enable_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encryption_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#encryption_type DataDatabricksCluster#encryption_type}.'''
        result = self._values.get("encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#endpoint DataDatabricksCluster#endpoint}.'''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#kms_key DataDatabricksCluster#kms_key}.'''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#region DataDatabricksCluster#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoInitScriptsS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoInitScriptsS3OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsS3OutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoInitScriptsS3OutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCannedAcl")
    def reset_canned_acl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCannedAcl", []))

    @jsii.member(jsii_name="resetEnableEncryption")
    def reset_enable_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableEncryption", []))

    @jsii.member(jsii_name="resetEncryptionType")
    def reset_encryption_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionType", []))

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @jsii.member(jsii_name="resetKmsKey")
    def reset_kms_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKey", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @builtins.property
    @jsii.member(jsii_name="cannedAclInput")
    def canned_acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cannedAclInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="enableEncryptionInput")
    def enable_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionTypeInput")
    def encryption_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyInput")
    def kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="cannedAcl")
    def canned_acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cannedAcl"))

    @canned_acl.setter
    def canned_acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoInitScriptsS3OutputReference, "canned_acl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cannedAcl", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoInitScriptsS3OutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="enableEncryption")
    def enable_encryption(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableEncryption"))

    @enable_encryption.setter
    def enable_encryption(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoInitScriptsS3OutputReference, "enable_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoInitScriptsS3OutputReference, "encryption_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoInitScriptsS3OutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoInitScriptsS3OutputReference, "kms_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoInitScriptsS3OutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoInitScriptsS3]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoInitScriptsS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoInitScriptsS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoInitScriptsS3OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksClusterClusterInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutoscale")
    def put_autoscale(
        self,
        *,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#max_workers DataDatabricksCluster#max_workers}.
        :param min_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#min_workers DataDatabricksCluster#min_workers}.
        '''
        value = DataDatabricksClusterClusterInfoAutoscale(
            max_workers=max_workers, min_workers=min_workers
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscale", [value]))

    @jsii.member(jsii_name="putAwsAttributes")
    def put_aws_attributes(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        ebs_volume_count: typing.Optional[jsii.Number] = None,
        ebs_volume_size: typing.Optional[jsii.Number] = None,
        ebs_volume_type: typing.Optional[builtins.str] = None,
        first_on_demand: typing.Optional[jsii.Number] = None,
        instance_profile_arn: typing.Optional[builtins.str] = None,
        spot_bid_price_percent: typing.Optional[jsii.Number] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.
        :param ebs_volume_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_count DataDatabricksCluster#ebs_volume_count}.
        :param ebs_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_size DataDatabricksCluster#ebs_volume_size}.
        :param ebs_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_type DataDatabricksCluster#ebs_volume_type}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#first_on_demand DataDatabricksCluster#first_on_demand}.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_profile_arn DataDatabricksCluster#instance_profile_arn}.
        :param spot_bid_price_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spot_bid_price_percent DataDatabricksCluster#spot_bid_price_percent}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#zone_id DataDatabricksCluster#zone_id}.
        '''
        value = DataDatabricksClusterClusterInfoAwsAttributes(
            availability=availability,
            ebs_volume_count=ebs_volume_count,
            ebs_volume_size=ebs_volume_size,
            ebs_volume_type=ebs_volume_type,
            first_on_demand=first_on_demand,
            instance_profile_arn=instance_profile_arn,
            spot_bid_price_percent=spot_bid_price_percent,
            zone_id=zone_id,
        )

        return typing.cast(None, jsii.invoke(self, "putAwsAttributes", [value]))

    @jsii.member(jsii_name="putAzureAttributes")
    def put_azure_attributes(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        first_on_demand: typing.Optional[jsii.Number] = None,
        spot_bid_max_price: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#first_on_demand DataDatabricksCluster#first_on_demand}.
        :param spot_bid_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spot_bid_max_price DataDatabricksCluster#spot_bid_max_price}.
        '''
        value = DataDatabricksClusterClusterInfoAzureAttributes(
            availability=availability,
            first_on_demand=first_on_demand,
            spot_bid_max_price=spot_bid_max_price,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureAttributes", [value]))

    @jsii.member(jsii_name="putClusterLogConf")
    def put_cluster_log_conf(
        self,
        *,
        dbfs: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoClusterLogConfDbfs, typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoClusterLogConfS3, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dbfs: dbfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#dbfs DataDatabricksCluster#dbfs}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#s3 DataDatabricksCluster#s3}
        '''
        value = DataDatabricksClusterClusterInfoClusterLogConf(dbfs=dbfs, s3=s3)

        return typing.cast(None, jsii.invoke(self, "putClusterLogConf", [value]))

    @jsii.member(jsii_name="putClusterLogStatus")
    def put_cluster_log_status(
        self,
        *,
        last_attempted: typing.Optional[jsii.Number] = None,
        last_exception: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param last_attempted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_attempted DataDatabricksCluster#last_attempted}.
        :param last_exception: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_exception DataDatabricksCluster#last_exception}.
        '''
        value = DataDatabricksClusterClusterInfoClusterLogStatus(
            last_attempted=last_attempted, last_exception=last_exception
        )

        return typing.cast(None, jsii.invoke(self, "putClusterLogStatus", [value]))

    @jsii.member(jsii_name="putDockerImage")
    def put_docker_image(
        self,
        *,
        url: builtins.str,
        basic_auth: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoDockerImageBasicAuth, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#url DataDatabricksCluster#url}.
        :param basic_auth: basic_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#basic_auth DataDatabricksCluster#basic_auth}
        '''
        value = DataDatabricksClusterClusterInfoDockerImage(
            url=url, basic_auth=basic_auth
        )

        return typing.cast(None, jsii.invoke(self, "putDockerImage", [value]))

    @jsii.member(jsii_name="putDriver")
    def put_driver(
        self,
        *,
        host_private_ip: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
        node_aws_attributes: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoDriverNodeAwsAttributes, typing.Dict[str, typing.Any]]] = None,
        node_id: typing.Optional[builtins.str] = None,
        private_ip: typing.Optional[builtins.str] = None,
        public_dns: typing.Optional[builtins.str] = None,
        start_timestamp: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param host_private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#host_private_ip DataDatabricksCluster#host_private_ip}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_id DataDatabricksCluster#instance_id}.
        :param node_aws_attributes: node_aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_aws_attributes DataDatabricksCluster#node_aws_attributes}
        :param node_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_id DataDatabricksCluster#node_id}.
        :param private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#private_ip DataDatabricksCluster#private_ip}.
        :param public_dns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#public_dns DataDatabricksCluster#public_dns}.
        :param start_timestamp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_timestamp DataDatabricksCluster#start_timestamp}.
        '''
        value = DataDatabricksClusterClusterInfoDriver(
            host_private_ip=host_private_ip,
            instance_id=instance_id,
            node_aws_attributes=node_aws_attributes,
            node_id=node_id,
            private_ip=private_ip,
            public_dns=public_dns,
            start_timestamp=start_timestamp,
        )

        return typing.cast(None, jsii.invoke(self, "putDriver", [value]))

    @jsii.member(jsii_name="putExecutors")
    def put_executors(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataDatabricksClusterClusterInfoExecutors, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoOutputReference.put_executors)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExecutors", [value]))

    @jsii.member(jsii_name="putGcpAttributes")
    def put_gcp_attributes(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        boot_disk_size: typing.Optional[jsii.Number] = None,
        google_service_account: typing.Optional[builtins.str] = None,
        use_preemptible_executors: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.
        :param boot_disk_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#boot_disk_size DataDatabricksCluster#boot_disk_size}.
        :param google_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#google_service_account DataDatabricksCluster#google_service_account}.
        :param use_preemptible_executors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#use_preemptible_executors DataDatabricksCluster#use_preemptible_executors}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#zone_id DataDatabricksCluster#zone_id}.
        '''
        value = DataDatabricksClusterClusterInfoGcpAttributes(
            availability=availability,
            boot_disk_size=boot_disk_size,
            google_service_account=google_service_account,
            use_preemptible_executors=use_preemptible_executors,
            zone_id=zone_id,
        )

        return typing.cast(None, jsii.invoke(self, "putGcpAttributes", [value]))

    @jsii.member(jsii_name="putInitScripts")
    def put_init_scripts(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataDatabricksClusterClusterInfoInitScripts, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoOutputReference.put_init_scripts)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInitScripts", [value]))

    @jsii.member(jsii_name="putTerminationReason")
    def put_termination_reason(
        self,
        *,
        code: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#code DataDatabricksCluster#code}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#parameters DataDatabricksCluster#parameters}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#type DataDatabricksCluster#type}.
        '''
        value = DataDatabricksClusterClusterInfoTerminationReason(
            code=code, parameters=parameters, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putTerminationReason", [value]))

    @jsii.member(jsii_name="resetAutoscale")
    def reset_autoscale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscale", []))

    @jsii.member(jsii_name="resetAutoterminationMinutes")
    def reset_autotermination_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoterminationMinutes", []))

    @jsii.member(jsii_name="resetAwsAttributes")
    def reset_aws_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsAttributes", []))

    @jsii.member(jsii_name="resetAzureAttributes")
    def reset_azure_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureAttributes", []))

    @jsii.member(jsii_name="resetClusterCores")
    def reset_cluster_cores(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterCores", []))

    @jsii.member(jsii_name="resetClusterId")
    def reset_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterId", []))

    @jsii.member(jsii_name="resetClusterLogConf")
    def reset_cluster_log_conf(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterLogConf", []))

    @jsii.member(jsii_name="resetClusterLogStatus")
    def reset_cluster_log_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterLogStatus", []))

    @jsii.member(jsii_name="resetClusterMemoryMb")
    def reset_cluster_memory_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterMemoryMb", []))

    @jsii.member(jsii_name="resetClusterName")
    def reset_cluster_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterName", []))

    @jsii.member(jsii_name="resetClusterSource")
    def reset_cluster_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterSource", []))

    @jsii.member(jsii_name="resetCreatorUserName")
    def reset_creator_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatorUserName", []))

    @jsii.member(jsii_name="resetCustomTags")
    def reset_custom_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomTags", []))

    @jsii.member(jsii_name="resetDataSecurityMode")
    def reset_data_security_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataSecurityMode", []))

    @jsii.member(jsii_name="resetDockerImage")
    def reset_docker_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerImage", []))

    @jsii.member(jsii_name="resetDriver")
    def reset_driver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriver", []))

    @jsii.member(jsii_name="resetDriverInstancePoolId")
    def reset_driver_instance_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverInstancePoolId", []))

    @jsii.member(jsii_name="resetDriverNodeTypeId")
    def reset_driver_node_type_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverNodeTypeId", []))

    @jsii.member(jsii_name="resetEnableElasticDisk")
    def reset_enable_elastic_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableElasticDisk", []))

    @jsii.member(jsii_name="resetEnableLocalDiskEncryption")
    def reset_enable_local_disk_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableLocalDiskEncryption", []))

    @jsii.member(jsii_name="resetExecutors")
    def reset_executors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutors", []))

    @jsii.member(jsii_name="resetGcpAttributes")
    def reset_gcp_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpAttributes", []))

    @jsii.member(jsii_name="resetInitScripts")
    def reset_init_scripts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitScripts", []))

    @jsii.member(jsii_name="resetInstancePoolId")
    def reset_instance_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePoolId", []))

    @jsii.member(jsii_name="resetJdbcPort")
    def reset_jdbc_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJdbcPort", []))

    @jsii.member(jsii_name="resetLastActivityTime")
    def reset_last_activity_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastActivityTime", []))

    @jsii.member(jsii_name="resetLastStateLossTime")
    def reset_last_state_loss_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastStateLossTime", []))

    @jsii.member(jsii_name="resetNodeTypeId")
    def reset_node_type_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeTypeId", []))

    @jsii.member(jsii_name="resetNumWorkers")
    def reset_num_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumWorkers", []))

    @jsii.member(jsii_name="resetPolicyId")
    def reset_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyId", []))

    @jsii.member(jsii_name="resetSingleUserName")
    def reset_single_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleUserName", []))

    @jsii.member(jsii_name="resetSparkConf")
    def reset_spark_conf(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkConf", []))

    @jsii.member(jsii_name="resetSparkContextId")
    def reset_spark_context_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkContextId", []))

    @jsii.member(jsii_name="resetSparkEnvVars")
    def reset_spark_env_vars(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkEnvVars", []))

    @jsii.member(jsii_name="resetSshPublicKeys")
    def reset_ssh_public_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshPublicKeys", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @jsii.member(jsii_name="resetStateMessage")
    def reset_state_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStateMessage", []))

    @jsii.member(jsii_name="resetTerminateTime")
    def reset_terminate_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminateTime", []))

    @jsii.member(jsii_name="resetTerminationReason")
    def reset_termination_reason(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminationReason", []))

    @builtins.property
    @jsii.member(jsii_name="autoscale")
    def autoscale(self) -> DataDatabricksClusterClusterInfoAutoscaleOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoAutoscaleOutputReference, jsii.get(self, "autoscale"))

    @builtins.property
    @jsii.member(jsii_name="awsAttributes")
    def aws_attributes(
        self,
    ) -> DataDatabricksClusterClusterInfoAwsAttributesOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoAwsAttributesOutputReference, jsii.get(self, "awsAttributes"))

    @builtins.property
    @jsii.member(jsii_name="azureAttributes")
    def azure_attributes(
        self,
    ) -> DataDatabricksClusterClusterInfoAzureAttributesOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoAzureAttributesOutputReference, jsii.get(self, "azureAttributes"))

    @builtins.property
    @jsii.member(jsii_name="clusterLogConf")
    def cluster_log_conf(
        self,
    ) -> DataDatabricksClusterClusterInfoClusterLogConfOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoClusterLogConfOutputReference, jsii.get(self, "clusterLogConf"))

    @builtins.property
    @jsii.member(jsii_name="clusterLogStatus")
    def cluster_log_status(
        self,
    ) -> DataDatabricksClusterClusterInfoClusterLogStatusOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoClusterLogStatusOutputReference, jsii.get(self, "clusterLogStatus"))

    @builtins.property
    @jsii.member(jsii_name="dockerImage")
    def docker_image(
        self,
    ) -> DataDatabricksClusterClusterInfoDockerImageOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoDockerImageOutputReference, jsii.get(self, "dockerImage"))

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> DataDatabricksClusterClusterInfoDriverOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoDriverOutputReference, jsii.get(self, "driver"))

    @builtins.property
    @jsii.member(jsii_name="executors")
    def executors(self) -> DataDatabricksClusterClusterInfoExecutorsList:
        return typing.cast(DataDatabricksClusterClusterInfoExecutorsList, jsii.get(self, "executors"))

    @builtins.property
    @jsii.member(jsii_name="gcpAttributes")
    def gcp_attributes(
        self,
    ) -> DataDatabricksClusterClusterInfoGcpAttributesOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoGcpAttributesOutputReference, jsii.get(self, "gcpAttributes"))

    @builtins.property
    @jsii.member(jsii_name="initScripts")
    def init_scripts(self) -> DataDatabricksClusterClusterInfoInitScriptsList:
        return typing.cast(DataDatabricksClusterClusterInfoInitScriptsList, jsii.get(self, "initScripts"))

    @builtins.property
    @jsii.member(jsii_name="terminationReason")
    def termination_reason(
        self,
    ) -> "DataDatabricksClusterClusterInfoTerminationReasonOutputReference":
        return typing.cast("DataDatabricksClusterClusterInfoTerminationReasonOutputReference", jsii.get(self, "terminationReason"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleInput")
    def autoscale_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoAutoscale]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoAutoscale], jsii.get(self, "autoscaleInput"))

    @builtins.property
    @jsii.member(jsii_name="autoterminationMinutesInput")
    def autotermination_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autoterminationMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="awsAttributesInput")
    def aws_attributes_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoAwsAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoAwsAttributes], jsii.get(self, "awsAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="azureAttributesInput")
    def azure_attributes_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoAzureAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoAzureAttributes], jsii.get(self, "azureAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterCoresInput")
    def cluster_cores_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "clusterCoresInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterLogConfInput")
    def cluster_log_conf_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoClusterLogConf]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoClusterLogConf], jsii.get(self, "clusterLogConfInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterLogStatusInput")
    def cluster_log_status_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoClusterLogStatus]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoClusterLogStatus], jsii.get(self, "clusterLogStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterMemoryMbInput")
    def cluster_memory_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "clusterMemoryMbInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterSourceInput")
    def cluster_source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="creatorUserNameInput")
    def creator_user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "creatorUserNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customTagsInput")
    def custom_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSecurityModeInput")
    def data_security_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSecurityModeInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTagsInput")
    def default_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "defaultTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerImageInput")
    def docker_image_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoDockerImage]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDockerImage], jsii.get(self, "dockerImageInput"))

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[DataDatabricksClusterClusterInfoDriver]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDriver], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="driverInstancePoolIdInput")
    def driver_instance_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInstancePoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="driverNodeTypeIdInput")
    def driver_node_type_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverNodeTypeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="enableElasticDiskInput")
    def enable_elastic_disk_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableElasticDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="enableLocalDiskEncryptionInput")
    def enable_local_disk_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableLocalDiskEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="executorsInput")
    def executors_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDatabricksClusterClusterInfoExecutors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDatabricksClusterClusterInfoExecutors]]], jsii.get(self, "executorsInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpAttributesInput")
    def gcp_attributes_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoGcpAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoGcpAttributes], jsii.get(self, "gcpAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="initScriptsInput")
    def init_scripts_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDatabricksClusterClusterInfoInitScripts]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDatabricksClusterClusterInfoInitScripts]]], jsii.get(self, "initScriptsInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolIdInput")
    def instance_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instancePoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="jdbcPortInput")
    def jdbc_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "jdbcPortInput"))

    @builtins.property
    @jsii.member(jsii_name="lastActivityTimeInput")
    def last_activity_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lastActivityTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="lastStateLossTimeInput")
    def last_state_loss_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lastStateLossTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeTypeIdInput")
    def node_type_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeTypeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="numWorkersInput")
    def num_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="policyIdInput")
    def policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="singleUserNameInput")
    def single_user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "singleUserNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkConfInput")
    def spark_conf_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sparkConfInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkContextIdInput")
    def spark_context_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sparkContextIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkEnvVarsInput")
    def spark_env_vars_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sparkEnvVarsInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkVersionInput")
    def spark_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sparkVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeysInput")
    def ssh_public_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshPublicKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="stateMessageInput")
    def state_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="terminateTimeInput")
    def terminate_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "terminateTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="terminationReasonInput")
    def termination_reason_input(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoTerminationReason"]:
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoTerminationReason"], jsii.get(self, "terminationReasonInput"))

    @builtins.property
    @jsii.member(jsii_name="autoterminationMinutes")
    def autotermination_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autoterminationMinutes"))

    @autotermination_minutes.setter
    def autotermination_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "autotermination_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoterminationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="clusterCores")
    def cluster_cores(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "clusterCores"))

    @cluster_cores.setter
    def cluster_cores(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "cluster_cores").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterCores", value)

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="clusterMemoryMb")
    def cluster_memory_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "clusterMemoryMb"))

    @cluster_memory_mb.setter
    def cluster_memory_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "cluster_memory_mb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterMemoryMb", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "cluster_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="clusterSource")
    def cluster_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterSource"))

    @cluster_source.setter
    def cluster_source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "cluster_source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterSource", value)

    @builtins.property
    @jsii.member(jsii_name="creatorUserName")
    def creator_user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creatorUserName"))

    @creator_user_name.setter
    def creator_user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "creator_user_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creatorUserName", value)

    @builtins.property
    @jsii.member(jsii_name="customTags")
    def custom_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customTags"))

    @custom_tags.setter
    def custom_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "custom_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customTags", value)

    @builtins.property
    @jsii.member(jsii_name="dataSecurityMode")
    def data_security_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSecurityMode"))

    @data_security_mode.setter
    def data_security_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "data_security_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSecurityMode", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTags")
    def default_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "defaultTags"))

    @default_tags.setter
    def default_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "default_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTags", value)

    @builtins.property
    @jsii.member(jsii_name="driverInstancePoolId")
    def driver_instance_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driverInstancePoolId"))

    @driver_instance_pool_id.setter
    def driver_instance_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "driver_instance_pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverInstancePoolId", value)

    @builtins.property
    @jsii.member(jsii_name="driverNodeTypeId")
    def driver_node_type_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driverNodeTypeId"))

    @driver_node_type_id.setter
    def driver_node_type_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "driver_node_type_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverNodeTypeId", value)

    @builtins.property
    @jsii.member(jsii_name="enableElasticDisk")
    def enable_elastic_disk(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableElasticDisk"))

    @enable_elastic_disk.setter
    def enable_elastic_disk(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "enable_elastic_disk").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableElasticDisk", value)

    @builtins.property
    @jsii.member(jsii_name="enableLocalDiskEncryption")
    def enable_local_disk_encryption(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableLocalDiskEncryption"))

    @enable_local_disk_encryption.setter
    def enable_local_disk_encryption(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "enable_local_disk_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLocalDiskEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="instancePoolId")
    def instance_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instancePoolId"))

    @instance_pool_id.setter
    def instance_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "instance_pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePoolId", value)

    @builtins.property
    @jsii.member(jsii_name="jdbcPort")
    def jdbc_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "jdbcPort"))

    @jdbc_port.setter
    def jdbc_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "jdbc_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jdbcPort", value)

    @builtins.property
    @jsii.member(jsii_name="lastActivityTime")
    def last_activity_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lastActivityTime"))

    @last_activity_time.setter
    def last_activity_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "last_activity_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastActivityTime", value)

    @builtins.property
    @jsii.member(jsii_name="lastStateLossTime")
    def last_state_loss_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lastStateLossTime"))

    @last_state_loss_time.setter
    def last_state_loss_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "last_state_loss_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastStateLossTime", value)

    @builtins.property
    @jsii.member(jsii_name="nodeTypeId")
    def node_type_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeTypeId"))

    @node_type_id.setter
    def node_type_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "node_type_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeTypeId", value)

    @builtins.property
    @jsii.member(jsii_name="numWorkers")
    def num_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numWorkers"))

    @num_workers.setter
    def num_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "num_workers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyId"))

    @policy_id.setter
    def policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyId", value)

    @builtins.property
    @jsii.member(jsii_name="singleUserName")
    def single_user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "singleUserName"))

    @single_user_name.setter
    def single_user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "single_user_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singleUserName", value)

    @builtins.property
    @jsii.member(jsii_name="sparkConf")
    def spark_conf(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sparkConf"))

    @spark_conf.setter
    def spark_conf(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "spark_conf").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkConf", value)

    @builtins.property
    @jsii.member(jsii_name="sparkContextId")
    def spark_context_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sparkContextId"))

    @spark_context_id.setter
    def spark_context_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "spark_context_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkContextId", value)

    @builtins.property
    @jsii.member(jsii_name="sparkEnvVars")
    def spark_env_vars(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sparkEnvVars"))

    @spark_env_vars.setter
    def spark_env_vars(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "spark_env_vars").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkEnvVars", value)

    @builtins.property
    @jsii.member(jsii_name="sparkVersion")
    def spark_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sparkVersion"))

    @spark_version.setter
    def spark_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "spark_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkVersion", value)

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeys")
    def ssh_public_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sshPublicKeys"))

    @ssh_public_keys.setter
    def ssh_public_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "ssh_public_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicKeys", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="stateMessage")
    def state_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateMessage"))

    @state_message.setter
    def state_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "state_message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateMessage", value)

    @builtins.property
    @jsii.member(jsii_name="terminateTime")
    def terminate_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "terminateTime"))

    @terminate_time.setter
    def terminate_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "terminate_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminateTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataDatabricksClusterClusterInfo]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoTerminationReason",
    jsii_struct_bases=[],
    name_mapping={"code": "code", "parameters": "parameters", "type": "type"},
)
class DataDatabricksClusterClusterInfoTerminationReason:
    def __init__(
        self,
        *,
        code: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#code DataDatabricksCluster#code}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#parameters DataDatabricksCluster#parameters}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#type DataDatabricksCluster#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoTerminationReason.__init__)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if code is not None:
            self._values["code"] = code
        if parameters is not None:
            self._values["parameters"] = parameters
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#code DataDatabricksCluster#code}.'''
        result = self._values.get("code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#parameters DataDatabricksCluster#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#type DataDatabricksCluster#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoTerminationReason(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoTerminationReasonOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoTerminationReasonOutputReference",
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
            type_hints = typing.get_type_hints(DataDatabricksClusterClusterInfoTerminationReasonOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCode")
    def reset_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCode", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="codeInput")
    def code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "code"))

    @code.setter
    def code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoTerminationReasonOutputReference, "code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoTerminationReasonOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoTerminationReasonOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoTerminationReason]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoTerminationReason], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoTerminationReason],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksClusterClusterInfoTerminationReasonOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksCluster.DataDatabricksClusterConfig",
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
        "cluster_info": "clusterInfo",
        "id": "id",
    },
)
class DataDatabricksClusterConfig(cdktf.TerraformMetaArguments):
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
        cluster_info: typing.Optional[typing.Union[DataDatabricksClusterClusterInfo, typing.Dict[str, typing.Any]]] = None,
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
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_id DataDatabricksCluster#cluster_id}.
        :param cluster_info: cluster_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_info DataDatabricksCluster#cluster_info}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#id DataDatabricksCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cluster_info, dict):
            cluster_info = DataDatabricksClusterClusterInfo(**cluster_info)
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument cluster_info", value=cluster_info, expected_type=type_hints["cluster_info"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
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
        if cluster_info is not None:
            self._values["cluster_info"] = cluster_info
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
    def cluster_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_id DataDatabricksCluster#cluster_id}.'''
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_info(self) -> typing.Optional[DataDatabricksClusterClusterInfo]:
        '''cluster_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_info DataDatabricksCluster#cluster_info}
        '''
        result = self._values.get("cluster_info")
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfo], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#id DataDatabricksCluster#id}.

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
        return "DataDatabricksClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataDatabricksCluster",
    "DataDatabricksClusterClusterInfo",
    "DataDatabricksClusterClusterInfoAutoscale",
    "DataDatabricksClusterClusterInfoAutoscaleOutputReference",
    "DataDatabricksClusterClusterInfoAwsAttributes",
    "DataDatabricksClusterClusterInfoAwsAttributesOutputReference",
    "DataDatabricksClusterClusterInfoAzureAttributes",
    "DataDatabricksClusterClusterInfoAzureAttributesOutputReference",
    "DataDatabricksClusterClusterInfoClusterLogConf",
    "DataDatabricksClusterClusterInfoClusterLogConfDbfs",
    "DataDatabricksClusterClusterInfoClusterLogConfDbfsOutputReference",
    "DataDatabricksClusterClusterInfoClusterLogConfOutputReference",
    "DataDatabricksClusterClusterInfoClusterLogConfS3",
    "DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference",
    "DataDatabricksClusterClusterInfoClusterLogStatus",
    "DataDatabricksClusterClusterInfoClusterLogStatusOutputReference",
    "DataDatabricksClusterClusterInfoDockerImage",
    "DataDatabricksClusterClusterInfoDockerImageBasicAuth",
    "DataDatabricksClusterClusterInfoDockerImageBasicAuthOutputReference",
    "DataDatabricksClusterClusterInfoDockerImageOutputReference",
    "DataDatabricksClusterClusterInfoDriver",
    "DataDatabricksClusterClusterInfoDriverNodeAwsAttributes",
    "DataDatabricksClusterClusterInfoDriverNodeAwsAttributesOutputReference",
    "DataDatabricksClusterClusterInfoDriverOutputReference",
    "DataDatabricksClusterClusterInfoExecutors",
    "DataDatabricksClusterClusterInfoExecutorsList",
    "DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes",
    "DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributesOutputReference",
    "DataDatabricksClusterClusterInfoExecutorsOutputReference",
    "DataDatabricksClusterClusterInfoGcpAttributes",
    "DataDatabricksClusterClusterInfoGcpAttributesOutputReference",
    "DataDatabricksClusterClusterInfoInitScripts",
    "DataDatabricksClusterClusterInfoInitScriptsDbfs",
    "DataDatabricksClusterClusterInfoInitScriptsDbfsOutputReference",
    "DataDatabricksClusterClusterInfoInitScriptsList",
    "DataDatabricksClusterClusterInfoInitScriptsOutputReference",
    "DataDatabricksClusterClusterInfoInitScriptsS3",
    "DataDatabricksClusterClusterInfoInitScriptsS3OutputReference",
    "DataDatabricksClusterClusterInfoOutputReference",
    "DataDatabricksClusterClusterInfoTerminationReason",
    "DataDatabricksClusterClusterInfoTerminationReasonOutputReference",
    "DataDatabricksClusterConfig",
]

publication.publish()
