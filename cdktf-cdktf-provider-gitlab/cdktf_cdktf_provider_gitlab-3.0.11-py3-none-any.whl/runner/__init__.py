'''
# `gitlab_runner`

Refer to the Terraform Registory for docs: [`gitlab_runner`](https://www.terraform.io/docs/providers/gitlab/r/runner).
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


class Runner(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.runner.Runner",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/runner gitlab_runner}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        registration_token: builtins.str,
        access_level: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        locked: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        maximum_timeout: typing.Optional[jsii.Number] = None,
        paused: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        run_untagged: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/runner gitlab_runner} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param registration_token: The registration token used to register the runner. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#registration_token Runner#registration_token}
        :param access_level: The access_level of the runner. Valid values are: ``not_protected``, ``ref_protected``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#access_level Runner#access_level}
        :param description: The runner's description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#description Runner#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#id Runner#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param locked: Whether the runner should be locked for current project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#locked Runner#locked}
        :param maximum_timeout: Maximum timeout set when this runner handles the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#maximum_timeout Runner#maximum_timeout}
        :param paused: Whether the runner should ignore new jobs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#paused Runner#paused}
        :param run_untagged: Whether the runner should handle untagged jobs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#run_untagged Runner#run_untagged}
        :param tag_list: List of runner’s tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#tag_list Runner#tag_list}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Runner.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RunnerConfig(
            registration_token=registration_token,
            access_level=access_level,
            description=description,
            id=id,
            locked=locked,
            maximum_timeout=maximum_timeout,
            paused=paused,
            run_untagged=run_untagged,
            tag_list=tag_list,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAccessLevel")
    def reset_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessLevel", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocked")
    def reset_locked(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocked", []))

    @jsii.member(jsii_name="resetMaximumTimeout")
    def reset_maximum_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumTimeout", []))

    @jsii.member(jsii_name="resetPaused")
    def reset_paused(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPaused", []))

    @jsii.member(jsii_name="resetRunUntagged")
    def reset_run_untagged(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunUntagged", []))

    @jsii.member(jsii_name="resetTagList")
    def reset_tag_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagList", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="authenticationToken")
    def authentication_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationToken"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="accessLevelInput")
    def access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lockedInput")
    def locked_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "lockedInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumTimeoutInput")
    def maximum_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="pausedInput")
    def paused_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "pausedInput"))

    @builtins.property
    @jsii.member(jsii_name="registrationTokenInput")
    def registration_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registrationTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="runUntaggedInput")
    def run_untagged_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "runUntaggedInput"))

    @builtins.property
    @jsii.member(jsii_name="tagListInput")
    def tag_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagListInput"))

    @builtins.property
    @jsii.member(jsii_name="accessLevel")
    def access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessLevel"))

    @access_level.setter
    def access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Runner, "access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Runner, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Runner, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="locked")
    def locked(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "locked"))

    @locked.setter
    def locked(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Runner, "locked").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locked", value)

    @builtins.property
    @jsii.member(jsii_name="maximumTimeout")
    def maximum_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumTimeout"))

    @maximum_timeout.setter
    def maximum_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Runner, "maximum_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="paused")
    def paused(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "paused"))

    @paused.setter
    def paused(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Runner, "paused").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paused", value)

    @builtins.property
    @jsii.member(jsii_name="registrationToken")
    def registration_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registrationToken"))

    @registration_token.setter
    def registration_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Runner, "registration_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registrationToken", value)

    @builtins.property
    @jsii.member(jsii_name="runUntagged")
    def run_untagged(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "runUntagged"))

    @run_untagged.setter
    def run_untagged(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Runner, "run_untagged").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runUntagged", value)

    @builtins.property
    @jsii.member(jsii_name="tagList")
    def tag_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tagList"))

    @tag_list.setter
    def tag_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Runner, "tag_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagList", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.runner.RunnerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "registration_token": "registrationToken",
        "access_level": "accessLevel",
        "description": "description",
        "id": "id",
        "locked": "locked",
        "maximum_timeout": "maximumTimeout",
        "paused": "paused",
        "run_untagged": "runUntagged",
        "tag_list": "tagList",
    },
)
class RunnerConfig(cdktf.TerraformMetaArguments):
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
        registration_token: builtins.str,
        access_level: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        locked: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        maximum_timeout: typing.Optional[jsii.Number] = None,
        paused: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        run_untagged: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param registration_token: The registration token used to register the runner. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#registration_token Runner#registration_token}
        :param access_level: The access_level of the runner. Valid values are: ``not_protected``, ``ref_protected``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#access_level Runner#access_level}
        :param description: The runner's description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#description Runner#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#id Runner#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param locked: Whether the runner should be locked for current project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#locked Runner#locked}
        :param maximum_timeout: Maximum timeout set when this runner handles the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#maximum_timeout Runner#maximum_timeout}
        :param paused: Whether the runner should ignore new jobs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#paused Runner#paused}
        :param run_untagged: Whether the runner should handle untagged jobs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#run_untagged Runner#run_untagged}
        :param tag_list: List of runner’s tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#tag_list Runner#tag_list}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(RunnerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument registration_token", value=registration_token, expected_type=type_hints["registration_token"])
            check_type(argname="argument access_level", value=access_level, expected_type=type_hints["access_level"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument locked", value=locked, expected_type=type_hints["locked"])
            check_type(argname="argument maximum_timeout", value=maximum_timeout, expected_type=type_hints["maximum_timeout"])
            check_type(argname="argument paused", value=paused, expected_type=type_hints["paused"])
            check_type(argname="argument run_untagged", value=run_untagged, expected_type=type_hints["run_untagged"])
            check_type(argname="argument tag_list", value=tag_list, expected_type=type_hints["tag_list"])
        self._values: typing.Dict[str, typing.Any] = {
            "registration_token": registration_token,
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
        if access_level is not None:
            self._values["access_level"] = access_level
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if locked is not None:
            self._values["locked"] = locked
        if maximum_timeout is not None:
            self._values["maximum_timeout"] = maximum_timeout
        if paused is not None:
            self._values["paused"] = paused
        if run_untagged is not None:
            self._values["run_untagged"] = run_untagged
        if tag_list is not None:
            self._values["tag_list"] = tag_list

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
    def registration_token(self) -> builtins.str:
        '''The registration token used to register the runner.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#registration_token Runner#registration_token}
        '''
        result = self._values.get("registration_token")
        assert result is not None, "Required property 'registration_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_level(self) -> typing.Optional[builtins.str]:
        '''The access_level of the runner. Valid values are: ``not_protected``, ``ref_protected``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#access_level Runner#access_level}
        '''
        result = self._values.get("access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The runner's description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#description Runner#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#id Runner#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locked(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the runner should be locked for current project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#locked Runner#locked}
        '''
        result = self._values.get("locked")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def maximum_timeout(self) -> typing.Optional[jsii.Number]:
        '''Maximum timeout set when this runner handles the job.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#maximum_timeout Runner#maximum_timeout}
        '''
        result = self._values.get("maximum_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def paused(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the runner should ignore new jobs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#paused Runner#paused}
        '''
        result = self._values.get("paused")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def run_untagged(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the runner should handle untagged jobs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#run_untagged Runner#run_untagged}
        '''
        result = self._values.get("run_untagged")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tag_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of runner’s tags.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/runner#tag_list Runner#tag_list}
        '''
        result = self._values.get("tag_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RunnerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Runner",
    "RunnerConfig",
]

publication.publish()
