'''
# `cloudflare_pages_project`

Refer to the Terraform Registory for docs: [`cloudflare_pages_project`](https://www.terraform.io/docs/providers/cloudflare/r/pages_project).
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


class PagesProject(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pagesProject.PagesProject",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project cloudflare_pages_project}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        account_id: builtins.str,
        name: builtins.str,
        production_branch: builtins.str,
        build_config: typing.Optional[typing.Union["PagesProjectBuildConfig", typing.Dict[str, typing.Any]]] = None,
        deployment_configs: typing.Optional[typing.Union["PagesProjectDeploymentConfigs", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        source: typing.Optional[typing.Union["PagesProjectSource", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project cloudflare_pages_project} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_id: The account identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#account_id PagesProject#account_id}
        :param name: Name of the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#name PagesProject#name}
        :param production_branch: The name of the branch that is used for the production environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#production_branch PagesProject#production_branch}
        :param build_config: build_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#build_config PagesProject#build_config}
        :param deployment_configs: deployment_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#deployment_configs PagesProject#deployment_configs}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#id PagesProject#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#source PagesProject#source}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PagesProject.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PagesProjectConfig(
            account_id=account_id,
            name=name,
            production_branch=production_branch,
            build_config=build_config,
            deployment_configs=deployment_configs,
            id=id,
            source=source,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBuildConfig")
    def put_build_config(
        self,
        *,
        build_command: typing.Optional[builtins.str] = None,
        destination_dir: typing.Optional[builtins.str] = None,
        root_dir: typing.Optional[builtins.str] = None,
        web_analytics_tag: typing.Optional[builtins.str] = None,
        web_analytics_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param build_command: Command used to build project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#build_command PagesProject#build_command}
        :param destination_dir: Output directory of the build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#destination_dir PagesProject#destination_dir}
        :param root_dir: Directory to run the command. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#root_dir PagesProject#root_dir}
        :param web_analytics_tag: The classifying tag for analytics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#web_analytics_tag PagesProject#web_analytics_tag}
        :param web_analytics_token: The auth token for analytics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#web_analytics_token PagesProject#web_analytics_token}
        '''
        value = PagesProjectBuildConfig(
            build_command=build_command,
            destination_dir=destination_dir,
            root_dir=root_dir,
            web_analytics_tag=web_analytics_tag,
            web_analytics_token=web_analytics_token,
        )

        return typing.cast(None, jsii.invoke(self, "putBuildConfig", [value]))

    @jsii.member(jsii_name="putDeploymentConfigs")
    def put_deployment_configs(
        self,
        *,
        preview: typing.Optional[typing.Union["PagesProjectDeploymentConfigsPreview", typing.Dict[str, typing.Any]]] = None,
        production: typing.Optional[typing.Union["PagesProjectDeploymentConfigsProduction", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param preview: preview block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#preview PagesProject#preview}
        :param production: production block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#production PagesProject#production}
        '''
        value = PagesProjectDeploymentConfigs(preview=preview, production=production)

        return typing.cast(None, jsii.invoke(self, "putDeploymentConfigs", [value]))

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        *,
        config: typing.Optional[typing.Union["PagesProjectSourceConfig", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#config PagesProject#config}
        :param type: Project host type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#type PagesProject#type}
        '''
        value = PagesProjectSource(config=config, type=type)

        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="resetBuildConfig")
    def reset_build_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildConfig", []))

    @jsii.member(jsii_name="resetDeploymentConfigs")
    def reset_deployment_configs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentConfigs", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="buildConfig")
    def build_config(self) -> "PagesProjectBuildConfigOutputReference":
        return typing.cast("PagesProjectBuildConfigOutputReference", jsii.get(self, "buildConfig"))

    @builtins.property
    @jsii.member(jsii_name="createdOn")
    def created_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdOn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigs")
    def deployment_configs(self) -> "PagesProjectDeploymentConfigsOutputReference":
        return typing.cast("PagesProjectDeploymentConfigsOutputReference", jsii.get(self, "deploymentConfigs"))

    @builtins.property
    @jsii.member(jsii_name="domains")
    def domains(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "domains"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "PagesProjectSourceOutputReference":
        return typing.cast("PagesProjectSourceOutputReference", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="subdomain")
    def subdomain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subdomain"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="buildConfigInput")
    def build_config_input(self) -> typing.Optional["PagesProjectBuildConfig"]:
        return typing.cast(typing.Optional["PagesProjectBuildConfig"], jsii.get(self, "buildConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigsInput")
    def deployment_configs_input(
        self,
    ) -> typing.Optional["PagesProjectDeploymentConfigs"]:
        return typing.cast(typing.Optional["PagesProjectDeploymentConfigs"], jsii.get(self, "deploymentConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="productionBranchInput")
    def production_branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productionBranchInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional["PagesProjectSource"]:
        return typing.cast(typing.Optional["PagesProjectSource"], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProject, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProject, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProject, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="productionBranch")
    def production_branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "productionBranch"))

    @production_branch.setter
    def production_branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProject, "production_branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productionBranch", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pagesProject.PagesProjectBuildConfig",
    jsii_struct_bases=[],
    name_mapping={
        "build_command": "buildCommand",
        "destination_dir": "destinationDir",
        "root_dir": "rootDir",
        "web_analytics_tag": "webAnalyticsTag",
        "web_analytics_token": "webAnalyticsToken",
    },
)
class PagesProjectBuildConfig:
    def __init__(
        self,
        *,
        build_command: typing.Optional[builtins.str] = None,
        destination_dir: typing.Optional[builtins.str] = None,
        root_dir: typing.Optional[builtins.str] = None,
        web_analytics_tag: typing.Optional[builtins.str] = None,
        web_analytics_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param build_command: Command used to build project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#build_command PagesProject#build_command}
        :param destination_dir: Output directory of the build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#destination_dir PagesProject#destination_dir}
        :param root_dir: Directory to run the command. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#root_dir PagesProject#root_dir}
        :param web_analytics_tag: The classifying tag for analytics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#web_analytics_tag PagesProject#web_analytics_tag}
        :param web_analytics_token: The auth token for analytics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#web_analytics_token PagesProject#web_analytics_token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PagesProjectBuildConfig.__init__)
            check_type(argname="argument build_command", value=build_command, expected_type=type_hints["build_command"])
            check_type(argname="argument destination_dir", value=destination_dir, expected_type=type_hints["destination_dir"])
            check_type(argname="argument root_dir", value=root_dir, expected_type=type_hints["root_dir"])
            check_type(argname="argument web_analytics_tag", value=web_analytics_tag, expected_type=type_hints["web_analytics_tag"])
            check_type(argname="argument web_analytics_token", value=web_analytics_token, expected_type=type_hints["web_analytics_token"])
        self._values: typing.Dict[str, typing.Any] = {}
        if build_command is not None:
            self._values["build_command"] = build_command
        if destination_dir is not None:
            self._values["destination_dir"] = destination_dir
        if root_dir is not None:
            self._values["root_dir"] = root_dir
        if web_analytics_tag is not None:
            self._values["web_analytics_tag"] = web_analytics_tag
        if web_analytics_token is not None:
            self._values["web_analytics_token"] = web_analytics_token

    @builtins.property
    def build_command(self) -> typing.Optional[builtins.str]:
        '''Command used to build project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#build_command PagesProject#build_command}
        '''
        result = self._values.get("build_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_dir(self) -> typing.Optional[builtins.str]:
        '''Output directory of the build.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#destination_dir PagesProject#destination_dir}
        '''
        result = self._values.get("destination_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_dir(self) -> typing.Optional[builtins.str]:
        '''Directory to run the command.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#root_dir PagesProject#root_dir}
        '''
        result = self._values.get("root_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def web_analytics_tag(self) -> typing.Optional[builtins.str]:
        '''The classifying tag for analytics.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#web_analytics_tag PagesProject#web_analytics_tag}
        '''
        result = self._values.get("web_analytics_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def web_analytics_token(self) -> typing.Optional[builtins.str]:
        '''The auth token for analytics.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#web_analytics_token PagesProject#web_analytics_token}
        '''
        result = self._values.get("web_analytics_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PagesProjectBuildConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PagesProjectBuildConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pagesProject.PagesProjectBuildConfigOutputReference",
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
            type_hints = typing.get_type_hints(PagesProjectBuildConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBuildCommand")
    def reset_build_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildCommand", []))

    @jsii.member(jsii_name="resetDestinationDir")
    def reset_destination_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationDir", []))

    @jsii.member(jsii_name="resetRootDir")
    def reset_root_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootDir", []))

    @jsii.member(jsii_name="resetWebAnalyticsTag")
    def reset_web_analytics_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebAnalyticsTag", []))

    @jsii.member(jsii_name="resetWebAnalyticsToken")
    def reset_web_analytics_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebAnalyticsToken", []))

    @builtins.property
    @jsii.member(jsii_name="buildCommandInput")
    def build_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationDirInput")
    def destination_dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationDirInput"))

    @builtins.property
    @jsii.member(jsii_name="rootDirInput")
    def root_dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootDirInput"))

    @builtins.property
    @jsii.member(jsii_name="webAnalyticsTagInput")
    def web_analytics_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webAnalyticsTagInput"))

    @builtins.property
    @jsii.member(jsii_name="webAnalyticsTokenInput")
    def web_analytics_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webAnalyticsTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="buildCommand")
    def build_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildCommand"))

    @build_command.setter
    def build_command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectBuildConfigOutputReference, "build_command").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildCommand", value)

    @builtins.property
    @jsii.member(jsii_name="destinationDir")
    def destination_dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationDir"))

    @destination_dir.setter
    def destination_dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectBuildConfigOutputReference, "destination_dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationDir", value)

    @builtins.property
    @jsii.member(jsii_name="rootDir")
    def root_dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootDir"))

    @root_dir.setter
    def root_dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectBuildConfigOutputReference, "root_dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootDir", value)

    @builtins.property
    @jsii.member(jsii_name="webAnalyticsTag")
    def web_analytics_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webAnalyticsTag"))

    @web_analytics_tag.setter
    def web_analytics_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectBuildConfigOutputReference, "web_analytics_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webAnalyticsTag", value)

    @builtins.property
    @jsii.member(jsii_name="webAnalyticsToken")
    def web_analytics_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webAnalyticsToken"))

    @web_analytics_token.setter
    def web_analytics_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectBuildConfigOutputReference, "web_analytics_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webAnalyticsToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PagesProjectBuildConfig]:
        return typing.cast(typing.Optional[PagesProjectBuildConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PagesProjectBuildConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectBuildConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pagesProject.PagesProjectConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_id": "accountId",
        "name": "name",
        "production_branch": "productionBranch",
        "build_config": "buildConfig",
        "deployment_configs": "deploymentConfigs",
        "id": "id",
        "source": "source",
    },
)
class PagesProjectConfig(cdktf.TerraformMetaArguments):
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
        account_id: builtins.str,
        name: builtins.str,
        production_branch: builtins.str,
        build_config: typing.Optional[typing.Union[PagesProjectBuildConfig, typing.Dict[str, typing.Any]]] = None,
        deployment_configs: typing.Optional[typing.Union["PagesProjectDeploymentConfigs", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        source: typing.Optional[typing.Union["PagesProjectSource", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_id: The account identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#account_id PagesProject#account_id}
        :param name: Name of the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#name PagesProject#name}
        :param production_branch: The name of the branch that is used for the production environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#production_branch PagesProject#production_branch}
        :param build_config: build_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#build_config PagesProject#build_config}
        :param deployment_configs: deployment_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#deployment_configs PagesProject#deployment_configs}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#id PagesProject#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#source PagesProject#source}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(build_config, dict):
            build_config = PagesProjectBuildConfig(**build_config)
        if isinstance(deployment_configs, dict):
            deployment_configs = PagesProjectDeploymentConfigs(**deployment_configs)
        if isinstance(source, dict):
            source = PagesProjectSource(**source)
        if __debug__:
            type_hints = typing.get_type_hints(PagesProjectConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument production_branch", value=production_branch, expected_type=type_hints["production_branch"])
            check_type(argname="argument build_config", value=build_config, expected_type=type_hints["build_config"])
            check_type(argname="argument deployment_configs", value=deployment_configs, expected_type=type_hints["deployment_configs"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
            "name": name,
            "production_branch": production_branch,
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
        if build_config is not None:
            self._values["build_config"] = build_config
        if deployment_configs is not None:
            self._values["deployment_configs"] = deployment_configs
        if id is not None:
            self._values["id"] = id
        if source is not None:
            self._values["source"] = source

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
    def account_id(self) -> builtins.str:
        '''The account identifier to target for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#account_id PagesProject#account_id}
        '''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#name PagesProject#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def production_branch(self) -> builtins.str:
        '''The name of the branch that is used for the production environment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#production_branch PagesProject#production_branch}
        '''
        result = self._values.get("production_branch")
        assert result is not None, "Required property 'production_branch' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def build_config(self) -> typing.Optional[PagesProjectBuildConfig]:
        '''build_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#build_config PagesProject#build_config}
        '''
        result = self._values.get("build_config")
        return typing.cast(typing.Optional[PagesProjectBuildConfig], result)

    @builtins.property
    def deployment_configs(self) -> typing.Optional["PagesProjectDeploymentConfigs"]:
        '''deployment_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#deployment_configs PagesProject#deployment_configs}
        '''
        result = self._values.get("deployment_configs")
        return typing.cast(typing.Optional["PagesProjectDeploymentConfigs"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#id PagesProject#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional["PagesProjectSource"]:
        '''source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#source PagesProject#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional["PagesProjectSource"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PagesProjectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pagesProject.PagesProjectDeploymentConfigs",
    jsii_struct_bases=[],
    name_mapping={"preview": "preview", "production": "production"},
)
class PagesProjectDeploymentConfigs:
    def __init__(
        self,
        *,
        preview: typing.Optional[typing.Union["PagesProjectDeploymentConfigsPreview", typing.Dict[str, typing.Any]]] = None,
        production: typing.Optional[typing.Union["PagesProjectDeploymentConfigsProduction", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param preview: preview block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#preview PagesProject#preview}
        :param production: production block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#production PagesProject#production}
        '''
        if isinstance(preview, dict):
            preview = PagesProjectDeploymentConfigsPreview(**preview)
        if isinstance(production, dict):
            production = PagesProjectDeploymentConfigsProduction(**production)
        if __debug__:
            type_hints = typing.get_type_hints(PagesProjectDeploymentConfigs.__init__)
            check_type(argname="argument preview", value=preview, expected_type=type_hints["preview"])
            check_type(argname="argument production", value=production, expected_type=type_hints["production"])
        self._values: typing.Dict[str, typing.Any] = {}
        if preview is not None:
            self._values["preview"] = preview
        if production is not None:
            self._values["production"] = production

    @builtins.property
    def preview(self) -> typing.Optional["PagesProjectDeploymentConfigsPreview"]:
        '''preview block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#preview PagesProject#preview}
        '''
        result = self._values.get("preview")
        return typing.cast(typing.Optional["PagesProjectDeploymentConfigsPreview"], result)

    @builtins.property
    def production(self) -> typing.Optional["PagesProjectDeploymentConfigsProduction"]:
        '''production block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#production PagesProject#production}
        '''
        result = self._values.get("production")
        return typing.cast(typing.Optional["PagesProjectDeploymentConfigsProduction"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PagesProjectDeploymentConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PagesProjectDeploymentConfigsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pagesProject.PagesProjectDeploymentConfigsOutputReference",
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
            type_hints = typing.get_type_hints(PagesProjectDeploymentConfigsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPreview")
    def put_preview(
        self,
        *,
        compatibility_date: typing.Optional[builtins.str] = None,
        compatibility_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
        d1_databases: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        durable_object_namespaces: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        kv_namespaces: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        r2_buckets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param compatibility_date: Compatibility date used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#compatibility_date PagesProject#compatibility_date}
        :param compatibility_flags: Compatibility flags used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#compatibility_flags PagesProject#compatibility_flags}
        :param d1_databases: D1 Databases used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#d1_databases PagesProject#d1_databases}
        :param durable_object_namespaces: Durable Object namespaces used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#durable_object_namespaces PagesProject#durable_object_namespaces}
        :param environment_variables: Environment variables for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#environment_variables PagesProject#environment_variables}
        :param kv_namespaces: KV namespaces used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#kv_namespaces PagesProject#kv_namespaces}
        :param r2_buckets: R2 Buckets used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#r2_buckets PagesProject#r2_buckets}
        '''
        value = PagesProjectDeploymentConfigsPreview(
            compatibility_date=compatibility_date,
            compatibility_flags=compatibility_flags,
            d1_databases=d1_databases,
            durable_object_namespaces=durable_object_namespaces,
            environment_variables=environment_variables,
            kv_namespaces=kv_namespaces,
            r2_buckets=r2_buckets,
        )

        return typing.cast(None, jsii.invoke(self, "putPreview", [value]))

    @jsii.member(jsii_name="putProduction")
    def put_production(
        self,
        *,
        compatibility_date: typing.Optional[builtins.str] = None,
        compatibility_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
        d1_databases: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        durable_object_namespaces: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        kv_namespaces: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        r2_buckets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param compatibility_date: Compatibility date used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#compatibility_date PagesProject#compatibility_date}
        :param compatibility_flags: Compatibility flags used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#compatibility_flags PagesProject#compatibility_flags}
        :param d1_databases: D1 Databases used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#d1_databases PagesProject#d1_databases}
        :param durable_object_namespaces: Durable Object namespaces used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#durable_object_namespaces PagesProject#durable_object_namespaces}
        :param environment_variables: Environment variables for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#environment_variables PagesProject#environment_variables}
        :param kv_namespaces: KV namespaces used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#kv_namespaces PagesProject#kv_namespaces}
        :param r2_buckets: R2 Buckets used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#r2_buckets PagesProject#r2_buckets}
        '''
        value = PagesProjectDeploymentConfigsProduction(
            compatibility_date=compatibility_date,
            compatibility_flags=compatibility_flags,
            d1_databases=d1_databases,
            durable_object_namespaces=durable_object_namespaces,
            environment_variables=environment_variables,
            kv_namespaces=kv_namespaces,
            r2_buckets=r2_buckets,
        )

        return typing.cast(None, jsii.invoke(self, "putProduction", [value]))

    @jsii.member(jsii_name="resetPreview")
    def reset_preview(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreview", []))

    @jsii.member(jsii_name="resetProduction")
    def reset_production(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProduction", []))

    @builtins.property
    @jsii.member(jsii_name="preview")
    def preview(self) -> "PagesProjectDeploymentConfigsPreviewOutputReference":
        return typing.cast("PagesProjectDeploymentConfigsPreviewOutputReference", jsii.get(self, "preview"))

    @builtins.property
    @jsii.member(jsii_name="production")
    def production(self) -> "PagesProjectDeploymentConfigsProductionOutputReference":
        return typing.cast("PagesProjectDeploymentConfigsProductionOutputReference", jsii.get(self, "production"))

    @builtins.property
    @jsii.member(jsii_name="previewInput")
    def preview_input(self) -> typing.Optional["PagesProjectDeploymentConfigsPreview"]:
        return typing.cast(typing.Optional["PagesProjectDeploymentConfigsPreview"], jsii.get(self, "previewInput"))

    @builtins.property
    @jsii.member(jsii_name="productionInput")
    def production_input(
        self,
    ) -> typing.Optional["PagesProjectDeploymentConfigsProduction"]:
        return typing.cast(typing.Optional["PagesProjectDeploymentConfigsProduction"], jsii.get(self, "productionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PagesProjectDeploymentConfigs]:
        return typing.cast(typing.Optional[PagesProjectDeploymentConfigs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PagesProjectDeploymentConfigs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pagesProject.PagesProjectDeploymentConfigsPreview",
    jsii_struct_bases=[],
    name_mapping={
        "compatibility_date": "compatibilityDate",
        "compatibility_flags": "compatibilityFlags",
        "d1_databases": "d1Databases",
        "durable_object_namespaces": "durableObjectNamespaces",
        "environment_variables": "environmentVariables",
        "kv_namespaces": "kvNamespaces",
        "r2_buckets": "r2Buckets",
    },
)
class PagesProjectDeploymentConfigsPreview:
    def __init__(
        self,
        *,
        compatibility_date: typing.Optional[builtins.str] = None,
        compatibility_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
        d1_databases: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        durable_object_namespaces: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        kv_namespaces: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        r2_buckets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param compatibility_date: Compatibility date used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#compatibility_date PagesProject#compatibility_date}
        :param compatibility_flags: Compatibility flags used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#compatibility_flags PagesProject#compatibility_flags}
        :param d1_databases: D1 Databases used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#d1_databases PagesProject#d1_databases}
        :param durable_object_namespaces: Durable Object namespaces used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#durable_object_namespaces PagesProject#durable_object_namespaces}
        :param environment_variables: Environment variables for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#environment_variables PagesProject#environment_variables}
        :param kv_namespaces: KV namespaces used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#kv_namespaces PagesProject#kv_namespaces}
        :param r2_buckets: R2 Buckets used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#r2_buckets PagesProject#r2_buckets}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PagesProjectDeploymentConfigsPreview.__init__)
            check_type(argname="argument compatibility_date", value=compatibility_date, expected_type=type_hints["compatibility_date"])
            check_type(argname="argument compatibility_flags", value=compatibility_flags, expected_type=type_hints["compatibility_flags"])
            check_type(argname="argument d1_databases", value=d1_databases, expected_type=type_hints["d1_databases"])
            check_type(argname="argument durable_object_namespaces", value=durable_object_namespaces, expected_type=type_hints["durable_object_namespaces"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument kv_namespaces", value=kv_namespaces, expected_type=type_hints["kv_namespaces"])
            check_type(argname="argument r2_buckets", value=r2_buckets, expected_type=type_hints["r2_buckets"])
        self._values: typing.Dict[str, typing.Any] = {}
        if compatibility_date is not None:
            self._values["compatibility_date"] = compatibility_date
        if compatibility_flags is not None:
            self._values["compatibility_flags"] = compatibility_flags
        if d1_databases is not None:
            self._values["d1_databases"] = d1_databases
        if durable_object_namespaces is not None:
            self._values["durable_object_namespaces"] = durable_object_namespaces
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if kv_namespaces is not None:
            self._values["kv_namespaces"] = kv_namespaces
        if r2_buckets is not None:
            self._values["r2_buckets"] = r2_buckets

    @builtins.property
    def compatibility_date(self) -> typing.Optional[builtins.str]:
        '''Compatibility date used for Pages Functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#compatibility_date PagesProject#compatibility_date}
        '''
        result = self._values.get("compatibility_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compatibility_flags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Compatibility flags used for Pages Functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#compatibility_flags PagesProject#compatibility_flags}
        '''
        result = self._values.get("compatibility_flags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def d1_databases(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''D1 Databases used for Pages Functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#d1_databases PagesProject#d1_databases}
        '''
        result = self._values.get("d1_databases")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def durable_object_namespaces(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Durable Object namespaces used for Pages Functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#durable_object_namespaces PagesProject#durable_object_namespaces}
        '''
        result = self._values.get("durable_object_namespaces")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Environment variables for Pages Functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#environment_variables PagesProject#environment_variables}
        '''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def kv_namespaces(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''KV namespaces used for Pages Functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#kv_namespaces PagesProject#kv_namespaces}
        '''
        result = self._values.get("kv_namespaces")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def r2_buckets(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''R2 Buckets used for Pages Functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#r2_buckets PagesProject#r2_buckets}
        '''
        result = self._values.get("r2_buckets")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PagesProjectDeploymentConfigsPreview(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PagesProjectDeploymentConfigsPreviewOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pagesProject.PagesProjectDeploymentConfigsPreviewOutputReference",
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
            type_hints = typing.get_type_hints(PagesProjectDeploymentConfigsPreviewOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCompatibilityDate")
    def reset_compatibility_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompatibilityDate", []))

    @jsii.member(jsii_name="resetCompatibilityFlags")
    def reset_compatibility_flags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompatibilityFlags", []))

    @jsii.member(jsii_name="resetD1Databases")
    def reset_d1_databases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetD1Databases", []))

    @jsii.member(jsii_name="resetDurableObjectNamespaces")
    def reset_durable_object_namespaces(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDurableObjectNamespaces", []))

    @jsii.member(jsii_name="resetEnvironmentVariables")
    def reset_environment_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentVariables", []))

    @jsii.member(jsii_name="resetKvNamespaces")
    def reset_kv_namespaces(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKvNamespaces", []))

    @jsii.member(jsii_name="resetR2Buckets")
    def reset_r2_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetR2Buckets", []))

    @builtins.property
    @jsii.member(jsii_name="compatibilityDateInput")
    def compatibility_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compatibilityDateInput"))

    @builtins.property
    @jsii.member(jsii_name="compatibilityFlagsInput")
    def compatibility_flags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "compatibilityFlagsInput"))

    @builtins.property
    @jsii.member(jsii_name="d1DatabasesInput")
    def d1_databases_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "d1DatabasesInput"))

    @builtins.property
    @jsii.member(jsii_name="durableObjectNamespacesInput")
    def durable_object_namespaces_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "durableObjectNamespacesInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentVariablesInput")
    def environment_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "environmentVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="kvNamespacesInput")
    def kv_namespaces_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "kvNamespacesInput"))

    @builtins.property
    @jsii.member(jsii_name="r2BucketsInput")
    def r2_buckets_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "r2BucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="compatibilityDate")
    def compatibility_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compatibilityDate"))

    @compatibility_date.setter
    def compatibility_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsPreviewOutputReference, "compatibility_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compatibilityDate", value)

    @builtins.property
    @jsii.member(jsii_name="compatibilityFlags")
    def compatibility_flags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "compatibilityFlags"))

    @compatibility_flags.setter
    def compatibility_flags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsPreviewOutputReference, "compatibility_flags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compatibilityFlags", value)

    @builtins.property
    @jsii.member(jsii_name="d1Databases")
    def d1_databases(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "d1Databases"))

    @d1_databases.setter
    def d1_databases(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsPreviewOutputReference, "d1_databases").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "d1Databases", value)

    @builtins.property
    @jsii.member(jsii_name="durableObjectNamespaces")
    def durable_object_namespaces(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "durableObjectNamespaces"))

    @durable_object_namespaces.setter
    def durable_object_namespaces(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsPreviewOutputReference, "durable_object_namespaces").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "durableObjectNamespaces", value)

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
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsPreviewOutputReference, "environment_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="kvNamespaces")
    def kv_namespaces(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "kvNamespaces"))

    @kv_namespaces.setter
    def kv_namespaces(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsPreviewOutputReference, "kv_namespaces").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kvNamespaces", value)

    @builtins.property
    @jsii.member(jsii_name="r2Buckets")
    def r2_buckets(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "r2Buckets"))

    @r2_buckets.setter
    def r2_buckets(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsPreviewOutputReference, "r2_buckets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "r2Buckets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PagesProjectDeploymentConfigsPreview]:
        return typing.cast(typing.Optional[PagesProjectDeploymentConfigsPreview], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PagesProjectDeploymentConfigsPreview],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsPreviewOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pagesProject.PagesProjectDeploymentConfigsProduction",
    jsii_struct_bases=[],
    name_mapping={
        "compatibility_date": "compatibilityDate",
        "compatibility_flags": "compatibilityFlags",
        "d1_databases": "d1Databases",
        "durable_object_namespaces": "durableObjectNamespaces",
        "environment_variables": "environmentVariables",
        "kv_namespaces": "kvNamespaces",
        "r2_buckets": "r2Buckets",
    },
)
class PagesProjectDeploymentConfigsProduction:
    def __init__(
        self,
        *,
        compatibility_date: typing.Optional[builtins.str] = None,
        compatibility_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
        d1_databases: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        durable_object_namespaces: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        kv_namespaces: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        r2_buckets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param compatibility_date: Compatibility date used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#compatibility_date PagesProject#compatibility_date}
        :param compatibility_flags: Compatibility flags used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#compatibility_flags PagesProject#compatibility_flags}
        :param d1_databases: D1 Databases used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#d1_databases PagesProject#d1_databases}
        :param durable_object_namespaces: Durable Object namespaces used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#durable_object_namespaces PagesProject#durable_object_namespaces}
        :param environment_variables: Environment variables for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#environment_variables PagesProject#environment_variables}
        :param kv_namespaces: KV namespaces used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#kv_namespaces PagesProject#kv_namespaces}
        :param r2_buckets: R2 Buckets used for Pages Functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#r2_buckets PagesProject#r2_buckets}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PagesProjectDeploymentConfigsProduction.__init__)
            check_type(argname="argument compatibility_date", value=compatibility_date, expected_type=type_hints["compatibility_date"])
            check_type(argname="argument compatibility_flags", value=compatibility_flags, expected_type=type_hints["compatibility_flags"])
            check_type(argname="argument d1_databases", value=d1_databases, expected_type=type_hints["d1_databases"])
            check_type(argname="argument durable_object_namespaces", value=durable_object_namespaces, expected_type=type_hints["durable_object_namespaces"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument kv_namespaces", value=kv_namespaces, expected_type=type_hints["kv_namespaces"])
            check_type(argname="argument r2_buckets", value=r2_buckets, expected_type=type_hints["r2_buckets"])
        self._values: typing.Dict[str, typing.Any] = {}
        if compatibility_date is not None:
            self._values["compatibility_date"] = compatibility_date
        if compatibility_flags is not None:
            self._values["compatibility_flags"] = compatibility_flags
        if d1_databases is not None:
            self._values["d1_databases"] = d1_databases
        if durable_object_namespaces is not None:
            self._values["durable_object_namespaces"] = durable_object_namespaces
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if kv_namespaces is not None:
            self._values["kv_namespaces"] = kv_namespaces
        if r2_buckets is not None:
            self._values["r2_buckets"] = r2_buckets

    @builtins.property
    def compatibility_date(self) -> typing.Optional[builtins.str]:
        '''Compatibility date used for Pages Functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#compatibility_date PagesProject#compatibility_date}
        '''
        result = self._values.get("compatibility_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compatibility_flags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Compatibility flags used for Pages Functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#compatibility_flags PagesProject#compatibility_flags}
        '''
        result = self._values.get("compatibility_flags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def d1_databases(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''D1 Databases used for Pages Functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#d1_databases PagesProject#d1_databases}
        '''
        result = self._values.get("d1_databases")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def durable_object_namespaces(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Durable Object namespaces used for Pages Functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#durable_object_namespaces PagesProject#durable_object_namespaces}
        '''
        result = self._values.get("durable_object_namespaces")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Environment variables for Pages Functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#environment_variables PagesProject#environment_variables}
        '''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def kv_namespaces(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''KV namespaces used for Pages Functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#kv_namespaces PagesProject#kv_namespaces}
        '''
        result = self._values.get("kv_namespaces")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def r2_buckets(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''R2 Buckets used for Pages Functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#r2_buckets PagesProject#r2_buckets}
        '''
        result = self._values.get("r2_buckets")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PagesProjectDeploymentConfigsProduction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PagesProjectDeploymentConfigsProductionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pagesProject.PagesProjectDeploymentConfigsProductionOutputReference",
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
            type_hints = typing.get_type_hints(PagesProjectDeploymentConfigsProductionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCompatibilityDate")
    def reset_compatibility_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompatibilityDate", []))

    @jsii.member(jsii_name="resetCompatibilityFlags")
    def reset_compatibility_flags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompatibilityFlags", []))

    @jsii.member(jsii_name="resetD1Databases")
    def reset_d1_databases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetD1Databases", []))

    @jsii.member(jsii_name="resetDurableObjectNamespaces")
    def reset_durable_object_namespaces(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDurableObjectNamespaces", []))

    @jsii.member(jsii_name="resetEnvironmentVariables")
    def reset_environment_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentVariables", []))

    @jsii.member(jsii_name="resetKvNamespaces")
    def reset_kv_namespaces(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKvNamespaces", []))

    @jsii.member(jsii_name="resetR2Buckets")
    def reset_r2_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetR2Buckets", []))

    @builtins.property
    @jsii.member(jsii_name="compatibilityDateInput")
    def compatibility_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compatibilityDateInput"))

    @builtins.property
    @jsii.member(jsii_name="compatibilityFlagsInput")
    def compatibility_flags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "compatibilityFlagsInput"))

    @builtins.property
    @jsii.member(jsii_name="d1DatabasesInput")
    def d1_databases_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "d1DatabasesInput"))

    @builtins.property
    @jsii.member(jsii_name="durableObjectNamespacesInput")
    def durable_object_namespaces_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "durableObjectNamespacesInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentVariablesInput")
    def environment_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "environmentVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="kvNamespacesInput")
    def kv_namespaces_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "kvNamespacesInput"))

    @builtins.property
    @jsii.member(jsii_name="r2BucketsInput")
    def r2_buckets_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "r2BucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="compatibilityDate")
    def compatibility_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compatibilityDate"))

    @compatibility_date.setter
    def compatibility_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsProductionOutputReference, "compatibility_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compatibilityDate", value)

    @builtins.property
    @jsii.member(jsii_name="compatibilityFlags")
    def compatibility_flags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "compatibilityFlags"))

    @compatibility_flags.setter
    def compatibility_flags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsProductionOutputReference, "compatibility_flags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compatibilityFlags", value)

    @builtins.property
    @jsii.member(jsii_name="d1Databases")
    def d1_databases(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "d1Databases"))

    @d1_databases.setter
    def d1_databases(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsProductionOutputReference, "d1_databases").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "d1Databases", value)

    @builtins.property
    @jsii.member(jsii_name="durableObjectNamespaces")
    def durable_object_namespaces(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "durableObjectNamespaces"))

    @durable_object_namespaces.setter
    def durable_object_namespaces(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsProductionOutputReference, "durable_object_namespaces").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "durableObjectNamespaces", value)

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
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsProductionOutputReference, "environment_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="kvNamespaces")
    def kv_namespaces(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "kvNamespaces"))

    @kv_namespaces.setter
    def kv_namespaces(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsProductionOutputReference, "kv_namespaces").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kvNamespaces", value)

    @builtins.property
    @jsii.member(jsii_name="r2Buckets")
    def r2_buckets(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "r2Buckets"))

    @r2_buckets.setter
    def r2_buckets(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsProductionOutputReference, "r2_buckets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "r2Buckets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PagesProjectDeploymentConfigsProduction]:
        return typing.cast(typing.Optional[PagesProjectDeploymentConfigsProduction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PagesProjectDeploymentConfigsProduction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectDeploymentConfigsProductionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pagesProject.PagesProjectSource",
    jsii_struct_bases=[],
    name_mapping={"config": "config", "type": "type"},
)
class PagesProjectSource:
    def __init__(
        self,
        *,
        config: typing.Optional[typing.Union["PagesProjectSourceConfig", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#config PagesProject#config}
        :param type: Project host type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#type PagesProject#type}
        '''
        if isinstance(config, dict):
            config = PagesProjectSourceConfig(**config)
        if __debug__:
            type_hints = typing.get_type_hints(PagesProjectSource.__init__)
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if config is not None:
            self._values["config"] = config
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def config(self) -> typing.Optional["PagesProjectSourceConfig"]:
        '''config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#config PagesProject#config}
        '''
        result = self._values.get("config")
        return typing.cast(typing.Optional["PagesProjectSourceConfig"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Project host type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#type PagesProject#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PagesProjectSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pagesProject.PagesProjectSourceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "production_branch": "productionBranch",
        "deployments_enabled": "deploymentsEnabled",
        "owner": "owner",
        "pr_comments_enabled": "prCommentsEnabled",
        "preview_branch_excludes": "previewBranchExcludes",
        "preview_branch_includes": "previewBranchIncludes",
        "preview_deployment_setting": "previewDeploymentSetting",
        "production_deployment_enabled": "productionDeploymentEnabled",
        "repo_name": "repoName",
    },
)
class PagesProjectSourceConfig:
    def __init__(
        self,
        *,
        production_branch: builtins.str,
        deployments_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        owner: typing.Optional[builtins.str] = None,
        pr_comments_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        preview_branch_excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        preview_branch_includes: typing.Optional[typing.Sequence[builtins.str]] = None,
        preview_deployment_setting: typing.Optional[builtins.str] = None,
        production_deployment_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param production_branch: Project production branch name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#production_branch PagesProject#production_branch}
        :param deployments_enabled: Toggle deployments on this repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#deployments_enabled PagesProject#deployments_enabled}
        :param owner: Project owner username. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#owner PagesProject#owner}
        :param pr_comments_enabled: Enable Pages to comment on Pull Requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#pr_comments_enabled PagesProject#pr_comments_enabled}
        :param preview_branch_excludes: Branches will be excluded from automatic deployment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#preview_branch_excludes PagesProject#preview_branch_excludes}
        :param preview_branch_includes: Branches will be included for automatic deployment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#preview_branch_includes PagesProject#preview_branch_includes}
        :param preview_deployment_setting: Preview Deployment Setting. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#preview_deployment_setting PagesProject#preview_deployment_setting}
        :param production_deployment_enabled: Enable production deployments. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#production_deployment_enabled PagesProject#production_deployment_enabled}
        :param repo_name: Project repository name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#repo_name PagesProject#repo_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PagesProjectSourceConfig.__init__)
            check_type(argname="argument production_branch", value=production_branch, expected_type=type_hints["production_branch"])
            check_type(argname="argument deployments_enabled", value=deployments_enabled, expected_type=type_hints["deployments_enabled"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument pr_comments_enabled", value=pr_comments_enabled, expected_type=type_hints["pr_comments_enabled"])
            check_type(argname="argument preview_branch_excludes", value=preview_branch_excludes, expected_type=type_hints["preview_branch_excludes"])
            check_type(argname="argument preview_branch_includes", value=preview_branch_includes, expected_type=type_hints["preview_branch_includes"])
            check_type(argname="argument preview_deployment_setting", value=preview_deployment_setting, expected_type=type_hints["preview_deployment_setting"])
            check_type(argname="argument production_deployment_enabled", value=production_deployment_enabled, expected_type=type_hints["production_deployment_enabled"])
            check_type(argname="argument repo_name", value=repo_name, expected_type=type_hints["repo_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "production_branch": production_branch,
        }
        if deployments_enabled is not None:
            self._values["deployments_enabled"] = deployments_enabled
        if owner is not None:
            self._values["owner"] = owner
        if pr_comments_enabled is not None:
            self._values["pr_comments_enabled"] = pr_comments_enabled
        if preview_branch_excludes is not None:
            self._values["preview_branch_excludes"] = preview_branch_excludes
        if preview_branch_includes is not None:
            self._values["preview_branch_includes"] = preview_branch_includes
        if preview_deployment_setting is not None:
            self._values["preview_deployment_setting"] = preview_deployment_setting
        if production_deployment_enabled is not None:
            self._values["production_deployment_enabled"] = production_deployment_enabled
        if repo_name is not None:
            self._values["repo_name"] = repo_name

    @builtins.property
    def production_branch(self) -> builtins.str:
        '''Project production branch name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#production_branch PagesProject#production_branch}
        '''
        result = self._values.get("production_branch")
        assert result is not None, "Required property 'production_branch' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployments_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Toggle deployments on this repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#deployments_enabled PagesProject#deployments_enabled}
        '''
        result = self._values.get("deployments_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def owner(self) -> typing.Optional[builtins.str]:
        '''Project owner username.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#owner PagesProject#owner}
        '''
        result = self._values.get("owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pr_comments_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable Pages to comment on Pull Requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#pr_comments_enabled PagesProject#pr_comments_enabled}
        '''
        result = self._values.get("pr_comments_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def preview_branch_excludes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Branches will be excluded from automatic deployment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#preview_branch_excludes PagesProject#preview_branch_excludes}
        '''
        result = self._values.get("preview_branch_excludes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def preview_branch_includes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Branches will be included for automatic deployment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#preview_branch_includes PagesProject#preview_branch_includes}
        '''
        result = self._values.get("preview_branch_includes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def preview_deployment_setting(self) -> typing.Optional[builtins.str]:
        '''Preview Deployment Setting.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#preview_deployment_setting PagesProject#preview_deployment_setting}
        '''
        result = self._values.get("preview_deployment_setting")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def production_deployment_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable production deployments.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#production_deployment_enabled PagesProject#production_deployment_enabled}
        '''
        result = self._values.get("production_deployment_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def repo_name(self) -> typing.Optional[builtins.str]:
        '''Project repository name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#repo_name PagesProject#repo_name}
        '''
        result = self._values.get("repo_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PagesProjectSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PagesProjectSourceConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pagesProject.PagesProjectSourceConfigOutputReference",
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
            type_hints = typing.get_type_hints(PagesProjectSourceConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeploymentsEnabled")
    def reset_deployments_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentsEnabled", []))

    @jsii.member(jsii_name="resetOwner")
    def reset_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwner", []))

    @jsii.member(jsii_name="resetPrCommentsEnabled")
    def reset_pr_comments_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrCommentsEnabled", []))

    @jsii.member(jsii_name="resetPreviewBranchExcludes")
    def reset_preview_branch_excludes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreviewBranchExcludes", []))

    @jsii.member(jsii_name="resetPreviewBranchIncludes")
    def reset_preview_branch_includes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreviewBranchIncludes", []))

    @jsii.member(jsii_name="resetPreviewDeploymentSetting")
    def reset_preview_deployment_setting(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreviewDeploymentSetting", []))

    @jsii.member(jsii_name="resetProductionDeploymentEnabled")
    def reset_production_deployment_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProductionDeploymentEnabled", []))

    @jsii.member(jsii_name="resetRepoName")
    def reset_repo_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepoName", []))

    @builtins.property
    @jsii.member(jsii_name="deploymentsEnabledInput")
    def deployments_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deploymentsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="prCommentsEnabledInput")
    def pr_comments_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "prCommentsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="previewBranchExcludesInput")
    def preview_branch_excludes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "previewBranchExcludesInput"))

    @builtins.property
    @jsii.member(jsii_name="previewBranchIncludesInput")
    def preview_branch_includes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "previewBranchIncludesInput"))

    @builtins.property
    @jsii.member(jsii_name="previewDeploymentSettingInput")
    def preview_deployment_setting_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "previewDeploymentSettingInput"))

    @builtins.property
    @jsii.member(jsii_name="productionBranchInput")
    def production_branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productionBranchInput"))

    @builtins.property
    @jsii.member(jsii_name="productionDeploymentEnabledInput")
    def production_deployment_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "productionDeploymentEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="repoNameInput")
    def repo_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentsEnabled")
    def deployments_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deploymentsEnabled"))

    @deployments_enabled.setter
    def deployments_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectSourceConfigOutputReference, "deployments_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectSourceConfigOutputReference, "owner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="prCommentsEnabled")
    def pr_comments_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "prCommentsEnabled"))

    @pr_comments_enabled.setter
    def pr_comments_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectSourceConfigOutputReference, "pr_comments_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prCommentsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="previewBranchExcludes")
    def preview_branch_excludes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "previewBranchExcludes"))

    @preview_branch_excludes.setter
    def preview_branch_excludes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectSourceConfigOutputReference, "preview_branch_excludes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "previewBranchExcludes", value)

    @builtins.property
    @jsii.member(jsii_name="previewBranchIncludes")
    def preview_branch_includes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "previewBranchIncludes"))

    @preview_branch_includes.setter
    def preview_branch_includes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectSourceConfigOutputReference, "preview_branch_includes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "previewBranchIncludes", value)

    @builtins.property
    @jsii.member(jsii_name="previewDeploymentSetting")
    def preview_deployment_setting(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "previewDeploymentSetting"))

    @preview_deployment_setting.setter
    def preview_deployment_setting(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectSourceConfigOutputReference, "preview_deployment_setting").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "previewDeploymentSetting", value)

    @builtins.property
    @jsii.member(jsii_name="productionBranch")
    def production_branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "productionBranch"))

    @production_branch.setter
    def production_branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectSourceConfigOutputReference, "production_branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productionBranch", value)

    @builtins.property
    @jsii.member(jsii_name="productionDeploymentEnabled")
    def production_deployment_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "productionDeploymentEnabled"))

    @production_deployment_enabled.setter
    def production_deployment_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectSourceConfigOutputReference, "production_deployment_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productionDeploymentEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="repoName")
    def repo_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoName"))

    @repo_name.setter
    def repo_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectSourceConfigOutputReference, "repo_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repoName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PagesProjectSourceConfig]:
        return typing.cast(typing.Optional[PagesProjectSourceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PagesProjectSourceConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectSourceConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PagesProjectSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pagesProject.PagesProjectSourceOutputReference",
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
            type_hints = typing.get_type_hints(PagesProjectSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConfig")
    def put_config(
        self,
        *,
        production_branch: builtins.str,
        deployments_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        owner: typing.Optional[builtins.str] = None,
        pr_comments_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        preview_branch_excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        preview_branch_includes: typing.Optional[typing.Sequence[builtins.str]] = None,
        preview_deployment_setting: typing.Optional[builtins.str] = None,
        production_deployment_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param production_branch: Project production branch name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#production_branch PagesProject#production_branch}
        :param deployments_enabled: Toggle deployments on this repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#deployments_enabled PagesProject#deployments_enabled}
        :param owner: Project owner username. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#owner PagesProject#owner}
        :param pr_comments_enabled: Enable Pages to comment on Pull Requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#pr_comments_enabled PagesProject#pr_comments_enabled}
        :param preview_branch_excludes: Branches will be excluded from automatic deployment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#preview_branch_excludes PagesProject#preview_branch_excludes}
        :param preview_branch_includes: Branches will be included for automatic deployment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#preview_branch_includes PagesProject#preview_branch_includes}
        :param preview_deployment_setting: Preview Deployment Setting. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#preview_deployment_setting PagesProject#preview_deployment_setting}
        :param production_deployment_enabled: Enable production deployments. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#production_deployment_enabled PagesProject#production_deployment_enabled}
        :param repo_name: Project repository name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/pages_project#repo_name PagesProject#repo_name}
        '''
        value = PagesProjectSourceConfig(
            production_branch=production_branch,
            deployments_enabled=deployments_enabled,
            owner=owner,
            pr_comments_enabled=pr_comments_enabled,
            preview_branch_excludes=preview_branch_excludes,
            preview_branch_includes=preview_branch_includes,
            preview_deployment_setting=preview_deployment_setting,
            production_deployment_enabled=production_deployment_enabled,
            repo_name=repo_name,
        )

        return typing.cast(None, jsii.invoke(self, "putConfig", [value]))

    @jsii.member(jsii_name="resetConfig")
    def reset_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfig", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(self) -> PagesProjectSourceConfigOutputReference:
        return typing.cast(PagesProjectSourceConfigOutputReference, jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="configInput")
    def config_input(self) -> typing.Optional[PagesProjectSourceConfig]:
        return typing.cast(typing.Optional[PagesProjectSourceConfig], jsii.get(self, "configInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectSourceOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PagesProjectSource]:
        return typing.cast(typing.Optional[PagesProjectSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PagesProjectSource]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagesProjectSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PagesProject",
    "PagesProjectBuildConfig",
    "PagesProjectBuildConfigOutputReference",
    "PagesProjectConfig",
    "PagesProjectDeploymentConfigs",
    "PagesProjectDeploymentConfigsOutputReference",
    "PagesProjectDeploymentConfigsPreview",
    "PagesProjectDeploymentConfigsPreviewOutputReference",
    "PagesProjectDeploymentConfigsProduction",
    "PagesProjectDeploymentConfigsProductionOutputReference",
    "PagesProjectSource",
    "PagesProjectSourceConfig",
    "PagesProjectSourceConfigOutputReference",
    "PagesProjectSourceOutputReference",
]

publication.publish()
