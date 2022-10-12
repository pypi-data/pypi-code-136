'''
# `google_data_fusion_instance`

Refer to the Terraform Registory for docs: [`google_data_fusion_instance`](https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance).
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


class GoogleDataFusionInstance(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataFusionInstance.GoogleDataFusionInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance google_data_fusion_instance}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        dataproc_service_account: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        enable_stackdriver_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_stackdriver_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        network_config: typing.Optional[typing.Union["GoogleDataFusionInstanceNetworkConfig", typing.Dict[str, typing.Any]]] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        private_instance: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataFusionInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance google_data_fusion_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The ID of the instance or a fully qualified identifier for the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#name GoogleDataFusionInstance#name}
        :param type: Represents the type of Data Fusion instance. Each type is configured with the default settings for processing and memory. - BASIC: Basic Data Fusion instance. In Basic type, the user will be able to create data pipelines using point and click UI. However, there are certain limitations, such as fewer number of concurrent pipelines, no support for streaming pipelines, etc. - ENTERPRISE: Enterprise Data Fusion instance. In Enterprise type, the user will have more features available, such as support for streaming pipelines, higher number of concurrent pipelines, etc. - DEVELOPER: Developer Data Fusion instance. In Developer type, the user will have all features available but with restrictive capabilities. This is to help enterprises design and develop their data ingestion and integration pipelines at low cost. Possible values: ["BASIC", "ENTERPRISE", "DEVELOPER"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#type GoogleDataFusionInstance#type}
        :param dataproc_service_account: User-managed service account to set on Dataproc when Cloud Data Fusion creates Dataproc to run data processing pipelines. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#dataproc_service_account GoogleDataFusionInstance#dataproc_service_account}
        :param description: An optional description of the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#description GoogleDataFusionInstance#description}
        :param enable_stackdriver_logging: Option to enable Stackdriver Logging. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#enable_stackdriver_logging GoogleDataFusionInstance#enable_stackdriver_logging}
        :param enable_stackdriver_monitoring: Option to enable Stackdriver Monitoring. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#enable_stackdriver_monitoring GoogleDataFusionInstance#enable_stackdriver_monitoring}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#id GoogleDataFusionInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: The resource labels for instance to use to annotate any related underlying resources, such as Compute Engine VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#labels GoogleDataFusionInstance#labels}
        :param network_config: network_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#network_config GoogleDataFusionInstance#network_config}
        :param options: Map of additional options used to configure the behavior of Data Fusion instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#options GoogleDataFusionInstance#options}
        :param private_instance: Specifies whether the Data Fusion instance should be private. If set to true, all Data Fusion nodes will have private IP addresses and will not be able to access the public internet. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#private_instance GoogleDataFusionInstance#private_instance}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#project GoogleDataFusionInstance#project}.
        :param region: The region of the Data Fusion instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#region GoogleDataFusionInstance#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#timeouts GoogleDataFusionInstance#timeouts}
        :param version: Current version of the Data Fusion. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#version GoogleDataFusionInstance#version}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataFusionInstance.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDataFusionInstanceConfig(
            name=name,
            type=type,
            dataproc_service_account=dataproc_service_account,
            description=description,
            enable_stackdriver_logging=enable_stackdriver_logging,
            enable_stackdriver_monitoring=enable_stackdriver_monitoring,
            id=id,
            labels=labels,
            network_config=network_config,
            options=options,
            private_instance=private_instance,
            project=project,
            region=region,
            timeouts=timeouts,
            version=version,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putNetworkConfig")
    def put_network_config(
        self,
        *,
        ip_allocation: builtins.str,
        network: builtins.str,
    ) -> None:
        '''
        :param ip_allocation: The IP range in CIDR notation to use for the managed Data Fusion instance nodes. This range must not overlap with any other ranges used in the Data Fusion instance network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#ip_allocation GoogleDataFusionInstance#ip_allocation}
        :param network: Name of the network in the project with which the tenant project will be peered for executing pipelines. In case of shared VPC where the network resides in another host project the network should specified in the form of projects/{host-project-id}/global/networks/{network} Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#network GoogleDataFusionInstance#network}
        '''
        value = GoogleDataFusionInstanceNetworkConfig(
            ip_allocation=ip_allocation, network=network
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#create GoogleDataFusionInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#delete GoogleDataFusionInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#update GoogleDataFusionInstance#update}.
        '''
        value = GoogleDataFusionInstanceTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDataprocServiceAccount")
    def reset_dataproc_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataprocServiceAccount", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnableStackdriverLogging")
    def reset_enable_stackdriver_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableStackdriverLogging", []))

    @jsii.member(jsii_name="resetEnableStackdriverMonitoring")
    def reset_enable_stackdriver_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableStackdriverMonitoring", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetNetworkConfig")
    def reset_network_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkConfig", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetPrivateInstance")
    def reset_private_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateInstance", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="gcsBucket")
    def gcs_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gcsBucket"))

    @builtins.property
    @jsii.member(jsii_name="networkConfig")
    def network_config(self) -> "GoogleDataFusionInstanceNetworkConfigOutputReference":
        return typing.cast("GoogleDataFusionInstanceNetworkConfigOutputReference", jsii.get(self, "networkConfig"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccount"))

    @builtins.property
    @jsii.member(jsii_name="serviceEndpoint")
    def service_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="stateMessage")
    def state_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateMessage"))

    @builtins.property
    @jsii.member(jsii_name="tenantProjectId")
    def tenant_project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantProjectId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleDataFusionInstanceTimeoutsOutputReference":
        return typing.cast("GoogleDataFusionInstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="dataprocServiceAccountInput")
    def dataproc_service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataprocServiceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enableStackdriverLoggingInput")
    def enable_stackdriver_logging_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableStackdriverLoggingInput"))

    @builtins.property
    @jsii.member(jsii_name="enableStackdriverMonitoringInput")
    def enable_stackdriver_monitoring_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableStackdriverMonitoringInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkConfigInput")
    def network_config_input(
        self,
    ) -> typing.Optional["GoogleDataFusionInstanceNetworkConfig"]:
        return typing.cast(typing.Optional["GoogleDataFusionInstanceNetworkConfig"], jsii.get(self, "networkConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="privateInstanceInput")
    def private_instance_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "privateInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleDataFusionInstanceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleDataFusionInstanceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="dataprocServiceAccount")
    def dataproc_service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataprocServiceAccount"))

    @dataproc_service_account.setter
    def dataproc_service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstance, "dataproc_service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataprocServiceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstance, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enableStackdriverLogging")
    def enable_stackdriver_logging(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableStackdriverLogging"))

    @enable_stackdriver_logging.setter
    def enable_stackdriver_logging(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstance, "enable_stackdriver_logging").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableStackdriverLogging", value)

    @builtins.property
    @jsii.member(jsii_name="enableStackdriverMonitoring")
    def enable_stackdriver_monitoring(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableStackdriverMonitoring"))

    @enable_stackdriver_monitoring.setter
    def enable_stackdriver_monitoring(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstance, "enable_stackdriver_monitoring").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableStackdriverMonitoring", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstance, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstance, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstance, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstance, "options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property
    @jsii.member(jsii_name="privateInstance")
    def private_instance(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "privateInstance"))

    @private_instance.setter
    def private_instance(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstance, "private_instance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateInstance", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstance, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstance, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstance, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstance, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataFusionInstance.GoogleDataFusionInstanceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "type": "type",
        "dataproc_service_account": "dataprocServiceAccount",
        "description": "description",
        "enable_stackdriver_logging": "enableStackdriverLogging",
        "enable_stackdriver_monitoring": "enableStackdriverMonitoring",
        "id": "id",
        "labels": "labels",
        "network_config": "networkConfig",
        "options": "options",
        "private_instance": "privateInstance",
        "project": "project",
        "region": "region",
        "timeouts": "timeouts",
        "version": "version",
    },
)
class GoogleDataFusionInstanceConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        type: builtins.str,
        dataproc_service_account: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        enable_stackdriver_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_stackdriver_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        network_config: typing.Optional[typing.Union["GoogleDataFusionInstanceNetworkConfig", typing.Dict[str, typing.Any]]] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        private_instance: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataFusionInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The ID of the instance or a fully qualified identifier for the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#name GoogleDataFusionInstance#name}
        :param type: Represents the type of Data Fusion instance. Each type is configured with the default settings for processing and memory. - BASIC: Basic Data Fusion instance. In Basic type, the user will be able to create data pipelines using point and click UI. However, there are certain limitations, such as fewer number of concurrent pipelines, no support for streaming pipelines, etc. - ENTERPRISE: Enterprise Data Fusion instance. In Enterprise type, the user will have more features available, such as support for streaming pipelines, higher number of concurrent pipelines, etc. - DEVELOPER: Developer Data Fusion instance. In Developer type, the user will have all features available but with restrictive capabilities. This is to help enterprises design and develop their data ingestion and integration pipelines at low cost. Possible values: ["BASIC", "ENTERPRISE", "DEVELOPER"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#type GoogleDataFusionInstance#type}
        :param dataproc_service_account: User-managed service account to set on Dataproc when Cloud Data Fusion creates Dataproc to run data processing pipelines. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#dataproc_service_account GoogleDataFusionInstance#dataproc_service_account}
        :param description: An optional description of the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#description GoogleDataFusionInstance#description}
        :param enable_stackdriver_logging: Option to enable Stackdriver Logging. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#enable_stackdriver_logging GoogleDataFusionInstance#enable_stackdriver_logging}
        :param enable_stackdriver_monitoring: Option to enable Stackdriver Monitoring. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#enable_stackdriver_monitoring GoogleDataFusionInstance#enable_stackdriver_monitoring}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#id GoogleDataFusionInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: The resource labels for instance to use to annotate any related underlying resources, such as Compute Engine VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#labels GoogleDataFusionInstance#labels}
        :param network_config: network_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#network_config GoogleDataFusionInstance#network_config}
        :param options: Map of additional options used to configure the behavior of Data Fusion instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#options GoogleDataFusionInstance#options}
        :param private_instance: Specifies whether the Data Fusion instance should be private. If set to true, all Data Fusion nodes will have private IP addresses and will not be able to access the public internet. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#private_instance GoogleDataFusionInstance#private_instance}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#project GoogleDataFusionInstance#project}.
        :param region: The region of the Data Fusion instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#region GoogleDataFusionInstance#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#timeouts GoogleDataFusionInstance#timeouts}
        :param version: Current version of the Data Fusion. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#version GoogleDataFusionInstance#version}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(network_config, dict):
            network_config = GoogleDataFusionInstanceNetworkConfig(**network_config)
        if isinstance(timeouts, dict):
            timeouts = GoogleDataFusionInstanceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataFusionInstanceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument dataproc_service_account", value=dataproc_service_account, expected_type=type_hints["dataproc_service_account"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enable_stackdriver_logging", value=enable_stackdriver_logging, expected_type=type_hints["enable_stackdriver_logging"])
            check_type(argname="argument enable_stackdriver_monitoring", value=enable_stackdriver_monitoring, expected_type=type_hints["enable_stackdriver_monitoring"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument network_config", value=network_config, expected_type=type_hints["network_config"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument private_instance", value=private_instance, expected_type=type_hints["private_instance"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
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
        if dataproc_service_account is not None:
            self._values["dataproc_service_account"] = dataproc_service_account
        if description is not None:
            self._values["description"] = description
        if enable_stackdriver_logging is not None:
            self._values["enable_stackdriver_logging"] = enable_stackdriver_logging
        if enable_stackdriver_monitoring is not None:
            self._values["enable_stackdriver_monitoring"] = enable_stackdriver_monitoring
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if network_config is not None:
            self._values["network_config"] = network_config
        if options is not None:
            self._values["options"] = options
        if private_instance is not None:
            self._values["private_instance"] = private_instance
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if version is not None:
            self._values["version"] = version

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
    def name(self) -> builtins.str:
        '''The ID of the instance or a fully qualified identifier for the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#name GoogleDataFusionInstance#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Represents the type of Data Fusion instance.

        Each type is configured with
        the default settings for processing and memory.

        - BASIC: Basic Data Fusion instance. In Basic type, the user will be able to create data pipelines
          using point and click UI. However, there are certain limitations, such as fewer number
          of concurrent pipelines, no support for streaming pipelines, etc.
        - ENTERPRISE: Enterprise Data Fusion instance. In Enterprise type, the user will have more features
          available, such as support for streaming pipelines, higher number of concurrent pipelines, etc.
        - DEVELOPER: Developer Data Fusion instance. In Developer type, the user will have all features available but
          with restrictive capabilities. This is to help enterprises design and develop their data ingestion and integration
          pipelines at low cost. Possible values: ["BASIC", "ENTERPRISE", "DEVELOPER"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#type GoogleDataFusionInstance#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataproc_service_account(self) -> typing.Optional[builtins.str]:
        '''User-managed service account to set on Dataproc when Cloud Data Fusion creates Dataproc to run data processing pipelines.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#dataproc_service_account GoogleDataFusionInstance#dataproc_service_account}
        '''
        result = self._values.get("dataproc_service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#description GoogleDataFusionInstance#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_stackdriver_logging(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Option to enable Stackdriver Logging.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#enable_stackdriver_logging GoogleDataFusionInstance#enable_stackdriver_logging}
        '''
        result = self._values.get("enable_stackdriver_logging")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_stackdriver_monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Option to enable Stackdriver Monitoring.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#enable_stackdriver_monitoring GoogleDataFusionInstance#enable_stackdriver_monitoring}
        '''
        result = self._values.get("enable_stackdriver_monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#id GoogleDataFusionInstance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The resource labels for instance to use to annotate any related underlying resources, such as Compute Engine VMs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#labels GoogleDataFusionInstance#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def network_config(
        self,
    ) -> typing.Optional["GoogleDataFusionInstanceNetworkConfig"]:
        '''network_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#network_config GoogleDataFusionInstance#network_config}
        '''
        result = self._values.get("network_config")
        return typing.cast(typing.Optional["GoogleDataFusionInstanceNetworkConfig"], result)

    @builtins.property
    def options(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of additional options used to configure the behavior of Data Fusion instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#options GoogleDataFusionInstance#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def private_instance(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether the Data Fusion instance should be private.

        If set to
        true, all Data Fusion nodes will have private IP addresses and will not be
        able to access the public internet.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#private_instance GoogleDataFusionInstance#private_instance}
        '''
        result = self._values.get("private_instance")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#project GoogleDataFusionInstance#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region of the Data Fusion instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#region GoogleDataFusionInstance#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDataFusionInstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#timeouts GoogleDataFusionInstance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDataFusionInstanceTimeouts"], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Current version of the Data Fusion.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#version GoogleDataFusionInstance#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataFusionInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataFusionInstance.GoogleDataFusionInstanceNetworkConfig",
    jsii_struct_bases=[],
    name_mapping={"ip_allocation": "ipAllocation", "network": "network"},
)
class GoogleDataFusionInstanceNetworkConfig:
    def __init__(self, *, ip_allocation: builtins.str, network: builtins.str) -> None:
        '''
        :param ip_allocation: The IP range in CIDR notation to use for the managed Data Fusion instance nodes. This range must not overlap with any other ranges used in the Data Fusion instance network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#ip_allocation GoogleDataFusionInstance#ip_allocation}
        :param network: Name of the network in the project with which the tenant project will be peered for executing pipelines. In case of shared VPC where the network resides in another host project the network should specified in the form of projects/{host-project-id}/global/networks/{network} Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#network GoogleDataFusionInstance#network}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataFusionInstanceNetworkConfig.__init__)
            check_type(argname="argument ip_allocation", value=ip_allocation, expected_type=type_hints["ip_allocation"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
        self._values: typing.Dict[str, typing.Any] = {
            "ip_allocation": ip_allocation,
            "network": network,
        }

    @builtins.property
    def ip_allocation(self) -> builtins.str:
        '''The IP range in CIDR notation to use for the managed Data Fusion instance nodes.

        This range must not overlap with any other ranges used in the Data Fusion instance network.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#ip_allocation GoogleDataFusionInstance#ip_allocation}
        '''
        result = self._values.get("ip_allocation")
        assert result is not None, "Required property 'ip_allocation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network(self) -> builtins.str:
        '''Name of the network in the project with which the tenant project will be peered for executing pipelines.

        In case of shared VPC where the network resides in another host
        project the network should specified in the form of projects/{host-project-id}/global/networks/{network}

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#network GoogleDataFusionInstance#network}
        '''
        result = self._values.get("network")
        assert result is not None, "Required property 'network' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataFusionInstanceNetworkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataFusionInstanceNetworkConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataFusionInstance.GoogleDataFusionInstanceNetworkConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataFusionInstanceNetworkConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="ipAllocationInput")
    def ip_allocation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAllocationInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAllocation")
    def ip_allocation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAllocation"))

    @ip_allocation.setter
    def ip_allocation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstanceNetworkConfigOutputReference, "ip_allocation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAllocation", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstanceNetworkConfigOutputReference, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDataFusionInstanceNetworkConfig]:
        return typing.cast(typing.Optional[GoogleDataFusionInstanceNetworkConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataFusionInstanceNetworkConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstanceNetworkConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataFusionInstance.GoogleDataFusionInstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleDataFusionInstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#create GoogleDataFusionInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#delete GoogleDataFusionInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#update GoogleDataFusionInstance#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataFusionInstanceTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#create GoogleDataFusionInstance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#delete GoogleDataFusionInstance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_fusion_instance#update GoogleDataFusionInstance#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataFusionInstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataFusionInstanceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataFusionInstance.GoogleDataFusionInstanceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataFusionInstanceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstanceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstanceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstanceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataFusionInstanceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataFusionInstanceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataFusionInstanceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataFusionInstanceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDataFusionInstance",
    "GoogleDataFusionInstanceConfig",
    "GoogleDataFusionInstanceNetworkConfig",
    "GoogleDataFusionInstanceNetworkConfigOutputReference",
    "GoogleDataFusionInstanceTimeouts",
    "GoogleDataFusionInstanceTimeoutsOutputReference",
]

publication.publish()
