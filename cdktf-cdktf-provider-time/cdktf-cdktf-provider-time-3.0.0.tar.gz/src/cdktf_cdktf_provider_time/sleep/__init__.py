'''
# `time_sleep`

Refer to the Terraform Registory for docs: [`time_sleep`](https://www.terraform.io/docs/providers/time/r/sleep).
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


class Sleep(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-time.sleep.Sleep",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/time/r/sleep time_sleep}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        create_duration: typing.Optional[builtins.str] = None,
        destroy_duration: typing.Optional[builtins.str] = None,
        triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/time/r/sleep time_sleep} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param create_duration: `Time duration <https://golang.org/pkg/time/#ParseDuration>`_ to delay resource creation. For example, ``30s`` for 30 seconds or ``5m`` for 5 minutes. Updating this value by itself will not trigger a delay. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/sleep#create_duration Sleep#create_duration}
        :param destroy_duration: `Time duration <https://golang.org/pkg/time/#ParseDuration>`_ to delay resource destroy. For example, ``30s`` for 30 seconds or ``5m`` for 5 minutes. Updating this value by itself will not trigger a delay. This value or any updates to it must be successfully applied into the Terraform state before destroying this resource to take effect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/sleep#destroy_duration Sleep#destroy_duration}
        :param triggers: (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See `the main provider documentation <../index.md>`_ for more information. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/sleep#triggers Sleep#triggers}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Sleep.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = SleepConfig(
            create_duration=create_duration,
            destroy_duration=destroy_duration,
            triggers=triggers,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetCreateDuration")
    def reset_create_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateDuration", []))

    @jsii.member(jsii_name="resetDestroyDuration")
    def reset_destroy_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestroyDuration", []))

    @jsii.member(jsii_name="resetTriggers")
    def reset_triggers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggers", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="createDurationInput")
    def create_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="destroyDurationInput")
    def destroy_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destroyDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="triggersInput")
    def triggers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "triggersInput"))

    @builtins.property
    @jsii.member(jsii_name="createDuration")
    def create_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createDuration"))

    @create_duration.setter
    def create_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Sleep, "create_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createDuration", value)

    @builtins.property
    @jsii.member(jsii_name="destroyDuration")
    def destroy_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destroyDuration"))

    @destroy_duration.setter
    def destroy_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Sleep, "destroy_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destroyDuration", value)

    @builtins.property
    @jsii.member(jsii_name="triggers")
    def triggers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "triggers"))

    @triggers.setter
    def triggers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Sleep, "triggers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggers", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-time.sleep.SleepConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "create_duration": "createDuration",
        "destroy_duration": "destroyDuration",
        "triggers": "triggers",
    },
)
class SleepConfig(cdktf.TerraformMetaArguments):
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
        create_duration: typing.Optional[builtins.str] = None,
        destroy_duration: typing.Optional[builtins.str] = None,
        triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param create_duration: `Time duration <https://golang.org/pkg/time/#ParseDuration>`_ to delay resource creation. For example, ``30s`` for 30 seconds or ``5m`` for 5 minutes. Updating this value by itself will not trigger a delay. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/sleep#create_duration Sleep#create_duration}
        :param destroy_duration: `Time duration <https://golang.org/pkg/time/#ParseDuration>`_ to delay resource destroy. For example, ``30s`` for 30 seconds or ``5m`` for 5 minutes. Updating this value by itself will not trigger a delay. This value or any updates to it must be successfully applied into the Terraform state before destroying this resource to take effect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/sleep#destroy_duration Sleep#destroy_duration}
        :param triggers: (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See `the main provider documentation <../index.md>`_ for more information. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/sleep#triggers Sleep#triggers}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(SleepConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument create_duration", value=create_duration, expected_type=type_hints["create_duration"])
            check_type(argname="argument destroy_duration", value=destroy_duration, expected_type=type_hints["destroy_duration"])
            check_type(argname="argument triggers", value=triggers, expected_type=type_hints["triggers"])
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
        if create_duration is not None:
            self._values["create_duration"] = create_duration
        if destroy_duration is not None:
            self._values["destroy_duration"] = destroy_duration
        if triggers is not None:
            self._values["triggers"] = triggers

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
    def create_duration(self) -> typing.Optional[builtins.str]:
        '''`Time duration <https://golang.org/pkg/time/#ParseDuration>`_ to delay resource creation. For example, ``30s`` for 30 seconds or ``5m`` for 5 minutes. Updating this value by itself will not trigger a delay.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/sleep#create_duration Sleep#create_duration}
        '''
        result = self._values.get("create_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destroy_duration(self) -> typing.Optional[builtins.str]:
        '''`Time duration <https://golang.org/pkg/time/#ParseDuration>`_ to delay resource destroy. For example, ``30s`` for 30 seconds or ``5m`` for 5 minutes. Updating this value by itself will not trigger a delay. This value or any updates to it must be successfully applied into the Terraform state before destroying this resource to take effect.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/sleep#destroy_duration Sleep#destroy_duration}
        '''
        result = self._values.get("destroy_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def triggers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again.

        See `the main provider documentation <../index.md>`_ for more information.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/sleep#triggers Sleep#triggers}
        '''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SleepConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Sleep",
    "SleepConfig",
]

publication.publish()
