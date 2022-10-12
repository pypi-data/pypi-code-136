'''
# `databricks_cluster`

Refer to the Terraform Registory for docs: [`databricks_cluster`](https://www.terraform.io/docs/providers/databricks/r/cluster).
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


class Cluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.Cluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/cluster databricks_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        spark_version: builtins.str,
        apply_policy_default_values: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autoscale: typing.Optional[typing.Union["ClusterAutoscale", typing.Dict[str, typing.Any]]] = None,
        autotermination_minutes: typing.Optional[jsii.Number] = None,
        aws_attributes: typing.Optional[typing.Union["ClusterAwsAttributes", typing.Dict[str, typing.Any]]] = None,
        azure_attributes: typing.Optional[typing.Union["ClusterAzureAttributes", typing.Dict[str, typing.Any]]] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        cluster_log_conf: typing.Optional[typing.Union["ClusterClusterLogConf", typing.Dict[str, typing.Any]]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        data_security_mode: typing.Optional[builtins.str] = None,
        docker_image: typing.Optional[typing.Union["ClusterDockerImage", typing.Dict[str, typing.Any]]] = None,
        driver_instance_pool_id: typing.Optional[builtins.str] = None,
        driver_node_type_id: typing.Optional[builtins.str] = None,
        enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_local_disk_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        gcp_attributes: typing.Optional[typing.Union["ClusterGcpAttributes", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        idempotency_token: typing.Optional[builtins.str] = None,
        init_scripts: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ClusterInitScripts", typing.Dict[str, typing.Any]]]]] = None,
        instance_pool_id: typing.Optional[builtins.str] = None,
        is_pinned: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        library: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ClusterLibrary", typing.Dict[str, typing.Any]]]]] = None,
        node_type_id: typing.Optional[builtins.str] = None,
        num_workers: typing.Optional[jsii.Number] = None,
        policy_id: typing.Optional[builtins.str] = None,
        single_user_name: typing.Optional[builtins.str] = None,
        spark_conf: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        spark_env_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        workload_type: typing.Optional[typing.Union["ClusterWorkloadType", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/cluster databricks_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param spark_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_version Cluster#spark_version}.
        :param apply_policy_default_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#apply_policy_default_values Cluster#apply_policy_default_values}.
        :param autoscale: autoscale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#autoscale Cluster#autoscale}
        :param autotermination_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#autotermination_minutes Cluster#autotermination_minutes}.
        :param aws_attributes: aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#aws_attributes Cluster#aws_attributes}
        :param azure_attributes: azure_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#azure_attributes Cluster#azure_attributes}
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_id Cluster#cluster_id}.
        :param cluster_log_conf: cluster_log_conf block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_log_conf Cluster#cluster_log_conf}
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_name Cluster#cluster_name}.
        :param custom_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#custom_tags Cluster#custom_tags}.
        :param data_security_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#data_security_mode Cluster#data_security_mode}.
        :param docker_image: docker_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#docker_image Cluster#docker_image}
        :param driver_instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#driver_instance_pool_id Cluster#driver_instance_pool_id}.
        :param driver_node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#driver_node_type_id Cluster#driver_node_type_id}.
        :param enable_elastic_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_elastic_disk Cluster#enable_elastic_disk}.
        :param enable_local_disk_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_local_disk_encryption Cluster#enable_local_disk_encryption}.
        :param gcp_attributes: gcp_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#gcp_attributes Cluster#gcp_attributes}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#id Cluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idempotency_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#idempotency_token Cluster#idempotency_token}.
        :param init_scripts: init_scripts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#init_scripts Cluster#init_scripts}
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#instance_pool_id Cluster#instance_pool_id}.
        :param is_pinned: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#is_pinned Cluster#is_pinned}.
        :param library: library block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#library Cluster#library}
        :param node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#node_type_id Cluster#node_type_id}.
        :param num_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#num_workers Cluster#num_workers}.
        :param policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#policy_id Cluster#policy_id}.
        :param single_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#single_user_name Cluster#single_user_name}.
        :param spark_conf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_conf Cluster#spark_conf}.
        :param spark_env_vars: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_env_vars Cluster#spark_env_vars}.
        :param ssh_public_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ssh_public_keys Cluster#ssh_public_keys}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#timeouts Cluster#timeouts}
        :param workload_type: workload_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#workload_type Cluster#workload_type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Cluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ClusterConfig(
            spark_version=spark_version,
            apply_policy_default_values=apply_policy_default_values,
            autoscale=autoscale,
            autotermination_minutes=autotermination_minutes,
            aws_attributes=aws_attributes,
            azure_attributes=azure_attributes,
            cluster_id=cluster_id,
            cluster_log_conf=cluster_log_conf,
            cluster_name=cluster_name,
            custom_tags=custom_tags,
            data_security_mode=data_security_mode,
            docker_image=docker_image,
            driver_instance_pool_id=driver_instance_pool_id,
            driver_node_type_id=driver_node_type_id,
            enable_elastic_disk=enable_elastic_disk,
            enable_local_disk_encryption=enable_local_disk_encryption,
            gcp_attributes=gcp_attributes,
            id=id,
            idempotency_token=idempotency_token,
            init_scripts=init_scripts,
            instance_pool_id=instance_pool_id,
            is_pinned=is_pinned,
            library=library,
            node_type_id=node_type_id,
            num_workers=num_workers,
            policy_id=policy_id,
            single_user_name=single_user_name,
            spark_conf=spark_conf,
            spark_env_vars=spark_env_vars,
            ssh_public_keys=ssh_public_keys,
            timeouts=timeouts,
            workload_type=workload_type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAutoscale")
    def put_autoscale(
        self,
        *,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#max_workers Cluster#max_workers}.
        :param min_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#min_workers Cluster#min_workers}.
        '''
        value = ClusterAutoscale(max_workers=max_workers, min_workers=min_workers)

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
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.
        :param ebs_volume_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_count Cluster#ebs_volume_count}.
        :param ebs_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_size Cluster#ebs_volume_size}.
        :param ebs_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_type Cluster#ebs_volume_type}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#first_on_demand Cluster#first_on_demand}.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#instance_profile_arn Cluster#instance_profile_arn}.
        :param spot_bid_price_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spot_bid_price_percent Cluster#spot_bid_price_percent}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#zone_id Cluster#zone_id}.
        '''
        value = ClusterAwsAttributes(
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
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#first_on_demand Cluster#first_on_demand}.
        :param spot_bid_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spot_bid_max_price Cluster#spot_bid_max_price}.
        '''
        value = ClusterAzureAttributes(
            availability=availability,
            first_on_demand=first_on_demand,
            spot_bid_max_price=spot_bid_max_price,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureAttributes", [value]))

    @jsii.member(jsii_name="putClusterLogConf")
    def put_cluster_log_conf(
        self,
        *,
        dbfs: typing.Optional[typing.Union["ClusterClusterLogConfDbfs", typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["ClusterClusterLogConfS3", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dbfs: dbfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#dbfs Cluster#dbfs}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#s3 Cluster#s3}
        '''
        value = ClusterClusterLogConf(dbfs=dbfs, s3=s3)

        return typing.cast(None, jsii.invoke(self, "putClusterLogConf", [value]))

    @jsii.member(jsii_name="putDockerImage")
    def put_docker_image(
        self,
        *,
        url: builtins.str,
        basic_auth: typing.Optional[typing.Union["ClusterDockerImageBasicAuth", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#url Cluster#url}.
        :param basic_auth: basic_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#basic_auth Cluster#basic_auth}
        '''
        value = ClusterDockerImage(url=url, basic_auth=basic_auth)

        return typing.cast(None, jsii.invoke(self, "putDockerImage", [value]))

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
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.
        :param boot_disk_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#boot_disk_size Cluster#boot_disk_size}.
        :param google_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#google_service_account Cluster#google_service_account}.
        :param use_preemptible_executors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#use_preemptible_executors Cluster#use_preemptible_executors}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#zone_id Cluster#zone_id}.
        '''
        value = ClusterGcpAttributes(
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
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ClusterInitScripts", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Cluster.put_init_scripts)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInitScripts", [value]))

    @jsii.member(jsii_name="putLibrary")
    def put_library(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ClusterLibrary", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Cluster.put_library)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLibrary", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#create Cluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#delete Cluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#update Cluster#update}.
        '''
        value = ClusterTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWorkloadType")
    def put_workload_type(
        self,
        *,
        clients: typing.Union["ClusterWorkloadTypeClients", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param clients: clients block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#clients Cluster#clients}
        '''
        value = ClusterWorkloadType(clients=clients)

        return typing.cast(None, jsii.invoke(self, "putWorkloadType", [value]))

    @jsii.member(jsii_name="resetApplyPolicyDefaultValues")
    def reset_apply_policy_default_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplyPolicyDefaultValues", []))

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

    @jsii.member(jsii_name="resetClusterId")
    def reset_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterId", []))

    @jsii.member(jsii_name="resetClusterLogConf")
    def reset_cluster_log_conf(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterLogConf", []))

    @jsii.member(jsii_name="resetClusterName")
    def reset_cluster_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterName", []))

    @jsii.member(jsii_name="resetCustomTags")
    def reset_custom_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomTags", []))

    @jsii.member(jsii_name="resetDataSecurityMode")
    def reset_data_security_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataSecurityMode", []))

    @jsii.member(jsii_name="resetDockerImage")
    def reset_docker_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerImage", []))

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

    @jsii.member(jsii_name="resetGcpAttributes")
    def reset_gcp_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpAttributes", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdempotencyToken")
    def reset_idempotency_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdempotencyToken", []))

    @jsii.member(jsii_name="resetInitScripts")
    def reset_init_scripts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitScripts", []))

    @jsii.member(jsii_name="resetInstancePoolId")
    def reset_instance_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePoolId", []))

    @jsii.member(jsii_name="resetIsPinned")
    def reset_is_pinned(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsPinned", []))

    @jsii.member(jsii_name="resetLibrary")
    def reset_library(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLibrary", []))

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

    @jsii.member(jsii_name="resetSparkEnvVars")
    def reset_spark_env_vars(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkEnvVars", []))

    @jsii.member(jsii_name="resetSshPublicKeys")
    def reset_ssh_public_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshPublicKeys", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWorkloadType")
    def reset_workload_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkloadType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="autoscale")
    def autoscale(self) -> "ClusterAutoscaleOutputReference":
        return typing.cast("ClusterAutoscaleOutputReference", jsii.get(self, "autoscale"))

    @builtins.property
    @jsii.member(jsii_name="awsAttributes")
    def aws_attributes(self) -> "ClusterAwsAttributesOutputReference":
        return typing.cast("ClusterAwsAttributesOutputReference", jsii.get(self, "awsAttributes"))

    @builtins.property
    @jsii.member(jsii_name="azureAttributes")
    def azure_attributes(self) -> "ClusterAzureAttributesOutputReference":
        return typing.cast("ClusterAzureAttributesOutputReference", jsii.get(self, "azureAttributes"))

    @builtins.property
    @jsii.member(jsii_name="clusterLogConf")
    def cluster_log_conf(self) -> "ClusterClusterLogConfOutputReference":
        return typing.cast("ClusterClusterLogConfOutputReference", jsii.get(self, "clusterLogConf"))

    @builtins.property
    @jsii.member(jsii_name="defaultTags")
    def default_tags(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "defaultTags"))

    @builtins.property
    @jsii.member(jsii_name="dockerImage")
    def docker_image(self) -> "ClusterDockerImageOutputReference":
        return typing.cast("ClusterDockerImageOutputReference", jsii.get(self, "dockerImage"))

    @builtins.property
    @jsii.member(jsii_name="gcpAttributes")
    def gcp_attributes(self) -> "ClusterGcpAttributesOutputReference":
        return typing.cast("ClusterGcpAttributesOutputReference", jsii.get(self, "gcpAttributes"))

    @builtins.property
    @jsii.member(jsii_name="initScripts")
    def init_scripts(self) -> "ClusterInitScriptsList":
        return typing.cast("ClusterInitScriptsList", jsii.get(self, "initScripts"))

    @builtins.property
    @jsii.member(jsii_name="library")
    def library(self) -> "ClusterLibraryList":
        return typing.cast("ClusterLibraryList", jsii.get(self, "library"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ClusterTimeoutsOutputReference":
        return typing.cast("ClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="workloadType")
    def workload_type(self) -> "ClusterWorkloadTypeOutputReference":
        return typing.cast("ClusterWorkloadTypeOutputReference", jsii.get(self, "workloadType"))

    @builtins.property
    @jsii.member(jsii_name="applyPolicyDefaultValuesInput")
    def apply_policy_default_values_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "applyPolicyDefaultValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleInput")
    def autoscale_input(self) -> typing.Optional["ClusterAutoscale"]:
        return typing.cast(typing.Optional["ClusterAutoscale"], jsii.get(self, "autoscaleInput"))

    @builtins.property
    @jsii.member(jsii_name="autoterminationMinutesInput")
    def autotermination_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autoterminationMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="awsAttributesInput")
    def aws_attributes_input(self) -> typing.Optional["ClusterAwsAttributes"]:
        return typing.cast(typing.Optional["ClusterAwsAttributes"], jsii.get(self, "awsAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="azureAttributesInput")
    def azure_attributes_input(self) -> typing.Optional["ClusterAzureAttributes"]:
        return typing.cast(typing.Optional["ClusterAzureAttributes"], jsii.get(self, "azureAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterLogConfInput")
    def cluster_log_conf_input(self) -> typing.Optional["ClusterClusterLogConf"]:
        return typing.cast(typing.Optional["ClusterClusterLogConf"], jsii.get(self, "clusterLogConfInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

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
    @jsii.member(jsii_name="dockerImageInput")
    def docker_image_input(self) -> typing.Optional["ClusterDockerImage"]:
        return typing.cast(typing.Optional["ClusterDockerImage"], jsii.get(self, "dockerImageInput"))

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
    @jsii.member(jsii_name="gcpAttributesInput")
    def gcp_attributes_input(self) -> typing.Optional["ClusterGcpAttributes"]:
        return typing.cast(typing.Optional["ClusterGcpAttributes"], jsii.get(self, "gcpAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="idempotencyTokenInput")
    def idempotency_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idempotencyTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initScriptsInput")
    def init_scripts_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ClusterInitScripts"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ClusterInitScripts"]]], jsii.get(self, "initScriptsInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolIdInput")
    def instance_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instancePoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="isPinnedInput")
    def is_pinned_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isPinnedInput"))

    @builtins.property
    @jsii.member(jsii_name="libraryInput")
    def library_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ClusterLibrary"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ClusterLibrary"]]], jsii.get(self, "libraryInput"))

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
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadTypeInput")
    def workload_type_input(self) -> typing.Optional["ClusterWorkloadType"]:
        return typing.cast(typing.Optional["ClusterWorkloadType"], jsii.get(self, "workloadTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="applyPolicyDefaultValues")
    def apply_policy_default_values(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "applyPolicyDefaultValues"))

    @apply_policy_default_values.setter
    def apply_policy_default_values(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "apply_policy_default_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyPolicyDefaultValues", value)

    @builtins.property
    @jsii.member(jsii_name="autoterminationMinutes")
    def autotermination_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autoterminationMinutes"))

    @autotermination_minutes.setter
    def autotermination_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "autotermination_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoterminationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "cluster_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="customTags")
    def custom_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customTags"))

    @custom_tags.setter
    def custom_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "custom_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customTags", value)

    @builtins.property
    @jsii.member(jsii_name="dataSecurityMode")
    def data_security_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSecurityMode"))

    @data_security_mode.setter
    def data_security_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "data_security_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSecurityMode", value)

    @builtins.property
    @jsii.member(jsii_name="driverInstancePoolId")
    def driver_instance_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driverInstancePoolId"))

    @driver_instance_pool_id.setter
    def driver_instance_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "driver_instance_pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverInstancePoolId", value)

    @builtins.property
    @jsii.member(jsii_name="driverNodeTypeId")
    def driver_node_type_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driverNodeTypeId"))

    @driver_node_type_id.setter
    def driver_node_type_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "driver_node_type_id").fset)
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
            type_hints = typing.get_type_hints(getattr(Cluster, "enable_elastic_disk").fset)
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
            type_hints = typing.get_type_hints(getattr(Cluster, "enable_local_disk_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLocalDiskEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="idempotencyToken")
    def idempotency_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idempotencyToken"))

    @idempotency_token.setter
    def idempotency_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "idempotency_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idempotencyToken", value)

    @builtins.property
    @jsii.member(jsii_name="instancePoolId")
    def instance_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instancePoolId"))

    @instance_pool_id.setter
    def instance_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "instance_pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePoolId", value)

    @builtins.property
    @jsii.member(jsii_name="isPinned")
    def is_pinned(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isPinned"))

    @is_pinned.setter
    def is_pinned(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "is_pinned").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isPinned", value)

    @builtins.property
    @jsii.member(jsii_name="nodeTypeId")
    def node_type_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeTypeId"))

    @node_type_id.setter
    def node_type_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "node_type_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeTypeId", value)

    @builtins.property
    @jsii.member(jsii_name="numWorkers")
    def num_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numWorkers"))

    @num_workers.setter
    def num_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "num_workers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyId"))

    @policy_id.setter
    def policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyId", value)

    @builtins.property
    @jsii.member(jsii_name="singleUserName")
    def single_user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "singleUserName"))

    @single_user_name.setter
    def single_user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "single_user_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singleUserName", value)

    @builtins.property
    @jsii.member(jsii_name="sparkConf")
    def spark_conf(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sparkConf"))

    @spark_conf.setter
    def spark_conf(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "spark_conf").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkConf", value)

    @builtins.property
    @jsii.member(jsii_name="sparkEnvVars")
    def spark_env_vars(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sparkEnvVars"))

    @spark_env_vars.setter
    def spark_env_vars(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "spark_env_vars").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkEnvVars", value)

    @builtins.property
    @jsii.member(jsii_name="sparkVersion")
    def spark_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sparkVersion"))

    @spark_version.setter
    def spark_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "spark_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkVersion", value)

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeys")
    def ssh_public_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sshPublicKeys"))

    @ssh_public_keys.setter
    def ssh_public_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Cluster, "ssh_public_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicKeys", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterAutoscale",
    jsii_struct_bases=[],
    name_mapping={"max_workers": "maxWorkers", "min_workers": "minWorkers"},
)
class ClusterAutoscale:
    def __init__(
        self,
        *,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#max_workers Cluster#max_workers}.
        :param min_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#min_workers Cluster#min_workers}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterAutoscale.__init__)
            check_type(argname="argument max_workers", value=max_workers, expected_type=type_hints["max_workers"])
            check_type(argname="argument min_workers", value=min_workers, expected_type=type_hints["min_workers"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_workers is not None:
            self._values["max_workers"] = max_workers
        if min_workers is not None:
            self._values["min_workers"] = min_workers

    @builtins.property
    def max_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#max_workers Cluster#max_workers}.'''
        result = self._values.get("max_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#min_workers Cluster#min_workers}.'''
        result = self._values.get("min_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterAutoscale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterAutoscaleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterAutoscaleOutputReference",
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
            type_hints = typing.get_type_hints(ClusterAutoscaleOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ClusterAutoscaleOutputReference, "max_workers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="minWorkers")
    def min_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minWorkers"))

    @min_workers.setter
    def min_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterAutoscaleOutputReference, "min_workers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterAutoscale]:
        return typing.cast(typing.Optional[ClusterAutoscale], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterAutoscale]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterAutoscaleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterAwsAttributes",
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
class ClusterAwsAttributes:
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
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.
        :param ebs_volume_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_count Cluster#ebs_volume_count}.
        :param ebs_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_size Cluster#ebs_volume_size}.
        :param ebs_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_type Cluster#ebs_volume_type}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#first_on_demand Cluster#first_on_demand}.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#instance_profile_arn Cluster#instance_profile_arn}.
        :param spot_bid_price_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spot_bid_price_percent Cluster#spot_bid_price_percent}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#zone_id Cluster#zone_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterAwsAttributes.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_volume_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_count Cluster#ebs_volume_count}.'''
        result = self._values.get("ebs_volume_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ebs_volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_size Cluster#ebs_volume_size}.'''
        result = self._values.get("ebs_volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ebs_volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_type Cluster#ebs_volume_type}.'''
        result = self._values.get("ebs_volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_on_demand(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#first_on_demand Cluster#first_on_demand}.'''
        result = self._values.get("first_on_demand")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#instance_profile_arn Cluster#instance_profile_arn}.'''
        result = self._values.get("instance_profile_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_bid_price_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spot_bid_price_percent Cluster#spot_bid_price_percent}.'''
        result = self._values.get("spot_bid_price_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#zone_id Cluster#zone_id}.'''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterAwsAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterAwsAttributesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterAwsAttributesOutputReference",
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
            type_hints = typing.get_type_hints(ClusterAwsAttributesOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ClusterAwsAttributesOutputReference, "availability").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeCount")
    def ebs_volume_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsVolumeCount"))

    @ebs_volume_count.setter
    def ebs_volume_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterAwsAttributesOutputReference, "ebs_volume_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeCount", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeSize")
    def ebs_volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsVolumeSize"))

    @ebs_volume_size.setter
    def ebs_volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterAwsAttributesOutputReference, "ebs_volume_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeType")
    def ebs_volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ebsVolumeType"))

    @ebs_volume_type.setter
    def ebs_volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterAwsAttributesOutputReference, "ebs_volume_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeType", value)

    @builtins.property
    @jsii.member(jsii_name="firstOnDemand")
    def first_on_demand(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "firstOnDemand"))

    @first_on_demand.setter
    def first_on_demand(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterAwsAttributesOutputReference, "first_on_demand").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstOnDemand", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArn")
    def instance_profile_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileArn"))

    @instance_profile_arn.setter
    def instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterAwsAttributesOutputReference, "instance_profile_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="spotBidPricePercent")
    def spot_bid_price_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotBidPricePercent"))

    @spot_bid_price_percent.setter
    def spot_bid_price_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterAwsAttributesOutputReference, "spot_bid_price_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotBidPricePercent", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterAwsAttributesOutputReference, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterAwsAttributes]:
        return typing.cast(typing.Optional[ClusterAwsAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterAwsAttributes]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterAwsAttributesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterAzureAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "first_on_demand": "firstOnDemand",
        "spot_bid_max_price": "spotBidMaxPrice",
    },
)
class ClusterAzureAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        first_on_demand: typing.Optional[jsii.Number] = None,
        spot_bid_max_price: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#first_on_demand Cluster#first_on_demand}.
        :param spot_bid_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spot_bid_max_price Cluster#spot_bid_max_price}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterAzureAttributes.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_on_demand(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#first_on_demand Cluster#first_on_demand}.'''
        result = self._values.get("first_on_demand")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spot_bid_max_price(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spot_bid_max_price Cluster#spot_bid_max_price}.'''
        result = self._values.get("spot_bid_max_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterAzureAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterAzureAttributesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterAzureAttributesOutputReference",
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
            type_hints = typing.get_type_hints(ClusterAzureAttributesOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ClusterAzureAttributesOutputReference, "availability").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="firstOnDemand")
    def first_on_demand(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "firstOnDemand"))

    @first_on_demand.setter
    def first_on_demand(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterAzureAttributesOutputReference, "first_on_demand").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstOnDemand", value)

    @builtins.property
    @jsii.member(jsii_name="spotBidMaxPrice")
    def spot_bid_max_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotBidMaxPrice"))

    @spot_bid_max_price.setter
    def spot_bid_max_price(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterAzureAttributesOutputReference, "spot_bid_max_price").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotBidMaxPrice", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterAzureAttributes]:
        return typing.cast(typing.Optional[ClusterAzureAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterAzureAttributes]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterAzureAttributesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterClusterLogConf",
    jsii_struct_bases=[],
    name_mapping={"dbfs": "dbfs", "s3": "s3"},
)
class ClusterClusterLogConf:
    def __init__(
        self,
        *,
        dbfs: typing.Optional[typing.Union["ClusterClusterLogConfDbfs", typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["ClusterClusterLogConfS3", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dbfs: dbfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#dbfs Cluster#dbfs}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#s3 Cluster#s3}
        '''
        if isinstance(dbfs, dict):
            dbfs = ClusterClusterLogConfDbfs(**dbfs)
        if isinstance(s3, dict):
            s3 = ClusterClusterLogConfS3(**s3)
        if __debug__:
            type_hints = typing.get_type_hints(ClusterClusterLogConf.__init__)
            check_type(argname="argument dbfs", value=dbfs, expected_type=type_hints["dbfs"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dbfs is not None:
            self._values["dbfs"] = dbfs
        if s3 is not None:
            self._values["s3"] = s3

    @builtins.property
    def dbfs(self) -> typing.Optional["ClusterClusterLogConfDbfs"]:
        '''dbfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#dbfs Cluster#dbfs}
        '''
        result = self._values.get("dbfs")
        return typing.cast(typing.Optional["ClusterClusterLogConfDbfs"], result)

    @builtins.property
    def s3(self) -> typing.Optional["ClusterClusterLogConfS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#s3 Cluster#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["ClusterClusterLogConfS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterClusterLogConf(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterClusterLogConfDbfs",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class ClusterClusterLogConfDbfs:
    def __init__(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterClusterLogConfDbfs.__init__)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterClusterLogConfDbfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterClusterLogConfDbfsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterClusterLogConfDbfsOutputReference",
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
            type_hints = typing.get_type_hints(ClusterClusterLogConfDbfsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ClusterClusterLogConfDbfsOutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterClusterLogConfDbfs]:
        return typing.cast(typing.Optional[ClusterClusterLogConfDbfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterClusterLogConfDbfs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterClusterLogConfDbfsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterClusterLogConfOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterClusterLogConfOutputReference",
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
            type_hints = typing.get_type_hints(ClusterClusterLogConfOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDbfs")
    def put_dbfs(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        value = ClusterClusterLogConfDbfs(destination=destination)

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
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#canned_acl Cluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_encryption Cluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#encryption_type Cluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#endpoint Cluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#kms_key Cluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#region Cluster#region}.
        '''
        value = ClusterClusterLogConfS3(
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
    def dbfs(self) -> ClusterClusterLogConfDbfsOutputReference:
        return typing.cast(ClusterClusterLogConfDbfsOutputReference, jsii.get(self, "dbfs"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "ClusterClusterLogConfS3OutputReference":
        return typing.cast("ClusterClusterLogConfS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="dbfsInput")
    def dbfs_input(self) -> typing.Optional[ClusterClusterLogConfDbfs]:
        return typing.cast(typing.Optional[ClusterClusterLogConfDbfs], jsii.get(self, "dbfsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional["ClusterClusterLogConfS3"]:
        return typing.cast(typing.Optional["ClusterClusterLogConfS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterClusterLogConf]:
        return typing.cast(typing.Optional[ClusterClusterLogConf], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterClusterLogConf]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterClusterLogConfOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterClusterLogConfS3",
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
class ClusterClusterLogConfS3:
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
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#canned_acl Cluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_encryption Cluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#encryption_type Cluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#endpoint Cluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#kms_key Cluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#region Cluster#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterClusterLogConfS3.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def canned_acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#canned_acl Cluster#canned_acl}.'''
        result = self._values.get("canned_acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_encryption Cluster#enable_encryption}.'''
        result = self._values.get("enable_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encryption_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#encryption_type Cluster#encryption_type}.'''
        result = self._values.get("encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#endpoint Cluster#endpoint}.'''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#kms_key Cluster#kms_key}.'''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#region Cluster#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterClusterLogConfS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterClusterLogConfS3OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterClusterLogConfS3OutputReference",
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
            type_hints = typing.get_type_hints(ClusterClusterLogConfS3OutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ClusterClusterLogConfS3OutputReference, "canned_acl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cannedAcl", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterClusterLogConfS3OutputReference, "destination").fset)
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
            type_hints = typing.get_type_hints(getattr(ClusterClusterLogConfS3OutputReference, "enable_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterClusterLogConfS3OutputReference, "encryption_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterClusterLogConfS3OutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterClusterLogConfS3OutputReference, "kms_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterClusterLogConfS3OutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterClusterLogConfS3]:
        return typing.cast(typing.Optional[ClusterClusterLogConfS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterClusterLogConfS3]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterClusterLogConfS3OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "spark_version": "sparkVersion",
        "apply_policy_default_values": "applyPolicyDefaultValues",
        "autoscale": "autoscale",
        "autotermination_minutes": "autoterminationMinutes",
        "aws_attributes": "awsAttributes",
        "azure_attributes": "azureAttributes",
        "cluster_id": "clusterId",
        "cluster_log_conf": "clusterLogConf",
        "cluster_name": "clusterName",
        "custom_tags": "customTags",
        "data_security_mode": "dataSecurityMode",
        "docker_image": "dockerImage",
        "driver_instance_pool_id": "driverInstancePoolId",
        "driver_node_type_id": "driverNodeTypeId",
        "enable_elastic_disk": "enableElasticDisk",
        "enable_local_disk_encryption": "enableLocalDiskEncryption",
        "gcp_attributes": "gcpAttributes",
        "id": "id",
        "idempotency_token": "idempotencyToken",
        "init_scripts": "initScripts",
        "instance_pool_id": "instancePoolId",
        "is_pinned": "isPinned",
        "library": "library",
        "node_type_id": "nodeTypeId",
        "num_workers": "numWorkers",
        "policy_id": "policyId",
        "single_user_name": "singleUserName",
        "spark_conf": "sparkConf",
        "spark_env_vars": "sparkEnvVars",
        "ssh_public_keys": "sshPublicKeys",
        "timeouts": "timeouts",
        "workload_type": "workloadType",
    },
)
class ClusterConfig(cdktf.TerraformMetaArguments):
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
        spark_version: builtins.str,
        apply_policy_default_values: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autoscale: typing.Optional[typing.Union[ClusterAutoscale, typing.Dict[str, typing.Any]]] = None,
        autotermination_minutes: typing.Optional[jsii.Number] = None,
        aws_attributes: typing.Optional[typing.Union[ClusterAwsAttributes, typing.Dict[str, typing.Any]]] = None,
        azure_attributes: typing.Optional[typing.Union[ClusterAzureAttributes, typing.Dict[str, typing.Any]]] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        cluster_log_conf: typing.Optional[typing.Union[ClusterClusterLogConf, typing.Dict[str, typing.Any]]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        data_security_mode: typing.Optional[builtins.str] = None,
        docker_image: typing.Optional[typing.Union["ClusterDockerImage", typing.Dict[str, typing.Any]]] = None,
        driver_instance_pool_id: typing.Optional[builtins.str] = None,
        driver_node_type_id: typing.Optional[builtins.str] = None,
        enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_local_disk_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        gcp_attributes: typing.Optional[typing.Union["ClusterGcpAttributes", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        idempotency_token: typing.Optional[builtins.str] = None,
        init_scripts: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ClusterInitScripts", typing.Dict[str, typing.Any]]]]] = None,
        instance_pool_id: typing.Optional[builtins.str] = None,
        is_pinned: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        library: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ClusterLibrary", typing.Dict[str, typing.Any]]]]] = None,
        node_type_id: typing.Optional[builtins.str] = None,
        num_workers: typing.Optional[jsii.Number] = None,
        policy_id: typing.Optional[builtins.str] = None,
        single_user_name: typing.Optional[builtins.str] = None,
        spark_conf: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        spark_env_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        workload_type: typing.Optional[typing.Union["ClusterWorkloadType", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param spark_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_version Cluster#spark_version}.
        :param apply_policy_default_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#apply_policy_default_values Cluster#apply_policy_default_values}.
        :param autoscale: autoscale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#autoscale Cluster#autoscale}
        :param autotermination_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#autotermination_minutes Cluster#autotermination_minutes}.
        :param aws_attributes: aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#aws_attributes Cluster#aws_attributes}
        :param azure_attributes: azure_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#azure_attributes Cluster#azure_attributes}
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_id Cluster#cluster_id}.
        :param cluster_log_conf: cluster_log_conf block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_log_conf Cluster#cluster_log_conf}
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_name Cluster#cluster_name}.
        :param custom_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#custom_tags Cluster#custom_tags}.
        :param data_security_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#data_security_mode Cluster#data_security_mode}.
        :param docker_image: docker_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#docker_image Cluster#docker_image}
        :param driver_instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#driver_instance_pool_id Cluster#driver_instance_pool_id}.
        :param driver_node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#driver_node_type_id Cluster#driver_node_type_id}.
        :param enable_elastic_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_elastic_disk Cluster#enable_elastic_disk}.
        :param enable_local_disk_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_local_disk_encryption Cluster#enable_local_disk_encryption}.
        :param gcp_attributes: gcp_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#gcp_attributes Cluster#gcp_attributes}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#id Cluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idempotency_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#idempotency_token Cluster#idempotency_token}.
        :param init_scripts: init_scripts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#init_scripts Cluster#init_scripts}
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#instance_pool_id Cluster#instance_pool_id}.
        :param is_pinned: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#is_pinned Cluster#is_pinned}.
        :param library: library block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#library Cluster#library}
        :param node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#node_type_id Cluster#node_type_id}.
        :param num_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#num_workers Cluster#num_workers}.
        :param policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#policy_id Cluster#policy_id}.
        :param single_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#single_user_name Cluster#single_user_name}.
        :param spark_conf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_conf Cluster#spark_conf}.
        :param spark_env_vars: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_env_vars Cluster#spark_env_vars}.
        :param ssh_public_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ssh_public_keys Cluster#ssh_public_keys}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#timeouts Cluster#timeouts}
        :param workload_type: workload_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#workload_type Cluster#workload_type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(autoscale, dict):
            autoscale = ClusterAutoscale(**autoscale)
        if isinstance(aws_attributes, dict):
            aws_attributes = ClusterAwsAttributes(**aws_attributes)
        if isinstance(azure_attributes, dict):
            azure_attributes = ClusterAzureAttributes(**azure_attributes)
        if isinstance(cluster_log_conf, dict):
            cluster_log_conf = ClusterClusterLogConf(**cluster_log_conf)
        if isinstance(docker_image, dict):
            docker_image = ClusterDockerImage(**docker_image)
        if isinstance(gcp_attributes, dict):
            gcp_attributes = ClusterGcpAttributes(**gcp_attributes)
        if isinstance(timeouts, dict):
            timeouts = ClusterTimeouts(**timeouts)
        if isinstance(workload_type, dict):
            workload_type = ClusterWorkloadType(**workload_type)
        if __debug__:
            type_hints = typing.get_type_hints(ClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument spark_version", value=spark_version, expected_type=type_hints["spark_version"])
            check_type(argname="argument apply_policy_default_values", value=apply_policy_default_values, expected_type=type_hints["apply_policy_default_values"])
            check_type(argname="argument autoscale", value=autoscale, expected_type=type_hints["autoscale"])
            check_type(argname="argument autotermination_minutes", value=autotermination_minutes, expected_type=type_hints["autotermination_minutes"])
            check_type(argname="argument aws_attributes", value=aws_attributes, expected_type=type_hints["aws_attributes"])
            check_type(argname="argument azure_attributes", value=azure_attributes, expected_type=type_hints["azure_attributes"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument cluster_log_conf", value=cluster_log_conf, expected_type=type_hints["cluster_log_conf"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument custom_tags", value=custom_tags, expected_type=type_hints["custom_tags"])
            check_type(argname="argument data_security_mode", value=data_security_mode, expected_type=type_hints["data_security_mode"])
            check_type(argname="argument docker_image", value=docker_image, expected_type=type_hints["docker_image"])
            check_type(argname="argument driver_instance_pool_id", value=driver_instance_pool_id, expected_type=type_hints["driver_instance_pool_id"])
            check_type(argname="argument driver_node_type_id", value=driver_node_type_id, expected_type=type_hints["driver_node_type_id"])
            check_type(argname="argument enable_elastic_disk", value=enable_elastic_disk, expected_type=type_hints["enable_elastic_disk"])
            check_type(argname="argument enable_local_disk_encryption", value=enable_local_disk_encryption, expected_type=type_hints["enable_local_disk_encryption"])
            check_type(argname="argument gcp_attributes", value=gcp_attributes, expected_type=type_hints["gcp_attributes"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument idempotency_token", value=idempotency_token, expected_type=type_hints["idempotency_token"])
            check_type(argname="argument init_scripts", value=init_scripts, expected_type=type_hints["init_scripts"])
            check_type(argname="argument instance_pool_id", value=instance_pool_id, expected_type=type_hints["instance_pool_id"])
            check_type(argname="argument is_pinned", value=is_pinned, expected_type=type_hints["is_pinned"])
            check_type(argname="argument library", value=library, expected_type=type_hints["library"])
            check_type(argname="argument node_type_id", value=node_type_id, expected_type=type_hints["node_type_id"])
            check_type(argname="argument num_workers", value=num_workers, expected_type=type_hints["num_workers"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument single_user_name", value=single_user_name, expected_type=type_hints["single_user_name"])
            check_type(argname="argument spark_conf", value=spark_conf, expected_type=type_hints["spark_conf"])
            check_type(argname="argument spark_env_vars", value=spark_env_vars, expected_type=type_hints["spark_env_vars"])
            check_type(argname="argument ssh_public_keys", value=ssh_public_keys, expected_type=type_hints["ssh_public_keys"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument workload_type", value=workload_type, expected_type=type_hints["workload_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "spark_version": spark_version,
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
        if apply_policy_default_values is not None:
            self._values["apply_policy_default_values"] = apply_policy_default_values
        if autoscale is not None:
            self._values["autoscale"] = autoscale
        if autotermination_minutes is not None:
            self._values["autotermination_minutes"] = autotermination_minutes
        if aws_attributes is not None:
            self._values["aws_attributes"] = aws_attributes
        if azure_attributes is not None:
            self._values["azure_attributes"] = azure_attributes
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if cluster_log_conf is not None:
            self._values["cluster_log_conf"] = cluster_log_conf
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if custom_tags is not None:
            self._values["custom_tags"] = custom_tags
        if data_security_mode is not None:
            self._values["data_security_mode"] = data_security_mode
        if docker_image is not None:
            self._values["docker_image"] = docker_image
        if driver_instance_pool_id is not None:
            self._values["driver_instance_pool_id"] = driver_instance_pool_id
        if driver_node_type_id is not None:
            self._values["driver_node_type_id"] = driver_node_type_id
        if enable_elastic_disk is not None:
            self._values["enable_elastic_disk"] = enable_elastic_disk
        if enable_local_disk_encryption is not None:
            self._values["enable_local_disk_encryption"] = enable_local_disk_encryption
        if gcp_attributes is not None:
            self._values["gcp_attributes"] = gcp_attributes
        if id is not None:
            self._values["id"] = id
        if idempotency_token is not None:
            self._values["idempotency_token"] = idempotency_token
        if init_scripts is not None:
            self._values["init_scripts"] = init_scripts
        if instance_pool_id is not None:
            self._values["instance_pool_id"] = instance_pool_id
        if is_pinned is not None:
            self._values["is_pinned"] = is_pinned
        if library is not None:
            self._values["library"] = library
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
        if spark_env_vars is not None:
            self._values["spark_env_vars"] = spark_env_vars
        if ssh_public_keys is not None:
            self._values["ssh_public_keys"] = ssh_public_keys
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if workload_type is not None:
            self._values["workload_type"] = workload_type

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
    def spark_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_version Cluster#spark_version}.'''
        result = self._values.get("spark_version")
        assert result is not None, "Required property 'spark_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def apply_policy_default_values(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#apply_policy_default_values Cluster#apply_policy_default_values}.'''
        result = self._values.get("apply_policy_default_values")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def autoscale(self) -> typing.Optional[ClusterAutoscale]:
        '''autoscale block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#autoscale Cluster#autoscale}
        '''
        result = self._values.get("autoscale")
        return typing.cast(typing.Optional[ClusterAutoscale], result)

    @builtins.property
    def autotermination_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#autotermination_minutes Cluster#autotermination_minutes}.'''
        result = self._values.get("autotermination_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def aws_attributes(self) -> typing.Optional[ClusterAwsAttributes]:
        '''aws_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#aws_attributes Cluster#aws_attributes}
        '''
        result = self._values.get("aws_attributes")
        return typing.cast(typing.Optional[ClusterAwsAttributes], result)

    @builtins.property
    def azure_attributes(self) -> typing.Optional[ClusterAzureAttributes]:
        '''azure_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#azure_attributes Cluster#azure_attributes}
        '''
        result = self._values.get("azure_attributes")
        return typing.cast(typing.Optional[ClusterAzureAttributes], result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_id Cluster#cluster_id}.'''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_log_conf(self) -> typing.Optional[ClusterClusterLogConf]:
        '''cluster_log_conf block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_log_conf Cluster#cluster_log_conf}
        '''
        result = self._values.get("cluster_log_conf")
        return typing.cast(typing.Optional[ClusterClusterLogConf], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_name Cluster#cluster_name}.'''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#custom_tags Cluster#custom_tags}.'''
        result = self._values.get("custom_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def data_security_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#data_security_mode Cluster#data_security_mode}.'''
        result = self._values.get("data_security_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_image(self) -> typing.Optional["ClusterDockerImage"]:
        '''docker_image block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#docker_image Cluster#docker_image}
        '''
        result = self._values.get("docker_image")
        return typing.cast(typing.Optional["ClusterDockerImage"], result)

    @builtins.property
    def driver_instance_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#driver_instance_pool_id Cluster#driver_instance_pool_id}.'''
        result = self._values.get("driver_instance_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def driver_node_type_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#driver_node_type_id Cluster#driver_node_type_id}.'''
        result = self._values.get("driver_node_type_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_elastic_disk(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_elastic_disk Cluster#enable_elastic_disk}.'''
        result = self._values.get("enable_elastic_disk")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_local_disk_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_local_disk_encryption Cluster#enable_local_disk_encryption}.'''
        result = self._values.get("enable_local_disk_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def gcp_attributes(self) -> typing.Optional["ClusterGcpAttributes"]:
        '''gcp_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#gcp_attributes Cluster#gcp_attributes}
        '''
        result = self._values.get("gcp_attributes")
        return typing.cast(typing.Optional["ClusterGcpAttributes"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#id Cluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idempotency_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#idempotency_token Cluster#idempotency_token}.'''
        result = self._values.get("idempotency_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def init_scripts(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ClusterInitScripts"]]]:
        '''init_scripts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#init_scripts Cluster#init_scripts}
        '''
        result = self._values.get("init_scripts")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ClusterInitScripts"]]], result)

    @builtins.property
    def instance_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#instance_pool_id Cluster#instance_pool_id}.'''
        result = self._values.get("instance_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_pinned(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#is_pinned Cluster#is_pinned}.'''
        result = self._values.get("is_pinned")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def library(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ClusterLibrary"]]]:
        '''library block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#library Cluster#library}
        '''
        result = self._values.get("library")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ClusterLibrary"]]], result)

    @builtins.property
    def node_type_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#node_type_id Cluster#node_type_id}.'''
        result = self._values.get("node_type_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#num_workers Cluster#num_workers}.'''
        result = self._values.get("num_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#policy_id Cluster#policy_id}.'''
        result = self._values.get("policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#single_user_name Cluster#single_user_name}.'''
        result = self._values.get("single_user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spark_conf(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_conf Cluster#spark_conf}.'''
        result = self._values.get("spark_conf")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def spark_env_vars(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_env_vars Cluster#spark_env_vars}.'''
        result = self._values.get("spark_env_vars")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def ssh_public_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ssh_public_keys Cluster#ssh_public_keys}.'''
        result = self._values.get("ssh_public_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#timeouts Cluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ClusterTimeouts"], result)

    @builtins.property
    def workload_type(self) -> typing.Optional["ClusterWorkloadType"]:
        '''workload_type block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#workload_type Cluster#workload_type}
        '''
        result = self._values.get("workload_type")
        return typing.cast(typing.Optional["ClusterWorkloadType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterDockerImage",
    jsii_struct_bases=[],
    name_mapping={"url": "url", "basic_auth": "basicAuth"},
)
class ClusterDockerImage:
    def __init__(
        self,
        *,
        url: builtins.str,
        basic_auth: typing.Optional[typing.Union["ClusterDockerImageBasicAuth", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#url Cluster#url}.
        :param basic_auth: basic_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#basic_auth Cluster#basic_auth}
        '''
        if isinstance(basic_auth, dict):
            basic_auth = ClusterDockerImageBasicAuth(**basic_auth)
        if __debug__:
            type_hints = typing.get_type_hints(ClusterDockerImage.__init__)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument basic_auth", value=basic_auth, expected_type=type_hints["basic_auth"])
        self._values: typing.Dict[str, typing.Any] = {
            "url": url,
        }
        if basic_auth is not None:
            self._values["basic_auth"] = basic_auth

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#url Cluster#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def basic_auth(self) -> typing.Optional["ClusterDockerImageBasicAuth"]:
        '''basic_auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#basic_auth Cluster#basic_auth}
        '''
        result = self._values.get("basic_auth")
        return typing.cast(typing.Optional["ClusterDockerImageBasicAuth"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterDockerImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterDockerImageBasicAuth",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class ClusterDockerImageBasicAuth:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#password Cluster#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#username Cluster#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterDockerImageBasicAuth.__init__)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#password Cluster#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#username Cluster#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterDockerImageBasicAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterDockerImageBasicAuthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterDockerImageBasicAuthOutputReference",
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
            type_hints = typing.get_type_hints(ClusterDockerImageBasicAuthOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ClusterDockerImageBasicAuthOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterDockerImageBasicAuthOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterDockerImageBasicAuth]:
        return typing.cast(typing.Optional[ClusterDockerImageBasicAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ClusterDockerImageBasicAuth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterDockerImageBasicAuthOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterDockerImageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterDockerImageOutputReference",
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
            type_hints = typing.get_type_hints(ClusterDockerImageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBasicAuth")
    def put_basic_auth(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#password Cluster#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#username Cluster#username}.
        '''
        value = ClusterDockerImageBasicAuth(password=password, username=username)

        return typing.cast(None, jsii.invoke(self, "putBasicAuth", [value]))

    @jsii.member(jsii_name="resetBasicAuth")
    def reset_basic_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuth", []))

    @builtins.property
    @jsii.member(jsii_name="basicAuth")
    def basic_auth(self) -> ClusterDockerImageBasicAuthOutputReference:
        return typing.cast(ClusterDockerImageBasicAuthOutputReference, jsii.get(self, "basicAuth"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthInput")
    def basic_auth_input(self) -> typing.Optional[ClusterDockerImageBasicAuth]:
        return typing.cast(typing.Optional[ClusterDockerImageBasicAuth], jsii.get(self, "basicAuthInput"))

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
            type_hints = typing.get_type_hints(getattr(ClusterDockerImageOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterDockerImage]:
        return typing.cast(typing.Optional[ClusterDockerImage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterDockerImage]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterDockerImageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterGcpAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "boot_disk_size": "bootDiskSize",
        "google_service_account": "googleServiceAccount",
        "use_preemptible_executors": "usePreemptibleExecutors",
        "zone_id": "zoneId",
    },
)
class ClusterGcpAttributes:
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
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.
        :param boot_disk_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#boot_disk_size Cluster#boot_disk_size}.
        :param google_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#google_service_account Cluster#google_service_account}.
        :param use_preemptible_executors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#use_preemptible_executors Cluster#use_preemptible_executors}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#zone_id Cluster#zone_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterGcpAttributes.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def boot_disk_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#boot_disk_size Cluster#boot_disk_size}.'''
        result = self._values.get("boot_disk_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def google_service_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#google_service_account Cluster#google_service_account}.'''
        result = self._values.get("google_service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_preemptible_executors(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#use_preemptible_executors Cluster#use_preemptible_executors}.'''
        result = self._values.get("use_preemptible_executors")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#zone_id Cluster#zone_id}.'''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterGcpAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterGcpAttributesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterGcpAttributesOutputReference",
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
            type_hints = typing.get_type_hints(ClusterGcpAttributesOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ClusterGcpAttributesOutputReference, "availability").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="bootDiskSize")
    def boot_disk_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bootDiskSize"))

    @boot_disk_size.setter
    def boot_disk_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterGcpAttributesOutputReference, "boot_disk_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskSize", value)

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccount")
    def google_service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "googleServiceAccount"))

    @google_service_account.setter
    def google_service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterGcpAttributesOutputReference, "google_service_account").fset)
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
            type_hints = typing.get_type_hints(getattr(ClusterGcpAttributesOutputReference, "use_preemptible_executors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usePreemptibleExecutors", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterGcpAttributesOutputReference, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterGcpAttributes]:
        return typing.cast(typing.Optional[ClusterGcpAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterGcpAttributes]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterGcpAttributesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterInitScripts",
    jsii_struct_bases=[],
    name_mapping={"dbfs": "dbfs", "file": "file", "gcs": "gcs", "s3": "s3"},
)
class ClusterInitScripts:
    def __init__(
        self,
        *,
        dbfs: typing.Optional[typing.Union["ClusterInitScriptsDbfs", typing.Dict[str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["ClusterInitScriptsFile", typing.Dict[str, typing.Any]]] = None,
        gcs: typing.Optional[typing.Union["ClusterInitScriptsGcs", typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["ClusterInitScriptsS3", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dbfs: dbfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#dbfs Cluster#dbfs}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#file Cluster#file}
        :param gcs: gcs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#gcs Cluster#gcs}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#s3 Cluster#s3}
        '''
        if isinstance(dbfs, dict):
            dbfs = ClusterInitScriptsDbfs(**dbfs)
        if isinstance(file, dict):
            file = ClusterInitScriptsFile(**file)
        if isinstance(gcs, dict):
            gcs = ClusterInitScriptsGcs(**gcs)
        if isinstance(s3, dict):
            s3 = ClusterInitScriptsS3(**s3)
        if __debug__:
            type_hints = typing.get_type_hints(ClusterInitScripts.__init__)
            check_type(argname="argument dbfs", value=dbfs, expected_type=type_hints["dbfs"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument gcs", value=gcs, expected_type=type_hints["gcs"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dbfs is not None:
            self._values["dbfs"] = dbfs
        if file is not None:
            self._values["file"] = file
        if gcs is not None:
            self._values["gcs"] = gcs
        if s3 is not None:
            self._values["s3"] = s3

    @builtins.property
    def dbfs(self) -> typing.Optional["ClusterInitScriptsDbfs"]:
        '''dbfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#dbfs Cluster#dbfs}
        '''
        result = self._values.get("dbfs")
        return typing.cast(typing.Optional["ClusterInitScriptsDbfs"], result)

    @builtins.property
    def file(self) -> typing.Optional["ClusterInitScriptsFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#file Cluster#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["ClusterInitScriptsFile"], result)

    @builtins.property
    def gcs(self) -> typing.Optional["ClusterInitScriptsGcs"]:
        '''gcs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#gcs Cluster#gcs}
        '''
        result = self._values.get("gcs")
        return typing.cast(typing.Optional["ClusterInitScriptsGcs"], result)

    @builtins.property
    def s3(self) -> typing.Optional["ClusterInitScriptsS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#s3 Cluster#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["ClusterInitScriptsS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterInitScripts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterInitScriptsDbfs",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class ClusterInitScriptsDbfs:
    def __init__(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterInitScriptsDbfs.__init__)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterInitScriptsDbfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterInitScriptsDbfsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterInitScriptsDbfsOutputReference",
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
            type_hints = typing.get_type_hints(ClusterInitScriptsDbfsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsDbfsOutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterInitScriptsDbfs]:
        return typing.cast(typing.Optional[ClusterInitScriptsDbfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterInitScriptsDbfs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsDbfsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterInitScriptsFile",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class ClusterInitScriptsFile:
    def __init__(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterInitScriptsFile.__init__)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.'''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterInitScriptsFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterInitScriptsFileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterInitScriptsFileOutputReference",
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
            type_hints = typing.get_type_hints(ClusterInitScriptsFileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDestination")
    def reset_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestination", []))

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
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsFileOutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterInitScriptsFile]:
        return typing.cast(typing.Optional[ClusterInitScriptsFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterInitScriptsFile]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsFileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterInitScriptsGcs",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class ClusterInitScriptsGcs:
    def __init__(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterInitScriptsGcs.__init__)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.'''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterInitScriptsGcs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterInitScriptsGcsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterInitScriptsGcsOutputReference",
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
            type_hints = typing.get_type_hints(ClusterInitScriptsGcsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDestination")
    def reset_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestination", []))

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
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsGcsOutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterInitScriptsGcs]:
        return typing.cast(typing.Optional[ClusterInitScriptsGcs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterInitScriptsGcs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsGcsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterInitScriptsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterInitScriptsList",
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
            type_hints = typing.get_type_hints(ClusterInitScriptsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ClusterInitScriptsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterInitScriptsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ClusterInitScriptsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ClusterInitScripts]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ClusterInitScripts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ClusterInitScripts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterInitScriptsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterInitScriptsOutputReference",
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
            type_hints = typing.get_type_hints(ClusterInitScriptsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDbfs")
    def put_dbfs(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        value = ClusterInitScriptsDbfs(destination=destination)

        return typing.cast(None, jsii.invoke(self, "putDbfs", [value]))

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        value = ClusterInitScriptsFile(destination=destination)

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putGcs")
    def put_gcs(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        value = ClusterInitScriptsGcs(destination=destination)

        return typing.cast(None, jsii.invoke(self, "putGcs", [value]))

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
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#canned_acl Cluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_encryption Cluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#encryption_type Cluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#endpoint Cluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#kms_key Cluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#region Cluster#region}.
        '''
        value = ClusterInitScriptsS3(
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

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetGcs")
    def reset_gcs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcs", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @builtins.property
    @jsii.member(jsii_name="dbfs")
    def dbfs(self) -> ClusterInitScriptsDbfsOutputReference:
        return typing.cast(ClusterInitScriptsDbfsOutputReference, jsii.get(self, "dbfs"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> ClusterInitScriptsFileOutputReference:
        return typing.cast(ClusterInitScriptsFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="gcs")
    def gcs(self) -> ClusterInitScriptsGcsOutputReference:
        return typing.cast(ClusterInitScriptsGcsOutputReference, jsii.get(self, "gcs"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "ClusterInitScriptsS3OutputReference":
        return typing.cast("ClusterInitScriptsS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="dbfsInput")
    def dbfs_input(self) -> typing.Optional[ClusterInitScriptsDbfs]:
        return typing.cast(typing.Optional[ClusterInitScriptsDbfs], jsii.get(self, "dbfsInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(self) -> typing.Optional[ClusterInitScriptsFile]:
        return typing.cast(typing.Optional[ClusterInitScriptsFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsInput")
    def gcs_input(self) -> typing.Optional[ClusterInitScriptsGcs]:
        return typing.cast(typing.Optional[ClusterInitScriptsGcs], jsii.get(self, "gcsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional["ClusterInitScriptsS3"]:
        return typing.cast(typing.Optional["ClusterInitScriptsS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ClusterInitScripts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ClusterInitScripts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ClusterInitScripts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterInitScriptsS3",
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
class ClusterInitScriptsS3:
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
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#canned_acl Cluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_encryption Cluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#encryption_type Cluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#endpoint Cluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#kms_key Cluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#region Cluster#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterInitScriptsS3.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def canned_acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#canned_acl Cluster#canned_acl}.'''
        result = self._values.get("canned_acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_encryption Cluster#enable_encryption}.'''
        result = self._values.get("enable_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encryption_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#encryption_type Cluster#encryption_type}.'''
        result = self._values.get("encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#endpoint Cluster#endpoint}.'''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#kms_key Cluster#kms_key}.'''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#region Cluster#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterInitScriptsS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterInitScriptsS3OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterInitScriptsS3OutputReference",
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
            type_hints = typing.get_type_hints(ClusterInitScriptsS3OutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsS3OutputReference, "canned_acl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cannedAcl", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsS3OutputReference, "destination").fset)
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
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsS3OutputReference, "enable_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsS3OutputReference, "encryption_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsS3OutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsS3OutputReference, "kms_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsS3OutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterInitScriptsS3]:
        return typing.cast(typing.Optional[ClusterInitScriptsS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterInitScriptsS3]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterInitScriptsS3OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterLibrary",
    jsii_struct_bases=[],
    name_mapping={
        "cran": "cran",
        "egg": "egg",
        "jar": "jar",
        "maven": "maven",
        "pypi": "pypi",
        "whl": "whl",
    },
)
class ClusterLibrary:
    def __init__(
        self,
        *,
        cran: typing.Optional[typing.Union["ClusterLibraryCran", typing.Dict[str, typing.Any]]] = None,
        egg: typing.Optional[builtins.str] = None,
        jar: typing.Optional[builtins.str] = None,
        maven: typing.Optional[typing.Union["ClusterLibraryMaven", typing.Dict[str, typing.Any]]] = None,
        pypi: typing.Optional[typing.Union["ClusterLibraryPypi", typing.Dict[str, typing.Any]]] = None,
        whl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cran: cran block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cran Cluster#cran}
        :param egg: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#egg Cluster#egg}.
        :param jar: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#jar Cluster#jar}.
        :param maven: maven block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#maven Cluster#maven}
        :param pypi: pypi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#pypi Cluster#pypi}
        :param whl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#whl Cluster#whl}.
        '''
        if isinstance(cran, dict):
            cran = ClusterLibraryCran(**cran)
        if isinstance(maven, dict):
            maven = ClusterLibraryMaven(**maven)
        if isinstance(pypi, dict):
            pypi = ClusterLibraryPypi(**pypi)
        if __debug__:
            type_hints = typing.get_type_hints(ClusterLibrary.__init__)
            check_type(argname="argument cran", value=cran, expected_type=type_hints["cran"])
            check_type(argname="argument egg", value=egg, expected_type=type_hints["egg"])
            check_type(argname="argument jar", value=jar, expected_type=type_hints["jar"])
            check_type(argname="argument maven", value=maven, expected_type=type_hints["maven"])
            check_type(argname="argument pypi", value=pypi, expected_type=type_hints["pypi"])
            check_type(argname="argument whl", value=whl, expected_type=type_hints["whl"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cran is not None:
            self._values["cran"] = cran
        if egg is not None:
            self._values["egg"] = egg
        if jar is not None:
            self._values["jar"] = jar
        if maven is not None:
            self._values["maven"] = maven
        if pypi is not None:
            self._values["pypi"] = pypi
        if whl is not None:
            self._values["whl"] = whl

    @builtins.property
    def cran(self) -> typing.Optional["ClusterLibraryCran"]:
        '''cran block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cran Cluster#cran}
        '''
        result = self._values.get("cran")
        return typing.cast(typing.Optional["ClusterLibraryCran"], result)

    @builtins.property
    def egg(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#egg Cluster#egg}.'''
        result = self._values.get("egg")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jar(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#jar Cluster#jar}.'''
        result = self._values.get("jar")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maven(self) -> typing.Optional["ClusterLibraryMaven"]:
        '''maven block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#maven Cluster#maven}
        '''
        result = self._values.get("maven")
        return typing.cast(typing.Optional["ClusterLibraryMaven"], result)

    @builtins.property
    def pypi(self) -> typing.Optional["ClusterLibraryPypi"]:
        '''pypi block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#pypi Cluster#pypi}
        '''
        result = self._values.get("pypi")
        return typing.cast(typing.Optional["ClusterLibraryPypi"], result)

    @builtins.property
    def whl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#whl Cluster#whl}.'''
        result = self._values.get("whl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterLibrary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterLibraryCran",
    jsii_struct_bases=[],
    name_mapping={"package": "package", "repo": "repo"},
)
class ClusterLibraryCran:
    def __init__(
        self,
        *,
        package: builtins.str,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param package: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#package Cluster#package}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterLibraryCran.__init__)
            check_type(argname="argument package", value=package, expected_type=type_hints["package"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[str, typing.Any] = {
            "package": package,
        }
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def package(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#package Cluster#package}.'''
        result = self._values.get("package")
        assert result is not None, "Required property 'package' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.'''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterLibraryCran(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterLibraryCranOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterLibraryCranOutputReference",
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
            type_hints = typing.get_type_hints(ClusterLibraryCranOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="packageInput")
    def package_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "packageInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="package")
    def package(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "package"))

    @package.setter
    def package(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryCranOutputReference, "package").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "package", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryCranOutputReference, "repo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterLibraryCran]:
        return typing.cast(typing.Optional[ClusterLibraryCran], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterLibraryCran]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryCranOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterLibraryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterLibraryList",
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
            type_hints = typing.get_type_hints(ClusterLibraryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ClusterLibraryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterLibraryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ClusterLibraryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ClusterLibraryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ClusterLibraryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ClusterLibrary]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ClusterLibrary]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ClusterLibrary]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterLibraryMaven",
    jsii_struct_bases=[],
    name_mapping={
        "coordinates": "coordinates",
        "exclusions": "exclusions",
        "repo": "repo",
    },
)
class ClusterLibraryMaven:
    def __init__(
        self,
        *,
        coordinates: builtins.str,
        exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param coordinates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#coordinates Cluster#coordinates}.
        :param exclusions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#exclusions Cluster#exclusions}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterLibraryMaven.__init__)
            check_type(argname="argument coordinates", value=coordinates, expected_type=type_hints["coordinates"])
            check_type(argname="argument exclusions", value=exclusions, expected_type=type_hints["exclusions"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[str, typing.Any] = {
            "coordinates": coordinates,
        }
        if exclusions is not None:
            self._values["exclusions"] = exclusions
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def coordinates(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#coordinates Cluster#coordinates}.'''
        result = self._values.get("coordinates")
        assert result is not None, "Required property 'coordinates' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclusions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#exclusions Cluster#exclusions}.'''
        result = self._values.get("exclusions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.'''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterLibraryMaven(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterLibraryMavenOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterLibraryMavenOutputReference",
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
            type_hints = typing.get_type_hints(ClusterLibraryMavenOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExclusions")
    def reset_exclusions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusions", []))

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="coordinatesInput")
    def coordinates_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "coordinatesInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionsInput")
    def exclusions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exclusionsInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="coordinates")
    def coordinates(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "coordinates"))

    @coordinates.setter
    def coordinates(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryMavenOutputReference, "coordinates").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coordinates", value)

    @builtins.property
    @jsii.member(jsii_name="exclusions")
    def exclusions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclusions"))

    @exclusions.setter
    def exclusions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryMavenOutputReference, "exclusions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusions", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryMavenOutputReference, "repo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterLibraryMaven]:
        return typing.cast(typing.Optional[ClusterLibraryMaven], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterLibraryMaven]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryMavenOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterLibraryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterLibraryOutputReference",
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
            type_hints = typing.get_type_hints(ClusterLibraryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCran")
    def put_cran(
        self,
        *,
        package: builtins.str,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param package: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#package Cluster#package}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.
        '''
        value = ClusterLibraryCran(package=package, repo=repo)

        return typing.cast(None, jsii.invoke(self, "putCran", [value]))

    @jsii.member(jsii_name="putMaven")
    def put_maven(
        self,
        *,
        coordinates: builtins.str,
        exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param coordinates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#coordinates Cluster#coordinates}.
        :param exclusions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#exclusions Cluster#exclusions}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.
        '''
        value = ClusterLibraryMaven(
            coordinates=coordinates, exclusions=exclusions, repo=repo
        )

        return typing.cast(None, jsii.invoke(self, "putMaven", [value]))

    @jsii.member(jsii_name="putPypi")
    def put_pypi(
        self,
        *,
        package: builtins.str,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param package: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#package Cluster#package}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.
        '''
        value = ClusterLibraryPypi(package=package, repo=repo)

        return typing.cast(None, jsii.invoke(self, "putPypi", [value]))

    @jsii.member(jsii_name="resetCran")
    def reset_cran(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCran", []))

    @jsii.member(jsii_name="resetEgg")
    def reset_egg(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgg", []))

    @jsii.member(jsii_name="resetJar")
    def reset_jar(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJar", []))

    @jsii.member(jsii_name="resetMaven")
    def reset_maven(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaven", []))

    @jsii.member(jsii_name="resetPypi")
    def reset_pypi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPypi", []))

    @jsii.member(jsii_name="resetWhl")
    def reset_whl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhl", []))

    @builtins.property
    @jsii.member(jsii_name="cran")
    def cran(self) -> ClusterLibraryCranOutputReference:
        return typing.cast(ClusterLibraryCranOutputReference, jsii.get(self, "cran"))

    @builtins.property
    @jsii.member(jsii_name="maven")
    def maven(self) -> ClusterLibraryMavenOutputReference:
        return typing.cast(ClusterLibraryMavenOutputReference, jsii.get(self, "maven"))

    @builtins.property
    @jsii.member(jsii_name="pypi")
    def pypi(self) -> "ClusterLibraryPypiOutputReference":
        return typing.cast("ClusterLibraryPypiOutputReference", jsii.get(self, "pypi"))

    @builtins.property
    @jsii.member(jsii_name="cranInput")
    def cran_input(self) -> typing.Optional[ClusterLibraryCran]:
        return typing.cast(typing.Optional[ClusterLibraryCran], jsii.get(self, "cranInput"))

    @builtins.property
    @jsii.member(jsii_name="eggInput")
    def egg_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eggInput"))

    @builtins.property
    @jsii.member(jsii_name="jarInput")
    def jar_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jarInput"))

    @builtins.property
    @jsii.member(jsii_name="mavenInput")
    def maven_input(self) -> typing.Optional[ClusterLibraryMaven]:
        return typing.cast(typing.Optional[ClusterLibraryMaven], jsii.get(self, "mavenInput"))

    @builtins.property
    @jsii.member(jsii_name="pypiInput")
    def pypi_input(self) -> typing.Optional["ClusterLibraryPypi"]:
        return typing.cast(typing.Optional["ClusterLibraryPypi"], jsii.get(self, "pypiInput"))

    @builtins.property
    @jsii.member(jsii_name="whlInput")
    def whl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whlInput"))

    @builtins.property
    @jsii.member(jsii_name="egg")
    def egg(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "egg"))

    @egg.setter
    def egg(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryOutputReference, "egg").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egg", value)

    @builtins.property
    @jsii.member(jsii_name="jar")
    def jar(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jar"))

    @jar.setter
    def jar(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryOutputReference, "jar").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jar", value)

    @builtins.property
    @jsii.member(jsii_name="whl")
    def whl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whl"))

    @whl.setter
    def whl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryOutputReference, "whl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ClusterLibrary, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ClusterLibrary, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ClusterLibrary, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterLibraryPypi",
    jsii_struct_bases=[],
    name_mapping={"package": "package", "repo": "repo"},
)
class ClusterLibraryPypi:
    def __init__(
        self,
        *,
        package: builtins.str,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param package: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#package Cluster#package}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterLibraryPypi.__init__)
            check_type(argname="argument package", value=package, expected_type=type_hints["package"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[str, typing.Any] = {
            "package": package,
        }
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def package(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#package Cluster#package}.'''
        result = self._values.get("package")
        assert result is not None, "Required property 'package' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.'''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterLibraryPypi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterLibraryPypiOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterLibraryPypiOutputReference",
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
            type_hints = typing.get_type_hints(ClusterLibraryPypiOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="packageInput")
    def package_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "packageInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="package")
    def package(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "package"))

    @package.setter
    def package(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryPypiOutputReference, "package").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "package", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryPypiOutputReference, "repo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterLibraryPypi]:
        return typing.cast(typing.Optional[ClusterLibraryPypi], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterLibraryPypi]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterLibraryPypiOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#create Cluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#delete Cluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#update Cluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#create Cluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#delete Cluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#update Cluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ClusterTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ClusterTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterWorkloadType",
    jsii_struct_bases=[],
    name_mapping={"clients": "clients"},
)
class ClusterWorkloadType:
    def __init__(
        self,
        *,
        clients: typing.Union["ClusterWorkloadTypeClients", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param clients: clients block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#clients Cluster#clients}
        '''
        if isinstance(clients, dict):
            clients = ClusterWorkloadTypeClients(**clients)
        if __debug__:
            type_hints = typing.get_type_hints(ClusterWorkloadType.__init__)
            check_type(argname="argument clients", value=clients, expected_type=type_hints["clients"])
        self._values: typing.Dict[str, typing.Any] = {
            "clients": clients,
        }

    @builtins.property
    def clients(self) -> "ClusterWorkloadTypeClients":
        '''clients block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#clients Cluster#clients}
        '''
        result = self._values.get("clients")
        assert result is not None, "Required property 'clients' is missing"
        return typing.cast("ClusterWorkloadTypeClients", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterWorkloadType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.cluster.ClusterWorkloadTypeClients",
    jsii_struct_bases=[],
    name_mapping={"jobs": "jobs", "notebooks": "notebooks"},
)
class ClusterWorkloadTypeClients:
    def __init__(
        self,
        *,
        jobs: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        notebooks: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param jobs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#jobs Cluster#jobs}.
        :param notebooks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#notebooks Cluster#notebooks}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClusterWorkloadTypeClients.__init__)
            check_type(argname="argument jobs", value=jobs, expected_type=type_hints["jobs"])
            check_type(argname="argument notebooks", value=notebooks, expected_type=type_hints["notebooks"])
        self._values: typing.Dict[str, typing.Any] = {}
        if jobs is not None:
            self._values["jobs"] = jobs
        if notebooks is not None:
            self._values["notebooks"] = notebooks

    @builtins.property
    def jobs(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#jobs Cluster#jobs}.'''
        result = self._values.get("jobs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def notebooks(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#notebooks Cluster#notebooks}.'''
        result = self._values.get("notebooks")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterWorkloadTypeClients(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterWorkloadTypeClientsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterWorkloadTypeClientsOutputReference",
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
            type_hints = typing.get_type_hints(ClusterWorkloadTypeClientsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetJobs")
    def reset_jobs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobs", []))

    @jsii.member(jsii_name="resetNotebooks")
    def reset_notebooks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotebooks", []))

    @builtins.property
    @jsii.member(jsii_name="jobsInput")
    def jobs_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "jobsInput"))

    @builtins.property
    @jsii.member(jsii_name="notebooksInput")
    def notebooks_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "notebooksInput"))

    @builtins.property
    @jsii.member(jsii_name="jobs")
    def jobs(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "jobs"))

    @jobs.setter
    def jobs(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterWorkloadTypeClientsOutputReference, "jobs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobs", value)

    @builtins.property
    @jsii.member(jsii_name="notebooks")
    def notebooks(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "notebooks"))

    @notebooks.setter
    def notebooks(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterWorkloadTypeClientsOutputReference, "notebooks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notebooks", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterWorkloadTypeClients]:
        return typing.cast(typing.Optional[ClusterWorkloadTypeClients], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ClusterWorkloadTypeClients],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterWorkloadTypeClientsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterWorkloadTypeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.cluster.ClusterWorkloadTypeOutputReference",
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
            type_hints = typing.get_type_hints(ClusterWorkloadTypeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClients")
    def put_clients(
        self,
        *,
        jobs: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        notebooks: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param jobs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#jobs Cluster#jobs}.
        :param notebooks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#notebooks Cluster#notebooks}.
        '''
        value = ClusterWorkloadTypeClients(jobs=jobs, notebooks=notebooks)

        return typing.cast(None, jsii.invoke(self, "putClients", [value]))

    @builtins.property
    @jsii.member(jsii_name="clients")
    def clients(self) -> ClusterWorkloadTypeClientsOutputReference:
        return typing.cast(ClusterWorkloadTypeClientsOutputReference, jsii.get(self, "clients"))

    @builtins.property
    @jsii.member(jsii_name="clientsInput")
    def clients_input(self) -> typing.Optional[ClusterWorkloadTypeClients]:
        return typing.cast(typing.Optional[ClusterWorkloadTypeClients], jsii.get(self, "clientsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterWorkloadType]:
        return typing.cast(typing.Optional[ClusterWorkloadType], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterWorkloadType]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClusterWorkloadTypeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Cluster",
    "ClusterAutoscale",
    "ClusterAutoscaleOutputReference",
    "ClusterAwsAttributes",
    "ClusterAwsAttributesOutputReference",
    "ClusterAzureAttributes",
    "ClusterAzureAttributesOutputReference",
    "ClusterClusterLogConf",
    "ClusterClusterLogConfDbfs",
    "ClusterClusterLogConfDbfsOutputReference",
    "ClusterClusterLogConfOutputReference",
    "ClusterClusterLogConfS3",
    "ClusterClusterLogConfS3OutputReference",
    "ClusterConfig",
    "ClusterDockerImage",
    "ClusterDockerImageBasicAuth",
    "ClusterDockerImageBasicAuthOutputReference",
    "ClusterDockerImageOutputReference",
    "ClusterGcpAttributes",
    "ClusterGcpAttributesOutputReference",
    "ClusterInitScripts",
    "ClusterInitScriptsDbfs",
    "ClusterInitScriptsDbfsOutputReference",
    "ClusterInitScriptsFile",
    "ClusterInitScriptsFileOutputReference",
    "ClusterInitScriptsGcs",
    "ClusterInitScriptsGcsOutputReference",
    "ClusterInitScriptsList",
    "ClusterInitScriptsOutputReference",
    "ClusterInitScriptsS3",
    "ClusterInitScriptsS3OutputReference",
    "ClusterLibrary",
    "ClusterLibraryCran",
    "ClusterLibraryCranOutputReference",
    "ClusterLibraryList",
    "ClusterLibraryMaven",
    "ClusterLibraryMavenOutputReference",
    "ClusterLibraryOutputReference",
    "ClusterLibraryPypi",
    "ClusterLibraryPypiOutputReference",
    "ClusterTimeouts",
    "ClusterTimeoutsOutputReference",
    "ClusterWorkloadType",
    "ClusterWorkloadTypeClients",
    "ClusterWorkloadTypeClientsOutputReference",
    "ClusterWorkloadTypeOutputReference",
]

publication.publish()
