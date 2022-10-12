'''
# `data_google_storage_object_signed_url`

Refer to the Terraform Registory for docs: [`data_google_storage_object_signed_url`](https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url).
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


class DataGoogleStorageObjectSignedUrl(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleStorageObjectSignedUrl.DataGoogleStorageObjectSignedUrl",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url google_storage_object_signed_url}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        bucket: builtins.str,
        path: builtins.str,
        content_md5: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[builtins.str] = None,
        duration: typing.Optional[builtins.str] = None,
        extension_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        http_method: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url google_storage_object_signed_url} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#bucket DataGoogleStorageObjectSignedUrl#bucket}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#path DataGoogleStorageObjectSignedUrl#path}.
        :param content_md5: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#content_md5 DataGoogleStorageObjectSignedUrl#content_md5}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#content_type DataGoogleStorageObjectSignedUrl#content_type}.
        :param credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#credentials DataGoogleStorageObjectSignedUrl#credentials}.
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#duration DataGoogleStorageObjectSignedUrl#duration}.
        :param extension_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#extension_headers DataGoogleStorageObjectSignedUrl#extension_headers}.
        :param http_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#http_method DataGoogleStorageObjectSignedUrl#http_method}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#id DataGoogleStorageObjectSignedUrl#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleStorageObjectSignedUrl.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataGoogleStorageObjectSignedUrlConfig(
            bucket=bucket,
            path=path,
            content_md5=content_md5,
            content_type=content_type,
            credentials=credentials,
            duration=duration,
            extension_headers=extension_headers,
            http_method=http_method,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetContentMd5")
    def reset_content_md5(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentMd5", []))

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetCredentials")
    def reset_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentials", []))

    @jsii.member(jsii_name="resetDuration")
    def reset_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuration", []))

    @jsii.member(jsii_name="resetExtensionHeaders")
    def reset_extension_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtensionHeaders", []))

    @jsii.member(jsii_name="resetHttpMethod")
    def reset_http_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpMethod", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="signedUrl")
    def signed_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signedUrl"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="contentMd5Input")
    def content_md5_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentMd5Input"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="extensionHeadersInput")
    def extension_headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "extensionHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="httpMethodInput")
    def http_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleStorageObjectSignedUrl, "bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="contentMd5")
    def content_md5(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentMd5"))

    @content_md5.setter
    def content_md5(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleStorageObjectSignedUrl, "content_md5").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentMd5", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleStorageObjectSignedUrl, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentials"))

    @credentials.setter
    def credentials(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleStorageObjectSignedUrl, "credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentials", value)

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleStorageObjectSignedUrl, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="extensionHeaders")
    def extension_headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "extensionHeaders"))

    @extension_headers.setter
    def extension_headers(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleStorageObjectSignedUrl, "extension_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extensionHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="httpMethod")
    def http_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpMethod"))

    @http_method.setter
    def http_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleStorageObjectSignedUrl, "http_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpMethod", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleStorageObjectSignedUrl, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleStorageObjectSignedUrl, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleStorageObjectSignedUrl.DataGoogleStorageObjectSignedUrlConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "bucket": "bucket",
        "path": "path",
        "content_md5": "contentMd5",
        "content_type": "contentType",
        "credentials": "credentials",
        "duration": "duration",
        "extension_headers": "extensionHeaders",
        "http_method": "httpMethod",
        "id": "id",
    },
)
class DataGoogleStorageObjectSignedUrlConfig(cdktf.TerraformMetaArguments):
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
        bucket: builtins.str,
        path: builtins.str,
        content_md5: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[builtins.str] = None,
        duration: typing.Optional[builtins.str] = None,
        extension_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        http_method: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#bucket DataGoogleStorageObjectSignedUrl#bucket}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#path DataGoogleStorageObjectSignedUrl#path}.
        :param content_md5: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#content_md5 DataGoogleStorageObjectSignedUrl#content_md5}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#content_type DataGoogleStorageObjectSignedUrl#content_type}.
        :param credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#credentials DataGoogleStorageObjectSignedUrl#credentials}.
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#duration DataGoogleStorageObjectSignedUrl#duration}.
        :param extension_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#extension_headers DataGoogleStorageObjectSignedUrl#extension_headers}.
        :param http_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#http_method DataGoogleStorageObjectSignedUrl#http_method}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#id DataGoogleStorageObjectSignedUrl#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleStorageObjectSignedUrlConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument content_md5", value=content_md5, expected_type=type_hints["content_md5"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument extension_headers", value=extension_headers, expected_type=type_hints["extension_headers"])
            check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "path": path,
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
        if content_md5 is not None:
            self._values["content_md5"] = content_md5
        if content_type is not None:
            self._values["content_type"] = content_type
        if credentials is not None:
            self._values["credentials"] = credentials
        if duration is not None:
            self._values["duration"] = duration
        if extension_headers is not None:
            self._values["extension_headers"] = extension_headers
        if http_method is not None:
            self._values["http_method"] = http_method
        if id is not None:
            self._values["id"] = id

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
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#bucket DataGoogleStorageObjectSignedUrl#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#path DataGoogleStorageObjectSignedUrl#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_md5(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#content_md5 DataGoogleStorageObjectSignedUrl#content_md5}.'''
        result = self._values.get("content_md5")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#content_type DataGoogleStorageObjectSignedUrl#content_type}.'''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credentials(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#credentials DataGoogleStorageObjectSignedUrl#credentials}.'''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def duration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#duration DataGoogleStorageObjectSignedUrl#duration}.'''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extension_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#extension_headers DataGoogleStorageObjectSignedUrl#extension_headers}.'''
        result = self._values.get("extension_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def http_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#http_method DataGoogleStorageObjectSignedUrl#http_method}.'''
        result = self._values.get("http_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_storage_object_signed_url#id DataGoogleStorageObjectSignedUrl#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleStorageObjectSignedUrlConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataGoogleStorageObjectSignedUrl",
    "DataGoogleStorageObjectSignedUrlConfig",
]

publication.publish()
