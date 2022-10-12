'''
# `google_dataproc_autoscaling_policy`

Refer to the Terraform Registory for docs: [`google_dataproc_autoscaling_policy`](https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy).
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


class GoogleDataprocAutoscalingPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocAutoscalingPolicy.GoogleDataprocAutoscalingPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy google_dataproc_autoscaling_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        policy_id: builtins.str,
        basic_algorithm: typing.Optional[typing.Union["GoogleDataprocAutoscalingPolicyBasicAlgorithm", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        secondary_worker_config: typing.Optional[typing.Union["GoogleDataprocAutoscalingPolicySecondaryWorkerConfig", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataprocAutoscalingPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        worker_config: typing.Optional[typing.Union["GoogleDataprocAutoscalingPolicyWorkerConfig", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy google_dataproc_autoscaling_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param policy_id: The policy id. The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between 3 and 50 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#policy_id GoogleDataprocAutoscalingPolicy#policy_id}
        :param basic_algorithm: basic_algorithm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#basic_algorithm GoogleDataprocAutoscalingPolicy#basic_algorithm}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#id GoogleDataprocAutoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location: The location where the autoscaling policy should reside. The default value is 'global'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#location GoogleDataprocAutoscalingPolicy#location}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#project GoogleDataprocAutoscalingPolicy#project}.
        :param secondary_worker_config: secondary_worker_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#secondary_worker_config GoogleDataprocAutoscalingPolicy#secondary_worker_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#timeouts GoogleDataprocAutoscalingPolicy#timeouts}
        :param worker_config: worker_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#worker_config GoogleDataprocAutoscalingPolicy#worker_config}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocAutoscalingPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDataprocAutoscalingPolicyConfig(
            policy_id=policy_id,
            basic_algorithm=basic_algorithm,
            id=id,
            location=location,
            project=project,
            secondary_worker_config=secondary_worker_config,
            timeouts=timeouts,
            worker_config=worker_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBasicAlgorithm")
    def put_basic_algorithm(
        self,
        *,
        yarn_config: typing.Union["GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig", typing.Dict[str, typing.Any]],
        cooldown_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param yarn_config: yarn_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#yarn_config GoogleDataprocAutoscalingPolicy#yarn_config}
        :param cooldown_period: Duration between scaling events. A scaling period starts after the update operation from the previous event has completed. Bounds: [2m, 1d]. Default: 2m. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#cooldown_period GoogleDataprocAutoscalingPolicy#cooldown_period}
        '''
        value = GoogleDataprocAutoscalingPolicyBasicAlgorithm(
            yarn_config=yarn_config, cooldown_period=cooldown_period
        )

        return typing.cast(None, jsii.invoke(self, "putBasicAlgorithm", [value]))

    @jsii.member(jsii_name="putSecondaryWorkerConfig")
    def put_secondary_worker_config(
        self,
        *,
        max_instances: typing.Optional[jsii.Number] = None,
        min_instances: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_instances: Maximum number of instances for this group. Note that by default, clusters will not use secondary workers. Required for secondary workers if the minimum secondary instances is set. Bounds: [minInstances, ). Defaults to 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#max_instances GoogleDataprocAutoscalingPolicy#max_instances}
        :param min_instances: Minimum number of instances for this group. Bounds: [0, maxInstances]. Defaults to 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#min_instances GoogleDataprocAutoscalingPolicy#min_instances}
        :param weight: Weight for the instance group, which is used to determine the fraction of total workers in the cluster from this instance group. For example, if primary workers have weight 2, and secondary workers have weight 1, the cluster will have approximately 2 primary workers for each secondary worker. The cluster may not reach the specified balance if constrained by min/max bounds or other autoscaling settings. For example, if maxInstances for secondary workers is 0, then only primary workers will be added. The cluster can also be out of balance when created. If weight is not set on any instance group, the cluster will default to equal weight for all groups: the cluster will attempt to maintain an equal number of workers in each group within the configured size bounds for each group. If weight is set for one group only, the cluster will default to zero weight on the unset group. For example if weight is set only on primary workers, the cluster will use primary workers only and no secondary workers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#weight GoogleDataprocAutoscalingPolicy#weight}
        '''
        value = GoogleDataprocAutoscalingPolicySecondaryWorkerConfig(
            max_instances=max_instances, min_instances=min_instances, weight=weight
        )

        return typing.cast(None, jsii.invoke(self, "putSecondaryWorkerConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#create GoogleDataprocAutoscalingPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#delete GoogleDataprocAutoscalingPolicy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#update GoogleDataprocAutoscalingPolicy#update}.
        '''
        value = GoogleDataprocAutoscalingPolicyTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWorkerConfig")
    def put_worker_config(
        self,
        *,
        max_instances: jsii.Number,
        min_instances: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_instances: Maximum number of instances for this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#max_instances GoogleDataprocAutoscalingPolicy#max_instances}
        :param min_instances: Minimum number of instances for this group. Bounds: [2, maxInstances]. Defaults to 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#min_instances GoogleDataprocAutoscalingPolicy#min_instances}
        :param weight: Weight for the instance group, which is used to determine the fraction of total workers in the cluster from this instance group. For example, if primary workers have weight 2, and secondary workers have weight 1, the cluster will have approximately 2 primary workers for each secondary worker. The cluster may not reach the specified balance if constrained by min/max bounds or other autoscaling settings. For example, if maxInstances for secondary workers is 0, then only primary workers will be added. The cluster can also be out of balance when created. If weight is not set on any instance group, the cluster will default to equal weight for all groups: the cluster will attempt to maintain an equal number of workers in each group within the configured size bounds for each group. If weight is set for one group only, the cluster will default to zero weight on the unset group. For example if weight is set only on primary workers, the cluster will use primary workers only and no secondary workers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#weight GoogleDataprocAutoscalingPolicy#weight}
        '''
        value = GoogleDataprocAutoscalingPolicyWorkerConfig(
            max_instances=max_instances, min_instances=min_instances, weight=weight
        )

        return typing.cast(None, jsii.invoke(self, "putWorkerConfig", [value]))

    @jsii.member(jsii_name="resetBasicAlgorithm")
    def reset_basic_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAlgorithm", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetSecondaryWorkerConfig")
    def reset_secondary_worker_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondaryWorkerConfig", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWorkerConfig")
    def reset_worker_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkerConfig", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="basicAlgorithm")
    def basic_algorithm(
        self,
    ) -> "GoogleDataprocAutoscalingPolicyBasicAlgorithmOutputReference":
        return typing.cast("GoogleDataprocAutoscalingPolicyBasicAlgorithmOutputReference", jsii.get(self, "basicAlgorithm"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="secondaryWorkerConfig")
    def secondary_worker_config(
        self,
    ) -> "GoogleDataprocAutoscalingPolicySecondaryWorkerConfigOutputReference":
        return typing.cast("GoogleDataprocAutoscalingPolicySecondaryWorkerConfigOutputReference", jsii.get(self, "secondaryWorkerConfig"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleDataprocAutoscalingPolicyTimeoutsOutputReference":
        return typing.cast("GoogleDataprocAutoscalingPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="workerConfig")
    def worker_config(
        self,
    ) -> "GoogleDataprocAutoscalingPolicyWorkerConfigOutputReference":
        return typing.cast("GoogleDataprocAutoscalingPolicyWorkerConfigOutputReference", jsii.get(self, "workerConfig"))

    @builtins.property
    @jsii.member(jsii_name="basicAlgorithmInput")
    def basic_algorithm_input(
        self,
    ) -> typing.Optional["GoogleDataprocAutoscalingPolicyBasicAlgorithm"]:
        return typing.cast(typing.Optional["GoogleDataprocAutoscalingPolicyBasicAlgorithm"], jsii.get(self, "basicAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="policyIdInput")
    def policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryWorkerConfigInput")
    def secondary_worker_config_input(
        self,
    ) -> typing.Optional["GoogleDataprocAutoscalingPolicySecondaryWorkerConfig"]:
        return typing.cast(typing.Optional["GoogleDataprocAutoscalingPolicySecondaryWorkerConfig"], jsii.get(self, "secondaryWorkerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleDataprocAutoscalingPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleDataprocAutoscalingPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="workerConfigInput")
    def worker_config_input(
        self,
    ) -> typing.Optional["GoogleDataprocAutoscalingPolicyWorkerConfig"]:
        return typing.cast(typing.Optional["GoogleDataprocAutoscalingPolicyWorkerConfig"], jsii.get(self, "workerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicy, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyId"))

    @policy_id.setter
    def policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicy, "policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyId", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicy, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocAutoscalingPolicy.GoogleDataprocAutoscalingPolicyBasicAlgorithm",
    jsii_struct_bases=[],
    name_mapping={"yarn_config": "yarnConfig", "cooldown_period": "cooldownPeriod"},
)
class GoogleDataprocAutoscalingPolicyBasicAlgorithm:
    def __init__(
        self,
        *,
        yarn_config: typing.Union["GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig", typing.Dict[str, typing.Any]],
        cooldown_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param yarn_config: yarn_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#yarn_config GoogleDataprocAutoscalingPolicy#yarn_config}
        :param cooldown_period: Duration between scaling events. A scaling period starts after the update operation from the previous event has completed. Bounds: [2m, 1d]. Default: 2m. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#cooldown_period GoogleDataprocAutoscalingPolicy#cooldown_period}
        '''
        if isinstance(yarn_config, dict):
            yarn_config = GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig(**yarn_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocAutoscalingPolicyBasicAlgorithm.__init__)
            check_type(argname="argument yarn_config", value=yarn_config, expected_type=type_hints["yarn_config"])
            check_type(argname="argument cooldown_period", value=cooldown_period, expected_type=type_hints["cooldown_period"])
        self._values: typing.Dict[str, typing.Any] = {
            "yarn_config": yarn_config,
        }
        if cooldown_period is not None:
            self._values["cooldown_period"] = cooldown_period

    @builtins.property
    def yarn_config(self) -> "GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig":
        '''yarn_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#yarn_config GoogleDataprocAutoscalingPolicy#yarn_config}
        '''
        result = self._values.get("yarn_config")
        assert result is not None, "Required property 'yarn_config' is missing"
        return typing.cast("GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig", result)

    @builtins.property
    def cooldown_period(self) -> typing.Optional[builtins.str]:
        '''Duration between scaling events. A scaling period starts after the update operation from the previous event has completed.

        Bounds: [2m, 1d]. Default: 2m.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#cooldown_period GoogleDataprocAutoscalingPolicy#cooldown_period}
        '''
        result = self._values.get("cooldown_period")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocAutoscalingPolicyBasicAlgorithm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocAutoscalingPolicyBasicAlgorithmOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocAutoscalingPolicy.GoogleDataprocAutoscalingPolicyBasicAlgorithmOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocAutoscalingPolicyBasicAlgorithmOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putYarnConfig")
    def put_yarn_config(
        self,
        *,
        graceful_decommission_timeout: builtins.str,
        scale_down_factor: jsii.Number,
        scale_up_factor: jsii.Number,
        scale_down_min_worker_fraction: typing.Optional[jsii.Number] = None,
        scale_up_min_worker_fraction: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param graceful_decommission_timeout: Timeout for YARN graceful decommissioning of Node Managers. Specifies the duration to wait for jobs to complete before forcefully removing workers (and potentially interrupting jobs). Only applicable to downscaling operations. Bounds: [0s, 1d]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#graceful_decommission_timeout GoogleDataprocAutoscalingPolicy#graceful_decommission_timeout}
        :param scale_down_factor: Fraction of average pending memory in the last cooldown period for which to remove workers. A scale-down factor of 1 will result in scaling down so that there is no available memory remaining after the update (more aggressive scaling). A scale-down factor of 0 disables removing workers, which can be beneficial for autoscaling a single job. Bounds: [0.0, 1.0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#scale_down_factor GoogleDataprocAutoscalingPolicy#scale_down_factor}
        :param scale_up_factor: Fraction of average pending memory in the last cooldown period for which to add workers. A scale-up factor of 1.0 will result in scaling up so that there is no pending memory remaining after the update (more aggressive scaling). A scale-up factor closer to 0 will result in a smaller magnitude of scaling up (less aggressive scaling). Bounds: [0.0, 1.0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#scale_up_factor GoogleDataprocAutoscalingPolicy#scale_up_factor}
        :param scale_down_min_worker_fraction: Minimum scale-down threshold as a fraction of total cluster size before scaling occurs. For example, in a 20-worker cluster, a threshold of 0.1 means the autoscaler must recommend at least a 2 worker scale-down for the cluster to scale. A threshold of 0 means the autoscaler will scale down on any recommended change. Bounds: [0.0, 1.0]. Default: 0.0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#scale_down_min_worker_fraction GoogleDataprocAutoscalingPolicy#scale_down_min_worker_fraction}
        :param scale_up_min_worker_fraction: Minimum scale-up threshold as a fraction of total cluster size before scaling occurs. For example, in a 20-worker cluster, a threshold of 0.1 means the autoscaler must recommend at least a 2-worker scale-up for the cluster to scale. A threshold of 0 means the autoscaler will scale up on any recommended change. Bounds: [0.0, 1.0]. Default: 0.0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#scale_up_min_worker_fraction GoogleDataprocAutoscalingPolicy#scale_up_min_worker_fraction}
        '''
        value = GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig(
            graceful_decommission_timeout=graceful_decommission_timeout,
            scale_down_factor=scale_down_factor,
            scale_up_factor=scale_up_factor,
            scale_down_min_worker_fraction=scale_down_min_worker_fraction,
            scale_up_min_worker_fraction=scale_up_min_worker_fraction,
        )

        return typing.cast(None, jsii.invoke(self, "putYarnConfig", [value]))

    @jsii.member(jsii_name="resetCooldownPeriod")
    def reset_cooldown_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCooldownPeriod", []))

    @builtins.property
    @jsii.member(jsii_name="yarnConfig")
    def yarn_config(
        self,
    ) -> "GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfigOutputReference":
        return typing.cast("GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfigOutputReference", jsii.get(self, "yarnConfig"))

    @builtins.property
    @jsii.member(jsii_name="cooldownPeriodInput")
    def cooldown_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cooldownPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="yarnConfigInput")
    def yarn_config_input(
        self,
    ) -> typing.Optional["GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig"]:
        return typing.cast(typing.Optional["GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig"], jsii.get(self, "yarnConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="cooldownPeriod")
    def cooldown_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cooldownPeriod"))

    @cooldown_period.setter
    def cooldown_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyBasicAlgorithmOutputReference, "cooldown_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cooldownPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocAutoscalingPolicyBasicAlgorithm]:
        return typing.cast(typing.Optional[GoogleDataprocAutoscalingPolicyBasicAlgorithm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocAutoscalingPolicyBasicAlgorithm],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyBasicAlgorithmOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocAutoscalingPolicy.GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig",
    jsii_struct_bases=[],
    name_mapping={
        "graceful_decommission_timeout": "gracefulDecommissionTimeout",
        "scale_down_factor": "scaleDownFactor",
        "scale_up_factor": "scaleUpFactor",
        "scale_down_min_worker_fraction": "scaleDownMinWorkerFraction",
        "scale_up_min_worker_fraction": "scaleUpMinWorkerFraction",
    },
)
class GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig:
    def __init__(
        self,
        *,
        graceful_decommission_timeout: builtins.str,
        scale_down_factor: jsii.Number,
        scale_up_factor: jsii.Number,
        scale_down_min_worker_fraction: typing.Optional[jsii.Number] = None,
        scale_up_min_worker_fraction: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param graceful_decommission_timeout: Timeout for YARN graceful decommissioning of Node Managers. Specifies the duration to wait for jobs to complete before forcefully removing workers (and potentially interrupting jobs). Only applicable to downscaling operations. Bounds: [0s, 1d]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#graceful_decommission_timeout GoogleDataprocAutoscalingPolicy#graceful_decommission_timeout}
        :param scale_down_factor: Fraction of average pending memory in the last cooldown period for which to remove workers. A scale-down factor of 1 will result in scaling down so that there is no available memory remaining after the update (more aggressive scaling). A scale-down factor of 0 disables removing workers, which can be beneficial for autoscaling a single job. Bounds: [0.0, 1.0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#scale_down_factor GoogleDataprocAutoscalingPolicy#scale_down_factor}
        :param scale_up_factor: Fraction of average pending memory in the last cooldown period for which to add workers. A scale-up factor of 1.0 will result in scaling up so that there is no pending memory remaining after the update (more aggressive scaling). A scale-up factor closer to 0 will result in a smaller magnitude of scaling up (less aggressive scaling). Bounds: [0.0, 1.0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#scale_up_factor GoogleDataprocAutoscalingPolicy#scale_up_factor}
        :param scale_down_min_worker_fraction: Minimum scale-down threshold as a fraction of total cluster size before scaling occurs. For example, in a 20-worker cluster, a threshold of 0.1 means the autoscaler must recommend at least a 2 worker scale-down for the cluster to scale. A threshold of 0 means the autoscaler will scale down on any recommended change. Bounds: [0.0, 1.0]. Default: 0.0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#scale_down_min_worker_fraction GoogleDataprocAutoscalingPolicy#scale_down_min_worker_fraction}
        :param scale_up_min_worker_fraction: Minimum scale-up threshold as a fraction of total cluster size before scaling occurs. For example, in a 20-worker cluster, a threshold of 0.1 means the autoscaler must recommend at least a 2-worker scale-up for the cluster to scale. A threshold of 0 means the autoscaler will scale up on any recommended change. Bounds: [0.0, 1.0]. Default: 0.0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#scale_up_min_worker_fraction GoogleDataprocAutoscalingPolicy#scale_up_min_worker_fraction}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig.__init__)
            check_type(argname="argument graceful_decommission_timeout", value=graceful_decommission_timeout, expected_type=type_hints["graceful_decommission_timeout"])
            check_type(argname="argument scale_down_factor", value=scale_down_factor, expected_type=type_hints["scale_down_factor"])
            check_type(argname="argument scale_up_factor", value=scale_up_factor, expected_type=type_hints["scale_up_factor"])
            check_type(argname="argument scale_down_min_worker_fraction", value=scale_down_min_worker_fraction, expected_type=type_hints["scale_down_min_worker_fraction"])
            check_type(argname="argument scale_up_min_worker_fraction", value=scale_up_min_worker_fraction, expected_type=type_hints["scale_up_min_worker_fraction"])
        self._values: typing.Dict[str, typing.Any] = {
            "graceful_decommission_timeout": graceful_decommission_timeout,
            "scale_down_factor": scale_down_factor,
            "scale_up_factor": scale_up_factor,
        }
        if scale_down_min_worker_fraction is not None:
            self._values["scale_down_min_worker_fraction"] = scale_down_min_worker_fraction
        if scale_up_min_worker_fraction is not None:
            self._values["scale_up_min_worker_fraction"] = scale_up_min_worker_fraction

    @builtins.property
    def graceful_decommission_timeout(self) -> builtins.str:
        '''Timeout for YARN graceful decommissioning of Node Managers.

        Specifies the
        duration to wait for jobs to complete before forcefully removing workers
        (and potentially interrupting jobs). Only applicable to downscaling operations.

        Bounds: [0s, 1d].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#graceful_decommission_timeout GoogleDataprocAutoscalingPolicy#graceful_decommission_timeout}
        '''
        result = self._values.get("graceful_decommission_timeout")
        assert result is not None, "Required property 'graceful_decommission_timeout' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scale_down_factor(self) -> jsii.Number:
        '''Fraction of average pending memory in the last cooldown period for which to remove workers.

        A scale-down factor of 1 will result in scaling down so that there
        is no available memory remaining after the update (more aggressive scaling).
        A scale-down factor of 0 disables removing workers, which can be beneficial for
        autoscaling a single job.

        Bounds: [0.0, 1.0].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#scale_down_factor GoogleDataprocAutoscalingPolicy#scale_down_factor}
        '''
        result = self._values.get("scale_down_factor")
        assert result is not None, "Required property 'scale_down_factor' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def scale_up_factor(self) -> jsii.Number:
        '''Fraction of average pending memory in the last cooldown period for which to add workers.

        A scale-up factor of 1.0 will result in scaling up so that there
        is no pending memory remaining after the update (more aggressive scaling).
        A scale-up factor closer to 0 will result in a smaller magnitude of scaling up
        (less aggressive scaling).

        Bounds: [0.0, 1.0].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#scale_up_factor GoogleDataprocAutoscalingPolicy#scale_up_factor}
        '''
        result = self._values.get("scale_up_factor")
        assert result is not None, "Required property 'scale_up_factor' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def scale_down_min_worker_fraction(self) -> typing.Optional[jsii.Number]:
        '''Minimum scale-down threshold as a fraction of total cluster size before scaling occurs.

        For example, in a 20-worker cluster, a threshold of 0.1 means the autoscaler must
        recommend at least a 2 worker scale-down for the cluster to scale. A threshold of 0
        means the autoscaler will scale down on any recommended change.

        Bounds: [0.0, 1.0]. Default: 0.0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#scale_down_min_worker_fraction GoogleDataprocAutoscalingPolicy#scale_down_min_worker_fraction}
        '''
        result = self._values.get("scale_down_min_worker_fraction")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scale_up_min_worker_fraction(self) -> typing.Optional[jsii.Number]:
        '''Minimum scale-up threshold as a fraction of total cluster size before scaling occurs.

        For example, in a 20-worker cluster, a threshold of 0.1 means the autoscaler
        must recommend at least a 2-worker scale-up for the cluster to scale. A threshold of
        0 means the autoscaler will scale up on any recommended change.

        Bounds: [0.0, 1.0]. Default: 0.0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#scale_up_min_worker_fraction GoogleDataprocAutoscalingPolicy#scale_up_min_worker_fraction}
        '''
        result = self._values.get("scale_up_min_worker_fraction")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocAutoscalingPolicy.GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetScaleDownMinWorkerFraction")
    def reset_scale_down_min_worker_fraction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleDownMinWorkerFraction", []))

    @jsii.member(jsii_name="resetScaleUpMinWorkerFraction")
    def reset_scale_up_min_worker_fraction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleUpMinWorkerFraction", []))

    @builtins.property
    @jsii.member(jsii_name="gracefulDecommissionTimeoutInput")
    def graceful_decommission_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gracefulDecommissionTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownFactorInput")
    def scale_down_factor_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scaleDownFactorInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownMinWorkerFractionInput")
    def scale_down_min_worker_fraction_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scaleDownMinWorkerFractionInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleUpFactorInput")
    def scale_up_factor_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scaleUpFactorInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleUpMinWorkerFractionInput")
    def scale_up_min_worker_fraction_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scaleUpMinWorkerFractionInput"))

    @builtins.property
    @jsii.member(jsii_name="gracefulDecommissionTimeout")
    def graceful_decommission_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gracefulDecommissionTimeout"))

    @graceful_decommission_timeout.setter
    def graceful_decommission_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfigOutputReference, "graceful_decommission_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gracefulDecommissionTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="scaleDownFactor")
    def scale_down_factor(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scaleDownFactor"))

    @scale_down_factor.setter
    def scale_down_factor(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfigOutputReference, "scale_down_factor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleDownFactor", value)

    @builtins.property
    @jsii.member(jsii_name="scaleDownMinWorkerFraction")
    def scale_down_min_worker_fraction(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scaleDownMinWorkerFraction"))

    @scale_down_min_worker_fraction.setter
    def scale_down_min_worker_fraction(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfigOutputReference, "scale_down_min_worker_fraction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleDownMinWorkerFraction", value)

    @builtins.property
    @jsii.member(jsii_name="scaleUpFactor")
    def scale_up_factor(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scaleUpFactor"))

    @scale_up_factor.setter
    def scale_up_factor(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfigOutputReference, "scale_up_factor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleUpFactor", value)

    @builtins.property
    @jsii.member(jsii_name="scaleUpMinWorkerFraction")
    def scale_up_min_worker_fraction(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scaleUpMinWorkerFraction"))

    @scale_up_min_worker_fraction.setter
    def scale_up_min_worker_fraction(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfigOutputReference, "scale_up_min_worker_fraction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleUpMinWorkerFraction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig]:
        return typing.cast(typing.Optional[GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocAutoscalingPolicy.GoogleDataprocAutoscalingPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "policy_id": "policyId",
        "basic_algorithm": "basicAlgorithm",
        "id": "id",
        "location": "location",
        "project": "project",
        "secondary_worker_config": "secondaryWorkerConfig",
        "timeouts": "timeouts",
        "worker_config": "workerConfig",
    },
)
class GoogleDataprocAutoscalingPolicyConfig(cdktf.TerraformMetaArguments):
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
        policy_id: builtins.str,
        basic_algorithm: typing.Optional[typing.Union[GoogleDataprocAutoscalingPolicyBasicAlgorithm, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        secondary_worker_config: typing.Optional[typing.Union["GoogleDataprocAutoscalingPolicySecondaryWorkerConfig", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataprocAutoscalingPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        worker_config: typing.Optional[typing.Union["GoogleDataprocAutoscalingPolicyWorkerConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param policy_id: The policy id. The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between 3 and 50 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#policy_id GoogleDataprocAutoscalingPolicy#policy_id}
        :param basic_algorithm: basic_algorithm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#basic_algorithm GoogleDataprocAutoscalingPolicy#basic_algorithm}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#id GoogleDataprocAutoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location: The location where the autoscaling policy should reside. The default value is 'global'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#location GoogleDataprocAutoscalingPolicy#location}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#project GoogleDataprocAutoscalingPolicy#project}.
        :param secondary_worker_config: secondary_worker_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#secondary_worker_config GoogleDataprocAutoscalingPolicy#secondary_worker_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#timeouts GoogleDataprocAutoscalingPolicy#timeouts}
        :param worker_config: worker_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#worker_config GoogleDataprocAutoscalingPolicy#worker_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(basic_algorithm, dict):
            basic_algorithm = GoogleDataprocAutoscalingPolicyBasicAlgorithm(**basic_algorithm)
        if isinstance(secondary_worker_config, dict):
            secondary_worker_config = GoogleDataprocAutoscalingPolicySecondaryWorkerConfig(**secondary_worker_config)
        if isinstance(timeouts, dict):
            timeouts = GoogleDataprocAutoscalingPolicyTimeouts(**timeouts)
        if isinstance(worker_config, dict):
            worker_config = GoogleDataprocAutoscalingPolicyWorkerConfig(**worker_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocAutoscalingPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument basic_algorithm", value=basic_algorithm, expected_type=type_hints["basic_algorithm"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument secondary_worker_config", value=secondary_worker_config, expected_type=type_hints["secondary_worker_config"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument worker_config", value=worker_config, expected_type=type_hints["worker_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "policy_id": policy_id,
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
        if basic_algorithm is not None:
            self._values["basic_algorithm"] = basic_algorithm
        if id is not None:
            self._values["id"] = id
        if location is not None:
            self._values["location"] = location
        if project is not None:
            self._values["project"] = project
        if secondary_worker_config is not None:
            self._values["secondary_worker_config"] = secondary_worker_config
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if worker_config is not None:
            self._values["worker_config"] = worker_config

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
    def policy_id(self) -> builtins.str:
        '''The policy id.

        The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_),
        and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between
        3 and 50 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#policy_id GoogleDataprocAutoscalingPolicy#policy_id}
        '''
        result = self._values.get("policy_id")
        assert result is not None, "Required property 'policy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def basic_algorithm(
        self,
    ) -> typing.Optional[GoogleDataprocAutoscalingPolicyBasicAlgorithm]:
        '''basic_algorithm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#basic_algorithm GoogleDataprocAutoscalingPolicy#basic_algorithm}
        '''
        result = self._values.get("basic_algorithm")
        return typing.cast(typing.Optional[GoogleDataprocAutoscalingPolicyBasicAlgorithm], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#id GoogleDataprocAutoscalingPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''The  location where the autoscaling policy should reside. The default value is 'global'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#location GoogleDataprocAutoscalingPolicy#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#project GoogleDataprocAutoscalingPolicy#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secondary_worker_config(
        self,
    ) -> typing.Optional["GoogleDataprocAutoscalingPolicySecondaryWorkerConfig"]:
        '''secondary_worker_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#secondary_worker_config GoogleDataprocAutoscalingPolicy#secondary_worker_config}
        '''
        result = self._values.get("secondary_worker_config")
        return typing.cast(typing.Optional["GoogleDataprocAutoscalingPolicySecondaryWorkerConfig"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDataprocAutoscalingPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#timeouts GoogleDataprocAutoscalingPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDataprocAutoscalingPolicyTimeouts"], result)

    @builtins.property
    def worker_config(
        self,
    ) -> typing.Optional["GoogleDataprocAutoscalingPolicyWorkerConfig"]:
        '''worker_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#worker_config GoogleDataprocAutoscalingPolicy#worker_config}
        '''
        result = self._values.get("worker_config")
        return typing.cast(typing.Optional["GoogleDataprocAutoscalingPolicyWorkerConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocAutoscalingPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocAutoscalingPolicy.GoogleDataprocAutoscalingPolicySecondaryWorkerConfig",
    jsii_struct_bases=[],
    name_mapping={
        "max_instances": "maxInstances",
        "min_instances": "minInstances",
        "weight": "weight",
    },
)
class GoogleDataprocAutoscalingPolicySecondaryWorkerConfig:
    def __init__(
        self,
        *,
        max_instances: typing.Optional[jsii.Number] = None,
        min_instances: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_instances: Maximum number of instances for this group. Note that by default, clusters will not use secondary workers. Required for secondary workers if the minimum secondary instances is set. Bounds: [minInstances, ). Defaults to 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#max_instances GoogleDataprocAutoscalingPolicy#max_instances}
        :param min_instances: Minimum number of instances for this group. Bounds: [0, maxInstances]. Defaults to 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#min_instances GoogleDataprocAutoscalingPolicy#min_instances}
        :param weight: Weight for the instance group, which is used to determine the fraction of total workers in the cluster from this instance group. For example, if primary workers have weight 2, and secondary workers have weight 1, the cluster will have approximately 2 primary workers for each secondary worker. The cluster may not reach the specified balance if constrained by min/max bounds or other autoscaling settings. For example, if maxInstances for secondary workers is 0, then only primary workers will be added. The cluster can also be out of balance when created. If weight is not set on any instance group, the cluster will default to equal weight for all groups: the cluster will attempt to maintain an equal number of workers in each group within the configured size bounds for each group. If weight is set for one group only, the cluster will default to zero weight on the unset group. For example if weight is set only on primary workers, the cluster will use primary workers only and no secondary workers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#weight GoogleDataprocAutoscalingPolicy#weight}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocAutoscalingPolicySecondaryWorkerConfig.__init__)
            check_type(argname="argument max_instances", value=max_instances, expected_type=type_hints["max_instances"])
            check_type(argname="argument min_instances", value=min_instances, expected_type=type_hints["min_instances"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_instances is not None:
            self._values["max_instances"] = max_instances
        if min_instances is not None:
            self._values["min_instances"] = min_instances
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def max_instances(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of instances for this group.

        Note that by default, clusters will not use
        secondary workers. Required for secondary workers if the minimum secondary instances is set.
        Bounds: [minInstances, ). Defaults to 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#max_instances GoogleDataprocAutoscalingPolicy#max_instances}
        '''
        result = self._values.get("max_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_instances(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of instances for this group. Bounds: [0, maxInstances]. Defaults to 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#min_instances GoogleDataprocAutoscalingPolicy#min_instances}
        '''
        result = self._values.get("min_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Weight for the instance group, which is used to determine the fraction of total workers in the cluster from this instance group.

        For example, if primary workers have weight 2,
        and secondary workers have weight 1, the cluster will have approximately 2 primary workers
        for each secondary worker.

        The cluster may not reach the specified balance if constrained by min/max bounds or other
        autoscaling settings. For example, if maxInstances for secondary workers is 0, then only
        primary workers will be added. The cluster can also be out of balance when created.

        If weight is not set on any instance group, the cluster will default to equal weight for
        all groups: the cluster will attempt to maintain an equal number of workers in each group
        within the configured size bounds for each group. If weight is set for one group only,
        the cluster will default to zero weight on the unset group. For example if weight is set
        only on primary workers, the cluster will use primary workers only and no secondary workers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#weight GoogleDataprocAutoscalingPolicy#weight}
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocAutoscalingPolicySecondaryWorkerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocAutoscalingPolicySecondaryWorkerConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocAutoscalingPolicy.GoogleDataprocAutoscalingPolicySecondaryWorkerConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocAutoscalingPolicySecondaryWorkerConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxInstances")
    def reset_max_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxInstances", []))

    @jsii.member(jsii_name="resetMinInstances")
    def reset_min_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinInstances", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @builtins.property
    @jsii.member(jsii_name="maxInstancesInput")
    def max_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="minInstancesInput")
    def min_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="maxInstances")
    def max_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxInstances"))

    @max_instances.setter
    def max_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicySecondaryWorkerConfigOutputReference, "max_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxInstances", value)

    @builtins.property
    @jsii.member(jsii_name="minInstances")
    def min_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minInstances"))

    @min_instances.setter
    def min_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicySecondaryWorkerConfigOutputReference, "min_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minInstances", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicySecondaryWorkerConfigOutputReference, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocAutoscalingPolicySecondaryWorkerConfig]:
        return typing.cast(typing.Optional[GoogleDataprocAutoscalingPolicySecondaryWorkerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocAutoscalingPolicySecondaryWorkerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicySecondaryWorkerConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocAutoscalingPolicy.GoogleDataprocAutoscalingPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleDataprocAutoscalingPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#create GoogleDataprocAutoscalingPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#delete GoogleDataprocAutoscalingPolicy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#update GoogleDataprocAutoscalingPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocAutoscalingPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#create GoogleDataprocAutoscalingPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#delete GoogleDataprocAutoscalingPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#update GoogleDataprocAutoscalingPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocAutoscalingPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocAutoscalingPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocAutoscalingPolicy.GoogleDataprocAutoscalingPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocAutoscalingPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataprocAutoscalingPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataprocAutoscalingPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataprocAutoscalingPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocAutoscalingPolicy.GoogleDataprocAutoscalingPolicyWorkerConfig",
    jsii_struct_bases=[],
    name_mapping={
        "max_instances": "maxInstances",
        "min_instances": "minInstances",
        "weight": "weight",
    },
)
class GoogleDataprocAutoscalingPolicyWorkerConfig:
    def __init__(
        self,
        *,
        max_instances: jsii.Number,
        min_instances: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_instances: Maximum number of instances for this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#max_instances GoogleDataprocAutoscalingPolicy#max_instances}
        :param min_instances: Minimum number of instances for this group. Bounds: [2, maxInstances]. Defaults to 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#min_instances GoogleDataprocAutoscalingPolicy#min_instances}
        :param weight: Weight for the instance group, which is used to determine the fraction of total workers in the cluster from this instance group. For example, if primary workers have weight 2, and secondary workers have weight 1, the cluster will have approximately 2 primary workers for each secondary worker. The cluster may not reach the specified balance if constrained by min/max bounds or other autoscaling settings. For example, if maxInstances for secondary workers is 0, then only primary workers will be added. The cluster can also be out of balance when created. If weight is not set on any instance group, the cluster will default to equal weight for all groups: the cluster will attempt to maintain an equal number of workers in each group within the configured size bounds for each group. If weight is set for one group only, the cluster will default to zero weight on the unset group. For example if weight is set only on primary workers, the cluster will use primary workers only and no secondary workers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#weight GoogleDataprocAutoscalingPolicy#weight}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocAutoscalingPolicyWorkerConfig.__init__)
            check_type(argname="argument max_instances", value=max_instances, expected_type=type_hints["max_instances"])
            check_type(argname="argument min_instances", value=min_instances, expected_type=type_hints["min_instances"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_instances": max_instances,
        }
        if min_instances is not None:
            self._values["min_instances"] = min_instances
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def max_instances(self) -> jsii.Number:
        '''Maximum number of instances for this group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#max_instances GoogleDataprocAutoscalingPolicy#max_instances}
        '''
        result = self._values.get("max_instances")
        assert result is not None, "Required property 'max_instances' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_instances(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of instances for this group. Bounds: [2, maxInstances]. Defaults to 2.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#min_instances GoogleDataprocAutoscalingPolicy#min_instances}
        '''
        result = self._values.get("min_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Weight for the instance group, which is used to determine the fraction of total workers in the cluster from this instance group.

        For example, if primary workers have weight 2,
        and secondary workers have weight 1, the cluster will have approximately 2 primary workers
        for each secondary worker.

        The cluster may not reach the specified balance if constrained by min/max bounds or other
        autoscaling settings. For example, if maxInstances for secondary workers is 0, then only
        primary workers will be added. The cluster can also be out of balance when created.

        If weight is not set on any instance group, the cluster will default to equal weight for
        all groups: the cluster will attempt to maintain an equal number of workers in each group
        within the configured size bounds for each group. If weight is set for one group only,
        the cluster will default to zero weight on the unset group. For example if weight is set
        only on primary workers, the cluster will use primary workers only and no secondary workers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_autoscaling_policy#weight GoogleDataprocAutoscalingPolicy#weight}
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocAutoscalingPolicyWorkerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocAutoscalingPolicyWorkerConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocAutoscalingPolicy.GoogleDataprocAutoscalingPolicyWorkerConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocAutoscalingPolicyWorkerConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMinInstances")
    def reset_min_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinInstances", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @builtins.property
    @jsii.member(jsii_name="maxInstancesInput")
    def max_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="minInstancesInput")
    def min_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="maxInstances")
    def max_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxInstances"))

    @max_instances.setter
    def max_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyWorkerConfigOutputReference, "max_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxInstances", value)

    @builtins.property
    @jsii.member(jsii_name="minInstances")
    def min_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minInstances"))

    @min_instances.setter
    def min_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyWorkerConfigOutputReference, "min_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minInstances", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyWorkerConfigOutputReference, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocAutoscalingPolicyWorkerConfig]:
        return typing.cast(typing.Optional[GoogleDataprocAutoscalingPolicyWorkerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocAutoscalingPolicyWorkerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocAutoscalingPolicyWorkerConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDataprocAutoscalingPolicy",
    "GoogleDataprocAutoscalingPolicyBasicAlgorithm",
    "GoogleDataprocAutoscalingPolicyBasicAlgorithmOutputReference",
    "GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfig",
    "GoogleDataprocAutoscalingPolicyBasicAlgorithmYarnConfigOutputReference",
    "GoogleDataprocAutoscalingPolicyConfig",
    "GoogleDataprocAutoscalingPolicySecondaryWorkerConfig",
    "GoogleDataprocAutoscalingPolicySecondaryWorkerConfigOutputReference",
    "GoogleDataprocAutoscalingPolicyTimeouts",
    "GoogleDataprocAutoscalingPolicyTimeoutsOutputReference",
    "GoogleDataprocAutoscalingPolicyWorkerConfig",
    "GoogleDataprocAutoscalingPolicyWorkerConfigOutputReference",
]

publication.publish()
