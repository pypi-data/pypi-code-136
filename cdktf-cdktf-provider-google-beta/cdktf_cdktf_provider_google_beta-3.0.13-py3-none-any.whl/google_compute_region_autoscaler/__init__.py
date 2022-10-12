'''
# `google_compute_region_autoscaler`

Refer to the Terraform Registory for docs: [`google_compute_region_autoscaler`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler).
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


class GoogleComputeRegionAutoscaler(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscaler",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler google_compute_region_autoscaler}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        autoscaling_policy: typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicy", typing.Dict[str, typing.Any]],
        name: builtins.str,
        target: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRegionAutoscalerTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler google_compute_region_autoscaler} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param autoscaling_policy: autoscaling_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#autoscaling_policy GoogleComputeRegionAutoscaler#autoscaling_policy}
        :param name: Name of the resource. The name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#name GoogleComputeRegionAutoscaler#name}
        :param target: URL of the managed instance group that this autoscaler will scale. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#target GoogleComputeRegionAutoscaler#target}
        :param description: An optional description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#description GoogleComputeRegionAutoscaler#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#id GoogleComputeRegionAutoscaler#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#project GoogleComputeRegionAutoscaler#project}.
        :param region: URL of the region where the instance group resides. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#region GoogleComputeRegionAutoscaler#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#timeouts GoogleComputeRegionAutoscaler#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscaler.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeRegionAutoscalerConfig(
            autoscaling_policy=autoscaling_policy,
            name=name,
            target=target,
            description=description,
            id=id,
            project=project,
            region=region,
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

    @jsii.member(jsii_name="putAutoscalingPolicy")
    def put_autoscaling_policy(
        self,
        *,
        max_replicas: jsii.Number,
        min_replicas: jsii.Number,
        cooldown_period: typing.Optional[jsii.Number] = None,
        cpu_utilization: typing.Optional[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization", typing.Dict[str, typing.Any]]] = None,
        load_balancing_utilization: typing.Optional[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization", typing.Dict[str, typing.Any]]] = None,
        metric: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyMetric", typing.Dict[str, typing.Any]]]]] = None,
        mode: typing.Optional[builtins.str] = None,
        scale_down_control: typing.Optional[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl", typing.Dict[str, typing.Any]]] = None,
        scale_in_control: typing.Optional[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl", typing.Dict[str, typing.Any]]] = None,
        scaling_schedules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param max_replicas: The maximum number of instances that the autoscaler can scale up to. This is required when creating or updating an autoscaler. The maximum number of replicas should not be lower than minimal number of replicas. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#max_replicas GoogleComputeRegionAutoscaler#max_replicas}
        :param min_replicas: The minimum number of replicas that the autoscaler can scale down to. This cannot be less than 0. If not provided, autoscaler will choose a default value depending on maximum number of instances allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#min_replicas GoogleComputeRegionAutoscaler#min_replicas}
        :param cooldown_period: The number of seconds that the autoscaler should wait before it starts collecting information from a new instance. This prevents the autoscaler from collecting information when the instance is initializing, during which the collected usage would not be reliable. The default time autoscaler waits is 60 seconds. Virtual machine initialization times might vary because of numerous factors. We recommend that you test how long an instance may take to initialize. To do this, create an instance and time the startup process. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#cooldown_period GoogleComputeRegionAutoscaler#cooldown_period}
        :param cpu_utilization: cpu_utilization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#cpu_utilization GoogleComputeRegionAutoscaler#cpu_utilization}
        :param load_balancing_utilization: load_balancing_utilization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#load_balancing_utilization GoogleComputeRegionAutoscaler#load_balancing_utilization}
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#metric GoogleComputeRegionAutoscaler#metric}
        :param mode: Defines operating mode for this policy. Default value: "ON" Possible values: ["OFF", "ONLY_UP", "ON"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#mode GoogleComputeRegionAutoscaler#mode}
        :param scale_down_control: scale_down_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#scale_down_control GoogleComputeRegionAutoscaler#scale_down_control}
        :param scale_in_control: scale_in_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#scale_in_control GoogleComputeRegionAutoscaler#scale_in_control}
        :param scaling_schedules: scaling_schedules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#scaling_schedules GoogleComputeRegionAutoscaler#scaling_schedules}
        '''
        value = GoogleComputeRegionAutoscalerAutoscalingPolicy(
            max_replicas=max_replicas,
            min_replicas=min_replicas,
            cooldown_period=cooldown_period,
            cpu_utilization=cpu_utilization,
            load_balancing_utilization=load_balancing_utilization,
            metric=metric,
            mode=mode,
            scale_down_control=scale_down_control,
            scale_in_control=scale_in_control,
            scaling_schedules=scaling_schedules,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscalingPolicy", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#create GoogleComputeRegionAutoscaler#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#delete GoogleComputeRegionAutoscaler#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#update GoogleComputeRegionAutoscaler#update}.
        '''
        value = GoogleComputeRegionAutoscalerTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

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
    @jsii.member(jsii_name="autoscalingPolicy")
    def autoscaling_policy(
        self,
    ) -> "GoogleComputeRegionAutoscalerAutoscalingPolicyOutputReference":
        return typing.cast("GoogleComputeRegionAutoscalerAutoscalingPolicyOutputReference", jsii.get(self, "autoscalingPolicy"))

    @builtins.property
    @jsii.member(jsii_name="creationTimestamp")
    def creation_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeRegionAutoscalerTimeoutsOutputReference":
        return typing.cast("GoogleComputeRegionAutoscalerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingPolicyInput")
    def autoscaling_policy_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicy"]:
        return typing.cast(typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicy"], jsii.get(self, "autoscalingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

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
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeRegionAutoscalerTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeRegionAutoscalerTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscaler, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscaler, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscaler, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscaler, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscaler, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscaler, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "max_replicas": "maxReplicas",
        "min_replicas": "minReplicas",
        "cooldown_period": "cooldownPeriod",
        "cpu_utilization": "cpuUtilization",
        "load_balancing_utilization": "loadBalancingUtilization",
        "metric": "metric",
        "mode": "mode",
        "scale_down_control": "scaleDownControl",
        "scale_in_control": "scaleInControl",
        "scaling_schedules": "scalingSchedules",
    },
)
class GoogleComputeRegionAutoscalerAutoscalingPolicy:
    def __init__(
        self,
        *,
        max_replicas: jsii.Number,
        min_replicas: jsii.Number,
        cooldown_period: typing.Optional[jsii.Number] = None,
        cpu_utilization: typing.Optional[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization", typing.Dict[str, typing.Any]]] = None,
        load_balancing_utilization: typing.Optional[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization", typing.Dict[str, typing.Any]]] = None,
        metric: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyMetric", typing.Dict[str, typing.Any]]]]] = None,
        mode: typing.Optional[builtins.str] = None,
        scale_down_control: typing.Optional[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl", typing.Dict[str, typing.Any]]] = None,
        scale_in_control: typing.Optional[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl", typing.Dict[str, typing.Any]]] = None,
        scaling_schedules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param max_replicas: The maximum number of instances that the autoscaler can scale up to. This is required when creating or updating an autoscaler. The maximum number of replicas should not be lower than minimal number of replicas. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#max_replicas GoogleComputeRegionAutoscaler#max_replicas}
        :param min_replicas: The minimum number of replicas that the autoscaler can scale down to. This cannot be less than 0. If not provided, autoscaler will choose a default value depending on maximum number of instances allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#min_replicas GoogleComputeRegionAutoscaler#min_replicas}
        :param cooldown_period: The number of seconds that the autoscaler should wait before it starts collecting information from a new instance. This prevents the autoscaler from collecting information when the instance is initializing, during which the collected usage would not be reliable. The default time autoscaler waits is 60 seconds. Virtual machine initialization times might vary because of numerous factors. We recommend that you test how long an instance may take to initialize. To do this, create an instance and time the startup process. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#cooldown_period GoogleComputeRegionAutoscaler#cooldown_period}
        :param cpu_utilization: cpu_utilization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#cpu_utilization GoogleComputeRegionAutoscaler#cpu_utilization}
        :param load_balancing_utilization: load_balancing_utilization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#load_balancing_utilization GoogleComputeRegionAutoscaler#load_balancing_utilization}
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#metric GoogleComputeRegionAutoscaler#metric}
        :param mode: Defines operating mode for this policy. Default value: "ON" Possible values: ["OFF", "ONLY_UP", "ON"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#mode GoogleComputeRegionAutoscaler#mode}
        :param scale_down_control: scale_down_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#scale_down_control GoogleComputeRegionAutoscaler#scale_down_control}
        :param scale_in_control: scale_in_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#scale_in_control GoogleComputeRegionAutoscaler#scale_in_control}
        :param scaling_schedules: scaling_schedules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#scaling_schedules GoogleComputeRegionAutoscaler#scaling_schedules}
        '''
        if isinstance(cpu_utilization, dict):
            cpu_utilization = GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization(**cpu_utilization)
        if isinstance(load_balancing_utilization, dict):
            load_balancing_utilization = GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization(**load_balancing_utilization)
        if isinstance(scale_down_control, dict):
            scale_down_control = GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl(**scale_down_control)
        if isinstance(scale_in_control, dict):
            scale_in_control = GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl(**scale_in_control)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicy.__init__)
            check_type(argname="argument max_replicas", value=max_replicas, expected_type=type_hints["max_replicas"])
            check_type(argname="argument min_replicas", value=min_replicas, expected_type=type_hints["min_replicas"])
            check_type(argname="argument cooldown_period", value=cooldown_period, expected_type=type_hints["cooldown_period"])
            check_type(argname="argument cpu_utilization", value=cpu_utilization, expected_type=type_hints["cpu_utilization"])
            check_type(argname="argument load_balancing_utilization", value=load_balancing_utilization, expected_type=type_hints["load_balancing_utilization"])
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument scale_down_control", value=scale_down_control, expected_type=type_hints["scale_down_control"])
            check_type(argname="argument scale_in_control", value=scale_in_control, expected_type=type_hints["scale_in_control"])
            check_type(argname="argument scaling_schedules", value=scaling_schedules, expected_type=type_hints["scaling_schedules"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_replicas": max_replicas,
            "min_replicas": min_replicas,
        }
        if cooldown_period is not None:
            self._values["cooldown_period"] = cooldown_period
        if cpu_utilization is not None:
            self._values["cpu_utilization"] = cpu_utilization
        if load_balancing_utilization is not None:
            self._values["load_balancing_utilization"] = load_balancing_utilization
        if metric is not None:
            self._values["metric"] = metric
        if mode is not None:
            self._values["mode"] = mode
        if scale_down_control is not None:
            self._values["scale_down_control"] = scale_down_control
        if scale_in_control is not None:
            self._values["scale_in_control"] = scale_in_control
        if scaling_schedules is not None:
            self._values["scaling_schedules"] = scaling_schedules

    @builtins.property
    def max_replicas(self) -> jsii.Number:
        '''The maximum number of instances that the autoscaler can scale up to.

        This is required when creating or updating an autoscaler. The
        maximum number of replicas should not be lower than minimal number
        of replicas.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#max_replicas GoogleComputeRegionAutoscaler#max_replicas}
        '''
        result = self._values.get("max_replicas")
        assert result is not None, "Required property 'max_replicas' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_replicas(self) -> jsii.Number:
        '''The minimum number of replicas that the autoscaler can scale down to.

        This cannot be less than 0. If not provided, autoscaler will
        choose a default value depending on maximum number of instances
        allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#min_replicas GoogleComputeRegionAutoscaler#min_replicas}
        '''
        result = self._values.get("min_replicas")
        assert result is not None, "Required property 'min_replicas' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def cooldown_period(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds that the autoscaler should wait before it starts collecting information from a new instance.

        This prevents
        the autoscaler from collecting information when the instance is
        initializing, during which the collected usage would not be
        reliable. The default time autoscaler waits is 60 seconds.

        Virtual machine initialization times might vary because of
        numerous factors. We recommend that you test how long an
        instance may take to initialize. To do this, create an instance
        and time the startup process.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#cooldown_period GoogleComputeRegionAutoscaler#cooldown_period}
        '''
        result = self._values.get("cooldown_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cpu_utilization(
        self,
    ) -> typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization"]:
        '''cpu_utilization block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#cpu_utilization GoogleComputeRegionAutoscaler#cpu_utilization}
        '''
        result = self._values.get("cpu_utilization")
        return typing.cast(typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization"], result)

    @builtins.property
    def load_balancing_utilization(
        self,
    ) -> typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization"]:
        '''load_balancing_utilization block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#load_balancing_utilization GoogleComputeRegionAutoscaler#load_balancing_utilization}
        '''
        result = self._values.get("load_balancing_utilization")
        return typing.cast(typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization"], result)

    @builtins.property
    def metric(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionAutoscalerAutoscalingPolicyMetric"]]]:
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#metric GoogleComputeRegionAutoscaler#metric}
        '''
        result = self._values.get("metric")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionAutoscalerAutoscalingPolicyMetric"]]], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Defines operating mode for this policy. Default value: "ON" Possible values: ["OFF", "ONLY_UP", "ON"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#mode GoogleComputeRegionAutoscaler#mode}
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_down_control(
        self,
    ) -> typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl"]:
        '''scale_down_control block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#scale_down_control GoogleComputeRegionAutoscaler#scale_down_control}
        '''
        result = self._values.get("scale_down_control")
        return typing.cast(typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl"], result)

    @builtins.property
    def scale_in_control(
        self,
    ) -> typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl"]:
        '''scale_in_control block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#scale_in_control GoogleComputeRegionAutoscaler#scale_in_control}
        '''
        result = self._values.get("scale_in_control")
        return typing.cast(typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl"], result)

    @builtins.property
    def scaling_schedules(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules"]]]:
        '''scaling_schedules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#scaling_schedules GoogleComputeRegionAutoscaler#scaling_schedules}
        '''
        result = self._values.get("scaling_schedules")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionAutoscalerAutoscalingPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization",
    jsii_struct_bases=[],
    name_mapping={"target": "target", "predictive_method": "predictiveMethod"},
)
class GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization:
    def __init__(
        self,
        *,
        target: jsii.Number,
        predictive_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target: The target CPU utilization that the autoscaler should maintain. Must be a float value in the range (0, 1]. If not specified, the default is 0.6. If the CPU level is below the target utilization, the autoscaler scales down the number of instances until it reaches the minimum number of instances you specified or until the average CPU of your instances reaches the target utilization. If the average CPU is above the target utilization, the autoscaler scales up until it reaches the maximum number of instances you specified or until the average utilization reaches the target utilization. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#target GoogleComputeRegionAutoscaler#target}
        :param predictive_method: Indicates whether predictive autoscaling based on CPU metric is enabled. Valid values are:. - NONE (default). No predictive method is used. The autoscaler scales the group to meet current demand based on real-time metrics. - OPTIMIZE_AVAILABILITY. Predictive autoscaling improves availability by monitoring daily and weekly load patterns and scaling out ahead of anticipated demand. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#predictive_method GoogleComputeRegionAutoscaler#predictive_method}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization.__init__)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument predictive_method", value=predictive_method, expected_type=type_hints["predictive_method"])
        self._values: typing.Dict[str, typing.Any] = {
            "target": target,
        }
        if predictive_method is not None:
            self._values["predictive_method"] = predictive_method

    @builtins.property
    def target(self) -> jsii.Number:
        '''The target CPU utilization that the autoscaler should maintain.

        Must be a float value in the range (0, 1]. If not specified, the
        default is 0.6.

        If the CPU level is below the target utilization, the autoscaler
        scales down the number of instances until it reaches the minimum
        number of instances you specified or until the average CPU of
        your instances reaches the target utilization.

        If the average CPU is above the target utilization, the autoscaler
        scales up until it reaches the maximum number of instances you
        specified or until the average utilization reaches the target
        utilization.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#target GoogleComputeRegionAutoscaler#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def predictive_method(self) -> typing.Optional[builtins.str]:
        '''Indicates whether predictive autoscaling based on CPU metric is enabled. Valid values are:.

        - NONE (default). No predictive method is used. The autoscaler scales the group to meet current demand based on real-time metrics.
        - OPTIMIZE_AVAILABILITY. Predictive autoscaling improves availability by monitoring daily and weekly load patterns and scaling out ahead of anticipated demand.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#predictive_method GoogleComputeRegionAutoscaler#predictive_method}
        '''
        result = self._values.get("predictive_method")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilizationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilizationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilizationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPredictiveMethod")
    def reset_predictive_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredictiveMethod", []))

    @builtins.property
    @jsii.member(jsii_name="predictiveMethodInput")
    def predictive_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "predictiveMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="predictiveMethod")
    def predictive_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "predictiveMethod"))

    @predictive_method.setter
    def predictive_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilizationOutputReference, "predictive_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predictiveMethod", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "target"))

    @target.setter
    def target(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilizationOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization]:
        return typing.cast(typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilizationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization",
    jsii_struct_bases=[],
    name_mapping={"target": "target"},
)
class GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization:
    def __init__(self, *, target: jsii.Number) -> None:
        '''
        :param target: Fraction of backend capacity utilization (set in HTTP(s) load balancing configuration) that autoscaler should maintain. Must be a positive float value. If not defined, the default is 0.8. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#target GoogleComputeRegionAutoscaler#target}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization.__init__)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {
            "target": target,
        }

    @builtins.property
    def target(self) -> jsii.Number:
        '''Fraction of backend capacity utilization (set in HTTP(s) load balancing configuration) that autoscaler should maintain.

        Must
        be a positive float value. If not defined, the default is 0.8.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#target GoogleComputeRegionAutoscaler#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilizationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilizationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilizationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "target"))

    @target.setter
    def target(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilizationOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization]:
        return typing.cast(typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilizationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyMetric",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "filter": "filter",
        "single_instance_assignment": "singleInstanceAssignment",
        "target": "target",
        "type": "type",
    },
)
class GoogleComputeRegionAutoscalerAutoscalingPolicyMetric:
    def __init__(
        self,
        *,
        name: builtins.str,
        filter: typing.Optional[builtins.str] = None,
        single_instance_assignment: typing.Optional[jsii.Number] = None,
        target: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The identifier (type) of the Stackdriver Monitoring metric. The metric cannot have negative values. The metric must have a value type of INT64 or DOUBLE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#name GoogleComputeRegionAutoscaler#name}
        :param filter: A filter string to be used as the filter string for a Stackdriver Monitoring TimeSeries.list API call. This filter is used to select a specific TimeSeries for the purpose of autoscaling and to determine whether the metric is exporting per-instance or per-group data. You can only use the AND operator for joining selectors. You can only use direct equality comparison operator (=) without any functions for each selector. You can specify the metric in both the filter string and in the metric field. However, if specified in both places, the metric must be identical. The monitored resource type determines what kind of values are expected for the metric. If it is a gce_instance, the autoscaler expects the metric to include a separate TimeSeries for each instance in a group. In such a case, you cannot filter on resource labels. If the resource type is any other value, the autoscaler expects this metric to contain values that apply to the entire autoscaled instance group and resource label filtering can be performed to point autoscaler at the correct TimeSeries to scale upon. This is called a per-group metric for the purpose of autoscaling. If not specified, the type defaults to gce_instance. You should provide a filter that is selective enough to pick just one TimeSeries for the autoscaled group or for each of the instances (if you are using gce_instance resource type). If multiple TimeSeries are returned upon the query execution, the autoscaler will sum their respective values to obtain its scaling value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#filter GoogleComputeRegionAutoscaler#filter}
        :param single_instance_assignment: If scaling is based on a per-group metric value that represents the total amount of work to be done or resource usage, set this value to an amount assigned for a single instance of the scaled group. The autoscaler will keep the number of instances proportional to the value of this metric, the metric itself should not change value due to group resizing. For example, a good metric to use with the target is 'pubsub.googleapis.com/subscription/num_undelivered_messages' or a custom metric exporting the total number of requests coming to your instances. A bad example would be a metric exporting an average or median latency, since this value can't include a chunk assignable to a single instance, it could be better used with utilization_target instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#single_instance_assignment GoogleComputeRegionAutoscaler#single_instance_assignment}
        :param target: The target value of the metric that autoscaler should maintain. This must be a positive value. A utilization metric scales number of virtual machines handling requests to increase or decrease proportionally to the metric. For example, a good metric to use as a utilizationTarget is www.googleapis.com/compute/instance/network/received_bytes_count. The autoscaler will work to keep this value constant for each of the instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#target GoogleComputeRegionAutoscaler#target}
        :param type: Defines how target utilization value is expressed for a Stackdriver Monitoring metric. Possible values: ["GAUGE", "DELTA_PER_SECOND", "DELTA_PER_MINUTE"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#type GoogleComputeRegionAutoscaler#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyMetric.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument single_instance_assignment", value=single_instance_assignment, expected_type=type_hints["single_instance_assignment"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if filter is not None:
            self._values["filter"] = filter
        if single_instance_assignment is not None:
            self._values["single_instance_assignment"] = single_instance_assignment
        if target is not None:
            self._values["target"] = target
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> builtins.str:
        '''The identifier (type) of the Stackdriver Monitoring metric. The metric cannot have negative values.

        The metric must have a value type of INT64 or DOUBLE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#name GoogleComputeRegionAutoscaler#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter(self) -> typing.Optional[builtins.str]:
        '''A filter string to be used as the filter string for a Stackdriver Monitoring TimeSeries.list API call. This filter is used to select a specific TimeSeries for the purpose of autoscaling and to determine whether the metric is exporting per-instance or per-group data.

        You can only use the AND operator for joining selectors.
        You can only use direct equality comparison operator (=) without
        any functions for each selector.
        You can specify the metric in both the filter string and in the
        metric field. However, if specified in both places, the metric must
        be identical.

        The monitored resource type determines what kind of values are
        expected for the metric. If it is a gce_instance, the autoscaler
        expects the metric to include a separate TimeSeries for each
        instance in a group. In such a case, you cannot filter on resource
        labels.

        If the resource type is any other value, the autoscaler expects
        this metric to contain values that apply to the entire autoscaled
        instance group and resource label filtering can be performed to
        point autoscaler at the correct TimeSeries to scale upon.
        This is called a per-group metric for the purpose of autoscaling.

        If not specified, the type defaults to gce_instance.

        You should provide a filter that is selective enough to pick just
        one TimeSeries for the autoscaled group or for each of the instances
        (if you are using gce_instance resource type). If multiple
        TimeSeries are returned upon the query execution, the autoscaler
        will sum their respective values to obtain its scaling value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#filter GoogleComputeRegionAutoscaler#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_instance_assignment(self) -> typing.Optional[jsii.Number]:
        '''If scaling is based on a per-group metric value that represents the total amount of work to be done or resource usage, set this value to an amount assigned for a single instance of the scaled group.

        The autoscaler will keep the number of instances proportional to the
        value of this metric, the metric itself should not change value due
        to group resizing.

        For example, a good metric to use with the target is
        'pubsub.googleapis.com/subscription/num_undelivered_messages'
        or a custom metric exporting the total number of requests coming to
        your instances.

        A bad example would be a metric exporting an average or median
        latency, since this value can't include a chunk assignable to a
        single instance, it could be better used with utilization_target
        instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#single_instance_assignment GoogleComputeRegionAutoscaler#single_instance_assignment}
        '''
        result = self._values.get("single_instance_assignment")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target(self) -> typing.Optional[jsii.Number]:
        '''The target value of the metric that autoscaler should maintain.

        This must be a positive value. A utilization
        metric scales number of virtual machines handling requests
        to increase or decrease proportionally to the metric.

        For example, a good metric to use as a utilizationTarget is
        www.googleapis.com/compute/instance/network/received_bytes_count.
        The autoscaler will work to keep this value constant for each
        of the instances.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#target GoogleComputeRegionAutoscaler#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Defines how target utilization value is expressed for a Stackdriver Monitoring metric. Possible values: ["GAUGE", "DELTA_PER_SECOND", "DELTA_PER_MINUTE"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#type GoogleComputeRegionAutoscaler#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionAutoscalerAutoscalingPolicyMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionAutoscalerAutoscalingPolicyMetricList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyMetricList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyMetricList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionAutoscalerAutoscalingPolicyMetricOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyMetricList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionAutoscalerAutoscalingPolicyMetricOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyMetricList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyMetricList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyMetricList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionAutoscalerAutoscalingPolicyMetric]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionAutoscalerAutoscalingPolicyMetric]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionAutoscalerAutoscalingPolicyMetric]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyMetricList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionAutoscalerAutoscalingPolicyMetricOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyMetricOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyMetricOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetSingleInstanceAssignment")
    def reset_single_instance_assignment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleInstanceAssignment", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="singleInstanceAssignmentInput")
    def single_instance_assignment_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "singleInstanceAssignmentInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filter"))

    @filter.setter
    def filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyMetricOutputReference, "filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyMetricOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="singleInstanceAssignment")
    def single_instance_assignment(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "singleInstanceAssignment"))

    @single_instance_assignment.setter
    def single_instance_assignment(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyMetricOutputReference, "single_instance_assignment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singleInstanceAssignment", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "target"))

    @target.setter
    def target(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyMetricOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyMetricOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionAutoscalerAutoscalingPolicyMetric, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionAutoscalerAutoscalingPolicyMetric, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionAutoscalerAutoscalingPolicyMetric, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyMetricOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionAutoscalerAutoscalingPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCpuUtilization")
    def put_cpu_utilization(
        self,
        *,
        target: jsii.Number,
        predictive_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target: The target CPU utilization that the autoscaler should maintain. Must be a float value in the range (0, 1]. If not specified, the default is 0.6. If the CPU level is below the target utilization, the autoscaler scales down the number of instances until it reaches the minimum number of instances you specified or until the average CPU of your instances reaches the target utilization. If the average CPU is above the target utilization, the autoscaler scales up until it reaches the maximum number of instances you specified or until the average utilization reaches the target utilization. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#target GoogleComputeRegionAutoscaler#target}
        :param predictive_method: Indicates whether predictive autoscaling based on CPU metric is enabled. Valid values are:. - NONE (default). No predictive method is used. The autoscaler scales the group to meet current demand based on real-time metrics. - OPTIMIZE_AVAILABILITY. Predictive autoscaling improves availability by monitoring daily and weekly load patterns and scaling out ahead of anticipated demand. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#predictive_method GoogleComputeRegionAutoscaler#predictive_method}
        '''
        value = GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization(
            target=target, predictive_method=predictive_method
        )

        return typing.cast(None, jsii.invoke(self, "putCpuUtilization", [value]))

    @jsii.member(jsii_name="putLoadBalancingUtilization")
    def put_load_balancing_utilization(self, *, target: jsii.Number) -> None:
        '''
        :param target: Fraction of backend capacity utilization (set in HTTP(s) load balancing configuration) that autoscaler should maintain. Must be a positive float value. If not defined, the default is 0.8. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#target GoogleComputeRegionAutoscaler#target}
        '''
        value = GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization(
            target=target
        )

        return typing.cast(None, jsii.invoke(self, "putLoadBalancingUtilization", [value]))

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeRegionAutoscalerAutoscalingPolicyMetric, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyOutputReference.put_metric)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

    @jsii.member(jsii_name="putScaleDownControl")
    def put_scale_down_control(
        self,
        *,
        max_scaled_down_replicas: typing.Optional[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas", typing.Dict[str, typing.Any]]] = None,
        time_window_sec: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_scaled_down_replicas: max_scaled_down_replicas block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#max_scaled_down_replicas GoogleComputeRegionAutoscaler#max_scaled_down_replicas}
        :param time_window_sec: How long back autoscaling should look when computing recommendations to include directives regarding slower scale down, as described above. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#time_window_sec GoogleComputeRegionAutoscaler#time_window_sec}
        '''
        value = GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl(
            max_scaled_down_replicas=max_scaled_down_replicas,
            time_window_sec=time_window_sec,
        )

        return typing.cast(None, jsii.invoke(self, "putScaleDownControl", [value]))

    @jsii.member(jsii_name="putScaleInControl")
    def put_scale_in_control(
        self,
        *,
        max_scaled_in_replicas: typing.Optional[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas", typing.Dict[str, typing.Any]]] = None,
        time_window_sec: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_scaled_in_replicas: max_scaled_in_replicas block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#max_scaled_in_replicas GoogleComputeRegionAutoscaler#max_scaled_in_replicas}
        :param time_window_sec: How long back autoscaling should look when computing recommendations to include directives regarding slower scale down, as described above. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#time_window_sec GoogleComputeRegionAutoscaler#time_window_sec}
        '''
        value = GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl(
            max_scaled_in_replicas=max_scaled_in_replicas,
            time_window_sec=time_window_sec,
        )

        return typing.cast(None, jsii.invoke(self, "putScaleInControl", [value]))

    @jsii.member(jsii_name="putScalingSchedules")
    def put_scaling_schedules(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyOutputReference.put_scaling_schedules)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScalingSchedules", [value]))

    @jsii.member(jsii_name="resetCooldownPeriod")
    def reset_cooldown_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCooldownPeriod", []))

    @jsii.member(jsii_name="resetCpuUtilization")
    def reset_cpu_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuUtilization", []))

    @jsii.member(jsii_name="resetLoadBalancingUtilization")
    def reset_load_balancing_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancingUtilization", []))

    @jsii.member(jsii_name="resetMetric")
    def reset_metric(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetric", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetScaleDownControl")
    def reset_scale_down_control(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleDownControl", []))

    @jsii.member(jsii_name="resetScaleInControl")
    def reset_scale_in_control(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleInControl", []))

    @jsii.member(jsii_name="resetScalingSchedules")
    def reset_scaling_schedules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScalingSchedules", []))

    @builtins.property
    @jsii.member(jsii_name="cpuUtilization")
    def cpu_utilization(
        self,
    ) -> GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilizationOutputReference:
        return typing.cast(GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilizationOutputReference, jsii.get(self, "cpuUtilization"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingUtilization")
    def load_balancing_utilization(
        self,
    ) -> GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilizationOutputReference:
        return typing.cast(GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilizationOutputReference, jsii.get(self, "loadBalancingUtilization"))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(self) -> GoogleComputeRegionAutoscalerAutoscalingPolicyMetricList:
        return typing.cast(GoogleComputeRegionAutoscalerAutoscalingPolicyMetricList, jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownControl")
    def scale_down_control(
        self,
    ) -> "GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlOutputReference":
        return typing.cast("GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlOutputReference", jsii.get(self, "scaleDownControl"))

    @builtins.property
    @jsii.member(jsii_name="scaleInControl")
    def scale_in_control(
        self,
    ) -> "GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlOutputReference":
        return typing.cast("GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlOutputReference", jsii.get(self, "scaleInControl"))

    @builtins.property
    @jsii.member(jsii_name="scalingSchedules")
    def scaling_schedules(
        self,
    ) -> "GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesList":
        return typing.cast("GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesList", jsii.get(self, "scalingSchedules"))

    @builtins.property
    @jsii.member(jsii_name="cooldownPeriodInput")
    def cooldown_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cooldownPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuUtilizationInput")
    def cpu_utilization_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization]:
        return typing.cast(typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization], jsii.get(self, "cpuUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingUtilizationInput")
    def load_balancing_utilization_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization]:
        return typing.cast(typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization], jsii.get(self, "loadBalancingUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="maxReplicasInput")
    def max_replicas_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxReplicasInput"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionAutoscalerAutoscalingPolicyMetric]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionAutoscalerAutoscalingPolicyMetric]]], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="minReplicasInput")
    def min_replicas_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minReplicasInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownControlInput")
    def scale_down_control_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl"]:
        return typing.cast(typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl"], jsii.get(self, "scaleDownControlInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleInControlInput")
    def scale_in_control_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl"]:
        return typing.cast(typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl"], jsii.get(self, "scaleInControlInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingSchedulesInput")
    def scaling_schedules_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules"]]], jsii.get(self, "scalingSchedulesInput"))

    @builtins.property
    @jsii.member(jsii_name="cooldownPeriod")
    def cooldown_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cooldownPeriod"))

    @cooldown_period.setter
    def cooldown_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyOutputReference, "cooldown_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cooldownPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="maxReplicas")
    def max_replicas(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxReplicas"))

    @max_replicas.setter
    def max_replicas(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyOutputReference, "max_replicas").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxReplicas", value)

    @builtins.property
    @jsii.member(jsii_name="minReplicas")
    def min_replicas(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minReplicas"))

    @min_replicas.setter
    def min_replicas(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyOutputReference, "min_replicas").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minReplicas", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicy]:
        return typing.cast(typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl",
    jsii_struct_bases=[],
    name_mapping={
        "max_scaled_down_replicas": "maxScaledDownReplicas",
        "time_window_sec": "timeWindowSec",
    },
)
class GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl:
    def __init__(
        self,
        *,
        max_scaled_down_replicas: typing.Optional[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas", typing.Dict[str, typing.Any]]] = None,
        time_window_sec: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_scaled_down_replicas: max_scaled_down_replicas block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#max_scaled_down_replicas GoogleComputeRegionAutoscaler#max_scaled_down_replicas}
        :param time_window_sec: How long back autoscaling should look when computing recommendations to include directives regarding slower scale down, as described above. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#time_window_sec GoogleComputeRegionAutoscaler#time_window_sec}
        '''
        if isinstance(max_scaled_down_replicas, dict):
            max_scaled_down_replicas = GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas(**max_scaled_down_replicas)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl.__init__)
            check_type(argname="argument max_scaled_down_replicas", value=max_scaled_down_replicas, expected_type=type_hints["max_scaled_down_replicas"])
            check_type(argname="argument time_window_sec", value=time_window_sec, expected_type=type_hints["time_window_sec"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_scaled_down_replicas is not None:
            self._values["max_scaled_down_replicas"] = max_scaled_down_replicas
        if time_window_sec is not None:
            self._values["time_window_sec"] = time_window_sec

    @builtins.property
    def max_scaled_down_replicas(
        self,
    ) -> typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas"]:
        '''max_scaled_down_replicas block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#max_scaled_down_replicas GoogleComputeRegionAutoscaler#max_scaled_down_replicas}
        '''
        result = self._values.get("max_scaled_down_replicas")
        return typing.cast(typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas"], result)

    @builtins.property
    def time_window_sec(self) -> typing.Optional[jsii.Number]:
        '''How long back autoscaling should look when computing recommendations to include directives regarding slower scale down, as described above.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#time_window_sec GoogleComputeRegionAutoscaler#time_window_sec}
        '''
        result = self._values.get("time_window_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas",
    jsii_struct_bases=[],
    name_mapping={"fixed": "fixed", "percent": "percent"},
)
class GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas:
    def __init__(
        self,
        *,
        fixed: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fixed: Specifies a fixed number of VM instances. This must be a positive integer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#fixed GoogleComputeRegionAutoscaler#fixed}
        :param percent: Specifies a percentage of instances between 0 to 100%, inclusive. For example, specify 80 for 80%. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#percent GoogleComputeRegionAutoscaler#percent}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas.__init__)
            check_type(argname="argument fixed", value=fixed, expected_type=type_hints["fixed"])
            check_type(argname="argument percent", value=percent, expected_type=type_hints["percent"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fixed is not None:
            self._values["fixed"] = fixed
        if percent is not None:
            self._values["percent"] = percent

    @builtins.property
    def fixed(self) -> typing.Optional[jsii.Number]:
        '''Specifies a fixed number of VM instances. This must be a positive integer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#fixed GoogleComputeRegionAutoscaler#fixed}
        '''
        result = self._values.get("fixed")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def percent(self) -> typing.Optional[jsii.Number]:
        '''Specifies a percentage of instances between 0 to 100%, inclusive. For example, specify 80 for 80%.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#percent GoogleComputeRegionAutoscaler#percent}
        '''
        result = self._values.get("percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicasOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicasOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicasOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFixed")
    def reset_fixed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFixed", []))

    @jsii.member(jsii_name="resetPercent")
    def reset_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercent", []))

    @builtins.property
    @jsii.member(jsii_name="fixedInput")
    def fixed_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fixedInput"))

    @builtins.property
    @jsii.member(jsii_name="percentInput")
    def percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentInput"))

    @builtins.property
    @jsii.member(jsii_name="fixed")
    def fixed(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fixed"))

    @fixed.setter
    def fixed(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicasOutputReference, "fixed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fixed", value)

    @builtins.property
    @jsii.member(jsii_name="percent")
    def percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percent"))

    @percent.setter
    def percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicasOutputReference, "percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas]:
        return typing.cast(typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicasOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMaxScaledDownReplicas")
    def put_max_scaled_down_replicas(
        self,
        *,
        fixed: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fixed: Specifies a fixed number of VM instances. This must be a positive integer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#fixed GoogleComputeRegionAutoscaler#fixed}
        :param percent: Specifies a percentage of instances between 0 to 100%, inclusive. For example, specify 80 for 80%. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#percent GoogleComputeRegionAutoscaler#percent}
        '''
        value = GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas(
            fixed=fixed, percent=percent
        )

        return typing.cast(None, jsii.invoke(self, "putMaxScaledDownReplicas", [value]))

    @jsii.member(jsii_name="resetMaxScaledDownReplicas")
    def reset_max_scaled_down_replicas(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxScaledDownReplicas", []))

    @jsii.member(jsii_name="resetTimeWindowSec")
    def reset_time_window_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeWindowSec", []))

    @builtins.property
    @jsii.member(jsii_name="maxScaledDownReplicas")
    def max_scaled_down_replicas(
        self,
    ) -> GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicasOutputReference:
        return typing.cast(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicasOutputReference, jsii.get(self, "maxScaledDownReplicas"))

    @builtins.property
    @jsii.member(jsii_name="maxScaledDownReplicasInput")
    def max_scaled_down_replicas_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas]:
        return typing.cast(typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas], jsii.get(self, "maxScaledDownReplicasInput"))

    @builtins.property
    @jsii.member(jsii_name="timeWindowSecInput")
    def time_window_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeWindowSecInput"))

    @builtins.property
    @jsii.member(jsii_name="timeWindowSec")
    def time_window_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeWindowSec"))

    @time_window_sec.setter
    def time_window_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlOutputReference, "time_window_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeWindowSec", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl]:
        return typing.cast(typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl",
    jsii_struct_bases=[],
    name_mapping={
        "max_scaled_in_replicas": "maxScaledInReplicas",
        "time_window_sec": "timeWindowSec",
    },
)
class GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl:
    def __init__(
        self,
        *,
        max_scaled_in_replicas: typing.Optional[typing.Union["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas", typing.Dict[str, typing.Any]]] = None,
        time_window_sec: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_scaled_in_replicas: max_scaled_in_replicas block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#max_scaled_in_replicas GoogleComputeRegionAutoscaler#max_scaled_in_replicas}
        :param time_window_sec: How long back autoscaling should look when computing recommendations to include directives regarding slower scale down, as described above. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#time_window_sec GoogleComputeRegionAutoscaler#time_window_sec}
        '''
        if isinstance(max_scaled_in_replicas, dict):
            max_scaled_in_replicas = GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas(**max_scaled_in_replicas)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl.__init__)
            check_type(argname="argument max_scaled_in_replicas", value=max_scaled_in_replicas, expected_type=type_hints["max_scaled_in_replicas"])
            check_type(argname="argument time_window_sec", value=time_window_sec, expected_type=type_hints["time_window_sec"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_scaled_in_replicas is not None:
            self._values["max_scaled_in_replicas"] = max_scaled_in_replicas
        if time_window_sec is not None:
            self._values["time_window_sec"] = time_window_sec

    @builtins.property
    def max_scaled_in_replicas(
        self,
    ) -> typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas"]:
        '''max_scaled_in_replicas block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#max_scaled_in_replicas GoogleComputeRegionAutoscaler#max_scaled_in_replicas}
        '''
        result = self._values.get("max_scaled_in_replicas")
        return typing.cast(typing.Optional["GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas"], result)

    @builtins.property
    def time_window_sec(self) -> typing.Optional[jsii.Number]:
        '''How long back autoscaling should look when computing recommendations to include directives regarding slower scale down, as described above.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#time_window_sec GoogleComputeRegionAutoscaler#time_window_sec}
        '''
        result = self._values.get("time_window_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas",
    jsii_struct_bases=[],
    name_mapping={"fixed": "fixed", "percent": "percent"},
)
class GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas:
    def __init__(
        self,
        *,
        fixed: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fixed: Specifies a fixed number of VM instances. This must be a positive integer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#fixed GoogleComputeRegionAutoscaler#fixed}
        :param percent: Specifies a percentage of instances between 0 to 100%, inclusive. For example, specify 80 for 80%. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#percent GoogleComputeRegionAutoscaler#percent}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas.__init__)
            check_type(argname="argument fixed", value=fixed, expected_type=type_hints["fixed"])
            check_type(argname="argument percent", value=percent, expected_type=type_hints["percent"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fixed is not None:
            self._values["fixed"] = fixed
        if percent is not None:
            self._values["percent"] = percent

    @builtins.property
    def fixed(self) -> typing.Optional[jsii.Number]:
        '''Specifies a fixed number of VM instances. This must be a positive integer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#fixed GoogleComputeRegionAutoscaler#fixed}
        '''
        result = self._values.get("fixed")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def percent(self) -> typing.Optional[jsii.Number]:
        '''Specifies a percentage of instances between 0 to 100%, inclusive. For example, specify 80 for 80%.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#percent GoogleComputeRegionAutoscaler#percent}
        '''
        result = self._values.get("percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicasOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicasOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicasOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFixed")
    def reset_fixed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFixed", []))

    @jsii.member(jsii_name="resetPercent")
    def reset_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercent", []))

    @builtins.property
    @jsii.member(jsii_name="fixedInput")
    def fixed_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fixedInput"))

    @builtins.property
    @jsii.member(jsii_name="percentInput")
    def percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentInput"))

    @builtins.property
    @jsii.member(jsii_name="fixed")
    def fixed(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fixed"))

    @fixed.setter
    def fixed(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicasOutputReference, "fixed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fixed", value)

    @builtins.property
    @jsii.member(jsii_name="percent")
    def percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percent"))

    @percent.setter
    def percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicasOutputReference, "percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas]:
        return typing.cast(typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicasOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMaxScaledInReplicas")
    def put_max_scaled_in_replicas(
        self,
        *,
        fixed: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fixed: Specifies a fixed number of VM instances. This must be a positive integer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#fixed GoogleComputeRegionAutoscaler#fixed}
        :param percent: Specifies a percentage of instances between 0 to 100%, inclusive. For example, specify 80 for 80%. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#percent GoogleComputeRegionAutoscaler#percent}
        '''
        value = GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas(
            fixed=fixed, percent=percent
        )

        return typing.cast(None, jsii.invoke(self, "putMaxScaledInReplicas", [value]))

    @jsii.member(jsii_name="resetMaxScaledInReplicas")
    def reset_max_scaled_in_replicas(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxScaledInReplicas", []))

    @jsii.member(jsii_name="resetTimeWindowSec")
    def reset_time_window_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeWindowSec", []))

    @builtins.property
    @jsii.member(jsii_name="maxScaledInReplicas")
    def max_scaled_in_replicas(
        self,
    ) -> GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicasOutputReference:
        return typing.cast(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicasOutputReference, jsii.get(self, "maxScaledInReplicas"))

    @builtins.property
    @jsii.member(jsii_name="maxScaledInReplicasInput")
    def max_scaled_in_replicas_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas]:
        return typing.cast(typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas], jsii.get(self, "maxScaledInReplicasInput"))

    @builtins.property
    @jsii.member(jsii_name="timeWindowSecInput")
    def time_window_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeWindowSecInput"))

    @builtins.property
    @jsii.member(jsii_name="timeWindowSec")
    def time_window_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeWindowSec"))

    @time_window_sec.setter
    def time_window_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlOutputReference, "time_window_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeWindowSec", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl]:
        return typing.cast(typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules",
    jsii_struct_bases=[],
    name_mapping={
        "duration_sec": "durationSec",
        "min_required_replicas": "minRequiredReplicas",
        "name": "name",
        "schedule": "schedule",
        "description": "description",
        "disabled": "disabled",
        "time_zone": "timeZone",
    },
)
class GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules:
    def __init__(
        self,
        *,
        duration_sec: jsii.Number,
        min_required_replicas: jsii.Number,
        name: builtins.str,
        schedule: builtins.str,
        description: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        time_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param duration_sec: The duration of time intervals (in seconds) for which this scaling schedule will be running. The minimum allowed value is 300. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#duration_sec GoogleComputeRegionAutoscaler#duration_sec}
        :param min_required_replicas: Minimum number of VM instances that autoscaler will recommend in time intervals starting according to schedule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#min_required_replicas GoogleComputeRegionAutoscaler#min_required_replicas}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#name GoogleComputeRegionAutoscaler#name}.
        :param schedule: The start timestamps of time intervals when this scaling schedule should provide a scaling signal. This field uses the extended cron format (with an optional year field). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#schedule GoogleComputeRegionAutoscaler#schedule}
        :param description: A description of a scaling schedule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#description GoogleComputeRegionAutoscaler#description}
        :param disabled: A boolean value that specifies if a scaling schedule can influence autoscaler recommendations. If set to true, then a scaling schedule has no effect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#disabled GoogleComputeRegionAutoscaler#disabled}
        :param time_zone: The time zone to be used when interpreting the schedule. The value of this field must be a time zone name from the tz database: http://en.wikipedia.org/wiki/Tz_database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#time_zone GoogleComputeRegionAutoscaler#time_zone}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules.__init__)
            check_type(argname="argument duration_sec", value=duration_sec, expected_type=type_hints["duration_sec"])
            check_type(argname="argument min_required_replicas", value=min_required_replicas, expected_type=type_hints["min_required_replicas"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
        self._values: typing.Dict[str, typing.Any] = {
            "duration_sec": duration_sec,
            "min_required_replicas": min_required_replicas,
            "name": name,
            "schedule": schedule,
        }
        if description is not None:
            self._values["description"] = description
        if disabled is not None:
            self._values["disabled"] = disabled
        if time_zone is not None:
            self._values["time_zone"] = time_zone

    @builtins.property
    def duration_sec(self) -> jsii.Number:
        '''The duration of time intervals (in seconds) for which this scaling schedule will be running.

        The minimum allowed value is 300.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#duration_sec GoogleComputeRegionAutoscaler#duration_sec}
        '''
        result = self._values.get("duration_sec")
        assert result is not None, "Required property 'duration_sec' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_required_replicas(self) -> jsii.Number:
        '''Minimum number of VM instances that autoscaler will recommend in time intervals starting according to schedule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#min_required_replicas GoogleComputeRegionAutoscaler#min_required_replicas}
        '''
        result = self._values.get("min_required_replicas")
        assert result is not None, "Required property 'min_required_replicas' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#name GoogleComputeRegionAutoscaler#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(self) -> builtins.str:
        '''The start timestamps of time intervals when this scaling schedule should provide a scaling signal.

        This field uses the extended cron format (with an optional year field).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#schedule GoogleComputeRegionAutoscaler#schedule}
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of a scaling schedule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#description GoogleComputeRegionAutoscaler#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''A boolean value that specifies if a scaling schedule can influence autoscaler recommendations.

        If set to true, then a scaling schedule has no effect.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#disabled GoogleComputeRegionAutoscaler#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''The time zone to be used when interpreting the schedule.

        The value of this field must be a time zone name from the tz database: http://en.wikipedia.org/wiki/Tz_database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#time_zone GoogleComputeRegionAutoscaler#time_zone}
        '''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetTimeZone")
    def reset_time_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeZone", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="durationSecInput")
    def duration_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationSecInput"))

    @builtins.property
    @jsii.member(jsii_name="minRequiredReplicasInput")
    def min_required_replicas_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minRequiredReplicasInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="timeZoneInput")
    def time_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="durationSec")
    def duration_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "durationSec"))

    @duration_sec.setter
    def duration_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesOutputReference, "duration_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "durationSec", value)

    @builtins.property
    @jsii.member(jsii_name="minRequiredReplicas")
    def min_required_replicas(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minRequiredReplicas"))

    @min_required_replicas.setter
    def min_required_replicas(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesOutputReference, "min_required_replicas").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minRequiredReplicas", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesOutputReference, "schedule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesOutputReference, "time_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "autoscaling_policy": "autoscalingPolicy",
        "name": "name",
        "target": "target",
        "description": "description",
        "id": "id",
        "project": "project",
        "region": "region",
        "timeouts": "timeouts",
    },
)
class GoogleComputeRegionAutoscalerConfig(cdktf.TerraformMetaArguments):
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
        autoscaling_policy: typing.Union[GoogleComputeRegionAutoscalerAutoscalingPolicy, typing.Dict[str, typing.Any]],
        name: builtins.str,
        target: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRegionAutoscalerTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param autoscaling_policy: autoscaling_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#autoscaling_policy GoogleComputeRegionAutoscaler#autoscaling_policy}
        :param name: Name of the resource. The name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#name GoogleComputeRegionAutoscaler#name}
        :param target: URL of the managed instance group that this autoscaler will scale. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#target GoogleComputeRegionAutoscaler#target}
        :param description: An optional description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#description GoogleComputeRegionAutoscaler#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#id GoogleComputeRegionAutoscaler#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#project GoogleComputeRegionAutoscaler#project}.
        :param region: URL of the region where the instance group resides. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#region GoogleComputeRegionAutoscaler#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#timeouts GoogleComputeRegionAutoscaler#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(autoscaling_policy, dict):
            autoscaling_policy = GoogleComputeRegionAutoscalerAutoscalingPolicy(**autoscaling_policy)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeRegionAutoscalerTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument autoscaling_policy", value=autoscaling_policy, expected_type=type_hints["autoscaling_policy"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "autoscaling_policy": autoscaling_policy,
            "name": name,
            "target": target,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
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
    def autoscaling_policy(self) -> GoogleComputeRegionAutoscalerAutoscalingPolicy:
        '''autoscaling_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#autoscaling_policy GoogleComputeRegionAutoscaler#autoscaling_policy}
        '''
        result = self._values.get("autoscaling_policy")
        assert result is not None, "Required property 'autoscaling_policy' is missing"
        return typing.cast(GoogleComputeRegionAutoscalerAutoscalingPolicy, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource.

        The name must be 1-63 characters long and match
        the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#name GoogleComputeRegionAutoscaler#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''URL of the managed instance group that this autoscaler will scale.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#target GoogleComputeRegionAutoscaler#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#description GoogleComputeRegionAutoscaler#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#id GoogleComputeRegionAutoscaler#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#project GoogleComputeRegionAutoscaler#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''URL of the region where the instance group resides.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#region GoogleComputeRegionAutoscaler#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeRegionAutoscalerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#timeouts GoogleComputeRegionAutoscaler#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeRegionAutoscalerTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionAutoscalerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeRegionAutoscalerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#create GoogleComputeRegionAutoscaler#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#delete GoogleComputeRegionAutoscaler#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#update GoogleComputeRegionAutoscaler#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#create GoogleComputeRegionAutoscaler#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#delete GoogleComputeRegionAutoscaler#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_autoscaler#update GoogleComputeRegionAutoscaler#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionAutoscalerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionAutoscalerTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionAutoscaler.GoogleComputeRegionAutoscalerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionAutoscalerTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionAutoscalerTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionAutoscalerTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionAutoscalerTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionAutoscalerTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeRegionAutoscaler",
    "GoogleComputeRegionAutoscalerAutoscalingPolicy",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilization",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyCpuUtilizationOutputReference",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilization",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyLoadBalancingUtilizationOutputReference",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyMetric",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyMetricList",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyMetricOutputReference",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyOutputReference",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControl",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicas",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlMaxScaledDownReplicasOutputReference",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyScaleDownControlOutputReference",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControl",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicas",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlMaxScaledInReplicasOutputReference",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyScaleInControlOutputReference",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedules",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesList",
    "GoogleComputeRegionAutoscalerAutoscalingPolicyScalingSchedulesOutputReference",
    "GoogleComputeRegionAutoscalerConfig",
    "GoogleComputeRegionAutoscalerTimeouts",
    "GoogleComputeRegionAutoscalerTimeoutsOutputReference",
]

publication.publish()
