'''
# `azurerm_spring_cloud_container_deployment`

Refer to the Terraform Registory for docs: [`azurerm_spring_cloud_container_deployment`](https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment).
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


class SpringCloudContainerDeployment(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudContainerDeployment.SpringCloudContainerDeployment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment azurerm_spring_cloud_container_deployment}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        image: builtins.str,
        name: builtins.str,
        server: builtins.str,
        spring_cloud_app_id: builtins.str,
        addon_json: typing.Optional[builtins.str] = None,
        arguments: typing.Optional[typing.Sequence[builtins.str]] = None,
        commands: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        language_framework: typing.Optional[builtins.str] = None,
        quota: typing.Optional[typing.Union["SpringCloudContainerDeploymentQuota", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["SpringCloudContainerDeploymentTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment azurerm_spring_cloud_container_deployment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#image SpringCloudContainerDeployment#image}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#name SpringCloudContainerDeployment#name}.
        :param server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#server SpringCloudContainerDeployment#server}.
        :param spring_cloud_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#spring_cloud_app_id SpringCloudContainerDeployment#spring_cloud_app_id}.
        :param addon_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#addon_json SpringCloudContainerDeployment#addon_json}.
        :param arguments: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#arguments SpringCloudContainerDeployment#arguments}.
        :param commands: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#commands SpringCloudContainerDeployment#commands}.
        :param environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#environment_variables SpringCloudContainerDeployment#environment_variables}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#id SpringCloudContainerDeployment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#instance_count SpringCloudContainerDeployment#instance_count}.
        :param language_framework: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#language_framework SpringCloudContainerDeployment#language_framework}.
        :param quota: quota block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#quota SpringCloudContainerDeployment#quota}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#timeouts SpringCloudContainerDeployment#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudContainerDeployment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SpringCloudContainerDeploymentConfig(
            image=image,
            name=name,
            server=server,
            spring_cloud_app_id=spring_cloud_app_id,
            addon_json=addon_json,
            arguments=arguments,
            commands=commands,
            environment_variables=environment_variables,
            id=id,
            instance_count=instance_count,
            language_framework=language_framework,
            quota=quota,
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

    @jsii.member(jsii_name="putQuota")
    def put_quota(
        self,
        *,
        cpu: typing.Optional[builtins.str] = None,
        memory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#cpu SpringCloudContainerDeployment#cpu}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#memory SpringCloudContainerDeployment#memory}.
        '''
        value = SpringCloudContainerDeploymentQuota(cpu=cpu, memory=memory)

        return typing.cast(None, jsii.invoke(self, "putQuota", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#create SpringCloudContainerDeployment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#delete SpringCloudContainerDeployment#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#read SpringCloudContainerDeployment#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#update SpringCloudContainerDeployment#update}.
        '''
        value = SpringCloudContainerDeploymentTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAddonJson")
    def reset_addon_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddonJson", []))

    @jsii.member(jsii_name="resetArguments")
    def reset_arguments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArguments", []))

    @jsii.member(jsii_name="resetCommands")
    def reset_commands(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommands", []))

    @jsii.member(jsii_name="resetEnvironmentVariables")
    def reset_environment_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentVariables", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstanceCount")
    def reset_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceCount", []))

    @jsii.member(jsii_name="resetLanguageFramework")
    def reset_language_framework(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLanguageFramework", []))

    @jsii.member(jsii_name="resetQuota")
    def reset_quota(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuota", []))

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
    @jsii.member(jsii_name="quota")
    def quota(self) -> "SpringCloudContainerDeploymentQuotaOutputReference":
        return typing.cast("SpringCloudContainerDeploymentQuotaOutputReference", jsii.get(self, "quota"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SpringCloudContainerDeploymentTimeoutsOutputReference":
        return typing.cast("SpringCloudContainerDeploymentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="addonJsonInput")
    def addon_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addonJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="argumentsInput")
    def arguments_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argumentsInput"))

    @builtins.property
    @jsii.member(jsii_name="commandsInput")
    def commands_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "commandsInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentVariablesInput")
    def environment_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "environmentVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceCountInput")
    def instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="languageFrameworkInput")
    def language_framework_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "languageFrameworkInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="quotaInput")
    def quota_input(self) -> typing.Optional["SpringCloudContainerDeploymentQuota"]:
        return typing.cast(typing.Optional["SpringCloudContainerDeploymentQuota"], jsii.get(self, "quotaInput"))

    @builtins.property
    @jsii.member(jsii_name="serverInput")
    def server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverInput"))

    @builtins.property
    @jsii.member(jsii_name="springCloudAppIdInput")
    def spring_cloud_app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "springCloudAppIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SpringCloudContainerDeploymentTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SpringCloudContainerDeploymentTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="addonJson")
    def addon_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addonJson"))

    @addon_json.setter
    def addon_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeployment, "addon_json").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addonJson", value)

    @builtins.property
    @jsii.member(jsii_name="arguments")
    def arguments(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "arguments"))

    @arguments.setter
    def arguments(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeployment, "arguments").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arguments", value)

    @builtins.property
    @jsii.member(jsii_name="commands")
    def commands(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "commands"))

    @commands.setter
    def commands(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeployment, "commands").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commands", value)

    @builtins.property
    @jsii.member(jsii_name="environmentVariables")
    def environment_variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "environmentVariables"))

    @environment_variables.setter
    def environment_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeployment, "environment_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeployment, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeployment, "image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "image", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeployment, "instance_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="languageFramework")
    def language_framework(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "languageFramework"))

    @language_framework.setter
    def language_framework(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeployment, "language_framework").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageFramework", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeployment, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "server"))

    @server.setter
    def server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeployment, "server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "server", value)

    @builtins.property
    @jsii.member(jsii_name="springCloudAppId")
    def spring_cloud_app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "springCloudAppId"))

    @spring_cloud_app_id.setter
    def spring_cloud_app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeployment, "spring_cloud_app_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "springCloudAppId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudContainerDeployment.SpringCloudContainerDeploymentConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "image": "image",
        "name": "name",
        "server": "server",
        "spring_cloud_app_id": "springCloudAppId",
        "addon_json": "addonJson",
        "arguments": "arguments",
        "commands": "commands",
        "environment_variables": "environmentVariables",
        "id": "id",
        "instance_count": "instanceCount",
        "language_framework": "languageFramework",
        "quota": "quota",
        "timeouts": "timeouts",
    },
)
class SpringCloudContainerDeploymentConfig(cdktf.TerraformMetaArguments):
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
        image: builtins.str,
        name: builtins.str,
        server: builtins.str,
        spring_cloud_app_id: builtins.str,
        addon_json: typing.Optional[builtins.str] = None,
        arguments: typing.Optional[typing.Sequence[builtins.str]] = None,
        commands: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        language_framework: typing.Optional[builtins.str] = None,
        quota: typing.Optional[typing.Union["SpringCloudContainerDeploymentQuota", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["SpringCloudContainerDeploymentTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#image SpringCloudContainerDeployment#image}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#name SpringCloudContainerDeployment#name}.
        :param server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#server SpringCloudContainerDeployment#server}.
        :param spring_cloud_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#spring_cloud_app_id SpringCloudContainerDeployment#spring_cloud_app_id}.
        :param addon_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#addon_json SpringCloudContainerDeployment#addon_json}.
        :param arguments: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#arguments SpringCloudContainerDeployment#arguments}.
        :param commands: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#commands SpringCloudContainerDeployment#commands}.
        :param environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#environment_variables SpringCloudContainerDeployment#environment_variables}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#id SpringCloudContainerDeployment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#instance_count SpringCloudContainerDeployment#instance_count}.
        :param language_framework: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#language_framework SpringCloudContainerDeployment#language_framework}.
        :param quota: quota block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#quota SpringCloudContainerDeployment#quota}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#timeouts SpringCloudContainerDeployment#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(quota, dict):
            quota = SpringCloudContainerDeploymentQuota(**quota)
        if isinstance(timeouts, dict):
            timeouts = SpringCloudContainerDeploymentTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudContainerDeploymentConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
            check_type(argname="argument spring_cloud_app_id", value=spring_cloud_app_id, expected_type=type_hints["spring_cloud_app_id"])
            check_type(argname="argument addon_json", value=addon_json, expected_type=type_hints["addon_json"])
            check_type(argname="argument arguments", value=arguments, expected_type=type_hints["arguments"])
            check_type(argname="argument commands", value=commands, expected_type=type_hints["commands"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
            check_type(argname="argument language_framework", value=language_framework, expected_type=type_hints["language_framework"])
            check_type(argname="argument quota", value=quota, expected_type=type_hints["quota"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "image": image,
            "name": name,
            "server": server,
            "spring_cloud_app_id": spring_cloud_app_id,
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
        if addon_json is not None:
            self._values["addon_json"] = addon_json
        if arguments is not None:
            self._values["arguments"] = arguments
        if commands is not None:
            self._values["commands"] = commands
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if id is not None:
            self._values["id"] = id
        if instance_count is not None:
            self._values["instance_count"] = instance_count
        if language_framework is not None:
            self._values["language_framework"] = language_framework
        if quota is not None:
            self._values["quota"] = quota
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
    def image(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#image SpringCloudContainerDeployment#image}.'''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#name SpringCloudContainerDeployment#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#server SpringCloudContainerDeployment#server}.'''
        result = self._values.get("server")
        assert result is not None, "Required property 'server' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spring_cloud_app_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#spring_cloud_app_id SpringCloudContainerDeployment#spring_cloud_app_id}.'''
        result = self._values.get("spring_cloud_app_id")
        assert result is not None, "Required property 'spring_cloud_app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def addon_json(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#addon_json SpringCloudContainerDeployment#addon_json}.'''
        result = self._values.get("addon_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arguments(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#arguments SpringCloudContainerDeployment#arguments}.'''
        result = self._values.get("arguments")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def commands(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#commands SpringCloudContainerDeployment#commands}.'''
        result = self._values.get("commands")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#environment_variables SpringCloudContainerDeployment#environment_variables}.'''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#id SpringCloudContainerDeployment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#instance_count SpringCloudContainerDeployment#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def language_framework(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#language_framework SpringCloudContainerDeployment#language_framework}.'''
        result = self._values.get("language_framework")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def quota(self) -> typing.Optional["SpringCloudContainerDeploymentQuota"]:
        '''quota block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#quota SpringCloudContainerDeployment#quota}
        '''
        result = self._values.get("quota")
        return typing.cast(typing.Optional["SpringCloudContainerDeploymentQuota"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SpringCloudContainerDeploymentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#timeouts SpringCloudContainerDeployment#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SpringCloudContainerDeploymentTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudContainerDeploymentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudContainerDeployment.SpringCloudContainerDeploymentQuota",
    jsii_struct_bases=[],
    name_mapping={"cpu": "cpu", "memory": "memory"},
)
class SpringCloudContainerDeploymentQuota:
    def __init__(
        self,
        *,
        cpu: typing.Optional[builtins.str] = None,
        memory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#cpu SpringCloudContainerDeployment#cpu}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#memory SpringCloudContainerDeployment#memory}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudContainerDeploymentQuota.__init__)
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cpu is not None:
            self._values["cpu"] = cpu
        if memory is not None:
            self._values["memory"] = memory

    @builtins.property
    def cpu(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#cpu SpringCloudContainerDeployment#cpu}.'''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#memory SpringCloudContainerDeployment#memory}.'''
        result = self._values.get("memory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudContainerDeploymentQuota(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudContainerDeploymentQuotaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudContainerDeployment.SpringCloudContainerDeploymentQuotaOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudContainerDeploymentQuotaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCpu")
    def reset_cpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpu", []))

    @jsii.member(jsii_name="resetMemory")
    def reset_memory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemory", []))

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInput")
    def memory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memoryInput"))

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeploymentQuotaOutputReference, "cpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpu", value)

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeploymentQuotaOutputReference, "memory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memory", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpringCloudContainerDeploymentQuota]:
        return typing.cast(typing.Optional[SpringCloudContainerDeploymentQuota], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpringCloudContainerDeploymentQuota],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeploymentQuotaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudContainerDeployment.SpringCloudContainerDeploymentTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SpringCloudContainerDeploymentTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#create SpringCloudContainerDeployment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#delete SpringCloudContainerDeployment#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#read SpringCloudContainerDeployment#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#update SpringCloudContainerDeployment#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudContainerDeploymentTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#create SpringCloudContainerDeployment#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#delete SpringCloudContainerDeployment#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#read SpringCloudContainerDeployment#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_container_deployment#update SpringCloudContainerDeployment#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudContainerDeploymentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudContainerDeploymentTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudContainerDeployment.SpringCloudContainerDeploymentTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudContainerDeploymentTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeploymentTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeploymentTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeploymentTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeploymentTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SpringCloudContainerDeploymentTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SpringCloudContainerDeploymentTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SpringCloudContainerDeploymentTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudContainerDeploymentTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SpringCloudContainerDeployment",
    "SpringCloudContainerDeploymentConfig",
    "SpringCloudContainerDeploymentQuota",
    "SpringCloudContainerDeploymentQuotaOutputReference",
    "SpringCloudContainerDeploymentTimeouts",
    "SpringCloudContainerDeploymentTimeoutsOutputReference",
]

publication.publish()
