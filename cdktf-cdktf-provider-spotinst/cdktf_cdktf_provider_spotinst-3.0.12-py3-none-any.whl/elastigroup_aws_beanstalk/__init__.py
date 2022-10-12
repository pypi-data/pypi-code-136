'''
# `spotinst_elastigroup_aws_beanstalk`

Refer to the Terraform Registory for docs: [`spotinst_elastigroup_aws_beanstalk`](https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk).
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


class ElastigroupAwsBeanstalk(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAwsBeanstalk.ElastigroupAwsBeanstalk",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk spotinst_elastigroup_aws_beanstalk}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        desired_capacity: jsii.Number,
        instance_types_spot: typing.Sequence[builtins.str],
        max_size: jsii.Number,
        min_size: jsii.Number,
        name: builtins.str,
        product: builtins.str,
        region: builtins.str,
        beanstalk_environment_id: typing.Optional[builtins.str] = None,
        beanstalk_environment_name: typing.Optional[builtins.str] = None,
        deployment_preferences: typing.Optional[typing.Union["ElastigroupAwsBeanstalkDeploymentPreferences", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        maintenance: typing.Optional[builtins.str] = None,
        managed_actions: typing.Optional[typing.Union["ElastigroupAwsBeanstalkManagedActions", typing.Dict[str, typing.Any]]] = None,
        scheduled_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAwsBeanstalkScheduledTask", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk spotinst_elastigroup_aws_beanstalk} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#desired_capacity ElastigroupAwsBeanstalk#desired_capacity}.
        :param instance_types_spot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#instance_types_spot ElastigroupAwsBeanstalk#instance_types_spot}.
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#max_size ElastigroupAwsBeanstalk#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#min_size ElastigroupAwsBeanstalk#min_size}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#name ElastigroupAwsBeanstalk#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#product ElastigroupAwsBeanstalk#product}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#region ElastigroupAwsBeanstalk#region}.
        :param beanstalk_environment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#beanstalk_environment_id ElastigroupAwsBeanstalk#beanstalk_environment_id}.
        :param beanstalk_environment_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#beanstalk_environment_name ElastigroupAwsBeanstalk#beanstalk_environment_name}.
        :param deployment_preferences: deployment_preferences block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#deployment_preferences ElastigroupAwsBeanstalk#deployment_preferences}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#id ElastigroupAwsBeanstalk#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#maintenance ElastigroupAwsBeanstalk#maintenance}.
        :param managed_actions: managed_actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#managed_actions ElastigroupAwsBeanstalk#managed_actions}
        :param scheduled_task: scheduled_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#scheduled_task ElastigroupAwsBeanstalk#scheduled_task}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalk.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ElastigroupAwsBeanstalkConfig(
            desired_capacity=desired_capacity,
            instance_types_spot=instance_types_spot,
            max_size=max_size,
            min_size=min_size,
            name=name,
            product=product,
            region=region,
            beanstalk_environment_id=beanstalk_environment_id,
            beanstalk_environment_name=beanstalk_environment_name,
            deployment_preferences=deployment_preferences,
            id=id,
            maintenance=maintenance,
            managed_actions=managed_actions,
            scheduled_task=scheduled_task,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDeploymentPreferences")
    def put_deployment_preferences(
        self,
        *,
        automatic_roll: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        batch_size_percentage: typing.Optional[jsii.Number] = None,
        grace_period: typing.Optional[jsii.Number] = None,
        strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAwsBeanstalkDeploymentPreferencesStrategy", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param automatic_roll: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#automatic_roll ElastigroupAwsBeanstalk#automatic_roll}.
        :param batch_size_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#batch_size_percentage ElastigroupAwsBeanstalk#batch_size_percentage}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#grace_period ElastigroupAwsBeanstalk#grace_period}.
        :param strategy: strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#strategy ElastigroupAwsBeanstalk#strategy}
        '''
        value = ElastigroupAwsBeanstalkDeploymentPreferences(
            automatic_roll=automatic_roll,
            batch_size_percentage=batch_size_percentage,
            grace_period=grace_period,
            strategy=strategy,
        )

        return typing.cast(None, jsii.invoke(self, "putDeploymentPreferences", [value]))

    @jsii.member(jsii_name="putManagedActions")
    def put_managed_actions(
        self,
        *,
        platform_update: typing.Optional[typing.Union["ElastigroupAwsBeanstalkManagedActionsPlatformUpdate", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param platform_update: platform_update block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#platform_update ElastigroupAwsBeanstalk#platform_update}
        '''
        value = ElastigroupAwsBeanstalkManagedActions(platform_update=platform_update)

        return typing.cast(None, jsii.invoke(self, "putManagedActions", [value]))

    @jsii.member(jsii_name="putScheduledTask")
    def put_scheduled_task(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAwsBeanstalkScheduledTask", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalk.put_scheduled_task)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScheduledTask", [value]))

    @jsii.member(jsii_name="resetBeanstalkEnvironmentId")
    def reset_beanstalk_environment_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBeanstalkEnvironmentId", []))

    @jsii.member(jsii_name="resetBeanstalkEnvironmentName")
    def reset_beanstalk_environment_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBeanstalkEnvironmentName", []))

    @jsii.member(jsii_name="resetDeploymentPreferences")
    def reset_deployment_preferences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentPreferences", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaintenance")
    def reset_maintenance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenance", []))

    @jsii.member(jsii_name="resetManagedActions")
    def reset_managed_actions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedActions", []))

    @jsii.member(jsii_name="resetScheduledTask")
    def reset_scheduled_task(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduledTask", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="deploymentPreferences")
    def deployment_preferences(
        self,
    ) -> "ElastigroupAwsBeanstalkDeploymentPreferencesOutputReference":
        return typing.cast("ElastigroupAwsBeanstalkDeploymentPreferencesOutputReference", jsii.get(self, "deploymentPreferences"))

    @builtins.property
    @jsii.member(jsii_name="managedActions")
    def managed_actions(self) -> "ElastigroupAwsBeanstalkManagedActionsOutputReference":
        return typing.cast("ElastigroupAwsBeanstalkManagedActionsOutputReference", jsii.get(self, "managedActions"))

    @builtins.property
    @jsii.member(jsii_name="scheduledTask")
    def scheduled_task(self) -> "ElastigroupAwsBeanstalkScheduledTaskList":
        return typing.cast("ElastigroupAwsBeanstalkScheduledTaskList", jsii.get(self, "scheduledTask"))

    @builtins.property
    @jsii.member(jsii_name="beanstalkEnvironmentIdInput")
    def beanstalk_environment_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "beanstalkEnvironmentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="beanstalkEnvironmentNameInput")
    def beanstalk_environment_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "beanstalkEnvironmentNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentPreferencesInput")
    def deployment_preferences_input(
        self,
    ) -> typing.Optional["ElastigroupAwsBeanstalkDeploymentPreferences"]:
        return typing.cast(typing.Optional["ElastigroupAwsBeanstalkDeploymentPreferences"], jsii.get(self, "deploymentPreferencesInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredCapacityInput")
    def desired_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypesSpotInput")
    def instance_types_spot_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instanceTypesSpotInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceInput")
    def maintenance_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maintenanceInput"))

    @builtins.property
    @jsii.member(jsii_name="managedActionsInput")
    def managed_actions_input(
        self,
    ) -> typing.Optional["ElastigroupAwsBeanstalkManagedActions"]:
        return typing.cast(typing.Optional["ElastigroupAwsBeanstalkManagedActions"], jsii.get(self, "managedActionsInput"))

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
    @jsii.member(jsii_name="productInput")
    def product_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduledTaskInput")
    def scheduled_task_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAwsBeanstalkScheduledTask"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAwsBeanstalkScheduledTask"]]], jsii.get(self, "scheduledTaskInput"))

    @builtins.property
    @jsii.member(jsii_name="beanstalkEnvironmentId")
    def beanstalk_environment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "beanstalkEnvironmentId"))

    @beanstalk_environment_id.setter
    def beanstalk_environment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalk, "beanstalk_environment_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "beanstalkEnvironmentId", value)

    @builtins.property
    @jsii.member(jsii_name="beanstalkEnvironmentName")
    def beanstalk_environment_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "beanstalkEnvironmentName"))

    @beanstalk_environment_name.setter
    def beanstalk_environment_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalk, "beanstalk_environment_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "beanstalkEnvironmentName", value)

    @builtins.property
    @jsii.member(jsii_name="desiredCapacity")
    def desired_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredCapacity"))

    @desired_capacity.setter
    def desired_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalk, "desired_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalk, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceTypesSpot")
    def instance_types_spot(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceTypesSpot"))

    @instance_types_spot.setter
    def instance_types_spot(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalk, "instance_types_spot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceTypesSpot", value)

    @builtins.property
    @jsii.member(jsii_name="maintenance")
    def maintenance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenance"))

    @maintenance.setter
    def maintenance(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalk, "maintenance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenance", value)

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSize"))

    @max_size.setter
    def max_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalk, "max_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSize", value)

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalk, "min_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalk, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="product")
    def product(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "product"))

    @product.setter
    def product(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalk, "product").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "product", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalk, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAwsBeanstalk.ElastigroupAwsBeanstalkConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "desired_capacity": "desiredCapacity",
        "instance_types_spot": "instanceTypesSpot",
        "max_size": "maxSize",
        "min_size": "minSize",
        "name": "name",
        "product": "product",
        "region": "region",
        "beanstalk_environment_id": "beanstalkEnvironmentId",
        "beanstalk_environment_name": "beanstalkEnvironmentName",
        "deployment_preferences": "deploymentPreferences",
        "id": "id",
        "maintenance": "maintenance",
        "managed_actions": "managedActions",
        "scheduled_task": "scheduledTask",
    },
)
class ElastigroupAwsBeanstalkConfig(cdktf.TerraformMetaArguments):
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
        desired_capacity: jsii.Number,
        instance_types_spot: typing.Sequence[builtins.str],
        max_size: jsii.Number,
        min_size: jsii.Number,
        name: builtins.str,
        product: builtins.str,
        region: builtins.str,
        beanstalk_environment_id: typing.Optional[builtins.str] = None,
        beanstalk_environment_name: typing.Optional[builtins.str] = None,
        deployment_preferences: typing.Optional[typing.Union["ElastigroupAwsBeanstalkDeploymentPreferences", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        maintenance: typing.Optional[builtins.str] = None,
        managed_actions: typing.Optional[typing.Union["ElastigroupAwsBeanstalkManagedActions", typing.Dict[str, typing.Any]]] = None,
        scheduled_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAwsBeanstalkScheduledTask", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#desired_capacity ElastigroupAwsBeanstalk#desired_capacity}.
        :param instance_types_spot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#instance_types_spot ElastigroupAwsBeanstalk#instance_types_spot}.
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#max_size ElastigroupAwsBeanstalk#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#min_size ElastigroupAwsBeanstalk#min_size}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#name ElastigroupAwsBeanstalk#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#product ElastigroupAwsBeanstalk#product}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#region ElastigroupAwsBeanstalk#region}.
        :param beanstalk_environment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#beanstalk_environment_id ElastigroupAwsBeanstalk#beanstalk_environment_id}.
        :param beanstalk_environment_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#beanstalk_environment_name ElastigroupAwsBeanstalk#beanstalk_environment_name}.
        :param deployment_preferences: deployment_preferences block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#deployment_preferences ElastigroupAwsBeanstalk#deployment_preferences}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#id ElastigroupAwsBeanstalk#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#maintenance ElastigroupAwsBeanstalk#maintenance}.
        :param managed_actions: managed_actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#managed_actions ElastigroupAwsBeanstalk#managed_actions}
        :param scheduled_task: scheduled_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#scheduled_task ElastigroupAwsBeanstalk#scheduled_task}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(deployment_preferences, dict):
            deployment_preferences = ElastigroupAwsBeanstalkDeploymentPreferences(**deployment_preferences)
        if isinstance(managed_actions, dict):
            managed_actions = ElastigroupAwsBeanstalkManagedActions(**managed_actions)
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument desired_capacity", value=desired_capacity, expected_type=type_hints["desired_capacity"])
            check_type(argname="argument instance_types_spot", value=instance_types_spot, expected_type=type_hints["instance_types_spot"])
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument beanstalk_environment_id", value=beanstalk_environment_id, expected_type=type_hints["beanstalk_environment_id"])
            check_type(argname="argument beanstalk_environment_name", value=beanstalk_environment_name, expected_type=type_hints["beanstalk_environment_name"])
            check_type(argname="argument deployment_preferences", value=deployment_preferences, expected_type=type_hints["deployment_preferences"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument maintenance", value=maintenance, expected_type=type_hints["maintenance"])
            check_type(argname="argument managed_actions", value=managed_actions, expected_type=type_hints["managed_actions"])
            check_type(argname="argument scheduled_task", value=scheduled_task, expected_type=type_hints["scheduled_task"])
        self._values: typing.Dict[str, typing.Any] = {
            "desired_capacity": desired_capacity,
            "instance_types_spot": instance_types_spot,
            "max_size": max_size,
            "min_size": min_size,
            "name": name,
            "product": product,
            "region": region,
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
        if beanstalk_environment_id is not None:
            self._values["beanstalk_environment_id"] = beanstalk_environment_id
        if beanstalk_environment_name is not None:
            self._values["beanstalk_environment_name"] = beanstalk_environment_name
        if deployment_preferences is not None:
            self._values["deployment_preferences"] = deployment_preferences
        if id is not None:
            self._values["id"] = id
        if maintenance is not None:
            self._values["maintenance"] = maintenance
        if managed_actions is not None:
            self._values["managed_actions"] = managed_actions
        if scheduled_task is not None:
            self._values["scheduled_task"] = scheduled_task

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
    def desired_capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#desired_capacity ElastigroupAwsBeanstalk#desired_capacity}.'''
        result = self._values.get("desired_capacity")
        assert result is not None, "Required property 'desired_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def instance_types_spot(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#instance_types_spot ElastigroupAwsBeanstalk#instance_types_spot}.'''
        result = self._values.get("instance_types_spot")
        assert result is not None, "Required property 'instance_types_spot' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def max_size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#max_size ElastigroupAwsBeanstalk#max_size}.'''
        result = self._values.get("max_size")
        assert result is not None, "Required property 'max_size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#min_size ElastigroupAwsBeanstalk#min_size}.'''
        result = self._values.get("min_size")
        assert result is not None, "Required property 'min_size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#name ElastigroupAwsBeanstalk#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#product ElastigroupAwsBeanstalk#product}.'''
        result = self._values.get("product")
        assert result is not None, "Required property 'product' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#region ElastigroupAwsBeanstalk#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def beanstalk_environment_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#beanstalk_environment_id ElastigroupAwsBeanstalk#beanstalk_environment_id}.'''
        result = self._values.get("beanstalk_environment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def beanstalk_environment_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#beanstalk_environment_name ElastigroupAwsBeanstalk#beanstalk_environment_name}.'''
        result = self._values.get("beanstalk_environment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_preferences(
        self,
    ) -> typing.Optional["ElastigroupAwsBeanstalkDeploymentPreferences"]:
        '''deployment_preferences block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#deployment_preferences ElastigroupAwsBeanstalk#deployment_preferences}
        '''
        result = self._values.get("deployment_preferences")
        return typing.cast(typing.Optional["ElastigroupAwsBeanstalkDeploymentPreferences"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#id ElastigroupAwsBeanstalk#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#maintenance ElastigroupAwsBeanstalk#maintenance}.'''
        result = self._values.get("maintenance")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_actions(
        self,
    ) -> typing.Optional["ElastigroupAwsBeanstalkManagedActions"]:
        '''managed_actions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#managed_actions ElastigroupAwsBeanstalk#managed_actions}
        '''
        result = self._values.get("managed_actions")
        return typing.cast(typing.Optional["ElastigroupAwsBeanstalkManagedActions"], result)

    @builtins.property
    def scheduled_task(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAwsBeanstalkScheduledTask"]]]:
        '''scheduled_task block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#scheduled_task ElastigroupAwsBeanstalk#scheduled_task}
        '''
        result = self._values.get("scheduled_task")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAwsBeanstalkScheduledTask"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAwsBeanstalkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAwsBeanstalk.ElastigroupAwsBeanstalkDeploymentPreferences",
    jsii_struct_bases=[],
    name_mapping={
        "automatic_roll": "automaticRoll",
        "batch_size_percentage": "batchSizePercentage",
        "grace_period": "gracePeriod",
        "strategy": "strategy",
    },
)
class ElastigroupAwsBeanstalkDeploymentPreferences:
    def __init__(
        self,
        *,
        automatic_roll: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        batch_size_percentage: typing.Optional[jsii.Number] = None,
        grace_period: typing.Optional[jsii.Number] = None,
        strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAwsBeanstalkDeploymentPreferencesStrategy", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param automatic_roll: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#automatic_roll ElastigroupAwsBeanstalk#automatic_roll}.
        :param batch_size_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#batch_size_percentage ElastigroupAwsBeanstalk#batch_size_percentage}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#grace_period ElastigroupAwsBeanstalk#grace_period}.
        :param strategy: strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#strategy ElastigroupAwsBeanstalk#strategy}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkDeploymentPreferences.__init__)
            check_type(argname="argument automatic_roll", value=automatic_roll, expected_type=type_hints["automatic_roll"])
            check_type(argname="argument batch_size_percentage", value=batch_size_percentage, expected_type=type_hints["batch_size_percentage"])
            check_type(argname="argument grace_period", value=grace_period, expected_type=type_hints["grace_period"])
            check_type(argname="argument strategy", value=strategy, expected_type=type_hints["strategy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if automatic_roll is not None:
            self._values["automatic_roll"] = automatic_roll
        if batch_size_percentage is not None:
            self._values["batch_size_percentage"] = batch_size_percentage
        if grace_period is not None:
            self._values["grace_period"] = grace_period
        if strategy is not None:
            self._values["strategy"] = strategy

    @builtins.property
    def automatic_roll(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#automatic_roll ElastigroupAwsBeanstalk#automatic_roll}.'''
        result = self._values.get("automatic_roll")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def batch_size_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#batch_size_percentage ElastigroupAwsBeanstalk#batch_size_percentage}.'''
        result = self._values.get("batch_size_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def grace_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#grace_period ElastigroupAwsBeanstalk#grace_period}.'''
        result = self._values.get("grace_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def strategy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAwsBeanstalkDeploymentPreferencesStrategy"]]]:
        '''strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#strategy ElastigroupAwsBeanstalk#strategy}
        '''
        result = self._values.get("strategy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAwsBeanstalkDeploymentPreferencesStrategy"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAwsBeanstalkDeploymentPreferences(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAwsBeanstalkDeploymentPreferencesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAwsBeanstalk.ElastigroupAwsBeanstalkDeploymentPreferencesOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkDeploymentPreferencesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putStrategy")
    def put_strategy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAwsBeanstalkDeploymentPreferencesStrategy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkDeploymentPreferencesOutputReference.put_strategy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStrategy", [value]))

    @jsii.member(jsii_name="resetAutomaticRoll")
    def reset_automatic_roll(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticRoll", []))

    @jsii.member(jsii_name="resetBatchSizePercentage")
    def reset_batch_size_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchSizePercentage", []))

    @jsii.member(jsii_name="resetGracePeriod")
    def reset_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGracePeriod", []))

    @jsii.member(jsii_name="resetStrategy")
    def reset_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStrategy", []))

    @builtins.property
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> "ElastigroupAwsBeanstalkDeploymentPreferencesStrategyList":
        return typing.cast("ElastigroupAwsBeanstalkDeploymentPreferencesStrategyList", jsii.get(self, "strategy"))

    @builtins.property
    @jsii.member(jsii_name="automaticRollInput")
    def automatic_roll_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "automaticRollInput"))

    @builtins.property
    @jsii.member(jsii_name="batchSizePercentageInput")
    def batch_size_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "batchSizePercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="gracePeriodInput")
    def grace_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gracePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="strategyInput")
    def strategy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAwsBeanstalkDeploymentPreferencesStrategy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAwsBeanstalkDeploymentPreferencesStrategy"]]], jsii.get(self, "strategyInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticRoll")
    def automatic_roll(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "automaticRoll"))

    @automatic_roll.setter
    def automatic_roll(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkDeploymentPreferencesOutputReference, "automatic_roll").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticRoll", value)

    @builtins.property
    @jsii.member(jsii_name="batchSizePercentage")
    def batch_size_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "batchSizePercentage"))

    @batch_size_percentage.setter
    def batch_size_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkDeploymentPreferencesOutputReference, "batch_size_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchSizePercentage", value)

    @builtins.property
    @jsii.member(jsii_name="gracePeriod")
    def grace_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gracePeriod"))

    @grace_period.setter
    def grace_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkDeploymentPreferencesOutputReference, "grace_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElastigroupAwsBeanstalkDeploymentPreferences]:
        return typing.cast(typing.Optional[ElastigroupAwsBeanstalkDeploymentPreferences], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastigroupAwsBeanstalkDeploymentPreferences],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkDeploymentPreferencesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAwsBeanstalk.ElastigroupAwsBeanstalkDeploymentPreferencesStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "should_drain_instances": "shouldDrainInstances",
    },
)
class ElastigroupAwsBeanstalkDeploymentPreferencesStrategy:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        should_drain_instances: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#action ElastigroupAwsBeanstalk#action}.
        :param should_drain_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#should_drain_instances ElastigroupAwsBeanstalk#should_drain_instances}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkDeploymentPreferencesStrategy.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument should_drain_instances", value=should_drain_instances, expected_type=type_hints["should_drain_instances"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if should_drain_instances is not None:
            self._values["should_drain_instances"] = should_drain_instances

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#action ElastigroupAwsBeanstalk#action}.'''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def should_drain_instances(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#should_drain_instances ElastigroupAwsBeanstalk#should_drain_instances}.'''
        result = self._values.get("should_drain_instances")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAwsBeanstalkDeploymentPreferencesStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAwsBeanstalkDeploymentPreferencesStrategyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAwsBeanstalk.ElastigroupAwsBeanstalkDeploymentPreferencesStrategyList",
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
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkDeploymentPreferencesStrategyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupAwsBeanstalkDeploymentPreferencesStrategyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkDeploymentPreferencesStrategyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAwsBeanstalkDeploymentPreferencesStrategyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkDeploymentPreferencesStrategyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkDeploymentPreferencesStrategyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkDeploymentPreferencesStrategyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAwsBeanstalkDeploymentPreferencesStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAwsBeanstalkDeploymentPreferencesStrategy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAwsBeanstalkDeploymentPreferencesStrategy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkDeploymentPreferencesStrategyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAwsBeanstalkDeploymentPreferencesStrategyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAwsBeanstalk.ElastigroupAwsBeanstalkDeploymentPreferencesStrategyOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkDeploymentPreferencesStrategyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetShouldDrainInstances")
    def reset_should_drain_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShouldDrainInstances", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="shouldDrainInstancesInput")
    def should_drain_instances_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "shouldDrainInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkDeploymentPreferencesStrategyOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="shouldDrainInstances")
    def should_drain_instances(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "shouldDrainInstances"))

    @should_drain_instances.setter
    def should_drain_instances(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkDeploymentPreferencesStrategyOutputReference, "should_drain_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shouldDrainInstances", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAwsBeanstalkDeploymentPreferencesStrategy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAwsBeanstalkDeploymentPreferencesStrategy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAwsBeanstalkDeploymentPreferencesStrategy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkDeploymentPreferencesStrategyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAwsBeanstalk.ElastigroupAwsBeanstalkManagedActions",
    jsii_struct_bases=[],
    name_mapping={"platform_update": "platformUpdate"},
)
class ElastigroupAwsBeanstalkManagedActions:
    def __init__(
        self,
        *,
        platform_update: typing.Optional[typing.Union["ElastigroupAwsBeanstalkManagedActionsPlatformUpdate", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param platform_update: platform_update block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#platform_update ElastigroupAwsBeanstalk#platform_update}
        '''
        if isinstance(platform_update, dict):
            platform_update = ElastigroupAwsBeanstalkManagedActionsPlatformUpdate(**platform_update)
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkManagedActions.__init__)
            check_type(argname="argument platform_update", value=platform_update, expected_type=type_hints["platform_update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if platform_update is not None:
            self._values["platform_update"] = platform_update

    @builtins.property
    def platform_update(
        self,
    ) -> typing.Optional["ElastigroupAwsBeanstalkManagedActionsPlatformUpdate"]:
        '''platform_update block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#platform_update ElastigroupAwsBeanstalk#platform_update}
        '''
        result = self._values.get("platform_update")
        return typing.cast(typing.Optional["ElastigroupAwsBeanstalkManagedActionsPlatformUpdate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAwsBeanstalkManagedActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAwsBeanstalkManagedActionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAwsBeanstalk.ElastigroupAwsBeanstalkManagedActionsOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkManagedActionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPlatformUpdate")
    def put_platform_update(
        self,
        *,
        perform_at: typing.Optional[builtins.str] = None,
        time_window: typing.Optional[builtins.str] = None,
        update_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param perform_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#perform_at ElastigroupAwsBeanstalk#perform_at}.
        :param time_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#time_window ElastigroupAwsBeanstalk#time_window}.
        :param update_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#update_level ElastigroupAwsBeanstalk#update_level}.
        '''
        value = ElastigroupAwsBeanstalkManagedActionsPlatformUpdate(
            perform_at=perform_at, time_window=time_window, update_level=update_level
        )

        return typing.cast(None, jsii.invoke(self, "putPlatformUpdate", [value]))

    @jsii.member(jsii_name="resetPlatformUpdate")
    def reset_platform_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatformUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="platformUpdate")
    def platform_update(
        self,
    ) -> "ElastigroupAwsBeanstalkManagedActionsPlatformUpdateOutputReference":
        return typing.cast("ElastigroupAwsBeanstalkManagedActionsPlatformUpdateOutputReference", jsii.get(self, "platformUpdate"))

    @builtins.property
    @jsii.member(jsii_name="platformUpdateInput")
    def platform_update_input(
        self,
    ) -> typing.Optional["ElastigroupAwsBeanstalkManagedActionsPlatformUpdate"]:
        return typing.cast(typing.Optional["ElastigroupAwsBeanstalkManagedActionsPlatformUpdate"], jsii.get(self, "platformUpdateInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastigroupAwsBeanstalkManagedActions]:
        return typing.cast(typing.Optional[ElastigroupAwsBeanstalkManagedActions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastigroupAwsBeanstalkManagedActions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkManagedActionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAwsBeanstalk.ElastigroupAwsBeanstalkManagedActionsPlatformUpdate",
    jsii_struct_bases=[],
    name_mapping={
        "perform_at": "performAt",
        "time_window": "timeWindow",
        "update_level": "updateLevel",
    },
)
class ElastigroupAwsBeanstalkManagedActionsPlatformUpdate:
    def __init__(
        self,
        *,
        perform_at: typing.Optional[builtins.str] = None,
        time_window: typing.Optional[builtins.str] = None,
        update_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param perform_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#perform_at ElastigroupAwsBeanstalk#perform_at}.
        :param time_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#time_window ElastigroupAwsBeanstalk#time_window}.
        :param update_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#update_level ElastigroupAwsBeanstalk#update_level}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkManagedActionsPlatformUpdate.__init__)
            check_type(argname="argument perform_at", value=perform_at, expected_type=type_hints["perform_at"])
            check_type(argname="argument time_window", value=time_window, expected_type=type_hints["time_window"])
            check_type(argname="argument update_level", value=update_level, expected_type=type_hints["update_level"])
        self._values: typing.Dict[str, typing.Any] = {}
        if perform_at is not None:
            self._values["perform_at"] = perform_at
        if time_window is not None:
            self._values["time_window"] = time_window
        if update_level is not None:
            self._values["update_level"] = update_level

    @builtins.property
    def perform_at(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#perform_at ElastigroupAwsBeanstalk#perform_at}.'''
        result = self._values.get("perform_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_window(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#time_window ElastigroupAwsBeanstalk#time_window}.'''
        result = self._values.get("time_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#update_level ElastigroupAwsBeanstalk#update_level}.'''
        result = self._values.get("update_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAwsBeanstalkManagedActionsPlatformUpdate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAwsBeanstalkManagedActionsPlatformUpdateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAwsBeanstalk.ElastigroupAwsBeanstalkManagedActionsPlatformUpdateOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkManagedActionsPlatformUpdateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPerformAt")
    def reset_perform_at(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerformAt", []))

    @jsii.member(jsii_name="resetTimeWindow")
    def reset_time_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeWindow", []))

    @jsii.member(jsii_name="resetUpdateLevel")
    def reset_update_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdateLevel", []))

    @builtins.property
    @jsii.member(jsii_name="performAtInput")
    def perform_at_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "performAtInput"))

    @builtins.property
    @jsii.member(jsii_name="timeWindowInput")
    def time_window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="updateLevelInput")
    def update_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="performAt")
    def perform_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "performAt"))

    @perform_at.setter
    def perform_at(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkManagedActionsPlatformUpdateOutputReference, "perform_at").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "performAt", value)

    @builtins.property
    @jsii.member(jsii_name="timeWindow")
    def time_window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeWindow"))

    @time_window.setter
    def time_window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkManagedActionsPlatformUpdateOutputReference, "time_window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeWindow", value)

    @builtins.property
    @jsii.member(jsii_name="updateLevel")
    def update_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateLevel"))

    @update_level.setter
    def update_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkManagedActionsPlatformUpdateOutputReference, "update_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updateLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElastigroupAwsBeanstalkManagedActionsPlatformUpdate]:
        return typing.cast(typing.Optional[ElastigroupAwsBeanstalkManagedActionsPlatformUpdate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastigroupAwsBeanstalkManagedActionsPlatformUpdate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkManagedActionsPlatformUpdateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAwsBeanstalk.ElastigroupAwsBeanstalkScheduledTask",
    jsii_struct_bases=[],
    name_mapping={
        "task_type": "taskType",
        "adjustment": "adjustment",
        "adjustment_percentage": "adjustmentPercentage",
        "batch_size_percentage": "batchSizePercentage",
        "cron_expression": "cronExpression",
        "frequency": "frequency",
        "grace_period": "gracePeriod",
        "is_enabled": "isEnabled",
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "scale_max_capacity": "scaleMaxCapacity",
        "scale_min_capacity": "scaleMinCapacity",
        "scale_target_capacity": "scaleTargetCapacity",
        "start_time": "startTime",
        "target_capacity": "targetCapacity",
    },
)
class ElastigroupAwsBeanstalkScheduledTask:
    def __init__(
        self,
        *,
        task_type: builtins.str,
        adjustment: typing.Optional[builtins.str] = None,
        adjustment_percentage: typing.Optional[builtins.str] = None,
        batch_size_percentage: typing.Optional[builtins.str] = None,
        cron_expression: typing.Optional[builtins.str] = None,
        frequency: typing.Optional[builtins.str] = None,
        grace_period: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_capacity: typing.Optional[builtins.str] = None,
        min_capacity: typing.Optional[builtins.str] = None,
        scale_max_capacity: typing.Optional[builtins.str] = None,
        scale_min_capacity: typing.Optional[builtins.str] = None,
        scale_target_capacity: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        target_capacity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param task_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#task_type ElastigroupAwsBeanstalk#task_type}.
        :param adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#adjustment ElastigroupAwsBeanstalk#adjustment}.
        :param adjustment_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#adjustment_percentage ElastigroupAwsBeanstalk#adjustment_percentage}.
        :param batch_size_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#batch_size_percentage ElastigroupAwsBeanstalk#batch_size_percentage}.
        :param cron_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#cron_expression ElastigroupAwsBeanstalk#cron_expression}.
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#frequency ElastigroupAwsBeanstalk#frequency}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#grace_period ElastigroupAwsBeanstalk#grace_period}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#is_enabled ElastigroupAwsBeanstalk#is_enabled}.
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#max_capacity ElastigroupAwsBeanstalk#max_capacity}.
        :param min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#min_capacity ElastigroupAwsBeanstalk#min_capacity}.
        :param scale_max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#scale_max_capacity ElastigroupAwsBeanstalk#scale_max_capacity}.
        :param scale_min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#scale_min_capacity ElastigroupAwsBeanstalk#scale_min_capacity}.
        :param scale_target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#scale_target_capacity ElastigroupAwsBeanstalk#scale_target_capacity}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#start_time ElastigroupAwsBeanstalk#start_time}.
        :param target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#target_capacity ElastigroupAwsBeanstalk#target_capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkScheduledTask.__init__)
            check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
            check_type(argname="argument adjustment", value=adjustment, expected_type=type_hints["adjustment"])
            check_type(argname="argument adjustment_percentage", value=adjustment_percentage, expected_type=type_hints["adjustment_percentage"])
            check_type(argname="argument batch_size_percentage", value=batch_size_percentage, expected_type=type_hints["batch_size_percentage"])
            check_type(argname="argument cron_expression", value=cron_expression, expected_type=type_hints["cron_expression"])
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument grace_period", value=grace_period, expected_type=type_hints["grace_period"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
            check_type(argname="argument scale_max_capacity", value=scale_max_capacity, expected_type=type_hints["scale_max_capacity"])
            check_type(argname="argument scale_min_capacity", value=scale_min_capacity, expected_type=type_hints["scale_min_capacity"])
            check_type(argname="argument scale_target_capacity", value=scale_target_capacity, expected_type=type_hints["scale_target_capacity"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument target_capacity", value=target_capacity, expected_type=type_hints["target_capacity"])
        self._values: typing.Dict[str, typing.Any] = {
            "task_type": task_type,
        }
        if adjustment is not None:
            self._values["adjustment"] = adjustment
        if adjustment_percentage is not None:
            self._values["adjustment_percentage"] = adjustment_percentage
        if batch_size_percentage is not None:
            self._values["batch_size_percentage"] = batch_size_percentage
        if cron_expression is not None:
            self._values["cron_expression"] = cron_expression
        if frequency is not None:
            self._values["frequency"] = frequency
        if grace_period is not None:
            self._values["grace_period"] = grace_period
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity
        if scale_max_capacity is not None:
            self._values["scale_max_capacity"] = scale_max_capacity
        if scale_min_capacity is not None:
            self._values["scale_min_capacity"] = scale_min_capacity
        if scale_target_capacity is not None:
            self._values["scale_target_capacity"] = scale_target_capacity
        if start_time is not None:
            self._values["start_time"] = start_time
        if target_capacity is not None:
            self._values["target_capacity"] = target_capacity

    @builtins.property
    def task_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#task_type ElastigroupAwsBeanstalk#task_type}.'''
        result = self._values.get("task_type")
        assert result is not None, "Required property 'task_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def adjustment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#adjustment ElastigroupAwsBeanstalk#adjustment}.'''
        result = self._values.get("adjustment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def adjustment_percentage(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#adjustment_percentage ElastigroupAwsBeanstalk#adjustment_percentage}.'''
        result = self._values.get("adjustment_percentage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def batch_size_percentage(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#batch_size_percentage ElastigroupAwsBeanstalk#batch_size_percentage}.'''
        result = self._values.get("batch_size_percentage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cron_expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#cron_expression ElastigroupAwsBeanstalk#cron_expression}.'''
        result = self._values.get("cron_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def frequency(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#frequency ElastigroupAwsBeanstalk#frequency}.'''
        result = self._values.get("frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grace_period(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#grace_period ElastigroupAwsBeanstalk#grace_period}.'''
        result = self._values.get("grace_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#is_enabled ElastigroupAwsBeanstalk#is_enabled}.'''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#max_capacity ElastigroupAwsBeanstalk#max_capacity}.'''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#min_capacity ElastigroupAwsBeanstalk#min_capacity}.'''
        result = self._values.get("min_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_max_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#scale_max_capacity ElastigroupAwsBeanstalk#scale_max_capacity}.'''
        result = self._values.get("scale_max_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_min_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#scale_min_capacity ElastigroupAwsBeanstalk#scale_min_capacity}.'''
        result = self._values.get("scale_min_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#scale_target_capacity ElastigroupAwsBeanstalk#scale_target_capacity}.'''
        result = self._values.get("scale_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#start_time ElastigroupAwsBeanstalk#start_time}.'''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk#target_capacity ElastigroupAwsBeanstalk#target_capacity}.'''
        result = self._values.get("target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAwsBeanstalkScheduledTask(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAwsBeanstalkScheduledTaskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAwsBeanstalk.ElastigroupAwsBeanstalkScheduledTaskList",
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
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkScheduledTaskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupAwsBeanstalkScheduledTaskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkScheduledTaskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAwsBeanstalkScheduledTaskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAwsBeanstalkScheduledTask]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAwsBeanstalkScheduledTask]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAwsBeanstalkScheduledTask]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAwsBeanstalkScheduledTaskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAwsBeanstalk.ElastigroupAwsBeanstalkScheduledTaskOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAwsBeanstalkScheduledTaskOutputReference.__init__)
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

    @jsii.member(jsii_name="resetCronExpression")
    def reset_cron_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCronExpression", []))

    @jsii.member(jsii_name="resetFrequency")
    def reset_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrequency", []))

    @jsii.member(jsii_name="resetGracePeriod")
    def reset_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGracePeriod", []))

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetMaxCapacity")
    def reset_max_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxCapacity", []))

    @jsii.member(jsii_name="resetMinCapacity")
    def reset_min_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCapacity", []))

    @jsii.member(jsii_name="resetScaleMaxCapacity")
    def reset_scale_max_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleMaxCapacity", []))

    @jsii.member(jsii_name="resetScaleMinCapacity")
    def reset_scale_min_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleMinCapacity", []))

    @jsii.member(jsii_name="resetScaleTargetCapacity")
    def reset_scale_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleTargetCapacity", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @jsii.member(jsii_name="resetTargetCapacity")
    def reset_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetCapacity", []))

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
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frequencyInput"))

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
    @jsii.member(jsii_name="maxCapacityInput")
    def max_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="minCapacityInput")
    def min_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minCapacityInput"))

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
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetCapacityInput")
    def target_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetCapacityInput"))

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
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "adjustment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustment", value)

    @builtins.property
    @jsii.member(jsii_name="adjustmentPercentage")
    def adjustment_percentage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adjustmentPercentage"))

    @adjustment_percentage.setter
    def adjustment_percentage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "adjustment_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustmentPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="batchSizePercentage")
    def batch_size_percentage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "batchSizePercentage"))

    @batch_size_percentage.setter
    def batch_size_percentage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "batch_size_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchSizePercentage", value)

    @builtins.property
    @jsii.member(jsii_name="cronExpression")
    def cron_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cronExpression"))

    @cron_expression.setter
    def cron_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "cron_expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cronExpression", value)

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="gracePeriod")
    def grace_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gracePeriod"))

    @grace_period.setter
    def grace_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "grace_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "max_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="minCapacity")
    def min_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minCapacity"))

    @min_capacity.setter
    def min_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "min_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="scaleMaxCapacity")
    def scale_max_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleMaxCapacity"))

    @scale_max_capacity.setter
    def scale_max_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "scale_max_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleMaxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="scaleMinCapacity")
    def scale_min_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleMinCapacity"))

    @scale_min_capacity.setter
    def scale_min_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "scale_min_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleMinCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="scaleTargetCapacity")
    def scale_target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleTargetCapacity"))

    @scale_target_capacity.setter
    def scale_target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "scale_target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleTargetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="targetCapacity")
    def target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetCapacity"))

    @target_capacity.setter
    def target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskType"))

    @task_type.setter
    def task_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "task_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAwsBeanstalkScheduledTask, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAwsBeanstalkScheduledTask, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAwsBeanstalkScheduledTask, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAwsBeanstalkScheduledTaskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ElastigroupAwsBeanstalk",
    "ElastigroupAwsBeanstalkConfig",
    "ElastigroupAwsBeanstalkDeploymentPreferences",
    "ElastigroupAwsBeanstalkDeploymentPreferencesOutputReference",
    "ElastigroupAwsBeanstalkDeploymentPreferencesStrategy",
    "ElastigroupAwsBeanstalkDeploymentPreferencesStrategyList",
    "ElastigroupAwsBeanstalkDeploymentPreferencesStrategyOutputReference",
    "ElastigroupAwsBeanstalkManagedActions",
    "ElastigroupAwsBeanstalkManagedActionsOutputReference",
    "ElastigroupAwsBeanstalkManagedActionsPlatformUpdate",
    "ElastigroupAwsBeanstalkManagedActionsPlatformUpdateOutputReference",
    "ElastigroupAwsBeanstalkScheduledTask",
    "ElastigroupAwsBeanstalkScheduledTaskList",
    "ElastigroupAwsBeanstalkScheduledTaskOutputReference",
]

publication.publish()
