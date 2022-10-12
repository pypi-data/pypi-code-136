'''
# `spotinst_ocean_aks`

Refer to the Terraform Registory for docs: [`spotinst_ocean_aks`](https://www.terraform.io/docs/providers/spotinst/r/ocean_aks).
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


class OceanAks(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAks",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks spotinst_ocean_aks}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        acd_identifier: builtins.str,
        aks_name: builtins.str,
        aks_resource_group_name: builtins.str,
        name: builtins.str,
        ssh_public_key: builtins.str,
        autoscaler: typing.Optional[typing.Union["OceanAksAutoscaler", typing.Dict[str, typing.Any]]] = None,
        controller_cluster_id: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
        extension: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksExtension", typing.Dict[str, typing.Any]]]]] = None,
        health: typing.Optional[typing.Union["OceanAksHealth", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        image: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksImage", typing.Dict[str, typing.Any]]]]] = None,
        load_balancer: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksLoadBalancer", typing.Dict[str, typing.Any]]]]] = None,
        managed_service_identity: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksManagedServiceIdentity", typing.Dict[str, typing.Any]]]]] = None,
        max_pods: typing.Optional[jsii.Number] = None,
        network: typing.Optional[typing.Union["OceanAksNetwork", typing.Dict[str, typing.Any]]] = None,
        os_disk: typing.Optional[typing.Union["OceanAksOsDisk", typing.Dict[str, typing.Any]]] = None,
        resource_group_name: typing.Optional[builtins.str] = None,
        strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksStrategy", typing.Dict[str, typing.Any]]]]] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksTag", typing.Dict[str, typing.Any]]]]] = None,
        user_name: typing.Optional[builtins.str] = None,
        vm_sizes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVmSizes", typing.Dict[str, typing.Any]]]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks spotinst_ocean_aks} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param acd_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#acd_identifier OceanAks#acd_identifier}.
        :param aks_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#aks_name OceanAks#aks_name}.
        :param aks_resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#aks_resource_group_name OceanAks#aks_resource_group_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#name OceanAks#name}.
        :param ssh_public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#ssh_public_key OceanAks#ssh_public_key}.
        :param autoscaler: autoscaler block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#autoscaler OceanAks#autoscaler}
        :param controller_cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#controller_cluster_id OceanAks#controller_cluster_id}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#custom_data OceanAks#custom_data}.
        :param extension: extension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#extension OceanAks#extension}
        :param health: health block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#health OceanAks#health}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#id OceanAks#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image: image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#image OceanAks#image}
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#load_balancer OceanAks#load_balancer}
        :param managed_service_identity: managed_service_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#managed_service_identity OceanAks#managed_service_identity}
        :param max_pods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#max_pods OceanAks#max_pods}.
        :param network: network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#network OceanAks#network}
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#os_disk OceanAks#os_disk}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_group_name OceanAks#resource_group_name}.
        :param strategy: strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#strategy OceanAks#strategy}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#tag OceanAks#tag}
        :param user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#user_name OceanAks#user_name}.
        :param vm_sizes: vm_sizes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#vm_sizes OceanAks#vm_sizes}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#zones OceanAks#zones}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAks.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OceanAksConfig(
            acd_identifier=acd_identifier,
            aks_name=aks_name,
            aks_resource_group_name=aks_resource_group_name,
            name=name,
            ssh_public_key=ssh_public_key,
            autoscaler=autoscaler,
            controller_cluster_id=controller_cluster_id,
            custom_data=custom_data,
            extension=extension,
            health=health,
            id=id,
            image=image,
            load_balancer=load_balancer,
            managed_service_identity=managed_service_identity,
            max_pods=max_pods,
            network=network,
            os_disk=os_disk,
            resource_group_name=resource_group_name,
            strategy=strategy,
            tag=tag,
            user_name=user_name,
            vm_sizes=vm_sizes,
            zones=zones,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAutoscaler")
    def put_autoscaler(
        self,
        *,
        autoscale_down: typing.Optional[typing.Union["OceanAksAutoscalerAutoscaleDown", typing.Dict[str, typing.Any]]] = None,
        autoscale_headroom: typing.Optional[typing.Union["OceanAksAutoscalerAutoscaleHeadroom", typing.Dict[str, typing.Any]]] = None,
        autoscale_is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        resource_limits: typing.Optional[typing.Union["OceanAksAutoscalerResourceLimits", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param autoscale_down: autoscale_down block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#autoscale_down OceanAks#autoscale_down}
        :param autoscale_headroom: autoscale_headroom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#autoscale_headroom OceanAks#autoscale_headroom}
        :param autoscale_is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#autoscale_is_enabled OceanAks#autoscale_is_enabled}.
        :param resource_limits: resource_limits block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_limits OceanAks#resource_limits}
        '''
        value = OceanAksAutoscaler(
            autoscale_down=autoscale_down,
            autoscale_headroom=autoscale_headroom,
            autoscale_is_enabled=autoscale_is_enabled,
            resource_limits=resource_limits,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscaler", [value]))

    @jsii.member(jsii_name="putExtension")
    def put_extension(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksExtension", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAks.put_extension)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExtension", [value]))

    @jsii.member(jsii_name="putHealth")
    def put_health(self, *, grace_period: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#grace_period OceanAks#grace_period}.
        '''
        value = OceanAksHealth(grace_period=grace_period)

        return typing.cast(None, jsii.invoke(self, "putHealth", [value]))

    @jsii.member(jsii_name="putImage")
    def put_image(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksImage", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAks.put_image)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putImage", [value]))

    @jsii.member(jsii_name="putLoadBalancer")
    def put_load_balancer(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksLoadBalancer", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAks.put_load_balancer)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLoadBalancer", [value]))

    @jsii.member(jsii_name="putManagedServiceIdentity")
    def put_managed_service_identity(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksManagedServiceIdentity", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAks.put_managed_service_identity)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putManagedServiceIdentity", [value]))

    @jsii.member(jsii_name="putNetwork")
    def put_network(
        self,
        *,
        network_interface: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksNetworkNetworkInterface", typing.Dict[str, typing.Any]]]]] = None,
        resource_group_name: typing.Optional[builtins.str] = None,
        virtual_network_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#network_interface OceanAks#network_interface}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_group_name OceanAks#resource_group_name}.
        :param virtual_network_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#virtual_network_name OceanAks#virtual_network_name}.
        '''
        value = OceanAksNetwork(
            network_interface=network_interface,
            resource_group_name=resource_group_name,
            virtual_network_name=virtual_network_name,
        )

        return typing.cast(None, jsii.invoke(self, "putNetwork", [value]))

    @jsii.member(jsii_name="putOsDisk")
    def put_os_disk(
        self,
        *,
        size_gb: jsii.Number,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#size_gb OceanAks#size_gb}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#type OceanAks#type}.
        '''
        value = OceanAksOsDisk(size_gb=size_gb, type=type)

        return typing.cast(None, jsii.invoke(self, "putOsDisk", [value]))

    @jsii.member(jsii_name="putStrategy")
    def put_strategy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksStrategy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAks.put_strategy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStrategy", [value]))

    @jsii.member(jsii_name="putTag")
    def put_tag(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksTag", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAks.put_tag)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTag", [value]))

    @jsii.member(jsii_name="putVmSizes")
    def put_vm_sizes(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVmSizes", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAks.put_vm_sizes)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVmSizes", [value]))

    @jsii.member(jsii_name="resetAutoscaler")
    def reset_autoscaler(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaler", []))

    @jsii.member(jsii_name="resetControllerClusterId")
    def reset_controller_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetControllerClusterId", []))

    @jsii.member(jsii_name="resetCustomData")
    def reset_custom_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomData", []))

    @jsii.member(jsii_name="resetExtension")
    def reset_extension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtension", []))

    @jsii.member(jsii_name="resetHealth")
    def reset_health(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealth", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImage")
    def reset_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImage", []))

    @jsii.member(jsii_name="resetLoadBalancer")
    def reset_load_balancer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancer", []))

    @jsii.member(jsii_name="resetManagedServiceIdentity")
    def reset_managed_service_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedServiceIdentity", []))

    @jsii.member(jsii_name="resetMaxPods")
    def reset_max_pods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPods", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetOsDisk")
    def reset_os_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsDisk", []))

    @jsii.member(jsii_name="resetResourceGroupName")
    def reset_resource_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroupName", []))

    @jsii.member(jsii_name="resetStrategy")
    def reset_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStrategy", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="resetUserName")
    def reset_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserName", []))

    @jsii.member(jsii_name="resetVmSizes")
    def reset_vm_sizes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVmSizes", []))

    @jsii.member(jsii_name="resetZones")
    def reset_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZones", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="autoscaler")
    def autoscaler(self) -> "OceanAksAutoscalerOutputReference":
        return typing.cast("OceanAksAutoscalerOutputReference", jsii.get(self, "autoscaler"))

    @builtins.property
    @jsii.member(jsii_name="extension")
    def extension(self) -> "OceanAksExtensionList":
        return typing.cast("OceanAksExtensionList", jsii.get(self, "extension"))

    @builtins.property
    @jsii.member(jsii_name="health")
    def health(self) -> "OceanAksHealthOutputReference":
        return typing.cast("OceanAksHealthOutputReference", jsii.get(self, "health"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> "OceanAksImageList":
        return typing.cast("OceanAksImageList", jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> "OceanAksLoadBalancerList":
        return typing.cast("OceanAksLoadBalancerList", jsii.get(self, "loadBalancer"))

    @builtins.property
    @jsii.member(jsii_name="managedServiceIdentity")
    def managed_service_identity(self) -> "OceanAksManagedServiceIdentityList":
        return typing.cast("OceanAksManagedServiceIdentityList", jsii.get(self, "managedServiceIdentity"))

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> "OceanAksNetworkOutputReference":
        return typing.cast("OceanAksNetworkOutputReference", jsii.get(self, "network"))

    @builtins.property
    @jsii.member(jsii_name="osDisk")
    def os_disk(self) -> "OceanAksOsDiskOutputReference":
        return typing.cast("OceanAksOsDiskOutputReference", jsii.get(self, "osDisk"))

    @builtins.property
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> "OceanAksStrategyList":
        return typing.cast("OceanAksStrategyList", jsii.get(self, "strategy"))

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> "OceanAksTagList":
        return typing.cast("OceanAksTagList", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="vmSizes")
    def vm_sizes(self) -> "OceanAksVmSizesList":
        return typing.cast("OceanAksVmSizesList", jsii.get(self, "vmSizes"))

    @builtins.property
    @jsii.member(jsii_name="acdIdentifierInput")
    def acd_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acdIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="aksNameInput")
    def aks_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aksNameInput"))

    @builtins.property
    @jsii.member(jsii_name="aksResourceGroupNameInput")
    def aks_resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aksResourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscalerInput")
    def autoscaler_input(self) -> typing.Optional["OceanAksAutoscaler"]:
        return typing.cast(typing.Optional["OceanAksAutoscaler"], jsii.get(self, "autoscalerInput"))

    @builtins.property
    @jsii.member(jsii_name="controllerClusterIdInput")
    def controller_cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "controllerClusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="customDataInput")
    def custom_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDataInput"))

    @builtins.property
    @jsii.member(jsii_name="extensionInput")
    def extension_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksExtension"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksExtension"]]], jsii.get(self, "extensionInput"))

    @builtins.property
    @jsii.member(jsii_name="healthInput")
    def health_input(self) -> typing.Optional["OceanAksHealth"]:
        return typing.cast(typing.Optional["OceanAksHealth"], jsii.get(self, "healthInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksImage"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksImage"]]], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInput")
    def load_balancer_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksLoadBalancer"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksLoadBalancer"]]], jsii.get(self, "loadBalancerInput"))

    @builtins.property
    @jsii.member(jsii_name="managedServiceIdentityInput")
    def managed_service_identity_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksManagedServiceIdentity"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksManagedServiceIdentity"]]], jsii.get(self, "managedServiceIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPodsInput")
    def max_pods_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPodsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional["OceanAksNetwork"]:
        return typing.cast(typing.Optional["OceanAksNetwork"], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="osDiskInput")
    def os_disk_input(self) -> typing.Optional["OceanAksOsDisk"]:
        return typing.cast(typing.Optional["OceanAksOsDisk"], jsii.get(self, "osDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeyInput")
    def ssh_public_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshPublicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="strategyInput")
    def strategy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksStrategy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksStrategy"]]], jsii.get(self, "strategyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksTag"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksTag"]]], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameInput")
    def user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameInput"))

    @builtins.property
    @jsii.member(jsii_name="vmSizesInput")
    def vm_sizes_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVmSizes"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVmSizes"]]], jsii.get(self, "vmSizesInput"))

    @builtins.property
    @jsii.member(jsii_name="zonesInput")
    def zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "zonesInput"))

    @builtins.property
    @jsii.member(jsii_name="acdIdentifier")
    def acd_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acdIdentifier"))

    @acd_identifier.setter
    def acd_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAks, "acd_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acdIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="aksName")
    def aks_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aksName"))

    @aks_name.setter
    def aks_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAks, "aks_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aksName", value)

    @builtins.property
    @jsii.member(jsii_name="aksResourceGroupName")
    def aks_resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aksResourceGroupName"))

    @aks_resource_group_name.setter
    def aks_resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAks, "aks_resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aksResourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="controllerClusterId")
    def controller_cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "controllerClusterId"))

    @controller_cluster_id.setter
    def controller_cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAks, "controller_cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "controllerClusterId", value)

    @builtins.property
    @jsii.member(jsii_name="customData")
    def custom_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customData"))

    @custom_data.setter
    def custom_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAks, "custom_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customData", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAks, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxPods")
    def max_pods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPods"))

    @max_pods.setter
    def max_pods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAks, "max_pods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPods", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAks, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAks, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="sshPublicKey")
    def ssh_public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshPublicKey"))

    @ssh_public_key.setter
    def ssh_public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAks, "ssh_public_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicKey", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAks, "user_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="zones")
    def zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "zones"))

    @zones.setter
    def zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAks, "zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zones", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksAutoscaler",
    jsii_struct_bases=[],
    name_mapping={
        "autoscale_down": "autoscaleDown",
        "autoscale_headroom": "autoscaleHeadroom",
        "autoscale_is_enabled": "autoscaleIsEnabled",
        "resource_limits": "resourceLimits",
    },
)
class OceanAksAutoscaler:
    def __init__(
        self,
        *,
        autoscale_down: typing.Optional[typing.Union["OceanAksAutoscalerAutoscaleDown", typing.Dict[str, typing.Any]]] = None,
        autoscale_headroom: typing.Optional[typing.Union["OceanAksAutoscalerAutoscaleHeadroom", typing.Dict[str, typing.Any]]] = None,
        autoscale_is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        resource_limits: typing.Optional[typing.Union["OceanAksAutoscalerResourceLimits", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param autoscale_down: autoscale_down block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#autoscale_down OceanAks#autoscale_down}
        :param autoscale_headroom: autoscale_headroom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#autoscale_headroom OceanAks#autoscale_headroom}
        :param autoscale_is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#autoscale_is_enabled OceanAks#autoscale_is_enabled}.
        :param resource_limits: resource_limits block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_limits OceanAks#resource_limits}
        '''
        if isinstance(autoscale_down, dict):
            autoscale_down = OceanAksAutoscalerAutoscaleDown(**autoscale_down)
        if isinstance(autoscale_headroom, dict):
            autoscale_headroom = OceanAksAutoscalerAutoscaleHeadroom(**autoscale_headroom)
        if isinstance(resource_limits, dict):
            resource_limits = OceanAksAutoscalerResourceLimits(**resource_limits)
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksAutoscaler.__init__)
            check_type(argname="argument autoscale_down", value=autoscale_down, expected_type=type_hints["autoscale_down"])
            check_type(argname="argument autoscale_headroom", value=autoscale_headroom, expected_type=type_hints["autoscale_headroom"])
            check_type(argname="argument autoscale_is_enabled", value=autoscale_is_enabled, expected_type=type_hints["autoscale_is_enabled"])
            check_type(argname="argument resource_limits", value=resource_limits, expected_type=type_hints["resource_limits"])
        self._values: typing.Dict[str, typing.Any] = {}
        if autoscale_down is not None:
            self._values["autoscale_down"] = autoscale_down
        if autoscale_headroom is not None:
            self._values["autoscale_headroom"] = autoscale_headroom
        if autoscale_is_enabled is not None:
            self._values["autoscale_is_enabled"] = autoscale_is_enabled
        if resource_limits is not None:
            self._values["resource_limits"] = resource_limits

    @builtins.property
    def autoscale_down(self) -> typing.Optional["OceanAksAutoscalerAutoscaleDown"]:
        '''autoscale_down block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#autoscale_down OceanAks#autoscale_down}
        '''
        result = self._values.get("autoscale_down")
        return typing.cast(typing.Optional["OceanAksAutoscalerAutoscaleDown"], result)

    @builtins.property
    def autoscale_headroom(
        self,
    ) -> typing.Optional["OceanAksAutoscalerAutoscaleHeadroom"]:
        '''autoscale_headroom block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#autoscale_headroom OceanAks#autoscale_headroom}
        '''
        result = self._values.get("autoscale_headroom")
        return typing.cast(typing.Optional["OceanAksAutoscalerAutoscaleHeadroom"], result)

    @builtins.property
    def autoscale_is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#autoscale_is_enabled OceanAks#autoscale_is_enabled}.'''
        result = self._values.get("autoscale_is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def resource_limits(self) -> typing.Optional["OceanAksAutoscalerResourceLimits"]:
        '''resource_limits block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_limits OceanAks#resource_limits}
        '''
        result = self._values.get("resource_limits")
        return typing.cast(typing.Optional["OceanAksAutoscalerResourceLimits"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksAutoscaler(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksAutoscalerAutoscaleDown",
    jsii_struct_bases=[],
    name_mapping={"max_scale_down_percentage": "maxScaleDownPercentage"},
)
class OceanAksAutoscalerAutoscaleDown:
    def __init__(
        self,
        *,
        max_scale_down_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_scale_down_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#max_scale_down_percentage OceanAks#max_scale_down_percentage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksAutoscalerAutoscaleDown.__init__)
            check_type(argname="argument max_scale_down_percentage", value=max_scale_down_percentage, expected_type=type_hints["max_scale_down_percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_scale_down_percentage is not None:
            self._values["max_scale_down_percentage"] = max_scale_down_percentage

    @builtins.property
    def max_scale_down_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#max_scale_down_percentage OceanAks#max_scale_down_percentage}.'''
        result = self._values.get("max_scale_down_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksAutoscalerAutoscaleDown(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksAutoscalerAutoscaleDownOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksAutoscalerAutoscaleDownOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksAutoscalerAutoscaleDownOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxScaleDownPercentage")
    def reset_max_scale_down_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxScaleDownPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="maxScaleDownPercentageInput")
    def max_scale_down_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxScaleDownPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="maxScaleDownPercentage")
    def max_scale_down_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxScaleDownPercentage"))

    @max_scale_down_percentage.setter
    def max_scale_down_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksAutoscalerAutoscaleDownOutputReference, "max_scale_down_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxScaleDownPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAksAutoscalerAutoscaleDown]:
        return typing.cast(typing.Optional[OceanAksAutoscalerAutoscaleDown], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanAksAutoscalerAutoscaleDown],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksAutoscalerAutoscaleDownOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksAutoscalerAutoscaleHeadroom",
    jsii_struct_bases=[],
    name_mapping={"automatic": "automatic"},
)
class OceanAksAutoscalerAutoscaleHeadroom:
    def __init__(
        self,
        *,
        automatic: typing.Optional[typing.Union["OceanAksAutoscalerAutoscaleHeadroomAutomatic", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param automatic: automatic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#automatic OceanAks#automatic}
        '''
        if isinstance(automatic, dict):
            automatic = OceanAksAutoscalerAutoscaleHeadroomAutomatic(**automatic)
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksAutoscalerAutoscaleHeadroom.__init__)
            check_type(argname="argument automatic", value=automatic, expected_type=type_hints["automatic"])
        self._values: typing.Dict[str, typing.Any] = {}
        if automatic is not None:
            self._values["automatic"] = automatic

    @builtins.property
    def automatic(
        self,
    ) -> typing.Optional["OceanAksAutoscalerAutoscaleHeadroomAutomatic"]:
        '''automatic block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#automatic OceanAks#automatic}
        '''
        result = self._values.get("automatic")
        return typing.cast(typing.Optional["OceanAksAutoscalerAutoscaleHeadroomAutomatic"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksAutoscalerAutoscaleHeadroom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksAutoscalerAutoscaleHeadroomAutomatic",
    jsii_struct_bases=[],
    name_mapping={"is_enabled": "isEnabled", "percentage": "percentage"},
)
class OceanAksAutoscalerAutoscaleHeadroomAutomatic:
    def __init__(
        self,
        *,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#is_enabled OceanAks#is_enabled}.
        :param percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#percentage OceanAks#percentage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksAutoscalerAutoscaleHeadroomAutomatic.__init__)
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if percentage is not None:
            self._values["percentage"] = percentage

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#is_enabled OceanAks#is_enabled}.'''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#percentage OceanAks#percentage}.'''
        result = self._values.get("percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksAutoscalerAutoscaleHeadroomAutomatic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksAutoscalerAutoscaleHeadroomAutomaticOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksAutoscalerAutoscaleHeadroomAutomaticOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksAutoscalerAutoscaleHeadroomAutomaticOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetPercentage")
    def reset_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="percentageInput")
    def percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentageInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksAutoscalerAutoscaleHeadroomAutomaticOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="percentage")
    def percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percentage"))

    @percentage.setter
    def percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksAutoscalerAutoscaleHeadroomAutomaticOutputReference, "percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OceanAksAutoscalerAutoscaleHeadroomAutomatic]:
        return typing.cast(typing.Optional[OceanAksAutoscalerAutoscaleHeadroomAutomatic], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanAksAutoscalerAutoscaleHeadroomAutomatic],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksAutoscalerAutoscaleHeadroomAutomaticOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksAutoscalerAutoscaleHeadroomOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksAutoscalerAutoscaleHeadroomOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksAutoscalerAutoscaleHeadroomOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutomatic")
    def put_automatic(
        self,
        *,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#is_enabled OceanAks#is_enabled}.
        :param percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#percentage OceanAks#percentage}.
        '''
        value = OceanAksAutoscalerAutoscaleHeadroomAutomatic(
            is_enabled=is_enabled, percentage=percentage
        )

        return typing.cast(None, jsii.invoke(self, "putAutomatic", [value]))

    @jsii.member(jsii_name="resetAutomatic")
    def reset_automatic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomatic", []))

    @builtins.property
    @jsii.member(jsii_name="automatic")
    def automatic(self) -> OceanAksAutoscalerAutoscaleHeadroomAutomaticOutputReference:
        return typing.cast(OceanAksAutoscalerAutoscaleHeadroomAutomaticOutputReference, jsii.get(self, "automatic"))

    @builtins.property
    @jsii.member(jsii_name="automaticInput")
    def automatic_input(
        self,
    ) -> typing.Optional[OceanAksAutoscalerAutoscaleHeadroomAutomatic]:
        return typing.cast(typing.Optional[OceanAksAutoscalerAutoscaleHeadroomAutomatic], jsii.get(self, "automaticInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAksAutoscalerAutoscaleHeadroom]:
        return typing.cast(typing.Optional[OceanAksAutoscalerAutoscaleHeadroom], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanAksAutoscalerAutoscaleHeadroom],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksAutoscalerAutoscaleHeadroomOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksAutoscalerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksAutoscalerOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksAutoscalerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutoscaleDown")
    def put_autoscale_down(
        self,
        *,
        max_scale_down_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_scale_down_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#max_scale_down_percentage OceanAks#max_scale_down_percentage}.
        '''
        value = OceanAksAutoscalerAutoscaleDown(
            max_scale_down_percentage=max_scale_down_percentage
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscaleDown", [value]))

    @jsii.member(jsii_name="putAutoscaleHeadroom")
    def put_autoscale_headroom(
        self,
        *,
        automatic: typing.Optional[typing.Union[OceanAksAutoscalerAutoscaleHeadroomAutomatic, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param automatic: automatic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#automatic OceanAks#automatic}
        '''
        value = OceanAksAutoscalerAutoscaleHeadroom(automatic=automatic)

        return typing.cast(None, jsii.invoke(self, "putAutoscaleHeadroom", [value]))

    @jsii.member(jsii_name="putResourceLimits")
    def put_resource_limits(
        self,
        *,
        max_memory_gib: typing.Optional[jsii.Number] = None,
        max_vcpu: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_memory_gib: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#max_memory_gib OceanAks#max_memory_gib}.
        :param max_vcpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#max_vcpu OceanAks#max_vcpu}.
        '''
        value = OceanAksAutoscalerResourceLimits(
            max_memory_gib=max_memory_gib, max_vcpu=max_vcpu
        )

        return typing.cast(None, jsii.invoke(self, "putResourceLimits", [value]))

    @jsii.member(jsii_name="resetAutoscaleDown")
    def reset_autoscale_down(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaleDown", []))

    @jsii.member(jsii_name="resetAutoscaleHeadroom")
    def reset_autoscale_headroom(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaleHeadroom", []))

    @jsii.member(jsii_name="resetAutoscaleIsEnabled")
    def reset_autoscale_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaleIsEnabled", []))

    @jsii.member(jsii_name="resetResourceLimits")
    def reset_resource_limits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceLimits", []))

    @builtins.property
    @jsii.member(jsii_name="autoscaleDown")
    def autoscale_down(self) -> OceanAksAutoscalerAutoscaleDownOutputReference:
        return typing.cast(OceanAksAutoscalerAutoscaleDownOutputReference, jsii.get(self, "autoscaleDown"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleHeadroom")
    def autoscale_headroom(self) -> OceanAksAutoscalerAutoscaleHeadroomOutputReference:
        return typing.cast(OceanAksAutoscalerAutoscaleHeadroomOutputReference, jsii.get(self, "autoscaleHeadroom"))

    @builtins.property
    @jsii.member(jsii_name="resourceLimits")
    def resource_limits(self) -> "OceanAksAutoscalerResourceLimitsOutputReference":
        return typing.cast("OceanAksAutoscalerResourceLimitsOutputReference", jsii.get(self, "resourceLimits"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleDownInput")
    def autoscale_down_input(self) -> typing.Optional[OceanAksAutoscalerAutoscaleDown]:
        return typing.cast(typing.Optional[OceanAksAutoscalerAutoscaleDown], jsii.get(self, "autoscaleDownInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleHeadroomInput")
    def autoscale_headroom_input(
        self,
    ) -> typing.Optional[OceanAksAutoscalerAutoscaleHeadroom]:
        return typing.cast(typing.Optional[OceanAksAutoscalerAutoscaleHeadroom], jsii.get(self, "autoscaleHeadroomInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleIsEnabledInput")
    def autoscale_is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoscaleIsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLimitsInput")
    def resource_limits_input(
        self,
    ) -> typing.Optional["OceanAksAutoscalerResourceLimits"]:
        return typing.cast(typing.Optional["OceanAksAutoscalerResourceLimits"], jsii.get(self, "resourceLimitsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleIsEnabled")
    def autoscale_is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoscaleIsEnabled"))

    @autoscale_is_enabled.setter
    def autoscale_is_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksAutoscalerOutputReference, "autoscale_is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscaleIsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAksAutoscaler]:
        return typing.cast(typing.Optional[OceanAksAutoscaler], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanAksAutoscaler]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksAutoscalerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksAutoscalerResourceLimits",
    jsii_struct_bases=[],
    name_mapping={"max_memory_gib": "maxMemoryGib", "max_vcpu": "maxVcpu"},
)
class OceanAksAutoscalerResourceLimits:
    def __init__(
        self,
        *,
        max_memory_gib: typing.Optional[jsii.Number] = None,
        max_vcpu: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_memory_gib: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#max_memory_gib OceanAks#max_memory_gib}.
        :param max_vcpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#max_vcpu OceanAks#max_vcpu}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksAutoscalerResourceLimits.__init__)
            check_type(argname="argument max_memory_gib", value=max_memory_gib, expected_type=type_hints["max_memory_gib"])
            check_type(argname="argument max_vcpu", value=max_vcpu, expected_type=type_hints["max_vcpu"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_memory_gib is not None:
            self._values["max_memory_gib"] = max_memory_gib
        if max_vcpu is not None:
            self._values["max_vcpu"] = max_vcpu

    @builtins.property
    def max_memory_gib(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#max_memory_gib OceanAks#max_memory_gib}.'''
        result = self._values.get("max_memory_gib")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_vcpu(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#max_vcpu OceanAks#max_vcpu}.'''
        result = self._values.get("max_vcpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksAutoscalerResourceLimits(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksAutoscalerResourceLimitsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksAutoscalerResourceLimitsOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksAutoscalerResourceLimitsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxMemoryGib")
    def reset_max_memory_gib(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxMemoryGib", []))

    @jsii.member(jsii_name="resetMaxVcpu")
    def reset_max_vcpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxVcpu", []))

    @builtins.property
    @jsii.member(jsii_name="maxMemoryGibInput")
    def max_memory_gib_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxMemoryGibInput"))

    @builtins.property
    @jsii.member(jsii_name="maxVcpuInput")
    def max_vcpu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxVcpuInput"))

    @builtins.property
    @jsii.member(jsii_name="maxMemoryGib")
    def max_memory_gib(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxMemoryGib"))

    @max_memory_gib.setter
    def max_memory_gib(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksAutoscalerResourceLimitsOutputReference, "max_memory_gib").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxMemoryGib", value)

    @builtins.property
    @jsii.member(jsii_name="maxVcpu")
    def max_vcpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxVcpu"))

    @max_vcpu.setter
    def max_vcpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksAutoscalerResourceLimitsOutputReference, "max_vcpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxVcpu", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAksAutoscalerResourceLimits]:
        return typing.cast(typing.Optional[OceanAksAutoscalerResourceLimits], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanAksAutoscalerResourceLimits],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksAutoscalerResourceLimitsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "acd_identifier": "acdIdentifier",
        "aks_name": "aksName",
        "aks_resource_group_name": "aksResourceGroupName",
        "name": "name",
        "ssh_public_key": "sshPublicKey",
        "autoscaler": "autoscaler",
        "controller_cluster_id": "controllerClusterId",
        "custom_data": "customData",
        "extension": "extension",
        "health": "health",
        "id": "id",
        "image": "image",
        "load_balancer": "loadBalancer",
        "managed_service_identity": "managedServiceIdentity",
        "max_pods": "maxPods",
        "network": "network",
        "os_disk": "osDisk",
        "resource_group_name": "resourceGroupName",
        "strategy": "strategy",
        "tag": "tag",
        "user_name": "userName",
        "vm_sizes": "vmSizes",
        "zones": "zones",
    },
)
class OceanAksConfig(cdktf.TerraformMetaArguments):
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
        acd_identifier: builtins.str,
        aks_name: builtins.str,
        aks_resource_group_name: builtins.str,
        name: builtins.str,
        ssh_public_key: builtins.str,
        autoscaler: typing.Optional[typing.Union[OceanAksAutoscaler, typing.Dict[str, typing.Any]]] = None,
        controller_cluster_id: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
        extension: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksExtension", typing.Dict[str, typing.Any]]]]] = None,
        health: typing.Optional[typing.Union["OceanAksHealth", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        image: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksImage", typing.Dict[str, typing.Any]]]]] = None,
        load_balancer: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksLoadBalancer", typing.Dict[str, typing.Any]]]]] = None,
        managed_service_identity: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksManagedServiceIdentity", typing.Dict[str, typing.Any]]]]] = None,
        max_pods: typing.Optional[jsii.Number] = None,
        network: typing.Optional[typing.Union["OceanAksNetwork", typing.Dict[str, typing.Any]]] = None,
        os_disk: typing.Optional[typing.Union["OceanAksOsDisk", typing.Dict[str, typing.Any]]] = None,
        resource_group_name: typing.Optional[builtins.str] = None,
        strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksStrategy", typing.Dict[str, typing.Any]]]]] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksTag", typing.Dict[str, typing.Any]]]]] = None,
        user_name: typing.Optional[builtins.str] = None,
        vm_sizes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVmSizes", typing.Dict[str, typing.Any]]]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param acd_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#acd_identifier OceanAks#acd_identifier}.
        :param aks_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#aks_name OceanAks#aks_name}.
        :param aks_resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#aks_resource_group_name OceanAks#aks_resource_group_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#name OceanAks#name}.
        :param ssh_public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#ssh_public_key OceanAks#ssh_public_key}.
        :param autoscaler: autoscaler block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#autoscaler OceanAks#autoscaler}
        :param controller_cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#controller_cluster_id OceanAks#controller_cluster_id}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#custom_data OceanAks#custom_data}.
        :param extension: extension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#extension OceanAks#extension}
        :param health: health block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#health OceanAks#health}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#id OceanAks#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image: image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#image OceanAks#image}
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#load_balancer OceanAks#load_balancer}
        :param managed_service_identity: managed_service_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#managed_service_identity OceanAks#managed_service_identity}
        :param max_pods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#max_pods OceanAks#max_pods}.
        :param network: network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#network OceanAks#network}
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#os_disk OceanAks#os_disk}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_group_name OceanAks#resource_group_name}.
        :param strategy: strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#strategy OceanAks#strategy}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#tag OceanAks#tag}
        :param user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#user_name OceanAks#user_name}.
        :param vm_sizes: vm_sizes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#vm_sizes OceanAks#vm_sizes}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#zones OceanAks#zones}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(autoscaler, dict):
            autoscaler = OceanAksAutoscaler(**autoscaler)
        if isinstance(health, dict):
            health = OceanAksHealth(**health)
        if isinstance(network, dict):
            network = OceanAksNetwork(**network)
        if isinstance(os_disk, dict):
            os_disk = OceanAksOsDisk(**os_disk)
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument acd_identifier", value=acd_identifier, expected_type=type_hints["acd_identifier"])
            check_type(argname="argument aks_name", value=aks_name, expected_type=type_hints["aks_name"])
            check_type(argname="argument aks_resource_group_name", value=aks_resource_group_name, expected_type=type_hints["aks_resource_group_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ssh_public_key", value=ssh_public_key, expected_type=type_hints["ssh_public_key"])
            check_type(argname="argument autoscaler", value=autoscaler, expected_type=type_hints["autoscaler"])
            check_type(argname="argument controller_cluster_id", value=controller_cluster_id, expected_type=type_hints["controller_cluster_id"])
            check_type(argname="argument custom_data", value=custom_data, expected_type=type_hints["custom_data"])
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
            check_type(argname="argument health", value=health, expected_type=type_hints["health"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
            check_type(argname="argument managed_service_identity", value=managed_service_identity, expected_type=type_hints["managed_service_identity"])
            check_type(argname="argument max_pods", value=max_pods, expected_type=type_hints["max_pods"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument os_disk", value=os_disk, expected_type=type_hints["os_disk"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument strategy", value=strategy, expected_type=type_hints["strategy"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument vm_sizes", value=vm_sizes, expected_type=type_hints["vm_sizes"])
            check_type(argname="argument zones", value=zones, expected_type=type_hints["zones"])
        self._values: typing.Dict[str, typing.Any] = {
            "acd_identifier": acd_identifier,
            "aks_name": aks_name,
            "aks_resource_group_name": aks_resource_group_name,
            "name": name,
            "ssh_public_key": ssh_public_key,
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
        if autoscaler is not None:
            self._values["autoscaler"] = autoscaler
        if controller_cluster_id is not None:
            self._values["controller_cluster_id"] = controller_cluster_id
        if custom_data is not None:
            self._values["custom_data"] = custom_data
        if extension is not None:
            self._values["extension"] = extension
        if health is not None:
            self._values["health"] = health
        if id is not None:
            self._values["id"] = id
        if image is not None:
            self._values["image"] = image
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if managed_service_identity is not None:
            self._values["managed_service_identity"] = managed_service_identity
        if max_pods is not None:
            self._values["max_pods"] = max_pods
        if network is not None:
            self._values["network"] = network
        if os_disk is not None:
            self._values["os_disk"] = os_disk
        if resource_group_name is not None:
            self._values["resource_group_name"] = resource_group_name
        if strategy is not None:
            self._values["strategy"] = strategy
        if tag is not None:
            self._values["tag"] = tag
        if user_name is not None:
            self._values["user_name"] = user_name
        if vm_sizes is not None:
            self._values["vm_sizes"] = vm_sizes
        if zones is not None:
            self._values["zones"] = zones

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
    def acd_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#acd_identifier OceanAks#acd_identifier}.'''
        result = self._values.get("acd_identifier")
        assert result is not None, "Required property 'acd_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aks_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#aks_name OceanAks#aks_name}.'''
        result = self._values.get("aks_name")
        assert result is not None, "Required property 'aks_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aks_resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#aks_resource_group_name OceanAks#aks_resource_group_name}.'''
        result = self._values.get("aks_resource_group_name")
        assert result is not None, "Required property 'aks_resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#name OceanAks#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ssh_public_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#ssh_public_key OceanAks#ssh_public_key}.'''
        result = self._values.get("ssh_public_key")
        assert result is not None, "Required property 'ssh_public_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def autoscaler(self) -> typing.Optional[OceanAksAutoscaler]:
        '''autoscaler block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#autoscaler OceanAks#autoscaler}
        '''
        result = self._values.get("autoscaler")
        return typing.cast(typing.Optional[OceanAksAutoscaler], result)

    @builtins.property
    def controller_cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#controller_cluster_id OceanAks#controller_cluster_id}.'''
        result = self._values.get("controller_cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#custom_data OceanAks#custom_data}.'''
        result = self._values.get("custom_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extension(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksExtension"]]]:
        '''extension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#extension OceanAks#extension}
        '''
        result = self._values.get("extension")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksExtension"]]], result)

    @builtins.property
    def health(self) -> typing.Optional["OceanAksHealth"]:
        '''health block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#health OceanAks#health}
        '''
        result = self._values.get("health")
        return typing.cast(typing.Optional["OceanAksHealth"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#id OceanAks#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksImage"]]]:
        '''image block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#image OceanAks#image}
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksImage"]]], result)

    @builtins.property
    def load_balancer(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksLoadBalancer"]]]:
        '''load_balancer block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#load_balancer OceanAks#load_balancer}
        '''
        result = self._values.get("load_balancer")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksLoadBalancer"]]], result)

    @builtins.property
    def managed_service_identity(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksManagedServiceIdentity"]]]:
        '''managed_service_identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#managed_service_identity OceanAks#managed_service_identity}
        '''
        result = self._values.get("managed_service_identity")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksManagedServiceIdentity"]]], result)

    @builtins.property
    def max_pods(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#max_pods OceanAks#max_pods}.'''
        result = self._values.get("max_pods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def network(self) -> typing.Optional["OceanAksNetwork"]:
        '''network block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#network OceanAks#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional["OceanAksNetwork"], result)

    @builtins.property
    def os_disk(self) -> typing.Optional["OceanAksOsDisk"]:
        '''os_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#os_disk OceanAks#os_disk}
        '''
        result = self._values.get("os_disk")
        return typing.cast(typing.Optional["OceanAksOsDisk"], result)

    @builtins.property
    def resource_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_group_name OceanAks#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def strategy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksStrategy"]]]:
        '''strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#strategy OceanAks#strategy}
        '''
        result = self._values.get("strategy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksStrategy"]]], result)

    @builtins.property
    def tag(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksTag"]]]:
        '''tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#tag OceanAks#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksTag"]]], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#user_name OceanAks#user_name}.'''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vm_sizes(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVmSizes"]]]:
        '''vm_sizes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#vm_sizes OceanAks#vm_sizes}
        '''
        result = self._values.get("vm_sizes")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVmSizes"]]], result)

    @builtins.property
    def zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#zones OceanAks#zones}.'''
        result = self._values.get("zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksExtension",
    jsii_struct_bases=[],
    name_mapping={
        "api_version": "apiVersion",
        "minor_version_auto_upgrade": "minorVersionAutoUpgrade",
        "name": "name",
        "publisher": "publisher",
        "type": "type",
    },
)
class OceanAksExtension:
    def __init__(
        self,
        *,
        api_version: typing.Optional[builtins.str] = None,
        minor_version_auto_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        publisher: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#api_version OceanAks#api_version}.
        :param minor_version_auto_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#minor_version_auto_upgrade OceanAks#minor_version_auto_upgrade}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#name OceanAks#name}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#publisher OceanAks#publisher}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#type OceanAks#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksExtension.__init__)
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument minor_version_auto_upgrade", value=minor_version_auto_upgrade, expected_type=type_hints["minor_version_auto_upgrade"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if api_version is not None:
            self._values["api_version"] = api_version
        if minor_version_auto_upgrade is not None:
            self._values["minor_version_auto_upgrade"] = minor_version_auto_upgrade
        if name is not None:
            self._values["name"] = name
        if publisher is not None:
            self._values["publisher"] = publisher
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#api_version OceanAks#api_version}.'''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minor_version_auto_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#minor_version_auto_upgrade OceanAks#minor_version_auto_upgrade}.'''
        result = self._values.get("minor_version_auto_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#name OceanAks#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publisher(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#publisher OceanAks#publisher}.'''
        result = self._values.get("publisher")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#type OceanAks#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksExtension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksExtensionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksExtensionList",
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
            type_hints = typing.get_type_hints(OceanAksExtensionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanAksExtensionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksExtensionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksExtensionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksExtensionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksExtensionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksExtensionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksExtension]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksExtension]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksExtension]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksExtensionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksExtensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksExtensionOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksExtensionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetApiVersion")
    def reset_api_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiVersion", []))

    @jsii.member(jsii_name="resetMinorVersionAutoUpgrade")
    def reset_minor_version_auto_upgrade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinorVersionAutoUpgrade", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPublisher")
    def reset_publisher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublisher", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="apiVersionInput")
    def api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="minorVersionAutoUpgradeInput")
    def minor_version_auto_upgrade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "minorVersionAutoUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherInput")
    def publisher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @api_version.setter
    def api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksExtensionOutputReference, "api_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="minorVersionAutoUpgrade")
    def minor_version_auto_upgrade(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "minorVersionAutoUpgrade"))

    @minor_version_auto_upgrade.setter
    def minor_version_auto_upgrade(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksExtensionOutputReference, "minor_version_auto_upgrade").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minorVersionAutoUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksExtensionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksExtensionOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksExtensionOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksExtension, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksExtension, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksExtension, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksExtensionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksHealth",
    jsii_struct_bases=[],
    name_mapping={"grace_period": "gracePeriod"},
)
class OceanAksHealth:
    def __init__(self, *, grace_period: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#grace_period OceanAks#grace_period}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksHealth.__init__)
            check_type(argname="argument grace_period", value=grace_period, expected_type=type_hints["grace_period"])
        self._values: typing.Dict[str, typing.Any] = {}
        if grace_period is not None:
            self._values["grace_period"] = grace_period

    @builtins.property
    def grace_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#grace_period OceanAks#grace_period}.'''
        result = self._values.get("grace_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksHealth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksHealthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksHealthOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksHealthOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGracePeriod")
    def reset_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGracePeriod", []))

    @builtins.property
    @jsii.member(jsii_name="gracePeriodInput")
    def grace_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gracePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="gracePeriod")
    def grace_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gracePeriod"))

    @grace_period.setter
    def grace_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksHealthOutputReference, "grace_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAksHealth]:
        return typing.cast(typing.Optional[OceanAksHealth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanAksHealth]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksHealthOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksImage",
    jsii_struct_bases=[],
    name_mapping={"marketplace": "marketplace"},
)
class OceanAksImage:
    def __init__(
        self,
        *,
        marketplace: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksImageMarketplace", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param marketplace: marketplace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#marketplace OceanAks#marketplace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksImage.__init__)
            check_type(argname="argument marketplace", value=marketplace, expected_type=type_hints["marketplace"])
        self._values: typing.Dict[str, typing.Any] = {}
        if marketplace is not None:
            self._values["marketplace"] = marketplace

    @builtins.property
    def marketplace(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksImageMarketplace"]]]:
        '''marketplace block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#marketplace OceanAks#marketplace}
        '''
        result = self._values.get("marketplace")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksImageMarketplace"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksImageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksImageList",
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
            type_hints = typing.get_type_hints(OceanAksImageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanAksImageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksImageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksImageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksImageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksImageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksImageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksImage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksImage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksImage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksImageList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksImageMarketplace",
    jsii_struct_bases=[],
    name_mapping={
        "offer": "offer",
        "publisher": "publisher",
        "sku": "sku",
        "version": "version",
    },
)
class OceanAksImageMarketplace:
    def __init__(
        self,
        *,
        offer: typing.Optional[builtins.str] = None,
        publisher: typing.Optional[builtins.str] = None,
        sku: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#offer OceanAks#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#publisher OceanAks#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#sku OceanAks#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#version OceanAks#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksImageMarketplace.__init__)
            check_type(argname="argument offer", value=offer, expected_type=type_hints["offer"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if offer is not None:
            self._values["offer"] = offer
        if publisher is not None:
            self._values["publisher"] = publisher
        if sku is not None:
            self._values["sku"] = sku
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def offer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#offer OceanAks#offer}.'''
        result = self._values.get("offer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publisher(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#publisher OceanAks#publisher}.'''
        result = self._values.get("publisher")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sku(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#sku OceanAks#sku}.'''
        result = self._values.get("sku")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#version OceanAks#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksImageMarketplace(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksImageMarketplaceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksImageMarketplaceList",
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
            type_hints = typing.get_type_hints(OceanAksImageMarketplaceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanAksImageMarketplaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksImageMarketplaceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksImageMarketplaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksImageMarketplaceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksImageMarketplaceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksImageMarketplaceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksImageMarketplace]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksImageMarketplace]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksImageMarketplace]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksImageMarketplaceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksImageMarketplaceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksImageMarketplaceOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksImageMarketplaceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetOffer")
    def reset_offer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOffer", []))

    @jsii.member(jsii_name="resetPublisher")
    def reset_publisher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublisher", []))

    @jsii.member(jsii_name="resetSku")
    def reset_sku(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSku", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="offerInput")
    def offer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "offerInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherInput")
    def publisher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="offer")
    def offer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "offer"))

    @offer.setter
    def offer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksImageMarketplaceOutputReference, "offer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offer", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksImageMarketplaceOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksImageMarketplaceOutputReference, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksImageMarketplaceOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksImageMarketplace, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksImageMarketplace, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksImageMarketplace, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksImageMarketplaceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksImageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksImageOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksImageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMarketplace")
    def put_marketplace(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OceanAksImageMarketplace, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksImageOutputReference.put_marketplace)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMarketplace", [value]))

    @jsii.member(jsii_name="resetMarketplace")
    def reset_marketplace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMarketplace", []))

    @builtins.property
    @jsii.member(jsii_name="marketplace")
    def marketplace(self) -> OceanAksImageMarketplaceList:
        return typing.cast(OceanAksImageMarketplaceList, jsii.get(self, "marketplace"))

    @builtins.property
    @jsii.member(jsii_name="marketplaceInput")
    def marketplace_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksImageMarketplace]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksImageMarketplace]]], jsii.get(self, "marketplaceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksImage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksImage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksImage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksImageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "backend_pool_names": "backendPoolNames",
        "load_balancer_sku": "loadBalancerSku",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "type": "type",
    },
)
class OceanAksLoadBalancer:
    def __init__(
        self,
        *,
        backend_pool_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        load_balancer_sku: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        resource_group_name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backend_pool_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#backend_pool_names OceanAks#backend_pool_names}.
        :param load_balancer_sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#load_balancer_sku OceanAks#load_balancer_sku}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#name OceanAks#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_group_name OceanAks#resource_group_name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#type OceanAks#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksLoadBalancer.__init__)
            check_type(argname="argument backend_pool_names", value=backend_pool_names, expected_type=type_hints["backend_pool_names"])
            check_type(argname="argument load_balancer_sku", value=load_balancer_sku, expected_type=type_hints["load_balancer_sku"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if backend_pool_names is not None:
            self._values["backend_pool_names"] = backend_pool_names
        if load_balancer_sku is not None:
            self._values["load_balancer_sku"] = load_balancer_sku
        if name is not None:
            self._values["name"] = name
        if resource_group_name is not None:
            self._values["resource_group_name"] = resource_group_name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def backend_pool_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#backend_pool_names OceanAks#backend_pool_names}.'''
        result = self._values.get("backend_pool_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def load_balancer_sku(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#load_balancer_sku OceanAks#load_balancer_sku}.'''
        result = self._values.get("load_balancer_sku")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#name OceanAks#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_group_name OceanAks#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#type OceanAks#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksLoadBalancerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksLoadBalancerList",
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
            type_hints = typing.get_type_hints(OceanAksLoadBalancerList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanAksLoadBalancerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksLoadBalancerList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksLoadBalancerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksLoadBalancerList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksLoadBalancerList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksLoadBalancerList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksLoadBalancer]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksLoadBalancer]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksLoadBalancer]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksLoadBalancerList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksLoadBalancerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksLoadBalancerOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksLoadBalancerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBackendPoolNames")
    def reset_backend_pool_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendPoolNames", []))

    @jsii.member(jsii_name="resetLoadBalancerSku")
    def reset_load_balancer_sku(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerSku", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetResourceGroupName")
    def reset_resource_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroupName", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="backendPoolNamesInput")
    def backend_pool_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "backendPoolNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerSkuInput")
    def load_balancer_sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancerSkuInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="backendPoolNames")
    def backend_pool_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "backendPoolNames"))

    @backend_pool_names.setter
    def backend_pool_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksLoadBalancerOutputReference, "backend_pool_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendPoolNames", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerSku")
    def load_balancer_sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancerSku"))

    @load_balancer_sku.setter
    def load_balancer_sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksLoadBalancerOutputReference, "load_balancer_sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerSku", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksLoadBalancerOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksLoadBalancerOutputReference, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksLoadBalancerOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksLoadBalancer, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksLoadBalancer, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksLoadBalancer, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksLoadBalancerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksManagedServiceIdentity",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "resource_group_name": "resourceGroupName"},
)
class OceanAksManagedServiceIdentity:
    def __init__(
        self,
        *,
        name: builtins.str,
        resource_group_name: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#name OceanAks#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_group_name OceanAks#resource_group_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksManagedServiceIdentity.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "resource_group_name": resource_group_name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#name OceanAks#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_group_name OceanAks#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksManagedServiceIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksManagedServiceIdentityList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksManagedServiceIdentityList",
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
            type_hints = typing.get_type_hints(OceanAksManagedServiceIdentityList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OceanAksManagedServiceIdentityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksManagedServiceIdentityList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksManagedServiceIdentityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksManagedServiceIdentityList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksManagedServiceIdentityList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksManagedServiceIdentityList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksManagedServiceIdentity]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksManagedServiceIdentity]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksManagedServiceIdentity]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksManagedServiceIdentityList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksManagedServiceIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksManagedServiceIdentityOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksManagedServiceIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksManagedServiceIdentityOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksManagedServiceIdentityOutputReference, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksManagedServiceIdentity, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksManagedServiceIdentity, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksManagedServiceIdentity, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksManagedServiceIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksNetwork",
    jsii_struct_bases=[],
    name_mapping={
        "network_interface": "networkInterface",
        "resource_group_name": "resourceGroupName",
        "virtual_network_name": "virtualNetworkName",
    },
)
class OceanAksNetwork:
    def __init__(
        self,
        *,
        network_interface: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksNetworkNetworkInterface", typing.Dict[str, typing.Any]]]]] = None,
        resource_group_name: typing.Optional[builtins.str] = None,
        virtual_network_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#network_interface OceanAks#network_interface}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_group_name OceanAks#resource_group_name}.
        :param virtual_network_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#virtual_network_name OceanAks#virtual_network_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksNetwork.__init__)
            check_type(argname="argument network_interface", value=network_interface, expected_type=type_hints["network_interface"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument virtual_network_name", value=virtual_network_name, expected_type=type_hints["virtual_network_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if network_interface is not None:
            self._values["network_interface"] = network_interface
        if resource_group_name is not None:
            self._values["resource_group_name"] = resource_group_name
        if virtual_network_name is not None:
            self._values["virtual_network_name"] = virtual_network_name

    @builtins.property
    def network_interface(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksNetworkNetworkInterface"]]]:
        '''network_interface block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#network_interface OceanAks#network_interface}
        '''
        result = self._values.get("network_interface")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksNetworkNetworkInterface"]]], result)

    @builtins.property
    def resource_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_group_name OceanAks#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_network_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#virtual_network_name OceanAks#virtual_network_name}.'''
        result = self._values.get("virtual_network_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksNetwork(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksNetworkNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={
        "additional_ip_config": "additionalIpConfig",
        "assign_public_ip": "assignPublicIp",
        "is_primary": "isPrimary",
        "security_group": "securityGroup",
        "subnet_name": "subnetName",
    },
)
class OceanAksNetworkNetworkInterface:
    def __init__(
        self,
        *,
        additional_ip_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksNetworkNetworkInterfaceAdditionalIpConfig", typing.Dict[str, typing.Any]]]]] = None,
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_primary: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        security_group: typing.Optional[typing.Union["OceanAksNetworkNetworkInterfaceSecurityGroup", typing.Dict[str, typing.Any]]] = None,
        subnet_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_ip_config: additional_ip_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#additional_ip_config OceanAks#additional_ip_config}
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#assign_public_ip OceanAks#assign_public_ip}.
        :param is_primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#is_primary OceanAks#is_primary}.
        :param security_group: security_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#security_group OceanAks#security_group}
        :param subnet_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#subnet_name OceanAks#subnet_name}.
        '''
        if isinstance(security_group, dict):
            security_group = OceanAksNetworkNetworkInterfaceSecurityGroup(**security_group)
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksNetworkNetworkInterface.__init__)
            check_type(argname="argument additional_ip_config", value=additional_ip_config, expected_type=type_hints["additional_ip_config"])
            check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
            check_type(argname="argument is_primary", value=is_primary, expected_type=type_hints["is_primary"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument subnet_name", value=subnet_name, expected_type=type_hints["subnet_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if additional_ip_config is not None:
            self._values["additional_ip_config"] = additional_ip_config
        if assign_public_ip is not None:
            self._values["assign_public_ip"] = assign_public_ip
        if is_primary is not None:
            self._values["is_primary"] = is_primary
        if security_group is not None:
            self._values["security_group"] = security_group
        if subnet_name is not None:
            self._values["subnet_name"] = subnet_name

    @builtins.property
    def additional_ip_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksNetworkNetworkInterfaceAdditionalIpConfig"]]]:
        '''additional_ip_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#additional_ip_config OceanAks#additional_ip_config}
        '''
        result = self._values.get("additional_ip_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksNetworkNetworkInterfaceAdditionalIpConfig"]]], result)

    @builtins.property
    def assign_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#assign_public_ip OceanAks#assign_public_ip}.'''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#is_primary OceanAks#is_primary}.'''
        result = self._values.get("is_primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def security_group(
        self,
    ) -> typing.Optional["OceanAksNetworkNetworkInterfaceSecurityGroup"]:
        '''security_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#security_group OceanAks#security_group}
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional["OceanAksNetworkNetworkInterfaceSecurityGroup"], result)

    @builtins.property
    def subnet_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#subnet_name OceanAks#subnet_name}.'''
        result = self._values.get("subnet_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksNetworkNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksNetworkNetworkInterfaceAdditionalIpConfig",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "private_ip_version": "privateIpVersion"},
)
class OceanAksNetworkNetworkInterfaceAdditionalIpConfig:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        private_ip_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#name OceanAks#name}.
        :param private_ip_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#private_ip_version OceanAks#private_ip_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksNetworkNetworkInterfaceAdditionalIpConfig.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument private_ip_version", value=private_ip_version, expected_type=type_hints["private_ip_version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if private_ip_version is not None:
            self._values["private_ip_version"] = private_ip_version

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#name OceanAks#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_ip_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#private_ip_version OceanAks#private_ip_version}.'''
        result = self._values.get("private_ip_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksNetworkNetworkInterfaceAdditionalIpConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksNetworkNetworkInterfaceAdditionalIpConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksNetworkNetworkInterfaceAdditionalIpConfigList",
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
            type_hints = typing.get_type_hints(OceanAksNetworkNetworkInterfaceAdditionalIpConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OceanAksNetworkNetworkInterfaceAdditionalIpConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksNetworkNetworkInterfaceAdditionalIpConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksNetworkNetworkInterfaceAdditionalIpConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceAdditionalIpConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceAdditionalIpConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceAdditionalIpConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksNetworkNetworkInterfaceAdditionalIpConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksNetworkNetworkInterfaceAdditionalIpConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksNetworkNetworkInterfaceAdditionalIpConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceAdditionalIpConfigList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksNetworkNetworkInterfaceAdditionalIpConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksNetworkNetworkInterfaceAdditionalIpConfigOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksNetworkNetworkInterfaceAdditionalIpConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPrivateIpVersion")
    def reset_private_ip_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpVersion", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpVersionInput")
    def private_ip_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceAdditionalIpConfigOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpVersion")
    def private_ip_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpVersion"))

    @private_ip_version.setter
    def private_ip_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceAdditionalIpConfigOutputReference, "private_ip_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksNetworkNetworkInterfaceAdditionalIpConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksNetworkNetworkInterfaceAdditionalIpConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksNetworkNetworkInterfaceAdditionalIpConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceAdditionalIpConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksNetworkNetworkInterfaceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksNetworkNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(OceanAksNetworkNetworkInterfaceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OceanAksNetworkNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksNetworkNetworkInterfaceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksNetworkNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksNetworkNetworkInterface]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksNetworkNetworkInterface]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksNetworkNetworkInterface]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksNetworkNetworkInterfaceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksNetworkNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksNetworkNetworkInterfaceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAdditionalIpConfig")
    def put_additional_ip_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OceanAksNetworkNetworkInterfaceAdditionalIpConfig, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksNetworkNetworkInterfaceOutputReference.put_additional_ip_config)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdditionalIpConfig", [value]))

    @jsii.member(jsii_name="putSecurityGroup")
    def put_security_group(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        resource_group_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#name OceanAks#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_group_name OceanAks#resource_group_name}.
        '''
        value = OceanAksNetworkNetworkInterfaceSecurityGroup(
            name=name, resource_group_name=resource_group_name
        )

        return typing.cast(None, jsii.invoke(self, "putSecurityGroup", [value]))

    @jsii.member(jsii_name="resetAdditionalIpConfig")
    def reset_additional_ip_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalIpConfig", []))

    @jsii.member(jsii_name="resetAssignPublicIp")
    def reset_assign_public_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssignPublicIp", []))

    @jsii.member(jsii_name="resetIsPrimary")
    def reset_is_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsPrimary", []))

    @jsii.member(jsii_name="resetSecurityGroup")
    def reset_security_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroup", []))

    @jsii.member(jsii_name="resetSubnetName")
    def reset_subnet_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetName", []))

    @builtins.property
    @jsii.member(jsii_name="additionalIpConfig")
    def additional_ip_config(
        self,
    ) -> OceanAksNetworkNetworkInterfaceAdditionalIpConfigList:
        return typing.cast(OceanAksNetworkNetworkInterfaceAdditionalIpConfigList, jsii.get(self, "additionalIpConfig"))

    @builtins.property
    @jsii.member(jsii_name="securityGroup")
    def security_group(
        self,
    ) -> "OceanAksNetworkNetworkInterfaceSecurityGroupOutputReference":
        return typing.cast("OceanAksNetworkNetworkInterfaceSecurityGroupOutputReference", jsii.get(self, "securityGroup"))

    @builtins.property
    @jsii.member(jsii_name="additionalIpConfigInput")
    def additional_ip_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksNetworkNetworkInterfaceAdditionalIpConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksNetworkNetworkInterfaceAdditionalIpConfig]]], jsii.get(self, "additionalIpConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIpInput")
    def assign_public_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "assignPublicIpInput"))

    @builtins.property
    @jsii.member(jsii_name="isPrimaryInput")
    def is_primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isPrimaryInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupInput")
    def security_group_input(
        self,
    ) -> typing.Optional["OceanAksNetworkNetworkInterfaceSecurityGroup"]:
        return typing.cast(typing.Optional["OceanAksNetworkNetworkInterfaceSecurityGroup"], jsii.get(self, "securityGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetNameInput")
    def subnet_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIp")
    def assign_public_ip(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "assignPublicIp"))

    @assign_public_ip.setter
    def assign_public_ip(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceOutputReference, "assign_public_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assignPublicIp", value)

    @builtins.property
    @jsii.member(jsii_name="isPrimary")
    def is_primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isPrimary"))

    @is_primary.setter
    def is_primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceOutputReference, "is_primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isPrimary", value)

    @builtins.property
    @jsii.member(jsii_name="subnetName")
    def subnet_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetName"))

    @subnet_name.setter
    def subnet_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceOutputReference, "subnet_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksNetworkNetworkInterface, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksNetworkNetworkInterface, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksNetworkNetworkInterface, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksNetworkNetworkInterfaceSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "resource_group_name": "resourceGroupName"},
)
class OceanAksNetworkNetworkInterfaceSecurityGroup:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        resource_group_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#name OceanAks#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_group_name OceanAks#resource_group_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksNetworkNetworkInterfaceSecurityGroup.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if resource_group_name is not None:
            self._values["resource_group_name"] = resource_group_name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#name OceanAks#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#resource_group_name OceanAks#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksNetworkNetworkInterfaceSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksNetworkNetworkInterfaceSecurityGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksNetworkNetworkInterfaceSecurityGroupOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksNetworkNetworkInterfaceSecurityGroupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetResourceGroupName")
    def reset_resource_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroupName", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceSecurityGroupOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceSecurityGroupOutputReference, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OceanAksNetworkNetworkInterfaceSecurityGroup]:
        return typing.cast(typing.Optional[OceanAksNetworkNetworkInterfaceSecurityGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanAksNetworkNetworkInterfaceSecurityGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkNetworkInterfaceSecurityGroupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksNetworkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksNetworkOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksNetworkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNetworkInterface")
    def put_network_interface(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OceanAksNetworkNetworkInterface, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksNetworkOutputReference.put_network_interface)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkInterface", [value]))

    @jsii.member(jsii_name="resetNetworkInterface")
    def reset_network_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkInterface", []))

    @jsii.member(jsii_name="resetResourceGroupName")
    def reset_resource_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroupName", []))

    @jsii.member(jsii_name="resetVirtualNetworkName")
    def reset_virtual_network_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkName", []))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(self) -> OceanAksNetworkNetworkInterfaceList:
        return typing.cast(OceanAksNetworkNetworkInterfaceList, jsii.get(self, "networkInterface"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceInput")
    def network_interface_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksNetworkNetworkInterface]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksNetworkNetworkInterface]]], jsii.get(self, "networkInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkNameInput")
    def virtual_network_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkNameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkOutputReference, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkName")
    def virtual_network_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkName"))

    @virtual_network_name.setter
    def virtual_network_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkOutputReference, "virtual_network_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAksNetwork]:
        return typing.cast(typing.Optional[OceanAksNetwork], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanAksNetwork]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksNetworkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksOsDisk",
    jsii_struct_bases=[],
    name_mapping={"size_gb": "sizeGb", "type": "type"},
)
class OceanAksOsDisk:
    def __init__(
        self,
        *,
        size_gb: jsii.Number,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#size_gb OceanAks#size_gb}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#type OceanAks#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksOsDisk.__init__)
            check_type(argname="argument size_gb", value=size_gb, expected_type=type_hints["size_gb"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "size_gb": size_gb,
        }
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def size_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#size_gb OceanAks#size_gb}.'''
        result = self._values.get("size_gb")
        assert result is not None, "Required property 'size_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#type OceanAks#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksOsDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksOsDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksOsDiskOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksOsDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="sizeGbInput")
    def size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeGb")
    def size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeGb"))

    @size_gb.setter
    def size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksOsDiskOutputReference, "size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksOsDiskOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAksOsDisk]:
        return typing.cast(typing.Optional[OceanAksOsDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanAksOsDisk]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksOsDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "fallback_to_ondemand": "fallbackToOndemand",
        "spot_percentage": "spotPercentage",
    },
)
class OceanAksStrategy:
    def __init__(
        self,
        *,
        fallback_to_ondemand: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        spot_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fallback_to_ondemand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#fallback_to_ondemand OceanAks#fallback_to_ondemand}.
        :param spot_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#spot_percentage OceanAks#spot_percentage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksStrategy.__init__)
            check_type(argname="argument fallback_to_ondemand", value=fallback_to_ondemand, expected_type=type_hints["fallback_to_ondemand"])
            check_type(argname="argument spot_percentage", value=spot_percentage, expected_type=type_hints["spot_percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fallback_to_ondemand is not None:
            self._values["fallback_to_ondemand"] = fallback_to_ondemand
        if spot_percentage is not None:
            self._values["spot_percentage"] = spot_percentage

    @builtins.property
    def fallback_to_ondemand(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#fallback_to_ondemand OceanAks#fallback_to_ondemand}.'''
        result = self._values.get("fallback_to_ondemand")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def spot_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#spot_percentage OceanAks#spot_percentage}.'''
        result = self._values.get("spot_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksStrategyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksStrategyList",
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
            type_hints = typing.get_type_hints(OceanAksStrategyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanAksStrategyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksStrategyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksStrategyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksStrategyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksStrategyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksStrategyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksStrategy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksStrategy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksStrategyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksStrategyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksStrategyOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksStrategyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetFallbackToOndemand")
    def reset_fallback_to_ondemand(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFallbackToOndemand", []))

    @jsii.member(jsii_name="resetSpotPercentage")
    def reset_spot_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="fallbackToOndemandInput")
    def fallback_to_ondemand_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fallbackToOndemandInput"))

    @builtins.property
    @jsii.member(jsii_name="spotPercentageInput")
    def spot_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "spotPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="fallbackToOndemand")
    def fallback_to_ondemand(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fallbackToOndemand"))

    @fallback_to_ondemand.setter
    def fallback_to_ondemand(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksStrategyOutputReference, "fallback_to_ondemand").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fallbackToOndemand", value)

    @builtins.property
    @jsii.member(jsii_name="spotPercentage")
    def spot_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotPercentage"))

    @spot_percentage.setter
    def spot_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksStrategyOutputReference, "spot_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksStrategy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksStrategy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksStrategy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksStrategyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksTag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class OceanAksTag:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#key OceanAks#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#value OceanAks#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksTag.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#key OceanAks#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#value OceanAks#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksTagList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksTagList",
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
            type_hints = typing.get_type_hints(OceanAksTagList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanAksTagOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksTagList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksTagOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksTagList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksTagList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksTagList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksTag]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksTag]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksTag]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksTagList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksTagOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksTagOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksTagOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksTagOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksTagOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksTag, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksTag, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksTag, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksTagOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksVmSizes",
    jsii_struct_bases=[],
    name_mapping={"whitelist": "whitelist"},
)
class OceanAksVmSizes:
    def __init__(
        self,
        *,
        whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param whitelist: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#whitelist OceanAks#whitelist}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVmSizes.__init__)
            check_type(argname="argument whitelist", value=whitelist, expected_type=type_hints["whitelist"])
        self._values: typing.Dict[str, typing.Any] = {}
        if whitelist is not None:
            self._values["whitelist"] = whitelist

    @builtins.property
    def whitelist(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks#whitelist OceanAks#whitelist}.'''
        result = self._values.get("whitelist")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksVmSizes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksVmSizesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksVmSizesList",
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
            type_hints = typing.get_type_hints(OceanAksVmSizesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanAksVmSizesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVmSizesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksVmSizesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVmSizesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVmSizesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVmSizesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVmSizes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVmSizes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVmSizes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVmSizesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksVmSizesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAks.OceanAksVmSizesOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksVmSizesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetWhitelist")
    def reset_whitelist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhitelist", []))

    @builtins.property
    @jsii.member(jsii_name="whitelistInput")
    def whitelist_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "whitelistInput"))

    @builtins.property
    @jsii.member(jsii_name="whitelist")
    def whitelist(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "whitelist"))

    @whitelist.setter
    def whitelist(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVmSizesOutputReference, "whitelist").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whitelist", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksVmSizes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksVmSizes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksVmSizes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVmSizesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OceanAks",
    "OceanAksAutoscaler",
    "OceanAksAutoscalerAutoscaleDown",
    "OceanAksAutoscalerAutoscaleDownOutputReference",
    "OceanAksAutoscalerAutoscaleHeadroom",
    "OceanAksAutoscalerAutoscaleHeadroomAutomatic",
    "OceanAksAutoscalerAutoscaleHeadroomAutomaticOutputReference",
    "OceanAksAutoscalerAutoscaleHeadroomOutputReference",
    "OceanAksAutoscalerOutputReference",
    "OceanAksAutoscalerResourceLimits",
    "OceanAksAutoscalerResourceLimitsOutputReference",
    "OceanAksConfig",
    "OceanAksExtension",
    "OceanAksExtensionList",
    "OceanAksExtensionOutputReference",
    "OceanAksHealth",
    "OceanAksHealthOutputReference",
    "OceanAksImage",
    "OceanAksImageList",
    "OceanAksImageMarketplace",
    "OceanAksImageMarketplaceList",
    "OceanAksImageMarketplaceOutputReference",
    "OceanAksImageOutputReference",
    "OceanAksLoadBalancer",
    "OceanAksLoadBalancerList",
    "OceanAksLoadBalancerOutputReference",
    "OceanAksManagedServiceIdentity",
    "OceanAksManagedServiceIdentityList",
    "OceanAksManagedServiceIdentityOutputReference",
    "OceanAksNetwork",
    "OceanAksNetworkNetworkInterface",
    "OceanAksNetworkNetworkInterfaceAdditionalIpConfig",
    "OceanAksNetworkNetworkInterfaceAdditionalIpConfigList",
    "OceanAksNetworkNetworkInterfaceAdditionalIpConfigOutputReference",
    "OceanAksNetworkNetworkInterfaceList",
    "OceanAksNetworkNetworkInterfaceOutputReference",
    "OceanAksNetworkNetworkInterfaceSecurityGroup",
    "OceanAksNetworkNetworkInterfaceSecurityGroupOutputReference",
    "OceanAksNetworkOutputReference",
    "OceanAksOsDisk",
    "OceanAksOsDiskOutputReference",
    "OceanAksStrategy",
    "OceanAksStrategyList",
    "OceanAksStrategyOutputReference",
    "OceanAksTag",
    "OceanAksTagList",
    "OceanAksTagOutputReference",
    "OceanAksVmSizes",
    "OceanAksVmSizesList",
    "OceanAksVmSizesOutputReference",
]

publication.publish()
