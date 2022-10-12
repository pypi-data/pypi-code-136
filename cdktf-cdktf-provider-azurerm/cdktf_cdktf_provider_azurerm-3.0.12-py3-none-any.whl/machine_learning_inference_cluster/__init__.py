'''
# `azurerm_machine_learning_inference_cluster`

Refer to the Terraform Registory for docs: [`azurerm_machine_learning_inference_cluster`](https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster).
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


class MachineLearningInferenceCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.machineLearningInferenceCluster.MachineLearningInferenceCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster azurerm_machine_learning_inference_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        kubernetes_cluster_id: builtins.str,
        location: builtins.str,
        machine_learning_workspace_id: builtins.str,
        name: builtins.str,
        cluster_purpose: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["MachineLearningInferenceClusterIdentity", typing.Dict[str, typing.Any]]] = None,
        ssl: typing.Optional[typing.Union["MachineLearningInferenceClusterSsl", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MachineLearningInferenceClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster azurerm_machine_learning_inference_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param kubernetes_cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#kubernetes_cluster_id MachineLearningInferenceCluster#kubernetes_cluster_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#location MachineLearningInferenceCluster#location}.
        :param machine_learning_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#machine_learning_workspace_id MachineLearningInferenceCluster#machine_learning_workspace_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#name MachineLearningInferenceCluster#name}.
        :param cluster_purpose: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#cluster_purpose MachineLearningInferenceCluster#cluster_purpose}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#description MachineLearningInferenceCluster#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#id MachineLearningInferenceCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#identity MachineLearningInferenceCluster#identity}
        :param ssl: ssl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#ssl MachineLearningInferenceCluster#ssl}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#tags MachineLearningInferenceCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#timeouts MachineLearningInferenceCluster#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MachineLearningInferenceCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MachineLearningInferenceClusterConfig(
            kubernetes_cluster_id=kubernetes_cluster_id,
            location=location,
            machine_learning_workspace_id=machine_learning_workspace_id,
            name=name,
            cluster_purpose=cluster_purpose,
            description=description,
            id=id,
            identity=identity,
            ssl=ssl,
            tags=tags,
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

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#type MachineLearningInferenceCluster#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#identity_ids MachineLearningInferenceCluster#identity_ids}.
        '''
        value = MachineLearningInferenceClusterIdentity(
            type=type, identity_ids=identity_ids
        )

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putSsl")
    def put_ssl(
        self,
        *,
        cert: typing.Optional[builtins.str] = None,
        cname: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        leaf_domain_label: typing.Optional[builtins.str] = None,
        overwrite_existing_domain: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cert: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#cert MachineLearningInferenceCluster#cert}.
        :param cname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#cname MachineLearningInferenceCluster#cname}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#key MachineLearningInferenceCluster#key}.
        :param leaf_domain_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#leaf_domain_label MachineLearningInferenceCluster#leaf_domain_label}.
        :param overwrite_existing_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#overwrite_existing_domain MachineLearningInferenceCluster#overwrite_existing_domain}.
        '''
        value = MachineLearningInferenceClusterSsl(
            cert=cert,
            cname=cname,
            key=key,
            leaf_domain_label=leaf_domain_label,
            overwrite_existing_domain=overwrite_existing_domain,
        )

        return typing.cast(None, jsii.invoke(self, "putSsl", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#create MachineLearningInferenceCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#delete MachineLearningInferenceCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#read MachineLearningInferenceCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#update MachineLearningInferenceCluster#update}.
        '''
        value = MachineLearningInferenceClusterTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetClusterPurpose")
    def reset_cluster_purpose(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterPurpose", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetSsl")
    def reset_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsl", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="identity")
    def identity(self) -> "MachineLearningInferenceClusterIdentityOutputReference":
        return typing.cast("MachineLearningInferenceClusterIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="ssl")
    def ssl(self) -> "MachineLearningInferenceClusterSslOutputReference":
        return typing.cast("MachineLearningInferenceClusterSslOutputReference", jsii.get(self, "ssl"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MachineLearningInferenceClusterTimeoutsOutputReference":
        return typing.cast("MachineLearningInferenceClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="clusterPurposeInput")
    def cluster_purpose_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterPurposeInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(
        self,
    ) -> typing.Optional["MachineLearningInferenceClusterIdentity"]:
        return typing.cast(typing.Optional["MachineLearningInferenceClusterIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesClusterIdInput")
    def kubernetes_cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kubernetesClusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="machineLearningWorkspaceIdInput")
    def machine_learning_workspace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineLearningWorkspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sslInput")
    def ssl_input(self) -> typing.Optional["MachineLearningInferenceClusterSsl"]:
        return typing.cast(typing.Optional["MachineLearningInferenceClusterSsl"], jsii.get(self, "sslInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MachineLearningInferenceClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MachineLearningInferenceClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterPurpose")
    def cluster_purpose(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterPurpose"))

    @cluster_purpose.setter
    def cluster_purpose(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceCluster, "cluster_purpose").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterPurpose", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceCluster, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kubernetesClusterId")
    def kubernetes_cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kubernetesClusterId"))

    @kubernetes_cluster_id.setter
    def kubernetes_cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceCluster, "kubernetes_cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kubernetesClusterId", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceCluster, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="machineLearningWorkspaceId")
    def machine_learning_workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineLearningWorkspaceId"))

    @machine_learning_workspace_id.setter
    def machine_learning_workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceCluster, "machine_learning_workspace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineLearningWorkspaceId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceCluster, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceCluster, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.machineLearningInferenceCluster.MachineLearningInferenceClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "kubernetes_cluster_id": "kubernetesClusterId",
        "location": "location",
        "machine_learning_workspace_id": "machineLearningWorkspaceId",
        "name": "name",
        "cluster_purpose": "clusterPurpose",
        "description": "description",
        "id": "id",
        "identity": "identity",
        "ssl": "ssl",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class MachineLearningInferenceClusterConfig(cdktf.TerraformMetaArguments):
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
        kubernetes_cluster_id: builtins.str,
        location: builtins.str,
        machine_learning_workspace_id: builtins.str,
        name: builtins.str,
        cluster_purpose: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["MachineLearningInferenceClusterIdentity", typing.Dict[str, typing.Any]]] = None,
        ssl: typing.Optional[typing.Union["MachineLearningInferenceClusterSsl", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MachineLearningInferenceClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param kubernetes_cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#kubernetes_cluster_id MachineLearningInferenceCluster#kubernetes_cluster_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#location MachineLearningInferenceCluster#location}.
        :param machine_learning_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#machine_learning_workspace_id MachineLearningInferenceCluster#machine_learning_workspace_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#name MachineLearningInferenceCluster#name}.
        :param cluster_purpose: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#cluster_purpose MachineLearningInferenceCluster#cluster_purpose}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#description MachineLearningInferenceCluster#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#id MachineLearningInferenceCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#identity MachineLearningInferenceCluster#identity}
        :param ssl: ssl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#ssl MachineLearningInferenceCluster#ssl}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#tags MachineLearningInferenceCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#timeouts MachineLearningInferenceCluster#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(identity, dict):
            identity = MachineLearningInferenceClusterIdentity(**identity)
        if isinstance(ssl, dict):
            ssl = MachineLearningInferenceClusterSsl(**ssl)
        if isinstance(timeouts, dict):
            timeouts = MachineLearningInferenceClusterTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MachineLearningInferenceClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument kubernetes_cluster_id", value=kubernetes_cluster_id, expected_type=type_hints["kubernetes_cluster_id"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument machine_learning_workspace_id", value=machine_learning_workspace_id, expected_type=type_hints["machine_learning_workspace_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument cluster_purpose", value=cluster_purpose, expected_type=type_hints["cluster_purpose"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument ssl", value=ssl, expected_type=type_hints["ssl"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "kubernetes_cluster_id": kubernetes_cluster_id,
            "location": location,
            "machine_learning_workspace_id": machine_learning_workspace_id,
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
        if cluster_purpose is not None:
            self._values["cluster_purpose"] = cluster_purpose
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if ssl is not None:
            self._values["ssl"] = ssl
        if tags is not None:
            self._values["tags"] = tags
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
    def kubernetes_cluster_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#kubernetes_cluster_id MachineLearningInferenceCluster#kubernetes_cluster_id}.'''
        result = self._values.get("kubernetes_cluster_id")
        assert result is not None, "Required property 'kubernetes_cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#location MachineLearningInferenceCluster#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def machine_learning_workspace_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#machine_learning_workspace_id MachineLearningInferenceCluster#machine_learning_workspace_id}.'''
        result = self._values.get("machine_learning_workspace_id")
        assert result is not None, "Required property 'machine_learning_workspace_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#name MachineLearningInferenceCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_purpose(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#cluster_purpose MachineLearningInferenceCluster#cluster_purpose}.'''
        result = self._values.get("cluster_purpose")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#description MachineLearningInferenceCluster#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#id MachineLearningInferenceCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["MachineLearningInferenceClusterIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#identity MachineLearningInferenceCluster#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["MachineLearningInferenceClusterIdentity"], result)

    @builtins.property
    def ssl(self) -> typing.Optional["MachineLearningInferenceClusterSsl"]:
        '''ssl block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#ssl MachineLearningInferenceCluster#ssl}
        '''
        result = self._values.get("ssl")
        return typing.cast(typing.Optional["MachineLearningInferenceClusterSsl"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#tags MachineLearningInferenceCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MachineLearningInferenceClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#timeouts MachineLearningInferenceCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MachineLearningInferenceClusterTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningInferenceClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.machineLearningInferenceCluster.MachineLearningInferenceClusterIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class MachineLearningInferenceClusterIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#type MachineLearningInferenceCluster#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#identity_ids MachineLearningInferenceCluster#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MachineLearningInferenceClusterIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#type MachineLearningInferenceCluster#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#identity_ids MachineLearningInferenceCluster#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningInferenceClusterIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MachineLearningInferenceClusterIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.machineLearningInferenceCluster.MachineLearningInferenceClusterIdentityOutputReference",
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
            type_hints = typing.get_type_hints(MachineLearningInferenceClusterIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdentityIds")
    def reset_identity_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityIds", []))

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="identityIdsInput")
    def identity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIds")
    def identity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityIds"))

    @identity_ids.setter
    def identity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceClusterIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceClusterIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MachineLearningInferenceClusterIdentity]:
        return typing.cast(typing.Optional[MachineLearningInferenceClusterIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MachineLearningInferenceClusterIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceClusterIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.machineLearningInferenceCluster.MachineLearningInferenceClusterSsl",
    jsii_struct_bases=[],
    name_mapping={
        "cert": "cert",
        "cname": "cname",
        "key": "key",
        "leaf_domain_label": "leafDomainLabel",
        "overwrite_existing_domain": "overwriteExistingDomain",
    },
)
class MachineLearningInferenceClusterSsl:
    def __init__(
        self,
        *,
        cert: typing.Optional[builtins.str] = None,
        cname: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        leaf_domain_label: typing.Optional[builtins.str] = None,
        overwrite_existing_domain: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cert: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#cert MachineLearningInferenceCluster#cert}.
        :param cname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#cname MachineLearningInferenceCluster#cname}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#key MachineLearningInferenceCluster#key}.
        :param leaf_domain_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#leaf_domain_label MachineLearningInferenceCluster#leaf_domain_label}.
        :param overwrite_existing_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#overwrite_existing_domain MachineLearningInferenceCluster#overwrite_existing_domain}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MachineLearningInferenceClusterSsl.__init__)
            check_type(argname="argument cert", value=cert, expected_type=type_hints["cert"])
            check_type(argname="argument cname", value=cname, expected_type=type_hints["cname"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument leaf_domain_label", value=leaf_domain_label, expected_type=type_hints["leaf_domain_label"])
            check_type(argname="argument overwrite_existing_domain", value=overwrite_existing_domain, expected_type=type_hints["overwrite_existing_domain"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cert is not None:
            self._values["cert"] = cert
        if cname is not None:
            self._values["cname"] = cname
        if key is not None:
            self._values["key"] = key
        if leaf_domain_label is not None:
            self._values["leaf_domain_label"] = leaf_domain_label
        if overwrite_existing_domain is not None:
            self._values["overwrite_existing_domain"] = overwrite_existing_domain

    @builtins.property
    def cert(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#cert MachineLearningInferenceCluster#cert}.'''
        result = self._values.get("cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#cname MachineLearningInferenceCluster#cname}.'''
        result = self._values.get("cname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#key MachineLearningInferenceCluster#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def leaf_domain_label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#leaf_domain_label MachineLearningInferenceCluster#leaf_domain_label}.'''
        result = self._values.get("leaf_domain_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overwrite_existing_domain(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#overwrite_existing_domain MachineLearningInferenceCluster#overwrite_existing_domain}.'''
        result = self._values.get("overwrite_existing_domain")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningInferenceClusterSsl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MachineLearningInferenceClusterSslOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.machineLearningInferenceCluster.MachineLearningInferenceClusterSslOutputReference",
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
            type_hints = typing.get_type_hints(MachineLearningInferenceClusterSslOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCert")
    def reset_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCert", []))

    @jsii.member(jsii_name="resetCname")
    def reset_cname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCname", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetLeafDomainLabel")
    def reset_leaf_domain_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLeafDomainLabel", []))

    @jsii.member(jsii_name="resetOverwriteExistingDomain")
    def reset_overwrite_existing_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverwriteExistingDomain", []))

    @builtins.property
    @jsii.member(jsii_name="certInput")
    def cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certInput"))

    @builtins.property
    @jsii.member(jsii_name="cnameInput")
    def cname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cnameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="leafDomainLabelInput")
    def leaf_domain_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "leafDomainLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="overwriteExistingDomainInput")
    def overwrite_existing_domain_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overwriteExistingDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="cert")
    def cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cert"))

    @cert.setter
    def cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceClusterSslOutputReference, "cert").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cert", value)

    @builtins.property
    @jsii.member(jsii_name="cname")
    def cname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cname"))

    @cname.setter
    def cname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceClusterSslOutputReference, "cname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cname", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceClusterSslOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="leafDomainLabel")
    def leaf_domain_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "leafDomainLabel"))

    @leaf_domain_label.setter
    def leaf_domain_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceClusterSslOutputReference, "leaf_domain_label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "leafDomainLabel", value)

    @builtins.property
    @jsii.member(jsii_name="overwriteExistingDomain")
    def overwrite_existing_domain(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "overwriteExistingDomain"))

    @overwrite_existing_domain.setter
    def overwrite_existing_domain(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceClusterSslOutputReference, "overwrite_existing_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overwriteExistingDomain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MachineLearningInferenceClusterSsl]:
        return typing.cast(typing.Optional[MachineLearningInferenceClusterSsl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MachineLearningInferenceClusterSsl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceClusterSslOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.machineLearningInferenceCluster.MachineLearningInferenceClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MachineLearningInferenceClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#create MachineLearningInferenceCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#delete MachineLearningInferenceCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#read MachineLearningInferenceCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#update MachineLearningInferenceCluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MachineLearningInferenceClusterTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#create MachineLearningInferenceCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#delete MachineLearningInferenceCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#read MachineLearningInferenceCluster#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_inference_cluster#update MachineLearningInferenceCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningInferenceClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MachineLearningInferenceClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.machineLearningInferenceCluster.MachineLearningInferenceClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MachineLearningInferenceClusterTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceClusterTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceClusterTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceClusterTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceClusterTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MachineLearningInferenceClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MachineLearningInferenceClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MachineLearningInferenceClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningInferenceClusterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MachineLearningInferenceCluster",
    "MachineLearningInferenceClusterConfig",
    "MachineLearningInferenceClusterIdentity",
    "MachineLearningInferenceClusterIdentityOutputReference",
    "MachineLearningInferenceClusterSsl",
    "MachineLearningInferenceClusterSslOutputReference",
    "MachineLearningInferenceClusterTimeouts",
    "MachineLearningInferenceClusterTimeoutsOutputReference",
]

publication.publish()
