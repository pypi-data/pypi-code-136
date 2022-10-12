'''
# `azurerm_data_factory_dataset_binary`

Refer to the Terraform Registory for docs: [`azurerm_data_factory_dataset_binary`](https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary).
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


class DataFactoryDatasetBinary(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryDatasetBinary.DataFactoryDatasetBinary",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary azurerm_data_factory_dataset_binary}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        data_factory_id: builtins.str,
        linked_service_name: builtins.str,
        name: builtins.str,
        additional_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        annotations: typing.Optional[typing.Sequence[builtins.str]] = None,
        azure_blob_storage_location: typing.Optional[typing.Union["DataFactoryDatasetBinaryAzureBlobStorageLocation", typing.Dict[str, typing.Any]]] = None,
        compression: typing.Optional[typing.Union["DataFactoryDatasetBinaryCompression", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        folder: typing.Optional[builtins.str] = None,
        http_server_location: typing.Optional[typing.Union["DataFactoryDatasetBinaryHttpServerLocation", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        sftp_server_location: typing.Optional[typing.Union["DataFactoryDatasetBinarySftpServerLocation", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["DataFactoryDatasetBinaryTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary azurerm_data_factory_dataset_binary} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_factory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#data_factory_id DataFactoryDatasetBinary#data_factory_id}.
        :param linked_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#linked_service_name DataFactoryDatasetBinary#linked_service_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#name DataFactoryDatasetBinary#name}.
        :param additional_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#additional_properties DataFactoryDatasetBinary#additional_properties}.
        :param annotations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#annotations DataFactoryDatasetBinary#annotations}.
        :param azure_blob_storage_location: azure_blob_storage_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#azure_blob_storage_location DataFactoryDatasetBinary#azure_blob_storage_location}
        :param compression: compression block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#compression DataFactoryDatasetBinary#compression}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#description DataFactoryDatasetBinary#description}.
        :param folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#folder DataFactoryDatasetBinary#folder}.
        :param http_server_location: http_server_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#http_server_location DataFactoryDatasetBinary#http_server_location}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#id DataFactoryDatasetBinary#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#parameters DataFactoryDatasetBinary#parameters}.
        :param sftp_server_location: sftp_server_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#sftp_server_location DataFactoryDatasetBinary#sftp_server_location}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#timeouts DataFactoryDatasetBinary#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryDatasetBinary.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataFactoryDatasetBinaryConfig(
            data_factory_id=data_factory_id,
            linked_service_name=linked_service_name,
            name=name,
            additional_properties=additional_properties,
            annotations=annotations,
            azure_blob_storage_location=azure_blob_storage_location,
            compression=compression,
            description=description,
            folder=folder,
            http_server_location=http_server_location,
            id=id,
            parameters=parameters,
            sftp_server_location=sftp_server_location,
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

    @jsii.member(jsii_name="putAzureBlobStorageLocation")
    def put_azure_blob_storage_location(
        self,
        *,
        container: builtins.str,
        dynamic_container_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dynamic_filename_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dynamic_path_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        filename: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#container DataFactoryDatasetBinary#container}.
        :param dynamic_container_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_container_enabled DataFactoryDatasetBinary#dynamic_container_enabled}.
        :param dynamic_filename_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_filename_enabled DataFactoryDatasetBinary#dynamic_filename_enabled}.
        :param dynamic_path_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_path_enabled DataFactoryDatasetBinary#dynamic_path_enabled}.
        :param filename: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#filename DataFactoryDatasetBinary#filename}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#path DataFactoryDatasetBinary#path}.
        '''
        value = DataFactoryDatasetBinaryAzureBlobStorageLocation(
            container=container,
            dynamic_container_enabled=dynamic_container_enabled,
            dynamic_filename_enabled=dynamic_filename_enabled,
            dynamic_path_enabled=dynamic_path_enabled,
            filename=filename,
            path=path,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureBlobStorageLocation", [value]))

    @jsii.member(jsii_name="putCompression")
    def put_compression(
        self,
        *,
        type: builtins.str,
        level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#type DataFactoryDatasetBinary#type}.
        :param level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#level DataFactoryDatasetBinary#level}.
        '''
        value = DataFactoryDatasetBinaryCompression(type=type, level=level)

        return typing.cast(None, jsii.invoke(self, "putCompression", [value]))

    @jsii.member(jsii_name="putHttpServerLocation")
    def put_http_server_location(
        self,
        *,
        filename: builtins.str,
        path: builtins.str,
        relative_url: builtins.str,
        dynamic_filename_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dynamic_path_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param filename: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#filename DataFactoryDatasetBinary#filename}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#path DataFactoryDatasetBinary#path}.
        :param relative_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#relative_url DataFactoryDatasetBinary#relative_url}.
        :param dynamic_filename_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_filename_enabled DataFactoryDatasetBinary#dynamic_filename_enabled}.
        :param dynamic_path_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_path_enabled DataFactoryDatasetBinary#dynamic_path_enabled}.
        '''
        value = DataFactoryDatasetBinaryHttpServerLocation(
            filename=filename,
            path=path,
            relative_url=relative_url,
            dynamic_filename_enabled=dynamic_filename_enabled,
            dynamic_path_enabled=dynamic_path_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpServerLocation", [value]))

    @jsii.member(jsii_name="putSftpServerLocation")
    def put_sftp_server_location(
        self,
        *,
        filename: builtins.str,
        path: builtins.str,
        dynamic_filename_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dynamic_path_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param filename: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#filename DataFactoryDatasetBinary#filename}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#path DataFactoryDatasetBinary#path}.
        :param dynamic_filename_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_filename_enabled DataFactoryDatasetBinary#dynamic_filename_enabled}.
        :param dynamic_path_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_path_enabled DataFactoryDatasetBinary#dynamic_path_enabled}.
        '''
        value = DataFactoryDatasetBinarySftpServerLocation(
            filename=filename,
            path=path,
            dynamic_filename_enabled=dynamic_filename_enabled,
            dynamic_path_enabled=dynamic_path_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putSftpServerLocation", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#create DataFactoryDatasetBinary#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#delete DataFactoryDatasetBinary#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#read DataFactoryDatasetBinary#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#update DataFactoryDatasetBinary#update}.
        '''
        value = DataFactoryDatasetBinaryTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdditionalProperties")
    def reset_additional_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalProperties", []))

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetAzureBlobStorageLocation")
    def reset_azure_blob_storage_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureBlobStorageLocation", []))

    @jsii.member(jsii_name="resetCompression")
    def reset_compression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompression", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFolder")
    def reset_folder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFolder", []))

    @jsii.member(jsii_name="resetHttpServerLocation")
    def reset_http_server_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpServerLocation", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetSftpServerLocation")
    def reset_sftp_server_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSftpServerLocation", []))

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
    @jsii.member(jsii_name="azureBlobStorageLocation")
    def azure_blob_storage_location(
        self,
    ) -> "DataFactoryDatasetBinaryAzureBlobStorageLocationOutputReference":
        return typing.cast("DataFactoryDatasetBinaryAzureBlobStorageLocationOutputReference", jsii.get(self, "azureBlobStorageLocation"))

    @builtins.property
    @jsii.member(jsii_name="compression")
    def compression(self) -> "DataFactoryDatasetBinaryCompressionOutputReference":
        return typing.cast("DataFactoryDatasetBinaryCompressionOutputReference", jsii.get(self, "compression"))

    @builtins.property
    @jsii.member(jsii_name="httpServerLocation")
    def http_server_location(
        self,
    ) -> "DataFactoryDatasetBinaryHttpServerLocationOutputReference":
        return typing.cast("DataFactoryDatasetBinaryHttpServerLocationOutputReference", jsii.get(self, "httpServerLocation"))

    @builtins.property
    @jsii.member(jsii_name="sftpServerLocation")
    def sftp_server_location(
        self,
    ) -> "DataFactoryDatasetBinarySftpServerLocationOutputReference":
        return typing.cast("DataFactoryDatasetBinarySftpServerLocationOutputReference", jsii.get(self, "sftpServerLocation"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DataFactoryDatasetBinaryTimeoutsOutputReference":
        return typing.cast("DataFactoryDatasetBinaryTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="additionalPropertiesInput")
    def additional_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "additionalPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "annotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="azureBlobStorageLocationInput")
    def azure_blob_storage_location_input(
        self,
    ) -> typing.Optional["DataFactoryDatasetBinaryAzureBlobStorageLocation"]:
        return typing.cast(typing.Optional["DataFactoryDatasetBinaryAzureBlobStorageLocation"], jsii.get(self, "azureBlobStorageLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionInput")
    def compression_input(
        self,
    ) -> typing.Optional["DataFactoryDatasetBinaryCompression"]:
        return typing.cast(typing.Optional["DataFactoryDatasetBinaryCompression"], jsii.get(self, "compressionInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFactoryIdInput")
    def data_factory_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataFactoryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="folderInput")
    def folder_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "folderInput"))

    @builtins.property
    @jsii.member(jsii_name="httpServerLocationInput")
    def http_server_location_input(
        self,
    ) -> typing.Optional["DataFactoryDatasetBinaryHttpServerLocation"]:
        return typing.cast(typing.Optional["DataFactoryDatasetBinaryHttpServerLocation"], jsii.get(self, "httpServerLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedServiceNameInput")
    def linked_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "linkedServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="sftpServerLocationInput")
    def sftp_server_location_input(
        self,
    ) -> typing.Optional["DataFactoryDatasetBinarySftpServerLocation"]:
        return typing.cast(typing.Optional["DataFactoryDatasetBinarySftpServerLocation"], jsii.get(self, "sftpServerLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataFactoryDatasetBinaryTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataFactoryDatasetBinaryTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalProperties")
    def additional_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "additionalProperties"))

    @additional_properties.setter
    def additional_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinary, "additional_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalProperties", value)

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinary, "annotations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="dataFactoryId")
    def data_factory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFactoryId"))

    @data_factory_id.setter
    def data_factory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinary, "data_factory_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFactoryId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinary, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="folder")
    def folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "folder"))

    @folder.setter
    def folder(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinary, "folder").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "folder", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinary, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="linkedServiceName")
    def linked_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "linkedServiceName"))

    @linked_service_name.setter
    def linked_service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinary, "linked_service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkedServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinary, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinary, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryDatasetBinary.DataFactoryDatasetBinaryAzureBlobStorageLocation",
    jsii_struct_bases=[],
    name_mapping={
        "container": "container",
        "dynamic_container_enabled": "dynamicContainerEnabled",
        "dynamic_filename_enabled": "dynamicFilenameEnabled",
        "dynamic_path_enabled": "dynamicPathEnabled",
        "filename": "filename",
        "path": "path",
    },
)
class DataFactoryDatasetBinaryAzureBlobStorageLocation:
    def __init__(
        self,
        *,
        container: builtins.str,
        dynamic_container_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dynamic_filename_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dynamic_path_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        filename: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#container DataFactoryDatasetBinary#container}.
        :param dynamic_container_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_container_enabled DataFactoryDatasetBinary#dynamic_container_enabled}.
        :param dynamic_filename_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_filename_enabled DataFactoryDatasetBinary#dynamic_filename_enabled}.
        :param dynamic_path_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_path_enabled DataFactoryDatasetBinary#dynamic_path_enabled}.
        :param filename: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#filename DataFactoryDatasetBinary#filename}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#path DataFactoryDatasetBinary#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryDatasetBinaryAzureBlobStorageLocation.__init__)
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument dynamic_container_enabled", value=dynamic_container_enabled, expected_type=type_hints["dynamic_container_enabled"])
            check_type(argname="argument dynamic_filename_enabled", value=dynamic_filename_enabled, expected_type=type_hints["dynamic_filename_enabled"])
            check_type(argname="argument dynamic_path_enabled", value=dynamic_path_enabled, expected_type=type_hints["dynamic_path_enabled"])
            check_type(argname="argument filename", value=filename, expected_type=type_hints["filename"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "container": container,
        }
        if dynamic_container_enabled is not None:
            self._values["dynamic_container_enabled"] = dynamic_container_enabled
        if dynamic_filename_enabled is not None:
            self._values["dynamic_filename_enabled"] = dynamic_filename_enabled
        if dynamic_path_enabled is not None:
            self._values["dynamic_path_enabled"] = dynamic_path_enabled
        if filename is not None:
            self._values["filename"] = filename
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def container(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#container DataFactoryDatasetBinary#container}.'''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dynamic_container_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_container_enabled DataFactoryDatasetBinary#dynamic_container_enabled}.'''
        result = self._values.get("dynamic_container_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def dynamic_filename_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_filename_enabled DataFactoryDatasetBinary#dynamic_filename_enabled}.'''
        result = self._values.get("dynamic_filename_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def dynamic_path_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_path_enabled DataFactoryDatasetBinary#dynamic_path_enabled}.'''
        result = self._values.get("dynamic_path_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def filename(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#filename DataFactoryDatasetBinary#filename}.'''
        result = self._values.get("filename")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#path DataFactoryDatasetBinary#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryDatasetBinaryAzureBlobStorageLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryDatasetBinaryAzureBlobStorageLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryDatasetBinary.DataFactoryDatasetBinaryAzureBlobStorageLocationOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryDatasetBinaryAzureBlobStorageLocationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDynamicContainerEnabled")
    def reset_dynamic_container_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicContainerEnabled", []))

    @jsii.member(jsii_name="resetDynamicFilenameEnabled")
    def reset_dynamic_filename_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicFilenameEnabled", []))

    @jsii.member(jsii_name="resetDynamicPathEnabled")
    def reset_dynamic_path_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicPathEnabled", []))

    @jsii.member(jsii_name="resetFilename")
    def reset_filename(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilename", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicContainerEnabledInput")
    def dynamic_container_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dynamicContainerEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicFilenameEnabledInput")
    def dynamic_filename_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dynamicFilenameEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicPathEnabledInput")
    def dynamic_path_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dynamicPathEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="filenameInput")
    def filename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filenameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "container"))

    @container.setter
    def container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryAzureBlobStorageLocationOutputReference, "container").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "container", value)

    @builtins.property
    @jsii.member(jsii_name="dynamicContainerEnabled")
    def dynamic_container_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dynamicContainerEnabled"))

    @dynamic_container_enabled.setter
    def dynamic_container_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryAzureBlobStorageLocationOutputReference, "dynamic_container_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamicContainerEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="dynamicFilenameEnabled")
    def dynamic_filename_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dynamicFilenameEnabled"))

    @dynamic_filename_enabled.setter
    def dynamic_filename_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryAzureBlobStorageLocationOutputReference, "dynamic_filename_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamicFilenameEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="dynamicPathEnabled")
    def dynamic_path_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dynamicPathEnabled"))

    @dynamic_path_enabled.setter
    def dynamic_path_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryAzureBlobStorageLocationOutputReference, "dynamic_path_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamicPathEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="filename")
    def filename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filename"))

    @filename.setter
    def filename(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryAzureBlobStorageLocationOutputReference, "filename").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filename", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryAzureBlobStorageLocationOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryDatasetBinaryAzureBlobStorageLocation]:
        return typing.cast(typing.Optional[DataFactoryDatasetBinaryAzureBlobStorageLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryDatasetBinaryAzureBlobStorageLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryAzureBlobStorageLocationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryDatasetBinary.DataFactoryDatasetBinaryCompression",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "level": "level"},
)
class DataFactoryDatasetBinaryCompression:
    def __init__(
        self,
        *,
        type: builtins.str,
        level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#type DataFactoryDatasetBinary#type}.
        :param level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#level DataFactoryDatasetBinary#level}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryDatasetBinaryCompression.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if level is not None:
            self._values["level"] = level

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#type DataFactoryDatasetBinary#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#level DataFactoryDatasetBinary#level}.'''
        result = self._values.get("level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryDatasetBinaryCompression(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryDatasetBinaryCompressionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryDatasetBinary.DataFactoryDatasetBinaryCompressionOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryDatasetBinaryCompressionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLevel")
    def reset_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLevel", []))

    @builtins.property
    @jsii.member(jsii_name="levelInput")
    def level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "levelInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "level"))

    @level.setter
    def level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryCompressionOutputReference, "level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "level", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryCompressionOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataFactoryDatasetBinaryCompression]:
        return typing.cast(typing.Optional[DataFactoryDatasetBinaryCompression], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryDatasetBinaryCompression],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryCompressionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryDatasetBinary.DataFactoryDatasetBinaryConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_factory_id": "dataFactoryId",
        "linked_service_name": "linkedServiceName",
        "name": "name",
        "additional_properties": "additionalProperties",
        "annotations": "annotations",
        "azure_blob_storage_location": "azureBlobStorageLocation",
        "compression": "compression",
        "description": "description",
        "folder": "folder",
        "http_server_location": "httpServerLocation",
        "id": "id",
        "parameters": "parameters",
        "sftp_server_location": "sftpServerLocation",
        "timeouts": "timeouts",
    },
)
class DataFactoryDatasetBinaryConfig(cdktf.TerraformMetaArguments):
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
        data_factory_id: builtins.str,
        linked_service_name: builtins.str,
        name: builtins.str,
        additional_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        annotations: typing.Optional[typing.Sequence[builtins.str]] = None,
        azure_blob_storage_location: typing.Optional[typing.Union[DataFactoryDatasetBinaryAzureBlobStorageLocation, typing.Dict[str, typing.Any]]] = None,
        compression: typing.Optional[typing.Union[DataFactoryDatasetBinaryCompression, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        folder: typing.Optional[builtins.str] = None,
        http_server_location: typing.Optional[typing.Union["DataFactoryDatasetBinaryHttpServerLocation", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        sftp_server_location: typing.Optional[typing.Union["DataFactoryDatasetBinarySftpServerLocation", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["DataFactoryDatasetBinaryTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_factory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#data_factory_id DataFactoryDatasetBinary#data_factory_id}.
        :param linked_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#linked_service_name DataFactoryDatasetBinary#linked_service_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#name DataFactoryDatasetBinary#name}.
        :param additional_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#additional_properties DataFactoryDatasetBinary#additional_properties}.
        :param annotations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#annotations DataFactoryDatasetBinary#annotations}.
        :param azure_blob_storage_location: azure_blob_storage_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#azure_blob_storage_location DataFactoryDatasetBinary#azure_blob_storage_location}
        :param compression: compression block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#compression DataFactoryDatasetBinary#compression}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#description DataFactoryDatasetBinary#description}.
        :param folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#folder DataFactoryDatasetBinary#folder}.
        :param http_server_location: http_server_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#http_server_location DataFactoryDatasetBinary#http_server_location}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#id DataFactoryDatasetBinary#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#parameters DataFactoryDatasetBinary#parameters}.
        :param sftp_server_location: sftp_server_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#sftp_server_location DataFactoryDatasetBinary#sftp_server_location}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#timeouts DataFactoryDatasetBinary#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(azure_blob_storage_location, dict):
            azure_blob_storage_location = DataFactoryDatasetBinaryAzureBlobStorageLocation(**azure_blob_storage_location)
        if isinstance(compression, dict):
            compression = DataFactoryDatasetBinaryCompression(**compression)
        if isinstance(http_server_location, dict):
            http_server_location = DataFactoryDatasetBinaryHttpServerLocation(**http_server_location)
        if isinstance(sftp_server_location, dict):
            sftp_server_location = DataFactoryDatasetBinarySftpServerLocation(**sftp_server_location)
        if isinstance(timeouts, dict):
            timeouts = DataFactoryDatasetBinaryTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryDatasetBinaryConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_factory_id", value=data_factory_id, expected_type=type_hints["data_factory_id"])
            check_type(argname="argument linked_service_name", value=linked_service_name, expected_type=type_hints["linked_service_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument additional_properties", value=additional_properties, expected_type=type_hints["additional_properties"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument azure_blob_storage_location", value=azure_blob_storage_location, expected_type=type_hints["azure_blob_storage_location"])
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument folder", value=folder, expected_type=type_hints["folder"])
            check_type(argname="argument http_server_location", value=http_server_location, expected_type=type_hints["http_server_location"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument sftp_server_location", value=sftp_server_location, expected_type=type_hints["sftp_server_location"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_factory_id": data_factory_id,
            "linked_service_name": linked_service_name,
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
        if additional_properties is not None:
            self._values["additional_properties"] = additional_properties
        if annotations is not None:
            self._values["annotations"] = annotations
        if azure_blob_storage_location is not None:
            self._values["azure_blob_storage_location"] = azure_blob_storage_location
        if compression is not None:
            self._values["compression"] = compression
        if description is not None:
            self._values["description"] = description
        if folder is not None:
            self._values["folder"] = folder
        if http_server_location is not None:
            self._values["http_server_location"] = http_server_location
        if id is not None:
            self._values["id"] = id
        if parameters is not None:
            self._values["parameters"] = parameters
        if sftp_server_location is not None:
            self._values["sftp_server_location"] = sftp_server_location
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
    def data_factory_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#data_factory_id DataFactoryDatasetBinary#data_factory_id}.'''
        result = self._values.get("data_factory_id")
        assert result is not None, "Required property 'data_factory_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def linked_service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#linked_service_name DataFactoryDatasetBinary#linked_service_name}.'''
        result = self._values.get("linked_service_name")
        assert result is not None, "Required property 'linked_service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#name DataFactoryDatasetBinary#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#additional_properties DataFactoryDatasetBinary#additional_properties}.'''
        result = self._values.get("additional_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def annotations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#annotations DataFactoryDatasetBinary#annotations}.'''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def azure_blob_storage_location(
        self,
    ) -> typing.Optional[DataFactoryDatasetBinaryAzureBlobStorageLocation]:
        '''azure_blob_storage_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#azure_blob_storage_location DataFactoryDatasetBinary#azure_blob_storage_location}
        '''
        result = self._values.get("azure_blob_storage_location")
        return typing.cast(typing.Optional[DataFactoryDatasetBinaryAzureBlobStorageLocation], result)

    @builtins.property
    def compression(self) -> typing.Optional[DataFactoryDatasetBinaryCompression]:
        '''compression block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#compression DataFactoryDatasetBinary#compression}
        '''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[DataFactoryDatasetBinaryCompression], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#description DataFactoryDatasetBinary#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def folder(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#folder DataFactoryDatasetBinary#folder}.'''
        result = self._values.get("folder")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_server_location(
        self,
    ) -> typing.Optional["DataFactoryDatasetBinaryHttpServerLocation"]:
        '''http_server_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#http_server_location DataFactoryDatasetBinary#http_server_location}
        '''
        result = self._values.get("http_server_location")
        return typing.cast(typing.Optional["DataFactoryDatasetBinaryHttpServerLocation"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#id DataFactoryDatasetBinary#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#parameters DataFactoryDatasetBinary#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def sftp_server_location(
        self,
    ) -> typing.Optional["DataFactoryDatasetBinarySftpServerLocation"]:
        '''sftp_server_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#sftp_server_location DataFactoryDatasetBinary#sftp_server_location}
        '''
        result = self._values.get("sftp_server_location")
        return typing.cast(typing.Optional["DataFactoryDatasetBinarySftpServerLocation"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataFactoryDatasetBinaryTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#timeouts DataFactoryDatasetBinary#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataFactoryDatasetBinaryTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryDatasetBinaryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryDatasetBinary.DataFactoryDatasetBinaryHttpServerLocation",
    jsii_struct_bases=[],
    name_mapping={
        "filename": "filename",
        "path": "path",
        "relative_url": "relativeUrl",
        "dynamic_filename_enabled": "dynamicFilenameEnabled",
        "dynamic_path_enabled": "dynamicPathEnabled",
    },
)
class DataFactoryDatasetBinaryHttpServerLocation:
    def __init__(
        self,
        *,
        filename: builtins.str,
        path: builtins.str,
        relative_url: builtins.str,
        dynamic_filename_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dynamic_path_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param filename: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#filename DataFactoryDatasetBinary#filename}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#path DataFactoryDatasetBinary#path}.
        :param relative_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#relative_url DataFactoryDatasetBinary#relative_url}.
        :param dynamic_filename_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_filename_enabled DataFactoryDatasetBinary#dynamic_filename_enabled}.
        :param dynamic_path_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_path_enabled DataFactoryDatasetBinary#dynamic_path_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryDatasetBinaryHttpServerLocation.__init__)
            check_type(argname="argument filename", value=filename, expected_type=type_hints["filename"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument relative_url", value=relative_url, expected_type=type_hints["relative_url"])
            check_type(argname="argument dynamic_filename_enabled", value=dynamic_filename_enabled, expected_type=type_hints["dynamic_filename_enabled"])
            check_type(argname="argument dynamic_path_enabled", value=dynamic_path_enabled, expected_type=type_hints["dynamic_path_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "filename": filename,
            "path": path,
            "relative_url": relative_url,
        }
        if dynamic_filename_enabled is not None:
            self._values["dynamic_filename_enabled"] = dynamic_filename_enabled
        if dynamic_path_enabled is not None:
            self._values["dynamic_path_enabled"] = dynamic_path_enabled

    @builtins.property
    def filename(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#filename DataFactoryDatasetBinary#filename}.'''
        result = self._values.get("filename")
        assert result is not None, "Required property 'filename' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#path DataFactoryDatasetBinary#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relative_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#relative_url DataFactoryDatasetBinary#relative_url}.'''
        result = self._values.get("relative_url")
        assert result is not None, "Required property 'relative_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dynamic_filename_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_filename_enabled DataFactoryDatasetBinary#dynamic_filename_enabled}.'''
        result = self._values.get("dynamic_filename_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def dynamic_path_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_path_enabled DataFactoryDatasetBinary#dynamic_path_enabled}.'''
        result = self._values.get("dynamic_path_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryDatasetBinaryHttpServerLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryDatasetBinaryHttpServerLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryDatasetBinary.DataFactoryDatasetBinaryHttpServerLocationOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryDatasetBinaryHttpServerLocationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDynamicFilenameEnabled")
    def reset_dynamic_filename_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicFilenameEnabled", []))

    @jsii.member(jsii_name="resetDynamicPathEnabled")
    def reset_dynamic_path_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicPathEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="dynamicFilenameEnabledInput")
    def dynamic_filename_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dynamicFilenameEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicPathEnabledInput")
    def dynamic_path_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dynamicPathEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="filenameInput")
    def filename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filenameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="relativeUrlInput")
    def relative_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "relativeUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicFilenameEnabled")
    def dynamic_filename_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dynamicFilenameEnabled"))

    @dynamic_filename_enabled.setter
    def dynamic_filename_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryHttpServerLocationOutputReference, "dynamic_filename_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamicFilenameEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="dynamicPathEnabled")
    def dynamic_path_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dynamicPathEnabled"))

    @dynamic_path_enabled.setter
    def dynamic_path_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryHttpServerLocationOutputReference, "dynamic_path_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamicPathEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="filename")
    def filename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filename"))

    @filename.setter
    def filename(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryHttpServerLocationOutputReference, "filename").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filename", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryHttpServerLocationOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="relativeUrl")
    def relative_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relativeUrl"))

    @relative_url.setter
    def relative_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryHttpServerLocationOutputReference, "relative_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relativeUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryDatasetBinaryHttpServerLocation]:
        return typing.cast(typing.Optional[DataFactoryDatasetBinaryHttpServerLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryDatasetBinaryHttpServerLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryHttpServerLocationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryDatasetBinary.DataFactoryDatasetBinarySftpServerLocation",
    jsii_struct_bases=[],
    name_mapping={
        "filename": "filename",
        "path": "path",
        "dynamic_filename_enabled": "dynamicFilenameEnabled",
        "dynamic_path_enabled": "dynamicPathEnabled",
    },
)
class DataFactoryDatasetBinarySftpServerLocation:
    def __init__(
        self,
        *,
        filename: builtins.str,
        path: builtins.str,
        dynamic_filename_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dynamic_path_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param filename: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#filename DataFactoryDatasetBinary#filename}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#path DataFactoryDatasetBinary#path}.
        :param dynamic_filename_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_filename_enabled DataFactoryDatasetBinary#dynamic_filename_enabled}.
        :param dynamic_path_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_path_enabled DataFactoryDatasetBinary#dynamic_path_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryDatasetBinarySftpServerLocation.__init__)
            check_type(argname="argument filename", value=filename, expected_type=type_hints["filename"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument dynamic_filename_enabled", value=dynamic_filename_enabled, expected_type=type_hints["dynamic_filename_enabled"])
            check_type(argname="argument dynamic_path_enabled", value=dynamic_path_enabled, expected_type=type_hints["dynamic_path_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "filename": filename,
            "path": path,
        }
        if dynamic_filename_enabled is not None:
            self._values["dynamic_filename_enabled"] = dynamic_filename_enabled
        if dynamic_path_enabled is not None:
            self._values["dynamic_path_enabled"] = dynamic_path_enabled

    @builtins.property
    def filename(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#filename DataFactoryDatasetBinary#filename}.'''
        result = self._values.get("filename")
        assert result is not None, "Required property 'filename' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#path DataFactoryDatasetBinary#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dynamic_filename_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_filename_enabled DataFactoryDatasetBinary#dynamic_filename_enabled}.'''
        result = self._values.get("dynamic_filename_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def dynamic_path_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#dynamic_path_enabled DataFactoryDatasetBinary#dynamic_path_enabled}.'''
        result = self._values.get("dynamic_path_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryDatasetBinarySftpServerLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryDatasetBinarySftpServerLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryDatasetBinary.DataFactoryDatasetBinarySftpServerLocationOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryDatasetBinarySftpServerLocationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDynamicFilenameEnabled")
    def reset_dynamic_filename_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicFilenameEnabled", []))

    @jsii.member(jsii_name="resetDynamicPathEnabled")
    def reset_dynamic_path_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicPathEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="dynamicFilenameEnabledInput")
    def dynamic_filename_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dynamicFilenameEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicPathEnabledInput")
    def dynamic_path_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dynamicPathEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="filenameInput")
    def filename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filenameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicFilenameEnabled")
    def dynamic_filename_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dynamicFilenameEnabled"))

    @dynamic_filename_enabled.setter
    def dynamic_filename_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinarySftpServerLocationOutputReference, "dynamic_filename_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamicFilenameEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="dynamicPathEnabled")
    def dynamic_path_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dynamicPathEnabled"))

    @dynamic_path_enabled.setter
    def dynamic_path_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinarySftpServerLocationOutputReference, "dynamic_path_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamicPathEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="filename")
    def filename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filename"))

    @filename.setter
    def filename(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinarySftpServerLocationOutputReference, "filename").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filename", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinarySftpServerLocationOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryDatasetBinarySftpServerLocation]:
        return typing.cast(typing.Optional[DataFactoryDatasetBinarySftpServerLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryDatasetBinarySftpServerLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinarySftpServerLocationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryDatasetBinary.DataFactoryDatasetBinaryTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class DataFactoryDatasetBinaryTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#create DataFactoryDatasetBinary#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#delete DataFactoryDatasetBinary#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#read DataFactoryDatasetBinary#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#update DataFactoryDatasetBinary#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryDatasetBinaryTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#create DataFactoryDatasetBinary#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#delete DataFactoryDatasetBinary#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#read DataFactoryDatasetBinary#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_dataset_binary#update DataFactoryDatasetBinary#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryDatasetBinaryTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryDatasetBinaryTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryDatasetBinary.DataFactoryDatasetBinaryTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryDatasetBinaryTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataFactoryDatasetBinaryTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataFactoryDatasetBinaryTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataFactoryDatasetBinaryTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryDatasetBinaryTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataFactoryDatasetBinary",
    "DataFactoryDatasetBinaryAzureBlobStorageLocation",
    "DataFactoryDatasetBinaryAzureBlobStorageLocationOutputReference",
    "DataFactoryDatasetBinaryCompression",
    "DataFactoryDatasetBinaryCompressionOutputReference",
    "DataFactoryDatasetBinaryConfig",
    "DataFactoryDatasetBinaryHttpServerLocation",
    "DataFactoryDatasetBinaryHttpServerLocationOutputReference",
    "DataFactoryDatasetBinarySftpServerLocation",
    "DataFactoryDatasetBinarySftpServerLocationOutputReference",
    "DataFactoryDatasetBinaryTimeouts",
    "DataFactoryDatasetBinaryTimeoutsOutputReference",
]

publication.publish()
