'''
# `vsphere_file`

Refer to the Terraform Registory for docs: [`vsphere_file`](https://www.terraform.io/docs/providers/vsphere/r/file).
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


class File(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.file.File",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vsphere/r/file vsphere_file}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        datastore: builtins.str,
        destination_file: builtins.str,
        source_file: builtins.str,
        create_directories: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        datacenter: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        source_datacenter: typing.Optional[builtins.str] = None,
        source_datastore: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vsphere/r/file vsphere_file} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param datastore: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#datastore File#datastore}.
        :param destination_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#destination_file File#destination_file}.
        :param source_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#source_file File#source_file}.
        :param create_directories: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#create_directories File#create_directories}.
        :param datacenter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#datacenter File#datacenter}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#id File#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param source_datacenter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#source_datacenter File#source_datacenter}.
        :param source_datastore: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#source_datastore File#source_datastore}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(File.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = FileConfig(
            datastore=datastore,
            destination_file=destination_file,
            source_file=source_file,
            create_directories=create_directories,
            datacenter=datacenter,
            id=id,
            source_datacenter=source_datacenter,
            source_datastore=source_datastore,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCreateDirectories")
    def reset_create_directories(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateDirectories", []))

    @jsii.member(jsii_name="resetDatacenter")
    def reset_datacenter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatacenter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSourceDatacenter")
    def reset_source_datacenter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDatacenter", []))

    @jsii.member(jsii_name="resetSourceDatastore")
    def reset_source_datastore(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDatastore", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createDirectoriesInput")
    def create_directories_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "createDirectoriesInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterInput")
    def datacenter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterInput"))

    @builtins.property
    @jsii.member(jsii_name="datastoreInput")
    def datastore_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datastoreInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationFileInput")
    def destination_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationFileInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDatacenterInput")
    def source_datacenter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDatacenterInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDatastoreInput")
    def source_datastore_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDatastoreInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileInput")
    def source_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileInput"))

    @builtins.property
    @jsii.member(jsii_name="createDirectories")
    def create_directories(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "createDirectories"))

    @create_directories.setter
    def create_directories(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(File, "create_directories").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createDirectories", value)

    @builtins.property
    @jsii.member(jsii_name="datacenter")
    def datacenter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenter"))

    @datacenter.setter
    def datacenter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(File, "datacenter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenter", value)

    @builtins.property
    @jsii.member(jsii_name="datastore")
    def datastore(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datastore"))

    @datastore.setter
    def datastore(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(File, "datastore").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datastore", value)

    @builtins.property
    @jsii.member(jsii_name="destinationFile")
    def destination_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationFile"))

    @destination_file.setter
    def destination_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(File, "destination_file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationFile", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(File, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDatacenter")
    def source_datacenter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDatacenter"))

    @source_datacenter.setter
    def source_datacenter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(File, "source_datacenter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDatacenter", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDatastore")
    def source_datastore(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDatastore"))

    @source_datastore.setter
    def source_datastore(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(File, "source_datastore").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDatastore", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFile")
    def source_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFile"))

    @source_file.setter
    def source_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(File, "source_file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFile", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.file.FileConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "datastore": "datastore",
        "destination_file": "destinationFile",
        "source_file": "sourceFile",
        "create_directories": "createDirectories",
        "datacenter": "datacenter",
        "id": "id",
        "source_datacenter": "sourceDatacenter",
        "source_datastore": "sourceDatastore",
    },
)
class FileConfig(cdktf.TerraformMetaArguments):
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
        datastore: builtins.str,
        destination_file: builtins.str,
        source_file: builtins.str,
        create_directories: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        datacenter: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        source_datacenter: typing.Optional[builtins.str] = None,
        source_datastore: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param datastore: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#datastore File#datastore}.
        :param destination_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#destination_file File#destination_file}.
        :param source_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#source_file File#source_file}.
        :param create_directories: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#create_directories File#create_directories}.
        :param datacenter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#datacenter File#datacenter}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#id File#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param source_datacenter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#source_datacenter File#source_datacenter}.
        :param source_datastore: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#source_datastore File#source_datastore}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(FileConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument datastore", value=datastore, expected_type=type_hints["datastore"])
            check_type(argname="argument destination_file", value=destination_file, expected_type=type_hints["destination_file"])
            check_type(argname="argument source_file", value=source_file, expected_type=type_hints["source_file"])
            check_type(argname="argument create_directories", value=create_directories, expected_type=type_hints["create_directories"])
            check_type(argname="argument datacenter", value=datacenter, expected_type=type_hints["datacenter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument source_datacenter", value=source_datacenter, expected_type=type_hints["source_datacenter"])
            check_type(argname="argument source_datastore", value=source_datastore, expected_type=type_hints["source_datastore"])
        self._values: typing.Dict[str, typing.Any] = {
            "datastore": datastore,
            "destination_file": destination_file,
            "source_file": source_file,
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
        if create_directories is not None:
            self._values["create_directories"] = create_directories
        if datacenter is not None:
            self._values["datacenter"] = datacenter
        if id is not None:
            self._values["id"] = id
        if source_datacenter is not None:
            self._values["source_datacenter"] = source_datacenter
        if source_datastore is not None:
            self._values["source_datastore"] = source_datastore

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
    def datastore(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#datastore File#datastore}.'''
        result = self._values.get("datastore")
        assert result is not None, "Required property 'datastore' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_file(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#destination_file File#destination_file}.'''
        result = self._values.get("destination_file")
        assert result is not None, "Required property 'destination_file' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_file(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#source_file File#source_file}.'''
        result = self._values.get("source_file")
        assert result is not None, "Required property 'source_file' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def create_directories(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#create_directories File#create_directories}.'''
        result = self._values.get("create_directories")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def datacenter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#datacenter File#datacenter}.'''
        result = self._values.get("datacenter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#id File#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_datacenter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#source_datacenter File#source_datacenter}.'''
        result = self._values.get("source_datacenter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_datastore(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/file#source_datastore File#source_datastore}.'''
        result = self._values.get("source_datastore")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "File",
    "FileConfig",
]

publication.publish()
