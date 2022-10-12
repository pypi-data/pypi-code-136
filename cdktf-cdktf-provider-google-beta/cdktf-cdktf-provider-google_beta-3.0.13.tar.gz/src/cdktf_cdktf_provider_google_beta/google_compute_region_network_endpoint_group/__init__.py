'''
# `google_compute_region_network_endpoint_group`

Refer to the Terraform Registory for docs: [`google_compute_region_network_endpoint_group`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group).
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


class GoogleComputeRegionNetworkEndpointGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionNetworkEndpointGroup.GoogleComputeRegionNetworkEndpointGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group google_compute_region_network_endpoint_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        region: builtins.str,
        app_engine: typing.Optional[typing.Union["GoogleComputeRegionNetworkEndpointGroupAppEngine", typing.Dict[str, typing.Any]]] = None,
        cloud_function: typing.Optional[typing.Union["GoogleComputeRegionNetworkEndpointGroupCloudFunction", typing.Dict[str, typing.Any]]] = None,
        cloud_run: typing.Optional[typing.Union["GoogleComputeRegionNetworkEndpointGroupCloudRun", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        network_endpoint_type: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        psc_target_service: typing.Optional[builtins.str] = None,
        serverless_deployment: typing.Optional[typing.Union["GoogleComputeRegionNetworkEndpointGroupServerlessDeployment", typing.Dict[str, typing.Any]]] = None,
        subnetwork: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRegionNetworkEndpointGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group google_compute_region_network_endpoint_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#name GoogleComputeRegionNetworkEndpointGroup#name}
        :param region: A reference to the region where the Serverless NEGs Reside. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#region GoogleComputeRegionNetworkEndpointGroup#region}
        :param app_engine: app_engine block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#app_engine GoogleComputeRegionNetworkEndpointGroup#app_engine}
        :param cloud_function: cloud_function block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#cloud_function GoogleComputeRegionNetworkEndpointGroup#cloud_function}
        :param cloud_run: cloud_run block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#cloud_run GoogleComputeRegionNetworkEndpointGroup#cloud_run}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#description GoogleComputeRegionNetworkEndpointGroup#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#id GoogleComputeRegionNetworkEndpointGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param network: This field is only used for PSC. The URL of the network to which all network endpoints in the NEG belong. Uses "default" project network if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#network GoogleComputeRegionNetworkEndpointGroup#network}
        :param network_endpoint_type: Type of network endpoints in this network endpoint group. Defaults to SERVERLESS Default value: "SERVERLESS" Possible values: ["SERVERLESS", "PRIVATE_SERVICE_CONNECT"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#network_endpoint_type GoogleComputeRegionNetworkEndpointGroup#network_endpoint_type}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#project GoogleComputeRegionNetworkEndpointGroup#project}.
        :param psc_target_service: The target service url used to set up private service connection to a Google API or a PSC Producer Service Attachment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#psc_target_service GoogleComputeRegionNetworkEndpointGroup#psc_target_service}
        :param serverless_deployment: serverless_deployment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#serverless_deployment GoogleComputeRegionNetworkEndpointGroup#serverless_deployment}
        :param subnetwork: This field is only used for PSC. Optional URL of the subnetwork to which all network endpoints in the NEG belong. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#subnetwork GoogleComputeRegionNetworkEndpointGroup#subnetwork}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#timeouts GoogleComputeRegionNetworkEndpointGroup#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionNetworkEndpointGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeRegionNetworkEndpointGroupConfig(
            name=name,
            region=region,
            app_engine=app_engine,
            cloud_function=cloud_function,
            cloud_run=cloud_run,
            description=description,
            id=id,
            network=network,
            network_endpoint_type=network_endpoint_type,
            project=project,
            psc_target_service=psc_target_service,
            serverless_deployment=serverless_deployment,
            subnetwork=subnetwork,
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

    @jsii.member(jsii_name="putAppEngine")
    def put_app_engine(
        self,
        *,
        service: typing.Optional[builtins.str] = None,
        url_mask: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service: Optional serving service. The service name must be 1-63 characters long, and comply with RFC1035. Example value: "default", "my-service". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#service GoogleComputeRegionNetworkEndpointGroup#service}
        :param url_mask: A template to parse service and version fields from a request URL. URL mask allows for routing to multiple App Engine services without having to create multiple Network Endpoint Groups and backend services. For example, the request URLs "foo1-dot-appname.appspot.com/v1" and "foo1-dot-appname.appspot.com/v2" can be backed by the same Serverless NEG with URL mask "-dot-appname.appspot.com/". The URL mask will parse them to { service = "foo1", version = "v1" } and { service = "foo1", version = "v2" } respectively. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#url_mask GoogleComputeRegionNetworkEndpointGroup#url_mask}
        :param version: Optional serving version. The version must be 1-63 characters long, and comply with RFC1035. Example value: "v1", "v2". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#version GoogleComputeRegionNetworkEndpointGroup#version}
        '''
        value = GoogleComputeRegionNetworkEndpointGroupAppEngine(
            service=service, url_mask=url_mask, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putAppEngine", [value]))

    @jsii.member(jsii_name="putCloudFunction")
    def put_cloud_function(
        self,
        *,
        function: typing.Optional[builtins.str] = None,
        url_mask: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param function: A user-defined name of the Cloud Function. The function name is case-sensitive and must be 1-63 characters long. Example value: "func1". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#function GoogleComputeRegionNetworkEndpointGroup#function}
        :param url_mask: A template to parse function field from a request URL. URL mask allows for routing to multiple Cloud Functions without having to create multiple Network Endpoint Groups and backend services. For example, request URLs "mydomain.com/function1" and "mydomain.com/function2" can be backed by the same Serverless NEG with URL mask "/". The URL mask will parse them to { function = "function1" } and { function = "function2" } respectively. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#url_mask GoogleComputeRegionNetworkEndpointGroup#url_mask}
        '''
        value = GoogleComputeRegionNetworkEndpointGroupCloudFunction(
            function=function, url_mask=url_mask
        )

        return typing.cast(None, jsii.invoke(self, "putCloudFunction", [value]))

    @jsii.member(jsii_name="putCloudRun")
    def put_cloud_run(
        self,
        *,
        service: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
        url_mask: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service: Cloud Run service is the main resource of Cloud Run. The service must be 1-63 characters long, and comply with RFC1035. Example value: "run-service". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#service GoogleComputeRegionNetworkEndpointGroup#service}
        :param tag: Cloud Run tag represents the "named-revision" to provide additional fine-grained traffic routing information. The tag must be 1-63 characters long, and comply with RFC1035. Example value: "revision-0010". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#tag GoogleComputeRegionNetworkEndpointGroup#tag}
        :param url_mask: A template to parse service and tag fields from a request URL. URL mask allows for routing to multiple Run services without having to create multiple network endpoint groups and backend services. For example, request URLs "foo1.domain.com/bar1" and "foo1.domain.com/bar2" an be backed by the same Serverless Network Endpoint Group (NEG) with URL mask ".domain.com/". The URL mask will parse them to { service="bar1", tag="foo1" } and { service="bar2", tag="foo2" } respectively. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#url_mask GoogleComputeRegionNetworkEndpointGroup#url_mask}
        '''
        value = GoogleComputeRegionNetworkEndpointGroupCloudRun(
            service=service, tag=tag, url_mask=url_mask
        )

        return typing.cast(None, jsii.invoke(self, "putCloudRun", [value]))

    @jsii.member(jsii_name="putServerlessDeployment")
    def put_serverless_deployment(
        self,
        *,
        platform: builtins.str,
        resource: typing.Optional[builtins.str] = None,
        url_mask: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param platform: The platform of the NEG backend target(s). Possible values: API Gateway: apigateway.googleapis.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#platform GoogleComputeRegionNetworkEndpointGroup#platform}
        :param resource: The user-defined name of the workload/instance. This value must be provided explicitly or in the urlMask. The resource identified by this value is platform-specific and is as follows: API Gateway: The gateway ID, App Engine: The service name, Cloud Functions: The function name, Cloud Run: The service name Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#resource GoogleComputeRegionNetworkEndpointGroup#resource}
        :param url_mask: A template to parse platform-specific fields from a request URL. URL mask allows for routing to multiple resources on the same serverless platform without having to create multiple Network Endpoint Groups and backend resources. The fields parsed by this template are platform-specific and are as follows: API Gateway: The gateway ID, App Engine: The service and version, Cloud Functions: The function name, Cloud Run: The service and tag Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#url_mask GoogleComputeRegionNetworkEndpointGroup#url_mask}
        :param version: The optional resource version. The version identified by this value is platform-specific and is follows: API Gateway: Unused, App Engine: The service version, Cloud Functions: Unused, Cloud Run: The service tag Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#version GoogleComputeRegionNetworkEndpointGroup#version}
        '''
        value = GoogleComputeRegionNetworkEndpointGroupServerlessDeployment(
            platform=platform, resource=resource, url_mask=url_mask, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putServerlessDeployment", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#create GoogleComputeRegionNetworkEndpointGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#delete GoogleComputeRegionNetworkEndpointGroup#delete}.
        '''
        value = GoogleComputeRegionNetworkEndpointGroupTimeouts(
            create=create, delete=delete
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAppEngine")
    def reset_app_engine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppEngine", []))

    @jsii.member(jsii_name="resetCloudFunction")
    def reset_cloud_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudFunction", []))

    @jsii.member(jsii_name="resetCloudRun")
    def reset_cloud_run(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudRun", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetNetworkEndpointType")
    def reset_network_endpoint_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkEndpointType", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetPscTargetService")
    def reset_psc_target_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPscTargetService", []))

    @jsii.member(jsii_name="resetServerlessDeployment")
    def reset_serverless_deployment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerlessDeployment", []))

    @jsii.member(jsii_name="resetSubnetwork")
    def reset_subnetwork(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetwork", []))

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
    @jsii.member(jsii_name="appEngine")
    def app_engine(
        self,
    ) -> "GoogleComputeRegionNetworkEndpointGroupAppEngineOutputReference":
        return typing.cast("GoogleComputeRegionNetworkEndpointGroupAppEngineOutputReference", jsii.get(self, "appEngine"))

    @builtins.property
    @jsii.member(jsii_name="cloudFunction")
    def cloud_function(
        self,
    ) -> "GoogleComputeRegionNetworkEndpointGroupCloudFunctionOutputReference":
        return typing.cast("GoogleComputeRegionNetworkEndpointGroupCloudFunctionOutputReference", jsii.get(self, "cloudFunction"))

    @builtins.property
    @jsii.member(jsii_name="cloudRun")
    def cloud_run(
        self,
    ) -> "GoogleComputeRegionNetworkEndpointGroupCloudRunOutputReference":
        return typing.cast("GoogleComputeRegionNetworkEndpointGroupCloudRunOutputReference", jsii.get(self, "cloudRun"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="serverlessDeployment")
    def serverless_deployment(
        self,
    ) -> "GoogleComputeRegionNetworkEndpointGroupServerlessDeploymentOutputReference":
        return typing.cast("GoogleComputeRegionNetworkEndpointGroupServerlessDeploymentOutputReference", jsii.get(self, "serverlessDeployment"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "GoogleComputeRegionNetworkEndpointGroupTimeoutsOutputReference":
        return typing.cast("GoogleComputeRegionNetworkEndpointGroupTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="appEngineInput")
    def app_engine_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionNetworkEndpointGroupAppEngine"]:
        return typing.cast(typing.Optional["GoogleComputeRegionNetworkEndpointGroupAppEngine"], jsii.get(self, "appEngineInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudFunctionInput")
    def cloud_function_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionNetworkEndpointGroupCloudFunction"]:
        return typing.cast(typing.Optional["GoogleComputeRegionNetworkEndpointGroupCloudFunction"], jsii.get(self, "cloudFunctionInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudRunInput")
    def cloud_run_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionNetworkEndpointGroupCloudRun"]:
        return typing.cast(typing.Optional["GoogleComputeRegionNetworkEndpointGroupCloudRun"], jsii.get(self, "cloudRunInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkEndpointTypeInput")
    def network_endpoint_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkEndpointTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="pscTargetServiceInput")
    def psc_target_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pscTargetServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="serverlessDeploymentInput")
    def serverless_deployment_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionNetworkEndpointGroupServerlessDeployment"]:
        return typing.cast(typing.Optional["GoogleComputeRegionNetworkEndpointGroupServerlessDeployment"], jsii.get(self, "serverlessDeploymentInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetworkInput")
    def subnetwork_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeRegionNetworkEndpointGroupTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeRegionNetworkEndpointGroupTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroup, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroup, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="networkEndpointType")
    def network_endpoint_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkEndpointType"))

    @network_endpoint_type.setter
    def network_endpoint_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroup, "network_endpoint_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkEndpointType", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroup, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="pscTargetService")
    def psc_target_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pscTargetService"))

    @psc_target_service.setter
    def psc_target_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroup, "psc_target_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pscTargetService", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroup, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="subnetwork")
    def subnetwork(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetwork"))

    @subnetwork.setter
    def subnetwork(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroup, "subnetwork").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetwork", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionNetworkEndpointGroup.GoogleComputeRegionNetworkEndpointGroupAppEngine",
    jsii_struct_bases=[],
    name_mapping={"service": "service", "url_mask": "urlMask", "version": "version"},
)
class GoogleComputeRegionNetworkEndpointGroupAppEngine:
    def __init__(
        self,
        *,
        service: typing.Optional[builtins.str] = None,
        url_mask: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service: Optional serving service. The service name must be 1-63 characters long, and comply with RFC1035. Example value: "default", "my-service". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#service GoogleComputeRegionNetworkEndpointGroup#service}
        :param url_mask: A template to parse service and version fields from a request URL. URL mask allows for routing to multiple App Engine services without having to create multiple Network Endpoint Groups and backend services. For example, the request URLs "foo1-dot-appname.appspot.com/v1" and "foo1-dot-appname.appspot.com/v2" can be backed by the same Serverless NEG with URL mask "-dot-appname.appspot.com/". The URL mask will parse them to { service = "foo1", version = "v1" } and { service = "foo1", version = "v2" } respectively. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#url_mask GoogleComputeRegionNetworkEndpointGroup#url_mask}
        :param version: Optional serving version. The version must be 1-63 characters long, and comply with RFC1035. Example value: "v1", "v2". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#version GoogleComputeRegionNetworkEndpointGroup#version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionNetworkEndpointGroupAppEngine.__init__)
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument url_mask", value=url_mask, expected_type=type_hints["url_mask"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if service is not None:
            self._values["service"] = service
        if url_mask is not None:
            self._values["url_mask"] = url_mask
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''Optional serving service. The service name must be 1-63 characters long, and comply with RFC1035. Example value: "default", "my-service".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#service GoogleComputeRegionNetworkEndpointGroup#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url_mask(self) -> typing.Optional[builtins.str]:
        '''A template to parse service and version fields from a request URL.

        URL mask allows for routing to multiple App Engine services without
        having to create multiple Network Endpoint Groups and backend services.

        For example, the request URLs "foo1-dot-appname.appspot.com/v1" and
        "foo1-dot-appname.appspot.com/v2" can be backed by the same Serverless NEG with
        URL mask "-dot-appname.appspot.com/". The URL mask will parse
        them to { service = "foo1", version = "v1" } and { service = "foo1", version = "v2" } respectively.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#url_mask GoogleComputeRegionNetworkEndpointGroup#url_mask}
        '''
        result = self._values.get("url_mask")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Optional serving version. The version must be 1-63 characters long, and comply with RFC1035. Example value: "v1", "v2".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#version GoogleComputeRegionNetworkEndpointGroup#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionNetworkEndpointGroupAppEngine(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionNetworkEndpointGroupAppEngineOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionNetworkEndpointGroup.GoogleComputeRegionNetworkEndpointGroupAppEngineOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionNetworkEndpointGroupAppEngineOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetUrlMask")
    def reset_url_mask(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlMask", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="urlMaskInput")
    def url_mask_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlMaskInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupAppEngineOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="urlMask")
    def url_mask(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urlMask"))

    @url_mask.setter
    def url_mask(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupAppEngineOutputReference, "url_mask").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlMask", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupAppEngineOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionNetworkEndpointGroupAppEngine]:
        return typing.cast(typing.Optional[GoogleComputeRegionNetworkEndpointGroupAppEngine], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionNetworkEndpointGroupAppEngine],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupAppEngineOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionNetworkEndpointGroup.GoogleComputeRegionNetworkEndpointGroupCloudFunction",
    jsii_struct_bases=[],
    name_mapping={"function": "function", "url_mask": "urlMask"},
)
class GoogleComputeRegionNetworkEndpointGroupCloudFunction:
    def __init__(
        self,
        *,
        function: typing.Optional[builtins.str] = None,
        url_mask: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param function: A user-defined name of the Cloud Function. The function name is case-sensitive and must be 1-63 characters long. Example value: "func1". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#function GoogleComputeRegionNetworkEndpointGroup#function}
        :param url_mask: A template to parse function field from a request URL. URL mask allows for routing to multiple Cloud Functions without having to create multiple Network Endpoint Groups and backend services. For example, request URLs "mydomain.com/function1" and "mydomain.com/function2" can be backed by the same Serverless NEG with URL mask "/". The URL mask will parse them to { function = "function1" } and { function = "function2" } respectively. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#url_mask GoogleComputeRegionNetworkEndpointGroup#url_mask}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionNetworkEndpointGroupCloudFunction.__init__)
            check_type(argname="argument function", value=function, expected_type=type_hints["function"])
            check_type(argname="argument url_mask", value=url_mask, expected_type=type_hints["url_mask"])
        self._values: typing.Dict[str, typing.Any] = {}
        if function is not None:
            self._values["function"] = function
        if url_mask is not None:
            self._values["url_mask"] = url_mask

    @builtins.property
    def function(self) -> typing.Optional[builtins.str]:
        '''A user-defined name of the Cloud Function. The function name is case-sensitive and must be 1-63 characters long. Example value: "func1".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#function GoogleComputeRegionNetworkEndpointGroup#function}
        '''
        result = self._values.get("function")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url_mask(self) -> typing.Optional[builtins.str]:
        '''A template to parse function field from a request URL.

        URL mask allows
        for routing to multiple Cloud Functions without having to create
        multiple Network Endpoint Groups and backend services.

        For example, request URLs "mydomain.com/function1" and "mydomain.com/function2"
        can be backed by the same Serverless NEG with URL mask "/". The URL mask
        will parse them to { function = "function1" } and { function = "function2" } respectively.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#url_mask GoogleComputeRegionNetworkEndpointGroup#url_mask}
        '''
        result = self._values.get("url_mask")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionNetworkEndpointGroupCloudFunction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionNetworkEndpointGroupCloudFunctionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionNetworkEndpointGroup.GoogleComputeRegionNetworkEndpointGroupCloudFunctionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionNetworkEndpointGroupCloudFunctionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFunction")
    def reset_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunction", []))

    @jsii.member(jsii_name="resetUrlMask")
    def reset_url_mask(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlMask", []))

    @builtins.property
    @jsii.member(jsii_name="functionInput")
    def function_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlMaskInput")
    def url_mask_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlMaskInput"))

    @builtins.property
    @jsii.member(jsii_name="function")
    def function(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "function"))

    @function.setter
    def function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupCloudFunctionOutputReference, "function").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "function", value)

    @builtins.property
    @jsii.member(jsii_name="urlMask")
    def url_mask(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urlMask"))

    @url_mask.setter
    def url_mask(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupCloudFunctionOutputReference, "url_mask").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlMask", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionNetworkEndpointGroupCloudFunction]:
        return typing.cast(typing.Optional[GoogleComputeRegionNetworkEndpointGroupCloudFunction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionNetworkEndpointGroupCloudFunction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupCloudFunctionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionNetworkEndpointGroup.GoogleComputeRegionNetworkEndpointGroupCloudRun",
    jsii_struct_bases=[],
    name_mapping={"service": "service", "tag": "tag", "url_mask": "urlMask"},
)
class GoogleComputeRegionNetworkEndpointGroupCloudRun:
    def __init__(
        self,
        *,
        service: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
        url_mask: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service: Cloud Run service is the main resource of Cloud Run. The service must be 1-63 characters long, and comply with RFC1035. Example value: "run-service". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#service GoogleComputeRegionNetworkEndpointGroup#service}
        :param tag: Cloud Run tag represents the "named-revision" to provide additional fine-grained traffic routing information. The tag must be 1-63 characters long, and comply with RFC1035. Example value: "revision-0010". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#tag GoogleComputeRegionNetworkEndpointGroup#tag}
        :param url_mask: A template to parse service and tag fields from a request URL. URL mask allows for routing to multiple Run services without having to create multiple network endpoint groups and backend services. For example, request URLs "foo1.domain.com/bar1" and "foo1.domain.com/bar2" an be backed by the same Serverless Network Endpoint Group (NEG) with URL mask ".domain.com/". The URL mask will parse them to { service="bar1", tag="foo1" } and { service="bar2", tag="foo2" } respectively. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#url_mask GoogleComputeRegionNetworkEndpointGroup#url_mask}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionNetworkEndpointGroupCloudRun.__init__)
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument url_mask", value=url_mask, expected_type=type_hints["url_mask"])
        self._values: typing.Dict[str, typing.Any] = {}
        if service is not None:
            self._values["service"] = service
        if tag is not None:
            self._values["tag"] = tag
        if url_mask is not None:
            self._values["url_mask"] = url_mask

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''Cloud Run service is the main resource of Cloud Run.

        The service must be 1-63 characters long, and comply with RFC1035.
        Example value: "run-service".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#service GoogleComputeRegionNetworkEndpointGroup#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''Cloud Run tag represents the "named-revision" to provide additional fine-grained traffic routing information.

        The tag must be 1-63 characters long, and comply with RFC1035.
        Example value: "revision-0010".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#tag GoogleComputeRegionNetworkEndpointGroup#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url_mask(self) -> typing.Optional[builtins.str]:
        '''A template to parse service and tag fields from a request URL.

        URL mask allows for routing to multiple Run services without having
        to create multiple network endpoint groups and backend services.

        For example, request URLs "foo1.domain.com/bar1" and "foo1.domain.com/bar2"
        an be backed by the same Serverless Network Endpoint Group (NEG) with
        URL mask ".domain.com/". The URL mask will parse them to { service="bar1", tag="foo1" }
        and { service="bar2", tag="foo2" } respectively.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#url_mask GoogleComputeRegionNetworkEndpointGroup#url_mask}
        '''
        result = self._values.get("url_mask")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionNetworkEndpointGroupCloudRun(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionNetworkEndpointGroupCloudRunOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionNetworkEndpointGroup.GoogleComputeRegionNetworkEndpointGroupCloudRunOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionNetworkEndpointGroupCloudRunOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="resetUrlMask")
    def reset_url_mask(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlMask", []))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="urlMaskInput")
    def url_mask_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlMaskInput"))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupCloudRunOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupCloudRunOutputReference, "tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="urlMask")
    def url_mask(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urlMask"))

    @url_mask.setter
    def url_mask(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupCloudRunOutputReference, "url_mask").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlMask", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionNetworkEndpointGroupCloudRun]:
        return typing.cast(typing.Optional[GoogleComputeRegionNetworkEndpointGroupCloudRun], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionNetworkEndpointGroupCloudRun],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupCloudRunOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionNetworkEndpointGroup.GoogleComputeRegionNetworkEndpointGroupConfig",
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
        "region": "region",
        "app_engine": "appEngine",
        "cloud_function": "cloudFunction",
        "cloud_run": "cloudRun",
        "description": "description",
        "id": "id",
        "network": "network",
        "network_endpoint_type": "networkEndpointType",
        "project": "project",
        "psc_target_service": "pscTargetService",
        "serverless_deployment": "serverlessDeployment",
        "subnetwork": "subnetwork",
        "timeouts": "timeouts",
    },
)
class GoogleComputeRegionNetworkEndpointGroupConfig(cdktf.TerraformMetaArguments):
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
        region: builtins.str,
        app_engine: typing.Optional[typing.Union[GoogleComputeRegionNetworkEndpointGroupAppEngine, typing.Dict[str, typing.Any]]] = None,
        cloud_function: typing.Optional[typing.Union[GoogleComputeRegionNetworkEndpointGroupCloudFunction, typing.Dict[str, typing.Any]]] = None,
        cloud_run: typing.Optional[typing.Union[GoogleComputeRegionNetworkEndpointGroupCloudRun, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        network_endpoint_type: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        psc_target_service: typing.Optional[builtins.str] = None,
        serverless_deployment: typing.Optional[typing.Union["GoogleComputeRegionNetworkEndpointGroupServerlessDeployment", typing.Dict[str, typing.Any]]] = None,
        subnetwork: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRegionNetworkEndpointGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#name GoogleComputeRegionNetworkEndpointGroup#name}
        :param region: A reference to the region where the Serverless NEGs Reside. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#region GoogleComputeRegionNetworkEndpointGroup#region}
        :param app_engine: app_engine block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#app_engine GoogleComputeRegionNetworkEndpointGroup#app_engine}
        :param cloud_function: cloud_function block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#cloud_function GoogleComputeRegionNetworkEndpointGroup#cloud_function}
        :param cloud_run: cloud_run block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#cloud_run GoogleComputeRegionNetworkEndpointGroup#cloud_run}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#description GoogleComputeRegionNetworkEndpointGroup#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#id GoogleComputeRegionNetworkEndpointGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param network: This field is only used for PSC. The URL of the network to which all network endpoints in the NEG belong. Uses "default" project network if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#network GoogleComputeRegionNetworkEndpointGroup#network}
        :param network_endpoint_type: Type of network endpoints in this network endpoint group. Defaults to SERVERLESS Default value: "SERVERLESS" Possible values: ["SERVERLESS", "PRIVATE_SERVICE_CONNECT"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#network_endpoint_type GoogleComputeRegionNetworkEndpointGroup#network_endpoint_type}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#project GoogleComputeRegionNetworkEndpointGroup#project}.
        :param psc_target_service: The target service url used to set up private service connection to a Google API or a PSC Producer Service Attachment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#psc_target_service GoogleComputeRegionNetworkEndpointGroup#psc_target_service}
        :param serverless_deployment: serverless_deployment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#serverless_deployment GoogleComputeRegionNetworkEndpointGroup#serverless_deployment}
        :param subnetwork: This field is only used for PSC. Optional URL of the subnetwork to which all network endpoints in the NEG belong. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#subnetwork GoogleComputeRegionNetworkEndpointGroup#subnetwork}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#timeouts GoogleComputeRegionNetworkEndpointGroup#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(app_engine, dict):
            app_engine = GoogleComputeRegionNetworkEndpointGroupAppEngine(**app_engine)
        if isinstance(cloud_function, dict):
            cloud_function = GoogleComputeRegionNetworkEndpointGroupCloudFunction(**cloud_function)
        if isinstance(cloud_run, dict):
            cloud_run = GoogleComputeRegionNetworkEndpointGroupCloudRun(**cloud_run)
        if isinstance(serverless_deployment, dict):
            serverless_deployment = GoogleComputeRegionNetworkEndpointGroupServerlessDeployment(**serverless_deployment)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeRegionNetworkEndpointGroupTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionNetworkEndpointGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument app_engine", value=app_engine, expected_type=type_hints["app_engine"])
            check_type(argname="argument cloud_function", value=cloud_function, expected_type=type_hints["cloud_function"])
            check_type(argname="argument cloud_run", value=cloud_run, expected_type=type_hints["cloud_run"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument network_endpoint_type", value=network_endpoint_type, expected_type=type_hints["network_endpoint_type"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument psc_target_service", value=psc_target_service, expected_type=type_hints["psc_target_service"])
            check_type(argname="argument serverless_deployment", value=serverless_deployment, expected_type=type_hints["serverless_deployment"])
            check_type(argname="argument subnetwork", value=subnetwork, expected_type=type_hints["subnetwork"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "region": region,
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
        if app_engine is not None:
            self._values["app_engine"] = app_engine
        if cloud_function is not None:
            self._values["cloud_function"] = cloud_function
        if cloud_run is not None:
            self._values["cloud_run"] = cloud_run
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if network is not None:
            self._values["network"] = network
        if network_endpoint_type is not None:
            self._values["network_endpoint_type"] = network_endpoint_type
        if project is not None:
            self._values["project"] = project
        if psc_target_service is not None:
            self._values["psc_target_service"] = psc_target_service
        if serverless_deployment is not None:
            self._values["serverless_deployment"] = serverless_deployment
        if subnetwork is not None:
            self._values["subnetwork"] = subnetwork
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
    def name(self) -> builtins.str:
        '''Name of the resource;

        provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#name GoogleComputeRegionNetworkEndpointGroup#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''A reference to the region where the Serverless NEGs Reside.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#region GoogleComputeRegionNetworkEndpointGroup#region}
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_engine(
        self,
    ) -> typing.Optional[GoogleComputeRegionNetworkEndpointGroupAppEngine]:
        '''app_engine block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#app_engine GoogleComputeRegionNetworkEndpointGroup#app_engine}
        '''
        result = self._values.get("app_engine")
        return typing.cast(typing.Optional[GoogleComputeRegionNetworkEndpointGroupAppEngine], result)

    @builtins.property
    def cloud_function(
        self,
    ) -> typing.Optional[GoogleComputeRegionNetworkEndpointGroupCloudFunction]:
        '''cloud_function block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#cloud_function GoogleComputeRegionNetworkEndpointGroup#cloud_function}
        '''
        result = self._values.get("cloud_function")
        return typing.cast(typing.Optional[GoogleComputeRegionNetworkEndpointGroupCloudFunction], result)

    @builtins.property
    def cloud_run(
        self,
    ) -> typing.Optional[GoogleComputeRegionNetworkEndpointGroupCloudRun]:
        '''cloud_run block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#cloud_run GoogleComputeRegionNetworkEndpointGroup#cloud_run}
        '''
        result = self._values.get("cloud_run")
        return typing.cast(typing.Optional[GoogleComputeRegionNetworkEndpointGroupCloudRun], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource. Provide this property when you create the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#description GoogleComputeRegionNetworkEndpointGroup#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#id GoogleComputeRegionNetworkEndpointGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''This field is only used for PSC.

        The URL of the network to which all network endpoints in the NEG belong. Uses
        "default" project network if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#network GoogleComputeRegionNetworkEndpointGroup#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_endpoint_type(self) -> typing.Optional[builtins.str]:
        '''Type of network endpoints in this network endpoint group. Defaults to SERVERLESS Default value: "SERVERLESS" Possible values: ["SERVERLESS", "PRIVATE_SERVICE_CONNECT"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#network_endpoint_type GoogleComputeRegionNetworkEndpointGroup#network_endpoint_type}
        '''
        result = self._values.get("network_endpoint_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#project GoogleComputeRegionNetworkEndpointGroup#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def psc_target_service(self) -> typing.Optional[builtins.str]:
        '''The target service url used to set up private service connection to a Google API or a PSC Producer Service Attachment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#psc_target_service GoogleComputeRegionNetworkEndpointGroup#psc_target_service}
        '''
        result = self._values.get("psc_target_service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def serverless_deployment(
        self,
    ) -> typing.Optional["GoogleComputeRegionNetworkEndpointGroupServerlessDeployment"]:
        '''serverless_deployment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#serverless_deployment GoogleComputeRegionNetworkEndpointGroup#serverless_deployment}
        '''
        result = self._values.get("serverless_deployment")
        return typing.cast(typing.Optional["GoogleComputeRegionNetworkEndpointGroupServerlessDeployment"], result)

    @builtins.property
    def subnetwork(self) -> typing.Optional[builtins.str]:
        '''This field is only used for PSC.

        Optional URL of the subnetwork to which all network endpoints in the NEG belong.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#subnetwork GoogleComputeRegionNetworkEndpointGroup#subnetwork}
        '''
        result = self._values.get("subnetwork")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["GoogleComputeRegionNetworkEndpointGroupTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#timeouts GoogleComputeRegionNetworkEndpointGroup#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeRegionNetworkEndpointGroupTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionNetworkEndpointGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionNetworkEndpointGroup.GoogleComputeRegionNetworkEndpointGroupServerlessDeployment",
    jsii_struct_bases=[],
    name_mapping={
        "platform": "platform",
        "resource": "resource",
        "url_mask": "urlMask",
        "version": "version",
    },
)
class GoogleComputeRegionNetworkEndpointGroupServerlessDeployment:
    def __init__(
        self,
        *,
        platform: builtins.str,
        resource: typing.Optional[builtins.str] = None,
        url_mask: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param platform: The platform of the NEG backend target(s). Possible values: API Gateway: apigateway.googleapis.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#platform GoogleComputeRegionNetworkEndpointGroup#platform}
        :param resource: The user-defined name of the workload/instance. This value must be provided explicitly or in the urlMask. The resource identified by this value is platform-specific and is as follows: API Gateway: The gateway ID, App Engine: The service name, Cloud Functions: The function name, Cloud Run: The service name Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#resource GoogleComputeRegionNetworkEndpointGroup#resource}
        :param url_mask: A template to parse platform-specific fields from a request URL. URL mask allows for routing to multiple resources on the same serverless platform without having to create multiple Network Endpoint Groups and backend resources. The fields parsed by this template are platform-specific and are as follows: API Gateway: The gateway ID, App Engine: The service and version, Cloud Functions: The function name, Cloud Run: The service and tag Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#url_mask GoogleComputeRegionNetworkEndpointGroup#url_mask}
        :param version: The optional resource version. The version identified by this value is platform-specific and is follows: API Gateway: Unused, App Engine: The service version, Cloud Functions: Unused, Cloud Run: The service tag Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#version GoogleComputeRegionNetworkEndpointGroup#version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionNetworkEndpointGroupServerlessDeployment.__init__)
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument url_mask", value=url_mask, expected_type=type_hints["url_mask"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "platform": platform,
        }
        if resource is not None:
            self._values["resource"] = resource
        if url_mask is not None:
            self._values["url_mask"] = url_mask
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def platform(self) -> builtins.str:
        '''The platform of the NEG backend target(s). Possible values: API Gateway: apigateway.googleapis.com.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#platform GoogleComputeRegionNetworkEndpointGroup#platform}
        '''
        result = self._values.get("platform")
        assert result is not None, "Required property 'platform' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource(self) -> typing.Optional[builtins.str]:
        '''The user-defined name of the workload/instance.

        This value must be provided explicitly or in the urlMask.
        The resource identified by this value is platform-specific and is as follows: API Gateway: The gateway ID, App Engine: The service name,
        Cloud Functions: The function name, Cloud Run: The service name

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#resource GoogleComputeRegionNetworkEndpointGroup#resource}
        '''
        result = self._values.get("resource")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url_mask(self) -> typing.Optional[builtins.str]:
        '''A template to parse platform-specific fields from a request URL.

        URL mask allows for routing to multiple resources
        on the same serverless platform without having to create multiple Network Endpoint Groups and backend resources.
        The fields parsed by this template are platform-specific and are as follows: API Gateway: The gateway ID,
        App Engine: The service and version, Cloud Functions: The function name, Cloud Run: The service and tag

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#url_mask GoogleComputeRegionNetworkEndpointGroup#url_mask}
        '''
        result = self._values.get("url_mask")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''The optional resource version.

        The version identified by this value is platform-specific and is follows:
        API Gateway: Unused, App Engine: The service version, Cloud Functions: Unused, Cloud Run: The service tag

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#version GoogleComputeRegionNetworkEndpointGroup#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionNetworkEndpointGroupServerlessDeployment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionNetworkEndpointGroupServerlessDeploymentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionNetworkEndpointGroup.GoogleComputeRegionNetworkEndpointGroupServerlessDeploymentOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionNetworkEndpointGroupServerlessDeploymentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetResource")
    def reset_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResource", []))

    @jsii.member(jsii_name="resetUrlMask")
    def reset_url_mask(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlMask", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="platformInput")
    def platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="urlMaskInput")
    def url_mask_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlMaskInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platform"))

    @platform.setter
    def platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupServerlessDeploymentOutputReference, "platform").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platform", value)

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @resource.setter
    def resource(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupServerlessDeploymentOutputReference, "resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="urlMask")
    def url_mask(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urlMask"))

    @url_mask.setter
    def url_mask(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupServerlessDeploymentOutputReference, "url_mask").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlMask", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupServerlessDeploymentOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionNetworkEndpointGroupServerlessDeployment]:
        return typing.cast(typing.Optional[GoogleComputeRegionNetworkEndpointGroupServerlessDeployment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionNetworkEndpointGroupServerlessDeployment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupServerlessDeploymentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionNetworkEndpointGroup.GoogleComputeRegionNetworkEndpointGroupTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GoogleComputeRegionNetworkEndpointGroupTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#create GoogleComputeRegionNetworkEndpointGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#delete GoogleComputeRegionNetworkEndpointGroup#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionNetworkEndpointGroupTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#create GoogleComputeRegionNetworkEndpointGroup#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_network_endpoint_group#delete GoogleComputeRegionNetworkEndpointGroup#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionNetworkEndpointGroupTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionNetworkEndpointGroupTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionNetworkEndpointGroup.GoogleComputeRegionNetworkEndpointGroupTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionNetworkEndpointGroupTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionNetworkEndpointGroupTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionNetworkEndpointGroupTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionNetworkEndpointGroupTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionNetworkEndpointGroupTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeRegionNetworkEndpointGroup",
    "GoogleComputeRegionNetworkEndpointGroupAppEngine",
    "GoogleComputeRegionNetworkEndpointGroupAppEngineOutputReference",
    "GoogleComputeRegionNetworkEndpointGroupCloudFunction",
    "GoogleComputeRegionNetworkEndpointGroupCloudFunctionOutputReference",
    "GoogleComputeRegionNetworkEndpointGroupCloudRun",
    "GoogleComputeRegionNetworkEndpointGroupCloudRunOutputReference",
    "GoogleComputeRegionNetworkEndpointGroupConfig",
    "GoogleComputeRegionNetworkEndpointGroupServerlessDeployment",
    "GoogleComputeRegionNetworkEndpointGroupServerlessDeploymentOutputReference",
    "GoogleComputeRegionNetworkEndpointGroupTimeouts",
    "GoogleComputeRegionNetworkEndpointGroupTimeoutsOutputReference",
]

publication.publish()
