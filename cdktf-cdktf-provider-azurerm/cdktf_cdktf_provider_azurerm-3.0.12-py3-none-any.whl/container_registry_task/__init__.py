'''
# `azurerm_container_registry_task`

Refer to the Terraform Registory for docs: [`azurerm_container_registry_task`](https://www.terraform.io/docs/providers/azurerm/r/container_registry_task).
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


class ContainerRegistryTask(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTask",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task azurerm_container_registry_task}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        container_registry_id: builtins.str,
        name: builtins.str,
        agent_pool_name: typing.Optional[builtins.str] = None,
        agent_setting: typing.Optional[typing.Union["ContainerRegistryTaskAgentSetting", typing.Dict[str, typing.Any]]] = None,
        base_image_trigger: typing.Optional[typing.Union["ContainerRegistryTaskBaseImageTrigger", typing.Dict[str, typing.Any]]] = None,
        docker_step: typing.Optional[typing.Union["ContainerRegistryTaskDockerStep", typing.Dict[str, typing.Any]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encoded_step: typing.Optional[typing.Union["ContainerRegistryTaskEncodedStep", typing.Dict[str, typing.Any]]] = None,
        file_step: typing.Optional[typing.Union["ContainerRegistryTaskFileStep", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["ContainerRegistryTaskIdentity", typing.Dict[str, typing.Any]]] = None,
        is_system_task: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_template: typing.Optional[builtins.str] = None,
        platform: typing.Optional[typing.Union["ContainerRegistryTaskPlatform", typing.Dict[str, typing.Any]]] = None,
        registry_credential: typing.Optional[typing.Union["ContainerRegistryTaskRegistryCredential", typing.Dict[str, typing.Any]]] = None,
        source_trigger: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerRegistryTaskSourceTrigger", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout_in_seconds: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["ContainerRegistryTaskTimeouts", typing.Dict[str, typing.Any]]] = None,
        timer_trigger: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerRegistryTaskTimerTrigger", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task azurerm_container_registry_task} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param container_registry_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#container_registry_id ContainerRegistryTask#container_registry_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#name ContainerRegistryTask#name}.
        :param agent_pool_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#agent_pool_name ContainerRegistryTask#agent_pool_name}.
        :param agent_setting: agent_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#agent_setting ContainerRegistryTask#agent_setting}
        :param base_image_trigger: base_image_trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#base_image_trigger ContainerRegistryTask#base_image_trigger}
        :param docker_step: docker_step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#docker_step ContainerRegistryTask#docker_step}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#enabled ContainerRegistryTask#enabled}.
        :param encoded_step: encoded_step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#encoded_step ContainerRegistryTask#encoded_step}
        :param file_step: file_step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#file_step ContainerRegistryTask#file_step}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#id ContainerRegistryTask#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#identity ContainerRegistryTask#identity}
        :param is_system_task: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#is_system_task ContainerRegistryTask#is_system_task}.
        :param log_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#log_template ContainerRegistryTask#log_template}.
        :param platform: platform block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#platform ContainerRegistryTask#platform}
        :param registry_credential: registry_credential block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#registry_credential ContainerRegistryTask#registry_credential}
        :param source_trigger: source_trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#source_trigger ContainerRegistryTask#source_trigger}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#tags ContainerRegistryTask#tags}.
        :param timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#timeout_in_seconds ContainerRegistryTask#timeout_in_seconds}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#timeouts ContainerRegistryTask#timeouts}
        :param timer_trigger: timer_trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#timer_trigger ContainerRegistryTask#timer_trigger}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTask.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ContainerRegistryTaskConfig(
            container_registry_id=container_registry_id,
            name=name,
            agent_pool_name=agent_pool_name,
            agent_setting=agent_setting,
            base_image_trigger=base_image_trigger,
            docker_step=docker_step,
            enabled=enabled,
            encoded_step=encoded_step,
            file_step=file_step,
            id=id,
            identity=identity,
            is_system_task=is_system_task,
            log_template=log_template,
            platform=platform,
            registry_credential=registry_credential,
            source_trigger=source_trigger,
            tags=tags,
            timeout_in_seconds=timeout_in_seconds,
            timeouts=timeouts,
            timer_trigger=timer_trigger,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAgentSetting")
    def put_agent_setting(self, *, cpu: jsii.Number) -> None:
        '''
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#cpu ContainerRegistryTask#cpu}.
        '''
        value = ContainerRegistryTaskAgentSetting(cpu=cpu)

        return typing.cast(None, jsii.invoke(self, "putAgentSetting", [value]))

    @jsii.member(jsii_name="putBaseImageTrigger")
    def put_base_image_trigger(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        update_trigger_endpoint: typing.Optional[builtins.str] = None,
        update_trigger_payload_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#name ContainerRegistryTask#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#type ContainerRegistryTask#type}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#enabled ContainerRegistryTask#enabled}.
        :param update_trigger_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#update_trigger_endpoint ContainerRegistryTask#update_trigger_endpoint}.
        :param update_trigger_payload_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#update_trigger_payload_type ContainerRegistryTask#update_trigger_payload_type}.
        '''
        value = ContainerRegistryTaskBaseImageTrigger(
            name=name,
            type=type,
            enabled=enabled,
            update_trigger_endpoint=update_trigger_endpoint,
            update_trigger_payload_type=update_trigger_payload_type,
        )

        return typing.cast(None, jsii.invoke(self, "putBaseImageTrigger", [value]))

    @jsii.member(jsii_name="putDockerStep")
    def put_docker_step(
        self,
        *,
        context_access_token: builtins.str,
        context_path: builtins.str,
        dockerfile_path: builtins.str,
        arguments: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        cache_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        image_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        push_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secret_arguments: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param context_access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_access_token ContainerRegistryTask#context_access_token}.
        :param context_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_path ContainerRegistryTask#context_path}.
        :param dockerfile_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#dockerfile_path ContainerRegistryTask#dockerfile_path}.
        :param arguments: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#arguments ContainerRegistryTask#arguments}.
        :param cache_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#cache_enabled ContainerRegistryTask#cache_enabled}.
        :param image_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#image_names ContainerRegistryTask#image_names}.
        :param push_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#push_enabled ContainerRegistryTask#push_enabled}.
        :param secret_arguments: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#secret_arguments ContainerRegistryTask#secret_arguments}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#target ContainerRegistryTask#target}.
        '''
        value = ContainerRegistryTaskDockerStep(
            context_access_token=context_access_token,
            context_path=context_path,
            dockerfile_path=dockerfile_path,
            arguments=arguments,
            cache_enabled=cache_enabled,
            image_names=image_names,
            push_enabled=push_enabled,
            secret_arguments=secret_arguments,
            target=target,
        )

        return typing.cast(None, jsii.invoke(self, "putDockerStep", [value]))

    @jsii.member(jsii_name="putEncodedStep")
    def put_encoded_step(
        self,
        *,
        task_content: builtins.str,
        context_access_token: typing.Optional[builtins.str] = None,
        context_path: typing.Optional[builtins.str] = None,
        secret_values: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        value_content: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param task_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#task_content ContainerRegistryTask#task_content}.
        :param context_access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_access_token ContainerRegistryTask#context_access_token}.
        :param context_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_path ContainerRegistryTask#context_path}.
        :param secret_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#secret_values ContainerRegistryTask#secret_values}.
        :param value_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#value_content ContainerRegistryTask#value_content}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#values ContainerRegistryTask#values}.
        '''
        value = ContainerRegistryTaskEncodedStep(
            task_content=task_content,
            context_access_token=context_access_token,
            context_path=context_path,
            secret_values=secret_values,
            value_content=value_content,
            values=values,
        )

        return typing.cast(None, jsii.invoke(self, "putEncodedStep", [value]))

    @jsii.member(jsii_name="putFileStep")
    def put_file_step(
        self,
        *,
        task_file_path: builtins.str,
        context_access_token: typing.Optional[builtins.str] = None,
        context_path: typing.Optional[builtins.str] = None,
        secret_values: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        value_file_path: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param task_file_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#task_file_path ContainerRegistryTask#task_file_path}.
        :param context_access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_access_token ContainerRegistryTask#context_access_token}.
        :param context_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_path ContainerRegistryTask#context_path}.
        :param secret_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#secret_values ContainerRegistryTask#secret_values}.
        :param value_file_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#value_file_path ContainerRegistryTask#value_file_path}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#values ContainerRegistryTask#values}.
        '''
        value = ContainerRegistryTaskFileStep(
            task_file_path=task_file_path,
            context_access_token=context_access_token,
            context_path=context_path,
            secret_values=secret_values,
            value_file_path=value_file_path,
            values=values,
        )

        return typing.cast(None, jsii.invoke(self, "putFileStep", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#type ContainerRegistryTask#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#identity_ids ContainerRegistryTask#identity_ids}.
        '''
        value = ContainerRegistryTaskIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putPlatform")
    def put_platform(
        self,
        *,
        os: builtins.str,
        architecture: typing.Optional[builtins.str] = None,
        variant: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param os: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#os ContainerRegistryTask#os}.
        :param architecture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#architecture ContainerRegistryTask#architecture}.
        :param variant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#variant ContainerRegistryTask#variant}.
        '''
        value = ContainerRegistryTaskPlatform(
            os=os, architecture=architecture, variant=variant
        )

        return typing.cast(None, jsii.invoke(self, "putPlatform", [value]))

    @jsii.member(jsii_name="putRegistryCredential")
    def put_registry_credential(
        self,
        *,
        custom: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerRegistryTaskRegistryCredentialCustom", typing.Dict[str, typing.Any]]]]] = None,
        source: typing.Optional[typing.Union["ContainerRegistryTaskRegistryCredentialSource", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom: custom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#custom ContainerRegistryTask#custom}
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#source ContainerRegistryTask#source}
        '''
        value = ContainerRegistryTaskRegistryCredential(custom=custom, source=source)

        return typing.cast(None, jsii.invoke(self, "putRegistryCredential", [value]))

    @jsii.member(jsii_name="putSourceTrigger")
    def put_source_trigger(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerRegistryTaskSourceTrigger", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTask.put_source_trigger)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSourceTrigger", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#create ContainerRegistryTask#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#delete ContainerRegistryTask#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#read ContainerRegistryTask#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#update ContainerRegistryTask#update}.
        '''
        value = ContainerRegistryTaskTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTimerTrigger")
    def put_timer_trigger(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerRegistryTaskTimerTrigger", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTask.put_timer_trigger)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTimerTrigger", [value]))

    @jsii.member(jsii_name="resetAgentPoolName")
    def reset_agent_pool_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAgentPoolName", []))

    @jsii.member(jsii_name="resetAgentSetting")
    def reset_agent_setting(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAgentSetting", []))

    @jsii.member(jsii_name="resetBaseImageTrigger")
    def reset_base_image_trigger(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseImageTrigger", []))

    @jsii.member(jsii_name="resetDockerStep")
    def reset_docker_step(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerStep", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEncodedStep")
    def reset_encoded_step(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncodedStep", []))

    @jsii.member(jsii_name="resetFileStep")
    def reset_file_step(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileStep", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetIsSystemTask")
    def reset_is_system_task(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsSystemTask", []))

    @jsii.member(jsii_name="resetLogTemplate")
    def reset_log_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogTemplate", []))

    @jsii.member(jsii_name="resetPlatform")
    def reset_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatform", []))

    @jsii.member(jsii_name="resetRegistryCredential")
    def reset_registry_credential(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistryCredential", []))

    @jsii.member(jsii_name="resetSourceTrigger")
    def reset_source_trigger(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceTrigger", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeoutInSeconds")
    def reset_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutInSeconds", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTimerTrigger")
    def reset_timer_trigger(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimerTrigger", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="agentSetting")
    def agent_setting(self) -> "ContainerRegistryTaskAgentSettingOutputReference":
        return typing.cast("ContainerRegistryTaskAgentSettingOutputReference", jsii.get(self, "agentSetting"))

    @builtins.property
    @jsii.member(jsii_name="baseImageTrigger")
    def base_image_trigger(
        self,
    ) -> "ContainerRegistryTaskBaseImageTriggerOutputReference":
        return typing.cast("ContainerRegistryTaskBaseImageTriggerOutputReference", jsii.get(self, "baseImageTrigger"))

    @builtins.property
    @jsii.member(jsii_name="dockerStep")
    def docker_step(self) -> "ContainerRegistryTaskDockerStepOutputReference":
        return typing.cast("ContainerRegistryTaskDockerStepOutputReference", jsii.get(self, "dockerStep"))

    @builtins.property
    @jsii.member(jsii_name="encodedStep")
    def encoded_step(self) -> "ContainerRegistryTaskEncodedStepOutputReference":
        return typing.cast("ContainerRegistryTaskEncodedStepOutputReference", jsii.get(self, "encodedStep"))

    @builtins.property
    @jsii.member(jsii_name="fileStep")
    def file_step(self) -> "ContainerRegistryTaskFileStepOutputReference":
        return typing.cast("ContainerRegistryTaskFileStepOutputReference", jsii.get(self, "fileStep"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "ContainerRegistryTaskIdentityOutputReference":
        return typing.cast("ContainerRegistryTaskIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> "ContainerRegistryTaskPlatformOutputReference":
        return typing.cast("ContainerRegistryTaskPlatformOutputReference", jsii.get(self, "platform"))

    @builtins.property
    @jsii.member(jsii_name="registryCredential")
    def registry_credential(
        self,
    ) -> "ContainerRegistryTaskRegistryCredentialOutputReference":
        return typing.cast("ContainerRegistryTaskRegistryCredentialOutputReference", jsii.get(self, "registryCredential"))

    @builtins.property
    @jsii.member(jsii_name="sourceTrigger")
    def source_trigger(self) -> "ContainerRegistryTaskSourceTriggerList":
        return typing.cast("ContainerRegistryTaskSourceTriggerList", jsii.get(self, "sourceTrigger"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ContainerRegistryTaskTimeoutsOutputReference":
        return typing.cast("ContainerRegistryTaskTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="timerTrigger")
    def timer_trigger(self) -> "ContainerRegistryTaskTimerTriggerList":
        return typing.cast("ContainerRegistryTaskTimerTriggerList", jsii.get(self, "timerTrigger"))

    @builtins.property
    @jsii.member(jsii_name="agentPoolNameInput")
    def agent_pool_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agentPoolNameInput"))

    @builtins.property
    @jsii.member(jsii_name="agentSettingInput")
    def agent_setting_input(
        self,
    ) -> typing.Optional["ContainerRegistryTaskAgentSetting"]:
        return typing.cast(typing.Optional["ContainerRegistryTaskAgentSetting"], jsii.get(self, "agentSettingInput"))

    @builtins.property
    @jsii.member(jsii_name="baseImageTriggerInput")
    def base_image_trigger_input(
        self,
    ) -> typing.Optional["ContainerRegistryTaskBaseImageTrigger"]:
        return typing.cast(typing.Optional["ContainerRegistryTaskBaseImageTrigger"], jsii.get(self, "baseImageTriggerInput"))

    @builtins.property
    @jsii.member(jsii_name="containerRegistryIdInput")
    def container_registry_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerRegistryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerStepInput")
    def docker_step_input(self) -> typing.Optional["ContainerRegistryTaskDockerStep"]:
        return typing.cast(typing.Optional["ContainerRegistryTaskDockerStep"], jsii.get(self, "dockerStepInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="encodedStepInput")
    def encoded_step_input(self) -> typing.Optional["ContainerRegistryTaskEncodedStep"]:
        return typing.cast(typing.Optional["ContainerRegistryTaskEncodedStep"], jsii.get(self, "encodedStepInput"))

    @builtins.property
    @jsii.member(jsii_name="fileStepInput")
    def file_step_input(self) -> typing.Optional["ContainerRegistryTaskFileStep"]:
        return typing.cast(typing.Optional["ContainerRegistryTaskFileStep"], jsii.get(self, "fileStepInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["ContainerRegistryTaskIdentity"]:
        return typing.cast(typing.Optional["ContainerRegistryTaskIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isSystemTaskInput")
    def is_system_task_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isSystemTaskInput"))

    @builtins.property
    @jsii.member(jsii_name="logTemplateInput")
    def log_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="platformInput")
    def platform_input(self) -> typing.Optional["ContainerRegistryTaskPlatform"]:
        return typing.cast(typing.Optional["ContainerRegistryTaskPlatform"], jsii.get(self, "platformInput"))

    @builtins.property
    @jsii.member(jsii_name="registryCredentialInput")
    def registry_credential_input(
        self,
    ) -> typing.Optional["ContainerRegistryTaskRegistryCredential"]:
        return typing.cast(typing.Optional["ContainerRegistryTaskRegistryCredential"], jsii.get(self, "registryCredentialInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceTriggerInput")
    def source_trigger_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerRegistryTaskSourceTrigger"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerRegistryTaskSourceTrigger"]]], jsii.get(self, "sourceTriggerInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInSecondsInput")
    def timeout_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ContainerRegistryTaskTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ContainerRegistryTaskTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timerTriggerInput")
    def timer_trigger_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerRegistryTaskTimerTrigger"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerRegistryTaskTimerTrigger"]]], jsii.get(self, "timerTriggerInput"))

    @builtins.property
    @jsii.member(jsii_name="agentPoolName")
    def agent_pool_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "agentPoolName"))

    @agent_pool_name.setter
    def agent_pool_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTask, "agent_pool_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentPoolName", value)

    @builtins.property
    @jsii.member(jsii_name="containerRegistryId")
    def container_registry_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerRegistryId"))

    @container_registry_id.setter
    def container_registry_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTask, "container_registry_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryId", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTask, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTask, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isSystemTask")
    def is_system_task(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isSystemTask"))

    @is_system_task.setter
    def is_system_task(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTask, "is_system_task").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isSystemTask", value)

    @builtins.property
    @jsii.member(jsii_name="logTemplate")
    def log_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logTemplate"))

    @log_template.setter
    def log_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTask, "log_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTask, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTask, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutInSeconds")
    def timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutInSeconds"))

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTask, "timeout_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutInSeconds", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskAgentSetting",
    jsii_struct_bases=[],
    name_mapping={"cpu": "cpu"},
)
class ContainerRegistryTaskAgentSetting:
    def __init__(self, *, cpu: jsii.Number) -> None:
        '''
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#cpu ContainerRegistryTask#cpu}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskAgentSetting.__init__)
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
        self._values: typing.Dict[str, typing.Any] = {
            "cpu": cpu,
        }

    @builtins.property
    def cpu(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#cpu ContainerRegistryTask#cpu}.'''
        result = self._values.get("cpu")
        assert result is not None, "Required property 'cpu' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTaskAgentSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerRegistryTaskAgentSettingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskAgentSettingOutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskAgentSettingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskAgentSettingOutputReference, "cpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpu", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerRegistryTaskAgentSetting]:
        return typing.cast(typing.Optional[ContainerRegistryTaskAgentSetting], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerRegistryTaskAgentSetting],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskAgentSettingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskBaseImageTrigger",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "enabled": "enabled",
        "update_trigger_endpoint": "updateTriggerEndpoint",
        "update_trigger_payload_type": "updateTriggerPayloadType",
    },
)
class ContainerRegistryTaskBaseImageTrigger:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        update_trigger_endpoint: typing.Optional[builtins.str] = None,
        update_trigger_payload_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#name ContainerRegistryTask#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#type ContainerRegistryTask#type}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#enabled ContainerRegistryTask#enabled}.
        :param update_trigger_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#update_trigger_endpoint ContainerRegistryTask#update_trigger_endpoint}.
        :param update_trigger_payload_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#update_trigger_payload_type ContainerRegistryTask#update_trigger_payload_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskBaseImageTrigger.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument update_trigger_endpoint", value=update_trigger_endpoint, expected_type=type_hints["update_trigger_endpoint"])
            check_type(argname="argument update_trigger_payload_type", value=update_trigger_payload_type, expected_type=type_hints["update_trigger_payload_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if update_trigger_endpoint is not None:
            self._values["update_trigger_endpoint"] = update_trigger_endpoint
        if update_trigger_payload_type is not None:
            self._values["update_trigger_payload_type"] = update_trigger_payload_type

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#name ContainerRegistryTask#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#type ContainerRegistryTask#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#enabled ContainerRegistryTask#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def update_trigger_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#update_trigger_endpoint ContainerRegistryTask#update_trigger_endpoint}.'''
        result = self._values.get("update_trigger_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update_trigger_payload_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#update_trigger_payload_type ContainerRegistryTask#update_trigger_payload_type}.'''
        result = self._values.get("update_trigger_payload_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTaskBaseImageTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerRegistryTaskBaseImageTriggerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskBaseImageTriggerOutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskBaseImageTriggerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetUpdateTriggerEndpoint")
    def reset_update_trigger_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdateTriggerEndpoint", []))

    @jsii.member(jsii_name="resetUpdateTriggerPayloadType")
    def reset_update_trigger_payload_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdateTriggerPayloadType", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="updateTriggerEndpointInput")
    def update_trigger_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateTriggerEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="updateTriggerPayloadTypeInput")
    def update_trigger_payload_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateTriggerPayloadTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskBaseImageTriggerOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskBaseImageTriggerOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskBaseImageTriggerOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="updateTriggerEndpoint")
    def update_trigger_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTriggerEndpoint"))

    @update_trigger_endpoint.setter
    def update_trigger_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskBaseImageTriggerOutputReference, "update_trigger_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updateTriggerEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="updateTriggerPayloadType")
    def update_trigger_payload_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTriggerPayloadType"))

    @update_trigger_payload_type.setter
    def update_trigger_payload_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskBaseImageTriggerOutputReference, "update_trigger_payload_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updateTriggerPayloadType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerRegistryTaskBaseImageTrigger]:
        return typing.cast(typing.Optional[ContainerRegistryTaskBaseImageTrigger], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerRegistryTaskBaseImageTrigger],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskBaseImageTriggerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "container_registry_id": "containerRegistryId",
        "name": "name",
        "agent_pool_name": "agentPoolName",
        "agent_setting": "agentSetting",
        "base_image_trigger": "baseImageTrigger",
        "docker_step": "dockerStep",
        "enabled": "enabled",
        "encoded_step": "encodedStep",
        "file_step": "fileStep",
        "id": "id",
        "identity": "identity",
        "is_system_task": "isSystemTask",
        "log_template": "logTemplate",
        "platform": "platform",
        "registry_credential": "registryCredential",
        "source_trigger": "sourceTrigger",
        "tags": "tags",
        "timeout_in_seconds": "timeoutInSeconds",
        "timeouts": "timeouts",
        "timer_trigger": "timerTrigger",
    },
)
class ContainerRegistryTaskConfig(cdktf.TerraformMetaArguments):
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
        container_registry_id: builtins.str,
        name: builtins.str,
        agent_pool_name: typing.Optional[builtins.str] = None,
        agent_setting: typing.Optional[typing.Union[ContainerRegistryTaskAgentSetting, typing.Dict[str, typing.Any]]] = None,
        base_image_trigger: typing.Optional[typing.Union[ContainerRegistryTaskBaseImageTrigger, typing.Dict[str, typing.Any]]] = None,
        docker_step: typing.Optional[typing.Union["ContainerRegistryTaskDockerStep", typing.Dict[str, typing.Any]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encoded_step: typing.Optional[typing.Union["ContainerRegistryTaskEncodedStep", typing.Dict[str, typing.Any]]] = None,
        file_step: typing.Optional[typing.Union["ContainerRegistryTaskFileStep", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["ContainerRegistryTaskIdentity", typing.Dict[str, typing.Any]]] = None,
        is_system_task: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_template: typing.Optional[builtins.str] = None,
        platform: typing.Optional[typing.Union["ContainerRegistryTaskPlatform", typing.Dict[str, typing.Any]]] = None,
        registry_credential: typing.Optional[typing.Union["ContainerRegistryTaskRegistryCredential", typing.Dict[str, typing.Any]]] = None,
        source_trigger: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerRegistryTaskSourceTrigger", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout_in_seconds: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["ContainerRegistryTaskTimeouts", typing.Dict[str, typing.Any]]] = None,
        timer_trigger: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerRegistryTaskTimerTrigger", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param container_registry_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#container_registry_id ContainerRegistryTask#container_registry_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#name ContainerRegistryTask#name}.
        :param agent_pool_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#agent_pool_name ContainerRegistryTask#agent_pool_name}.
        :param agent_setting: agent_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#agent_setting ContainerRegistryTask#agent_setting}
        :param base_image_trigger: base_image_trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#base_image_trigger ContainerRegistryTask#base_image_trigger}
        :param docker_step: docker_step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#docker_step ContainerRegistryTask#docker_step}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#enabled ContainerRegistryTask#enabled}.
        :param encoded_step: encoded_step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#encoded_step ContainerRegistryTask#encoded_step}
        :param file_step: file_step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#file_step ContainerRegistryTask#file_step}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#id ContainerRegistryTask#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#identity ContainerRegistryTask#identity}
        :param is_system_task: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#is_system_task ContainerRegistryTask#is_system_task}.
        :param log_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#log_template ContainerRegistryTask#log_template}.
        :param platform: platform block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#platform ContainerRegistryTask#platform}
        :param registry_credential: registry_credential block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#registry_credential ContainerRegistryTask#registry_credential}
        :param source_trigger: source_trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#source_trigger ContainerRegistryTask#source_trigger}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#tags ContainerRegistryTask#tags}.
        :param timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#timeout_in_seconds ContainerRegistryTask#timeout_in_seconds}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#timeouts ContainerRegistryTask#timeouts}
        :param timer_trigger: timer_trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#timer_trigger ContainerRegistryTask#timer_trigger}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(agent_setting, dict):
            agent_setting = ContainerRegistryTaskAgentSetting(**agent_setting)
        if isinstance(base_image_trigger, dict):
            base_image_trigger = ContainerRegistryTaskBaseImageTrigger(**base_image_trigger)
        if isinstance(docker_step, dict):
            docker_step = ContainerRegistryTaskDockerStep(**docker_step)
        if isinstance(encoded_step, dict):
            encoded_step = ContainerRegistryTaskEncodedStep(**encoded_step)
        if isinstance(file_step, dict):
            file_step = ContainerRegistryTaskFileStep(**file_step)
        if isinstance(identity, dict):
            identity = ContainerRegistryTaskIdentity(**identity)
        if isinstance(platform, dict):
            platform = ContainerRegistryTaskPlatform(**platform)
        if isinstance(registry_credential, dict):
            registry_credential = ContainerRegistryTaskRegistryCredential(**registry_credential)
        if isinstance(timeouts, dict):
            timeouts = ContainerRegistryTaskTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument container_registry_id", value=container_registry_id, expected_type=type_hints["container_registry_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument agent_pool_name", value=agent_pool_name, expected_type=type_hints["agent_pool_name"])
            check_type(argname="argument agent_setting", value=agent_setting, expected_type=type_hints["agent_setting"])
            check_type(argname="argument base_image_trigger", value=base_image_trigger, expected_type=type_hints["base_image_trigger"])
            check_type(argname="argument docker_step", value=docker_step, expected_type=type_hints["docker_step"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument encoded_step", value=encoded_step, expected_type=type_hints["encoded_step"])
            check_type(argname="argument file_step", value=file_step, expected_type=type_hints["file_step"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument is_system_task", value=is_system_task, expected_type=type_hints["is_system_task"])
            check_type(argname="argument log_template", value=log_template, expected_type=type_hints["log_template"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument registry_credential", value=registry_credential, expected_type=type_hints["registry_credential"])
            check_type(argname="argument source_trigger", value=source_trigger, expected_type=type_hints["source_trigger"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeout_in_seconds", value=timeout_in_seconds, expected_type=type_hints["timeout_in_seconds"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument timer_trigger", value=timer_trigger, expected_type=type_hints["timer_trigger"])
        self._values: typing.Dict[str, typing.Any] = {
            "container_registry_id": container_registry_id,
            "name": name,
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
        if agent_pool_name is not None:
            self._values["agent_pool_name"] = agent_pool_name
        if agent_setting is not None:
            self._values["agent_setting"] = agent_setting
        if base_image_trigger is not None:
            self._values["base_image_trigger"] = base_image_trigger
        if docker_step is not None:
            self._values["docker_step"] = docker_step
        if enabled is not None:
            self._values["enabled"] = enabled
        if encoded_step is not None:
            self._values["encoded_step"] = encoded_step
        if file_step is not None:
            self._values["file_step"] = file_step
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if is_system_task is not None:
            self._values["is_system_task"] = is_system_task
        if log_template is not None:
            self._values["log_template"] = log_template
        if platform is not None:
            self._values["platform"] = platform
        if registry_credential is not None:
            self._values["registry_credential"] = registry_credential
        if source_trigger is not None:
            self._values["source_trigger"] = source_trigger
        if tags is not None:
            self._values["tags"] = tags
        if timeout_in_seconds is not None:
            self._values["timeout_in_seconds"] = timeout_in_seconds
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if timer_trigger is not None:
            self._values["timer_trigger"] = timer_trigger

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
    def container_registry_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#container_registry_id ContainerRegistryTask#container_registry_id}.'''
        result = self._values.get("container_registry_id")
        assert result is not None, "Required property 'container_registry_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#name ContainerRegistryTask#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_pool_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#agent_pool_name ContainerRegistryTask#agent_pool_name}.'''
        result = self._values.get("agent_pool_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def agent_setting(self) -> typing.Optional[ContainerRegistryTaskAgentSetting]:
        '''agent_setting block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#agent_setting ContainerRegistryTask#agent_setting}
        '''
        result = self._values.get("agent_setting")
        return typing.cast(typing.Optional[ContainerRegistryTaskAgentSetting], result)

    @builtins.property
    def base_image_trigger(
        self,
    ) -> typing.Optional[ContainerRegistryTaskBaseImageTrigger]:
        '''base_image_trigger block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#base_image_trigger ContainerRegistryTask#base_image_trigger}
        '''
        result = self._values.get("base_image_trigger")
        return typing.cast(typing.Optional[ContainerRegistryTaskBaseImageTrigger], result)

    @builtins.property
    def docker_step(self) -> typing.Optional["ContainerRegistryTaskDockerStep"]:
        '''docker_step block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#docker_step ContainerRegistryTask#docker_step}
        '''
        result = self._values.get("docker_step")
        return typing.cast(typing.Optional["ContainerRegistryTaskDockerStep"], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#enabled ContainerRegistryTask#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encoded_step(self) -> typing.Optional["ContainerRegistryTaskEncodedStep"]:
        '''encoded_step block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#encoded_step ContainerRegistryTask#encoded_step}
        '''
        result = self._values.get("encoded_step")
        return typing.cast(typing.Optional["ContainerRegistryTaskEncodedStep"], result)

    @builtins.property
    def file_step(self) -> typing.Optional["ContainerRegistryTaskFileStep"]:
        '''file_step block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#file_step ContainerRegistryTask#file_step}
        '''
        result = self._values.get("file_step")
        return typing.cast(typing.Optional["ContainerRegistryTaskFileStep"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#id ContainerRegistryTask#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["ContainerRegistryTaskIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#identity ContainerRegistryTask#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["ContainerRegistryTaskIdentity"], result)

    @builtins.property
    def is_system_task(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#is_system_task ContainerRegistryTask#is_system_task}.'''
        result = self._values.get("is_system_task")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#log_template ContainerRegistryTask#log_template}.'''
        result = self._values.get("log_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def platform(self) -> typing.Optional["ContainerRegistryTaskPlatform"]:
        '''platform block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#platform ContainerRegistryTask#platform}
        '''
        result = self._values.get("platform")
        return typing.cast(typing.Optional["ContainerRegistryTaskPlatform"], result)

    @builtins.property
    def registry_credential(
        self,
    ) -> typing.Optional["ContainerRegistryTaskRegistryCredential"]:
        '''registry_credential block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#registry_credential ContainerRegistryTask#registry_credential}
        '''
        result = self._values.get("registry_credential")
        return typing.cast(typing.Optional["ContainerRegistryTaskRegistryCredential"], result)

    @builtins.property
    def source_trigger(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerRegistryTaskSourceTrigger"]]]:
        '''source_trigger block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#source_trigger ContainerRegistryTask#source_trigger}
        '''
        result = self._values.get("source_trigger")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerRegistryTaskSourceTrigger"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#tags ContainerRegistryTask#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#timeout_in_seconds ContainerRegistryTask#timeout_in_seconds}.'''
        result = self._values.get("timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ContainerRegistryTaskTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#timeouts ContainerRegistryTask#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ContainerRegistryTaskTimeouts"], result)

    @builtins.property
    def timer_trigger(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerRegistryTaskTimerTrigger"]]]:
        '''timer_trigger block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#timer_trigger ContainerRegistryTask#timer_trigger}
        '''
        result = self._values.get("timer_trigger")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerRegistryTaskTimerTrigger"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTaskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskDockerStep",
    jsii_struct_bases=[],
    name_mapping={
        "context_access_token": "contextAccessToken",
        "context_path": "contextPath",
        "dockerfile_path": "dockerfilePath",
        "arguments": "arguments",
        "cache_enabled": "cacheEnabled",
        "image_names": "imageNames",
        "push_enabled": "pushEnabled",
        "secret_arguments": "secretArguments",
        "target": "target",
    },
)
class ContainerRegistryTaskDockerStep:
    def __init__(
        self,
        *,
        context_access_token: builtins.str,
        context_path: builtins.str,
        dockerfile_path: builtins.str,
        arguments: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        cache_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        image_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        push_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secret_arguments: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param context_access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_access_token ContainerRegistryTask#context_access_token}.
        :param context_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_path ContainerRegistryTask#context_path}.
        :param dockerfile_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#dockerfile_path ContainerRegistryTask#dockerfile_path}.
        :param arguments: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#arguments ContainerRegistryTask#arguments}.
        :param cache_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#cache_enabled ContainerRegistryTask#cache_enabled}.
        :param image_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#image_names ContainerRegistryTask#image_names}.
        :param push_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#push_enabled ContainerRegistryTask#push_enabled}.
        :param secret_arguments: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#secret_arguments ContainerRegistryTask#secret_arguments}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#target ContainerRegistryTask#target}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskDockerStep.__init__)
            check_type(argname="argument context_access_token", value=context_access_token, expected_type=type_hints["context_access_token"])
            check_type(argname="argument context_path", value=context_path, expected_type=type_hints["context_path"])
            check_type(argname="argument dockerfile_path", value=dockerfile_path, expected_type=type_hints["dockerfile_path"])
            check_type(argname="argument arguments", value=arguments, expected_type=type_hints["arguments"])
            check_type(argname="argument cache_enabled", value=cache_enabled, expected_type=type_hints["cache_enabled"])
            check_type(argname="argument image_names", value=image_names, expected_type=type_hints["image_names"])
            check_type(argname="argument push_enabled", value=push_enabled, expected_type=type_hints["push_enabled"])
            check_type(argname="argument secret_arguments", value=secret_arguments, expected_type=type_hints["secret_arguments"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {
            "context_access_token": context_access_token,
            "context_path": context_path,
            "dockerfile_path": dockerfile_path,
        }
        if arguments is not None:
            self._values["arguments"] = arguments
        if cache_enabled is not None:
            self._values["cache_enabled"] = cache_enabled
        if image_names is not None:
            self._values["image_names"] = image_names
        if push_enabled is not None:
            self._values["push_enabled"] = push_enabled
        if secret_arguments is not None:
            self._values["secret_arguments"] = secret_arguments
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def context_access_token(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_access_token ContainerRegistryTask#context_access_token}.'''
        result = self._values.get("context_access_token")
        assert result is not None, "Required property 'context_access_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def context_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_path ContainerRegistryTask#context_path}.'''
        result = self._values.get("context_path")
        assert result is not None, "Required property 'context_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dockerfile_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#dockerfile_path ContainerRegistryTask#dockerfile_path}.'''
        result = self._values.get("dockerfile_path")
        assert result is not None, "Required property 'dockerfile_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def arguments(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#arguments ContainerRegistryTask#arguments}.'''
        result = self._values.get("arguments")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def cache_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#cache_enabled ContainerRegistryTask#cache_enabled}.'''
        result = self._values.get("cache_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def image_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#image_names ContainerRegistryTask#image_names}.'''
        result = self._values.get("image_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def push_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#push_enabled ContainerRegistryTask#push_enabled}.'''
        result = self._values.get("push_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def secret_arguments(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#secret_arguments ContainerRegistryTask#secret_arguments}.'''
        result = self._values.get("secret_arguments")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#target ContainerRegistryTask#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTaskDockerStep(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerRegistryTaskDockerStepOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskDockerStepOutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskDockerStepOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetArguments")
    def reset_arguments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArguments", []))

    @jsii.member(jsii_name="resetCacheEnabled")
    def reset_cache_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheEnabled", []))

    @jsii.member(jsii_name="resetImageNames")
    def reset_image_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageNames", []))

    @jsii.member(jsii_name="resetPushEnabled")
    def reset_push_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPushEnabled", []))

    @jsii.member(jsii_name="resetSecretArguments")
    def reset_secret_arguments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretArguments", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="argumentsInput")
    def arguments_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "argumentsInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheEnabledInput")
    def cache_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cacheEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="contextAccessTokenInput")
    def context_access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contextAccessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="contextPathInput")
    def context_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contextPathInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerfilePathInput")
    def dockerfile_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerfilePathInput"))

    @builtins.property
    @jsii.member(jsii_name="imageNamesInput")
    def image_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "imageNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="pushEnabledInput")
    def push_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "pushEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="secretArgumentsInput")
    def secret_arguments_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "secretArgumentsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="arguments")
    def arguments(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "arguments"))

    @arguments.setter
    def arguments(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskDockerStepOutputReference, "arguments").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arguments", value)

    @builtins.property
    @jsii.member(jsii_name="cacheEnabled")
    def cache_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cacheEnabled"))

    @cache_enabled.setter
    def cache_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskDockerStepOutputReference, "cache_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="contextAccessToken")
    def context_access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contextAccessToken"))

    @context_access_token.setter
    def context_access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskDockerStepOutputReference, "context_access_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contextAccessToken", value)

    @builtins.property
    @jsii.member(jsii_name="contextPath")
    def context_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contextPath"))

    @context_path.setter
    def context_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskDockerStepOutputReference, "context_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contextPath", value)

    @builtins.property
    @jsii.member(jsii_name="dockerfilePath")
    def dockerfile_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerfilePath"))

    @dockerfile_path.setter
    def dockerfile_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskDockerStepOutputReference, "dockerfile_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerfilePath", value)

    @builtins.property
    @jsii.member(jsii_name="imageNames")
    def image_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "imageNames"))

    @image_names.setter
    def image_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskDockerStepOutputReference, "image_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageNames", value)

    @builtins.property
    @jsii.member(jsii_name="pushEnabled")
    def push_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "pushEnabled"))

    @push_enabled.setter
    def push_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskDockerStepOutputReference, "push_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pushEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="secretArguments")
    def secret_arguments(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "secretArguments"))

    @secret_arguments.setter
    def secret_arguments(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskDockerStepOutputReference, "secret_arguments").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretArguments", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskDockerStepOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerRegistryTaskDockerStep]:
        return typing.cast(typing.Optional[ContainerRegistryTaskDockerStep], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerRegistryTaskDockerStep],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskDockerStepOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskEncodedStep",
    jsii_struct_bases=[],
    name_mapping={
        "task_content": "taskContent",
        "context_access_token": "contextAccessToken",
        "context_path": "contextPath",
        "secret_values": "secretValues",
        "value_content": "valueContent",
        "values": "values",
    },
)
class ContainerRegistryTaskEncodedStep:
    def __init__(
        self,
        *,
        task_content: builtins.str,
        context_access_token: typing.Optional[builtins.str] = None,
        context_path: typing.Optional[builtins.str] = None,
        secret_values: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        value_content: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param task_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#task_content ContainerRegistryTask#task_content}.
        :param context_access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_access_token ContainerRegistryTask#context_access_token}.
        :param context_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_path ContainerRegistryTask#context_path}.
        :param secret_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#secret_values ContainerRegistryTask#secret_values}.
        :param value_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#value_content ContainerRegistryTask#value_content}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#values ContainerRegistryTask#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskEncodedStep.__init__)
            check_type(argname="argument task_content", value=task_content, expected_type=type_hints["task_content"])
            check_type(argname="argument context_access_token", value=context_access_token, expected_type=type_hints["context_access_token"])
            check_type(argname="argument context_path", value=context_path, expected_type=type_hints["context_path"])
            check_type(argname="argument secret_values", value=secret_values, expected_type=type_hints["secret_values"])
            check_type(argname="argument value_content", value=value_content, expected_type=type_hints["value_content"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "task_content": task_content,
        }
        if context_access_token is not None:
            self._values["context_access_token"] = context_access_token
        if context_path is not None:
            self._values["context_path"] = context_path
        if secret_values is not None:
            self._values["secret_values"] = secret_values
        if value_content is not None:
            self._values["value_content"] = value_content
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def task_content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#task_content ContainerRegistryTask#task_content}.'''
        result = self._values.get("task_content")
        assert result is not None, "Required property 'task_content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def context_access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_access_token ContainerRegistryTask#context_access_token}.'''
        result = self._values.get("context_access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def context_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_path ContainerRegistryTask#context_path}.'''
        result = self._values.get("context_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#secret_values ContainerRegistryTask#secret_values}.'''
        result = self._values.get("secret_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def value_content(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#value_content ContainerRegistryTask#value_content}.'''
        result = self._values.get("value_content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#values ContainerRegistryTask#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTaskEncodedStep(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerRegistryTaskEncodedStepOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskEncodedStepOutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskEncodedStepOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContextAccessToken")
    def reset_context_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContextAccessToken", []))

    @jsii.member(jsii_name="resetContextPath")
    def reset_context_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContextPath", []))

    @jsii.member(jsii_name="resetSecretValues")
    def reset_secret_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretValues", []))

    @jsii.member(jsii_name="resetValueContent")
    def reset_value_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueContent", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="contextAccessTokenInput")
    def context_access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contextAccessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="contextPathInput")
    def context_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contextPathInput"))

    @builtins.property
    @jsii.member(jsii_name="secretValuesInput")
    def secret_values_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "secretValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="taskContentInput")
    def task_content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskContentInput"))

    @builtins.property
    @jsii.member(jsii_name="valueContentInput")
    def value_content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueContentInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="contextAccessToken")
    def context_access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contextAccessToken"))

    @context_access_token.setter
    def context_access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskEncodedStepOutputReference, "context_access_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contextAccessToken", value)

    @builtins.property
    @jsii.member(jsii_name="contextPath")
    def context_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contextPath"))

    @context_path.setter
    def context_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskEncodedStepOutputReference, "context_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contextPath", value)

    @builtins.property
    @jsii.member(jsii_name="secretValues")
    def secret_values(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "secretValues"))

    @secret_values.setter
    def secret_values(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskEncodedStepOutputReference, "secret_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretValues", value)

    @builtins.property
    @jsii.member(jsii_name="taskContent")
    def task_content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskContent"))

    @task_content.setter
    def task_content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskEncodedStepOutputReference, "task_content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskContent", value)

    @builtins.property
    @jsii.member(jsii_name="valueContent")
    def value_content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueContent"))

    @value_content.setter
    def value_content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskEncodedStepOutputReference, "value_content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueContent", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskEncodedStepOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerRegistryTaskEncodedStep]:
        return typing.cast(typing.Optional[ContainerRegistryTaskEncodedStep], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerRegistryTaskEncodedStep],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskEncodedStepOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskFileStep",
    jsii_struct_bases=[],
    name_mapping={
        "task_file_path": "taskFilePath",
        "context_access_token": "contextAccessToken",
        "context_path": "contextPath",
        "secret_values": "secretValues",
        "value_file_path": "valueFilePath",
        "values": "values",
    },
)
class ContainerRegistryTaskFileStep:
    def __init__(
        self,
        *,
        task_file_path: builtins.str,
        context_access_token: typing.Optional[builtins.str] = None,
        context_path: typing.Optional[builtins.str] = None,
        secret_values: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        value_file_path: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param task_file_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#task_file_path ContainerRegistryTask#task_file_path}.
        :param context_access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_access_token ContainerRegistryTask#context_access_token}.
        :param context_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_path ContainerRegistryTask#context_path}.
        :param secret_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#secret_values ContainerRegistryTask#secret_values}.
        :param value_file_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#value_file_path ContainerRegistryTask#value_file_path}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#values ContainerRegistryTask#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskFileStep.__init__)
            check_type(argname="argument task_file_path", value=task_file_path, expected_type=type_hints["task_file_path"])
            check_type(argname="argument context_access_token", value=context_access_token, expected_type=type_hints["context_access_token"])
            check_type(argname="argument context_path", value=context_path, expected_type=type_hints["context_path"])
            check_type(argname="argument secret_values", value=secret_values, expected_type=type_hints["secret_values"])
            check_type(argname="argument value_file_path", value=value_file_path, expected_type=type_hints["value_file_path"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "task_file_path": task_file_path,
        }
        if context_access_token is not None:
            self._values["context_access_token"] = context_access_token
        if context_path is not None:
            self._values["context_path"] = context_path
        if secret_values is not None:
            self._values["secret_values"] = secret_values
        if value_file_path is not None:
            self._values["value_file_path"] = value_file_path
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def task_file_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#task_file_path ContainerRegistryTask#task_file_path}.'''
        result = self._values.get("task_file_path")
        assert result is not None, "Required property 'task_file_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def context_access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_access_token ContainerRegistryTask#context_access_token}.'''
        result = self._values.get("context_access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def context_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#context_path ContainerRegistryTask#context_path}.'''
        result = self._values.get("context_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#secret_values ContainerRegistryTask#secret_values}.'''
        result = self._values.get("secret_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def value_file_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#value_file_path ContainerRegistryTask#value_file_path}.'''
        result = self._values.get("value_file_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#values ContainerRegistryTask#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTaskFileStep(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerRegistryTaskFileStepOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskFileStepOutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskFileStepOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContextAccessToken")
    def reset_context_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContextAccessToken", []))

    @jsii.member(jsii_name="resetContextPath")
    def reset_context_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContextPath", []))

    @jsii.member(jsii_name="resetSecretValues")
    def reset_secret_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretValues", []))

    @jsii.member(jsii_name="resetValueFilePath")
    def reset_value_file_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueFilePath", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="contextAccessTokenInput")
    def context_access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contextAccessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="contextPathInput")
    def context_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contextPathInput"))

    @builtins.property
    @jsii.member(jsii_name="secretValuesInput")
    def secret_values_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "secretValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="taskFilePathInput")
    def task_file_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskFilePathInput"))

    @builtins.property
    @jsii.member(jsii_name="valueFilePathInput")
    def value_file_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueFilePathInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="contextAccessToken")
    def context_access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contextAccessToken"))

    @context_access_token.setter
    def context_access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskFileStepOutputReference, "context_access_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contextAccessToken", value)

    @builtins.property
    @jsii.member(jsii_name="contextPath")
    def context_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contextPath"))

    @context_path.setter
    def context_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskFileStepOutputReference, "context_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contextPath", value)

    @builtins.property
    @jsii.member(jsii_name="secretValues")
    def secret_values(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "secretValues"))

    @secret_values.setter
    def secret_values(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskFileStepOutputReference, "secret_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretValues", value)

    @builtins.property
    @jsii.member(jsii_name="taskFilePath")
    def task_file_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskFilePath"))

    @task_file_path.setter
    def task_file_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskFileStepOutputReference, "task_file_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskFilePath", value)

    @builtins.property
    @jsii.member(jsii_name="valueFilePath")
    def value_file_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueFilePath"))

    @value_file_path.setter
    def value_file_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskFileStepOutputReference, "value_file_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueFilePath", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskFileStepOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerRegistryTaskFileStep]:
        return typing.cast(typing.Optional[ContainerRegistryTaskFileStep], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerRegistryTaskFileStep],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskFileStepOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class ContainerRegistryTaskIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#type ContainerRegistryTask#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#identity_ids ContainerRegistryTask#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#type ContainerRegistryTask#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#identity_ids ContainerRegistryTask#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTaskIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerRegistryTaskIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskIdentityOutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdentityIds")
    def reset_identity_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityIds", []))

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="identityIdsInput")
    def identity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIds")
    def identity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityIds"))

    @identity_ids.setter
    def identity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerRegistryTaskIdentity]:
        return typing.cast(typing.Optional[ContainerRegistryTaskIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerRegistryTaskIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskPlatform",
    jsii_struct_bases=[],
    name_mapping={"os": "os", "architecture": "architecture", "variant": "variant"},
)
class ContainerRegistryTaskPlatform:
    def __init__(
        self,
        *,
        os: builtins.str,
        architecture: typing.Optional[builtins.str] = None,
        variant: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param os: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#os ContainerRegistryTask#os}.
        :param architecture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#architecture ContainerRegistryTask#architecture}.
        :param variant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#variant ContainerRegistryTask#variant}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskPlatform.__init__)
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument variant", value=variant, expected_type=type_hints["variant"])
        self._values: typing.Dict[str, typing.Any] = {
            "os": os,
        }
        if architecture is not None:
            self._values["architecture"] = architecture
        if variant is not None:
            self._values["variant"] = variant

    @builtins.property
    def os(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#os ContainerRegistryTask#os}.'''
        result = self._values.get("os")
        assert result is not None, "Required property 'os' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def architecture(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#architecture ContainerRegistryTask#architecture}.'''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def variant(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#variant ContainerRegistryTask#variant}.'''
        result = self._values.get("variant")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTaskPlatform(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerRegistryTaskPlatformOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskPlatformOutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskPlatformOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetArchitecture")
    def reset_architecture(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchitecture", []))

    @jsii.member(jsii_name="resetVariant")
    def reset_variant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVariant", []))

    @builtins.property
    @jsii.member(jsii_name="architectureInput")
    def architecture_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "architectureInput"))

    @builtins.property
    @jsii.member(jsii_name="osInput")
    def os_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osInput"))

    @builtins.property
    @jsii.member(jsii_name="variantInput")
    def variant_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "variantInput"))

    @builtins.property
    @jsii.member(jsii_name="architecture")
    def architecture(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "architecture"))

    @architecture.setter
    def architecture(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskPlatformOutputReference, "architecture").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "architecture", value)

    @builtins.property
    @jsii.member(jsii_name="os")
    def os(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "os"))

    @os.setter
    def os(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskPlatformOutputReference, "os").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "os", value)

    @builtins.property
    @jsii.member(jsii_name="variant")
    def variant(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "variant"))

    @variant.setter
    def variant(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskPlatformOutputReference, "variant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variant", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerRegistryTaskPlatform]:
        return typing.cast(typing.Optional[ContainerRegistryTaskPlatform], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerRegistryTaskPlatform],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskPlatformOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskRegistryCredential",
    jsii_struct_bases=[],
    name_mapping={"custom": "custom", "source": "source"},
)
class ContainerRegistryTaskRegistryCredential:
    def __init__(
        self,
        *,
        custom: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerRegistryTaskRegistryCredentialCustom", typing.Dict[str, typing.Any]]]]] = None,
        source: typing.Optional[typing.Union["ContainerRegistryTaskRegistryCredentialSource", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom: custom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#custom ContainerRegistryTask#custom}
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#source ContainerRegistryTask#source}
        '''
        if isinstance(source, dict):
            source = ContainerRegistryTaskRegistryCredentialSource(**source)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskRegistryCredential.__init__)
            check_type(argname="argument custom", value=custom, expected_type=type_hints["custom"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[str, typing.Any] = {}
        if custom is not None:
            self._values["custom"] = custom
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def custom(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerRegistryTaskRegistryCredentialCustom"]]]:
        '''custom block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#custom ContainerRegistryTask#custom}
        '''
        result = self._values.get("custom")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerRegistryTaskRegistryCredentialCustom"]]], result)

    @builtins.property
    def source(
        self,
    ) -> typing.Optional["ContainerRegistryTaskRegistryCredentialSource"]:
        '''source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#source ContainerRegistryTask#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional["ContainerRegistryTaskRegistryCredentialSource"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTaskRegistryCredential(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskRegistryCredentialCustom",
    jsii_struct_bases=[],
    name_mapping={
        "login_server": "loginServer",
        "identity": "identity",
        "password": "password",
        "username": "username",
    },
)
class ContainerRegistryTaskRegistryCredentialCustom:
    def __init__(
        self,
        *,
        login_server: builtins.str,
        identity: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param login_server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#login_server ContainerRegistryTask#login_server}.
        :param identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#identity ContainerRegistryTask#identity}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#password ContainerRegistryTask#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#username ContainerRegistryTask#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskRegistryCredentialCustom.__init__)
            check_type(argname="argument login_server", value=login_server, expected_type=type_hints["login_server"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "login_server": login_server,
        }
        if identity is not None:
            self._values["identity"] = identity
        if password is not None:
            self._values["password"] = password
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def login_server(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#login_server ContainerRegistryTask#login_server}.'''
        result = self._values.get("login_server")
        assert result is not None, "Required property 'login_server' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#identity ContainerRegistryTask#identity}.'''
        result = self._values.get("identity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#password ContainerRegistryTask#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#username ContainerRegistryTask#username}.'''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTaskRegistryCredentialCustom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerRegistryTaskRegistryCredentialCustomList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskRegistryCredentialCustomList",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskRegistryCredentialCustomList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerRegistryTaskRegistryCredentialCustomOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskRegistryCredentialCustomList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerRegistryTaskRegistryCredentialCustomOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskRegistryCredentialCustomList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskRegistryCredentialCustomList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskRegistryCredentialCustomList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerRegistryTaskRegistryCredentialCustom]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerRegistryTaskRegistryCredentialCustom]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerRegistryTaskRegistryCredentialCustom]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskRegistryCredentialCustomList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerRegistryTaskRegistryCredentialCustomOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskRegistryCredentialCustomOutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskRegistryCredentialCustomOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="loginServerInput")
    def login_server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loginServerInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identity"))

    @identity.setter
    def identity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskRegistryCredentialCustomOutputReference, "identity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identity", value)

    @builtins.property
    @jsii.member(jsii_name="loginServer")
    def login_server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loginServer"))

    @login_server.setter
    def login_server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskRegistryCredentialCustomOutputReference, "login_server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginServer", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskRegistryCredentialCustomOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskRegistryCredentialCustomOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerRegistryTaskRegistryCredentialCustom, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerRegistryTaskRegistryCredentialCustom, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerRegistryTaskRegistryCredentialCustom, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskRegistryCredentialCustomOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerRegistryTaskRegistryCredentialOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskRegistryCredentialOutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskRegistryCredentialOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustom")
    def put_custom(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ContainerRegistryTaskRegistryCredentialCustom, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskRegistryCredentialOutputReference.put_custom)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustom", [value]))

    @jsii.member(jsii_name="putSource")
    def put_source(self, *, login_mode: builtins.str) -> None:
        '''
        :param login_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#login_mode ContainerRegistryTask#login_mode}.
        '''
        value = ContainerRegistryTaskRegistryCredentialSource(login_mode=login_mode)

        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="resetCustom")
    def reset_custom(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustom", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @builtins.property
    @jsii.member(jsii_name="custom")
    def custom(self) -> ContainerRegistryTaskRegistryCredentialCustomList:
        return typing.cast(ContainerRegistryTaskRegistryCredentialCustomList, jsii.get(self, "custom"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "ContainerRegistryTaskRegistryCredentialSourceOutputReference":
        return typing.cast("ContainerRegistryTaskRegistryCredentialSourceOutputReference", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="customInput")
    def custom_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerRegistryTaskRegistryCredentialCustom]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerRegistryTaskRegistryCredentialCustom]]], jsii.get(self, "customInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(
        self,
    ) -> typing.Optional["ContainerRegistryTaskRegistryCredentialSource"]:
        return typing.cast(typing.Optional["ContainerRegistryTaskRegistryCredentialSource"], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerRegistryTaskRegistryCredential]:
        return typing.cast(typing.Optional[ContainerRegistryTaskRegistryCredential], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerRegistryTaskRegistryCredential],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskRegistryCredentialOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskRegistryCredentialSource",
    jsii_struct_bases=[],
    name_mapping={"login_mode": "loginMode"},
)
class ContainerRegistryTaskRegistryCredentialSource:
    def __init__(self, *, login_mode: builtins.str) -> None:
        '''
        :param login_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#login_mode ContainerRegistryTask#login_mode}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskRegistryCredentialSource.__init__)
            check_type(argname="argument login_mode", value=login_mode, expected_type=type_hints["login_mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "login_mode": login_mode,
        }

    @builtins.property
    def login_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#login_mode ContainerRegistryTask#login_mode}.'''
        result = self._values.get("login_mode")
        assert result is not None, "Required property 'login_mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTaskRegistryCredentialSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerRegistryTaskRegistryCredentialSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskRegistryCredentialSourceOutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskRegistryCredentialSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="loginModeInput")
    def login_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loginModeInput"))

    @builtins.property
    @jsii.member(jsii_name="loginMode")
    def login_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loginMode"))

    @login_mode.setter
    def login_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskRegistryCredentialSourceOutputReference, "login_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerRegistryTaskRegistryCredentialSource]:
        return typing.cast(typing.Optional[ContainerRegistryTaskRegistryCredentialSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerRegistryTaskRegistryCredentialSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskRegistryCredentialSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskSourceTrigger",
    jsii_struct_bases=[],
    name_mapping={
        "events": "events",
        "name": "name",
        "repository_url": "repositoryUrl",
        "source_type": "sourceType",
        "authentication": "authentication",
        "branch": "branch",
        "enabled": "enabled",
    },
)
class ContainerRegistryTaskSourceTrigger:
    def __init__(
        self,
        *,
        events: typing.Sequence[builtins.str],
        name: builtins.str,
        repository_url: builtins.str,
        source_type: builtins.str,
        authentication: typing.Optional[typing.Union["ContainerRegistryTaskSourceTriggerAuthentication", typing.Dict[str, typing.Any]]] = None,
        branch: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#events ContainerRegistryTask#events}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#name ContainerRegistryTask#name}.
        :param repository_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#repository_url ContainerRegistryTask#repository_url}.
        :param source_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#source_type ContainerRegistryTask#source_type}.
        :param authentication: authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#authentication ContainerRegistryTask#authentication}
        :param branch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#branch ContainerRegistryTask#branch}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#enabled ContainerRegistryTask#enabled}.
        '''
        if isinstance(authentication, dict):
            authentication = ContainerRegistryTaskSourceTriggerAuthentication(**authentication)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskSourceTrigger.__init__)
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument repository_url", value=repository_url, expected_type=type_hints["repository_url"])
            check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
            check_type(argname="argument authentication", value=authentication, expected_type=type_hints["authentication"])
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "events": events,
            "name": name,
            "repository_url": repository_url,
            "source_type": source_type,
        }
        if authentication is not None:
            self._values["authentication"] = authentication
        if branch is not None:
            self._values["branch"] = branch
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def events(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#events ContainerRegistryTask#events}.'''
        result = self._values.get("events")
        assert result is not None, "Required property 'events' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#name ContainerRegistryTask#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#repository_url ContainerRegistryTask#repository_url}.'''
        result = self._values.get("repository_url")
        assert result is not None, "Required property 'repository_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#source_type ContainerRegistryTask#source_type}.'''
        result = self._values.get("source_type")
        assert result is not None, "Required property 'source_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authentication(
        self,
    ) -> typing.Optional["ContainerRegistryTaskSourceTriggerAuthentication"]:
        '''authentication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#authentication ContainerRegistryTask#authentication}
        '''
        result = self._values.get("authentication")
        return typing.cast(typing.Optional["ContainerRegistryTaskSourceTriggerAuthentication"], result)

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#branch ContainerRegistryTask#branch}.'''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#enabled ContainerRegistryTask#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTaskSourceTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskSourceTriggerAuthentication",
    jsii_struct_bases=[],
    name_mapping={
        "token": "token",
        "token_type": "tokenType",
        "expire_in_seconds": "expireInSeconds",
        "refresh_token": "refreshToken",
        "scope": "scope",
    },
)
class ContainerRegistryTaskSourceTriggerAuthentication:
    def __init__(
        self,
        *,
        token: builtins.str,
        token_type: builtins.str,
        expire_in_seconds: typing.Optional[jsii.Number] = None,
        refresh_token: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#token ContainerRegistryTask#token}.
        :param token_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#token_type ContainerRegistryTask#token_type}.
        :param expire_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#expire_in_seconds ContainerRegistryTask#expire_in_seconds}.
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#refresh_token ContainerRegistryTask#refresh_token}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#scope ContainerRegistryTask#scope}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskSourceTriggerAuthentication.__init__)
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument token_type", value=token_type, expected_type=type_hints["token_type"])
            check_type(argname="argument expire_in_seconds", value=expire_in_seconds, expected_type=type_hints["expire_in_seconds"])
            check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[str, typing.Any] = {
            "token": token,
            "token_type": token_type,
        }
        if expire_in_seconds is not None:
            self._values["expire_in_seconds"] = expire_in_seconds
        if refresh_token is not None:
            self._values["refresh_token"] = refresh_token
        if scope is not None:
            self._values["scope"] = scope

    @builtins.property
    def token(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#token ContainerRegistryTask#token}.'''
        result = self._values.get("token")
        assert result is not None, "Required property 'token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#token_type ContainerRegistryTask#token_type}.'''
        result = self._values.get("token_type")
        assert result is not None, "Required property 'token_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expire_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#expire_in_seconds ContainerRegistryTask#expire_in_seconds}.'''
        result = self._values.get("expire_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def refresh_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#refresh_token ContainerRegistryTask#refresh_token}.'''
        result = self._values.get("refresh_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#scope ContainerRegistryTask#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTaskSourceTriggerAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerRegistryTaskSourceTriggerAuthenticationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskSourceTriggerAuthenticationOutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskSourceTriggerAuthenticationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExpireInSeconds")
    def reset_expire_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpireInSeconds", []))

    @jsii.member(jsii_name="resetRefreshToken")
    def reset_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshToken", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @builtins.property
    @jsii.member(jsii_name="expireInSecondsInput")
    def expire_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expireInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshTokenInput")
    def refresh_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refreshTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenTypeInput")
    def token_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="expireInSeconds")
    def expire_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "expireInSeconds"))

    @expire_in_seconds.setter
    def expire_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerAuthenticationOutputReference, "expire_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expireInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="refreshToken")
    def refresh_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "refreshToken"))

    @refresh_token.setter
    def refresh_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerAuthenticationOutputReference, "refresh_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshToken", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerAuthenticationOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @token.setter
    def token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerAuthenticationOutputReference, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="tokenType")
    def token_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenType"))

    @token_type.setter
    def token_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerAuthenticationOutputReference, "token_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerRegistryTaskSourceTriggerAuthentication]:
        return typing.cast(typing.Optional[ContainerRegistryTaskSourceTriggerAuthentication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerRegistryTaskSourceTriggerAuthentication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerAuthenticationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerRegistryTaskSourceTriggerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskSourceTriggerList",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskSourceTriggerList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerRegistryTaskSourceTriggerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskSourceTriggerList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerRegistryTaskSourceTriggerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerRegistryTaskSourceTrigger]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerRegistryTaskSourceTrigger]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerRegistryTaskSourceTrigger]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerRegistryTaskSourceTriggerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskSourceTriggerOutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskSourceTriggerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAuthentication")
    def put_authentication(
        self,
        *,
        token: builtins.str,
        token_type: builtins.str,
        expire_in_seconds: typing.Optional[jsii.Number] = None,
        refresh_token: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#token ContainerRegistryTask#token}.
        :param token_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#token_type ContainerRegistryTask#token_type}.
        :param expire_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#expire_in_seconds ContainerRegistryTask#expire_in_seconds}.
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#refresh_token ContainerRegistryTask#refresh_token}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#scope ContainerRegistryTask#scope}.
        '''
        value = ContainerRegistryTaskSourceTriggerAuthentication(
            token=token,
            token_type=token_type,
            expire_in_seconds=expire_in_seconds,
            refresh_token=refresh_token,
            scope=scope,
        )

        return typing.cast(None, jsii.invoke(self, "putAuthentication", [value]))

    @jsii.member(jsii_name="resetAuthentication")
    def reset_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthentication", []))

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="authentication")
    def authentication(
        self,
    ) -> ContainerRegistryTaskSourceTriggerAuthenticationOutputReference:
        return typing.cast(ContainerRegistryTaskSourceTriggerAuthenticationOutputReference, jsii.get(self, "authentication"))

    @builtins.property
    @jsii.member(jsii_name="authenticationInput")
    def authentication_input(
        self,
    ) -> typing.Optional[ContainerRegistryTaskSourceTriggerAuthentication]:
        return typing.cast(typing.Optional[ContainerRegistryTaskSourceTriggerAuthentication], jsii.get(self, "authenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="eventsInput")
    def events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryUrlInput")
    def repository_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceTypeInput")
    def source_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="events")
    def events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "events"))

    @events.setter
    def events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerOutputReference, "events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "events", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryUrl")
    def repository_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repositoryUrl"))

    @repository_url.setter
    def repository_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerOutputReference, "repository_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryUrl", value)

    @builtins.property
    @jsii.member(jsii_name="sourceType")
    def source_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceType"))

    @source_type.setter
    def source_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerOutputReference, "source_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerRegistryTaskSourceTrigger, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerRegistryTaskSourceTrigger, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerRegistryTaskSourceTrigger, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskSourceTriggerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ContainerRegistryTaskTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#create ContainerRegistryTask#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#delete ContainerRegistryTask#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#read ContainerRegistryTask#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#update ContainerRegistryTask#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#create ContainerRegistryTask#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#delete ContainerRegistryTask#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#read ContainerRegistryTask#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#update ContainerRegistryTask#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTaskTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerRegistryTaskTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

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
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

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
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerRegistryTaskTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerRegistryTaskTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerRegistryTaskTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskTimerTrigger",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "schedule": "schedule", "enabled": "enabled"},
)
class ContainerRegistryTaskTimerTrigger:
    def __init__(
        self,
        *,
        name: builtins.str,
        schedule: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#name ContainerRegistryTask#name}.
        :param schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#schedule ContainerRegistryTask#schedule}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#enabled ContainerRegistryTask#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskTimerTrigger.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "schedule": schedule,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#name ContainerRegistryTask#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#schedule ContainerRegistryTask#schedule}.'''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_task#enabled ContainerRegistryTask#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTaskTimerTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerRegistryTaskTimerTriggerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskTimerTriggerList",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskTimerTriggerList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerRegistryTaskTimerTriggerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTaskTimerTriggerList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerRegistryTaskTimerTriggerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskTimerTriggerList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskTimerTriggerList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskTimerTriggerList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerRegistryTaskTimerTrigger]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerRegistryTaskTimerTrigger]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerRegistryTaskTimerTrigger]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskTimerTriggerList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerRegistryTaskTimerTriggerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTask.ContainerRegistryTaskTimerTriggerOutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTaskTimerTriggerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskTimerTriggerOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskTimerTriggerOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskTimerTriggerOutputReference, "schedule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerRegistryTaskTimerTrigger, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerRegistryTaskTimerTrigger, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerRegistryTaskTimerTrigger, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTaskTimerTriggerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ContainerRegistryTask",
    "ContainerRegistryTaskAgentSetting",
    "ContainerRegistryTaskAgentSettingOutputReference",
    "ContainerRegistryTaskBaseImageTrigger",
    "ContainerRegistryTaskBaseImageTriggerOutputReference",
    "ContainerRegistryTaskConfig",
    "ContainerRegistryTaskDockerStep",
    "ContainerRegistryTaskDockerStepOutputReference",
    "ContainerRegistryTaskEncodedStep",
    "ContainerRegistryTaskEncodedStepOutputReference",
    "ContainerRegistryTaskFileStep",
    "ContainerRegistryTaskFileStepOutputReference",
    "ContainerRegistryTaskIdentity",
    "ContainerRegistryTaskIdentityOutputReference",
    "ContainerRegistryTaskPlatform",
    "ContainerRegistryTaskPlatformOutputReference",
    "ContainerRegistryTaskRegistryCredential",
    "ContainerRegistryTaskRegistryCredentialCustom",
    "ContainerRegistryTaskRegistryCredentialCustomList",
    "ContainerRegistryTaskRegistryCredentialCustomOutputReference",
    "ContainerRegistryTaskRegistryCredentialOutputReference",
    "ContainerRegistryTaskRegistryCredentialSource",
    "ContainerRegistryTaskRegistryCredentialSourceOutputReference",
    "ContainerRegistryTaskSourceTrigger",
    "ContainerRegistryTaskSourceTriggerAuthentication",
    "ContainerRegistryTaskSourceTriggerAuthenticationOutputReference",
    "ContainerRegistryTaskSourceTriggerList",
    "ContainerRegistryTaskSourceTriggerOutputReference",
    "ContainerRegistryTaskTimeouts",
    "ContainerRegistryTaskTimeoutsOutputReference",
    "ContainerRegistryTaskTimerTrigger",
    "ContainerRegistryTaskTimerTriggerList",
    "ContainerRegistryTaskTimerTriggerOutputReference",
]

publication.publish()
