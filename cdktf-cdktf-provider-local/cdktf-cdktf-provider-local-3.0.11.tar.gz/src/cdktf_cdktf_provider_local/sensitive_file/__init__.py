'''
# `local_sensitive_file`

Refer to the Terraform Registory for docs: [`local_sensitive_file`](https://www.terraform.io/docs/providers/local/r/sensitive_file).
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


class SensitiveFile(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-local.sensitiveFile.SensitiveFile",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/local/r/sensitive_file local_sensitive_file}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        filename: builtins.str,
        content: typing.Optional[builtins.str] = None,
        content_base64: typing.Optional[builtins.str] = None,
        directory_permission: typing.Optional[builtins.str] = None,
        file_permission: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/local/r/sensitive_file local_sensitive_file} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param filename: The path to the file that will be created. Missing parent directories will be created. If the file already exists, it will be overridden with the given content. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#filename SensitiveFile#filename}
        :param content: Sensitive content to store in the file, expected to be an UTF-8 encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#content SensitiveFile#content}
        :param content_base64: Sensitive content to store in the file, expected to be binary encoded as base64 string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#content_base64 SensitiveFile#content_base64}
        :param directory_permission: Permissions to set for directories created (in numeric notation). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#directory_permission SensitiveFile#directory_permission}
        :param file_permission: Permissions to set for the output file (in numeric notation). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#file_permission SensitiveFile#file_permission}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#id SensitiveFile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param source: Path to file to use as source for the one we are creating. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#source SensitiveFile#source}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SensitiveFile.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SensitiveFileConfig(
            filename=filename,
            content=content,
            content_base64=content_base64,
            directory_permission=directory_permission,
            file_permission=file_permission,
            id=id,
            source=source,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetContentBase64")
    def reset_content_base64(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentBase64", []))

    @jsii.member(jsii_name="resetDirectoryPermission")
    def reset_directory_permission(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectoryPermission", []))

    @jsii.member(jsii_name="resetFilePermission")
    def reset_file_permission(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilePermission", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="contentBase64Input")
    def content_base64_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentBase64Input"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryPermissionInput")
    def directory_permission_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryPermissionInput"))

    @builtins.property
    @jsii.member(jsii_name="filenameInput")
    def filename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filenameInput"))

    @builtins.property
    @jsii.member(jsii_name="filePermissionInput")
    def file_permission_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filePermissionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SensitiveFile, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentBase64")
    def content_base64(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentBase64"))

    @content_base64.setter
    def content_base64(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SensitiveFile, "content_base64").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentBase64", value)

    @builtins.property
    @jsii.member(jsii_name="directoryPermission")
    def directory_permission(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryPermission"))

    @directory_permission.setter
    def directory_permission(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SensitiveFile, "directory_permission").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryPermission", value)

    @builtins.property
    @jsii.member(jsii_name="filename")
    def filename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filename"))

    @filename.setter
    def filename(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SensitiveFile, "filename").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filename", value)

    @builtins.property
    @jsii.member(jsii_name="filePermission")
    def file_permission(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filePermission"))

    @file_permission.setter
    def file_permission(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SensitiveFile, "file_permission").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filePermission", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SensitiveFile, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SensitiveFile, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-local.sensitiveFile.SensitiveFileConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "filename": "filename",
        "content": "content",
        "content_base64": "contentBase64",
        "directory_permission": "directoryPermission",
        "file_permission": "filePermission",
        "id": "id",
        "source": "source",
    },
)
class SensitiveFileConfig(cdktf.TerraformMetaArguments):
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
        filename: builtins.str,
        content: typing.Optional[builtins.str] = None,
        content_base64: typing.Optional[builtins.str] = None,
        directory_permission: typing.Optional[builtins.str] = None,
        file_permission: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param filename: The path to the file that will be created. Missing parent directories will be created. If the file already exists, it will be overridden with the given content. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#filename SensitiveFile#filename}
        :param content: Sensitive content to store in the file, expected to be an UTF-8 encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#content SensitiveFile#content}
        :param content_base64: Sensitive content to store in the file, expected to be binary encoded as base64 string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#content_base64 SensitiveFile#content_base64}
        :param directory_permission: Permissions to set for directories created (in numeric notation). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#directory_permission SensitiveFile#directory_permission}
        :param file_permission: Permissions to set for the output file (in numeric notation). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#file_permission SensitiveFile#file_permission}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#id SensitiveFile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param source: Path to file to use as source for the one we are creating. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#source SensitiveFile#source}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(SensitiveFileConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument filename", value=filename, expected_type=type_hints["filename"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_base64", value=content_base64, expected_type=type_hints["content_base64"])
            check_type(argname="argument directory_permission", value=directory_permission, expected_type=type_hints["directory_permission"])
            check_type(argname="argument file_permission", value=file_permission, expected_type=type_hints["file_permission"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[str, typing.Any] = {
            "filename": filename,
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
        if content is not None:
            self._values["content"] = content
        if content_base64 is not None:
            self._values["content_base64"] = content_base64
        if directory_permission is not None:
            self._values["directory_permission"] = directory_permission
        if file_permission is not None:
            self._values["file_permission"] = file_permission
        if id is not None:
            self._values["id"] = id
        if source is not None:
            self._values["source"] = source

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
    def filename(self) -> builtins.str:
        '''The path to the file that will be created.

        Missing parent directories will be created.
        If the file already exists, it will be overridden with the given content.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#filename SensitiveFile#filename}
        '''
        result = self._values.get("filename")
        assert result is not None, "Required property 'filename' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''Sensitive content to store in the file, expected to be an UTF-8 encoded string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#content SensitiveFile#content}
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_base64(self) -> typing.Optional[builtins.str]:
        '''Sensitive content to store in the file, expected to be binary encoded as base64 string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#content_base64 SensitiveFile#content_base64}
        '''
        result = self._values.get("content_base64")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory_permission(self) -> typing.Optional[builtins.str]:
        '''Permissions to set for directories created (in numeric notation).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#directory_permission SensitiveFile#directory_permission}
        '''
        result = self._values.get("directory_permission")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_permission(self) -> typing.Optional[builtins.str]:
        '''Permissions to set for the output file (in numeric notation).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#file_permission SensitiveFile#file_permission}
        '''
        result = self._values.get("file_permission")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#id SensitiveFile#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Path to file to use as source for the one we are creating.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/sensitive_file#source SensitiveFile#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SensitiveFileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SensitiveFile",
    "SensitiveFileConfig",
]

publication.publish()
