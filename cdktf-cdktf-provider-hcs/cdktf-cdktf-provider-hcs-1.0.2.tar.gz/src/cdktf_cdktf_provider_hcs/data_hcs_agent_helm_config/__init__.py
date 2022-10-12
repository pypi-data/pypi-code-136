'''
# `data_hcs_agent_helm_config`

Refer to the Terraform Registory for docs: [`data_hcs_agent_helm_config`](https://www.terraform.io/docs/providers/hcs/d/agent_helm_config).
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


class DataHcsAgentHelmConfig(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcs.dataHcsAgentHelmConfig.DataHcsAgentHelmConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config hcs_agent_helm_config}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        aks_cluster_name: builtins.str,
        managed_application_name: builtins.str,
        resource_group_name: builtins.str,
        aks_resource_group: typing.Optional[builtins.str] = None,
        expose_gossip_ports: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataHcsAgentHelmConfigTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config hcs_agent_helm_config} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param aks_cluster_name: The name of the AKS cluster that will consume the Helm config. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#aks_cluster_name DataHcsAgentHelmConfig#aks_cluster_name}
        :param managed_application_name: The name of the HCS Azure Managed Application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#managed_application_name DataHcsAgentHelmConfig#managed_application_name}
        :param resource_group_name: The name of the Resource Group in which the HCS Azure Managed Application belongs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#resource_group_name DataHcsAgentHelmConfig#resource_group_name}
        :param aks_resource_group: The resource group name of the AKS cluster that will consume the Helm config. If not specified, it is defaulted to the value of ``resource_group_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#aks_resource_group DataHcsAgentHelmConfig#aks_resource_group}
        :param expose_gossip_ports: Denotes that the gossip ports should be exposed. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#expose_gossip_ports DataHcsAgentHelmConfig#expose_gossip_ports}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#id DataHcsAgentHelmConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#timeouts DataHcsAgentHelmConfig#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataHcsAgentHelmConfig.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataHcsAgentHelmConfigConfig(
            aks_cluster_name=aks_cluster_name,
            managed_application_name=managed_application_name,
            resource_group_name=resource_group_name,
            aks_resource_group=aks_resource_group,
            expose_gossip_ports=expose_gossip_ports,
            id=id,
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

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#default DataHcsAgentHelmConfig#default}.
        '''
        value = DataHcsAgentHelmConfigTimeouts(default=default)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAksResourceGroup")
    def reset_aks_resource_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAksResourceGroup", []))

    @jsii.member(jsii_name="resetExposeGossipPorts")
    def reset_expose_gossip_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExposeGossipPorts", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="config")
    def config(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DataHcsAgentHelmConfigTimeoutsOutputReference":
        return typing.cast("DataHcsAgentHelmConfigTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="aksClusterNameInput")
    def aks_cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aksClusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="aksResourceGroupInput")
    def aks_resource_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aksResourceGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="exposeGossipPortsInput")
    def expose_gossip_ports_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "exposeGossipPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="managedApplicationNameInput")
    def managed_application_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedApplicationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataHcsAgentHelmConfigTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataHcsAgentHelmConfigTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="aksClusterName")
    def aks_cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aksClusterName"))

    @aks_cluster_name.setter
    def aks_cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcsAgentHelmConfig, "aks_cluster_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aksClusterName", value)

    @builtins.property
    @jsii.member(jsii_name="aksResourceGroup")
    def aks_resource_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aksResourceGroup"))

    @aks_resource_group.setter
    def aks_resource_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcsAgentHelmConfig, "aks_resource_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aksResourceGroup", value)

    @builtins.property
    @jsii.member(jsii_name="exposeGossipPorts")
    def expose_gossip_ports(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "exposeGossipPorts"))

    @expose_gossip_ports.setter
    def expose_gossip_ports(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcsAgentHelmConfig, "expose_gossip_ports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposeGossipPorts", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcsAgentHelmConfig, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="managedApplicationName")
    def managed_application_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedApplicationName"))

    @managed_application_name.setter
    def managed_application_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcsAgentHelmConfig, "managed_application_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedApplicationName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcsAgentHelmConfig, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcs.dataHcsAgentHelmConfig.DataHcsAgentHelmConfigConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "aks_cluster_name": "aksClusterName",
        "managed_application_name": "managedApplicationName",
        "resource_group_name": "resourceGroupName",
        "aks_resource_group": "aksResourceGroup",
        "expose_gossip_ports": "exposeGossipPorts",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class DataHcsAgentHelmConfigConfig(cdktf.TerraformMetaArguments):
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
        aks_cluster_name: builtins.str,
        managed_application_name: builtins.str,
        resource_group_name: builtins.str,
        aks_resource_group: typing.Optional[builtins.str] = None,
        expose_gossip_ports: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataHcsAgentHelmConfigTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param aks_cluster_name: The name of the AKS cluster that will consume the Helm config. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#aks_cluster_name DataHcsAgentHelmConfig#aks_cluster_name}
        :param managed_application_name: The name of the HCS Azure Managed Application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#managed_application_name DataHcsAgentHelmConfig#managed_application_name}
        :param resource_group_name: The name of the Resource Group in which the HCS Azure Managed Application belongs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#resource_group_name DataHcsAgentHelmConfig#resource_group_name}
        :param aks_resource_group: The resource group name of the AKS cluster that will consume the Helm config. If not specified, it is defaulted to the value of ``resource_group_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#aks_resource_group DataHcsAgentHelmConfig#aks_resource_group}
        :param expose_gossip_ports: Denotes that the gossip ports should be exposed. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#expose_gossip_ports DataHcsAgentHelmConfig#expose_gossip_ports}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#id DataHcsAgentHelmConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#timeouts DataHcsAgentHelmConfig#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DataHcsAgentHelmConfigTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DataHcsAgentHelmConfigConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument aks_cluster_name", value=aks_cluster_name, expected_type=type_hints["aks_cluster_name"])
            check_type(argname="argument managed_application_name", value=managed_application_name, expected_type=type_hints["managed_application_name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument aks_resource_group", value=aks_resource_group, expected_type=type_hints["aks_resource_group"])
            check_type(argname="argument expose_gossip_ports", value=expose_gossip_ports, expected_type=type_hints["expose_gossip_ports"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "aks_cluster_name": aks_cluster_name,
            "managed_application_name": managed_application_name,
            "resource_group_name": resource_group_name,
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
        if aks_resource_group is not None:
            self._values["aks_resource_group"] = aks_resource_group
        if expose_gossip_ports is not None:
            self._values["expose_gossip_ports"] = expose_gossip_ports
        if id is not None:
            self._values["id"] = id
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
    def aks_cluster_name(self) -> builtins.str:
        '''The name of the AKS cluster that will consume the Helm config.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#aks_cluster_name DataHcsAgentHelmConfig#aks_cluster_name}
        '''
        result = self._values.get("aks_cluster_name")
        assert result is not None, "Required property 'aks_cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def managed_application_name(self) -> builtins.str:
        '''The name of the HCS Azure Managed Application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#managed_application_name DataHcsAgentHelmConfig#managed_application_name}
        '''
        result = self._values.get("managed_application_name")
        assert result is not None, "Required property 'managed_application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''The name of the Resource Group in which the HCS Azure Managed Application belongs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#resource_group_name DataHcsAgentHelmConfig#resource_group_name}
        '''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aks_resource_group(self) -> typing.Optional[builtins.str]:
        '''The resource group name of the AKS cluster that will consume the Helm config.

        If not specified, it is defaulted to the value of ``resource_group_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#aks_resource_group DataHcsAgentHelmConfig#aks_resource_group}
        '''
        result = self._values.get("aks_resource_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expose_gossip_ports(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Denotes that the gossip ports should be exposed. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#expose_gossip_ports DataHcsAgentHelmConfig#expose_gossip_ports}
        '''
        result = self._values.get("expose_gossip_ports")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#id DataHcsAgentHelmConfig#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataHcsAgentHelmConfigTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#timeouts DataHcsAgentHelmConfig#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataHcsAgentHelmConfigTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataHcsAgentHelmConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-hcs.dataHcsAgentHelmConfig.DataHcsAgentHelmConfigTimeouts",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class DataHcsAgentHelmConfigTimeouts:
    def __init__(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#default DataHcsAgentHelmConfig#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataHcsAgentHelmConfigTimeouts.__init__)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/d/agent_helm_config#default DataHcsAgentHelmConfig#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataHcsAgentHelmConfigTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataHcsAgentHelmConfigTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcs.dataHcsAgentHelmConfig.DataHcsAgentHelmConfigTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataHcsAgentHelmConfigTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcsAgentHelmConfigTimeoutsOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataHcsAgentHelmConfigTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataHcsAgentHelmConfigTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataHcsAgentHelmConfigTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcsAgentHelmConfigTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataHcsAgentHelmConfig",
    "DataHcsAgentHelmConfigConfig",
    "DataHcsAgentHelmConfigTimeouts",
    "DataHcsAgentHelmConfigTimeoutsOutputReference",
]

publication.publish()
