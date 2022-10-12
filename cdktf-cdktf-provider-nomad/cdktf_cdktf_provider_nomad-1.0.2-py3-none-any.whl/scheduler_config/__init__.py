'''
# `nomad_scheduler_config`

Refer to the Terraform Registory for docs: [`nomad_scheduler_config`](https://www.terraform.io/docs/providers/nomad/r/scheduler_config).
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


class SchedulerConfig(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.schedulerConfig.SchedulerConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/nomad/r/scheduler_config nomad_scheduler_config}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        id: typing.Optional[builtins.str] = None,
        memory_oversubscription_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        preemption_config: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, cdktf.IResolvable]]] = None,
        scheduler_algorithm: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/nomad/r/scheduler_config nomad_scheduler_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/scheduler_config#id SchedulerConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param memory_oversubscription_enabled: When true, tasks may exceed their reserved memory limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/scheduler_config#memory_oversubscription_enabled SchedulerConfig#memory_oversubscription_enabled}
        :param preemption_config: Options to enable preemption for various schedulers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/scheduler_config#preemption_config SchedulerConfig#preemption_config}
        :param scheduler_algorithm: Specifies whether scheduler binpacks or spreads allocations on available nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/scheduler_config#scheduler_algorithm SchedulerConfig#scheduler_algorithm}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SchedulerConfig.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SchedulerConfigConfig(
            id=id,
            memory_oversubscription_enabled=memory_oversubscription_enabled,
            preemption_config=preemption_config,
            scheduler_algorithm=scheduler_algorithm,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMemoryOversubscriptionEnabled")
    def reset_memory_oversubscription_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryOversubscriptionEnabled", []))

    @jsii.member(jsii_name="resetPreemptionConfig")
    def reset_preemption_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreemptionConfig", []))

    @jsii.member(jsii_name="resetSchedulerAlgorithm")
    def reset_scheduler_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedulerAlgorithm", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryOversubscriptionEnabledInput")
    def memory_oversubscription_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "memoryOversubscriptionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="preemptionConfigInput")
    def preemption_config_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, cdktf.IResolvable]]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, cdktf.IResolvable]]], jsii.get(self, "preemptionConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulerAlgorithmInput")
    def scheduler_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedulerAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SchedulerConfig, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="memoryOversubscriptionEnabled")
    def memory_oversubscription_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "memoryOversubscriptionEnabled"))

    @memory_oversubscription_enabled.setter
    def memory_oversubscription_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SchedulerConfig, "memory_oversubscription_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryOversubscriptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="preemptionConfig")
    def preemption_config(
        self,
    ) -> typing.Mapping[builtins.str, typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Mapping[builtins.str, typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preemptionConfig"))

    @preemption_config.setter
    def preemption_config(
        self,
        value: typing.Mapping[builtins.str, typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SchedulerConfig, "preemption_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preemptionConfig", value)

    @builtins.property
    @jsii.member(jsii_name="schedulerAlgorithm")
    def scheduler_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedulerAlgorithm"))

    @scheduler_algorithm.setter
    def scheduler_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SchedulerConfig, "scheduler_algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulerAlgorithm", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.schedulerConfig.SchedulerConfigConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "id": "id",
        "memory_oversubscription_enabled": "memoryOversubscriptionEnabled",
        "preemption_config": "preemptionConfig",
        "scheduler_algorithm": "schedulerAlgorithm",
    },
)
class SchedulerConfigConfig(cdktf.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
        memory_oversubscription_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        preemption_config: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, cdktf.IResolvable]]] = None,
        scheduler_algorithm: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/scheduler_config#id SchedulerConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param memory_oversubscription_enabled: When true, tasks may exceed their reserved memory limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/scheduler_config#memory_oversubscription_enabled SchedulerConfig#memory_oversubscription_enabled}
        :param preemption_config: Options to enable preemption for various schedulers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/scheduler_config#preemption_config SchedulerConfig#preemption_config}
        :param scheduler_algorithm: Specifies whether scheduler binpacks or spreads allocations on available nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/scheduler_config#scheduler_algorithm SchedulerConfig#scheduler_algorithm}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(SchedulerConfigConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument memory_oversubscription_enabled", value=memory_oversubscription_enabled, expected_type=type_hints["memory_oversubscription_enabled"])
            check_type(argname="argument preemption_config", value=preemption_config, expected_type=type_hints["preemption_config"])
            check_type(argname="argument scheduler_algorithm", value=scheduler_algorithm, expected_type=type_hints["scheduler_algorithm"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if id is not None:
            self._values["id"] = id
        if memory_oversubscription_enabled is not None:
            self._values["memory_oversubscription_enabled"] = memory_oversubscription_enabled
        if preemption_config is not None:
            self._values["preemption_config"] = preemption_config
        if scheduler_algorithm is not None:
            self._values["scheduler_algorithm"] = scheduler_algorithm

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
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/scheduler_config#id SchedulerConfig#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory_oversubscription_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, tasks may exceed their reserved memory limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/scheduler_config#memory_oversubscription_enabled SchedulerConfig#memory_oversubscription_enabled}
        '''
        result = self._values.get("memory_oversubscription_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def preemption_config(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, cdktf.IResolvable]]]:
        '''Options to enable preemption for various schedulers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/scheduler_config#preemption_config SchedulerConfig#preemption_config}
        '''
        result = self._values.get("preemption_config")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, cdktf.IResolvable]]], result)

    @builtins.property
    def scheduler_algorithm(self) -> typing.Optional[builtins.str]:
        '''Specifies whether scheduler binpacks or spreads allocations on available nodes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/scheduler_config#scheduler_algorithm SchedulerConfig#scheduler_algorithm}
        '''
        result = self._values.get("scheduler_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchedulerConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SchedulerConfig",
    "SchedulerConfigConfig",
]

publication.publish()
