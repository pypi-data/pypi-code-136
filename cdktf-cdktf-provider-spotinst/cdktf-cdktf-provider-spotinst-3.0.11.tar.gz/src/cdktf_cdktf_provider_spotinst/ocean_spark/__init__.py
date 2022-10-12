'''
# `spotinst_ocean_spark`

Refer to the Terraform Registory for docs: [`spotinst_ocean_spark`](https://www.terraform.io/docs/providers/spotinst/r/ocean_spark).
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


class OceanSpark(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanSpark.OceanSpark",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark spotinst_ocean_spark}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        ocean_cluster_id: builtins.str,
        compute: typing.Optional[typing.Union["OceanSparkCompute", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        ingress: typing.Optional[typing.Union["OceanSparkIngress", typing.Dict[str, typing.Any]]] = None,
        log_collection: typing.Optional[typing.Union["OceanSparkLogCollection", typing.Dict[str, typing.Any]]] = None,
        webhook: typing.Optional[typing.Union["OceanSparkWebhook", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark spotinst_ocean_spark} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param ocean_cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#ocean_cluster_id OceanSpark#ocean_cluster_id}.
        :param compute: compute block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#compute OceanSpark#compute}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#id OceanSpark#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ingress: ingress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#ingress OceanSpark#ingress}
        :param log_collection: log_collection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#log_collection OceanSpark#log_collection}
        :param webhook: webhook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#webhook OceanSpark#webhook}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanSpark.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OceanSparkConfig(
            ocean_cluster_id=ocean_cluster_id,
            compute=compute,
            id=id,
            ingress=ingress,
            log_collection=log_collection,
            webhook=webhook,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCompute")
    def put_compute(
        self,
        *,
        create_vngs: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use_taints: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param create_vngs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#create_vngs OceanSpark#create_vngs}.
        :param use_taints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#use_taints OceanSpark#use_taints}.
        '''
        value = OceanSparkCompute(create_vngs=create_vngs, use_taints=use_taints)

        return typing.cast(None, jsii.invoke(self, "putCompute", [value]))

    @jsii.member(jsii_name="putIngress")
    def put_ingress(
        self,
        *,
        service_annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param service_annotations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#service_annotations OceanSpark#service_annotations}.
        '''
        value = OceanSparkIngress(service_annotations=service_annotations)

        return typing.cast(None, jsii.invoke(self, "putIngress", [value]))

    @jsii.member(jsii_name="putLogCollection")
    def put_log_collection(
        self,
        *,
        collect_driver_logs: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param collect_driver_logs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#collect_driver_logs OceanSpark#collect_driver_logs}.
        '''
        value = OceanSparkLogCollection(collect_driver_logs=collect_driver_logs)

        return typing.cast(None, jsii.invoke(self, "putLogCollection", [value]))

    @jsii.member(jsii_name="putWebhook")
    def put_webhook(
        self,
        *,
        host_network_ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
        use_host_network: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param host_network_ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#host_network_ports OceanSpark#host_network_ports}.
        :param use_host_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#use_host_network OceanSpark#use_host_network}.
        '''
        value = OceanSparkWebhook(
            host_network_ports=host_network_ports, use_host_network=use_host_network
        )

        return typing.cast(None, jsii.invoke(self, "putWebhook", [value]))

    @jsii.member(jsii_name="resetCompute")
    def reset_compute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompute", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIngress")
    def reset_ingress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngress", []))

    @jsii.member(jsii_name="resetLogCollection")
    def reset_log_collection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogCollection", []))

    @jsii.member(jsii_name="resetWebhook")
    def reset_webhook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebhook", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="compute")
    def compute(self) -> "OceanSparkComputeOutputReference":
        return typing.cast("OceanSparkComputeOutputReference", jsii.get(self, "compute"))

    @builtins.property
    @jsii.member(jsii_name="ingress")
    def ingress(self) -> "OceanSparkIngressOutputReference":
        return typing.cast("OceanSparkIngressOutputReference", jsii.get(self, "ingress"))

    @builtins.property
    @jsii.member(jsii_name="logCollection")
    def log_collection(self) -> "OceanSparkLogCollectionOutputReference":
        return typing.cast("OceanSparkLogCollectionOutputReference", jsii.get(self, "logCollection"))

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> "OceanSparkWebhookOutputReference":
        return typing.cast("OceanSparkWebhookOutputReference", jsii.get(self, "webhook"))

    @builtins.property
    @jsii.member(jsii_name="computeInput")
    def compute_input(self) -> typing.Optional["OceanSparkCompute"]:
        return typing.cast(typing.Optional["OceanSparkCompute"], jsii.get(self, "computeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressInput")
    def ingress_input(self) -> typing.Optional["OceanSparkIngress"]:
        return typing.cast(typing.Optional["OceanSparkIngress"], jsii.get(self, "ingressInput"))

    @builtins.property
    @jsii.member(jsii_name="logCollectionInput")
    def log_collection_input(self) -> typing.Optional["OceanSparkLogCollection"]:
        return typing.cast(typing.Optional["OceanSparkLogCollection"], jsii.get(self, "logCollectionInput"))

    @builtins.property
    @jsii.member(jsii_name="oceanClusterIdInput")
    def ocean_cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oceanClusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookInput")
    def webhook_input(self) -> typing.Optional["OceanSparkWebhook"]:
        return typing.cast(typing.Optional["OceanSparkWebhook"], jsii.get(self, "webhookInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanSpark, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="oceanClusterId")
    def ocean_cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oceanClusterId"))

    @ocean_cluster_id.setter
    def ocean_cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanSpark, "ocean_cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oceanClusterId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanSpark.OceanSparkCompute",
    jsii_struct_bases=[],
    name_mapping={"create_vngs": "createVngs", "use_taints": "useTaints"},
)
class OceanSparkCompute:
    def __init__(
        self,
        *,
        create_vngs: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use_taints: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param create_vngs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#create_vngs OceanSpark#create_vngs}.
        :param use_taints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#use_taints OceanSpark#use_taints}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanSparkCompute.__init__)
            check_type(argname="argument create_vngs", value=create_vngs, expected_type=type_hints["create_vngs"])
            check_type(argname="argument use_taints", value=use_taints, expected_type=type_hints["use_taints"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create_vngs is not None:
            self._values["create_vngs"] = create_vngs
        if use_taints is not None:
            self._values["use_taints"] = use_taints

    @builtins.property
    def create_vngs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#create_vngs OceanSpark#create_vngs}.'''
        result = self._values.get("create_vngs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def use_taints(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#use_taints OceanSpark#use_taints}.'''
        result = self._values.get("use_taints")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanSparkCompute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanSparkComputeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanSpark.OceanSparkComputeOutputReference",
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
            type_hints = typing.get_type_hints(OceanSparkComputeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreateVngs")
    def reset_create_vngs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateVngs", []))

    @jsii.member(jsii_name="resetUseTaints")
    def reset_use_taints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseTaints", []))

    @builtins.property
    @jsii.member(jsii_name="createVngsInput")
    def create_vngs_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "createVngsInput"))

    @builtins.property
    @jsii.member(jsii_name="useTaintsInput")
    def use_taints_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useTaintsInput"))

    @builtins.property
    @jsii.member(jsii_name="createVngs")
    def create_vngs(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "createVngs"))

    @create_vngs.setter
    def create_vngs(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanSparkComputeOutputReference, "create_vngs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createVngs", value)

    @builtins.property
    @jsii.member(jsii_name="useTaints")
    def use_taints(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useTaints"))

    @use_taints.setter
    def use_taints(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanSparkComputeOutputReference, "use_taints").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useTaints", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanSparkCompute]:
        return typing.cast(typing.Optional[OceanSparkCompute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanSparkCompute]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanSparkComputeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanSpark.OceanSparkConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "ocean_cluster_id": "oceanClusterId",
        "compute": "compute",
        "id": "id",
        "ingress": "ingress",
        "log_collection": "logCollection",
        "webhook": "webhook",
    },
)
class OceanSparkConfig(cdktf.TerraformMetaArguments):
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
        ocean_cluster_id: builtins.str,
        compute: typing.Optional[typing.Union[OceanSparkCompute, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        ingress: typing.Optional[typing.Union["OceanSparkIngress", typing.Dict[str, typing.Any]]] = None,
        log_collection: typing.Optional[typing.Union["OceanSparkLogCollection", typing.Dict[str, typing.Any]]] = None,
        webhook: typing.Optional[typing.Union["OceanSparkWebhook", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param ocean_cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#ocean_cluster_id OceanSpark#ocean_cluster_id}.
        :param compute: compute block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#compute OceanSpark#compute}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#id OceanSpark#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ingress: ingress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#ingress OceanSpark#ingress}
        :param log_collection: log_collection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#log_collection OceanSpark#log_collection}
        :param webhook: webhook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#webhook OceanSpark#webhook}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(compute, dict):
            compute = OceanSparkCompute(**compute)
        if isinstance(ingress, dict):
            ingress = OceanSparkIngress(**ingress)
        if isinstance(log_collection, dict):
            log_collection = OceanSparkLogCollection(**log_collection)
        if isinstance(webhook, dict):
            webhook = OceanSparkWebhook(**webhook)
        if __debug__:
            type_hints = typing.get_type_hints(OceanSparkConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument ocean_cluster_id", value=ocean_cluster_id, expected_type=type_hints["ocean_cluster_id"])
            check_type(argname="argument compute", value=compute, expected_type=type_hints["compute"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ingress", value=ingress, expected_type=type_hints["ingress"])
            check_type(argname="argument log_collection", value=log_collection, expected_type=type_hints["log_collection"])
            check_type(argname="argument webhook", value=webhook, expected_type=type_hints["webhook"])
        self._values: typing.Dict[str, typing.Any] = {
            "ocean_cluster_id": ocean_cluster_id,
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
        if compute is not None:
            self._values["compute"] = compute
        if id is not None:
            self._values["id"] = id
        if ingress is not None:
            self._values["ingress"] = ingress
        if log_collection is not None:
            self._values["log_collection"] = log_collection
        if webhook is not None:
            self._values["webhook"] = webhook

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
    def ocean_cluster_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#ocean_cluster_id OceanSpark#ocean_cluster_id}.'''
        result = self._values.get("ocean_cluster_id")
        assert result is not None, "Required property 'ocean_cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compute(self) -> typing.Optional[OceanSparkCompute]:
        '''compute block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#compute OceanSpark#compute}
        '''
        result = self._values.get("compute")
        return typing.cast(typing.Optional[OceanSparkCompute], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#id OceanSpark#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingress(self) -> typing.Optional["OceanSparkIngress"]:
        '''ingress block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#ingress OceanSpark#ingress}
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional["OceanSparkIngress"], result)

    @builtins.property
    def log_collection(self) -> typing.Optional["OceanSparkLogCollection"]:
        '''log_collection block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#log_collection OceanSpark#log_collection}
        '''
        result = self._values.get("log_collection")
        return typing.cast(typing.Optional["OceanSparkLogCollection"], result)

    @builtins.property
    def webhook(self) -> typing.Optional["OceanSparkWebhook"]:
        '''webhook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#webhook OceanSpark#webhook}
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional["OceanSparkWebhook"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanSparkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanSpark.OceanSparkIngress",
    jsii_struct_bases=[],
    name_mapping={"service_annotations": "serviceAnnotations"},
)
class OceanSparkIngress:
    def __init__(
        self,
        *,
        service_annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param service_annotations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#service_annotations OceanSpark#service_annotations}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanSparkIngress.__init__)
            check_type(argname="argument service_annotations", value=service_annotations, expected_type=type_hints["service_annotations"])
        self._values: typing.Dict[str, typing.Any] = {}
        if service_annotations is not None:
            self._values["service_annotations"] = service_annotations

    @builtins.property
    def service_annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#service_annotations OceanSpark#service_annotations}.'''
        result = self._values.get("service_annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanSparkIngress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanSparkIngressOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanSpark.OceanSparkIngressOutputReference",
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
            type_hints = typing.get_type_hints(OceanSparkIngressOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetServiceAnnotations")
    def reset_service_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAnnotations", []))

    @builtins.property
    @jsii.member(jsii_name="serviceAnnotationsInput")
    def service_annotations_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "serviceAnnotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAnnotations")
    def service_annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "serviceAnnotations"))

    @service_annotations.setter
    def service_annotations(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanSparkIngressOutputReference, "service_annotations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAnnotations", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanSparkIngress]:
        return typing.cast(typing.Optional[OceanSparkIngress], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanSparkIngress]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanSparkIngressOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanSpark.OceanSparkLogCollection",
    jsii_struct_bases=[],
    name_mapping={"collect_driver_logs": "collectDriverLogs"},
)
class OceanSparkLogCollection:
    def __init__(
        self,
        *,
        collect_driver_logs: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param collect_driver_logs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#collect_driver_logs OceanSpark#collect_driver_logs}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanSparkLogCollection.__init__)
            check_type(argname="argument collect_driver_logs", value=collect_driver_logs, expected_type=type_hints["collect_driver_logs"])
        self._values: typing.Dict[str, typing.Any] = {}
        if collect_driver_logs is not None:
            self._values["collect_driver_logs"] = collect_driver_logs

    @builtins.property
    def collect_driver_logs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#collect_driver_logs OceanSpark#collect_driver_logs}.'''
        result = self._values.get("collect_driver_logs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanSparkLogCollection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanSparkLogCollectionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanSpark.OceanSparkLogCollectionOutputReference",
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
            type_hints = typing.get_type_hints(OceanSparkLogCollectionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCollectDriverLogs")
    def reset_collect_driver_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCollectDriverLogs", []))

    @builtins.property
    @jsii.member(jsii_name="collectDriverLogsInput")
    def collect_driver_logs_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "collectDriverLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="collectDriverLogs")
    def collect_driver_logs(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "collectDriverLogs"))

    @collect_driver_logs.setter
    def collect_driver_logs(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanSparkLogCollectionOutputReference, "collect_driver_logs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collectDriverLogs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanSparkLogCollection]:
        return typing.cast(typing.Optional[OceanSparkLogCollection], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanSparkLogCollection]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanSparkLogCollectionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanSpark.OceanSparkWebhook",
    jsii_struct_bases=[],
    name_mapping={
        "host_network_ports": "hostNetworkPorts",
        "use_host_network": "useHostNetwork",
    },
)
class OceanSparkWebhook:
    def __init__(
        self,
        *,
        host_network_ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
        use_host_network: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param host_network_ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#host_network_ports OceanSpark#host_network_ports}.
        :param use_host_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#use_host_network OceanSpark#use_host_network}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanSparkWebhook.__init__)
            check_type(argname="argument host_network_ports", value=host_network_ports, expected_type=type_hints["host_network_ports"])
            check_type(argname="argument use_host_network", value=use_host_network, expected_type=type_hints["use_host_network"])
        self._values: typing.Dict[str, typing.Any] = {}
        if host_network_ports is not None:
            self._values["host_network_ports"] = host_network_ports
        if use_host_network is not None:
            self._values["use_host_network"] = use_host_network

    @builtins.property
    def host_network_ports(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#host_network_ports OceanSpark#host_network_ports}.'''
        result = self._values.get("host_network_ports")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def use_host_network(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#use_host_network OceanSpark#use_host_network}.'''
        result = self._values.get("use_host_network")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanSparkWebhook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanSparkWebhookOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanSpark.OceanSparkWebhookOutputReference",
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
            type_hints = typing.get_type_hints(OceanSparkWebhookOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostNetworkPorts")
    def reset_host_network_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostNetworkPorts", []))

    @jsii.member(jsii_name="resetUseHostNetwork")
    def reset_use_host_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseHostNetwork", []))

    @builtins.property
    @jsii.member(jsii_name="hostNetworkPortsInput")
    def host_network_ports_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "hostNetworkPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="useHostNetworkInput")
    def use_host_network_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useHostNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNetworkPorts")
    def host_network_ports(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "hostNetworkPorts"))

    @host_network_ports.setter
    def host_network_ports(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanSparkWebhookOutputReference, "host_network_ports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostNetworkPorts", value)

    @builtins.property
    @jsii.member(jsii_name="useHostNetwork")
    def use_host_network(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useHostNetwork"))

    @use_host_network.setter
    def use_host_network(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanSparkWebhookOutputReference, "use_host_network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useHostNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanSparkWebhook]:
        return typing.cast(typing.Optional[OceanSparkWebhook], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanSparkWebhook]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanSparkWebhookOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OceanSpark",
    "OceanSparkCompute",
    "OceanSparkComputeOutputReference",
    "OceanSparkConfig",
    "OceanSparkIngress",
    "OceanSparkIngressOutputReference",
    "OceanSparkLogCollection",
    "OceanSparkLogCollectionOutputReference",
    "OceanSparkWebhook",
    "OceanSparkWebhookOutputReference",
]

publication.publish()
