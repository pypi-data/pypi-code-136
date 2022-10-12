'''
# `spotinst_elastigroup_azure`

Refer to the Terraform Registory for docs: [`spotinst_elastigroup_azure`](https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure).
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


class ElastigroupAzure(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzure",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure spotinst_elastigroup_azure}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        low_priority_sizes: typing.Sequence[builtins.str],
        name: builtins.str,
        network: typing.Union["ElastigroupAzureNetwork", typing.Dict[str, typing.Any]],
        od_sizes: typing.Sequence[builtins.str],
        product: builtins.str,
        region: builtins.str,
        resource_group_name: builtins.str,
        strategy: typing.Union["ElastigroupAzureStrategy", typing.Dict[str, typing.Any]],
        custom_data: typing.Optional[builtins.str] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        health_check: typing.Optional[typing.Union["ElastigroupAzureHealthCheck", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        image: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureImage", typing.Dict[str, typing.Any]]]]] = None,
        integration_kubernetes: typing.Optional[typing.Union["ElastigroupAzureIntegrationKubernetes", typing.Dict[str, typing.Any]]] = None,
        integration_multai_runtime: typing.Optional[typing.Union["ElastigroupAzureIntegrationMultaiRuntime", typing.Dict[str, typing.Any]]] = None,
        load_balancers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureLoadBalancers", typing.Dict[str, typing.Any]]]]] = None,
        login: typing.Optional[typing.Union["ElastigroupAzureLogin", typing.Dict[str, typing.Any]]] = None,
        managed_service_identities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureManagedServiceIdentities", typing.Dict[str, typing.Any]]]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        scaling_down_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureScalingDownPolicy", typing.Dict[str, typing.Any]]]]] = None,
        scaling_up_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureScalingUpPolicy", typing.Dict[str, typing.Any]]]]] = None,
        scheduled_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureScheduledTask", typing.Dict[str, typing.Any]]]]] = None,
        shutdown_script: typing.Optional[builtins.str] = None,
        update_policy: typing.Optional[typing.Union["ElastigroupAzureUpdatePolicy", typing.Dict[str, typing.Any]]] = None,
        user_data: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure spotinst_elastigroup_azure} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param low_priority_sizes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#low_priority_sizes ElastigroupAzure#low_priority_sizes}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#name ElastigroupAzure#name}.
        :param network: network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#network ElastigroupAzure#network}
        :param od_sizes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#od_sizes ElastigroupAzure#od_sizes}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#product ElastigroupAzure#product}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#region ElastigroupAzure#region}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#resource_group_name ElastigroupAzure#resource_group_name}.
        :param strategy: strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#strategy ElastigroupAzure#strategy}
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#custom_data ElastigroupAzure#custom_data}.
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#desired_capacity ElastigroupAzure#desired_capacity}.
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#health_check ElastigroupAzure#health_check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#id ElastigroupAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image: image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#image ElastigroupAzure#image}
        :param integration_kubernetes: integration_kubernetes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#integration_kubernetes ElastigroupAzure#integration_kubernetes}
        :param integration_multai_runtime: integration_multai_runtime block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#integration_multai_runtime ElastigroupAzure#integration_multai_runtime}
        :param load_balancers: load_balancers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#load_balancers ElastigroupAzure#load_balancers}
        :param login: login block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#login ElastigroupAzure#login}
        :param managed_service_identities: managed_service_identities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#managed_service_identities ElastigroupAzure#managed_service_identities}
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#max_size ElastigroupAzure#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#min_size ElastigroupAzure#min_size}.
        :param scaling_down_policy: scaling_down_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#scaling_down_policy ElastigroupAzure#scaling_down_policy}
        :param scaling_up_policy: scaling_up_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#scaling_up_policy ElastigroupAzure#scaling_up_policy}
        :param scheduled_task: scheduled_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#scheduled_task ElastigroupAzure#scheduled_task}
        :param shutdown_script: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#shutdown_script ElastigroupAzure#shutdown_script}.
        :param update_policy: update_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#update_policy ElastigroupAzure#update_policy}
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#user_data ElastigroupAzure#user_data}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzure.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ElastigroupAzureConfig(
            low_priority_sizes=low_priority_sizes,
            name=name,
            network=network,
            od_sizes=od_sizes,
            product=product,
            region=region,
            resource_group_name=resource_group_name,
            strategy=strategy,
            custom_data=custom_data,
            desired_capacity=desired_capacity,
            health_check=health_check,
            id=id,
            image=image,
            integration_kubernetes=integration_kubernetes,
            integration_multai_runtime=integration_multai_runtime,
            load_balancers=load_balancers,
            login=login,
            managed_service_identities=managed_service_identities,
            max_size=max_size,
            min_size=min_size,
            scaling_down_policy=scaling_down_policy,
            scaling_up_policy=scaling_up_policy,
            scheduled_task=scheduled_task,
            shutdown_script=shutdown_script,
            update_policy=update_policy,
            user_data=user_data,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putHealthCheck")
    def put_health_check(
        self,
        *,
        health_check_type: builtins.str,
        auto_healing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        grace_period: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param health_check_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#health_check_type ElastigroupAzure#health_check_type}.
        :param auto_healing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#auto_healing ElastigroupAzure#auto_healing}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#grace_period ElastigroupAzure#grace_period}.
        '''
        value = ElastigroupAzureHealthCheck(
            health_check_type=health_check_type,
            auto_healing=auto_healing,
            grace_period=grace_period,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthCheck", [value]))

    @jsii.member(jsii_name="putImage")
    def put_image(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureImage", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzure.put_image)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putImage", [value]))

    @jsii.member(jsii_name="putIntegrationKubernetes")
    def put_integration_kubernetes(self, *, cluster_identifier: builtins.str) -> None:
        '''
        :param cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#cluster_identifier ElastigroupAzure#cluster_identifier}.
        '''
        value = ElastigroupAzureIntegrationKubernetes(
            cluster_identifier=cluster_identifier
        )

        return typing.cast(None, jsii.invoke(self, "putIntegrationKubernetes", [value]))

    @jsii.member(jsii_name="putIntegrationMultaiRuntime")
    def put_integration_multai_runtime(self, *, deployment_id: builtins.str) -> None:
        '''
        :param deployment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#deployment_id ElastigroupAzure#deployment_id}.
        '''
        value = ElastigroupAzureIntegrationMultaiRuntime(deployment_id=deployment_id)

        return typing.cast(None, jsii.invoke(self, "putIntegrationMultaiRuntime", [value]))

    @jsii.member(jsii_name="putLoadBalancers")
    def put_load_balancers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureLoadBalancers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzure.put_load_balancers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLoadBalancers", [value]))

    @jsii.member(jsii_name="putLogin")
    def put_login(
        self,
        *,
        user_name: builtins.str,
        password: typing.Optional[builtins.str] = None,
        ssh_public_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#user_name ElastigroupAzure#user_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#password ElastigroupAzure#password}.
        :param ssh_public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#ssh_public_key ElastigroupAzure#ssh_public_key}.
        '''
        value = ElastigroupAzureLogin(
            user_name=user_name, password=password, ssh_public_key=ssh_public_key
        )

        return typing.cast(None, jsii.invoke(self, "putLogin", [value]))

    @jsii.member(jsii_name="putManagedServiceIdentities")
    def put_managed_service_identities(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureManagedServiceIdentities", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzure.put_managed_service_identities)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putManagedServiceIdentities", [value]))

    @jsii.member(jsii_name="putNetwork")
    def put_network(
        self,
        *,
        resource_group_name: builtins.str,
        subnet_name: builtins.str,
        virtual_network_name: builtins.str,
        additional_ip_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureNetworkAdditionalIpConfigs", typing.Dict[str, typing.Any]]]]] = None,
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#resource_group_name ElastigroupAzure#resource_group_name}.
        :param subnet_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#subnet_name ElastigroupAzure#subnet_name}.
        :param virtual_network_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#virtual_network_name ElastigroupAzure#virtual_network_name}.
        :param additional_ip_configs: additional_ip_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#additional_ip_configs ElastigroupAzure#additional_ip_configs}
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#assign_public_ip ElastigroupAzure#assign_public_ip}.
        '''
        value = ElastigroupAzureNetwork(
            resource_group_name=resource_group_name,
            subnet_name=subnet_name,
            virtual_network_name=virtual_network_name,
            additional_ip_configs=additional_ip_configs,
            assign_public_ip=assign_public_ip,
        )

        return typing.cast(None, jsii.invoke(self, "putNetwork", [value]))

    @jsii.member(jsii_name="putScalingDownPolicy")
    def put_scaling_down_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureScalingDownPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzure.put_scaling_down_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScalingDownPolicy", [value]))

    @jsii.member(jsii_name="putScalingUpPolicy")
    def put_scaling_up_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureScalingUpPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzure.put_scaling_up_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScalingUpPolicy", [value]))

    @jsii.member(jsii_name="putScheduledTask")
    def put_scheduled_task(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureScheduledTask", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzure.put_scheduled_task)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScheduledTask", [value]))

    @jsii.member(jsii_name="putStrategy")
    def put_strategy(
        self,
        *,
        draining_timeout: typing.Optional[jsii.Number] = None,
        low_priority_percentage: typing.Optional[jsii.Number] = None,
        od_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param draining_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#draining_timeout ElastigroupAzure#draining_timeout}.
        :param low_priority_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#low_priority_percentage ElastigroupAzure#low_priority_percentage}.
        :param od_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#od_count ElastigroupAzure#od_count}.
        '''
        value = ElastigroupAzureStrategy(
            draining_timeout=draining_timeout,
            low_priority_percentage=low_priority_percentage,
            od_count=od_count,
        )

        return typing.cast(None, jsii.invoke(self, "putStrategy", [value]))

    @jsii.member(jsii_name="putUpdatePolicy")
    def put_update_policy(
        self,
        *,
        should_roll: typing.Union[builtins.bool, cdktf.IResolvable],
        roll_config: typing.Optional[typing.Union["ElastigroupAzureUpdatePolicyRollConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param should_roll: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#should_roll ElastigroupAzure#should_roll}.
        :param roll_config: roll_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#roll_config ElastigroupAzure#roll_config}
        '''
        value = ElastigroupAzureUpdatePolicy(
            should_roll=should_roll, roll_config=roll_config
        )

        return typing.cast(None, jsii.invoke(self, "putUpdatePolicy", [value]))

    @jsii.member(jsii_name="resetCustomData")
    def reset_custom_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomData", []))

    @jsii.member(jsii_name="resetDesiredCapacity")
    def reset_desired_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredCapacity", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImage")
    def reset_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImage", []))

    @jsii.member(jsii_name="resetIntegrationKubernetes")
    def reset_integration_kubernetes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegrationKubernetes", []))

    @jsii.member(jsii_name="resetIntegrationMultaiRuntime")
    def reset_integration_multai_runtime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegrationMultaiRuntime", []))

    @jsii.member(jsii_name="resetLoadBalancers")
    def reset_load_balancers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancers", []))

    @jsii.member(jsii_name="resetLogin")
    def reset_login(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogin", []))

    @jsii.member(jsii_name="resetManagedServiceIdentities")
    def reset_managed_service_identities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedServiceIdentities", []))

    @jsii.member(jsii_name="resetMaxSize")
    def reset_max_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxSize", []))

    @jsii.member(jsii_name="resetMinSize")
    def reset_min_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinSize", []))

    @jsii.member(jsii_name="resetScalingDownPolicy")
    def reset_scaling_down_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScalingDownPolicy", []))

    @jsii.member(jsii_name="resetScalingUpPolicy")
    def reset_scaling_up_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScalingUpPolicy", []))

    @jsii.member(jsii_name="resetScheduledTask")
    def reset_scheduled_task(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduledTask", []))

    @jsii.member(jsii_name="resetShutdownScript")
    def reset_shutdown_script(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShutdownScript", []))

    @jsii.member(jsii_name="resetUpdatePolicy")
    def reset_update_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdatePolicy", []))

    @jsii.member(jsii_name="resetUserData")
    def reset_user_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserData", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> "ElastigroupAzureHealthCheckOutputReference":
        return typing.cast("ElastigroupAzureHealthCheckOutputReference", jsii.get(self, "healthCheck"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> "ElastigroupAzureImageList":
        return typing.cast("ElastigroupAzureImageList", jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="integrationKubernetes")
    def integration_kubernetes(
        self,
    ) -> "ElastigroupAzureIntegrationKubernetesOutputReference":
        return typing.cast("ElastigroupAzureIntegrationKubernetesOutputReference", jsii.get(self, "integrationKubernetes"))

    @builtins.property
    @jsii.member(jsii_name="integrationMultaiRuntime")
    def integration_multai_runtime(
        self,
    ) -> "ElastigroupAzureIntegrationMultaiRuntimeOutputReference":
        return typing.cast("ElastigroupAzureIntegrationMultaiRuntimeOutputReference", jsii.get(self, "integrationMultaiRuntime"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancers")
    def load_balancers(self) -> "ElastigroupAzureLoadBalancersList":
        return typing.cast("ElastigroupAzureLoadBalancersList", jsii.get(self, "loadBalancers"))

    @builtins.property
    @jsii.member(jsii_name="login")
    def login(self) -> "ElastigroupAzureLoginOutputReference":
        return typing.cast("ElastigroupAzureLoginOutputReference", jsii.get(self, "login"))

    @builtins.property
    @jsii.member(jsii_name="managedServiceIdentities")
    def managed_service_identities(
        self,
    ) -> "ElastigroupAzureManagedServiceIdentitiesList":
        return typing.cast("ElastigroupAzureManagedServiceIdentitiesList", jsii.get(self, "managedServiceIdentities"))

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> "ElastigroupAzureNetworkOutputReference":
        return typing.cast("ElastigroupAzureNetworkOutputReference", jsii.get(self, "network"))

    @builtins.property
    @jsii.member(jsii_name="scalingDownPolicy")
    def scaling_down_policy(self) -> "ElastigroupAzureScalingDownPolicyList":
        return typing.cast("ElastigroupAzureScalingDownPolicyList", jsii.get(self, "scalingDownPolicy"))

    @builtins.property
    @jsii.member(jsii_name="scalingUpPolicy")
    def scaling_up_policy(self) -> "ElastigroupAzureScalingUpPolicyList":
        return typing.cast("ElastigroupAzureScalingUpPolicyList", jsii.get(self, "scalingUpPolicy"))

    @builtins.property
    @jsii.member(jsii_name="scheduledTask")
    def scheduled_task(self) -> "ElastigroupAzureScheduledTaskList":
        return typing.cast("ElastigroupAzureScheduledTaskList", jsii.get(self, "scheduledTask"))

    @builtins.property
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> "ElastigroupAzureStrategyOutputReference":
        return typing.cast("ElastigroupAzureStrategyOutputReference", jsii.get(self, "strategy"))

    @builtins.property
    @jsii.member(jsii_name="updatePolicy")
    def update_policy(self) -> "ElastigroupAzureUpdatePolicyOutputReference":
        return typing.cast("ElastigroupAzureUpdatePolicyOutputReference", jsii.get(self, "updatePolicy"))

    @builtins.property
    @jsii.member(jsii_name="customDataInput")
    def custom_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDataInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredCapacityInput")
    def desired_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional["ElastigroupAzureHealthCheck"]:
        return typing.cast(typing.Optional["ElastigroupAzureHealthCheck"], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureImage"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureImage"]]], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationKubernetesInput")
    def integration_kubernetes_input(
        self,
    ) -> typing.Optional["ElastigroupAzureIntegrationKubernetes"]:
        return typing.cast(typing.Optional["ElastigroupAzureIntegrationKubernetes"], jsii.get(self, "integrationKubernetesInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationMultaiRuntimeInput")
    def integration_multai_runtime_input(
        self,
    ) -> typing.Optional["ElastigroupAzureIntegrationMultaiRuntime"]:
        return typing.cast(typing.Optional["ElastigroupAzureIntegrationMultaiRuntime"], jsii.get(self, "integrationMultaiRuntimeInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancersInput")
    def load_balancers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureLoadBalancers"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureLoadBalancers"]]], jsii.get(self, "loadBalancersInput"))

    @builtins.property
    @jsii.member(jsii_name="loginInput")
    def login_input(self) -> typing.Optional["ElastigroupAzureLogin"]:
        return typing.cast(typing.Optional["ElastigroupAzureLogin"], jsii.get(self, "loginInput"))

    @builtins.property
    @jsii.member(jsii_name="lowPrioritySizesInput")
    def low_priority_sizes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lowPrioritySizesInput"))

    @builtins.property
    @jsii.member(jsii_name="managedServiceIdentitiesInput")
    def managed_service_identities_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureManagedServiceIdentities"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureManagedServiceIdentities"]]], jsii.get(self, "managedServiceIdentitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSizeInput")
    def max_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="minSizeInput")
    def min_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional["ElastigroupAzureNetwork"]:
        return typing.cast(typing.Optional["ElastigroupAzureNetwork"], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="odSizesInput")
    def od_sizes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "odSizesInput"))

    @builtins.property
    @jsii.member(jsii_name="productInput")
    def product_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingDownPolicyInput")
    def scaling_down_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScalingDownPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScalingDownPolicy"]]], jsii.get(self, "scalingDownPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingUpPolicyInput")
    def scaling_up_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScalingUpPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScalingUpPolicy"]]], jsii.get(self, "scalingUpPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduledTaskInput")
    def scheduled_task_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScheduledTask"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScheduledTask"]]], jsii.get(self, "scheduledTaskInput"))

    @builtins.property
    @jsii.member(jsii_name="shutdownScriptInput")
    def shutdown_script_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shutdownScriptInput"))

    @builtins.property
    @jsii.member(jsii_name="strategyInput")
    def strategy_input(self) -> typing.Optional["ElastigroupAzureStrategy"]:
        return typing.cast(typing.Optional["ElastigroupAzureStrategy"], jsii.get(self, "strategyInput"))

    @builtins.property
    @jsii.member(jsii_name="updatePolicyInput")
    def update_policy_input(self) -> typing.Optional["ElastigroupAzureUpdatePolicy"]:
        return typing.cast(typing.Optional["ElastigroupAzureUpdatePolicy"], jsii.get(self, "updatePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="userDataInput")
    def user_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDataInput"))

    @builtins.property
    @jsii.member(jsii_name="customData")
    def custom_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customData"))

    @custom_data.setter
    def custom_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzure, "custom_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customData", value)

    @builtins.property
    @jsii.member(jsii_name="desiredCapacity")
    def desired_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredCapacity"))

    @desired_capacity.setter
    def desired_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzure, "desired_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzure, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="lowPrioritySizes")
    def low_priority_sizes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lowPrioritySizes"))

    @low_priority_sizes.setter
    def low_priority_sizes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzure, "low_priority_sizes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lowPrioritySizes", value)

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSize"))

    @max_size.setter
    def max_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzure, "max_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSize", value)

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzure, "min_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzure, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="odSizes")
    def od_sizes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "odSizes"))

    @od_sizes.setter
    def od_sizes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzure, "od_sizes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "odSizes", value)

    @builtins.property
    @jsii.member(jsii_name="product")
    def product(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "product"))

    @product.setter
    def product(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzure, "product").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "product", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzure, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzure, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="shutdownScript")
    def shutdown_script(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shutdownScript"))

    @shutdown_script.setter
    def shutdown_script(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzure, "shutdown_script").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shutdownScript", value)

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzure, "user_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userData", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "low_priority_sizes": "lowPrioritySizes",
        "name": "name",
        "network": "network",
        "od_sizes": "odSizes",
        "product": "product",
        "region": "region",
        "resource_group_name": "resourceGroupName",
        "strategy": "strategy",
        "custom_data": "customData",
        "desired_capacity": "desiredCapacity",
        "health_check": "healthCheck",
        "id": "id",
        "image": "image",
        "integration_kubernetes": "integrationKubernetes",
        "integration_multai_runtime": "integrationMultaiRuntime",
        "load_balancers": "loadBalancers",
        "login": "login",
        "managed_service_identities": "managedServiceIdentities",
        "max_size": "maxSize",
        "min_size": "minSize",
        "scaling_down_policy": "scalingDownPolicy",
        "scaling_up_policy": "scalingUpPolicy",
        "scheduled_task": "scheduledTask",
        "shutdown_script": "shutdownScript",
        "update_policy": "updatePolicy",
        "user_data": "userData",
    },
)
class ElastigroupAzureConfig(cdktf.TerraformMetaArguments):
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
        low_priority_sizes: typing.Sequence[builtins.str],
        name: builtins.str,
        network: typing.Union["ElastigroupAzureNetwork", typing.Dict[str, typing.Any]],
        od_sizes: typing.Sequence[builtins.str],
        product: builtins.str,
        region: builtins.str,
        resource_group_name: builtins.str,
        strategy: typing.Union["ElastigroupAzureStrategy", typing.Dict[str, typing.Any]],
        custom_data: typing.Optional[builtins.str] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        health_check: typing.Optional[typing.Union["ElastigroupAzureHealthCheck", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        image: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureImage", typing.Dict[str, typing.Any]]]]] = None,
        integration_kubernetes: typing.Optional[typing.Union["ElastigroupAzureIntegrationKubernetes", typing.Dict[str, typing.Any]]] = None,
        integration_multai_runtime: typing.Optional[typing.Union["ElastigroupAzureIntegrationMultaiRuntime", typing.Dict[str, typing.Any]]] = None,
        load_balancers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureLoadBalancers", typing.Dict[str, typing.Any]]]]] = None,
        login: typing.Optional[typing.Union["ElastigroupAzureLogin", typing.Dict[str, typing.Any]]] = None,
        managed_service_identities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureManagedServiceIdentities", typing.Dict[str, typing.Any]]]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        scaling_down_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureScalingDownPolicy", typing.Dict[str, typing.Any]]]]] = None,
        scaling_up_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureScalingUpPolicy", typing.Dict[str, typing.Any]]]]] = None,
        scheduled_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureScheduledTask", typing.Dict[str, typing.Any]]]]] = None,
        shutdown_script: typing.Optional[builtins.str] = None,
        update_policy: typing.Optional[typing.Union["ElastigroupAzureUpdatePolicy", typing.Dict[str, typing.Any]]] = None,
        user_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param low_priority_sizes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#low_priority_sizes ElastigroupAzure#low_priority_sizes}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#name ElastigroupAzure#name}.
        :param network: network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#network ElastigroupAzure#network}
        :param od_sizes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#od_sizes ElastigroupAzure#od_sizes}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#product ElastigroupAzure#product}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#region ElastigroupAzure#region}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#resource_group_name ElastigroupAzure#resource_group_name}.
        :param strategy: strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#strategy ElastigroupAzure#strategy}
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#custom_data ElastigroupAzure#custom_data}.
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#desired_capacity ElastigroupAzure#desired_capacity}.
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#health_check ElastigroupAzure#health_check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#id ElastigroupAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image: image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#image ElastigroupAzure#image}
        :param integration_kubernetes: integration_kubernetes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#integration_kubernetes ElastigroupAzure#integration_kubernetes}
        :param integration_multai_runtime: integration_multai_runtime block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#integration_multai_runtime ElastigroupAzure#integration_multai_runtime}
        :param load_balancers: load_balancers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#load_balancers ElastigroupAzure#load_balancers}
        :param login: login block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#login ElastigroupAzure#login}
        :param managed_service_identities: managed_service_identities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#managed_service_identities ElastigroupAzure#managed_service_identities}
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#max_size ElastigroupAzure#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#min_size ElastigroupAzure#min_size}.
        :param scaling_down_policy: scaling_down_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#scaling_down_policy ElastigroupAzure#scaling_down_policy}
        :param scaling_up_policy: scaling_up_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#scaling_up_policy ElastigroupAzure#scaling_up_policy}
        :param scheduled_task: scheduled_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#scheduled_task ElastigroupAzure#scheduled_task}
        :param shutdown_script: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#shutdown_script ElastigroupAzure#shutdown_script}.
        :param update_policy: update_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#update_policy ElastigroupAzure#update_policy}
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#user_data ElastigroupAzure#user_data}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(network, dict):
            network = ElastigroupAzureNetwork(**network)
        if isinstance(strategy, dict):
            strategy = ElastigroupAzureStrategy(**strategy)
        if isinstance(health_check, dict):
            health_check = ElastigroupAzureHealthCheck(**health_check)
        if isinstance(integration_kubernetes, dict):
            integration_kubernetes = ElastigroupAzureIntegrationKubernetes(**integration_kubernetes)
        if isinstance(integration_multai_runtime, dict):
            integration_multai_runtime = ElastigroupAzureIntegrationMultaiRuntime(**integration_multai_runtime)
        if isinstance(login, dict):
            login = ElastigroupAzureLogin(**login)
        if isinstance(update_policy, dict):
            update_policy = ElastigroupAzureUpdatePolicy(**update_policy)
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument low_priority_sizes", value=low_priority_sizes, expected_type=type_hints["low_priority_sizes"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument od_sizes", value=od_sizes, expected_type=type_hints["od_sizes"])
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument strategy", value=strategy, expected_type=type_hints["strategy"])
            check_type(argname="argument custom_data", value=custom_data, expected_type=type_hints["custom_data"])
            check_type(argname="argument desired_capacity", value=desired_capacity, expected_type=type_hints["desired_capacity"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument integration_kubernetes", value=integration_kubernetes, expected_type=type_hints["integration_kubernetes"])
            check_type(argname="argument integration_multai_runtime", value=integration_multai_runtime, expected_type=type_hints["integration_multai_runtime"])
            check_type(argname="argument load_balancers", value=load_balancers, expected_type=type_hints["load_balancers"])
            check_type(argname="argument login", value=login, expected_type=type_hints["login"])
            check_type(argname="argument managed_service_identities", value=managed_service_identities, expected_type=type_hints["managed_service_identities"])
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument scaling_down_policy", value=scaling_down_policy, expected_type=type_hints["scaling_down_policy"])
            check_type(argname="argument scaling_up_policy", value=scaling_up_policy, expected_type=type_hints["scaling_up_policy"])
            check_type(argname="argument scheduled_task", value=scheduled_task, expected_type=type_hints["scheduled_task"])
            check_type(argname="argument shutdown_script", value=shutdown_script, expected_type=type_hints["shutdown_script"])
            check_type(argname="argument update_policy", value=update_policy, expected_type=type_hints["update_policy"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
        self._values: typing.Dict[str, typing.Any] = {
            "low_priority_sizes": low_priority_sizes,
            "name": name,
            "network": network,
            "od_sizes": od_sizes,
            "product": product,
            "region": region,
            "resource_group_name": resource_group_name,
            "strategy": strategy,
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
        if custom_data is not None:
            self._values["custom_data"] = custom_data
        if desired_capacity is not None:
            self._values["desired_capacity"] = desired_capacity
        if health_check is not None:
            self._values["health_check"] = health_check
        if id is not None:
            self._values["id"] = id
        if image is not None:
            self._values["image"] = image
        if integration_kubernetes is not None:
            self._values["integration_kubernetes"] = integration_kubernetes
        if integration_multai_runtime is not None:
            self._values["integration_multai_runtime"] = integration_multai_runtime
        if load_balancers is not None:
            self._values["load_balancers"] = load_balancers
        if login is not None:
            self._values["login"] = login
        if managed_service_identities is not None:
            self._values["managed_service_identities"] = managed_service_identities
        if max_size is not None:
            self._values["max_size"] = max_size
        if min_size is not None:
            self._values["min_size"] = min_size
        if scaling_down_policy is not None:
            self._values["scaling_down_policy"] = scaling_down_policy
        if scaling_up_policy is not None:
            self._values["scaling_up_policy"] = scaling_up_policy
        if scheduled_task is not None:
            self._values["scheduled_task"] = scheduled_task
        if shutdown_script is not None:
            self._values["shutdown_script"] = shutdown_script
        if update_policy is not None:
            self._values["update_policy"] = update_policy
        if user_data is not None:
            self._values["user_data"] = user_data

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
    def low_priority_sizes(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#low_priority_sizes ElastigroupAzure#low_priority_sizes}.'''
        result = self._values.get("low_priority_sizes")
        assert result is not None, "Required property 'low_priority_sizes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#name ElastigroupAzure#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network(self) -> "ElastigroupAzureNetwork":
        '''network block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#network ElastigroupAzure#network}
        '''
        result = self._values.get("network")
        assert result is not None, "Required property 'network' is missing"
        return typing.cast("ElastigroupAzureNetwork", result)

    @builtins.property
    def od_sizes(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#od_sizes ElastigroupAzure#od_sizes}.'''
        result = self._values.get("od_sizes")
        assert result is not None, "Required property 'od_sizes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def product(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#product ElastigroupAzure#product}.'''
        result = self._values.get("product")
        assert result is not None, "Required property 'product' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#region ElastigroupAzure#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#resource_group_name ElastigroupAzure#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def strategy(self) -> "ElastigroupAzureStrategy":
        '''strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#strategy ElastigroupAzure#strategy}
        '''
        result = self._values.get("strategy")
        assert result is not None, "Required property 'strategy' is missing"
        return typing.cast("ElastigroupAzureStrategy", result)

    @builtins.property
    def custom_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#custom_data ElastigroupAzure#custom_data}.'''
        result = self._values.get("custom_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def desired_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#desired_capacity ElastigroupAzure#desired_capacity}.'''
        result = self._values.get("desired_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check(self) -> typing.Optional["ElastigroupAzureHealthCheck"]:
        '''health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#health_check ElastigroupAzure#health_check}
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional["ElastigroupAzureHealthCheck"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#id ElastigroupAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureImage"]]]:
        '''image block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#image ElastigroupAzure#image}
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureImage"]]], result)

    @builtins.property
    def integration_kubernetes(
        self,
    ) -> typing.Optional["ElastigroupAzureIntegrationKubernetes"]:
        '''integration_kubernetes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#integration_kubernetes ElastigroupAzure#integration_kubernetes}
        '''
        result = self._values.get("integration_kubernetes")
        return typing.cast(typing.Optional["ElastigroupAzureIntegrationKubernetes"], result)

    @builtins.property
    def integration_multai_runtime(
        self,
    ) -> typing.Optional["ElastigroupAzureIntegrationMultaiRuntime"]:
        '''integration_multai_runtime block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#integration_multai_runtime ElastigroupAzure#integration_multai_runtime}
        '''
        result = self._values.get("integration_multai_runtime")
        return typing.cast(typing.Optional["ElastigroupAzureIntegrationMultaiRuntime"], result)

    @builtins.property
    def load_balancers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureLoadBalancers"]]]:
        '''load_balancers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#load_balancers ElastigroupAzure#load_balancers}
        '''
        result = self._values.get("load_balancers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureLoadBalancers"]]], result)

    @builtins.property
    def login(self) -> typing.Optional["ElastigroupAzureLogin"]:
        '''login block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#login ElastigroupAzure#login}
        '''
        result = self._values.get("login")
        return typing.cast(typing.Optional["ElastigroupAzureLogin"], result)

    @builtins.property
    def managed_service_identities(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureManagedServiceIdentities"]]]:
        '''managed_service_identities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#managed_service_identities ElastigroupAzure#managed_service_identities}
        '''
        result = self._values.get("managed_service_identities")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureManagedServiceIdentities"]]], result)

    @builtins.property
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#max_size ElastigroupAzure#max_size}.'''
        result = self._values.get("max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#min_size ElastigroupAzure#min_size}.'''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scaling_down_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScalingDownPolicy"]]]:
        '''scaling_down_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#scaling_down_policy ElastigroupAzure#scaling_down_policy}
        '''
        result = self._values.get("scaling_down_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScalingDownPolicy"]]], result)

    @builtins.property
    def scaling_up_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScalingUpPolicy"]]]:
        '''scaling_up_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#scaling_up_policy ElastigroupAzure#scaling_up_policy}
        '''
        result = self._values.get("scaling_up_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScalingUpPolicy"]]], result)

    @builtins.property
    def scheduled_task(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScheduledTask"]]]:
        '''scheduled_task block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#scheduled_task ElastigroupAzure#scheduled_task}
        '''
        result = self._values.get("scheduled_task")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScheduledTask"]]], result)

    @builtins.property
    def shutdown_script(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#shutdown_script ElastigroupAzure#shutdown_script}.'''
        result = self._values.get("shutdown_script")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update_policy(self) -> typing.Optional["ElastigroupAzureUpdatePolicy"]:
        '''update_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#update_policy ElastigroupAzure#update_policy}
        '''
        result = self._values.get("update_policy")
        return typing.cast(typing.Optional["ElastigroupAzureUpdatePolicy"], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#user_data ElastigroupAzure#user_data}.'''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureHealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "health_check_type": "healthCheckType",
        "auto_healing": "autoHealing",
        "grace_period": "gracePeriod",
    },
)
class ElastigroupAzureHealthCheck:
    def __init__(
        self,
        *,
        health_check_type: builtins.str,
        auto_healing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        grace_period: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param health_check_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#health_check_type ElastigroupAzure#health_check_type}.
        :param auto_healing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#auto_healing ElastigroupAzure#auto_healing}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#grace_period ElastigroupAzure#grace_period}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureHealthCheck.__init__)
            check_type(argname="argument health_check_type", value=health_check_type, expected_type=type_hints["health_check_type"])
            check_type(argname="argument auto_healing", value=auto_healing, expected_type=type_hints["auto_healing"])
            check_type(argname="argument grace_period", value=grace_period, expected_type=type_hints["grace_period"])
        self._values: typing.Dict[str, typing.Any] = {
            "health_check_type": health_check_type,
        }
        if auto_healing is not None:
            self._values["auto_healing"] = auto_healing
        if grace_period is not None:
            self._values["grace_period"] = grace_period

    @builtins.property
    def health_check_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#health_check_type ElastigroupAzure#health_check_type}.'''
        result = self._values.get("health_check_type")
        assert result is not None, "Required property 'health_check_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_healing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#auto_healing ElastigroupAzure#auto_healing}.'''
        result = self._values.get("auto_healing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def grace_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#grace_period ElastigroupAzure#grace_period}.'''
        result = self._values.get("grace_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureHealthCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureHealthCheckOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureHealthCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAutoHealing")
    def reset_auto_healing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoHealing", []))

    @jsii.member(jsii_name="resetGracePeriod")
    def reset_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGracePeriod", []))

    @builtins.property
    @jsii.member(jsii_name="autoHealingInput")
    def auto_healing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoHealingInput"))

    @builtins.property
    @jsii.member(jsii_name="gracePeriodInput")
    def grace_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gracePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckTypeInput")
    def health_check_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="autoHealing")
    def auto_healing(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoHealing"))

    @auto_healing.setter
    def auto_healing(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureHealthCheckOutputReference, "auto_healing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHealing", value)

    @builtins.property
    @jsii.member(jsii_name="gracePeriod")
    def grace_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gracePeriod"))

    @grace_period.setter
    def grace_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureHealthCheckOutputReference, "grace_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckType")
    def health_check_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckType"))

    @health_check_type.setter
    def health_check_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureHealthCheckOutputReference, "health_check_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastigroupAzureHealthCheck]:
        return typing.cast(typing.Optional[ElastigroupAzureHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastigroupAzureHealthCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureHealthCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureImage",
    jsii_struct_bases=[],
    name_mapping={"custom": "custom", "marketplace": "marketplace"},
)
class ElastigroupAzureImage:
    def __init__(
        self,
        *,
        custom: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureImageCustom", typing.Dict[str, typing.Any]]]]] = None,
        marketplace: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureImageMarketplace", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param custom: custom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#custom ElastigroupAzure#custom}
        :param marketplace: marketplace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#marketplace ElastigroupAzure#marketplace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureImage.__init__)
            check_type(argname="argument custom", value=custom, expected_type=type_hints["custom"])
            check_type(argname="argument marketplace", value=marketplace, expected_type=type_hints["marketplace"])
        self._values: typing.Dict[str, typing.Any] = {}
        if custom is not None:
            self._values["custom"] = custom
        if marketplace is not None:
            self._values["marketplace"] = marketplace

    @builtins.property
    def custom(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureImageCustom"]]]:
        '''custom block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#custom ElastigroupAzure#custom}
        '''
        result = self._values.get("custom")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureImageCustom"]]], result)

    @builtins.property
    def marketplace(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureImageMarketplace"]]]:
        '''marketplace block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#marketplace ElastigroupAzure#marketplace}
        '''
        result = self._values.get("marketplace")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureImageMarketplace"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureImageCustom",
    jsii_struct_bases=[],
    name_mapping={
        "image_name": "imageName",
        "resource_group_name": "resourceGroupName",
    },
)
class ElastigroupAzureImageCustom:
    def __init__(
        self,
        *,
        image_name: builtins.str,
        resource_group_name: builtins.str,
    ) -> None:
        '''
        :param image_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#image_name ElastigroupAzure#image_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#resource_group_name ElastigroupAzure#resource_group_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureImageCustom.__init__)
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "image_name": image_name,
            "resource_group_name": resource_group_name,
        }

    @builtins.property
    def image_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#image_name ElastigroupAzure#image_name}.'''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#resource_group_name ElastigroupAzure#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureImageCustom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureImageCustomList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureImageCustomList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureImageCustomList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ElastigroupAzureImageCustomOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureImageCustomList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureImageCustomOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageCustomList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageCustomList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageCustomList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureImageCustom]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureImageCustom]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureImageCustom]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageCustomList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureImageCustomOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureImageCustomOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureImageCustomOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="imageNameInput")
    def image_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageCustomOutputReference, "image_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageCustomOutputReference, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureImageCustom, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureImageCustom, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureImageCustom, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageCustomOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureImageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureImageList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureImageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ElastigroupAzureImageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureImageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureImageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureImage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureImage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureImage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureImageMarketplace",
    jsii_struct_bases=[],
    name_mapping={"offer": "offer", "publisher": "publisher", "sku": "sku"},
)
class ElastigroupAzureImageMarketplace:
    def __init__(
        self,
        *,
        offer: builtins.str,
        publisher: builtins.str,
        sku: builtins.str,
    ) -> None:
        '''
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#offer ElastigroupAzure#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#publisher ElastigroupAzure#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#sku ElastigroupAzure#sku}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureImageMarketplace.__init__)
            check_type(argname="argument offer", value=offer, expected_type=type_hints["offer"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
        self._values: typing.Dict[str, typing.Any] = {
            "offer": offer,
            "publisher": publisher,
            "sku": sku,
        }

    @builtins.property
    def offer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#offer ElastigroupAzure#offer}.'''
        result = self._values.get("offer")
        assert result is not None, "Required property 'offer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#publisher ElastigroupAzure#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#sku ElastigroupAzure#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureImageMarketplace(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureImageMarketplaceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureImageMarketplaceList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureImageMarketplaceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupAzureImageMarketplaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureImageMarketplaceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureImageMarketplaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageMarketplaceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageMarketplaceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageMarketplaceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureImageMarketplace]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureImageMarketplace]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureImageMarketplace]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageMarketplaceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureImageMarketplaceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureImageMarketplaceOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureImageMarketplaceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="offerInput")
    def offer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "offerInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherInput")
    def publisher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="offer")
    def offer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "offer"))

    @offer.setter
    def offer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageMarketplaceOutputReference, "offer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offer", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageMarketplaceOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageMarketplaceOutputReference, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureImageMarketplace, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureImageMarketplace, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureImageMarketplace, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageMarketplaceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureImageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureImageOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureImageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCustom")
    def put_custom(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupAzureImageCustom, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureImageOutputReference.put_custom)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustom", [value]))

    @jsii.member(jsii_name="putMarketplace")
    def put_marketplace(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupAzureImageMarketplace, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureImageOutputReference.put_marketplace)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMarketplace", [value]))

    @jsii.member(jsii_name="resetCustom")
    def reset_custom(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustom", []))

    @jsii.member(jsii_name="resetMarketplace")
    def reset_marketplace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMarketplace", []))

    @builtins.property
    @jsii.member(jsii_name="custom")
    def custom(self) -> ElastigroupAzureImageCustomList:
        return typing.cast(ElastigroupAzureImageCustomList, jsii.get(self, "custom"))

    @builtins.property
    @jsii.member(jsii_name="marketplace")
    def marketplace(self) -> ElastigroupAzureImageMarketplaceList:
        return typing.cast(ElastigroupAzureImageMarketplaceList, jsii.get(self, "marketplace"))

    @builtins.property
    @jsii.member(jsii_name="customInput")
    def custom_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureImageCustom]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureImageCustom]]], jsii.get(self, "customInput"))

    @builtins.property
    @jsii.member(jsii_name="marketplaceInput")
    def marketplace_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureImageMarketplace]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureImageMarketplace]]], jsii.get(self, "marketplaceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureImage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureImage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureImage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureImageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureIntegrationKubernetes",
    jsii_struct_bases=[],
    name_mapping={"cluster_identifier": "clusterIdentifier"},
)
class ElastigroupAzureIntegrationKubernetes:
    def __init__(self, *, cluster_identifier: builtins.str) -> None:
        '''
        :param cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#cluster_identifier ElastigroupAzure#cluster_identifier}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureIntegrationKubernetes.__init__)
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_identifier": cluster_identifier,
        }

    @builtins.property
    def cluster_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#cluster_identifier ElastigroupAzure#cluster_identifier}.'''
        result = self._values.get("cluster_identifier")
        assert result is not None, "Required property 'cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureIntegrationKubernetes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureIntegrationKubernetesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureIntegrationKubernetesOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureIntegrationKubernetesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifierInput")
    def cluster_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifier"))

    @cluster_identifier.setter
    def cluster_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureIntegrationKubernetesOutputReference, "cluster_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastigroupAzureIntegrationKubernetes]:
        return typing.cast(typing.Optional[ElastigroupAzureIntegrationKubernetes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastigroupAzureIntegrationKubernetes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureIntegrationKubernetesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureIntegrationMultaiRuntime",
    jsii_struct_bases=[],
    name_mapping={"deployment_id": "deploymentId"},
)
class ElastigroupAzureIntegrationMultaiRuntime:
    def __init__(self, *, deployment_id: builtins.str) -> None:
        '''
        :param deployment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#deployment_id ElastigroupAzure#deployment_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureIntegrationMultaiRuntime.__init__)
            check_type(argname="argument deployment_id", value=deployment_id, expected_type=type_hints["deployment_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "deployment_id": deployment_id,
        }

    @builtins.property
    def deployment_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#deployment_id ElastigroupAzure#deployment_id}.'''
        result = self._values.get("deployment_id")
        assert result is not None, "Required property 'deployment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureIntegrationMultaiRuntime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureIntegrationMultaiRuntimeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureIntegrationMultaiRuntimeOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureIntegrationMultaiRuntimeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="deploymentIdInput")
    def deployment_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentId")
    def deployment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentId"))

    @deployment_id.setter
    def deployment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureIntegrationMultaiRuntimeOutputReference, "deployment_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElastigroupAzureIntegrationMultaiRuntime]:
        return typing.cast(typing.Optional[ElastigroupAzureIntegrationMultaiRuntime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastigroupAzureIntegrationMultaiRuntime],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureIntegrationMultaiRuntimeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureLoadBalancers",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "auto_weight": "autoWeight",
        "balancer_id": "balancerId",
        "target_set_id": "targetSetId",
    },
)
class ElastigroupAzureLoadBalancers:
    def __init__(
        self,
        *,
        type: builtins.str,
        auto_weight: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        balancer_id: typing.Optional[builtins.str] = None,
        target_set_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#type ElastigroupAzure#type}.
        :param auto_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#auto_weight ElastigroupAzure#auto_weight}.
        :param balancer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#balancer_id ElastigroupAzure#balancer_id}.
        :param target_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#target_set_id ElastigroupAzure#target_set_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureLoadBalancers.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument auto_weight", value=auto_weight, expected_type=type_hints["auto_weight"])
            check_type(argname="argument balancer_id", value=balancer_id, expected_type=type_hints["balancer_id"])
            check_type(argname="argument target_set_id", value=target_set_id, expected_type=type_hints["target_set_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if auto_weight is not None:
            self._values["auto_weight"] = auto_weight
        if balancer_id is not None:
            self._values["balancer_id"] = balancer_id
        if target_set_id is not None:
            self._values["target_set_id"] = target_set_id

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#type ElastigroupAzure#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_weight(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#auto_weight ElastigroupAzure#auto_weight}.'''
        result = self._values.get("auto_weight")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def balancer_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#balancer_id ElastigroupAzure#balancer_id}.'''
        result = self._values.get("balancer_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#target_set_id ElastigroupAzure#target_set_id}.'''
        result = self._values.get("target_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureLoadBalancers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureLoadBalancersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureLoadBalancersList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureLoadBalancersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ElastigroupAzureLoadBalancersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureLoadBalancersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureLoadBalancersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureLoadBalancersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureLoadBalancersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureLoadBalancersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureLoadBalancers]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureLoadBalancers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureLoadBalancers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureLoadBalancersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureLoadBalancersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureLoadBalancersOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureLoadBalancersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAutoWeight")
    def reset_auto_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoWeight", []))

    @jsii.member(jsii_name="resetBalancerId")
    def reset_balancer_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBalancerId", []))

    @jsii.member(jsii_name="resetTargetSetId")
    def reset_target_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetSetId", []))

    @builtins.property
    @jsii.member(jsii_name="autoWeightInput")
    def auto_weight_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoWeightInput"))

    @builtins.property
    @jsii.member(jsii_name="balancerIdInput")
    def balancer_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "balancerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="targetSetIdInput")
    def target_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="autoWeight")
    def auto_weight(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoWeight"))

    @auto_weight.setter
    def auto_weight(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureLoadBalancersOutputReference, "auto_weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoWeight", value)

    @builtins.property
    @jsii.member(jsii_name="balancerId")
    def balancer_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "balancerId"))

    @balancer_id.setter
    def balancer_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureLoadBalancersOutputReference, "balancer_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "balancerId", value)

    @builtins.property
    @jsii.member(jsii_name="targetSetId")
    def target_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetSetId"))

    @target_set_id.setter
    def target_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureLoadBalancersOutputReference, "target_set_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetSetId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureLoadBalancersOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureLoadBalancers, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureLoadBalancers, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureLoadBalancers, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureLoadBalancersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureLogin",
    jsii_struct_bases=[],
    name_mapping={
        "user_name": "userName",
        "password": "password",
        "ssh_public_key": "sshPublicKey",
    },
)
class ElastigroupAzureLogin:
    def __init__(
        self,
        *,
        user_name: builtins.str,
        password: typing.Optional[builtins.str] = None,
        ssh_public_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#user_name ElastigroupAzure#user_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#password ElastigroupAzure#password}.
        :param ssh_public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#ssh_public_key ElastigroupAzure#ssh_public_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureLogin.__init__)
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument ssh_public_key", value=ssh_public_key, expected_type=type_hints["ssh_public_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "user_name": user_name,
        }
        if password is not None:
            self._values["password"] = password
        if ssh_public_key is not None:
            self._values["ssh_public_key"] = ssh_public_key

    @builtins.property
    def user_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#user_name ElastigroupAzure#user_name}.'''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#password ElastigroupAzure#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssh_public_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#ssh_public_key ElastigroupAzure#ssh_public_key}.'''
        result = self._values.get("ssh_public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureLogin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureLoginOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureLoginOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureLoginOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetSshPublicKey")
    def reset_ssh_public_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshPublicKey", []))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeyInput")
    def ssh_public_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshPublicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameInput")
    def user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureLoginOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="sshPublicKey")
    def ssh_public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshPublicKey"))

    @ssh_public_key.setter
    def ssh_public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureLoginOutputReference, "ssh_public_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicKey", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureLoginOutputReference, "user_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastigroupAzureLogin]:
        return typing.cast(typing.Optional[ElastigroupAzureLogin], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ElastigroupAzureLogin]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureLoginOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureManagedServiceIdentities",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "resource_group_name": "resourceGroupName"},
)
class ElastigroupAzureManagedServiceIdentities:
    def __init__(
        self,
        *,
        name: builtins.str,
        resource_group_name: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#name ElastigroupAzure#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#resource_group_name ElastigroupAzure#resource_group_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureManagedServiceIdentities.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "resource_group_name": resource_group_name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#name ElastigroupAzure#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#resource_group_name ElastigroupAzure#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureManagedServiceIdentities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureManagedServiceIdentitiesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureManagedServiceIdentitiesList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureManagedServiceIdentitiesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupAzureManagedServiceIdentitiesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureManagedServiceIdentitiesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureManagedServiceIdentitiesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureManagedServiceIdentitiesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureManagedServiceIdentitiesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureManagedServiceIdentitiesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureManagedServiceIdentities]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureManagedServiceIdentities]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureManagedServiceIdentities]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureManagedServiceIdentitiesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureManagedServiceIdentitiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureManagedServiceIdentitiesOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureManagedServiceIdentitiesOutputReference.__init__)
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
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureManagedServiceIdentitiesOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureManagedServiceIdentitiesOutputReference, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureManagedServiceIdentities, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureManagedServiceIdentities, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureManagedServiceIdentities, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureManagedServiceIdentitiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureNetwork",
    jsii_struct_bases=[],
    name_mapping={
        "resource_group_name": "resourceGroupName",
        "subnet_name": "subnetName",
        "virtual_network_name": "virtualNetworkName",
        "additional_ip_configs": "additionalIpConfigs",
        "assign_public_ip": "assignPublicIp",
    },
)
class ElastigroupAzureNetwork:
    def __init__(
        self,
        *,
        resource_group_name: builtins.str,
        subnet_name: builtins.str,
        virtual_network_name: builtins.str,
        additional_ip_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureNetworkAdditionalIpConfigs", typing.Dict[str, typing.Any]]]]] = None,
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#resource_group_name ElastigroupAzure#resource_group_name}.
        :param subnet_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#subnet_name ElastigroupAzure#subnet_name}.
        :param virtual_network_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#virtual_network_name ElastigroupAzure#virtual_network_name}.
        :param additional_ip_configs: additional_ip_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#additional_ip_configs ElastigroupAzure#additional_ip_configs}
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#assign_public_ip ElastigroupAzure#assign_public_ip}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureNetwork.__init__)
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument subnet_name", value=subnet_name, expected_type=type_hints["subnet_name"])
            check_type(argname="argument virtual_network_name", value=virtual_network_name, expected_type=type_hints["virtual_network_name"])
            check_type(argname="argument additional_ip_configs", value=additional_ip_configs, expected_type=type_hints["additional_ip_configs"])
            check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource_group_name": resource_group_name,
            "subnet_name": subnet_name,
            "virtual_network_name": virtual_network_name,
        }
        if additional_ip_configs is not None:
            self._values["additional_ip_configs"] = additional_ip_configs
        if assign_public_ip is not None:
            self._values["assign_public_ip"] = assign_public_ip

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#resource_group_name ElastigroupAzure#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#subnet_name ElastigroupAzure#subnet_name}.'''
        result = self._values.get("subnet_name")
        assert result is not None, "Required property 'subnet_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_network_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#virtual_network_name ElastigroupAzure#virtual_network_name}.'''
        result = self._values.get("virtual_network_name")
        assert result is not None, "Required property 'virtual_network_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_ip_configs(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureNetworkAdditionalIpConfigs"]]]:
        '''additional_ip_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#additional_ip_configs ElastigroupAzure#additional_ip_configs}
        '''
        result = self._values.get("additional_ip_configs")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureNetworkAdditionalIpConfigs"]]], result)

    @builtins.property
    def assign_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#assign_public_ip ElastigroupAzure#assign_public_ip}.'''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureNetwork(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureNetworkAdditionalIpConfigs",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "private_ip_version": "privateIpVersion"},
)
class ElastigroupAzureNetworkAdditionalIpConfigs:
    def __init__(
        self,
        *,
        name: builtins.str,
        private_ip_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#name ElastigroupAzure#name}.
        :param private_ip_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#private_ip_version ElastigroupAzure#private_ip_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureNetworkAdditionalIpConfigs.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument private_ip_version", value=private_ip_version, expected_type=type_hints["private_ip_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if private_ip_version is not None:
            self._values["private_ip_version"] = private_ip_version

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#name ElastigroupAzure#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_ip_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#private_ip_version ElastigroupAzure#private_ip_version}.'''
        result = self._values.get("private_ip_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureNetworkAdditionalIpConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureNetworkAdditionalIpConfigsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureNetworkAdditionalIpConfigsList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureNetworkAdditionalIpConfigsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupAzureNetworkAdditionalIpConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureNetworkAdditionalIpConfigsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureNetworkAdditionalIpConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureNetworkAdditionalIpConfigsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureNetworkAdditionalIpConfigsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureNetworkAdditionalIpConfigsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureNetworkAdditionalIpConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureNetworkAdditionalIpConfigs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureNetworkAdditionalIpConfigs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureNetworkAdditionalIpConfigsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureNetworkAdditionalIpConfigsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureNetworkAdditionalIpConfigsOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureNetworkAdditionalIpConfigsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPrivateIpVersion")
    def reset_private_ip_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpVersion", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpVersionInput")
    def private_ip_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureNetworkAdditionalIpConfigsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpVersion")
    def private_ip_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpVersion"))

    @private_ip_version.setter
    def private_ip_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureNetworkAdditionalIpConfigsOutputReference, "private_ip_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureNetworkAdditionalIpConfigs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureNetworkAdditionalIpConfigs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureNetworkAdditionalIpConfigs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureNetworkAdditionalIpConfigsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureNetworkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureNetworkOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureNetworkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAdditionalIpConfigs")
    def put_additional_ip_configs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupAzureNetworkAdditionalIpConfigs, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureNetworkOutputReference.put_additional_ip_configs)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdditionalIpConfigs", [value]))

    @jsii.member(jsii_name="resetAdditionalIpConfigs")
    def reset_additional_ip_configs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalIpConfigs", []))

    @jsii.member(jsii_name="resetAssignPublicIp")
    def reset_assign_public_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssignPublicIp", []))

    @builtins.property
    @jsii.member(jsii_name="additionalIpConfigs")
    def additional_ip_configs(self) -> ElastigroupAzureNetworkAdditionalIpConfigsList:
        return typing.cast(ElastigroupAzureNetworkAdditionalIpConfigsList, jsii.get(self, "additionalIpConfigs"))

    @builtins.property
    @jsii.member(jsii_name="additionalIpConfigsInput")
    def additional_ip_configs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureNetworkAdditionalIpConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureNetworkAdditionalIpConfigs]]], jsii.get(self, "additionalIpConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIpInput")
    def assign_public_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "assignPublicIpInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetNameInput")
    def subnet_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkNameInput")
    def virtual_network_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkNameInput"))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIp")
    def assign_public_ip(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "assignPublicIp"))

    @assign_public_ip.setter
    def assign_public_ip(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureNetworkOutputReference, "assign_public_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assignPublicIp", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureNetworkOutputReference, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="subnetName")
    def subnet_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetName"))

    @subnet_name.setter
    def subnet_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureNetworkOutputReference, "subnet_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetName", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkName")
    def virtual_network_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkName"))

    @virtual_network_name.setter
    def virtual_network_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureNetworkOutputReference, "virtual_network_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastigroupAzureNetwork]:
        return typing.cast(typing.Optional[ElastigroupAzureNetwork], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ElastigroupAzureNetwork]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureNetworkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureScalingDownPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "policy_name": "policyName",
        "threshold": "threshold",
        "action_type": "actionType",
        "adjustment": "adjustment",
        "cooldown": "cooldown",
        "dimensions": "dimensions",
        "evaluation_periods": "evaluationPeriods",
        "maximum": "maximum",
        "max_target_capacity": "maxTargetCapacity",
        "minimum": "minimum",
        "min_target_capacity": "minTargetCapacity",
        "operator": "operator",
        "period": "period",
        "statistic": "statistic",
        "target": "target",
        "unit": "unit",
    },
)
class ElastigroupAzureScalingDownPolicy:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        policy_name: builtins.str,
        threshold: jsii.Number,
        action_type: typing.Optional[builtins.str] = None,
        adjustment: typing.Optional[builtins.str] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureScalingDownPolicyDimensions", typing.Dict[str, typing.Any]]]]] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        maximum: typing.Optional[builtins.str] = None,
        max_target_capacity: typing.Optional[builtins.str] = None,
        minimum: typing.Optional[builtins.str] = None,
        min_target_capacity: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        period: typing.Optional[jsii.Number] = None,
        statistic: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#metric_name ElastigroupAzure#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#namespace ElastigroupAzure#namespace}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#policy_name ElastigroupAzure#policy_name}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#threshold ElastigroupAzure#threshold}.
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#action_type ElastigroupAzure#action_type}.
        :param adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#adjustment ElastigroupAzure#adjustment}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#cooldown ElastigroupAzure#cooldown}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#dimensions ElastigroupAzure#dimensions}
        :param evaluation_periods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#evaluation_periods ElastigroupAzure#evaluation_periods}.
        :param maximum: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#maximum ElastigroupAzure#maximum}.
        :param max_target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#max_target_capacity ElastigroupAzure#max_target_capacity}.
        :param minimum: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#minimum ElastigroupAzure#minimum}.
        :param min_target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#min_target_capacity ElastigroupAzure#min_target_capacity}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#operator ElastigroupAzure#operator}.
        :param period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#period ElastigroupAzure#period}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#statistic ElastigroupAzure#statistic}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#target ElastigroupAzure#target}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#unit ElastigroupAzure#unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureScalingDownPolicy.__init__)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument action_type", value=action_type, expected_type=type_hints["action_type"])
            check_type(argname="argument adjustment", value=adjustment, expected_type=type_hints["adjustment"])
            check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
            check_type(argname="argument maximum", value=maximum, expected_type=type_hints["maximum"])
            check_type(argname="argument max_target_capacity", value=max_target_capacity, expected_type=type_hints["max_target_capacity"])
            check_type(argname="argument minimum", value=minimum, expected_type=type_hints["minimum"])
            check_type(argname="argument min_target_capacity", value=min_target_capacity, expected_type=type_hints["min_target_capacity"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
            "policy_name": policy_name,
            "threshold": threshold,
        }
        if action_type is not None:
            self._values["action_type"] = action_type
        if adjustment is not None:
            self._values["adjustment"] = adjustment
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if evaluation_periods is not None:
            self._values["evaluation_periods"] = evaluation_periods
        if maximum is not None:
            self._values["maximum"] = maximum
        if max_target_capacity is not None:
            self._values["max_target_capacity"] = max_target_capacity
        if minimum is not None:
            self._values["minimum"] = minimum
        if min_target_capacity is not None:
            self._values["min_target_capacity"] = min_target_capacity
        if operator is not None:
            self._values["operator"] = operator
        if period is not None:
            self._values["period"] = period
        if statistic is not None:
            self._values["statistic"] = statistic
        if target is not None:
            self._values["target"] = target
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#metric_name ElastigroupAzure#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#namespace ElastigroupAzure#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#policy_name ElastigroupAzure#policy_name}.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#threshold ElastigroupAzure#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def action_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#action_type ElastigroupAzure#action_type}.'''
        result = self._values.get("action_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def adjustment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#adjustment ElastigroupAzure#adjustment}.'''
        result = self._values.get("adjustment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#cooldown ElastigroupAzure#cooldown}.'''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScalingDownPolicyDimensions"]]]:
        '''dimensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#dimensions ElastigroupAzure#dimensions}
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScalingDownPolicyDimensions"]]], result)

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#evaluation_periods ElastigroupAzure#evaluation_periods}.'''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#maximum ElastigroupAzure#maximum}.'''
        result = self._values.get("maximum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#max_target_capacity ElastigroupAzure#max_target_capacity}.'''
        result = self._values.get("max_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#minimum ElastigroupAzure#minimum}.'''
        result = self._values.get("minimum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#min_target_capacity ElastigroupAzure#min_target_capacity}.'''
        result = self._values.get("min_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#operator ElastigroupAzure#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#period ElastigroupAzure#period}.'''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#statistic ElastigroupAzure#statistic}.'''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#target ElastigroupAzure#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#unit ElastigroupAzure#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureScalingDownPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureScalingDownPolicyDimensions",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class ElastigroupAzureScalingDownPolicyDimensions:
    def __init__(
        self,
        *,
        name: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#name ElastigroupAzure#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#value ElastigroupAzure#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureScalingDownPolicyDimensions.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#name ElastigroupAzure#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#value ElastigroupAzure#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureScalingDownPolicyDimensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureScalingDownPolicyDimensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureScalingDownPolicyDimensionsList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureScalingDownPolicyDimensionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupAzureScalingDownPolicyDimensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureScalingDownPolicyDimensionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureScalingDownPolicyDimensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyDimensionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyDimensionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyDimensionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingDownPolicyDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingDownPolicyDimensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingDownPolicyDimensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyDimensionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureScalingDownPolicyDimensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureScalingDownPolicyDimensionsOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureScalingDownPolicyDimensionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyDimensionsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyDimensionsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureScalingDownPolicyDimensions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureScalingDownPolicyDimensions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureScalingDownPolicyDimensions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyDimensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureScalingDownPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureScalingDownPolicyList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureScalingDownPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupAzureScalingDownPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureScalingDownPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureScalingDownPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingDownPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingDownPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingDownPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureScalingDownPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureScalingDownPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureScalingDownPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDimensions")
    def put_dimensions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupAzureScalingDownPolicyDimensions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureScalingDownPolicyOutputReference.put_dimensions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimensions", [value]))

    @jsii.member(jsii_name="resetActionType")
    def reset_action_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionType", []))

    @jsii.member(jsii_name="resetAdjustment")
    def reset_adjustment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdjustment", []))

    @jsii.member(jsii_name="resetCooldown")
    def reset_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCooldown", []))

    @jsii.member(jsii_name="resetDimensions")
    def reset_dimensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensions", []))

    @jsii.member(jsii_name="resetEvaluationPeriods")
    def reset_evaluation_periods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationPeriods", []))

    @jsii.member(jsii_name="resetMaximum")
    def reset_maximum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximum", []))

    @jsii.member(jsii_name="resetMaxTargetCapacity")
    def reset_max_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTargetCapacity", []))

    @jsii.member(jsii_name="resetMinimum")
    def reset_minimum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimum", []))

    @jsii.member(jsii_name="resetMinTargetCapacity")
    def reset_min_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinTargetCapacity", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetStatistic")
    def reset_statistic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatistic", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(self) -> ElastigroupAzureScalingDownPolicyDimensionsList:
        return typing.cast(ElastigroupAzureScalingDownPolicyDimensionsList, jsii.get(self, "dimensions"))

    @builtins.property
    @jsii.member(jsii_name="actionTypeInput")
    def action_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentInput")
    def adjustment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="cooldownInput")
    def cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingDownPolicyDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingDownPolicyDimensions]]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriodsInput")
    def evaluation_periods_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "evaluationPeriodsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumInput")
    def maximum_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTargetCapacityInput")
    def max_target_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxTargetCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumInput")
    def minimum_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumInput"))

    @builtins.property
    @jsii.member(jsii_name="minTargetCapacityInput")
    def min_target_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minTargetCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="periodInput")
    def period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "periodInput"))

    @builtins.property
    @jsii.member(jsii_name="policyNameInput")
    def policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="statisticInput")
    def statistic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statisticInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="actionType")
    def action_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionType"))

    @action_type.setter
    def action_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "action_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionType", value)

    @builtins.property
    @jsii.member(jsii_name="adjustment")
    def adjustment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adjustment"))

    @adjustment.setter
    def adjustment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "adjustment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustment", value)

    @builtins.property
    @jsii.member(jsii_name="cooldown")
    def cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cooldown"))

    @cooldown.setter
    def cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "cooldown").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cooldown", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriods")
    def evaluation_periods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evaluationPeriods"))

    @evaluation_periods.setter
    def evaluation_periods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "evaluation_periods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationPeriods", value)

    @builtins.property
    @jsii.member(jsii_name="maximum")
    def maximum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maximum"))

    @maximum.setter
    def maximum(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "maximum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximum", value)

    @builtins.property
    @jsii.member(jsii_name="maxTargetCapacity")
    def max_target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxTargetCapacity"))

    @max_target_capacity.setter
    def max_target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "max_target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTargetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="minimum")
    def minimum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimum"))

    @minimum.setter
    def minimum(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "minimum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimum", value)

    @builtins.property
    @jsii.member(jsii_name="minTargetCapacity")
    def min_target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minTargetCapacity"))

    @min_target_capacity.setter
    def min_target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "min_target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minTargetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "period"))

    @period.setter
    def period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "statistic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureScalingDownPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureScalingDownPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureScalingDownPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingDownPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureScalingUpPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "policy_name": "policyName",
        "threshold": "threshold",
        "action_type": "actionType",
        "adjustment": "adjustment",
        "cooldown": "cooldown",
        "dimensions": "dimensions",
        "evaluation_periods": "evaluationPeriods",
        "maximum": "maximum",
        "max_target_capacity": "maxTargetCapacity",
        "minimum": "minimum",
        "min_target_capacity": "minTargetCapacity",
        "operator": "operator",
        "period": "period",
        "statistic": "statistic",
        "target": "target",
        "unit": "unit",
    },
)
class ElastigroupAzureScalingUpPolicy:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        policy_name: builtins.str,
        threshold: jsii.Number,
        action_type: typing.Optional[builtins.str] = None,
        adjustment: typing.Optional[builtins.str] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureScalingUpPolicyDimensions", typing.Dict[str, typing.Any]]]]] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        maximum: typing.Optional[builtins.str] = None,
        max_target_capacity: typing.Optional[builtins.str] = None,
        minimum: typing.Optional[builtins.str] = None,
        min_target_capacity: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        period: typing.Optional[jsii.Number] = None,
        statistic: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#metric_name ElastigroupAzure#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#namespace ElastigroupAzure#namespace}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#policy_name ElastigroupAzure#policy_name}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#threshold ElastigroupAzure#threshold}.
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#action_type ElastigroupAzure#action_type}.
        :param adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#adjustment ElastigroupAzure#adjustment}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#cooldown ElastigroupAzure#cooldown}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#dimensions ElastigroupAzure#dimensions}
        :param evaluation_periods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#evaluation_periods ElastigroupAzure#evaluation_periods}.
        :param maximum: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#maximum ElastigroupAzure#maximum}.
        :param max_target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#max_target_capacity ElastigroupAzure#max_target_capacity}.
        :param minimum: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#minimum ElastigroupAzure#minimum}.
        :param min_target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#min_target_capacity ElastigroupAzure#min_target_capacity}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#operator ElastigroupAzure#operator}.
        :param period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#period ElastigroupAzure#period}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#statistic ElastigroupAzure#statistic}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#target ElastigroupAzure#target}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#unit ElastigroupAzure#unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureScalingUpPolicy.__init__)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument action_type", value=action_type, expected_type=type_hints["action_type"])
            check_type(argname="argument adjustment", value=adjustment, expected_type=type_hints["adjustment"])
            check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
            check_type(argname="argument maximum", value=maximum, expected_type=type_hints["maximum"])
            check_type(argname="argument max_target_capacity", value=max_target_capacity, expected_type=type_hints["max_target_capacity"])
            check_type(argname="argument minimum", value=minimum, expected_type=type_hints["minimum"])
            check_type(argname="argument min_target_capacity", value=min_target_capacity, expected_type=type_hints["min_target_capacity"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
            "policy_name": policy_name,
            "threshold": threshold,
        }
        if action_type is not None:
            self._values["action_type"] = action_type
        if adjustment is not None:
            self._values["adjustment"] = adjustment
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if evaluation_periods is not None:
            self._values["evaluation_periods"] = evaluation_periods
        if maximum is not None:
            self._values["maximum"] = maximum
        if max_target_capacity is not None:
            self._values["max_target_capacity"] = max_target_capacity
        if minimum is not None:
            self._values["minimum"] = minimum
        if min_target_capacity is not None:
            self._values["min_target_capacity"] = min_target_capacity
        if operator is not None:
            self._values["operator"] = operator
        if period is not None:
            self._values["period"] = period
        if statistic is not None:
            self._values["statistic"] = statistic
        if target is not None:
            self._values["target"] = target
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#metric_name ElastigroupAzure#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#namespace ElastigroupAzure#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#policy_name ElastigroupAzure#policy_name}.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#threshold ElastigroupAzure#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def action_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#action_type ElastigroupAzure#action_type}.'''
        result = self._values.get("action_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def adjustment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#adjustment ElastigroupAzure#adjustment}.'''
        result = self._values.get("adjustment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#cooldown ElastigroupAzure#cooldown}.'''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScalingUpPolicyDimensions"]]]:
        '''dimensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#dimensions ElastigroupAzure#dimensions}
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureScalingUpPolicyDimensions"]]], result)

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#evaluation_periods ElastigroupAzure#evaluation_periods}.'''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#maximum ElastigroupAzure#maximum}.'''
        result = self._values.get("maximum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#max_target_capacity ElastigroupAzure#max_target_capacity}.'''
        result = self._values.get("max_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#minimum ElastigroupAzure#minimum}.'''
        result = self._values.get("minimum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#min_target_capacity ElastigroupAzure#min_target_capacity}.'''
        result = self._values.get("min_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#operator ElastigroupAzure#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#period ElastigroupAzure#period}.'''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#statistic ElastigroupAzure#statistic}.'''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#target ElastigroupAzure#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#unit ElastigroupAzure#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureScalingUpPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureScalingUpPolicyDimensions",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class ElastigroupAzureScalingUpPolicyDimensions:
    def __init__(
        self,
        *,
        name: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#name ElastigroupAzure#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#value ElastigroupAzure#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureScalingUpPolicyDimensions.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#name ElastigroupAzure#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#value ElastigroupAzure#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureScalingUpPolicyDimensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureScalingUpPolicyDimensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureScalingUpPolicyDimensionsList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureScalingUpPolicyDimensionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupAzureScalingUpPolicyDimensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureScalingUpPolicyDimensionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureScalingUpPolicyDimensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyDimensionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyDimensionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyDimensionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingUpPolicyDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingUpPolicyDimensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingUpPolicyDimensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyDimensionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureScalingUpPolicyDimensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureScalingUpPolicyDimensionsOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureScalingUpPolicyDimensionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyDimensionsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyDimensionsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureScalingUpPolicyDimensions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureScalingUpPolicyDimensions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureScalingUpPolicyDimensions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyDimensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureScalingUpPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureScalingUpPolicyList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureScalingUpPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupAzureScalingUpPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureScalingUpPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureScalingUpPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingUpPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingUpPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingUpPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureScalingUpPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureScalingUpPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureScalingUpPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDimensions")
    def put_dimensions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupAzureScalingUpPolicyDimensions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureScalingUpPolicyOutputReference.put_dimensions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimensions", [value]))

    @jsii.member(jsii_name="resetActionType")
    def reset_action_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionType", []))

    @jsii.member(jsii_name="resetAdjustment")
    def reset_adjustment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdjustment", []))

    @jsii.member(jsii_name="resetCooldown")
    def reset_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCooldown", []))

    @jsii.member(jsii_name="resetDimensions")
    def reset_dimensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensions", []))

    @jsii.member(jsii_name="resetEvaluationPeriods")
    def reset_evaluation_periods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationPeriods", []))

    @jsii.member(jsii_name="resetMaximum")
    def reset_maximum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximum", []))

    @jsii.member(jsii_name="resetMaxTargetCapacity")
    def reset_max_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTargetCapacity", []))

    @jsii.member(jsii_name="resetMinimum")
    def reset_minimum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimum", []))

    @jsii.member(jsii_name="resetMinTargetCapacity")
    def reset_min_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinTargetCapacity", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetStatistic")
    def reset_statistic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatistic", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(self) -> ElastigroupAzureScalingUpPolicyDimensionsList:
        return typing.cast(ElastigroupAzureScalingUpPolicyDimensionsList, jsii.get(self, "dimensions"))

    @builtins.property
    @jsii.member(jsii_name="actionTypeInput")
    def action_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentInput")
    def adjustment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="cooldownInput")
    def cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingUpPolicyDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScalingUpPolicyDimensions]]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriodsInput")
    def evaluation_periods_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "evaluationPeriodsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumInput")
    def maximum_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTargetCapacityInput")
    def max_target_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxTargetCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumInput")
    def minimum_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumInput"))

    @builtins.property
    @jsii.member(jsii_name="minTargetCapacityInput")
    def min_target_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minTargetCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="periodInput")
    def period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "periodInput"))

    @builtins.property
    @jsii.member(jsii_name="policyNameInput")
    def policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="statisticInput")
    def statistic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statisticInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="actionType")
    def action_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionType"))

    @action_type.setter
    def action_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "action_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionType", value)

    @builtins.property
    @jsii.member(jsii_name="adjustment")
    def adjustment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adjustment"))

    @adjustment.setter
    def adjustment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "adjustment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustment", value)

    @builtins.property
    @jsii.member(jsii_name="cooldown")
    def cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cooldown"))

    @cooldown.setter
    def cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "cooldown").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cooldown", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriods")
    def evaluation_periods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evaluationPeriods"))

    @evaluation_periods.setter
    def evaluation_periods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "evaluation_periods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationPeriods", value)

    @builtins.property
    @jsii.member(jsii_name="maximum")
    def maximum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maximum"))

    @maximum.setter
    def maximum(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "maximum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximum", value)

    @builtins.property
    @jsii.member(jsii_name="maxTargetCapacity")
    def max_target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxTargetCapacity"))

    @max_target_capacity.setter
    def max_target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "max_target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTargetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="minimum")
    def minimum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimum"))

    @minimum.setter
    def minimum(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "minimum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimum", value)

    @builtins.property
    @jsii.member(jsii_name="minTargetCapacity")
    def min_target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minTargetCapacity"))

    @min_target_capacity.setter
    def min_target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "min_target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minTargetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "period"))

    @period.setter
    def period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "statistic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureScalingUpPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureScalingUpPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureScalingUpPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScalingUpPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureScheduledTask",
    jsii_struct_bases=[],
    name_mapping={
        "cron_expression": "cronExpression",
        "task_type": "taskType",
        "adjustment": "adjustment",
        "adjustment_percentage": "adjustmentPercentage",
        "batch_size_percentage": "batchSizePercentage",
        "grace_period": "gracePeriod",
        "is_enabled": "isEnabled",
        "scale_max_capacity": "scaleMaxCapacity",
        "scale_min_capacity": "scaleMinCapacity",
        "scale_target_capacity": "scaleTargetCapacity",
    },
)
class ElastigroupAzureScheduledTask:
    def __init__(
        self,
        *,
        cron_expression: builtins.str,
        task_type: builtins.str,
        adjustment: typing.Optional[builtins.str] = None,
        adjustment_percentage: typing.Optional[builtins.str] = None,
        batch_size_percentage: typing.Optional[builtins.str] = None,
        grace_period: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scale_max_capacity: typing.Optional[builtins.str] = None,
        scale_min_capacity: typing.Optional[builtins.str] = None,
        scale_target_capacity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cron_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#cron_expression ElastigroupAzure#cron_expression}.
        :param task_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#task_type ElastigroupAzure#task_type}.
        :param adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#adjustment ElastigroupAzure#adjustment}.
        :param adjustment_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#adjustment_percentage ElastigroupAzure#adjustment_percentage}.
        :param batch_size_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#batch_size_percentage ElastigroupAzure#batch_size_percentage}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#grace_period ElastigroupAzure#grace_period}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#is_enabled ElastigroupAzure#is_enabled}.
        :param scale_max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#scale_max_capacity ElastigroupAzure#scale_max_capacity}.
        :param scale_min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#scale_min_capacity ElastigroupAzure#scale_min_capacity}.
        :param scale_target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#scale_target_capacity ElastigroupAzure#scale_target_capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureScheduledTask.__init__)
            check_type(argname="argument cron_expression", value=cron_expression, expected_type=type_hints["cron_expression"])
            check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
            check_type(argname="argument adjustment", value=adjustment, expected_type=type_hints["adjustment"])
            check_type(argname="argument adjustment_percentage", value=adjustment_percentage, expected_type=type_hints["adjustment_percentage"])
            check_type(argname="argument batch_size_percentage", value=batch_size_percentage, expected_type=type_hints["batch_size_percentage"])
            check_type(argname="argument grace_period", value=grace_period, expected_type=type_hints["grace_period"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument scale_max_capacity", value=scale_max_capacity, expected_type=type_hints["scale_max_capacity"])
            check_type(argname="argument scale_min_capacity", value=scale_min_capacity, expected_type=type_hints["scale_min_capacity"])
            check_type(argname="argument scale_target_capacity", value=scale_target_capacity, expected_type=type_hints["scale_target_capacity"])
        self._values: typing.Dict[str, typing.Any] = {
            "cron_expression": cron_expression,
            "task_type": task_type,
        }
        if adjustment is not None:
            self._values["adjustment"] = adjustment
        if adjustment_percentage is not None:
            self._values["adjustment_percentage"] = adjustment_percentage
        if batch_size_percentage is not None:
            self._values["batch_size_percentage"] = batch_size_percentage
        if grace_period is not None:
            self._values["grace_period"] = grace_period
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if scale_max_capacity is not None:
            self._values["scale_max_capacity"] = scale_max_capacity
        if scale_min_capacity is not None:
            self._values["scale_min_capacity"] = scale_min_capacity
        if scale_target_capacity is not None:
            self._values["scale_target_capacity"] = scale_target_capacity

    @builtins.property
    def cron_expression(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#cron_expression ElastigroupAzure#cron_expression}.'''
        result = self._values.get("cron_expression")
        assert result is not None, "Required property 'cron_expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#task_type ElastigroupAzure#task_type}.'''
        result = self._values.get("task_type")
        assert result is not None, "Required property 'task_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def adjustment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#adjustment ElastigroupAzure#adjustment}.'''
        result = self._values.get("adjustment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def adjustment_percentage(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#adjustment_percentage ElastigroupAzure#adjustment_percentage}.'''
        result = self._values.get("adjustment_percentage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def batch_size_percentage(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#batch_size_percentage ElastigroupAzure#batch_size_percentage}.'''
        result = self._values.get("batch_size_percentage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grace_period(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#grace_period ElastigroupAzure#grace_period}.'''
        result = self._values.get("grace_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#is_enabled ElastigroupAzure#is_enabled}.'''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def scale_max_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#scale_max_capacity ElastigroupAzure#scale_max_capacity}.'''
        result = self._values.get("scale_max_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_min_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#scale_min_capacity ElastigroupAzure#scale_min_capacity}.'''
        result = self._values.get("scale_min_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#scale_target_capacity ElastigroupAzure#scale_target_capacity}.'''
        result = self._values.get("scale_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureScheduledTask(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureScheduledTaskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureScheduledTaskList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureScheduledTaskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ElastigroupAzureScheduledTaskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureScheduledTaskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureScheduledTaskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScheduledTaskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScheduledTaskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScheduledTaskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScheduledTask]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScheduledTask]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureScheduledTask]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScheduledTaskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureScheduledTaskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureScheduledTaskOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureScheduledTaskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAdjustment")
    def reset_adjustment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdjustment", []))

    @jsii.member(jsii_name="resetAdjustmentPercentage")
    def reset_adjustment_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdjustmentPercentage", []))

    @jsii.member(jsii_name="resetBatchSizePercentage")
    def reset_batch_size_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchSizePercentage", []))

    @jsii.member(jsii_name="resetGracePeriod")
    def reset_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGracePeriod", []))

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetScaleMaxCapacity")
    def reset_scale_max_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleMaxCapacity", []))

    @jsii.member(jsii_name="resetScaleMinCapacity")
    def reset_scale_min_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleMinCapacity", []))

    @jsii.member(jsii_name="resetScaleTargetCapacity")
    def reset_scale_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleTargetCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="adjustmentInput")
    def adjustment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentPercentageInput")
    def adjustment_percentage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adjustmentPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="batchSizePercentageInput")
    def batch_size_percentage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "batchSizePercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="cronExpressionInput")
    def cron_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cronExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="gracePeriodInput")
    def grace_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gracePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleMaxCapacityInput")
    def scale_max_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleMaxCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleMinCapacityInput")
    def scale_min_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleMinCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleTargetCapacityInput")
    def scale_target_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleTargetCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="taskTypeInput")
    def task_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="adjustment")
    def adjustment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adjustment"))

    @adjustment.setter
    def adjustment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScheduledTaskOutputReference, "adjustment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustment", value)

    @builtins.property
    @jsii.member(jsii_name="adjustmentPercentage")
    def adjustment_percentage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adjustmentPercentage"))

    @adjustment_percentage.setter
    def adjustment_percentage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScheduledTaskOutputReference, "adjustment_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustmentPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="batchSizePercentage")
    def batch_size_percentage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "batchSizePercentage"))

    @batch_size_percentage.setter
    def batch_size_percentage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScheduledTaskOutputReference, "batch_size_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchSizePercentage", value)

    @builtins.property
    @jsii.member(jsii_name="cronExpression")
    def cron_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cronExpression"))

    @cron_expression.setter
    def cron_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScheduledTaskOutputReference, "cron_expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cronExpression", value)

    @builtins.property
    @jsii.member(jsii_name="gracePeriod")
    def grace_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gracePeriod"))

    @grace_period.setter
    def grace_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScheduledTaskOutputReference, "grace_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScheduledTaskOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="scaleMaxCapacity")
    def scale_max_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleMaxCapacity"))

    @scale_max_capacity.setter
    def scale_max_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScheduledTaskOutputReference, "scale_max_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleMaxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="scaleMinCapacity")
    def scale_min_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleMinCapacity"))

    @scale_min_capacity.setter
    def scale_min_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScheduledTaskOutputReference, "scale_min_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleMinCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="scaleTargetCapacity")
    def scale_target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleTargetCapacity"))

    @scale_target_capacity.setter
    def scale_target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScheduledTaskOutputReference, "scale_target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleTargetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskType"))

    @task_type.setter
    def task_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScheduledTaskOutputReference, "task_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureScheduledTask, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureScheduledTask, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureScheduledTask, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureScheduledTaskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "draining_timeout": "drainingTimeout",
        "low_priority_percentage": "lowPriorityPercentage",
        "od_count": "odCount",
    },
)
class ElastigroupAzureStrategy:
    def __init__(
        self,
        *,
        draining_timeout: typing.Optional[jsii.Number] = None,
        low_priority_percentage: typing.Optional[jsii.Number] = None,
        od_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param draining_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#draining_timeout ElastigroupAzure#draining_timeout}.
        :param low_priority_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#low_priority_percentage ElastigroupAzure#low_priority_percentage}.
        :param od_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#od_count ElastigroupAzure#od_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureStrategy.__init__)
            check_type(argname="argument draining_timeout", value=draining_timeout, expected_type=type_hints["draining_timeout"])
            check_type(argname="argument low_priority_percentage", value=low_priority_percentage, expected_type=type_hints["low_priority_percentage"])
            check_type(argname="argument od_count", value=od_count, expected_type=type_hints["od_count"])
        self._values: typing.Dict[str, typing.Any] = {}
        if draining_timeout is not None:
            self._values["draining_timeout"] = draining_timeout
        if low_priority_percentage is not None:
            self._values["low_priority_percentage"] = low_priority_percentage
        if od_count is not None:
            self._values["od_count"] = od_count

    @builtins.property
    def draining_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#draining_timeout ElastigroupAzure#draining_timeout}.'''
        result = self._values.get("draining_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def low_priority_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#low_priority_percentage ElastigroupAzure#low_priority_percentage}.'''
        result = self._values.get("low_priority_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def od_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#od_count ElastigroupAzure#od_count}.'''
        result = self._values.get("od_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureStrategyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureStrategyOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureStrategyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDrainingTimeout")
    def reset_draining_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDrainingTimeout", []))

    @jsii.member(jsii_name="resetLowPriorityPercentage")
    def reset_low_priority_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLowPriorityPercentage", []))

    @jsii.member(jsii_name="resetOdCount")
    def reset_od_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOdCount", []))

    @builtins.property
    @jsii.member(jsii_name="drainingTimeoutInput")
    def draining_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "drainingTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="lowPriorityPercentageInput")
    def low_priority_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lowPriorityPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="odCountInput")
    def od_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "odCountInput"))

    @builtins.property
    @jsii.member(jsii_name="drainingTimeout")
    def draining_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "drainingTimeout"))

    @draining_timeout.setter
    def draining_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureStrategyOutputReference, "draining_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "drainingTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="lowPriorityPercentage")
    def low_priority_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lowPriorityPercentage"))

    @low_priority_percentage.setter
    def low_priority_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureStrategyOutputReference, "low_priority_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lowPriorityPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="odCount")
    def od_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "odCount"))

    @od_count.setter
    def od_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureStrategyOutputReference, "od_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "odCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastigroupAzureStrategy]:
        return typing.cast(typing.Optional[ElastigroupAzureStrategy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ElastigroupAzureStrategy]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureStrategyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureUpdatePolicy",
    jsii_struct_bases=[],
    name_mapping={"should_roll": "shouldRoll", "roll_config": "rollConfig"},
)
class ElastigroupAzureUpdatePolicy:
    def __init__(
        self,
        *,
        should_roll: typing.Union[builtins.bool, cdktf.IResolvable],
        roll_config: typing.Optional[typing.Union["ElastigroupAzureUpdatePolicyRollConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param should_roll: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#should_roll ElastigroupAzure#should_roll}.
        :param roll_config: roll_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#roll_config ElastigroupAzure#roll_config}
        '''
        if isinstance(roll_config, dict):
            roll_config = ElastigroupAzureUpdatePolicyRollConfig(**roll_config)
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureUpdatePolicy.__init__)
            check_type(argname="argument should_roll", value=should_roll, expected_type=type_hints["should_roll"])
            check_type(argname="argument roll_config", value=roll_config, expected_type=type_hints["roll_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "should_roll": should_roll,
        }
        if roll_config is not None:
            self._values["roll_config"] = roll_config

    @builtins.property
    def should_roll(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#should_roll ElastigroupAzure#should_roll}.'''
        result = self._values.get("should_roll")
        assert result is not None, "Required property 'should_roll' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def roll_config(self) -> typing.Optional["ElastigroupAzureUpdatePolicyRollConfig"]:
        '''roll_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#roll_config ElastigroupAzure#roll_config}
        '''
        result = self._values.get("roll_config")
        return typing.cast(typing.Optional["ElastigroupAzureUpdatePolicyRollConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureUpdatePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureUpdatePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureUpdatePolicyOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureUpdatePolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRollConfig")
    def put_roll_config(
        self,
        *,
        batch_size_percentage: jsii.Number,
        grace_period: typing.Optional[jsii.Number] = None,
        health_check_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param batch_size_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#batch_size_percentage ElastigroupAzure#batch_size_percentage}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#grace_period ElastigroupAzure#grace_period}.
        :param health_check_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#health_check_type ElastigroupAzure#health_check_type}.
        '''
        value = ElastigroupAzureUpdatePolicyRollConfig(
            batch_size_percentage=batch_size_percentage,
            grace_period=grace_period,
            health_check_type=health_check_type,
        )

        return typing.cast(None, jsii.invoke(self, "putRollConfig", [value]))

    @jsii.member(jsii_name="resetRollConfig")
    def reset_roll_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRollConfig", []))

    @builtins.property
    @jsii.member(jsii_name="rollConfig")
    def roll_config(self) -> "ElastigroupAzureUpdatePolicyRollConfigOutputReference":
        return typing.cast("ElastigroupAzureUpdatePolicyRollConfigOutputReference", jsii.get(self, "rollConfig"))

    @builtins.property
    @jsii.member(jsii_name="rollConfigInput")
    def roll_config_input(
        self,
    ) -> typing.Optional["ElastigroupAzureUpdatePolicyRollConfig"]:
        return typing.cast(typing.Optional["ElastigroupAzureUpdatePolicyRollConfig"], jsii.get(self, "rollConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="shouldRollInput")
    def should_roll_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "shouldRollInput"))

    @builtins.property
    @jsii.member(jsii_name="shouldRoll")
    def should_roll(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "shouldRoll"))

    @should_roll.setter
    def should_roll(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureUpdatePolicyOutputReference, "should_roll").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shouldRoll", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastigroupAzureUpdatePolicy]:
        return typing.cast(typing.Optional[ElastigroupAzureUpdatePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastigroupAzureUpdatePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureUpdatePolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureUpdatePolicyRollConfig",
    jsii_struct_bases=[],
    name_mapping={
        "batch_size_percentage": "batchSizePercentage",
        "grace_period": "gracePeriod",
        "health_check_type": "healthCheckType",
    },
)
class ElastigroupAzureUpdatePolicyRollConfig:
    def __init__(
        self,
        *,
        batch_size_percentage: jsii.Number,
        grace_period: typing.Optional[jsii.Number] = None,
        health_check_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param batch_size_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#batch_size_percentage ElastigroupAzure#batch_size_percentage}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#grace_period ElastigroupAzure#grace_period}.
        :param health_check_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#health_check_type ElastigroupAzure#health_check_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureUpdatePolicyRollConfig.__init__)
            check_type(argname="argument batch_size_percentage", value=batch_size_percentage, expected_type=type_hints["batch_size_percentage"])
            check_type(argname="argument grace_period", value=grace_period, expected_type=type_hints["grace_period"])
            check_type(argname="argument health_check_type", value=health_check_type, expected_type=type_hints["health_check_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "batch_size_percentage": batch_size_percentage,
        }
        if grace_period is not None:
            self._values["grace_period"] = grace_period
        if health_check_type is not None:
            self._values["health_check_type"] = health_check_type

    @builtins.property
    def batch_size_percentage(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#batch_size_percentage ElastigroupAzure#batch_size_percentage}.'''
        result = self._values.get("batch_size_percentage")
        assert result is not None, "Required property 'batch_size_percentage' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def grace_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#grace_period ElastigroupAzure#grace_period}.'''
        result = self._values.get("grace_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure#health_check_type ElastigroupAzure#health_check_type}.'''
        result = self._values.get("health_check_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureUpdatePolicyRollConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureUpdatePolicyRollConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzure.ElastigroupAzureUpdatePolicyRollConfigOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureUpdatePolicyRollConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGracePeriod")
    def reset_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGracePeriod", []))

    @jsii.member(jsii_name="resetHealthCheckType")
    def reset_health_check_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckType", []))

    @builtins.property
    @jsii.member(jsii_name="batchSizePercentageInput")
    def batch_size_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "batchSizePercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="gracePeriodInput")
    def grace_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gracePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckTypeInput")
    def health_check_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="batchSizePercentage")
    def batch_size_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "batchSizePercentage"))

    @batch_size_percentage.setter
    def batch_size_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureUpdatePolicyRollConfigOutputReference, "batch_size_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchSizePercentage", value)

    @builtins.property
    @jsii.member(jsii_name="gracePeriod")
    def grace_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gracePeriod"))

    @grace_period.setter
    def grace_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureUpdatePolicyRollConfigOutputReference, "grace_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckType")
    def health_check_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckType"))

    @health_check_type.setter
    def health_check_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureUpdatePolicyRollConfigOutputReference, "health_check_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastigroupAzureUpdatePolicyRollConfig]:
        return typing.cast(typing.Optional[ElastigroupAzureUpdatePolicyRollConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastigroupAzureUpdatePolicyRollConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureUpdatePolicyRollConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ElastigroupAzure",
    "ElastigroupAzureConfig",
    "ElastigroupAzureHealthCheck",
    "ElastigroupAzureHealthCheckOutputReference",
    "ElastigroupAzureImage",
    "ElastigroupAzureImageCustom",
    "ElastigroupAzureImageCustomList",
    "ElastigroupAzureImageCustomOutputReference",
    "ElastigroupAzureImageList",
    "ElastigroupAzureImageMarketplace",
    "ElastigroupAzureImageMarketplaceList",
    "ElastigroupAzureImageMarketplaceOutputReference",
    "ElastigroupAzureImageOutputReference",
    "ElastigroupAzureIntegrationKubernetes",
    "ElastigroupAzureIntegrationKubernetesOutputReference",
    "ElastigroupAzureIntegrationMultaiRuntime",
    "ElastigroupAzureIntegrationMultaiRuntimeOutputReference",
    "ElastigroupAzureLoadBalancers",
    "ElastigroupAzureLoadBalancersList",
    "ElastigroupAzureLoadBalancersOutputReference",
    "ElastigroupAzureLogin",
    "ElastigroupAzureLoginOutputReference",
    "ElastigroupAzureManagedServiceIdentities",
    "ElastigroupAzureManagedServiceIdentitiesList",
    "ElastigroupAzureManagedServiceIdentitiesOutputReference",
    "ElastigroupAzureNetwork",
    "ElastigroupAzureNetworkAdditionalIpConfigs",
    "ElastigroupAzureNetworkAdditionalIpConfigsList",
    "ElastigroupAzureNetworkAdditionalIpConfigsOutputReference",
    "ElastigroupAzureNetworkOutputReference",
    "ElastigroupAzureScalingDownPolicy",
    "ElastigroupAzureScalingDownPolicyDimensions",
    "ElastigroupAzureScalingDownPolicyDimensionsList",
    "ElastigroupAzureScalingDownPolicyDimensionsOutputReference",
    "ElastigroupAzureScalingDownPolicyList",
    "ElastigroupAzureScalingDownPolicyOutputReference",
    "ElastigroupAzureScalingUpPolicy",
    "ElastigroupAzureScalingUpPolicyDimensions",
    "ElastigroupAzureScalingUpPolicyDimensionsList",
    "ElastigroupAzureScalingUpPolicyDimensionsOutputReference",
    "ElastigroupAzureScalingUpPolicyList",
    "ElastigroupAzureScalingUpPolicyOutputReference",
    "ElastigroupAzureScheduledTask",
    "ElastigroupAzureScheduledTaskList",
    "ElastigroupAzureScheduledTaskOutputReference",
    "ElastigroupAzureStrategy",
    "ElastigroupAzureStrategyOutputReference",
    "ElastigroupAzureUpdatePolicy",
    "ElastigroupAzureUpdatePolicyOutputReference",
    "ElastigroupAzureUpdatePolicyRollConfig",
    "ElastigroupAzureUpdatePolicyRollConfigOutputReference",
]

publication.publish()
