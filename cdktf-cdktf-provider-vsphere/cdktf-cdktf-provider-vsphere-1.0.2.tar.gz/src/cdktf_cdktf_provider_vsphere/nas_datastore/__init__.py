'''
# `vsphere_nas_datastore`

Refer to the Terraform Registory for docs: [`vsphere_nas_datastore`](https://www.terraform.io/docs/providers/vsphere/r/nas_datastore).
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


class NasDatastore(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.nasDatastore.NasDatastore",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore vsphere_nas_datastore}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        host_system_ids: typing.Sequence[builtins.str],
        name: builtins.str,
        remote_hosts: typing.Sequence[builtins.str],
        remote_path: builtins.str,
        access_mode: typing.Optional[builtins.str] = None,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        datastore_cluster_id: typing.Optional[builtins.str] = None,
        folder: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        security_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore vsphere_nas_datastore} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param host_system_ids: The managed object IDs of the hosts to mount the datastore on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#host_system_ids NasDatastore#host_system_ids}
        :param name: The name of the datastore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#name NasDatastore#name}
        :param remote_hosts: The hostnames or IP addresses of the remote server or servers. Only one element should be present for NFS v3 but multiple can be present for NFS v4.1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#remote_hosts NasDatastore#remote_hosts}
        :param remote_path: The remote path of the mount point. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#remote_path NasDatastore#remote_path}
        :param access_mode: Access mode for the mount point. Can be one of readOnly or readWrite. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#access_mode NasDatastore#access_mode}
        :param custom_attributes: A list of custom attributes to set on this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#custom_attributes NasDatastore#custom_attributes}
        :param datastore_cluster_id: The managed object ID of the datastore cluster to place the datastore in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#datastore_cluster_id NasDatastore#datastore_cluster_id}
        :param folder: The path to the datastore folder to put the datastore in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#folder NasDatastore#folder}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#id NasDatastore#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security_type: The security type to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#security_type NasDatastore#security_type}
        :param tags: A list of tag IDs to apply to this object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#tags NasDatastore#tags}
        :param type: The type of NAS volume. Can be one of NFS (to denote v3) or NFS41 (to denote NFS v4.1). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#type NasDatastore#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NasDatastore.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NasDatastoreConfig(
            host_system_ids=host_system_ids,
            name=name,
            remote_hosts=remote_hosts,
            remote_path=remote_path,
            access_mode=access_mode,
            custom_attributes=custom_attributes,
            datastore_cluster_id=datastore_cluster_id,
            folder=folder,
            id=id,
            security_type=security_type,
            tags=tags,
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

    @jsii.member(jsii_name="resetAccessMode")
    def reset_access_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessMode", []))

    @jsii.member(jsii_name="resetCustomAttributes")
    def reset_custom_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomAttributes", []))

    @jsii.member(jsii_name="resetDatastoreClusterId")
    def reset_datastore_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatastoreClusterId", []))

    @jsii.member(jsii_name="resetFolder")
    def reset_folder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFolder", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSecurityType")
    def reset_security_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityType", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="accessible")
    def accessible(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "accessible"))

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacity"))

    @builtins.property
    @jsii.member(jsii_name="freeSpace")
    def free_space(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "freeSpace"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceMode")
    def maintenance_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenanceMode"))

    @builtins.property
    @jsii.member(jsii_name="multipleHostAccess")
    def multiple_host_access(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "multipleHostAccess"))

    @builtins.property
    @jsii.member(jsii_name="protocolEndpoint")
    def protocol_endpoint(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "protocolEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="uncommittedSpace")
    def uncommitted_space(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "uncommittedSpace"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="accessModeInput")
    def access_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessModeInput"))

    @builtins.property
    @jsii.member(jsii_name="customAttributesInput")
    def custom_attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="datastoreClusterIdInput")
    def datastore_cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datastoreClusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="folderInput")
    def folder_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "folderInput"))

    @builtins.property
    @jsii.member(jsii_name="hostSystemIdsInput")
    def host_system_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hostSystemIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteHostsInput")
    def remote_hosts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "remoteHostsInput"))

    @builtins.property
    @jsii.member(jsii_name="remotePathInput")
    def remote_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remotePathInput"))

    @builtins.property
    @jsii.member(jsii_name="securityTypeInput")
    def security_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="accessMode")
    def access_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessMode"))

    @access_mode.setter
    def access_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NasDatastore, "access_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessMode", value)

    @builtins.property
    @jsii.member(jsii_name="customAttributes")
    def custom_attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customAttributes"))

    @custom_attributes.setter
    def custom_attributes(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NasDatastore, "custom_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="datastoreClusterId")
    def datastore_cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datastoreClusterId"))

    @datastore_cluster_id.setter
    def datastore_cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NasDatastore, "datastore_cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datastoreClusterId", value)

    @builtins.property
    @jsii.member(jsii_name="folder")
    def folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "folder"))

    @folder.setter
    def folder(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NasDatastore, "folder").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "folder", value)

    @builtins.property
    @jsii.member(jsii_name="hostSystemIds")
    def host_system_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hostSystemIds"))

    @host_system_ids.setter
    def host_system_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NasDatastore, "host_system_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostSystemIds", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NasDatastore, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NasDatastore, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="remoteHosts")
    def remote_hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "remoteHosts"))

    @remote_hosts.setter
    def remote_hosts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NasDatastore, "remote_hosts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteHosts", value)

    @builtins.property
    @jsii.member(jsii_name="remotePath")
    def remote_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remotePath"))

    @remote_path.setter
    def remote_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NasDatastore, "remote_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remotePath", value)

    @builtins.property
    @jsii.member(jsii_name="securityType")
    def security_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityType"))

    @security_type.setter
    def security_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NasDatastore, "security_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NasDatastore, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NasDatastore, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.nasDatastore.NasDatastoreConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "host_system_ids": "hostSystemIds",
        "name": "name",
        "remote_hosts": "remoteHosts",
        "remote_path": "remotePath",
        "access_mode": "accessMode",
        "custom_attributes": "customAttributes",
        "datastore_cluster_id": "datastoreClusterId",
        "folder": "folder",
        "id": "id",
        "security_type": "securityType",
        "tags": "tags",
        "type": "type",
    },
)
class NasDatastoreConfig(cdktf.TerraformMetaArguments):
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
        host_system_ids: typing.Sequence[builtins.str],
        name: builtins.str,
        remote_hosts: typing.Sequence[builtins.str],
        remote_path: builtins.str,
        access_mode: typing.Optional[builtins.str] = None,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        datastore_cluster_id: typing.Optional[builtins.str] = None,
        folder: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        security_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        :param host_system_ids: The managed object IDs of the hosts to mount the datastore on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#host_system_ids NasDatastore#host_system_ids}
        :param name: The name of the datastore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#name NasDatastore#name}
        :param remote_hosts: The hostnames or IP addresses of the remote server or servers. Only one element should be present for NFS v3 but multiple can be present for NFS v4.1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#remote_hosts NasDatastore#remote_hosts}
        :param remote_path: The remote path of the mount point. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#remote_path NasDatastore#remote_path}
        :param access_mode: Access mode for the mount point. Can be one of readOnly or readWrite. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#access_mode NasDatastore#access_mode}
        :param custom_attributes: A list of custom attributes to set on this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#custom_attributes NasDatastore#custom_attributes}
        :param datastore_cluster_id: The managed object ID of the datastore cluster to place the datastore in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#datastore_cluster_id NasDatastore#datastore_cluster_id}
        :param folder: The path to the datastore folder to put the datastore in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#folder NasDatastore#folder}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#id NasDatastore#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security_type: The security type to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#security_type NasDatastore#security_type}
        :param tags: A list of tag IDs to apply to this object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#tags NasDatastore#tags}
        :param type: The type of NAS volume. Can be one of NFS (to denote v3) or NFS41 (to denote NFS v4.1). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#type NasDatastore#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(NasDatastoreConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument host_system_ids", value=host_system_ids, expected_type=type_hints["host_system_ids"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument remote_hosts", value=remote_hosts, expected_type=type_hints["remote_hosts"])
            check_type(argname="argument remote_path", value=remote_path, expected_type=type_hints["remote_path"])
            check_type(argname="argument access_mode", value=access_mode, expected_type=type_hints["access_mode"])
            check_type(argname="argument custom_attributes", value=custom_attributes, expected_type=type_hints["custom_attributes"])
            check_type(argname="argument datastore_cluster_id", value=datastore_cluster_id, expected_type=type_hints["datastore_cluster_id"])
            check_type(argname="argument folder", value=folder, expected_type=type_hints["folder"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument security_type", value=security_type, expected_type=type_hints["security_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_system_ids": host_system_ids,
            "name": name,
            "remote_hosts": remote_hosts,
            "remote_path": remote_path,
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
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if datastore_cluster_id is not None:
            self._values["datastore_cluster_id"] = datastore_cluster_id
        if folder is not None:
            self._values["folder"] = folder
        if id is not None:
            self._values["id"] = id
        if security_type is not None:
            self._values["security_type"] = security_type
        if tags is not None:
            self._values["tags"] = tags
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
    def host_system_ids(self) -> typing.List[builtins.str]:
        '''The managed object IDs of the hosts to mount the datastore on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#host_system_ids NasDatastore#host_system_ids}
        '''
        result = self._values.get("host_system_ids")
        assert result is not None, "Required property 'host_system_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the datastore.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#name NasDatastore#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def remote_hosts(self) -> typing.List[builtins.str]:
        '''The hostnames or IP addresses of the remote server or servers.

        Only one element should be present for NFS v3 but multiple can be present for NFS v4.1.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#remote_hosts NasDatastore#remote_hosts}
        '''
        result = self._values.get("remote_hosts")
        assert result is not None, "Required property 'remote_hosts' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def remote_path(self) -> builtins.str:
        '''The remote path of the mount point.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#remote_path NasDatastore#remote_path}
        '''
        result = self._values.get("remote_path")
        assert result is not None, "Required property 'remote_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_mode(self) -> typing.Optional[builtins.str]:
        '''Access mode for the mount point. Can be one of readOnly or readWrite.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#access_mode NasDatastore#access_mode}
        '''
        result = self._values.get("access_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of custom attributes to set on this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#custom_attributes NasDatastore#custom_attributes}
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def datastore_cluster_id(self) -> typing.Optional[builtins.str]:
        '''The managed object ID of the datastore cluster to place the datastore in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#datastore_cluster_id NasDatastore#datastore_cluster_id}
        '''
        result = self._values.get("datastore_cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def folder(self) -> typing.Optional[builtins.str]:
        '''The path to the datastore folder to put the datastore in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#folder NasDatastore#folder}
        '''
        result = self._values.get("folder")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#id NasDatastore#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_type(self) -> typing.Optional[builtins.str]:
        '''The security type to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#security_type NasDatastore#security_type}
        '''
        result = self._values.get("security_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of tag IDs to apply to this object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#tags NasDatastore#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of NAS volume. Can be one of NFS (to denote v3) or NFS41 (to denote NFS v4.1).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/nas_datastore#type NasDatastore#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NasDatastoreConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "NasDatastore",
    "NasDatastoreConfig",
]

publication.publish()
