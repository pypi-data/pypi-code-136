'''
# `nomad_job`

Refer to the Terraform Registory for docs: [`nomad_job`](https://www.terraform.io/docs/providers/nomad/r/job).
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


class Job(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.Job",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/nomad/r/job nomad_job}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        jobspec: builtins.str,
        consul_token: typing.Optional[builtins.str] = None,
        deregister_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        deregister_on_id_change: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        detach: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hcl2: typing.Optional[typing.Union["JobHcl2", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        json: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        policy_override: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        purge_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["JobTimeouts", typing.Dict[str, typing.Any]]] = None,
        vault_token: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/nomad/r/job nomad_job} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param jobspec: Job specification. If you want to point to a file use the file() function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#jobspec Job#jobspec}
        :param consul_token: The Consul token used to submit this job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#consul_token Job#consul_token}
        :param deregister_on_destroy: If true, the job will be deregistered on destroy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#deregister_on_destroy Job#deregister_on_destroy}
        :param deregister_on_id_change: If true, the job will be deregistered when the job ID changes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#deregister_on_id_change Job#deregister_on_id_change}
        :param detach: If true, the provider will return immediately after creating or updating, instead of monitoring. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#detach Job#detach}
        :param hcl2: hcl2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#hcl2 Job#hcl2}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#id Job#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param json: If true, the ``jobspec`` will be parsed as json instead of HCL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#json Job#json}
        :param policy_override: Override any soft-mandatory Sentinel policies that fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#policy_override Job#policy_override}
        :param purge_on_destroy: Whether to purge the job when the resource is destroyed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#purge_on_destroy Job#purge_on_destroy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#timeouts Job#timeouts}
        :param vault_token: The Vault token used to submit this job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#vault_token Job#vault_token}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Job.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = JobConfig(
            jobspec=jobspec,
            consul_token=consul_token,
            deregister_on_destroy=deregister_on_destroy,
            deregister_on_id_change=deregister_on_id_change,
            detach=detach,
            hcl2=hcl2,
            id=id,
            json=json,
            policy_override=policy_override,
            purge_on_destroy=purge_on_destroy,
            timeouts=timeouts,
            vault_token=vault_token,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putHcl2")
    def put_hcl2(
        self,
        *,
        allow_fs: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param allow_fs: If true, HCL2 file system functions will be enabled when parsing the ``jobspec``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#allow_fs Job#allow_fs}
        :param enabled: If true, the ``jobspec`` will be parsed as HCL2 instead of HCL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#enabled Job#enabled}
        :param vars: Additional variables to use when templating the job with HCL2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#vars Job#vars}
        '''
        value = JobHcl2(allow_fs=allow_fs, enabled=enabled, vars=vars)

        return typing.cast(None, jsii.invoke(self, "putHcl2", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#create Job#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#update Job#update}.
        '''
        value = JobTimeouts(create=create, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetConsulToken")
    def reset_consul_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsulToken", []))

    @jsii.member(jsii_name="resetDeregisterOnDestroy")
    def reset_deregister_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeregisterOnDestroy", []))

    @jsii.member(jsii_name="resetDeregisterOnIdChange")
    def reset_deregister_on_id_change(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeregisterOnIdChange", []))

    @jsii.member(jsii_name="resetDetach")
    def reset_detach(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDetach", []))

    @jsii.member(jsii_name="resetHcl2")
    def reset_hcl2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHcl2", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetJson")
    def reset_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJson", []))

    @jsii.member(jsii_name="resetPolicyOverride")
    def reset_policy_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyOverride", []))

    @jsii.member(jsii_name="resetPurgeOnDestroy")
    def reset_purge_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPurgeOnDestroy", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVaultToken")
    def reset_vault_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVaultToken", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allocationIds")
    def allocation_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allocationIds"))

    @builtins.property
    @jsii.member(jsii_name="datacenters")
    def datacenters(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "datacenters"))

    @builtins.property
    @jsii.member(jsii_name="deploymentId")
    def deployment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentId"))

    @builtins.property
    @jsii.member(jsii_name="deploymentStatus")
    def deployment_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentStatus"))

    @builtins.property
    @jsii.member(jsii_name="hcl2")
    def hcl2(self) -> "JobHcl2OutputReference":
        return typing.cast("JobHcl2OutputReference", jsii.get(self, "hcl2"))

    @builtins.property
    @jsii.member(jsii_name="modifyIndex")
    def modify_index(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modifyIndex"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="taskGroups")
    def task_groups(self) -> "JobTaskGroupsList":
        return typing.cast("JobTaskGroupsList", jsii.get(self, "taskGroups"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "JobTimeoutsOutputReference":
        return typing.cast("JobTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="consulTokenInput")
    def consul_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consulTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="deregisterOnDestroyInput")
    def deregister_on_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deregisterOnDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="deregisterOnIdChangeInput")
    def deregister_on_id_change_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deregisterOnIdChangeInput"))

    @builtins.property
    @jsii.member(jsii_name="detachInput")
    def detach_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "detachInput"))

    @builtins.property
    @jsii.member(jsii_name="hcl2Input")
    def hcl2_input(self) -> typing.Optional["JobHcl2"]:
        return typing.cast(typing.Optional["JobHcl2"], jsii.get(self, "hcl2Input"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="jobspecInput")
    def jobspec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobspecInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonInput")
    def json_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "jsonInput"))

    @builtins.property
    @jsii.member(jsii_name="policyOverrideInput")
    def policy_override_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "policyOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="purgeOnDestroyInput")
    def purge_on_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "purgeOnDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["JobTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["JobTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vaultTokenInput")
    def vault_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vaultTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="consulToken")
    def consul_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulToken"))

    @consul_token.setter
    def consul_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Job, "consul_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consulToken", value)

    @builtins.property
    @jsii.member(jsii_name="deregisterOnDestroy")
    def deregister_on_destroy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deregisterOnDestroy"))

    @deregister_on_destroy.setter
    def deregister_on_destroy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Job, "deregister_on_destroy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deregisterOnDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="deregisterOnIdChange")
    def deregister_on_id_change(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deregisterOnIdChange"))

    @deregister_on_id_change.setter
    def deregister_on_id_change(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Job, "deregister_on_id_change").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deregisterOnIdChange", value)

    @builtins.property
    @jsii.member(jsii_name="detach")
    def detach(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "detach"))

    @detach.setter
    def detach(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Job, "detach").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detach", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Job, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="jobspec")
    def jobspec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobspec"))

    @jobspec.setter
    def jobspec(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Job, "jobspec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobspec", value)

    @builtins.property
    @jsii.member(jsii_name="json")
    def json(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "json"))

    @json.setter
    def json(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Job, "json").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "json", value)

    @builtins.property
    @jsii.member(jsii_name="policyOverride")
    def policy_override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "policyOverride"))

    @policy_override.setter
    def policy_override(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Job, "policy_override").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyOverride", value)

    @builtins.property
    @jsii.member(jsii_name="purgeOnDestroy")
    def purge_on_destroy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "purgeOnDestroy"))

    @purge_on_destroy.setter
    def purge_on_destroy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Job, "purge_on_destroy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "purgeOnDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="vaultToken")
    def vault_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vaultToken"))

    @vault_token.setter
    def vault_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Job, "vault_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vaultToken", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.job.JobConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "jobspec": "jobspec",
        "consul_token": "consulToken",
        "deregister_on_destroy": "deregisterOnDestroy",
        "deregister_on_id_change": "deregisterOnIdChange",
        "detach": "detach",
        "hcl2": "hcl2",
        "id": "id",
        "json": "json",
        "policy_override": "policyOverride",
        "purge_on_destroy": "purgeOnDestroy",
        "timeouts": "timeouts",
        "vault_token": "vaultToken",
    },
)
class JobConfig(cdktf.TerraformMetaArguments):
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
        jobspec: builtins.str,
        consul_token: typing.Optional[builtins.str] = None,
        deregister_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        deregister_on_id_change: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        detach: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hcl2: typing.Optional[typing.Union["JobHcl2", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        json: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        policy_override: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        purge_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["JobTimeouts", typing.Dict[str, typing.Any]]] = None,
        vault_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param jobspec: Job specification. If you want to point to a file use the file() function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#jobspec Job#jobspec}
        :param consul_token: The Consul token used to submit this job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#consul_token Job#consul_token}
        :param deregister_on_destroy: If true, the job will be deregistered on destroy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#deregister_on_destroy Job#deregister_on_destroy}
        :param deregister_on_id_change: If true, the job will be deregistered when the job ID changes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#deregister_on_id_change Job#deregister_on_id_change}
        :param detach: If true, the provider will return immediately after creating or updating, instead of monitoring. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#detach Job#detach}
        :param hcl2: hcl2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#hcl2 Job#hcl2}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#id Job#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param json: If true, the ``jobspec`` will be parsed as json instead of HCL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#json Job#json}
        :param policy_override: Override any soft-mandatory Sentinel policies that fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#policy_override Job#policy_override}
        :param purge_on_destroy: Whether to purge the job when the resource is destroyed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#purge_on_destroy Job#purge_on_destroy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#timeouts Job#timeouts}
        :param vault_token: The Vault token used to submit this job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#vault_token Job#vault_token}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(hcl2, dict):
            hcl2 = JobHcl2(**hcl2)
        if isinstance(timeouts, dict):
            timeouts = JobTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(JobConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument jobspec", value=jobspec, expected_type=type_hints["jobspec"])
            check_type(argname="argument consul_token", value=consul_token, expected_type=type_hints["consul_token"])
            check_type(argname="argument deregister_on_destroy", value=deregister_on_destroy, expected_type=type_hints["deregister_on_destroy"])
            check_type(argname="argument deregister_on_id_change", value=deregister_on_id_change, expected_type=type_hints["deregister_on_id_change"])
            check_type(argname="argument detach", value=detach, expected_type=type_hints["detach"])
            check_type(argname="argument hcl2", value=hcl2, expected_type=type_hints["hcl2"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument json", value=json, expected_type=type_hints["json"])
            check_type(argname="argument policy_override", value=policy_override, expected_type=type_hints["policy_override"])
            check_type(argname="argument purge_on_destroy", value=purge_on_destroy, expected_type=type_hints["purge_on_destroy"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vault_token", value=vault_token, expected_type=type_hints["vault_token"])
        self._values: typing.Dict[str, typing.Any] = {
            "jobspec": jobspec,
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
        if consul_token is not None:
            self._values["consul_token"] = consul_token
        if deregister_on_destroy is not None:
            self._values["deregister_on_destroy"] = deregister_on_destroy
        if deregister_on_id_change is not None:
            self._values["deregister_on_id_change"] = deregister_on_id_change
        if detach is not None:
            self._values["detach"] = detach
        if hcl2 is not None:
            self._values["hcl2"] = hcl2
        if id is not None:
            self._values["id"] = id
        if json is not None:
            self._values["json"] = json
        if policy_override is not None:
            self._values["policy_override"] = policy_override
        if purge_on_destroy is not None:
            self._values["purge_on_destroy"] = purge_on_destroy
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vault_token is not None:
            self._values["vault_token"] = vault_token

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
    def jobspec(self) -> builtins.str:
        '''Job specification. If you want to point to a file use the file() function.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#jobspec Job#jobspec}
        '''
        result = self._values.get("jobspec")
        assert result is not None, "Required property 'jobspec' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def consul_token(self) -> typing.Optional[builtins.str]:
        '''The Consul token used to submit this job.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#consul_token Job#consul_token}
        '''
        result = self._values.get("consul_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deregister_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the job will be deregistered on destroy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#deregister_on_destroy Job#deregister_on_destroy}
        '''
        result = self._values.get("deregister_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def deregister_on_id_change(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the job will be deregistered when the job ID changes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#deregister_on_id_change Job#deregister_on_id_change}
        '''
        result = self._values.get("deregister_on_id_change")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def detach(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the provider will return immediately after creating or updating, instead of monitoring.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#detach Job#detach}
        '''
        result = self._values.get("detach")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def hcl2(self) -> typing.Optional["JobHcl2"]:
        '''hcl2 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#hcl2 Job#hcl2}
        '''
        result = self._values.get("hcl2")
        return typing.cast(typing.Optional["JobHcl2"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#id Job#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def json(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the ``jobspec`` will be parsed as json instead of HCL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#json Job#json}
        '''
        result = self._values.get("json")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def policy_override(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Override any soft-mandatory Sentinel policies that fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#policy_override Job#policy_override}
        '''
        result = self._values.get("policy_override")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def purge_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to purge the job when the resource is destroyed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#purge_on_destroy Job#purge_on_destroy}
        '''
        result = self._values.get("purge_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["JobTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#timeouts Job#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["JobTimeouts"], result)

    @builtins.property
    def vault_token(self) -> typing.Optional[builtins.str]:
        '''The Vault token used to submit this job.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#vault_token Job#vault_token}
        '''
        result = self._values.get("vault_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.job.JobHcl2",
    jsii_struct_bases=[],
    name_mapping={"allow_fs": "allowFs", "enabled": "enabled", "vars": "vars"},
)
class JobHcl2:
    def __init__(
        self,
        *,
        allow_fs: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param allow_fs: If true, HCL2 file system functions will be enabled when parsing the ``jobspec``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#allow_fs Job#allow_fs}
        :param enabled: If true, the ``jobspec`` will be parsed as HCL2 instead of HCL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#enabled Job#enabled}
        :param vars: Additional variables to use when templating the job with HCL2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#vars Job#vars}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(JobHcl2.__init__)
            check_type(argname="argument allow_fs", value=allow_fs, expected_type=type_hints["allow_fs"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument vars", value=vars, expected_type=type_hints["vars"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_fs is not None:
            self._values["allow_fs"] = allow_fs
        if enabled is not None:
            self._values["enabled"] = enabled
        if vars is not None:
            self._values["vars"] = vars

    @builtins.property
    def allow_fs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, HCL2 file system functions will be enabled when parsing the ``jobspec``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#allow_fs Job#allow_fs}
        '''
        result = self._values.get("allow_fs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the ``jobspec`` will be parsed as HCL2 instead of HCL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#enabled Job#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def vars(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional variables to use when templating the job with HCL2.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#vars Job#vars}
        '''
        result = self._values.get("vars")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobHcl2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JobHcl2OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobHcl2OutputReference",
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
            type_hints = typing.get_type_hints(JobHcl2OutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowFs")
    def reset_allow_fs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowFs", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetVars")
    def reset_vars(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVars", []))

    @builtins.property
    @jsii.member(jsii_name="allowFsInput")
    def allow_fs_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowFsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="varsInput")
    def vars_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "varsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowFs")
    def allow_fs(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowFs"))

    @allow_fs.setter
    def allow_fs(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JobHcl2OutputReference, "allow_fs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowFs", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JobHcl2OutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="vars")
    def vars(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "vars"))

    @vars.setter
    def vars(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JobHcl2OutputReference, "vars").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vars", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[JobHcl2]:
        return typing.cast(typing.Optional[JobHcl2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[JobHcl2]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JobHcl2OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroups",
    jsii_struct_bases=[],
    name_mapping={},
)
class JobTaskGroups:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobTaskGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JobTaskGroupsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsList",
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
            type_hints = typing.get_type_hints(JobTaskGroupsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "JobTaskGroupsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(JobTaskGroupsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("JobTaskGroupsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class JobTaskGroupsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsOutputReference",
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
            type_hints = typing.get_type_hints(JobTaskGroupsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @builtins.property
    @jsii.member(jsii_name="meta")
    def meta(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "meta"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="task")
    def task(self) -> "JobTaskGroupsTaskList":
        return typing.cast("JobTaskGroupsTaskList", jsii.get(self, "task"))

    @builtins.property
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> "JobTaskGroupsVolumesList":
        return typing.cast("JobTaskGroupsVolumesList", jsii.get(self, "volumes"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[JobTaskGroups]:
        return typing.cast(typing.Optional[JobTaskGroups], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[JobTaskGroups]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsTask",
    jsii_struct_bases=[],
    name_mapping={},
)
class JobTaskGroupsTask:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobTaskGroupsTask(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JobTaskGroupsTaskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsTaskList",
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
            type_hints = typing.get_type_hints(JobTaskGroupsTaskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "JobTaskGroupsTaskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(JobTaskGroupsTaskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("JobTaskGroupsTaskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsTaskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsTaskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsTaskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class JobTaskGroupsTaskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsTaskOutputReference",
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
            type_hints = typing.get_type_hints(JobTaskGroupsTaskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @builtins.property
    @jsii.member(jsii_name="meta")
    def meta(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "meta"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="volumeMounts")
    def volume_mounts(self) -> "JobTaskGroupsTaskVolumeMountsList":
        return typing.cast("JobTaskGroupsTaskVolumeMountsList", jsii.get(self, "volumeMounts"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[JobTaskGroupsTask]:
        return typing.cast(typing.Optional[JobTaskGroupsTask], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[JobTaskGroupsTask]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsTaskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsTaskVolumeMounts",
    jsii_struct_bases=[],
    name_mapping={},
)
class JobTaskGroupsTaskVolumeMounts:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobTaskGroupsTaskVolumeMounts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JobTaskGroupsTaskVolumeMountsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsTaskVolumeMountsList",
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
            type_hints = typing.get_type_hints(JobTaskGroupsTaskVolumeMountsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "JobTaskGroupsTaskVolumeMountsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(JobTaskGroupsTaskVolumeMountsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("JobTaskGroupsTaskVolumeMountsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsTaskVolumeMountsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsTaskVolumeMountsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsTaskVolumeMountsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class JobTaskGroupsTaskVolumeMountsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsTaskVolumeMountsOutputReference",
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
            type_hints = typing.get_type_hints(JobTaskGroupsTaskVolumeMountsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "readOnly"))

    @builtins.property
    @jsii.member(jsii_name="volume")
    def volume(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volume"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[JobTaskGroupsTaskVolumeMounts]:
        return typing.cast(typing.Optional[JobTaskGroupsTaskVolumeMounts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[JobTaskGroupsTaskVolumeMounts],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsTaskVolumeMountsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsVolumes",
    jsii_struct_bases=[],
    name_mapping={},
)
class JobTaskGroupsVolumes:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobTaskGroupsVolumes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JobTaskGroupsVolumesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsVolumesList",
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
            type_hints = typing.get_type_hints(JobTaskGroupsVolumesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "JobTaskGroupsVolumesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(JobTaskGroupsVolumesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("JobTaskGroupsVolumesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsVolumesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsVolumesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsVolumesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class JobTaskGroupsVolumesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsVolumesOutputReference",
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
            type_hints = typing.get_type_hints(JobTaskGroupsVolumesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "readOnly"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[JobTaskGroupsVolumes]:
        return typing.cast(typing.Optional[JobTaskGroupsVolumes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[JobTaskGroupsVolumes]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JobTaskGroupsVolumesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.job.JobTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "update": "update"},
)
class JobTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#create Job#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#update Job#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(JobTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#create Job#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#update Job#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JobTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(JobTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

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
            type_hints = typing.get_type_hints(getattr(JobTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JobTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[JobTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[JobTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[JobTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JobTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Job",
    "JobConfig",
    "JobHcl2",
    "JobHcl2OutputReference",
    "JobTaskGroups",
    "JobTaskGroupsList",
    "JobTaskGroupsOutputReference",
    "JobTaskGroupsTask",
    "JobTaskGroupsTaskList",
    "JobTaskGroupsTaskOutputReference",
    "JobTaskGroupsTaskVolumeMounts",
    "JobTaskGroupsTaskVolumeMountsList",
    "JobTaskGroupsTaskVolumeMountsOutputReference",
    "JobTaskGroupsVolumes",
    "JobTaskGroupsVolumesList",
    "JobTaskGroupsVolumesOutputReference",
    "JobTimeouts",
    "JobTimeoutsOutputReference",
]

publication.publish()
