'''
# `nomad_volume`

Refer to the Terraform Registory for docs: [`nomad_volume`](https://www.terraform.io/docs/providers/nomad/r/volume).
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


class Volume(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.Volume",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/nomad/r/volume nomad_volume}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        external_id: builtins.str,
        name: builtins.str,
        plugin_id: builtins.str,
        volume_id: builtins.str,
        access_mode: typing.Optional[builtins.str] = None,
        attachment_mode: typing.Optional[builtins.str] = None,
        capability: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VolumeCapability", typing.Dict[str, typing.Any]]]]] = None,
        context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        deregister_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[typing.Union["VolumeMountOptions", typing.Dict[str, typing.Any]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        topology_request: typing.Optional[typing.Union["VolumeTopologyRequest", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/nomad/r/volume nomad_volume} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param external_id: The ID of the physical volume from the storage provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#external_id Volume#external_id}
        :param name: The display name of the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#name Volume#name}
        :param plugin_id: The ID of the CSI plugin that manages this volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#plugin_id Volume#plugin_id}
        :param volume_id: The unique ID of the volume, how jobs will refer to the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#volume_id Volume#volume_id}
        :param access_mode: Defines whether a volume should be available concurrently. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#access_mode Volume#access_mode}
        :param attachment_mode: The storage API that will be used by the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#attachment_mode Volume#attachment_mode}
        :param capability: capability block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#capability Volume#capability}
        :param context: An optional key-value map of strings passed directly to the CSI plugin to validate the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#context Volume#context}
        :param deregister_on_destroy: If true, the volume will be deregistered on destroy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#deregister_on_destroy Volume#deregister_on_destroy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#id Volume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mount_options: mount_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#mount_options Volume#mount_options}
        :param namespace: The namespace in which to create the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#namespace Volume#namespace}
        :param parameters: An optional key-value map of strings passed directly to the CSI plugin to configure the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#parameters Volume#parameters}
        :param secrets: An optional key-value map of strings used as credentials for publishing and unpublishing volumes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#secrets Volume#secrets}
        :param topology_request: topology_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#topology_request Volume#topology_request}
        :param type: The type of the volume. Currently, only 'csi' is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#type Volume#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Volume.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VolumeConfig(
            external_id=external_id,
            name=name,
            plugin_id=plugin_id,
            volume_id=volume_id,
            access_mode=access_mode,
            attachment_mode=attachment_mode,
            capability=capability,
            context=context,
            deregister_on_destroy=deregister_on_destroy,
            id=id,
            mount_options=mount_options,
            namespace=namespace,
            parameters=parameters,
            secrets=secrets,
            topology_request=topology_request,
            type=type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCapability")
    def put_capability(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VolumeCapability", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Volume.put_capability)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCapability", [value]))

    @jsii.member(jsii_name="putMountOptions")
    def put_mount_options(
        self,
        *,
        fs_type: typing.Optional[builtins.str] = None,
        mount_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fs_type: The file system type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#fs_type Volume#fs_type}
        :param mount_flags: The flags passed to mount. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#mount_flags Volume#mount_flags}
        '''
        value = VolumeMountOptions(fs_type=fs_type, mount_flags=mount_flags)

        return typing.cast(None, jsii.invoke(self, "putMountOptions", [value]))

    @jsii.member(jsii_name="putTopologyRequest")
    def put_topology_request(
        self,
        *,
        required: typing.Optional[typing.Union["VolumeTopologyRequestRequired", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param required: required block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#required Volume#required}
        '''
        value = VolumeTopologyRequest(required=required)

        return typing.cast(None, jsii.invoke(self, "putTopologyRequest", [value]))

    @jsii.member(jsii_name="resetAccessMode")
    def reset_access_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessMode", []))

    @jsii.member(jsii_name="resetAttachmentMode")
    def reset_attachment_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttachmentMode", []))

    @jsii.member(jsii_name="resetCapability")
    def reset_capability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapability", []))

    @jsii.member(jsii_name="resetContext")
    def reset_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContext", []))

    @jsii.member(jsii_name="resetDeregisterOnDestroy")
    def reset_deregister_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeregisterOnDestroy", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMountOptions")
    def reset_mount_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountOptions", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetSecrets")
    def reset_secrets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecrets", []))

    @jsii.member(jsii_name="resetTopologyRequest")
    def reset_topology_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTopologyRequest", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="capability")
    def capability(self) -> "VolumeCapabilityList":
        return typing.cast("VolumeCapabilityList", jsii.get(self, "capability"))

    @builtins.property
    @jsii.member(jsii_name="controllerRequired")
    def controller_required(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "controllerRequired"))

    @builtins.property
    @jsii.member(jsii_name="controllersExpected")
    def controllers_expected(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "controllersExpected"))

    @builtins.property
    @jsii.member(jsii_name="controllersHealthy")
    def controllers_healthy(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "controllersHealthy"))

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> "VolumeMountOptionsOutputReference":
        return typing.cast("VolumeMountOptionsOutputReference", jsii.get(self, "mountOptions"))

    @builtins.property
    @jsii.member(jsii_name="nodesExpected")
    def nodes_expected(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nodesExpected"))

    @builtins.property
    @jsii.member(jsii_name="nodesHealthy")
    def nodes_healthy(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nodesHealthy"))

    @builtins.property
    @jsii.member(jsii_name="pluginProvider")
    def plugin_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginProvider"))

    @builtins.property
    @jsii.member(jsii_name="pluginProviderVersion")
    def plugin_provider_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginProviderVersion"))

    @builtins.property
    @jsii.member(jsii_name="schedulable")
    def schedulable(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "schedulable"))

    @builtins.property
    @jsii.member(jsii_name="topologies")
    def topologies(self) -> "VolumeTopologiesList":
        return typing.cast("VolumeTopologiesList", jsii.get(self, "topologies"))

    @builtins.property
    @jsii.member(jsii_name="topologyRequest")
    def topology_request(self) -> "VolumeTopologyRequestOutputReference":
        return typing.cast("VolumeTopologyRequestOutputReference", jsii.get(self, "topologyRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessModeInput")
    def access_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessModeInput"))

    @builtins.property
    @jsii.member(jsii_name="attachmentModeInput")
    def attachment_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attachmentModeInput"))

    @builtins.property
    @jsii.member(jsii_name="capabilityInput")
    def capability_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VolumeCapability"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VolumeCapability"]]], jsii.get(self, "capabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="contextInput")
    def context_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "contextInput"))

    @builtins.property
    @jsii.member(jsii_name="deregisterOnDestroyInput")
    def deregister_on_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deregisterOnDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="externalIdInput")
    def external_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional["VolumeMountOptions"]:
        return typing.cast(typing.Optional["VolumeMountOptions"], jsii.get(self, "mountOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginIdInput")
    def plugin_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginIdInput"))

    @builtins.property
    @jsii.member(jsii_name="secretsInput")
    def secrets_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "secretsInput"))

    @builtins.property
    @jsii.member(jsii_name="topologyRequestInput")
    def topology_request_input(self) -> typing.Optional["VolumeTopologyRequest"]:
        return typing.cast(typing.Optional["VolumeTopologyRequest"], jsii.get(self, "topologyRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeIdInput")
    def volume_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accessMode")
    def access_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessMode"))

    @access_mode.setter
    def access_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Volume, "access_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessMode", value)

    @builtins.property
    @jsii.member(jsii_name="attachmentMode")
    def attachment_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attachmentMode"))

    @attachment_mode.setter
    def attachment_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Volume, "attachment_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attachmentMode", value)

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "context"))

    @context.setter
    def context(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Volume, "context").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)

    @builtins.property
    @jsii.member(jsii_name="deregisterOnDestroy")
    def deregister_on_destroy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deregisterOnDestroy"))

    @deregister_on_destroy.setter
    def deregister_on_destroy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Volume, "deregister_on_destroy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deregisterOnDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="externalId")
    def external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalId"))

    @external_id.setter
    def external_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Volume, "external_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Volume, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Volume, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Volume, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Volume, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="pluginId")
    def plugin_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginId"))

    @plugin_id.setter
    def plugin_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Volume, "plugin_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginId", value)

    @builtins.property
    @jsii.member(jsii_name="secrets")
    def secrets(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "secrets"))

    @secrets.setter
    def secrets(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Volume, "secrets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secrets", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Volume, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @volume_id.setter
    def volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Volume, "volume_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.volume.VolumeCapability",
    jsii_struct_bases=[],
    name_mapping={"access_mode": "accessMode", "attachment_mode": "attachmentMode"},
)
class VolumeCapability:
    def __init__(
        self,
        *,
        access_mode: builtins.str,
        attachment_mode: builtins.str,
    ) -> None:
        '''
        :param access_mode: Defines whether a volume should be available concurrently. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#access_mode Volume#access_mode}
        :param attachment_mode: The storage API that will be used by the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#attachment_mode Volume#attachment_mode}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VolumeCapability.__init__)
            check_type(argname="argument access_mode", value=access_mode, expected_type=type_hints["access_mode"])
            check_type(argname="argument attachment_mode", value=attachment_mode, expected_type=type_hints["attachment_mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "access_mode": access_mode,
            "attachment_mode": attachment_mode,
        }

    @builtins.property
    def access_mode(self) -> builtins.str:
        '''Defines whether a volume should be available concurrently.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#access_mode Volume#access_mode}
        '''
        result = self._values.get("access_mode")
        assert result is not None, "Required property 'access_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attachment_mode(self) -> builtins.str:
        '''The storage API that will be used by the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#attachment_mode Volume#attachment_mode}
        '''
        result = self._values.get("attachment_mode")
        assert result is not None, "Required property 'attachment_mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeCapability(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VolumeCapabilityList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeCapabilityList",
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
            type_hints = typing.get_type_hints(VolumeCapabilityList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "VolumeCapabilityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VolumeCapabilityList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VolumeCapabilityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeCapabilityList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VolumeCapabilityList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VolumeCapabilityList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VolumeCapability]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VolumeCapability]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VolumeCapability]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeCapabilityList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VolumeCapabilityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeCapabilityOutputReference",
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
            type_hints = typing.get_type_hints(VolumeCapabilityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="accessModeInput")
    def access_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessModeInput"))

    @builtins.property
    @jsii.member(jsii_name="attachmentModeInput")
    def attachment_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attachmentModeInput"))

    @builtins.property
    @jsii.member(jsii_name="accessMode")
    def access_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessMode"))

    @access_mode.setter
    def access_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeCapabilityOutputReference, "access_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessMode", value)

    @builtins.property
    @jsii.member(jsii_name="attachmentMode")
    def attachment_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attachmentMode"))

    @attachment_mode.setter
    def attachment_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeCapabilityOutputReference, "attachment_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attachmentMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VolumeCapability, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VolumeCapability, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VolumeCapability, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeCapabilityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.volume.VolumeConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "external_id": "externalId",
        "name": "name",
        "plugin_id": "pluginId",
        "volume_id": "volumeId",
        "access_mode": "accessMode",
        "attachment_mode": "attachmentMode",
        "capability": "capability",
        "context": "context",
        "deregister_on_destroy": "deregisterOnDestroy",
        "id": "id",
        "mount_options": "mountOptions",
        "namespace": "namespace",
        "parameters": "parameters",
        "secrets": "secrets",
        "topology_request": "topologyRequest",
        "type": "type",
    },
)
class VolumeConfig(cdktf.TerraformMetaArguments):
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
        external_id: builtins.str,
        name: builtins.str,
        plugin_id: builtins.str,
        volume_id: builtins.str,
        access_mode: typing.Optional[builtins.str] = None,
        attachment_mode: typing.Optional[builtins.str] = None,
        capability: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[VolumeCapability, typing.Dict[str, typing.Any]]]]] = None,
        context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        deregister_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[typing.Union["VolumeMountOptions", typing.Dict[str, typing.Any]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        topology_request: typing.Optional[typing.Union["VolumeTopologyRequest", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param external_id: The ID of the physical volume from the storage provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#external_id Volume#external_id}
        :param name: The display name of the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#name Volume#name}
        :param plugin_id: The ID of the CSI plugin that manages this volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#plugin_id Volume#plugin_id}
        :param volume_id: The unique ID of the volume, how jobs will refer to the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#volume_id Volume#volume_id}
        :param access_mode: Defines whether a volume should be available concurrently. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#access_mode Volume#access_mode}
        :param attachment_mode: The storage API that will be used by the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#attachment_mode Volume#attachment_mode}
        :param capability: capability block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#capability Volume#capability}
        :param context: An optional key-value map of strings passed directly to the CSI plugin to validate the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#context Volume#context}
        :param deregister_on_destroy: If true, the volume will be deregistered on destroy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#deregister_on_destroy Volume#deregister_on_destroy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#id Volume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mount_options: mount_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#mount_options Volume#mount_options}
        :param namespace: The namespace in which to create the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#namespace Volume#namespace}
        :param parameters: An optional key-value map of strings passed directly to the CSI plugin to configure the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#parameters Volume#parameters}
        :param secrets: An optional key-value map of strings used as credentials for publishing and unpublishing volumes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#secrets Volume#secrets}
        :param topology_request: topology_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#topology_request Volume#topology_request}
        :param type: The type of the volume. Currently, only 'csi' is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#type Volume#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(mount_options, dict):
            mount_options = VolumeMountOptions(**mount_options)
        if isinstance(topology_request, dict):
            topology_request = VolumeTopologyRequest(**topology_request)
        if __debug__:
            type_hints = typing.get_type_hints(VolumeConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument plugin_id", value=plugin_id, expected_type=type_hints["plugin_id"])
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument access_mode", value=access_mode, expected_type=type_hints["access_mode"])
            check_type(argname="argument attachment_mode", value=attachment_mode, expected_type=type_hints["attachment_mode"])
            check_type(argname="argument capability", value=capability, expected_type=type_hints["capability"])
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument deregister_on_destroy", value=deregister_on_destroy, expected_type=type_hints["deregister_on_destroy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument secrets", value=secrets, expected_type=type_hints["secrets"])
            check_type(argname="argument topology_request", value=topology_request, expected_type=type_hints["topology_request"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "external_id": external_id,
            "name": name,
            "plugin_id": plugin_id,
            "volume_id": volume_id,
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
        if access_mode is not None:
            self._values["access_mode"] = access_mode
        if attachment_mode is not None:
            self._values["attachment_mode"] = attachment_mode
        if capability is not None:
            self._values["capability"] = capability
        if context is not None:
            self._values["context"] = context
        if deregister_on_destroy is not None:
            self._values["deregister_on_destroy"] = deregister_on_destroy
        if id is not None:
            self._values["id"] = id
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if namespace is not None:
            self._values["namespace"] = namespace
        if parameters is not None:
            self._values["parameters"] = parameters
        if secrets is not None:
            self._values["secrets"] = secrets
        if topology_request is not None:
            self._values["topology_request"] = topology_request
        if type is not None:
            self._values["type"] = type

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
    def external_id(self) -> builtins.str:
        '''The ID of the physical volume from the storage provider.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#external_id Volume#external_id}
        '''
        result = self._values.get("external_id")
        assert result is not None, "Required property 'external_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The display name of the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#name Volume#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def plugin_id(self) -> builtins.str:
        '''The ID of the CSI plugin that manages this volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#plugin_id Volume#plugin_id}
        '''
        result = self._values.get("plugin_id")
        assert result is not None, "Required property 'plugin_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''The unique ID of the volume, how jobs will refer to the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#volume_id Volume#volume_id}
        '''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_mode(self) -> typing.Optional[builtins.str]:
        '''Defines whether a volume should be available concurrently.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#access_mode Volume#access_mode}
        '''
        result = self._values.get("access_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attachment_mode(self) -> typing.Optional[builtins.str]:
        '''The storage API that will be used by the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#attachment_mode Volume#attachment_mode}
        '''
        result = self._values.get("attachment_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capability(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VolumeCapability]]]:
        '''capability block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#capability Volume#capability}
        '''
        result = self._values.get("capability")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VolumeCapability]]], result)

    @builtins.property
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An optional key-value map of strings passed directly to the CSI plugin to validate the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#context Volume#context}
        '''
        result = self._values.get("context")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def deregister_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the volume will be deregistered on destroy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#deregister_on_destroy Volume#deregister_on_destroy}
        '''
        result = self._values.get("deregister_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#id Volume#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_options(self) -> typing.Optional["VolumeMountOptions"]:
        '''mount_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#mount_options Volume#mount_options}
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional["VolumeMountOptions"], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace in which to create the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#namespace Volume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An optional key-value map of strings passed directly to the CSI plugin to configure the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#parameters Volume#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def secrets(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An optional key-value map of strings used as credentials for publishing and unpublishing volumes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#secrets Volume#secrets}
        '''
        result = self._values.get("secrets")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def topology_request(self) -> typing.Optional["VolumeTopologyRequest"]:
        '''topology_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#topology_request Volume#topology_request}
        '''
        result = self._values.get("topology_request")
        return typing.cast(typing.Optional["VolumeTopologyRequest"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the volume. Currently, only 'csi' is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#type Volume#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.volume.VolumeMountOptions",
    jsii_struct_bases=[],
    name_mapping={"fs_type": "fsType", "mount_flags": "mountFlags"},
)
class VolumeMountOptions:
    def __init__(
        self,
        *,
        fs_type: typing.Optional[builtins.str] = None,
        mount_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fs_type: The file system type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#fs_type Volume#fs_type}
        :param mount_flags: The flags passed to mount. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#mount_flags Volume#mount_flags}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VolumeMountOptions.__init__)
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument mount_flags", value=mount_flags, expected_type=type_hints["mount_flags"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if mount_flags is not None:
            self._values["mount_flags"] = mount_flags

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''The file system type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#fs_type Volume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_flags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The flags passed to mount.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#mount_flags Volume#mount_flags}
        '''
        result = self._values.get("mount_flags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeMountOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VolumeMountOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeMountOptionsOutputReference",
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
            type_hints = typing.get_type_hints(VolumeMountOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetMountFlags")
    def reset_mount_flags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountFlags", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="mountFlagsInput")
    def mount_flags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "mountFlagsInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeMountOptionsOutputReference, "fs_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="mountFlags")
    def mount_flags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "mountFlags"))

    @mount_flags.setter
    def mount_flags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeMountOptionsOutputReference, "mount_flags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountFlags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VolumeMountOptions]:
        return typing.cast(typing.Optional[VolumeMountOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VolumeMountOptions]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeMountOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologies",
    jsii_struct_bases=[],
    name_mapping={},
)
class VolumeTopologies:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeTopologies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VolumeTopologiesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologiesList",
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
            type_hints = typing.get_type_hints(VolumeTopologiesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "VolumeTopologiesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VolumeTopologiesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VolumeTopologiesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeTopologiesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VolumeTopologiesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VolumeTopologiesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class VolumeTopologiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologiesOutputReference",
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
            type_hints = typing.get_type_hints(VolumeTopologiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="segments")
    def segments(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "segments"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VolumeTopologies]:
        return typing.cast(typing.Optional[VolumeTopologies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VolumeTopologies]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeTopologiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologyRequest",
    jsii_struct_bases=[],
    name_mapping={"required": "required"},
)
class VolumeTopologyRequest:
    def __init__(
        self,
        *,
        required: typing.Optional[typing.Union["VolumeTopologyRequestRequired", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param required: required block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#required Volume#required}
        '''
        if isinstance(required, dict):
            required = VolumeTopologyRequestRequired(**required)
        if __debug__:
            type_hints = typing.get_type_hints(VolumeTopologyRequest.__init__)
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
        self._values: typing.Dict[str, typing.Any] = {}
        if required is not None:
            self._values["required"] = required

    @builtins.property
    def required(self) -> typing.Optional["VolumeTopologyRequestRequired"]:
        '''required block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#required Volume#required}
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional["VolumeTopologyRequestRequired"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeTopologyRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VolumeTopologyRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologyRequestOutputReference",
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
            type_hints = typing.get_type_hints(VolumeTopologyRequestOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequired")
    def put_required(
        self,
        *,
        topology: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VolumeTopologyRequestRequiredTopology", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param topology: topology block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#topology Volume#topology}
        '''
        value = VolumeTopologyRequestRequired(topology=topology)

        return typing.cast(None, jsii.invoke(self, "putRequired", [value]))

    @jsii.member(jsii_name="resetRequired")
    def reset_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequired", []))

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> "VolumeTopologyRequestRequiredOutputReference":
        return typing.cast("VolumeTopologyRequestRequiredOutputReference", jsii.get(self, "required"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(self) -> typing.Optional["VolumeTopologyRequestRequired"]:
        return typing.cast(typing.Optional["VolumeTopologyRequestRequired"], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VolumeTopologyRequest]:
        return typing.cast(typing.Optional[VolumeTopologyRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VolumeTopologyRequest]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeTopologyRequestOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologyRequestRequired",
    jsii_struct_bases=[],
    name_mapping={"topology": "topology"},
)
class VolumeTopologyRequestRequired:
    def __init__(
        self,
        *,
        topology: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VolumeTopologyRequestRequiredTopology", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param topology: topology block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#topology Volume#topology}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VolumeTopologyRequestRequired.__init__)
            check_type(argname="argument topology", value=topology, expected_type=type_hints["topology"])
        self._values: typing.Dict[str, typing.Any] = {
            "topology": topology,
        }

    @builtins.property
    def topology(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["VolumeTopologyRequestRequiredTopology"]]:
        '''topology block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#topology Volume#topology}
        '''
        result = self._values.get("topology")
        assert result is not None, "Required property 'topology' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["VolumeTopologyRequestRequiredTopology"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeTopologyRequestRequired(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VolumeTopologyRequestRequiredOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologyRequestRequiredOutputReference",
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
            type_hints = typing.get_type_hints(VolumeTopologyRequestRequiredOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTopology")
    def put_topology(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VolumeTopologyRequestRequiredTopology", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VolumeTopologyRequestRequiredOutputReference.put_topology)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTopology", [value]))

    @builtins.property
    @jsii.member(jsii_name="topology")
    def topology(self) -> "VolumeTopologyRequestRequiredTopologyList":
        return typing.cast("VolumeTopologyRequestRequiredTopologyList", jsii.get(self, "topology"))

    @builtins.property
    @jsii.member(jsii_name="topologyInput")
    def topology_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VolumeTopologyRequestRequiredTopology"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VolumeTopologyRequestRequiredTopology"]]], jsii.get(self, "topologyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VolumeTopologyRequestRequired]:
        return typing.cast(typing.Optional[VolumeTopologyRequestRequired], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VolumeTopologyRequestRequired],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeTopologyRequestRequiredOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologyRequestRequiredTopology",
    jsii_struct_bases=[],
    name_mapping={"segments": "segments"},
)
class VolumeTopologyRequestRequiredTopology:
    def __init__(self, *, segments: typing.Mapping[builtins.str, builtins.str]) -> None:
        '''
        :param segments: Define attributes for the topology request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#segments Volume#segments}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VolumeTopologyRequestRequiredTopology.__init__)
            check_type(argname="argument segments", value=segments, expected_type=type_hints["segments"])
        self._values: typing.Dict[str, typing.Any] = {
            "segments": segments,
        }

    @builtins.property
    def segments(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Define attributes for the topology request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#segments Volume#segments}
        '''
        result = self._values.get("segments")
        assert result is not None, "Required property 'segments' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeTopologyRequestRequiredTopology(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VolumeTopologyRequestRequiredTopologyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologyRequestRequiredTopologyList",
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
            type_hints = typing.get_type_hints(VolumeTopologyRequestRequiredTopologyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VolumeTopologyRequestRequiredTopologyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VolumeTopologyRequestRequiredTopologyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VolumeTopologyRequestRequiredTopologyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeTopologyRequestRequiredTopologyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VolumeTopologyRequestRequiredTopologyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VolumeTopologyRequestRequiredTopologyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VolumeTopologyRequestRequiredTopology]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VolumeTopologyRequestRequiredTopology]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VolumeTopologyRequestRequiredTopology]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeTopologyRequestRequiredTopologyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VolumeTopologyRequestRequiredTopologyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologyRequestRequiredTopologyOutputReference",
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
            type_hints = typing.get_type_hints(VolumeTopologyRequestRequiredTopologyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="segmentsInput")
    def segments_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "segmentsInput"))

    @builtins.property
    @jsii.member(jsii_name="segments")
    def segments(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "segments"))

    @segments.setter
    def segments(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeTopologyRequestRequiredTopologyOutputReference, "segments").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "segments", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VolumeTopologyRequestRequiredTopology, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VolumeTopologyRequestRequiredTopology, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VolumeTopologyRequestRequiredTopology, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VolumeTopologyRequestRequiredTopologyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Volume",
    "VolumeCapability",
    "VolumeCapabilityList",
    "VolumeCapabilityOutputReference",
    "VolumeConfig",
    "VolumeMountOptions",
    "VolumeMountOptionsOutputReference",
    "VolumeTopologies",
    "VolumeTopologiesList",
    "VolumeTopologiesOutputReference",
    "VolumeTopologyRequest",
    "VolumeTopologyRequestOutputReference",
    "VolumeTopologyRequestRequired",
    "VolumeTopologyRequestRequiredOutputReference",
    "VolumeTopologyRequestRequiredTopology",
    "VolumeTopologyRequestRequiredTopologyList",
    "VolumeTopologyRequestRequiredTopologyOutputReference",
]

publication.publish()
