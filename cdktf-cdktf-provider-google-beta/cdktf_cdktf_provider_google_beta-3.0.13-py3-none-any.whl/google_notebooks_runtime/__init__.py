'''
# `google_notebooks_runtime`

Refer to the Terraform Registory for docs: [`google_notebooks_runtime`](https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime).
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


class GoogleNotebooksRuntime(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntime",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime google_notebooks_runtime}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        access_config: typing.Optional[typing.Union["GoogleNotebooksRuntimeAccessConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        software_config: typing.Optional[typing.Union["GoogleNotebooksRuntimeSoftwareConfig", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleNotebooksRuntimeTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_machine: typing.Optional[typing.Union["GoogleNotebooksRuntimeVirtualMachine", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime google_notebooks_runtime} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: A reference to the zone where the machine resides. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#location GoogleNotebooksRuntime#location}
        :param name: The name specified for the Notebook runtime. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#name GoogleNotebooksRuntime#name}
        :param access_config: access_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#access_config GoogleNotebooksRuntime#access_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#id GoogleNotebooksRuntime#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#project GoogleNotebooksRuntime#project}.
        :param software_config: software_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#software_config GoogleNotebooksRuntime#software_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#timeouts GoogleNotebooksRuntime#timeouts}
        :param virtual_machine: virtual_machine block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#virtual_machine GoogleNotebooksRuntime#virtual_machine}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntime.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleNotebooksRuntimeConfig(
            location=location,
            name=name,
            access_config=access_config,
            id=id,
            project=project,
            software_config=software_config,
            timeouts=timeouts,
            virtual_machine=virtual_machine,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAccessConfig")
    def put_access_config(
        self,
        *,
        access_type: typing.Optional[builtins.str] = None,
        runtime_owner: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_type: The type of access mode this instance. For valid values, see 'https://cloud.google.com/vertex-ai/docs/workbench/reference/ rest/v1/projects.locations.runtimes#RuntimeAccessType'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#access_type GoogleNotebooksRuntime#access_type}
        :param runtime_owner: The owner of this runtime after creation. Format: 'alias@example.com'. Currently supports one owner only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#runtime_owner GoogleNotebooksRuntime#runtime_owner}
        '''
        value = GoogleNotebooksRuntimeAccessConfig(
            access_type=access_type, runtime_owner=runtime_owner
        )

        return typing.cast(None, jsii.invoke(self, "putAccessConfig", [value]))

    @jsii.member(jsii_name="putSoftwareConfig")
    def put_software_config(
        self,
        *,
        custom_gpu_driver_path: typing.Optional[builtins.str] = None,
        enable_health_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        idle_shutdown: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        idle_shutdown_timeout: typing.Optional[jsii.Number] = None,
        install_gpu_driver: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        kernels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleNotebooksRuntimeSoftwareConfigKernels", typing.Dict[str, typing.Any]]]]] = None,
        notebook_upgrade_schedule: typing.Optional[builtins.str] = None,
        post_startup_script: typing.Optional[builtins.str] = None,
        post_startup_script_behavior: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param custom_gpu_driver_path: Specify a custom Cloud Storage path where the GPU driver is stored. If not specified, we'll automatically choose from official GPU drivers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#custom_gpu_driver_path GoogleNotebooksRuntime#custom_gpu_driver_path}
        :param enable_health_monitoring: Verifies core internal services are running. Default: True. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#enable_health_monitoring GoogleNotebooksRuntime#enable_health_monitoring}
        :param idle_shutdown: Runtime will automatically shutdown after idle_shutdown_time. Default: True. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#idle_shutdown GoogleNotebooksRuntime#idle_shutdown}
        :param idle_shutdown_timeout: Time in minutes to wait before shuting down runtime. Default: 180 minutes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#idle_shutdown_timeout GoogleNotebooksRuntime#idle_shutdown_timeout}
        :param install_gpu_driver: Install Nvidia Driver automatically. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#install_gpu_driver GoogleNotebooksRuntime#install_gpu_driver}
        :param kernels: kernels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#kernels GoogleNotebooksRuntime#kernels}
        :param notebook_upgrade_schedule: Cron expression in UTC timezone for schedule instance auto upgrade. Please follow the `cron format <https://en.wikipedia.org/wiki/Cron>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#notebook_upgrade_schedule GoogleNotebooksRuntime#notebook_upgrade_schedule}
        :param post_startup_script: Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path (gs://path-to-file/file-name). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#post_startup_script GoogleNotebooksRuntime#post_startup_script}
        :param post_startup_script_behavior: Behavior for the post startup script. Possible values: ["POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED", "RUN_EVERY_START", "DOWNLOAD_AND_RUN_EVERY_START"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#post_startup_script_behavior GoogleNotebooksRuntime#post_startup_script_behavior}
        '''
        value = GoogleNotebooksRuntimeSoftwareConfig(
            custom_gpu_driver_path=custom_gpu_driver_path,
            enable_health_monitoring=enable_health_monitoring,
            idle_shutdown=idle_shutdown,
            idle_shutdown_timeout=idle_shutdown_timeout,
            install_gpu_driver=install_gpu_driver,
            kernels=kernels,
            notebook_upgrade_schedule=notebook_upgrade_schedule,
            post_startup_script=post_startup_script,
            post_startup_script_behavior=post_startup_script_behavior,
        )

        return typing.cast(None, jsii.invoke(self, "putSoftwareConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#create GoogleNotebooksRuntime#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#delete GoogleNotebooksRuntime#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#update GoogleNotebooksRuntime#update}.
        '''
        value = GoogleNotebooksRuntimeTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVirtualMachine")
    def put_virtual_machine(
        self,
        *,
        virtual_machine_config: typing.Optional[typing.Union["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param virtual_machine_config: virtual_machine_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#virtual_machine_config GoogleNotebooksRuntime#virtual_machine_config}
        '''
        value = GoogleNotebooksRuntimeVirtualMachine(
            virtual_machine_config=virtual_machine_config
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualMachine", [value]))

    @jsii.member(jsii_name="resetAccessConfig")
    def reset_access_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetSoftwareConfig")
    def reset_software_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSoftwareConfig", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVirtualMachine")
    def reset_virtual_machine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualMachine", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessConfig")
    def access_config(self) -> "GoogleNotebooksRuntimeAccessConfigOutputReference":
        return typing.cast("GoogleNotebooksRuntimeAccessConfigOutputReference", jsii.get(self, "accessConfig"))

    @builtins.property
    @jsii.member(jsii_name="healthState")
    def health_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthState"))

    @builtins.property
    @jsii.member(jsii_name="metrics")
    def metrics(self) -> "GoogleNotebooksRuntimeMetricsList":
        return typing.cast("GoogleNotebooksRuntimeMetricsList", jsii.get(self, "metrics"))

    @builtins.property
    @jsii.member(jsii_name="softwareConfig")
    def software_config(self) -> "GoogleNotebooksRuntimeSoftwareConfigOutputReference":
        return typing.cast("GoogleNotebooksRuntimeSoftwareConfigOutputReference", jsii.get(self, "softwareConfig"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleNotebooksRuntimeTimeoutsOutputReference":
        return typing.cast("GoogleNotebooksRuntimeTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachine")
    def virtual_machine(self) -> "GoogleNotebooksRuntimeVirtualMachineOutputReference":
        return typing.cast("GoogleNotebooksRuntimeVirtualMachineOutputReference", jsii.get(self, "virtualMachine"))

    @builtins.property
    @jsii.member(jsii_name="accessConfigInput")
    def access_config_input(
        self,
    ) -> typing.Optional["GoogleNotebooksRuntimeAccessConfig"]:
        return typing.cast(typing.Optional["GoogleNotebooksRuntimeAccessConfig"], jsii.get(self, "accessConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="softwareConfigInput")
    def software_config_input(
        self,
    ) -> typing.Optional["GoogleNotebooksRuntimeSoftwareConfig"]:
        return typing.cast(typing.Optional["GoogleNotebooksRuntimeSoftwareConfig"], jsii.get(self, "softwareConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleNotebooksRuntimeTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleNotebooksRuntimeTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineInput")
    def virtual_machine_input(
        self,
    ) -> typing.Optional["GoogleNotebooksRuntimeVirtualMachine"]:
        return typing.cast(typing.Optional["GoogleNotebooksRuntimeVirtualMachine"], jsii.get(self, "virtualMachineInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntime, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntime, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntime, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntime, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeAccessConfig",
    jsii_struct_bases=[],
    name_mapping={"access_type": "accessType", "runtime_owner": "runtimeOwner"},
)
class GoogleNotebooksRuntimeAccessConfig:
    def __init__(
        self,
        *,
        access_type: typing.Optional[builtins.str] = None,
        runtime_owner: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_type: The type of access mode this instance. For valid values, see 'https://cloud.google.com/vertex-ai/docs/workbench/reference/ rest/v1/projects.locations.runtimes#RuntimeAccessType'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#access_type GoogleNotebooksRuntime#access_type}
        :param runtime_owner: The owner of this runtime after creation. Format: 'alias@example.com'. Currently supports one owner only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#runtime_owner GoogleNotebooksRuntime#runtime_owner}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeAccessConfig.__init__)
            check_type(argname="argument access_type", value=access_type, expected_type=type_hints["access_type"])
            check_type(argname="argument runtime_owner", value=runtime_owner, expected_type=type_hints["runtime_owner"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_type is not None:
            self._values["access_type"] = access_type
        if runtime_owner is not None:
            self._values["runtime_owner"] = runtime_owner

    @builtins.property
    def access_type(self) -> typing.Optional[builtins.str]:
        '''The type of access mode this instance. For valid values, see 'https://cloud.google.com/vertex-ai/docs/workbench/reference/ rest/v1/projects.locations.runtimes#RuntimeAccessType'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#access_type GoogleNotebooksRuntime#access_type}
        '''
        result = self._values.get("access_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime_owner(self) -> typing.Optional[builtins.str]:
        '''The owner of this runtime after creation. Format: 'alias@example.com'. Currently supports one owner only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#runtime_owner GoogleNotebooksRuntime#runtime_owner}
        '''
        result = self._values.get("runtime_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNotebooksRuntimeAccessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleNotebooksRuntimeAccessConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeAccessConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeAccessConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAccessType")
    def reset_access_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessType", []))

    @jsii.member(jsii_name="resetRuntimeOwner")
    def reset_runtime_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeOwner", []))

    @builtins.property
    @jsii.member(jsii_name="proxyUri")
    def proxy_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proxyUri"))

    @builtins.property
    @jsii.member(jsii_name="accessTypeInput")
    def access_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeOwnerInput")
    def runtime_owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeOwnerInput"))

    @builtins.property
    @jsii.member(jsii_name="accessType")
    def access_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessType"))

    @access_type.setter
    def access_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeAccessConfigOutputReference, "access_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessType", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeOwner")
    def runtime_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeOwner"))

    @runtime_owner.setter
    def runtime_owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeAccessConfigOutputReference, "runtime_owner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeOwner", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleNotebooksRuntimeAccessConfig]:
        return typing.cast(typing.Optional[GoogleNotebooksRuntimeAccessConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleNotebooksRuntimeAccessConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeAccessConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "access_config": "accessConfig",
        "id": "id",
        "project": "project",
        "software_config": "softwareConfig",
        "timeouts": "timeouts",
        "virtual_machine": "virtualMachine",
    },
)
class GoogleNotebooksRuntimeConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        access_config: typing.Optional[typing.Union[GoogleNotebooksRuntimeAccessConfig, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        software_config: typing.Optional[typing.Union["GoogleNotebooksRuntimeSoftwareConfig", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleNotebooksRuntimeTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_machine: typing.Optional[typing.Union["GoogleNotebooksRuntimeVirtualMachine", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: A reference to the zone where the machine resides. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#location GoogleNotebooksRuntime#location}
        :param name: The name specified for the Notebook runtime. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#name GoogleNotebooksRuntime#name}
        :param access_config: access_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#access_config GoogleNotebooksRuntime#access_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#id GoogleNotebooksRuntime#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#project GoogleNotebooksRuntime#project}.
        :param software_config: software_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#software_config GoogleNotebooksRuntime#software_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#timeouts GoogleNotebooksRuntime#timeouts}
        :param virtual_machine: virtual_machine block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#virtual_machine GoogleNotebooksRuntime#virtual_machine}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(access_config, dict):
            access_config = GoogleNotebooksRuntimeAccessConfig(**access_config)
        if isinstance(software_config, dict):
            software_config = GoogleNotebooksRuntimeSoftwareConfig(**software_config)
        if isinstance(timeouts, dict):
            timeouts = GoogleNotebooksRuntimeTimeouts(**timeouts)
        if isinstance(virtual_machine, dict):
            virtual_machine = GoogleNotebooksRuntimeVirtualMachine(**virtual_machine)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument access_config", value=access_config, expected_type=type_hints["access_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument software_config", value=software_config, expected_type=type_hints["software_config"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument virtual_machine", value=virtual_machine, expected_type=type_hints["virtual_machine"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
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
        if access_config is not None:
            self._values["access_config"] = access_config
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project
        if software_config is not None:
            self._values["software_config"] = software_config
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if virtual_machine is not None:
            self._values["virtual_machine"] = virtual_machine

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
    def location(self) -> builtins.str:
        '''A reference to the zone where the machine resides.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#location GoogleNotebooksRuntime#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name specified for the Notebook runtime.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#name GoogleNotebooksRuntime#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_config(self) -> typing.Optional[GoogleNotebooksRuntimeAccessConfig]:
        '''access_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#access_config GoogleNotebooksRuntime#access_config}
        '''
        result = self._values.get("access_config")
        return typing.cast(typing.Optional[GoogleNotebooksRuntimeAccessConfig], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#id GoogleNotebooksRuntime#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#project GoogleNotebooksRuntime#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def software_config(
        self,
    ) -> typing.Optional["GoogleNotebooksRuntimeSoftwareConfig"]:
        '''software_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#software_config GoogleNotebooksRuntime#software_config}
        '''
        result = self._values.get("software_config")
        return typing.cast(typing.Optional["GoogleNotebooksRuntimeSoftwareConfig"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleNotebooksRuntimeTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#timeouts GoogleNotebooksRuntime#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleNotebooksRuntimeTimeouts"], result)

    @builtins.property
    def virtual_machine(
        self,
    ) -> typing.Optional["GoogleNotebooksRuntimeVirtualMachine"]:
        '''virtual_machine block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#virtual_machine GoogleNotebooksRuntime#virtual_machine}
        '''
        result = self._values.get("virtual_machine")
        return typing.cast(typing.Optional["GoogleNotebooksRuntimeVirtualMachine"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNotebooksRuntimeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeMetrics",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleNotebooksRuntimeMetrics:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNotebooksRuntimeMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleNotebooksRuntimeMetricsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeMetricsList",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeMetricsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GoogleNotebooksRuntimeMetricsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeMetricsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleNotebooksRuntimeMetricsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeMetricsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeMetricsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeMetricsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleNotebooksRuntimeMetricsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeMetricsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeMetricsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="systemMetrics")
    def system_metrics(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "systemMetrics"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleNotebooksRuntimeMetrics]:
        return typing.cast(typing.Optional[GoogleNotebooksRuntimeMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleNotebooksRuntimeMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeMetricsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeSoftwareConfig",
    jsii_struct_bases=[],
    name_mapping={
        "custom_gpu_driver_path": "customGpuDriverPath",
        "enable_health_monitoring": "enableHealthMonitoring",
        "idle_shutdown": "idleShutdown",
        "idle_shutdown_timeout": "idleShutdownTimeout",
        "install_gpu_driver": "installGpuDriver",
        "kernels": "kernels",
        "notebook_upgrade_schedule": "notebookUpgradeSchedule",
        "post_startup_script": "postStartupScript",
        "post_startup_script_behavior": "postStartupScriptBehavior",
    },
)
class GoogleNotebooksRuntimeSoftwareConfig:
    def __init__(
        self,
        *,
        custom_gpu_driver_path: typing.Optional[builtins.str] = None,
        enable_health_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        idle_shutdown: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        idle_shutdown_timeout: typing.Optional[jsii.Number] = None,
        install_gpu_driver: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        kernels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleNotebooksRuntimeSoftwareConfigKernels", typing.Dict[str, typing.Any]]]]] = None,
        notebook_upgrade_schedule: typing.Optional[builtins.str] = None,
        post_startup_script: typing.Optional[builtins.str] = None,
        post_startup_script_behavior: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param custom_gpu_driver_path: Specify a custom Cloud Storage path where the GPU driver is stored. If not specified, we'll automatically choose from official GPU drivers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#custom_gpu_driver_path GoogleNotebooksRuntime#custom_gpu_driver_path}
        :param enable_health_monitoring: Verifies core internal services are running. Default: True. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#enable_health_monitoring GoogleNotebooksRuntime#enable_health_monitoring}
        :param idle_shutdown: Runtime will automatically shutdown after idle_shutdown_time. Default: True. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#idle_shutdown GoogleNotebooksRuntime#idle_shutdown}
        :param idle_shutdown_timeout: Time in minutes to wait before shuting down runtime. Default: 180 minutes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#idle_shutdown_timeout GoogleNotebooksRuntime#idle_shutdown_timeout}
        :param install_gpu_driver: Install Nvidia Driver automatically. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#install_gpu_driver GoogleNotebooksRuntime#install_gpu_driver}
        :param kernels: kernels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#kernels GoogleNotebooksRuntime#kernels}
        :param notebook_upgrade_schedule: Cron expression in UTC timezone for schedule instance auto upgrade. Please follow the `cron format <https://en.wikipedia.org/wiki/Cron>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#notebook_upgrade_schedule GoogleNotebooksRuntime#notebook_upgrade_schedule}
        :param post_startup_script: Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path (gs://path-to-file/file-name). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#post_startup_script GoogleNotebooksRuntime#post_startup_script}
        :param post_startup_script_behavior: Behavior for the post startup script. Possible values: ["POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED", "RUN_EVERY_START", "DOWNLOAD_AND_RUN_EVERY_START"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#post_startup_script_behavior GoogleNotebooksRuntime#post_startup_script_behavior}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeSoftwareConfig.__init__)
            check_type(argname="argument custom_gpu_driver_path", value=custom_gpu_driver_path, expected_type=type_hints["custom_gpu_driver_path"])
            check_type(argname="argument enable_health_monitoring", value=enable_health_monitoring, expected_type=type_hints["enable_health_monitoring"])
            check_type(argname="argument idle_shutdown", value=idle_shutdown, expected_type=type_hints["idle_shutdown"])
            check_type(argname="argument idle_shutdown_timeout", value=idle_shutdown_timeout, expected_type=type_hints["idle_shutdown_timeout"])
            check_type(argname="argument install_gpu_driver", value=install_gpu_driver, expected_type=type_hints["install_gpu_driver"])
            check_type(argname="argument kernels", value=kernels, expected_type=type_hints["kernels"])
            check_type(argname="argument notebook_upgrade_schedule", value=notebook_upgrade_schedule, expected_type=type_hints["notebook_upgrade_schedule"])
            check_type(argname="argument post_startup_script", value=post_startup_script, expected_type=type_hints["post_startup_script"])
            check_type(argname="argument post_startup_script_behavior", value=post_startup_script_behavior, expected_type=type_hints["post_startup_script_behavior"])
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_gpu_driver_path is not None:
            self._values["custom_gpu_driver_path"] = custom_gpu_driver_path
        if enable_health_monitoring is not None:
            self._values["enable_health_monitoring"] = enable_health_monitoring
        if idle_shutdown is not None:
            self._values["idle_shutdown"] = idle_shutdown
        if idle_shutdown_timeout is not None:
            self._values["idle_shutdown_timeout"] = idle_shutdown_timeout
        if install_gpu_driver is not None:
            self._values["install_gpu_driver"] = install_gpu_driver
        if kernels is not None:
            self._values["kernels"] = kernels
        if notebook_upgrade_schedule is not None:
            self._values["notebook_upgrade_schedule"] = notebook_upgrade_schedule
        if post_startup_script is not None:
            self._values["post_startup_script"] = post_startup_script
        if post_startup_script_behavior is not None:
            self._values["post_startup_script_behavior"] = post_startup_script_behavior

    @builtins.property
    def custom_gpu_driver_path(self) -> typing.Optional[builtins.str]:
        '''Specify a custom Cloud Storage path where the GPU driver is stored.

        If not specified, we'll automatically choose from official GPU drivers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#custom_gpu_driver_path GoogleNotebooksRuntime#custom_gpu_driver_path}
        '''
        result = self._values.get("custom_gpu_driver_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_health_monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Verifies core internal services are running. Default: True.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#enable_health_monitoring GoogleNotebooksRuntime#enable_health_monitoring}
        '''
        result = self._values.get("enable_health_monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def idle_shutdown(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Runtime will automatically shutdown after idle_shutdown_time. Default: True.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#idle_shutdown GoogleNotebooksRuntime#idle_shutdown}
        '''
        result = self._values.get("idle_shutdown")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def idle_shutdown_timeout(self) -> typing.Optional[jsii.Number]:
        '''Time in minutes to wait before shuting down runtime. Default: 180 minutes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#idle_shutdown_timeout GoogleNotebooksRuntime#idle_shutdown_timeout}
        '''
        result = self._values.get("idle_shutdown_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def install_gpu_driver(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Install Nvidia Driver automatically.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#install_gpu_driver GoogleNotebooksRuntime#install_gpu_driver}
        '''
        result = self._values.get("install_gpu_driver")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def kernels(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleNotebooksRuntimeSoftwareConfigKernels"]]]:
        '''kernels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#kernels GoogleNotebooksRuntime#kernels}
        '''
        result = self._values.get("kernels")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleNotebooksRuntimeSoftwareConfigKernels"]]], result)

    @builtins.property
    def notebook_upgrade_schedule(self) -> typing.Optional[builtins.str]:
        '''Cron expression in UTC timezone for schedule instance auto upgrade. Please follow the `cron format <https://en.wikipedia.org/wiki/Cron>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#notebook_upgrade_schedule GoogleNotebooksRuntime#notebook_upgrade_schedule}
        '''
        result = self._values.get("notebook_upgrade_schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def post_startup_script(self) -> typing.Optional[builtins.str]:
        '''Path to a Bash script that automatically runs after a notebook instance fully boots up.

        The path must be a URL or
        Cloud Storage path (gs://path-to-file/file-name).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#post_startup_script GoogleNotebooksRuntime#post_startup_script}
        '''
        result = self._values.get("post_startup_script")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def post_startup_script_behavior(self) -> typing.Optional[builtins.str]:
        '''Behavior for the post startup script. Possible values: ["POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED", "RUN_EVERY_START", "DOWNLOAD_AND_RUN_EVERY_START"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#post_startup_script_behavior GoogleNotebooksRuntime#post_startup_script_behavior}
        '''
        result = self._values.get("post_startup_script_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNotebooksRuntimeSoftwareConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeSoftwareConfigKernels",
    jsii_struct_bases=[],
    name_mapping={"repository": "repository", "tag": "tag"},
)
class GoogleNotebooksRuntimeSoftwareConfigKernels:
    def __init__(
        self,
        *,
        repository: builtins.str,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param repository: The path to the container image repository. For example: gcr.io/{project_id}/{imageName}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#repository GoogleNotebooksRuntime#repository}
        :param tag: The tag of the container image. If not specified, this defaults to the latest tag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#tag GoogleNotebooksRuntime#tag}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeSoftwareConfigKernels.__init__)
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[str, typing.Any] = {
            "repository": repository,
        }
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def repository(self) -> builtins.str:
        '''The path to the container image repository. For example: gcr.io/{project_id}/{imageName}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#repository GoogleNotebooksRuntime#repository}
        '''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The tag of the container image. If not specified, this defaults to the latest tag.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#tag GoogleNotebooksRuntime#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNotebooksRuntimeSoftwareConfigKernels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleNotebooksRuntimeSoftwareConfigKernelsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeSoftwareConfigKernelsList",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeSoftwareConfigKernelsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleNotebooksRuntimeSoftwareConfigKernelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeSoftwareConfigKernelsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleNotebooksRuntimeSoftwareConfigKernelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigKernelsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigKernelsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigKernelsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleNotebooksRuntimeSoftwareConfigKernels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleNotebooksRuntimeSoftwareConfigKernels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleNotebooksRuntimeSoftwareConfigKernels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigKernelsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleNotebooksRuntimeSoftwareConfigKernelsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeSoftwareConfigKernelsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeSoftwareConfigKernelsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @builtins.property
    @jsii.member(jsii_name="repositoryInput")
    def repository_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repository"))

    @repository.setter
    def repository(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigKernelsOutputReference, "repository").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repository", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigKernelsOutputReference, "tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleNotebooksRuntimeSoftwareConfigKernels, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleNotebooksRuntimeSoftwareConfigKernels, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleNotebooksRuntimeSoftwareConfigKernels, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigKernelsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleNotebooksRuntimeSoftwareConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeSoftwareConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeSoftwareConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putKernels")
    def put_kernels(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleNotebooksRuntimeSoftwareConfigKernels, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeSoftwareConfigOutputReference.put_kernels)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putKernels", [value]))

    @jsii.member(jsii_name="resetCustomGpuDriverPath")
    def reset_custom_gpu_driver_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomGpuDriverPath", []))

    @jsii.member(jsii_name="resetEnableHealthMonitoring")
    def reset_enable_health_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableHealthMonitoring", []))

    @jsii.member(jsii_name="resetIdleShutdown")
    def reset_idle_shutdown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleShutdown", []))

    @jsii.member(jsii_name="resetIdleShutdownTimeout")
    def reset_idle_shutdown_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleShutdownTimeout", []))

    @jsii.member(jsii_name="resetInstallGpuDriver")
    def reset_install_gpu_driver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstallGpuDriver", []))

    @jsii.member(jsii_name="resetKernels")
    def reset_kernels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKernels", []))

    @jsii.member(jsii_name="resetNotebookUpgradeSchedule")
    def reset_notebook_upgrade_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotebookUpgradeSchedule", []))

    @jsii.member(jsii_name="resetPostStartupScript")
    def reset_post_startup_script(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostStartupScript", []))

    @jsii.member(jsii_name="resetPostStartupScriptBehavior")
    def reset_post_startup_script_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostStartupScriptBehavior", []))

    @builtins.property
    @jsii.member(jsii_name="kernels")
    def kernels(self) -> GoogleNotebooksRuntimeSoftwareConfigKernelsList:
        return typing.cast(GoogleNotebooksRuntimeSoftwareConfigKernelsList, jsii.get(self, "kernels"))

    @builtins.property
    @jsii.member(jsii_name="upgradeable")
    def upgradeable(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "upgradeable"))

    @builtins.property
    @jsii.member(jsii_name="customGpuDriverPathInput")
    def custom_gpu_driver_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customGpuDriverPathInput"))

    @builtins.property
    @jsii.member(jsii_name="enableHealthMonitoringInput")
    def enable_health_monitoring_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableHealthMonitoringInput"))

    @builtins.property
    @jsii.member(jsii_name="idleShutdownInput")
    def idle_shutdown_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "idleShutdownInput"))

    @builtins.property
    @jsii.member(jsii_name="idleShutdownTimeoutInput")
    def idle_shutdown_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleShutdownTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="installGpuDriverInput")
    def install_gpu_driver_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "installGpuDriverInput"))

    @builtins.property
    @jsii.member(jsii_name="kernelsInput")
    def kernels_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleNotebooksRuntimeSoftwareConfigKernels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleNotebooksRuntimeSoftwareConfigKernels]]], jsii.get(self, "kernelsInput"))

    @builtins.property
    @jsii.member(jsii_name="notebookUpgradeScheduleInput")
    def notebook_upgrade_schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notebookUpgradeScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="postStartupScriptBehaviorInput")
    def post_startup_script_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postStartupScriptBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="postStartupScriptInput")
    def post_startup_script_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postStartupScriptInput"))

    @builtins.property
    @jsii.member(jsii_name="customGpuDriverPath")
    def custom_gpu_driver_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customGpuDriverPath"))

    @custom_gpu_driver_path.setter
    def custom_gpu_driver_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigOutputReference, "custom_gpu_driver_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customGpuDriverPath", value)

    @builtins.property
    @jsii.member(jsii_name="enableHealthMonitoring")
    def enable_health_monitoring(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableHealthMonitoring"))

    @enable_health_monitoring.setter
    def enable_health_monitoring(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigOutputReference, "enable_health_monitoring").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableHealthMonitoring", value)

    @builtins.property
    @jsii.member(jsii_name="idleShutdown")
    def idle_shutdown(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "idleShutdown"))

    @idle_shutdown.setter
    def idle_shutdown(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigOutputReference, "idle_shutdown").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleShutdown", value)

    @builtins.property
    @jsii.member(jsii_name="idleShutdownTimeout")
    def idle_shutdown_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleShutdownTimeout"))

    @idle_shutdown_timeout.setter
    def idle_shutdown_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigOutputReference, "idle_shutdown_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleShutdownTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="installGpuDriver")
    def install_gpu_driver(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "installGpuDriver"))

    @install_gpu_driver.setter
    def install_gpu_driver(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigOutputReference, "install_gpu_driver").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "installGpuDriver", value)

    @builtins.property
    @jsii.member(jsii_name="notebookUpgradeSchedule")
    def notebook_upgrade_schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notebookUpgradeSchedule"))

    @notebook_upgrade_schedule.setter
    def notebook_upgrade_schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigOutputReference, "notebook_upgrade_schedule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notebookUpgradeSchedule", value)

    @builtins.property
    @jsii.member(jsii_name="postStartupScript")
    def post_startup_script(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postStartupScript"))

    @post_startup_script.setter
    def post_startup_script(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigOutputReference, "post_startup_script").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postStartupScript", value)

    @builtins.property
    @jsii.member(jsii_name="postStartupScriptBehavior")
    def post_startup_script_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postStartupScriptBehavior"))

    @post_startup_script_behavior.setter
    def post_startup_script_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigOutputReference, "post_startup_script_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postStartupScriptBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleNotebooksRuntimeSoftwareConfig]:
        return typing.cast(typing.Optional[GoogleNotebooksRuntimeSoftwareConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleNotebooksRuntimeSoftwareConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeSoftwareConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleNotebooksRuntimeTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#create GoogleNotebooksRuntime#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#delete GoogleNotebooksRuntime#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#update GoogleNotebooksRuntime#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#create GoogleNotebooksRuntime#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#delete GoogleNotebooksRuntime#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#update GoogleNotebooksRuntime#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNotebooksRuntimeTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleNotebooksRuntimeTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleNotebooksRuntimeTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleNotebooksRuntimeTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleNotebooksRuntimeTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachine",
    jsii_struct_bases=[],
    name_mapping={"virtual_machine_config": "virtualMachineConfig"},
)
class GoogleNotebooksRuntimeVirtualMachine:
    def __init__(
        self,
        *,
        virtual_machine_config: typing.Optional[typing.Union["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param virtual_machine_config: virtual_machine_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#virtual_machine_config GoogleNotebooksRuntime#virtual_machine_config}
        '''
        if isinstance(virtual_machine_config, dict):
            virtual_machine_config = GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig(**virtual_machine_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachine.__init__)
            check_type(argname="argument virtual_machine_config", value=virtual_machine_config, expected_type=type_hints["virtual_machine_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if virtual_machine_config is not None:
            self._values["virtual_machine_config"] = virtual_machine_config

    @builtins.property
    def virtual_machine_config(
        self,
    ) -> typing.Optional["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig"]:
        '''virtual_machine_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#virtual_machine_config GoogleNotebooksRuntime#virtual_machine_config}
        '''
        result = self._values.get("virtual_machine_config")
        return typing.cast(typing.Optional["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNotebooksRuntimeVirtualMachine(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleNotebooksRuntimeVirtualMachineOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineOutputReference",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putVirtualMachineConfig")
    def put_virtual_machine_config(
        self,
        *,
        data_disk: typing.Union["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk", typing.Dict[str, typing.Any]],
        machine_type: builtins.str,
        accelerator_config: typing.Optional[typing.Union["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig", typing.Dict[str, typing.Any]]] = None,
        container_images: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages", typing.Dict[str, typing.Any]]]]] = None,
        encryption_config: typing.Optional[typing.Union["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig", typing.Dict[str, typing.Any]]] = None,
        internal_ip_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        network: typing.Optional[builtins.str] = None,
        nic_type: typing.Optional[builtins.str] = None,
        reserved_ip_range: typing.Optional[builtins.str] = None,
        shielded_instance_config: typing.Optional[typing.Union["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig", typing.Dict[str, typing.Any]]] = None,
        subnet: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param data_disk: data_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#data_disk GoogleNotebooksRuntime#data_disk}
        :param machine_type: The Compute Engine machine type used for runtimes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#machine_type GoogleNotebooksRuntime#machine_type}
        :param accelerator_config: accelerator_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#accelerator_config GoogleNotebooksRuntime#accelerator_config}
        :param container_images: container_images block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#container_images GoogleNotebooksRuntime#container_images}
        :param encryption_config: encryption_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#encryption_config GoogleNotebooksRuntime#encryption_config}
        :param internal_ip_only: If true, runtime will only have internal IP addresses. By default, runtimes are not restricted to internal IP addresses, and will have ephemeral external IP addresses assigned to each vm. This 'internal_ip_only' restriction can only be enabled for subnetwork enabled networks, and all dependencies must be configured to be accessible without external IP addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#internal_ip_only GoogleNotebooksRuntime#internal_ip_only}
        :param labels: The labels to associate with this runtime. Label **keys** must contain 1 to 63 characters, and must conform to [RFC 1035] (https://www.ietf.org/rfc/rfc1035.txt). Label **values** may be empty, but, if present, must contain 1 to 63 characters, and must conform to `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`_. No more than 32 labels can be associated with a cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#labels GoogleNotebooksRuntime#labels}
        :param metadata: The Compute Engine metadata entries to add to virtual machine. (see [Project and instance metadata](https://cloud.google.com /compute/docs/storing-retrieving-metadata#project_and_instance _metadata)). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#metadata GoogleNotebooksRuntime#metadata}
        :param network: The Compute Engine network to be used for machine communications. Cannot be specified with subnetwork. If neither 'network' nor 'subnet' is specified, the "default" network of the project is used, if it exists. A full URL or partial URI. Examples: 'https://www.googleapis.com/compute/v1/projects/[project_id]/ regions/global/default' 'projects/[project_id]/regions/global/default' Runtimes are managed resources inside Google Infrastructure. Runtimes support the following network configurations: Google Managed Network (Network & subnet are empty) Consumer Project VPC (network & subnet are required). Requires configuring Private Service Access. Shared VPC (network & subnet are required). Requires configuring Private Service Access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#network GoogleNotebooksRuntime#network}
        :param nic_type: The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet. Possible values: ["UNSPECIFIED_NIC_TYPE", "VIRTIO_NET", "GVNIC"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#nic_type GoogleNotebooksRuntime#nic_type}
        :param reserved_ip_range: Reserved IP Range name is used for VPC Peering. The subnetwork allocation will use the range *name* if it's assigned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#reserved_ip_range GoogleNotebooksRuntime#reserved_ip_range}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#shielded_instance_config GoogleNotebooksRuntime#shielded_instance_config}
        :param subnet: The Compute Engine subnetwork to be used for machine communications. Cannot be specified with network. A full URL or partial URI are valid. Examples: 'https://www.googleapis.com/compute/v1/projects/[project_id]/ regions/us-east1/subnetworks/sub0' 'projects/[project_id]/regions/us-east1/subnetworks/sub0' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#subnet GoogleNotebooksRuntime#subnet}
        :param tags: The Compute Engine tags to add to runtime (see [Tagging instances] (https://cloud.google.com/compute/docs/ label-or-tag-resources#tags)). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#tags GoogleNotebooksRuntime#tags}
        '''
        value = GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig(
            data_disk=data_disk,
            machine_type=machine_type,
            accelerator_config=accelerator_config,
            container_images=container_images,
            encryption_config=encryption_config,
            internal_ip_only=internal_ip_only,
            labels=labels,
            metadata=metadata,
            network=network,
            nic_type=nic_type,
            reserved_ip_range=reserved_ip_range,
            shielded_instance_config=shielded_instance_config,
            subnet=subnet,
            tags=tags,
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualMachineConfig", [value]))

    @jsii.member(jsii_name="resetVirtualMachineConfig")
    def reset_virtual_machine_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualMachineConfig", []))

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @builtins.property
    @jsii.member(jsii_name="instanceName")
    def instance_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceName"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineConfig")
    def virtual_machine_config(
        self,
    ) -> "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference":
        return typing.cast("GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference", jsii.get(self, "virtualMachineConfig"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineConfigInput")
    def virtual_machine_config_input(
        self,
    ) -> typing.Optional["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig"]:
        return typing.cast(typing.Optional["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig"], jsii.get(self, "virtualMachineConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleNotebooksRuntimeVirtualMachine]:
        return typing.cast(typing.Optional[GoogleNotebooksRuntimeVirtualMachine], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleNotebooksRuntimeVirtualMachine],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig",
    jsii_struct_bases=[],
    name_mapping={
        "data_disk": "dataDisk",
        "machine_type": "machineType",
        "accelerator_config": "acceleratorConfig",
        "container_images": "containerImages",
        "encryption_config": "encryptionConfig",
        "internal_ip_only": "internalIpOnly",
        "labels": "labels",
        "metadata": "metadata",
        "network": "network",
        "nic_type": "nicType",
        "reserved_ip_range": "reservedIpRange",
        "shielded_instance_config": "shieldedInstanceConfig",
        "subnet": "subnet",
        "tags": "tags",
    },
)
class GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig:
    def __init__(
        self,
        *,
        data_disk: typing.Union["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk", typing.Dict[str, typing.Any]],
        machine_type: builtins.str,
        accelerator_config: typing.Optional[typing.Union["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig", typing.Dict[str, typing.Any]]] = None,
        container_images: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages", typing.Dict[str, typing.Any]]]]] = None,
        encryption_config: typing.Optional[typing.Union["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig", typing.Dict[str, typing.Any]]] = None,
        internal_ip_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        network: typing.Optional[builtins.str] = None,
        nic_type: typing.Optional[builtins.str] = None,
        reserved_ip_range: typing.Optional[builtins.str] = None,
        shielded_instance_config: typing.Optional[typing.Union["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig", typing.Dict[str, typing.Any]]] = None,
        subnet: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param data_disk: data_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#data_disk GoogleNotebooksRuntime#data_disk}
        :param machine_type: The Compute Engine machine type used for runtimes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#machine_type GoogleNotebooksRuntime#machine_type}
        :param accelerator_config: accelerator_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#accelerator_config GoogleNotebooksRuntime#accelerator_config}
        :param container_images: container_images block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#container_images GoogleNotebooksRuntime#container_images}
        :param encryption_config: encryption_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#encryption_config GoogleNotebooksRuntime#encryption_config}
        :param internal_ip_only: If true, runtime will only have internal IP addresses. By default, runtimes are not restricted to internal IP addresses, and will have ephemeral external IP addresses assigned to each vm. This 'internal_ip_only' restriction can only be enabled for subnetwork enabled networks, and all dependencies must be configured to be accessible without external IP addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#internal_ip_only GoogleNotebooksRuntime#internal_ip_only}
        :param labels: The labels to associate with this runtime. Label **keys** must contain 1 to 63 characters, and must conform to [RFC 1035] (https://www.ietf.org/rfc/rfc1035.txt). Label **values** may be empty, but, if present, must contain 1 to 63 characters, and must conform to `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`_. No more than 32 labels can be associated with a cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#labels GoogleNotebooksRuntime#labels}
        :param metadata: The Compute Engine metadata entries to add to virtual machine. (see [Project and instance metadata](https://cloud.google.com /compute/docs/storing-retrieving-metadata#project_and_instance _metadata)). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#metadata GoogleNotebooksRuntime#metadata}
        :param network: The Compute Engine network to be used for machine communications. Cannot be specified with subnetwork. If neither 'network' nor 'subnet' is specified, the "default" network of the project is used, if it exists. A full URL or partial URI. Examples: 'https://www.googleapis.com/compute/v1/projects/[project_id]/ regions/global/default' 'projects/[project_id]/regions/global/default' Runtimes are managed resources inside Google Infrastructure. Runtimes support the following network configurations: Google Managed Network (Network & subnet are empty) Consumer Project VPC (network & subnet are required). Requires configuring Private Service Access. Shared VPC (network & subnet are required). Requires configuring Private Service Access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#network GoogleNotebooksRuntime#network}
        :param nic_type: The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet. Possible values: ["UNSPECIFIED_NIC_TYPE", "VIRTIO_NET", "GVNIC"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#nic_type GoogleNotebooksRuntime#nic_type}
        :param reserved_ip_range: Reserved IP Range name is used for VPC Peering. The subnetwork allocation will use the range *name* if it's assigned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#reserved_ip_range GoogleNotebooksRuntime#reserved_ip_range}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#shielded_instance_config GoogleNotebooksRuntime#shielded_instance_config}
        :param subnet: The Compute Engine subnetwork to be used for machine communications. Cannot be specified with network. A full URL or partial URI are valid. Examples: 'https://www.googleapis.com/compute/v1/projects/[project_id]/ regions/us-east1/subnetworks/sub0' 'projects/[project_id]/regions/us-east1/subnetworks/sub0' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#subnet GoogleNotebooksRuntime#subnet}
        :param tags: The Compute Engine tags to add to runtime (see [Tagging instances] (https://cloud.google.com/compute/docs/ label-or-tag-resources#tags)). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#tags GoogleNotebooksRuntime#tags}
        '''
        if isinstance(data_disk, dict):
            data_disk = GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk(**data_disk)
        if isinstance(accelerator_config, dict):
            accelerator_config = GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig(**accelerator_config)
        if isinstance(encryption_config, dict):
            encryption_config = GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig(**encryption_config)
        if isinstance(shielded_instance_config, dict):
            shielded_instance_config = GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig(**shielded_instance_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig.__init__)
            check_type(argname="argument data_disk", value=data_disk, expected_type=type_hints["data_disk"])
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            check_type(argname="argument accelerator_config", value=accelerator_config, expected_type=type_hints["accelerator_config"])
            check_type(argname="argument container_images", value=container_images, expected_type=type_hints["container_images"])
            check_type(argname="argument encryption_config", value=encryption_config, expected_type=type_hints["encryption_config"])
            check_type(argname="argument internal_ip_only", value=internal_ip_only, expected_type=type_hints["internal_ip_only"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument nic_type", value=nic_type, expected_type=type_hints["nic_type"])
            check_type(argname="argument reserved_ip_range", value=reserved_ip_range, expected_type=type_hints["reserved_ip_range"])
            check_type(argname="argument shielded_instance_config", value=shielded_instance_config, expected_type=type_hints["shielded_instance_config"])
            check_type(argname="argument subnet", value=subnet, expected_type=type_hints["subnet"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_disk": data_disk,
            "machine_type": machine_type,
        }
        if accelerator_config is not None:
            self._values["accelerator_config"] = accelerator_config
        if container_images is not None:
            self._values["container_images"] = container_images
        if encryption_config is not None:
            self._values["encryption_config"] = encryption_config
        if internal_ip_only is not None:
            self._values["internal_ip_only"] = internal_ip_only
        if labels is not None:
            self._values["labels"] = labels
        if metadata is not None:
            self._values["metadata"] = metadata
        if network is not None:
            self._values["network"] = network
        if nic_type is not None:
            self._values["nic_type"] = nic_type
        if reserved_ip_range is not None:
            self._values["reserved_ip_range"] = reserved_ip_range
        if shielded_instance_config is not None:
            self._values["shielded_instance_config"] = shielded_instance_config
        if subnet is not None:
            self._values["subnet"] = subnet
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data_disk(
        self,
    ) -> "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk":
        '''data_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#data_disk GoogleNotebooksRuntime#data_disk}
        '''
        result = self._values.get("data_disk")
        assert result is not None, "Required property 'data_disk' is missing"
        return typing.cast("GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk", result)

    @builtins.property
    def machine_type(self) -> builtins.str:
        '''The Compute Engine machine type used for runtimes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#machine_type GoogleNotebooksRuntime#machine_type}
        '''
        result = self._values.get("machine_type")
        assert result is not None, "Required property 'machine_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accelerator_config(
        self,
    ) -> typing.Optional["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig"]:
        '''accelerator_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#accelerator_config GoogleNotebooksRuntime#accelerator_config}
        '''
        result = self._values.get("accelerator_config")
        return typing.cast(typing.Optional["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig"], result)

    @builtins.property
    def container_images(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages"]]]:
        '''container_images block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#container_images GoogleNotebooksRuntime#container_images}
        '''
        result = self._values.get("container_images")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages"]]], result)

    @builtins.property
    def encryption_config(
        self,
    ) -> typing.Optional["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig"]:
        '''encryption_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#encryption_config GoogleNotebooksRuntime#encryption_config}
        '''
        result = self._values.get("encryption_config")
        return typing.cast(typing.Optional["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig"], result)

    @builtins.property
    def internal_ip_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, runtime will only have internal IP addresses.

        By default,
        runtimes are not restricted to internal IP addresses, and will
        have ephemeral external IP addresses assigned to each vm. This
        'internal_ip_only' restriction can only be enabled for subnetwork
        enabled networks, and all dependencies must be configured to be
        accessible without external IP addresses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#internal_ip_only GoogleNotebooksRuntime#internal_ip_only}
        '''
        result = self._values.get("internal_ip_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The labels to associate with this runtime.

        Label **keys** must
        contain 1 to 63 characters, and must conform to [RFC 1035]
        (https://www.ietf.org/rfc/rfc1035.txt). Label **values** may be
        empty, but, if present, must contain 1 to 63 characters, and must
        conform to `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`_. No
        more than 32 labels can be associated with a cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#labels GoogleNotebooksRuntime#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The Compute Engine metadata entries to add to virtual machine. (see [Project and instance metadata](https://cloud.google.com /compute/docs/storing-retrieving-metadata#project_and_instance _metadata)).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#metadata GoogleNotebooksRuntime#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''The Compute Engine network to be used for machine communications.

        Cannot be specified with subnetwork. If neither 'network' nor
        'subnet' is specified, the "default" network of the project is
        used, if it exists. A full URL or partial URI. Examples:
        'https://www.googleapis.com/compute/v1/projects/[project_id]/
        regions/global/default'
        'projects/[project_id]/regions/global/default'
        Runtimes are managed resources inside Google Infrastructure.
        Runtimes support the following network configurations:
        Google Managed Network (Network & subnet are empty)
        Consumer Project VPC (network & subnet are required). Requires
        configuring Private Service Access.
        Shared VPC (network & subnet are required). Requires
        configuring Private Service Access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#network GoogleNotebooksRuntime#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nic_type(self) -> typing.Optional[builtins.str]:
        '''The type of vNIC to be used on this interface.

        This may be gVNIC
        or VirtioNet. Possible values: ["UNSPECIFIED_NIC_TYPE", "VIRTIO_NET", "GVNIC"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#nic_type GoogleNotebooksRuntime#nic_type}
        '''
        result = self._values.get("nic_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reserved_ip_range(self) -> typing.Optional[builtins.str]:
        '''Reserved IP Range name is used for VPC Peering. The subnetwork allocation will use the range *name* if it's assigned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#reserved_ip_range GoogleNotebooksRuntime#reserved_ip_range}
        '''
        result = self._values.get("reserved_ip_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shielded_instance_config(
        self,
    ) -> typing.Optional["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig"]:
        '''shielded_instance_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#shielded_instance_config GoogleNotebooksRuntime#shielded_instance_config}
        '''
        result = self._values.get("shielded_instance_config")
        return typing.cast(typing.Optional["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig"], result)

    @builtins.property
    def subnet(self) -> typing.Optional[builtins.str]:
        '''The Compute Engine subnetwork to be used for machine communications.

        Cannot be specified with network. A full URL or
        partial URI are valid. Examples:
        'https://www.googleapis.com/compute/v1/projects/[project_id]/
        regions/us-east1/subnetworks/sub0'
        'projects/[project_id]/regions/us-east1/subnetworks/sub0'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#subnet GoogleNotebooksRuntime#subnet}
        '''
        result = self._values.get("subnet")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Compute Engine tags to add to runtime (see [Tagging instances] (https://cloud.google.com/compute/docs/ label-or-tag-resources#tags)).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#tags GoogleNotebooksRuntime#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig",
    jsii_struct_bases=[],
    name_mapping={"core_count": "coreCount", "type": "type"},
)
class GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig:
    def __init__(
        self,
        *,
        core_count: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param core_count: Count of cores of this accelerator. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#core_count GoogleNotebooksRuntime#core_count}
        :param type: Accelerator model. For valid values, see 'https://cloud.google.com/vertex-ai/docs/workbench/reference/ rest/v1/projects.locations.runtimes#AcceleratorType'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#type GoogleNotebooksRuntime#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig.__init__)
            check_type(argname="argument core_count", value=core_count, expected_type=type_hints["core_count"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if core_count is not None:
            self._values["core_count"] = core_count
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def core_count(self) -> typing.Optional[jsii.Number]:
        '''Count of cores of this accelerator.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#core_count GoogleNotebooksRuntime#core_count}
        '''
        result = self._values.get("core_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Accelerator model. For valid values, see 'https://cloud.google.com/vertex-ai/docs/workbench/reference/ rest/v1/projects.locations.runtimes#AcceleratorType'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#type GoogleNotebooksRuntime#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCoreCount")
    def reset_core_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreCount", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="coreCountInput")
    def core_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "coreCountInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="coreCount")
    def core_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "coreCount"))

    @core_count.setter
    def core_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfigOutputReference, "core_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreCount", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfigOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig]:
        return typing.cast(typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages",
    jsii_struct_bases=[],
    name_mapping={"repository": "repository", "tag": "tag"},
)
class GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages:
    def __init__(
        self,
        *,
        repository: builtins.str,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param repository: The path to the container image repository. For example: gcr.io/{project_id}/{imageName}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#repository GoogleNotebooksRuntime#repository}
        :param tag: The tag of the container image. If not specified, this defaults to the latest tag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#tag GoogleNotebooksRuntime#tag}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages.__init__)
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[str, typing.Any] = {
            "repository": repository,
        }
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def repository(self) -> builtins.str:
        '''The path to the container image repository. For example: gcr.io/{project_id}/{imageName}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#repository GoogleNotebooksRuntime#repository}
        '''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The tag of the container image. If not specified, this defaults to the latest tag.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#tag GoogleNotebooksRuntime#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesList",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @builtins.property
    @jsii.member(jsii_name="repositoryInput")
    def repository_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repository"))

    @repository.setter
    def repository(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesOutputReference, "repository").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repository", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesOutputReference, "tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk",
    jsii_struct_bases=[],
    name_mapping={
        "initialize_params": "initializeParams",
        "interface": "interface",
        "mode": "mode",
        "source": "source",
        "type": "type",
    },
)
class GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk:
    def __init__(
        self,
        *,
        initialize_params: typing.Optional[typing.Union["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams", typing.Dict[str, typing.Any]]] = None,
        interface: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param initialize_params: initialize_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#initialize_params GoogleNotebooksRuntime#initialize_params}
        :param interface: "Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME. The default is SCSI. Persistent disks must always use SCSI and the request will fail if you attempt to attach a persistent disk in any other format than SCSI. Local SSDs can use either NVME or SCSI. For performance characteristics of SCSI over NVMe, see Local SSD performance. Valid values: * NVME * SCSI". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#interface GoogleNotebooksRuntime#interface}
        :param mode: The mode in which to attach this disk, either READ_WRITE or READ_ONLY. If not specified, the default is to attach the disk in READ_WRITE mode. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#mode GoogleNotebooksRuntime#mode}
        :param source: Specifies a valid partial or full URL to an existing Persistent Disk resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#source GoogleNotebooksRuntime#source}
        :param type: Specifies the type of the disk, either SCRATCH or PERSISTENT. If not specified, the default is PERSISTENT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#type GoogleNotebooksRuntime#type}
        '''
        if isinstance(initialize_params, dict):
            initialize_params = GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams(**initialize_params)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk.__init__)
            check_type(argname="argument initialize_params", value=initialize_params, expected_type=type_hints["initialize_params"])
            check_type(argname="argument interface", value=interface, expected_type=type_hints["interface"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if initialize_params is not None:
            self._values["initialize_params"] = initialize_params
        if interface is not None:
            self._values["interface"] = interface
        if mode is not None:
            self._values["mode"] = mode
        if source is not None:
            self._values["source"] = source
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def initialize_params(
        self,
    ) -> typing.Optional["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams"]:
        '''initialize_params block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#initialize_params GoogleNotebooksRuntime#initialize_params}
        '''
        result = self._values.get("initialize_params")
        return typing.cast(typing.Optional["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams"], result)

    @builtins.property
    def interface(self) -> typing.Optional[builtins.str]:
        '''"Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME.

        The default is SCSI. Persistent
        disks must always use SCSI and the request will fail if you attempt
        to attach a persistent disk in any other format than SCSI. Local SSDs
        can use either NVME or SCSI. For performance characteristics of SCSI
        over NVMe, see Local SSD performance. Valid values: * NVME * SCSI".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#interface GoogleNotebooksRuntime#interface}
        '''
        result = self._values.get("interface")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''The mode in which to attach this disk, either READ_WRITE or READ_ONLY.

        If not specified, the default is to attach
        the disk in READ_WRITE mode.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#mode GoogleNotebooksRuntime#mode}
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Specifies a valid partial or full URL to an existing Persistent Disk resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#source GoogleNotebooksRuntime#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of the disk, either SCRATCH or PERSISTENT. If not specified, the default is PERSISTENT.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#type GoogleNotebooksRuntime#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "disk_name": "diskName",
        "disk_size_gb": "diskSizeGb",
        "disk_type": "diskType",
        "labels": "labels",
    },
)
class GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        disk_name: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        disk_type: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param description: Provide this property when creating the disk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#description GoogleNotebooksRuntime#description}
        :param disk_name: Specifies the disk name. If not specified, the default is to use the name of the instance. If the disk with the instance name exists already in the given zone/region, a new name will be automatically generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#disk_name GoogleNotebooksRuntime#disk_name}
        :param disk_size_gb: Specifies the size of the disk in base-2 GB. If not specified, the disk will be the same size as the image (usually 10GB). If specified, the size must be equal to or larger than 10GB. Default 100 GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#disk_size_gb GoogleNotebooksRuntime#disk_size_gb}
        :param disk_type: The type of the boot disk attached to this runtime, defaults to standard persistent disk. For valid values, see 'https://cloud.google.com/vertex-ai/docs/workbench/ reference/rest/v1/projects.locations.runtimes#disktype'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#disk_type GoogleNotebooksRuntime#disk_type}
        :param labels: Labels to apply to this disk. These can be later modified by the disks.setLabels method. This field is only applicable for persistent disks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#labels GoogleNotebooksRuntime#labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disk_name", value=disk_name, expected_type=type_hints["disk_name"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument disk_type", value=disk_type, expected_type=type_hints["disk_type"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if disk_name is not None:
            self._values["disk_name"] = disk_name
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if disk_type is not None:
            self._values["disk_type"] = disk_type
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Provide this property when creating the disk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#description GoogleNotebooksRuntime#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the disk name.

        If not specified, the default is
        to use the name of the instance. If the disk with the
        instance name exists already in the given zone/region, a
        new name will be automatically generated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#disk_name GoogleNotebooksRuntime#disk_name}
        '''
        result = self._values.get("disk_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Specifies the size of the disk in base-2 GB.

        If not
        specified, the disk will be the same size as the image
        (usually 10GB). If specified, the size must be equal to
        or larger than 10GB. Default 100 GB.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#disk_size_gb GoogleNotebooksRuntime#disk_size_gb}
        '''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_type(self) -> typing.Optional[builtins.str]:
        '''The type of the boot disk attached to this runtime, defaults to standard persistent disk. For valid values, see 'https://cloud.google.com/vertex-ai/docs/workbench/ reference/rest/v1/projects.locations.runtimes#disktype'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#disk_type GoogleNotebooksRuntime#disk_type}
        '''
        result = self._values.get("disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels to apply to this disk.

        These can be later modified
        by the disks.setLabels method. This field is only
        applicable for persistent disks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#labels GoogleNotebooksRuntime#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDiskName")
    def reset_disk_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskName", []))

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetDiskType")
    def reset_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskType", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="diskNameInput")
    def disk_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskNameInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="diskTypeInput")
    def disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="diskName")
    def disk_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskName"))

    @disk_name.setter
    def disk_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsOutputReference, "disk_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskName", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsOutputReference, "disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="diskType")
    def disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskType"))

    @disk_type.setter
    def disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsOutputReference, "disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskType", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams]:
        return typing.cast(typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskOutputReference",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInitializeParams")
    def put_initialize_params(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        disk_name: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        disk_type: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param description: Provide this property when creating the disk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#description GoogleNotebooksRuntime#description}
        :param disk_name: Specifies the disk name. If not specified, the default is to use the name of the instance. If the disk with the instance name exists already in the given zone/region, a new name will be automatically generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#disk_name GoogleNotebooksRuntime#disk_name}
        :param disk_size_gb: Specifies the size of the disk in base-2 GB. If not specified, the disk will be the same size as the image (usually 10GB). If specified, the size must be equal to or larger than 10GB. Default 100 GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#disk_size_gb GoogleNotebooksRuntime#disk_size_gb}
        :param disk_type: The type of the boot disk attached to this runtime, defaults to standard persistent disk. For valid values, see 'https://cloud.google.com/vertex-ai/docs/workbench/ reference/rest/v1/projects.locations.runtimes#disktype'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#disk_type GoogleNotebooksRuntime#disk_type}
        :param labels: Labels to apply to this disk. These can be later modified by the disks.setLabels method. This field is only applicable for persistent disks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#labels GoogleNotebooksRuntime#labels}
        '''
        value = GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams(
            description=description,
            disk_name=disk_name,
            disk_size_gb=disk_size_gb,
            disk_type=disk_type,
            labels=labels,
        )

        return typing.cast(None, jsii.invoke(self, "putInitializeParams", [value]))

    @jsii.member(jsii_name="resetInitializeParams")
    def reset_initialize_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitializeParams", []))

    @jsii.member(jsii_name="resetInterface")
    def reset_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterface", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="autoDelete")
    def auto_delete(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "autoDelete"))

    @builtins.property
    @jsii.member(jsii_name="boot")
    def boot(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "boot"))

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @builtins.property
    @jsii.member(jsii_name="guestOsFeatures")
    def guest_os_features(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "guestOsFeatures"))

    @builtins.property
    @jsii.member(jsii_name="index")
    def index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "index"))

    @builtins.property
    @jsii.member(jsii_name="initializeParams")
    def initialize_params(
        self,
    ) -> GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsOutputReference:
        return typing.cast(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsOutputReference, jsii.get(self, "initializeParams"))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="licenses")
    def licenses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "licenses"))

    @builtins.property
    @jsii.member(jsii_name="initializeParamsInput")
    def initialize_params_input(
        self,
    ) -> typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams]:
        return typing.cast(typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams], jsii.get(self, "initializeParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="interfaceInput")
    def interface_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="interface")
    def interface(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interface"))

    @interface.setter
    def interface(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskOutputReference, "interface").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interface", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk]:
        return typing.cast(typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig",
    jsii_struct_bases=[],
    name_mapping={"kms_key": "kmsKey"},
)
class GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig:
    def __init__(self, *, kms_key: typing.Optional[builtins.str] = None) -> None:
        '''
        :param kms_key: The Cloud KMS resource identifier of the customer-managed encryption key used to protect a resource, such as a disks. It has the following format: 'projects/{PROJECT_ID}/locations/{REGION}/keyRings/ {KEY_RING_NAME}/cryptoKeys/{KEY_NAME}' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#kms_key GoogleNotebooksRuntime#kms_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig.__init__)
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
        self._values: typing.Dict[str, typing.Any] = {}
        if kms_key is not None:
            self._values["kms_key"] = kms_key

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''The Cloud KMS resource identifier of the customer-managed encryption key used to protect a resource, such as a disks.

        It has the following format:
        'projects/{PROJECT_ID}/locations/{REGION}/keyRings/
        {KEY_RING_NAME}/cryptoKeys/{KEY_NAME}'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#kms_key GoogleNotebooksRuntime#kms_key}
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKmsKey")
    def reset_kms_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKey", []))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyInput")
    def kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfigOutputReference, "kms_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig]:
        return typing.cast(typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAcceleratorConfig")
    def put_accelerator_config(
        self,
        *,
        core_count: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param core_count: Count of cores of this accelerator. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#core_count GoogleNotebooksRuntime#core_count}
        :param type: Accelerator model. For valid values, see 'https://cloud.google.com/vertex-ai/docs/workbench/reference/ rest/v1/projects.locations.runtimes#AcceleratorType'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#type GoogleNotebooksRuntime#type}
        '''
        value = GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig(
            core_count=core_count, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putAcceleratorConfig", [value]))

    @jsii.member(jsii_name="putContainerImages")
    def put_container_images(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference.put_container_images)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putContainerImages", [value]))

    @jsii.member(jsii_name="putDataDisk")
    def put_data_disk(
        self,
        *,
        initialize_params: typing.Optional[typing.Union[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams, typing.Dict[str, typing.Any]]] = None,
        interface: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param initialize_params: initialize_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#initialize_params GoogleNotebooksRuntime#initialize_params}
        :param interface: "Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME. The default is SCSI. Persistent disks must always use SCSI and the request will fail if you attempt to attach a persistent disk in any other format than SCSI. Local SSDs can use either NVME or SCSI. For performance characteristics of SCSI over NVMe, see Local SSD performance. Valid values: * NVME * SCSI". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#interface GoogleNotebooksRuntime#interface}
        :param mode: The mode in which to attach this disk, either READ_WRITE or READ_ONLY. If not specified, the default is to attach the disk in READ_WRITE mode. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#mode GoogleNotebooksRuntime#mode}
        :param source: Specifies a valid partial or full URL to an existing Persistent Disk resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#source GoogleNotebooksRuntime#source}
        :param type: Specifies the type of the disk, either SCRATCH or PERSISTENT. If not specified, the default is PERSISTENT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#type GoogleNotebooksRuntime#type}
        '''
        value = GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk(
            initialize_params=initialize_params,
            interface=interface,
            mode=mode,
            source=source,
            type=type,
        )

        return typing.cast(None, jsii.invoke(self, "putDataDisk", [value]))

    @jsii.member(jsii_name="putEncryptionConfig")
    def put_encryption_config(
        self,
        *,
        kms_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key: The Cloud KMS resource identifier of the customer-managed encryption key used to protect a resource, such as a disks. It has the following format: 'projects/{PROJECT_ID}/locations/{REGION}/keyRings/ {KEY_RING_NAME}/cryptoKeys/{KEY_NAME}' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#kms_key GoogleNotebooksRuntime#kms_key}
        '''
        value = GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig(
            kms_key=kms_key
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptionConfig", [value]))

    @jsii.member(jsii_name="putShieldedInstanceConfig")
    def put_shielded_instance_config(
        self,
        *,
        enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_secure_boot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_vtpm: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_integrity_monitoring: Defines whether the instance has integrity monitoring enabled. Enables monitoring and attestation of the boot integrity of the instance. The attestation is performed against the integrity policy baseline. This baseline is initially derived from the implicitly trusted boot image when the instance is created. Enabled by default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#enable_integrity_monitoring GoogleNotebooksRuntime#enable_integrity_monitoring}
        :param enable_secure_boot: Defines whether the instance has Secure Boot enabled.Secure Boot helps ensure that the system only runs authentic software by verifying the digital signature of all boot components, and halting the boot process if signature verification fails. Disabled by default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#enable_secure_boot GoogleNotebooksRuntime#enable_secure_boot}
        :param enable_vtpm: Defines whether the instance has the vTPM enabled. Enabled by default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#enable_vtpm GoogleNotebooksRuntime#enable_vtpm}
        '''
        value = GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig(
            enable_integrity_monitoring=enable_integrity_monitoring,
            enable_secure_boot=enable_secure_boot,
            enable_vtpm=enable_vtpm,
        )

        return typing.cast(None, jsii.invoke(self, "putShieldedInstanceConfig", [value]))

    @jsii.member(jsii_name="resetAcceleratorConfig")
    def reset_accelerator_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorConfig", []))

    @jsii.member(jsii_name="resetContainerImages")
    def reset_container_images(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerImages", []))

    @jsii.member(jsii_name="resetEncryptionConfig")
    def reset_encryption_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionConfig", []))

    @jsii.member(jsii_name="resetInternalIpOnly")
    def reset_internal_ip_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternalIpOnly", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetNicType")
    def reset_nic_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNicType", []))

    @jsii.member(jsii_name="resetReservedIpRange")
    def reset_reserved_ip_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReservedIpRange", []))

    @jsii.member(jsii_name="resetShieldedInstanceConfig")
    def reset_shielded_instance_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShieldedInstanceConfig", []))

    @jsii.member(jsii_name="resetSubnet")
    def reset_subnet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnet", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="acceleratorConfig")
    def accelerator_config(
        self,
    ) -> GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfigOutputReference:
        return typing.cast(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfigOutputReference, jsii.get(self, "acceleratorConfig"))

    @builtins.property
    @jsii.member(jsii_name="containerImages")
    def container_images(
        self,
    ) -> GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesList:
        return typing.cast(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesList, jsii.get(self, "containerImages"))

    @builtins.property
    @jsii.member(jsii_name="dataDisk")
    def data_disk(
        self,
    ) -> GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskOutputReference:
        return typing.cast(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskOutputReference, jsii.get(self, "dataDisk"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfig")
    def encryption_config(
        self,
    ) -> GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfigOutputReference:
        return typing.cast(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfigOutputReference, jsii.get(self, "encryptionConfig"))

    @builtins.property
    @jsii.member(jsii_name="guestAttributes")
    def guest_attributes(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "guestAttributes"))

    @builtins.property
    @jsii.member(jsii_name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigOutputReference":
        return typing.cast("GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigOutputReference", jsii.get(self, "shieldedInstanceConfig"))

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorConfigInput")
    def accelerator_config_input(
        self,
    ) -> typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig]:
        return typing.cast(typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig], jsii.get(self, "acceleratorConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="containerImagesInput")
    def container_images_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages]]], jsii.get(self, "containerImagesInput"))

    @builtins.property
    @jsii.member(jsii_name="dataDiskInput")
    def data_disk_input(
        self,
    ) -> typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk]:
        return typing.cast(typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk], jsii.get(self, "dataDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfigInput")
    def encryption_config_input(
        self,
    ) -> typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig]:
        return typing.cast(typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig], jsii.get(self, "encryptionConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalIpOnlyInput")
    def internal_ip_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "internalIpOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="nicTypeInput")
    def nic_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nicTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="reservedIpRangeInput")
    def reserved_ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reservedIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="shieldedInstanceConfigInput")
    def shielded_instance_config_input(
        self,
    ) -> typing.Optional["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig"]:
        return typing.cast(typing.Optional["GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig"], jsii.get(self, "shieldedInstanceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetInput")
    def subnet_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalIpOnly")
    def internal_ip_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "internalIpOnly"))

    @internal_ip_only.setter
    def internal_ip_only(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference, "internal_ip_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalIpOnly", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference, "metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="nicType")
    def nic_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nicType"))

    @nic_type.setter
    def nic_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference, "nic_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nicType", value)

    @builtins.property
    @jsii.member(jsii_name="reservedIpRange")
    def reserved_ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reservedIpRange"))

    @reserved_ip_range.setter
    def reserved_ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference, "reserved_ip_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reservedIpRange", value)

    @builtins.property
    @jsii.member(jsii_name="subnet")
    def subnet(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnet"))

    @subnet.setter
    def subnet(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference, "subnet").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnet", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig]:
        return typing.cast(typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "enable_integrity_monitoring": "enableIntegrityMonitoring",
        "enable_secure_boot": "enableSecureBoot",
        "enable_vtpm": "enableVtpm",
    },
)
class GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig:
    def __init__(
        self,
        *,
        enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_secure_boot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_vtpm: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_integrity_monitoring: Defines whether the instance has integrity monitoring enabled. Enables monitoring and attestation of the boot integrity of the instance. The attestation is performed against the integrity policy baseline. This baseline is initially derived from the implicitly trusted boot image when the instance is created. Enabled by default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#enable_integrity_monitoring GoogleNotebooksRuntime#enable_integrity_monitoring}
        :param enable_secure_boot: Defines whether the instance has Secure Boot enabled.Secure Boot helps ensure that the system only runs authentic software by verifying the digital signature of all boot components, and halting the boot process if signature verification fails. Disabled by default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#enable_secure_boot GoogleNotebooksRuntime#enable_secure_boot}
        :param enable_vtpm: Defines whether the instance has the vTPM enabled. Enabled by default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#enable_vtpm GoogleNotebooksRuntime#enable_vtpm}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig.__init__)
            check_type(argname="argument enable_integrity_monitoring", value=enable_integrity_monitoring, expected_type=type_hints["enable_integrity_monitoring"])
            check_type(argname="argument enable_secure_boot", value=enable_secure_boot, expected_type=type_hints["enable_secure_boot"])
            check_type(argname="argument enable_vtpm", value=enable_vtpm, expected_type=type_hints["enable_vtpm"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enable_integrity_monitoring is not None:
            self._values["enable_integrity_monitoring"] = enable_integrity_monitoring
        if enable_secure_boot is not None:
            self._values["enable_secure_boot"] = enable_secure_boot
        if enable_vtpm is not None:
            self._values["enable_vtpm"] = enable_vtpm

    @builtins.property
    def enable_integrity_monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defines whether the instance has integrity monitoring enabled.

        Enables monitoring and attestation of the boot integrity of
        the instance. The attestation is performed against the
        integrity policy baseline. This baseline is initially derived
        from the implicitly trusted boot image when the instance is
        created. Enabled by default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#enable_integrity_monitoring GoogleNotebooksRuntime#enable_integrity_monitoring}
        '''
        result = self._values.get("enable_integrity_monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_secure_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defines whether the instance has Secure Boot enabled.Secure Boot helps ensure that the system only runs authentic software by verifying the digital signature of all boot components, and halting the boot process if signature verification fails. Disabled by default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#enable_secure_boot GoogleNotebooksRuntime#enable_secure_boot}
        '''
        result = self._values.get("enable_secure_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_vtpm(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defines whether the instance has the vTPM enabled. Enabled by default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_notebooks_runtime#enable_vtpm GoogleNotebooksRuntime#enable_vtpm}
        '''
        result = self._values.get("enable_vtpm")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNotebooksRuntime.GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableIntegrityMonitoring")
    def reset_enable_integrity_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableIntegrityMonitoring", []))

    @jsii.member(jsii_name="resetEnableSecureBoot")
    def reset_enable_secure_boot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableSecureBoot", []))

    @jsii.member(jsii_name="resetEnableVtpm")
    def reset_enable_vtpm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableVtpm", []))

    @builtins.property
    @jsii.member(jsii_name="enableIntegrityMonitoringInput")
    def enable_integrity_monitoring_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableIntegrityMonitoringInput"))

    @builtins.property
    @jsii.member(jsii_name="enableSecureBootInput")
    def enable_secure_boot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableSecureBootInput"))

    @builtins.property
    @jsii.member(jsii_name="enableVtpmInput")
    def enable_vtpm_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableVtpmInput"))

    @builtins.property
    @jsii.member(jsii_name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableIntegrityMonitoring"))

    @enable_integrity_monitoring.setter
    def enable_integrity_monitoring(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigOutputReference, "enable_integrity_monitoring").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIntegrityMonitoring", value)

    @builtins.property
    @jsii.member(jsii_name="enableSecureBoot")
    def enable_secure_boot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableSecureBoot"))

    @enable_secure_boot.setter
    def enable_secure_boot(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigOutputReference, "enable_secure_boot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSecureBoot", value)

    @builtins.property
    @jsii.member(jsii_name="enableVtpm")
    def enable_vtpm(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableVtpm"))

    @enable_vtpm.setter
    def enable_vtpm(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigOutputReference, "enable_vtpm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableVtpm", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig]:
        return typing.cast(typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleNotebooksRuntime",
    "GoogleNotebooksRuntimeAccessConfig",
    "GoogleNotebooksRuntimeAccessConfigOutputReference",
    "GoogleNotebooksRuntimeConfig",
    "GoogleNotebooksRuntimeMetrics",
    "GoogleNotebooksRuntimeMetricsList",
    "GoogleNotebooksRuntimeMetricsOutputReference",
    "GoogleNotebooksRuntimeSoftwareConfig",
    "GoogleNotebooksRuntimeSoftwareConfigKernels",
    "GoogleNotebooksRuntimeSoftwareConfigKernelsList",
    "GoogleNotebooksRuntimeSoftwareConfigKernelsOutputReference",
    "GoogleNotebooksRuntimeSoftwareConfigOutputReference",
    "GoogleNotebooksRuntimeTimeouts",
    "GoogleNotebooksRuntimeTimeoutsOutputReference",
    "GoogleNotebooksRuntimeVirtualMachine",
    "GoogleNotebooksRuntimeVirtualMachineOutputReference",
    "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfig",
    "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig",
    "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigAcceleratorConfigOutputReference",
    "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImages",
    "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesList",
    "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigContainerImagesOutputReference",
    "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDisk",
    "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams",
    "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsOutputReference",
    "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigDataDiskOutputReference",
    "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfig",
    "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigEncryptionConfigOutputReference",
    "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigOutputReference",
    "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig",
    "GoogleNotebooksRuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigOutputReference",
]

publication.publish()
