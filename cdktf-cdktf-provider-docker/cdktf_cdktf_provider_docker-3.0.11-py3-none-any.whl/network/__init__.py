'''
# `docker_network`

Refer to the Terraform Registory for docs: [`docker_network`](https://www.terraform.io/docs/providers/docker/r/network).
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


class Network(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.network.Network",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/docker/r/network docker_network}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        attachable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        check_duplicate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        driver: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ingress: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        internal: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ipam_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkIpamConfig", typing.Dict[str, typing.Any]]]]] = None,
        ipam_driver: typing.Optional[builtins.str] = None,
        ipv6: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkLabels", typing.Dict[str, typing.Any]]]]] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/docker/r/network docker_network} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the Docker network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#name Network#name}
        :param attachable: Enable manual container attachment to the network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#attachable Network#attachable}
        :param check_duplicate: Requests daemon to check for networks with same name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#check_duplicate Network#check_duplicate}
        :param driver: The driver of the Docker network. Possible values are ``bridge``, ``host``, ``overlay``, ``macvlan``. See `network docs <https://docs.docker.com/network/#network-drivers>`_ for more details. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#driver Network#driver}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#id Network#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ingress: Create swarm routing-mesh network. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#ingress Network#ingress}
        :param internal: Whether the network is internal. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#internal Network#internal}
        :param ipam_config: ipam_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#ipam_config Network#ipam_config}
        :param ipam_driver: Driver used by the custom IP scheme of the network. Defaults to ``default``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#ipam_driver Network#ipam_driver}
        :param ipv6: Enable IPv6 networking. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#ipv6 Network#ipv6}
        :param labels: labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#labels Network#labels}
        :param options: Only available with bridge networks. See `bridge options docs <https://docs.docker.com/engine/reference/commandline/network_create/#bridge-driver-options>`_ for more details. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#options Network#options}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Network.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NetworkConfig(
            name=name,
            attachable=attachable,
            check_duplicate=check_duplicate,
            driver=driver,
            id=id,
            ingress=ingress,
            internal=internal,
            ipam_config=ipam_config,
            ipam_driver=ipam_driver,
            ipv6=ipv6,
            labels=labels,
            options=options,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putIpamConfig")
    def put_ipam_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkIpamConfig", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Network.put_ipam_config)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpamConfig", [value]))

    @jsii.member(jsii_name="putLabels")
    def put_labels(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkLabels", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Network.put_labels)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLabels", [value]))

    @jsii.member(jsii_name="resetAttachable")
    def reset_attachable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttachable", []))

    @jsii.member(jsii_name="resetCheckDuplicate")
    def reset_check_duplicate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckDuplicate", []))

    @jsii.member(jsii_name="resetDriver")
    def reset_driver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriver", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIngress")
    def reset_ingress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngress", []))

    @jsii.member(jsii_name="resetInternal")
    def reset_internal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternal", []))

    @jsii.member(jsii_name="resetIpamConfig")
    def reset_ipam_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpamConfig", []))

    @jsii.member(jsii_name="resetIpamDriver")
    def reset_ipam_driver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpamDriver", []))

    @jsii.member(jsii_name="resetIpv6")
    def reset_ipv6(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="ipamConfig")
    def ipam_config(self) -> "NetworkIpamConfigList":
        return typing.cast("NetworkIpamConfigList", jsii.get(self, "ipamConfig"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> "NetworkLabelsList":
        return typing.cast("NetworkLabelsList", jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @builtins.property
    @jsii.member(jsii_name="attachableInput")
    def attachable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "attachableInput"))

    @builtins.property
    @jsii.member(jsii_name="checkDuplicateInput")
    def check_duplicate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "checkDuplicateInput"))

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressInput")
    def ingress_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ingressInput"))

    @builtins.property
    @jsii.member(jsii_name="internalInput")
    def internal_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "internalInput"))

    @builtins.property
    @jsii.member(jsii_name="ipamConfigInput")
    def ipam_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkIpamConfig"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkIpamConfig"]]], jsii.get(self, "ipamConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="ipamDriverInput")
    def ipam_driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipamDriverInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6Input")
    def ipv6_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ipv6Input"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkLabels"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkLabels"]]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="attachable")
    def attachable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "attachable"))

    @attachable.setter
    def attachable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Network, "attachable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attachable", value)

    @builtins.property
    @jsii.member(jsii_name="checkDuplicate")
    def check_duplicate(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "checkDuplicate"))

    @check_duplicate.setter
    def check_duplicate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Network, "check_duplicate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkDuplicate", value)

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @driver.setter
    def driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Network, "driver").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driver", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Network, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ingress")
    def ingress(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ingress"))

    @ingress.setter
    def ingress(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Network, "ingress").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingress", value)

    @builtins.property
    @jsii.member(jsii_name="internal")
    def internal(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "internal"))

    @internal.setter
    def internal(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Network, "internal").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internal", value)

    @builtins.property
    @jsii.member(jsii_name="ipamDriver")
    def ipam_driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipamDriver"))

    @ipam_driver.setter
    def ipam_driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Network, "ipam_driver").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipamDriver", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6")
    def ipv6(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ipv6"))

    @ipv6.setter
    def ipv6(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Network, "ipv6").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Network, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Network, "options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.network.NetworkConfig",
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
        "attachable": "attachable",
        "check_duplicate": "checkDuplicate",
        "driver": "driver",
        "id": "id",
        "ingress": "ingress",
        "internal": "internal",
        "ipam_config": "ipamConfig",
        "ipam_driver": "ipamDriver",
        "ipv6": "ipv6",
        "labels": "labels",
        "options": "options",
    },
)
class NetworkConfig(cdktf.TerraformMetaArguments):
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
        attachable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        check_duplicate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        driver: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ingress: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        internal: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ipam_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkIpamConfig", typing.Dict[str, typing.Any]]]]] = None,
        ipam_driver: typing.Optional[builtins.str] = None,
        ipv6: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkLabels", typing.Dict[str, typing.Any]]]]] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the Docker network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#name Network#name}
        :param attachable: Enable manual container attachment to the network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#attachable Network#attachable}
        :param check_duplicate: Requests daemon to check for networks with same name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#check_duplicate Network#check_duplicate}
        :param driver: The driver of the Docker network. Possible values are ``bridge``, ``host``, ``overlay``, ``macvlan``. See `network docs <https://docs.docker.com/network/#network-drivers>`_ for more details. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#driver Network#driver}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#id Network#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ingress: Create swarm routing-mesh network. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#ingress Network#ingress}
        :param internal: Whether the network is internal. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#internal Network#internal}
        :param ipam_config: ipam_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#ipam_config Network#ipam_config}
        :param ipam_driver: Driver used by the custom IP scheme of the network. Defaults to ``default``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#ipam_driver Network#ipam_driver}
        :param ipv6: Enable IPv6 networking. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#ipv6 Network#ipv6}
        :param labels: labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#labels Network#labels}
        :param options: Only available with bridge networks. See `bridge options docs <https://docs.docker.com/engine/reference/commandline/network_create/#bridge-driver-options>`_ for more details. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#options Network#options}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument attachable", value=attachable, expected_type=type_hints["attachable"])
            check_type(argname="argument check_duplicate", value=check_duplicate, expected_type=type_hints["check_duplicate"])
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ingress", value=ingress, expected_type=type_hints["ingress"])
            check_type(argname="argument internal", value=internal, expected_type=type_hints["internal"])
            check_type(argname="argument ipam_config", value=ipam_config, expected_type=type_hints["ipam_config"])
            check_type(argname="argument ipam_driver", value=ipam_driver, expected_type=type_hints["ipam_driver"])
            check_type(argname="argument ipv6", value=ipv6, expected_type=type_hints["ipv6"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if attachable is not None:
            self._values["attachable"] = attachable
        if check_duplicate is not None:
            self._values["check_duplicate"] = check_duplicate
        if driver is not None:
            self._values["driver"] = driver
        if id is not None:
            self._values["id"] = id
        if ingress is not None:
            self._values["ingress"] = ingress
        if internal is not None:
            self._values["internal"] = internal
        if ipam_config is not None:
            self._values["ipam_config"] = ipam_config
        if ipam_driver is not None:
            self._values["ipam_driver"] = ipam_driver
        if ipv6 is not None:
            self._values["ipv6"] = ipv6
        if labels is not None:
            self._values["labels"] = labels
        if options is not None:
            self._values["options"] = options

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
        '''The name of the Docker network.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#name Network#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attachable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable manual container attachment to the network.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#attachable Network#attachable}
        '''
        result = self._values.get("attachable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def check_duplicate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Requests daemon to check for networks with same name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#check_duplicate Network#check_duplicate}
        '''
        result = self._values.get("check_duplicate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def driver(self) -> typing.Optional[builtins.str]:
        '''The driver of the Docker network. Possible values are ``bridge``, ``host``, ``overlay``, ``macvlan``. See `network docs <https://docs.docker.com/network/#network-drivers>`_ for more details.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#driver Network#driver}
        '''
        result = self._values.get("driver")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#id Network#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingress(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Create swarm routing-mesh network. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#ingress Network#ingress}
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def internal(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the network is internal.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#internal Network#internal}
        '''
        result = self._values.get("internal")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ipam_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkIpamConfig"]]]:
        '''ipam_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#ipam_config Network#ipam_config}
        '''
        result = self._values.get("ipam_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkIpamConfig"]]], result)

    @builtins.property
    def ipam_driver(self) -> typing.Optional[builtins.str]:
        '''Driver used by the custom IP scheme of the network. Defaults to ``default``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#ipam_driver Network#ipam_driver}
        '''
        result = self._values.get("ipam_driver")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable IPv6 networking. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#ipv6 Network#ipv6}
        '''
        result = self._values.get("ipv6")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def labels(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkLabels"]]]:
        '''labels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#labels Network#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkLabels"]]], result)

    @builtins.property
    def options(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Only available with bridge networks. See `bridge options docs <https://docs.docker.com/engine/reference/commandline/network_create/#bridge-driver-options>`_ for more details.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#options Network#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.network.NetworkIpamConfig",
    jsii_struct_bases=[],
    name_mapping={
        "aux_address": "auxAddress",
        "gateway": "gateway",
        "ip_range": "ipRange",
        "subnet": "subnet",
    },
)
class NetworkIpamConfig:
    def __init__(
        self,
        *,
        aux_address: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        gateway: typing.Optional[builtins.str] = None,
        ip_range: typing.Optional[builtins.str] = None,
        subnet: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aux_address: Auxiliary IPv4 or IPv6 addresses used by Network driver. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#aux_address Network#aux_address}
        :param gateway: The IP address of the gateway. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#gateway Network#gateway}
        :param ip_range: The ip range in CIDR form. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#ip_range Network#ip_range}
        :param subnet: The subnet in CIDR form. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#subnet Network#subnet}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkIpamConfig.__init__)
            check_type(argname="argument aux_address", value=aux_address, expected_type=type_hints["aux_address"])
            check_type(argname="argument gateway", value=gateway, expected_type=type_hints["gateway"])
            check_type(argname="argument ip_range", value=ip_range, expected_type=type_hints["ip_range"])
            check_type(argname="argument subnet", value=subnet, expected_type=type_hints["subnet"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aux_address is not None:
            self._values["aux_address"] = aux_address
        if gateway is not None:
            self._values["gateway"] = gateway
        if ip_range is not None:
            self._values["ip_range"] = ip_range
        if subnet is not None:
            self._values["subnet"] = subnet

    @builtins.property
    def aux_address(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Auxiliary IPv4 or IPv6 addresses used by Network driver.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#aux_address Network#aux_address}
        '''
        result = self._values.get("aux_address")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def gateway(self) -> typing.Optional[builtins.str]:
        '''The IP address of the gateway.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#gateway Network#gateway}
        '''
        result = self._values.get("gateway")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_range(self) -> typing.Optional[builtins.str]:
        '''The ip range in CIDR form.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#ip_range Network#ip_range}
        '''
        result = self._values.get("ip_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet(self) -> typing.Optional[builtins.str]:
        '''The subnet in CIDR form.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#subnet Network#subnet}
        '''
        result = self._values.get("subnet")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkIpamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkIpamConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.network.NetworkIpamConfigList",
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
            type_hints = typing.get_type_hints(NetworkIpamConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "NetworkIpamConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkIpamConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkIpamConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkIpamConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkIpamConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkIpamConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkIpamConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkIpamConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkIpamConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkIpamConfigList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkIpamConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.network.NetworkIpamConfigOutputReference",
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
            type_hints = typing.get_type_hints(NetworkIpamConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAuxAddress")
    def reset_aux_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuxAddress", []))

    @jsii.member(jsii_name="resetGateway")
    def reset_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGateway", []))

    @jsii.member(jsii_name="resetIpRange")
    def reset_ip_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpRange", []))

    @jsii.member(jsii_name="resetSubnet")
    def reset_subnet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnet", []))

    @builtins.property
    @jsii.member(jsii_name="auxAddressInput")
    def aux_address_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "auxAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayInput")
    def gateway_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="ipRangeInput")
    def ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetInput")
    def subnet_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetInput"))

    @builtins.property
    @jsii.member(jsii_name="auxAddress")
    def aux_address(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "auxAddress"))

    @aux_address.setter
    def aux_address(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkIpamConfigOutputReference, "aux_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auxAddress", value)

    @builtins.property
    @jsii.member(jsii_name="gateway")
    def gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gateway"))

    @gateway.setter
    def gateway(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkIpamConfigOutputReference, "gateway").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gateway", value)

    @builtins.property
    @jsii.member(jsii_name="ipRange")
    def ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipRange"))

    @ip_range.setter
    def ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkIpamConfigOutputReference, "ip_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipRange", value)

    @builtins.property
    @jsii.member(jsii_name="subnet")
    def subnet(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnet"))

    @subnet.setter
    def subnet(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkIpamConfigOutputReference, "subnet").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkIpamConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkIpamConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkIpamConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkIpamConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.network.NetworkLabels",
    jsii_struct_bases=[],
    name_mapping={"label": "label", "value": "value"},
)
class NetworkLabels:
    def __init__(self, *, label: builtins.str, value: builtins.str) -> None:
        '''
        :param label: Name of the label. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#label Network#label}
        :param value: Value of the label. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#value Network#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkLabels.__init__)
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "label": label,
            "value": value,
        }

    @builtins.property
    def label(self) -> builtins.str:
        '''Name of the label.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#label Network#label}
        '''
        result = self._values.get("label")
        assert result is not None, "Required property 'label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of the label.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/network#value Network#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkLabelsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.network.NetworkLabelsList",
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
            type_hints = typing.get_type_hints(NetworkLabelsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "NetworkLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkLabelsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkLabelsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkLabelsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkLabelsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkLabelsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkLabelsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.network.NetworkLabelsOutputReference",
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
            type_hints = typing.get_type_hints(NetworkLabelsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkLabelsOutputReference, "label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkLabelsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkLabels, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkLabels, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkLabels, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkLabelsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Network",
    "NetworkConfig",
    "NetworkIpamConfig",
    "NetworkIpamConfigList",
    "NetworkIpamConfigOutputReference",
    "NetworkLabels",
    "NetworkLabelsList",
    "NetworkLabelsOutputReference",
]

publication.publish()
