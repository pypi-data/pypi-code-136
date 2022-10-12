'''
# `spotinst_elastigroup_azure_v3`

Refer to the Terraform Registory for docs: [`spotinst_elastigroup_azure_v3`](https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3).
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


class ElastigroupAzureV3(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3 spotinst_elastigroup_azure_v3}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        network: typing.Union["ElastigroupAzureV3Network", typing.Dict[str, typing.Any]],
        od_sizes: typing.Sequence[builtins.str],
        os: builtins.str,
        region: builtins.str,
        resource_group_name: builtins.str,
        spot_sizes: typing.Sequence[builtins.str],
        strategy: typing.Union["ElastigroupAzureV3Strategy", typing.Dict[str, typing.Any]],
        custom_data: typing.Optional[builtins.str] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        image: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureV3Image", typing.Dict[str, typing.Any]]]]] = None,
        login: typing.Optional[typing.Union["ElastigroupAzureV3Login", typing.Dict[str, typing.Any]]] = None,
        managed_service_identity: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureV3ManagedServiceIdentity", typing.Dict[str, typing.Any]]]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3 spotinst_elastigroup_azure_v3} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#name ElastigroupAzureV3#name}.
        :param network: network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#network ElastigroupAzureV3#network}
        :param od_sizes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#od_sizes ElastigroupAzureV3#od_sizes}.
        :param os: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#os ElastigroupAzureV3#os}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#region ElastigroupAzureV3#region}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#resource_group_name ElastigroupAzureV3#resource_group_name}.
        :param spot_sizes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#spot_sizes ElastigroupAzureV3#spot_sizes}.
        :param strategy: strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#strategy ElastigroupAzureV3#strategy}
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#custom_data ElastigroupAzureV3#custom_data}.
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#desired_capacity ElastigroupAzureV3#desired_capacity}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#id ElastigroupAzureV3#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image: image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#image ElastigroupAzureV3#image}
        :param login: login block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#login ElastigroupAzureV3#login}
        :param managed_service_identity: managed_service_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#managed_service_identity ElastigroupAzureV3#managed_service_identity}
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#max_size ElastigroupAzureV3#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#min_size ElastigroupAzureV3#min_size}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ElastigroupAzureV3Config(
            name=name,
            network=network,
            od_sizes=od_sizes,
            os=os,
            region=region,
            resource_group_name=resource_group_name,
            spot_sizes=spot_sizes,
            strategy=strategy,
            custom_data=custom_data,
            desired_capacity=desired_capacity,
            id=id,
            image=image,
            login=login,
            managed_service_identity=managed_service_identity,
            max_size=max_size,
            min_size=min_size,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putImage")
    def put_image(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureV3Image", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3.put_image)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putImage", [value]))

    @jsii.member(jsii_name="putLogin")
    def put_login(
        self,
        *,
        user_name: builtins.str,
        password: typing.Optional[builtins.str] = None,
        ssh_public_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#user_name ElastigroupAzureV3#user_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#password ElastigroupAzureV3#password}.
        :param ssh_public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#ssh_public_key ElastigroupAzureV3#ssh_public_key}.
        '''
        value = ElastigroupAzureV3Login(
            user_name=user_name, password=password, ssh_public_key=ssh_public_key
        )

        return typing.cast(None, jsii.invoke(self, "putLogin", [value]))

    @jsii.member(jsii_name="putManagedServiceIdentity")
    def put_managed_service_identity(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureV3ManagedServiceIdentity", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3.put_managed_service_identity)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putManagedServiceIdentity", [value]))

    @jsii.member(jsii_name="putNetwork")
    def put_network(
        self,
        *,
        network_interfaces: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureV3NetworkNetworkInterfaces", typing.Dict[str, typing.Any]]]],
        resource_group_name: builtins.str,
        virtual_network_name: builtins.str,
    ) -> None:
        '''
        :param network_interfaces: network_interfaces block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#network_interfaces ElastigroupAzureV3#network_interfaces}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#resource_group_name ElastigroupAzureV3#resource_group_name}.
        :param virtual_network_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#virtual_network_name ElastigroupAzureV3#virtual_network_name}.
        '''
        value = ElastigroupAzureV3Network(
            network_interfaces=network_interfaces,
            resource_group_name=resource_group_name,
            virtual_network_name=virtual_network_name,
        )

        return typing.cast(None, jsii.invoke(self, "putNetwork", [value]))

    @jsii.member(jsii_name="putStrategy")
    def put_strategy(
        self,
        *,
        draining_timeout: typing.Optional[jsii.Number] = None,
        fallback_to_on_demand: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        od_count: typing.Optional[jsii.Number] = None,
        spot_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param draining_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#draining_timeout ElastigroupAzureV3#draining_timeout}.
        :param fallback_to_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#fallback_to_on_demand ElastigroupAzureV3#fallback_to_on_demand}.
        :param od_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#od_count ElastigroupAzureV3#od_count}.
        :param spot_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#spot_percentage ElastigroupAzureV3#spot_percentage}.
        '''
        value = ElastigroupAzureV3Strategy(
            draining_timeout=draining_timeout,
            fallback_to_on_demand=fallback_to_on_demand,
            od_count=od_count,
            spot_percentage=spot_percentage,
        )

        return typing.cast(None, jsii.invoke(self, "putStrategy", [value]))

    @jsii.member(jsii_name="resetCustomData")
    def reset_custom_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomData", []))

    @jsii.member(jsii_name="resetDesiredCapacity")
    def reset_desired_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredCapacity", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImage")
    def reset_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImage", []))

    @jsii.member(jsii_name="resetLogin")
    def reset_login(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogin", []))

    @jsii.member(jsii_name="resetManagedServiceIdentity")
    def reset_managed_service_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedServiceIdentity", []))

    @jsii.member(jsii_name="resetMaxSize")
    def reset_max_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxSize", []))

    @jsii.member(jsii_name="resetMinSize")
    def reset_min_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinSize", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> "ElastigroupAzureV3ImageList":
        return typing.cast("ElastigroupAzureV3ImageList", jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="login")
    def login(self) -> "ElastigroupAzureV3LoginOutputReference":
        return typing.cast("ElastigroupAzureV3LoginOutputReference", jsii.get(self, "login"))

    @builtins.property
    @jsii.member(jsii_name="managedServiceIdentity")
    def managed_service_identity(
        self,
    ) -> "ElastigroupAzureV3ManagedServiceIdentityList":
        return typing.cast("ElastigroupAzureV3ManagedServiceIdentityList", jsii.get(self, "managedServiceIdentity"))

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> "ElastigroupAzureV3NetworkOutputReference":
        return typing.cast("ElastigroupAzureV3NetworkOutputReference", jsii.get(self, "network"))

    @builtins.property
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> "ElastigroupAzureV3StrategyOutputReference":
        return typing.cast("ElastigroupAzureV3StrategyOutputReference", jsii.get(self, "strategy"))

    @builtins.property
    @jsii.member(jsii_name="customDataInput")
    def custom_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDataInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredCapacityInput")
    def desired_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3Image"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3Image"]]], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="loginInput")
    def login_input(self) -> typing.Optional["ElastigroupAzureV3Login"]:
        return typing.cast(typing.Optional["ElastigroupAzureV3Login"], jsii.get(self, "loginInput"))

    @builtins.property
    @jsii.member(jsii_name="managedServiceIdentityInput")
    def managed_service_identity_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3ManagedServiceIdentity"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3ManagedServiceIdentity"]]], jsii.get(self, "managedServiceIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSizeInput")
    def max_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="minSizeInput")
    def min_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional["ElastigroupAzureV3Network"]:
        return typing.cast(typing.Optional["ElastigroupAzureV3Network"], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="odSizesInput")
    def od_sizes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "odSizesInput"))

    @builtins.property
    @jsii.member(jsii_name="osInput")
    def os_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="spotSizesInput")
    def spot_sizes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "spotSizesInput"))

    @builtins.property
    @jsii.member(jsii_name="strategyInput")
    def strategy_input(self) -> typing.Optional["ElastigroupAzureV3Strategy"]:
        return typing.cast(typing.Optional["ElastigroupAzureV3Strategy"], jsii.get(self, "strategyInput"))

    @builtins.property
    @jsii.member(jsii_name="customData")
    def custom_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customData"))

    @custom_data.setter
    def custom_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3, "custom_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customData", value)

    @builtins.property
    @jsii.member(jsii_name="desiredCapacity")
    def desired_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredCapacity"))

    @desired_capacity.setter
    def desired_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3, "desired_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSize"))

    @max_size.setter
    def max_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3, "max_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSize", value)

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3, "min_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="odSizes")
    def od_sizes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "odSizes"))

    @od_sizes.setter
    def od_sizes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3, "od_sizes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "odSizes", value)

    @builtins.property
    @jsii.member(jsii_name="os")
    def os(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "os"))

    @os.setter
    def os(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3, "os").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "os", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="spotSizes")
    def spot_sizes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "spotSizes"))

    @spot_sizes.setter
    def spot_sizes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3, "spot_sizes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotSizes", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3Config",
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
        "network": "network",
        "od_sizes": "odSizes",
        "os": "os",
        "region": "region",
        "resource_group_name": "resourceGroupName",
        "spot_sizes": "spotSizes",
        "strategy": "strategy",
        "custom_data": "customData",
        "desired_capacity": "desiredCapacity",
        "id": "id",
        "image": "image",
        "login": "login",
        "managed_service_identity": "managedServiceIdentity",
        "max_size": "maxSize",
        "min_size": "minSize",
    },
)
class ElastigroupAzureV3Config(cdktf.TerraformMetaArguments):
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
        network: typing.Union["ElastigroupAzureV3Network", typing.Dict[str, typing.Any]],
        od_sizes: typing.Sequence[builtins.str],
        os: builtins.str,
        region: builtins.str,
        resource_group_name: builtins.str,
        spot_sizes: typing.Sequence[builtins.str],
        strategy: typing.Union["ElastigroupAzureV3Strategy", typing.Dict[str, typing.Any]],
        custom_data: typing.Optional[builtins.str] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        image: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureV3Image", typing.Dict[str, typing.Any]]]]] = None,
        login: typing.Optional[typing.Union["ElastigroupAzureV3Login", typing.Dict[str, typing.Any]]] = None,
        managed_service_identity: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureV3ManagedServiceIdentity", typing.Dict[str, typing.Any]]]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#name ElastigroupAzureV3#name}.
        :param network: network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#network ElastigroupAzureV3#network}
        :param od_sizes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#od_sizes ElastigroupAzureV3#od_sizes}.
        :param os: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#os ElastigroupAzureV3#os}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#region ElastigroupAzureV3#region}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#resource_group_name ElastigroupAzureV3#resource_group_name}.
        :param spot_sizes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#spot_sizes ElastigroupAzureV3#spot_sizes}.
        :param strategy: strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#strategy ElastigroupAzureV3#strategy}
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#custom_data ElastigroupAzureV3#custom_data}.
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#desired_capacity ElastigroupAzureV3#desired_capacity}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#id ElastigroupAzureV3#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image: image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#image ElastigroupAzureV3#image}
        :param login: login block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#login ElastigroupAzureV3#login}
        :param managed_service_identity: managed_service_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#managed_service_identity ElastigroupAzureV3#managed_service_identity}
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#max_size ElastigroupAzureV3#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#min_size ElastigroupAzureV3#min_size}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(network, dict):
            network = ElastigroupAzureV3Network(**network)
        if isinstance(strategy, dict):
            strategy = ElastigroupAzureV3Strategy(**strategy)
        if isinstance(login, dict):
            login = ElastigroupAzureV3Login(**login)
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3Config.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument od_sizes", value=od_sizes, expected_type=type_hints["od_sizes"])
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument spot_sizes", value=spot_sizes, expected_type=type_hints["spot_sizes"])
            check_type(argname="argument strategy", value=strategy, expected_type=type_hints["strategy"])
            check_type(argname="argument custom_data", value=custom_data, expected_type=type_hints["custom_data"])
            check_type(argname="argument desired_capacity", value=desired_capacity, expected_type=type_hints["desired_capacity"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument login", value=login, expected_type=type_hints["login"])
            check_type(argname="argument managed_service_identity", value=managed_service_identity, expected_type=type_hints["managed_service_identity"])
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "network": network,
            "od_sizes": od_sizes,
            "os": os,
            "region": region,
            "resource_group_name": resource_group_name,
            "spot_sizes": spot_sizes,
            "strategy": strategy,
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
        if custom_data is not None:
            self._values["custom_data"] = custom_data
        if desired_capacity is not None:
            self._values["desired_capacity"] = desired_capacity
        if id is not None:
            self._values["id"] = id
        if image is not None:
            self._values["image"] = image
        if login is not None:
            self._values["login"] = login
        if managed_service_identity is not None:
            self._values["managed_service_identity"] = managed_service_identity
        if max_size is not None:
            self._values["max_size"] = max_size
        if min_size is not None:
            self._values["min_size"] = min_size

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#name ElastigroupAzureV3#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network(self) -> "ElastigroupAzureV3Network":
        '''network block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#network ElastigroupAzureV3#network}
        '''
        result = self._values.get("network")
        assert result is not None, "Required property 'network' is missing"
        return typing.cast("ElastigroupAzureV3Network", result)

    @builtins.property
    def od_sizes(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#od_sizes ElastigroupAzureV3#od_sizes}.'''
        result = self._values.get("od_sizes")
        assert result is not None, "Required property 'od_sizes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def os(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#os ElastigroupAzureV3#os}.'''
        result = self._values.get("os")
        assert result is not None, "Required property 'os' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#region ElastigroupAzureV3#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#resource_group_name ElastigroupAzureV3#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spot_sizes(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#spot_sizes ElastigroupAzureV3#spot_sizes}.'''
        result = self._values.get("spot_sizes")
        assert result is not None, "Required property 'spot_sizes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def strategy(self) -> "ElastigroupAzureV3Strategy":
        '''strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#strategy ElastigroupAzureV3#strategy}
        '''
        result = self._values.get("strategy")
        assert result is not None, "Required property 'strategy' is missing"
        return typing.cast("ElastigroupAzureV3Strategy", result)

    @builtins.property
    def custom_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#custom_data ElastigroupAzureV3#custom_data}.'''
        result = self._values.get("custom_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def desired_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#desired_capacity ElastigroupAzureV3#desired_capacity}.'''
        result = self._values.get("desired_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#id ElastigroupAzureV3#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3Image"]]]:
        '''image block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#image ElastigroupAzureV3#image}
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3Image"]]], result)

    @builtins.property
    def login(self) -> typing.Optional["ElastigroupAzureV3Login"]:
        '''login block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#login ElastigroupAzureV3#login}
        '''
        result = self._values.get("login")
        return typing.cast(typing.Optional["ElastigroupAzureV3Login"], result)

    @builtins.property
    def managed_service_identity(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3ManagedServiceIdentity"]]]:
        '''managed_service_identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#managed_service_identity ElastigroupAzureV3#managed_service_identity}
        '''
        result = self._values.get("managed_service_identity")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3ManagedServiceIdentity"]]], result)

    @builtins.property
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#max_size ElastigroupAzureV3#max_size}.'''
        result = self._values.get("max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#min_size ElastigroupAzureV3#min_size}.'''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureV3Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3Image",
    jsii_struct_bases=[],
    name_mapping={"custom": "custom", "marketplace": "marketplace"},
)
class ElastigroupAzureV3Image:
    def __init__(
        self,
        *,
        custom: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureV3ImageCustom", typing.Dict[str, typing.Any]]]]] = None,
        marketplace: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureV3ImageMarketplace", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param custom: custom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#custom ElastigroupAzureV3#custom}
        :param marketplace: marketplace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#marketplace ElastigroupAzureV3#marketplace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3Image.__init__)
            check_type(argname="argument custom", value=custom, expected_type=type_hints["custom"])
            check_type(argname="argument marketplace", value=marketplace, expected_type=type_hints["marketplace"])
        self._values: typing.Dict[str, typing.Any] = {}
        if custom is not None:
            self._values["custom"] = custom
        if marketplace is not None:
            self._values["marketplace"] = marketplace

    @builtins.property
    def custom(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3ImageCustom"]]]:
        '''custom block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#custom ElastigroupAzureV3#custom}
        '''
        result = self._values.get("custom")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3ImageCustom"]]], result)

    @builtins.property
    def marketplace(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3ImageMarketplace"]]]:
        '''marketplace block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#marketplace ElastigroupAzureV3#marketplace}
        '''
        result = self._values.get("marketplace")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3ImageMarketplace"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureV3Image(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3ImageCustom",
    jsii_struct_bases=[],
    name_mapping={
        "image_name": "imageName",
        "resource_group_name": "resourceGroupName",
    },
)
class ElastigroupAzureV3ImageCustom:
    def __init__(
        self,
        *,
        image_name: builtins.str,
        resource_group_name: builtins.str,
    ) -> None:
        '''
        :param image_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#image_name ElastigroupAzureV3#image_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#resource_group_name ElastigroupAzureV3#resource_group_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3ImageCustom.__init__)
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "image_name": image_name,
            "resource_group_name": resource_group_name,
        }

    @builtins.property
    def image_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#image_name ElastigroupAzureV3#image_name}.'''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#resource_group_name ElastigroupAzureV3#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureV3ImageCustom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureV3ImageCustomList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3ImageCustomList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3ImageCustomList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ElastigroupAzureV3ImageCustomOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3ImageCustomList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureV3ImageCustomOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageCustomList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageCustomList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageCustomList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3ImageCustom]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3ImageCustom]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3ImageCustom]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageCustomList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureV3ImageCustomOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3ImageCustomOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3ImageCustomOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="imageNameInput")
    def image_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageCustomOutputReference, "image_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageCustomOutputReference, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureV3ImageCustom, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureV3ImageCustom, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureV3ImageCustom, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageCustomOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureV3ImageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3ImageList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3ImageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ElastigroupAzureV3ImageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3ImageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureV3ImageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3Image]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3Image]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3Image]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3ImageMarketplace",
    jsii_struct_bases=[],
    name_mapping={
        "offer": "offer",
        "publisher": "publisher",
        "sku": "sku",
        "version": "version",
    },
)
class ElastigroupAzureV3ImageMarketplace:
    def __init__(
        self,
        *,
        offer: builtins.str,
        publisher: builtins.str,
        sku: builtins.str,
        version: builtins.str,
    ) -> None:
        '''
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#offer ElastigroupAzureV3#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#publisher ElastigroupAzureV3#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#sku ElastigroupAzureV3#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#version ElastigroupAzureV3#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3ImageMarketplace.__init__)
            check_type(argname="argument offer", value=offer, expected_type=type_hints["offer"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "offer": offer,
            "publisher": publisher,
            "sku": sku,
            "version": version,
        }

    @builtins.property
    def offer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#offer ElastigroupAzureV3#offer}.'''
        result = self._values.get("offer")
        assert result is not None, "Required property 'offer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#publisher ElastigroupAzureV3#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#sku ElastigroupAzureV3#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#version ElastigroupAzureV3#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureV3ImageMarketplace(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureV3ImageMarketplaceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3ImageMarketplaceList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3ImageMarketplaceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupAzureV3ImageMarketplaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3ImageMarketplaceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureV3ImageMarketplaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageMarketplaceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageMarketplaceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageMarketplaceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3ImageMarketplace]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3ImageMarketplace]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3ImageMarketplace]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageMarketplaceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureV3ImageMarketplaceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3ImageMarketplaceOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3ImageMarketplaceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageMarketplaceOutputReference, "offer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offer", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageMarketplaceOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageMarketplaceOutputReference, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageMarketplaceOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureV3ImageMarketplace, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureV3ImageMarketplace, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureV3ImageMarketplace, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageMarketplaceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureV3ImageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3ImageOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3ImageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCustom")
    def put_custom(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupAzureV3ImageCustom, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3ImageOutputReference.put_custom)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustom", [value]))

    @jsii.member(jsii_name="putMarketplace")
    def put_marketplace(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupAzureV3ImageMarketplace, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3ImageOutputReference.put_marketplace)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMarketplace", [value]))

    @jsii.member(jsii_name="resetCustom")
    def reset_custom(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustom", []))

    @jsii.member(jsii_name="resetMarketplace")
    def reset_marketplace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMarketplace", []))

    @builtins.property
    @jsii.member(jsii_name="custom")
    def custom(self) -> ElastigroupAzureV3ImageCustomList:
        return typing.cast(ElastigroupAzureV3ImageCustomList, jsii.get(self, "custom"))

    @builtins.property
    @jsii.member(jsii_name="marketplace")
    def marketplace(self) -> ElastigroupAzureV3ImageMarketplaceList:
        return typing.cast(ElastigroupAzureV3ImageMarketplaceList, jsii.get(self, "marketplace"))

    @builtins.property
    @jsii.member(jsii_name="customInput")
    def custom_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3ImageCustom]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3ImageCustom]]], jsii.get(self, "customInput"))

    @builtins.property
    @jsii.member(jsii_name="marketplaceInput")
    def marketplace_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3ImageMarketplace]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3ImageMarketplace]]], jsii.get(self, "marketplaceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureV3Image, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureV3Image, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureV3Image, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ImageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3Login",
    jsii_struct_bases=[],
    name_mapping={
        "user_name": "userName",
        "password": "password",
        "ssh_public_key": "sshPublicKey",
    },
)
class ElastigroupAzureV3Login:
    def __init__(
        self,
        *,
        user_name: builtins.str,
        password: typing.Optional[builtins.str] = None,
        ssh_public_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#user_name ElastigroupAzureV3#user_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#password ElastigroupAzureV3#password}.
        :param ssh_public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#ssh_public_key ElastigroupAzureV3#ssh_public_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3Login.__init__)
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument ssh_public_key", value=ssh_public_key, expected_type=type_hints["ssh_public_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "user_name": user_name,
        }
        if password is not None:
            self._values["password"] = password
        if ssh_public_key is not None:
            self._values["ssh_public_key"] = ssh_public_key

    @builtins.property
    def user_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#user_name ElastigroupAzureV3#user_name}.'''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#password ElastigroupAzureV3#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssh_public_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#ssh_public_key ElastigroupAzureV3#ssh_public_key}.'''
        result = self._values.get("ssh_public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureV3Login(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureV3LoginOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3LoginOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3LoginOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetSshPublicKey")
    def reset_ssh_public_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshPublicKey", []))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeyInput")
    def ssh_public_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshPublicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameInput")
    def user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3LoginOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="sshPublicKey")
    def ssh_public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshPublicKey"))

    @ssh_public_key.setter
    def ssh_public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3LoginOutputReference, "ssh_public_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicKey", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3LoginOutputReference, "user_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastigroupAzureV3Login]:
        return typing.cast(typing.Optional[ElastigroupAzureV3Login], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ElastigroupAzureV3Login]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3LoginOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3ManagedServiceIdentity",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "resource_group_name": "resourceGroupName"},
)
class ElastigroupAzureV3ManagedServiceIdentity:
    def __init__(
        self,
        *,
        name: builtins.str,
        resource_group_name: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#name ElastigroupAzureV3#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#resource_group_name ElastigroupAzureV3#resource_group_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3ManagedServiceIdentity.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "resource_group_name": resource_group_name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#name ElastigroupAzureV3#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#resource_group_name ElastigroupAzureV3#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureV3ManagedServiceIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureV3ManagedServiceIdentityList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3ManagedServiceIdentityList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3ManagedServiceIdentityList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupAzureV3ManagedServiceIdentityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3ManagedServiceIdentityList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureV3ManagedServiceIdentityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ManagedServiceIdentityList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ManagedServiceIdentityList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ManagedServiceIdentityList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3ManagedServiceIdentity]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3ManagedServiceIdentity]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3ManagedServiceIdentity]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ManagedServiceIdentityList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureV3ManagedServiceIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3ManagedServiceIdentityOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3ManagedServiceIdentityOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ManagedServiceIdentityOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ManagedServiceIdentityOutputReference, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureV3ManagedServiceIdentity, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureV3ManagedServiceIdentity, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureV3ManagedServiceIdentity, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3ManagedServiceIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3Network",
    jsii_struct_bases=[],
    name_mapping={
        "network_interfaces": "networkInterfaces",
        "resource_group_name": "resourceGroupName",
        "virtual_network_name": "virtualNetworkName",
    },
)
class ElastigroupAzureV3Network:
    def __init__(
        self,
        *,
        network_interfaces: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureV3NetworkNetworkInterfaces", typing.Dict[str, typing.Any]]]],
        resource_group_name: builtins.str,
        virtual_network_name: builtins.str,
    ) -> None:
        '''
        :param network_interfaces: network_interfaces block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#network_interfaces ElastigroupAzureV3#network_interfaces}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#resource_group_name ElastigroupAzureV3#resource_group_name}.
        :param virtual_network_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#virtual_network_name ElastigroupAzureV3#virtual_network_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3Network.__init__)
            check_type(argname="argument network_interfaces", value=network_interfaces, expected_type=type_hints["network_interfaces"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument virtual_network_name", value=virtual_network_name, expected_type=type_hints["virtual_network_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "network_interfaces": network_interfaces,
            "resource_group_name": resource_group_name,
            "virtual_network_name": virtual_network_name,
        }

    @builtins.property
    def network_interfaces(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3NetworkNetworkInterfaces"]]:
        '''network_interfaces block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#network_interfaces ElastigroupAzureV3#network_interfaces}
        '''
        result = self._values.get("network_interfaces")
        assert result is not None, "Required property 'network_interfaces' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3NetworkNetworkInterfaces"]], result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#resource_group_name ElastigroupAzureV3#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_network_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#virtual_network_name ElastigroupAzureV3#virtual_network_name}.'''
        result = self._values.get("virtual_network_name")
        assert result is not None, "Required property 'virtual_network_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureV3Network(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3NetworkNetworkInterfaces",
    jsii_struct_bases=[],
    name_mapping={
        "assign_public_ip": "assignPublicIp",
        "is_primary": "isPrimary",
        "subnet_name": "subnetName",
        "additional_ip_configs": "additionalIpConfigs",
        "application_security_group": "applicationSecurityGroup",
    },
)
class ElastigroupAzureV3NetworkNetworkInterfaces:
    def __init__(
        self,
        *,
        assign_public_ip: typing.Union[builtins.bool, cdktf.IResolvable],
        is_primary: typing.Union[builtins.bool, cdktf.IResolvable],
        subnet_name: builtins.str,
        additional_ip_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs", typing.Dict[str, typing.Any]]]]] = None,
        application_security_group: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#assign_public_ip ElastigroupAzureV3#assign_public_ip}.
        :param is_primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#is_primary ElastigroupAzureV3#is_primary}.
        :param subnet_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#subnet_name ElastigroupAzureV3#subnet_name}.
        :param additional_ip_configs: additional_ip_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#additional_ip_configs ElastigroupAzureV3#additional_ip_configs}
        :param application_security_group: application_security_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#application_security_group ElastigroupAzureV3#application_security_group}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkNetworkInterfaces.__init__)
            check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
            check_type(argname="argument is_primary", value=is_primary, expected_type=type_hints["is_primary"])
            check_type(argname="argument subnet_name", value=subnet_name, expected_type=type_hints["subnet_name"])
            check_type(argname="argument additional_ip_configs", value=additional_ip_configs, expected_type=type_hints["additional_ip_configs"])
            check_type(argname="argument application_security_group", value=application_security_group, expected_type=type_hints["application_security_group"])
        self._values: typing.Dict[str, typing.Any] = {
            "assign_public_ip": assign_public_ip,
            "is_primary": is_primary,
            "subnet_name": subnet_name,
        }
        if additional_ip_configs is not None:
            self._values["additional_ip_configs"] = additional_ip_configs
        if application_security_group is not None:
            self._values["application_security_group"] = application_security_group

    @builtins.property
    def assign_public_ip(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#assign_public_ip ElastigroupAzureV3#assign_public_ip}.'''
        result = self._values.get("assign_public_ip")
        assert result is not None, "Required property 'assign_public_ip' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def is_primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#is_primary ElastigroupAzureV3#is_primary}.'''
        result = self._values.get("is_primary")
        assert result is not None, "Required property 'is_primary' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def subnet_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#subnet_name ElastigroupAzureV3#subnet_name}.'''
        result = self._values.get("subnet_name")
        assert result is not None, "Required property 'subnet_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_ip_configs(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs"]]]:
        '''additional_ip_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#additional_ip_configs ElastigroupAzureV3#additional_ip_configs}
        '''
        result = self._values.get("additional_ip_configs")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs"]]], result)

    @builtins.property
    def application_security_group(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup"]]]:
        '''application_security_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#application_security_group ElastigroupAzureV3#application_security_group}
        '''
        result = self._values.get("application_security_group")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureV3NetworkNetworkInterfaces(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "private_ip_version": "privateIpVersion"},
)
class ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs:
    def __init__(
        self,
        *,
        name: builtins.str,
        private_ip_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#name ElastigroupAzureV3#name}.
        :param private_ip_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#private_ip_version ElastigroupAzureV3#private_ip_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument private_ip_version", value=private_ip_version, expected_type=type_hints["private_ip_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if private_ip_version is not None:
            self._values["private_ip_version"] = private_ip_version

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#name ElastigroupAzureV3#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_ip_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#private_ip_version ElastigroupAzureV3#private_ip_version}.'''
        result = self._values.get("private_ip_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpVersion")
    def private_ip_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpVersion"))

    @private_ip_version.setter
    def private_ip_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsOutputReference, "private_ip_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "resource_group_name": "resourceGroupName"},
)
class ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup:
    def __init__(
        self,
        *,
        name: builtins.str,
        resource_group_name: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#name ElastigroupAzureV3#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#resource_group_name ElastigroupAzureV3#resource_group_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "resource_group_name": resource_group_name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#name ElastigroupAzureV3#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#resource_group_name ElastigroupAzureV3#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupOutputReference, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureV3NetworkNetworkInterfacesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3NetworkNetworkInterfacesList",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkNetworkInterfacesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupAzureV3NetworkNetworkInterfacesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkNetworkInterfacesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupAzureV3NetworkNetworkInterfacesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3NetworkNetworkInterfaces]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3NetworkNetworkInterfaces]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3NetworkNetworkInterfaces]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureV3NetworkNetworkInterfacesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3NetworkNetworkInterfacesOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkNetworkInterfacesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAdditionalIpConfigs")
    def put_additional_ip_configs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkNetworkInterfacesOutputReference.put_additional_ip_configs)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdditionalIpConfigs", [value]))

    @jsii.member(jsii_name="putApplicationSecurityGroup")
    def put_application_security_group(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkNetworkInterfacesOutputReference.put_application_security_group)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putApplicationSecurityGroup", [value]))

    @jsii.member(jsii_name="resetAdditionalIpConfigs")
    def reset_additional_ip_configs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalIpConfigs", []))

    @jsii.member(jsii_name="resetApplicationSecurityGroup")
    def reset_application_security_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationSecurityGroup", []))

    @builtins.property
    @jsii.member(jsii_name="additionalIpConfigs")
    def additional_ip_configs(
        self,
    ) -> ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsList:
        return typing.cast(ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsList, jsii.get(self, "additionalIpConfigs"))

    @builtins.property
    @jsii.member(jsii_name="applicationSecurityGroup")
    def application_security_group(
        self,
    ) -> ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupList:
        return typing.cast(ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupList, jsii.get(self, "applicationSecurityGroup"))

    @builtins.property
    @jsii.member(jsii_name="additionalIpConfigsInput")
    def additional_ip_configs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs]]], jsii.get(self, "additionalIpConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationSecurityGroupInput")
    def application_security_group_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup]]], jsii.get(self, "applicationSecurityGroupInput"))

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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesOutputReference, "assign_public_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assignPublicIp", value)

    @builtins.property
    @jsii.member(jsii_name="isPrimary")
    def is_primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isPrimary"))

    @is_primary.setter
    def is_primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesOutputReference, "is_primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isPrimary", value)

    @builtins.property
    @jsii.member(jsii_name="subnetName")
    def subnet_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetName"))

    @subnet_name.setter
    def subnet_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesOutputReference, "subnet_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupAzureV3NetworkNetworkInterfaces, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupAzureV3NetworkNetworkInterfaces, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupAzureV3NetworkNetworkInterfaces, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkNetworkInterfacesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupAzureV3NetworkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3NetworkOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNetworkInterfaces")
    def put_network_interfaces(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupAzureV3NetworkNetworkInterfaces, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3NetworkOutputReference.put_network_interfaces)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkInterfaces", [value]))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaces")
    def network_interfaces(self) -> ElastigroupAzureV3NetworkNetworkInterfacesList:
        return typing.cast(ElastigroupAzureV3NetworkNetworkInterfacesList, jsii.get(self, "networkInterfaces"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfacesInput")
    def network_interfaces_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3NetworkNetworkInterfaces]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupAzureV3NetworkNetworkInterfaces]]], jsii.get(self, "networkInterfacesInput"))

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
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkOutputReference, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkName")
    def virtual_network_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkName"))

    @virtual_network_name.setter
    def virtual_network_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkOutputReference, "virtual_network_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastigroupAzureV3Network]:
        return typing.cast(typing.Optional[ElastigroupAzureV3Network], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ElastigroupAzureV3Network]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3NetworkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3Strategy",
    jsii_struct_bases=[],
    name_mapping={
        "draining_timeout": "drainingTimeout",
        "fallback_to_on_demand": "fallbackToOnDemand",
        "od_count": "odCount",
        "spot_percentage": "spotPercentage",
    },
)
class ElastigroupAzureV3Strategy:
    def __init__(
        self,
        *,
        draining_timeout: typing.Optional[jsii.Number] = None,
        fallback_to_on_demand: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        od_count: typing.Optional[jsii.Number] = None,
        spot_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param draining_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#draining_timeout ElastigroupAzureV3#draining_timeout}.
        :param fallback_to_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#fallback_to_on_demand ElastigroupAzureV3#fallback_to_on_demand}.
        :param od_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#od_count ElastigroupAzureV3#od_count}.
        :param spot_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#spot_percentage ElastigroupAzureV3#spot_percentage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupAzureV3Strategy.__init__)
            check_type(argname="argument draining_timeout", value=draining_timeout, expected_type=type_hints["draining_timeout"])
            check_type(argname="argument fallback_to_on_demand", value=fallback_to_on_demand, expected_type=type_hints["fallback_to_on_demand"])
            check_type(argname="argument od_count", value=od_count, expected_type=type_hints["od_count"])
            check_type(argname="argument spot_percentage", value=spot_percentage, expected_type=type_hints["spot_percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if draining_timeout is not None:
            self._values["draining_timeout"] = draining_timeout
        if fallback_to_on_demand is not None:
            self._values["fallback_to_on_demand"] = fallback_to_on_demand
        if od_count is not None:
            self._values["od_count"] = od_count
        if spot_percentage is not None:
            self._values["spot_percentage"] = spot_percentage

    @builtins.property
    def draining_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#draining_timeout ElastigroupAzureV3#draining_timeout}.'''
        result = self._values.get("draining_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fallback_to_on_demand(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#fallback_to_on_demand ElastigroupAzureV3#fallback_to_on_demand}.'''
        result = self._values.get("fallback_to_on_demand")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def od_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#od_count ElastigroupAzureV3#od_count}.'''
        result = self._values.get("od_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spot_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure_v3#spot_percentage ElastigroupAzureV3#spot_percentage}.'''
        result = self._values.get("spot_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupAzureV3Strategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupAzureV3StrategyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupAzureV3.ElastigroupAzureV3StrategyOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupAzureV3StrategyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDrainingTimeout")
    def reset_draining_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDrainingTimeout", []))

    @jsii.member(jsii_name="resetFallbackToOnDemand")
    def reset_fallback_to_on_demand(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFallbackToOnDemand", []))

    @jsii.member(jsii_name="resetOdCount")
    def reset_od_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOdCount", []))

    @jsii.member(jsii_name="resetSpotPercentage")
    def reset_spot_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="drainingTimeoutInput")
    def draining_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "drainingTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="fallbackToOnDemandInput")
    def fallback_to_on_demand_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fallbackToOnDemandInput"))

    @builtins.property
    @jsii.member(jsii_name="odCountInput")
    def od_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "odCountInput"))

    @builtins.property
    @jsii.member(jsii_name="spotPercentageInput")
    def spot_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "spotPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="drainingTimeout")
    def draining_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "drainingTimeout"))

    @draining_timeout.setter
    def draining_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3StrategyOutputReference, "draining_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "drainingTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="fallbackToOnDemand")
    def fallback_to_on_demand(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fallbackToOnDemand"))

    @fallback_to_on_demand.setter
    def fallback_to_on_demand(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3StrategyOutputReference, "fallback_to_on_demand").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fallbackToOnDemand", value)

    @builtins.property
    @jsii.member(jsii_name="odCount")
    def od_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "odCount"))

    @od_count.setter
    def od_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3StrategyOutputReference, "od_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "odCount", value)

    @builtins.property
    @jsii.member(jsii_name="spotPercentage")
    def spot_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotPercentage"))

    @spot_percentage.setter
    def spot_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3StrategyOutputReference, "spot_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastigroupAzureV3Strategy]:
        return typing.cast(typing.Optional[ElastigroupAzureV3Strategy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastigroupAzureV3Strategy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupAzureV3StrategyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ElastigroupAzureV3",
    "ElastigroupAzureV3Config",
    "ElastigroupAzureV3Image",
    "ElastigroupAzureV3ImageCustom",
    "ElastigroupAzureV3ImageCustomList",
    "ElastigroupAzureV3ImageCustomOutputReference",
    "ElastigroupAzureV3ImageList",
    "ElastigroupAzureV3ImageMarketplace",
    "ElastigroupAzureV3ImageMarketplaceList",
    "ElastigroupAzureV3ImageMarketplaceOutputReference",
    "ElastigroupAzureV3ImageOutputReference",
    "ElastigroupAzureV3Login",
    "ElastigroupAzureV3LoginOutputReference",
    "ElastigroupAzureV3ManagedServiceIdentity",
    "ElastigroupAzureV3ManagedServiceIdentityList",
    "ElastigroupAzureV3ManagedServiceIdentityOutputReference",
    "ElastigroupAzureV3Network",
    "ElastigroupAzureV3NetworkNetworkInterfaces",
    "ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigs",
    "ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsList",
    "ElastigroupAzureV3NetworkNetworkInterfacesAdditionalIpConfigsOutputReference",
    "ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroup",
    "ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupList",
    "ElastigroupAzureV3NetworkNetworkInterfacesApplicationSecurityGroupOutputReference",
    "ElastigroupAzureV3NetworkNetworkInterfacesList",
    "ElastigroupAzureV3NetworkNetworkInterfacesOutputReference",
    "ElastigroupAzureV3NetworkOutputReference",
    "ElastigroupAzureV3Strategy",
    "ElastigroupAzureV3StrategyOutputReference",
]

publication.publish()
