'''
# `datadog_logs_archive`

Refer to the Terraform Registory for docs: [`datadog_logs_archive`](https://www.terraform.io/docs/providers/datadog/r/logs_archive).
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


class LogsArchive(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsArchive.LogsArchive",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive datadog_logs_archive}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        query: builtins.str,
        azure_archive: typing.Optional[typing.Union["LogsArchiveAzureArchive", typing.Dict[str, typing.Any]]] = None,
        gcs_archive: typing.Optional[typing.Union["LogsArchiveGcsArchive", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        include_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rehydration_max_scan_size_in_gb: typing.Optional[jsii.Number] = None,
        rehydration_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        s3_archive: typing.Optional[typing.Union["LogsArchiveS3Archive", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive datadog_logs_archive} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Your archive name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#name LogsArchive#name}
        :param query: The archive query/filter. Logs matching this query are included in the archive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#query LogsArchive#query}
        :param azure_archive: azure_archive block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#azure_archive LogsArchive#azure_archive}
        :param gcs_archive: gcs_archive block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#gcs_archive LogsArchive#gcs_archive}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#id LogsArchive#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param include_tags: To store the tags in the archive, set the value ``true``. If it is set to ``false``, the tags will be dropped when the logs are sent to the archive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#include_tags LogsArchive#include_tags}
        :param rehydration_max_scan_size_in_gb: To limit the rehydration scan size for the archive, set a value in GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#rehydration_max_scan_size_in_gb LogsArchive#rehydration_max_scan_size_in_gb}
        :param rehydration_tags: An array of tags to add to rehydrated logs from an archive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#rehydration_tags LogsArchive#rehydration_tags}
        :param s3_archive: s3_archive block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#s3_archive LogsArchive#s3_archive}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsArchive.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LogsArchiveConfig(
            name=name,
            query=query,
            azure_archive=azure_archive,
            gcs_archive=gcs_archive,
            id=id,
            include_tags=include_tags,
            rehydration_max_scan_size_in_gb=rehydration_max_scan_size_in_gb,
            rehydration_tags=rehydration_tags,
            s3_archive=s3_archive,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAzureArchive")
    def put_azure_archive(
        self,
        *,
        client_id: builtins.str,
        container: builtins.str,
        storage_account: builtins.str,
        tenant_id: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Your client id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#client_id LogsArchive#client_id}
        :param container: The container where the archive will be stored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#container LogsArchive#container}
        :param storage_account: The associated storage account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#storage_account LogsArchive#storage_account}
        :param tenant_id: Your tenant id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#tenant_id LogsArchive#tenant_id}
        :param path: The path where the archive will be stored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#path LogsArchive#path}
        '''
        value = LogsArchiveAzureArchive(
            client_id=client_id,
            container=container,
            storage_account=storage_account,
            tenant_id=tenant_id,
            path=path,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureArchive", [value]))

    @jsii.member(jsii_name="putGcsArchive")
    def put_gcs_archive(
        self,
        *,
        bucket: builtins.str,
        client_email: builtins.str,
        path: builtins.str,
        project_id: builtins.str,
    ) -> None:
        '''
        :param bucket: Name of your GCS bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#bucket LogsArchive#bucket}
        :param client_email: Your client email. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#client_email LogsArchive#client_email}
        :param path: Path where the archive will be stored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#path LogsArchive#path}
        :param project_id: Your project id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#project_id LogsArchive#project_id}
        '''
        value = LogsArchiveGcsArchive(
            bucket=bucket, client_email=client_email, path=path, project_id=project_id
        )

        return typing.cast(None, jsii.invoke(self, "putGcsArchive", [value]))

    @jsii.member(jsii_name="putS3Archive")
    def put_s3_archive(
        self,
        *,
        account_id: builtins.str,
        bucket: builtins.str,
        path: builtins.str,
        role_name: builtins.str,
    ) -> None:
        '''
        :param account_id: Your AWS account id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#account_id LogsArchive#account_id}
        :param bucket: Name of your s3 bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#bucket LogsArchive#bucket}
        :param path: Path where the archive will be stored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#path LogsArchive#path}
        :param role_name: Your AWS role name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#role_name LogsArchive#role_name}
        '''
        value = LogsArchiveS3Archive(
            account_id=account_id, bucket=bucket, path=path, role_name=role_name
        )

        return typing.cast(None, jsii.invoke(self, "putS3Archive", [value]))

    @jsii.member(jsii_name="resetAzureArchive")
    def reset_azure_archive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureArchive", []))

    @jsii.member(jsii_name="resetGcsArchive")
    def reset_gcs_archive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcsArchive", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIncludeTags")
    def reset_include_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeTags", []))

    @jsii.member(jsii_name="resetRehydrationMaxScanSizeInGb")
    def reset_rehydration_max_scan_size_in_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRehydrationMaxScanSizeInGb", []))

    @jsii.member(jsii_name="resetRehydrationTags")
    def reset_rehydration_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRehydrationTags", []))

    @jsii.member(jsii_name="resetS3Archive")
    def reset_s3_archive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Archive", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="azureArchive")
    def azure_archive(self) -> "LogsArchiveAzureArchiveOutputReference":
        return typing.cast("LogsArchiveAzureArchiveOutputReference", jsii.get(self, "azureArchive"))

    @builtins.property
    @jsii.member(jsii_name="gcsArchive")
    def gcs_archive(self) -> "LogsArchiveGcsArchiveOutputReference":
        return typing.cast("LogsArchiveGcsArchiveOutputReference", jsii.get(self, "gcsArchive"))

    @builtins.property
    @jsii.member(jsii_name="s3Archive")
    def s3_archive(self) -> "LogsArchiveS3ArchiveOutputReference":
        return typing.cast("LogsArchiveS3ArchiveOutputReference", jsii.get(self, "s3Archive"))

    @builtins.property
    @jsii.member(jsii_name="azureArchiveInput")
    def azure_archive_input(self) -> typing.Optional["LogsArchiveAzureArchive"]:
        return typing.cast(typing.Optional["LogsArchiveAzureArchive"], jsii.get(self, "azureArchiveInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsArchiveInput")
    def gcs_archive_input(self) -> typing.Optional["LogsArchiveGcsArchive"]:
        return typing.cast(typing.Optional["LogsArchiveGcsArchive"], jsii.get(self, "gcsArchiveInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="includeTagsInput")
    def include_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="rehydrationMaxScanSizeInGbInput")
    def rehydration_max_scan_size_in_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rehydrationMaxScanSizeInGbInput"))

    @builtins.property
    @jsii.member(jsii_name="rehydrationTagsInput")
    def rehydration_tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rehydrationTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3ArchiveInput")
    def s3_archive_input(self) -> typing.Optional["LogsArchiveS3Archive"]:
        return typing.cast(typing.Optional["LogsArchiveS3Archive"], jsii.get(self, "s3ArchiveInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchive, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="includeTags")
    def include_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeTags"))

    @include_tags.setter
    def include_tags(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchive, "include_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeTags", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchive, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchive, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="rehydrationMaxScanSizeInGb")
    def rehydration_max_scan_size_in_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rehydrationMaxScanSizeInGb"))

    @rehydration_max_scan_size_in_gb.setter
    def rehydration_max_scan_size_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchive, "rehydration_max_scan_size_in_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rehydrationMaxScanSizeInGb", value)

    @builtins.property
    @jsii.member(jsii_name="rehydrationTags")
    def rehydration_tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rehydrationTags"))

    @rehydration_tags.setter
    def rehydration_tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchive, "rehydration_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rehydrationTags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsArchive.LogsArchiveAzureArchive",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "container": "container",
        "storage_account": "storageAccount",
        "tenant_id": "tenantId",
        "path": "path",
    },
)
class LogsArchiveAzureArchive:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        container: builtins.str,
        storage_account: builtins.str,
        tenant_id: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Your client id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#client_id LogsArchive#client_id}
        :param container: The container where the archive will be stored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#container LogsArchive#container}
        :param storage_account: The associated storage account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#storage_account LogsArchive#storage_account}
        :param tenant_id: Your tenant id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#tenant_id LogsArchive#tenant_id}
        :param path: The path where the archive will be stored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#path LogsArchive#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsArchiveAzureArchive.__init__)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument storage_account", value=storage_account, expected_type=type_hints["storage_account"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
            "container": container,
            "storage_account": storage_account,
            "tenant_id": tenant_id,
        }
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Your client id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#client_id LogsArchive#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container(self) -> builtins.str:
        '''The container where the archive will be stored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#container LogsArchive#container}
        '''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account(self) -> builtins.str:
        '''The associated storage account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#storage_account LogsArchive#storage_account}
        '''
        result = self._values.get("storage_account")
        assert result is not None, "Required property 'storage_account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenant_id(self) -> builtins.str:
        '''Your tenant id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#tenant_id LogsArchive#tenant_id}
        '''
        result = self._values.get("tenant_id")
        assert result is not None, "Required property 'tenant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path where the archive will be stored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#path LogsArchive#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsArchiveAzureArchive(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsArchiveAzureArchiveOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsArchive.LogsArchiveAzureArchiveOutputReference",
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
            type_hints = typing.get_type_hints(LogsArchiveAzureArchiveOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountInput")
    def storage_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveAzureArchiveOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "container"))

    @container.setter
    def container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveAzureArchiveOutputReference, "container").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "container", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveAzureArchiveOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccount")
    def storage_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccount"))

    @storage_account.setter
    def storage_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveAzureArchiveOutputReference, "storage_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccount", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveAzureArchiveOutputReference, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LogsArchiveAzureArchive]:
        return typing.cast(typing.Optional[LogsArchiveAzureArchive], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LogsArchiveAzureArchive]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveAzureArchiveOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsArchive.LogsArchiveConfig",
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
        "query": "query",
        "azure_archive": "azureArchive",
        "gcs_archive": "gcsArchive",
        "id": "id",
        "include_tags": "includeTags",
        "rehydration_max_scan_size_in_gb": "rehydrationMaxScanSizeInGb",
        "rehydration_tags": "rehydrationTags",
        "s3_archive": "s3Archive",
    },
)
class LogsArchiveConfig(cdktf.TerraformMetaArguments):
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
        query: builtins.str,
        azure_archive: typing.Optional[typing.Union[LogsArchiveAzureArchive, typing.Dict[str, typing.Any]]] = None,
        gcs_archive: typing.Optional[typing.Union["LogsArchiveGcsArchive", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        include_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rehydration_max_scan_size_in_gb: typing.Optional[jsii.Number] = None,
        rehydration_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        s3_archive: typing.Optional[typing.Union["LogsArchiveS3Archive", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Your archive name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#name LogsArchive#name}
        :param query: The archive query/filter. Logs matching this query are included in the archive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#query LogsArchive#query}
        :param azure_archive: azure_archive block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#azure_archive LogsArchive#azure_archive}
        :param gcs_archive: gcs_archive block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#gcs_archive LogsArchive#gcs_archive}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#id LogsArchive#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param include_tags: To store the tags in the archive, set the value ``true``. If it is set to ``false``, the tags will be dropped when the logs are sent to the archive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#include_tags LogsArchive#include_tags}
        :param rehydration_max_scan_size_in_gb: To limit the rehydration scan size for the archive, set a value in GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#rehydration_max_scan_size_in_gb LogsArchive#rehydration_max_scan_size_in_gb}
        :param rehydration_tags: An array of tags to add to rehydrated logs from an archive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#rehydration_tags LogsArchive#rehydration_tags}
        :param s3_archive: s3_archive block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#s3_archive LogsArchive#s3_archive}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(azure_archive, dict):
            azure_archive = LogsArchiveAzureArchive(**azure_archive)
        if isinstance(gcs_archive, dict):
            gcs_archive = LogsArchiveGcsArchive(**gcs_archive)
        if isinstance(s3_archive, dict):
            s3_archive = LogsArchiveS3Archive(**s3_archive)
        if __debug__:
            type_hints = typing.get_type_hints(LogsArchiveConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument azure_archive", value=azure_archive, expected_type=type_hints["azure_archive"])
            check_type(argname="argument gcs_archive", value=gcs_archive, expected_type=type_hints["gcs_archive"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument include_tags", value=include_tags, expected_type=type_hints["include_tags"])
            check_type(argname="argument rehydration_max_scan_size_in_gb", value=rehydration_max_scan_size_in_gb, expected_type=type_hints["rehydration_max_scan_size_in_gb"])
            check_type(argname="argument rehydration_tags", value=rehydration_tags, expected_type=type_hints["rehydration_tags"])
            check_type(argname="argument s3_archive", value=s3_archive, expected_type=type_hints["s3_archive"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "query": query,
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
        if azure_archive is not None:
            self._values["azure_archive"] = azure_archive
        if gcs_archive is not None:
            self._values["gcs_archive"] = gcs_archive
        if id is not None:
            self._values["id"] = id
        if include_tags is not None:
            self._values["include_tags"] = include_tags
        if rehydration_max_scan_size_in_gb is not None:
            self._values["rehydration_max_scan_size_in_gb"] = rehydration_max_scan_size_in_gb
        if rehydration_tags is not None:
            self._values["rehydration_tags"] = rehydration_tags
        if s3_archive is not None:
            self._values["s3_archive"] = s3_archive

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
        '''Your archive name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#name LogsArchive#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''The archive query/filter. Logs matching this query are included in the archive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#query LogsArchive#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def azure_archive(self) -> typing.Optional[LogsArchiveAzureArchive]:
        '''azure_archive block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#azure_archive LogsArchive#azure_archive}
        '''
        result = self._values.get("azure_archive")
        return typing.cast(typing.Optional[LogsArchiveAzureArchive], result)

    @builtins.property
    def gcs_archive(self) -> typing.Optional["LogsArchiveGcsArchive"]:
        '''gcs_archive block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#gcs_archive LogsArchive#gcs_archive}
        '''
        result = self._values.get("gcs_archive")
        return typing.cast(typing.Optional["LogsArchiveGcsArchive"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#id LogsArchive#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''To store the tags in the archive, set the value ``true``.

        If it is set to ``false``, the tags will be dropped when the logs are sent to the archive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#include_tags LogsArchive#include_tags}
        '''
        result = self._values.get("include_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def rehydration_max_scan_size_in_gb(self) -> typing.Optional[jsii.Number]:
        '''To limit the rehydration scan size for the archive, set a value in GB.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#rehydration_max_scan_size_in_gb LogsArchive#rehydration_max_scan_size_in_gb}
        '''
        result = self._values.get("rehydration_max_scan_size_in_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rehydration_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of tags to add to rehydrated logs from an archive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#rehydration_tags LogsArchive#rehydration_tags}
        '''
        result = self._values.get("rehydration_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def s3_archive(self) -> typing.Optional["LogsArchiveS3Archive"]:
        '''s3_archive block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#s3_archive LogsArchive#s3_archive}
        '''
        result = self._values.get("s3_archive")
        return typing.cast(typing.Optional["LogsArchiveS3Archive"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsArchiveConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsArchive.LogsArchiveGcsArchive",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "client_email": "clientEmail",
        "path": "path",
        "project_id": "projectId",
    },
)
class LogsArchiveGcsArchive:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        client_email: builtins.str,
        path: builtins.str,
        project_id: builtins.str,
    ) -> None:
        '''
        :param bucket: Name of your GCS bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#bucket LogsArchive#bucket}
        :param client_email: Your client email. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#client_email LogsArchive#client_email}
        :param path: Path where the archive will be stored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#path LogsArchive#path}
        :param project_id: Your project id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#project_id LogsArchive#project_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsArchiveGcsArchive.__init__)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument client_email", value=client_email, expected_type=type_hints["client_email"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "client_email": client_email,
            "path": path,
            "project_id": project_id,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Name of your GCS bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#bucket LogsArchive#bucket}
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_email(self) -> builtins.str:
        '''Your client email.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#client_email LogsArchive#client_email}
        '''
        result = self._values.get("client_email")
        assert result is not None, "Required property 'client_email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Path where the archive will be stored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#path LogsArchive#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Your project id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#project_id LogsArchive#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsArchiveGcsArchive(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsArchiveGcsArchiveOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsArchive.LogsArchiveGcsArchiveOutputReference",
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
            type_hints = typing.get_type_hints(LogsArchiveGcsArchiveOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="clientEmailInput")
    def client_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveGcsArchiveOutputReference, "bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="clientEmail")
    def client_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientEmail"))

    @client_email.setter
    def client_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveGcsArchiveOutputReference, "client_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientEmail", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveGcsArchiveOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveGcsArchiveOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LogsArchiveGcsArchive]:
        return typing.cast(typing.Optional[LogsArchiveGcsArchive], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LogsArchiveGcsArchive]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveGcsArchiveOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsArchive.LogsArchiveS3Archive",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "bucket": "bucket",
        "path": "path",
        "role_name": "roleName",
    },
)
class LogsArchiveS3Archive:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        bucket: builtins.str,
        path: builtins.str,
        role_name: builtins.str,
    ) -> None:
        '''
        :param account_id: Your AWS account id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#account_id LogsArchive#account_id}
        :param bucket: Name of your s3 bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#bucket LogsArchive#bucket}
        :param path: Path where the archive will be stored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#path LogsArchive#path}
        :param role_name: Your AWS role name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#role_name LogsArchive#role_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsArchiveS3Archive.__init__)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
            "bucket": bucket,
            "path": path,
            "role_name": role_name,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''Your AWS account id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#account_id LogsArchive#account_id}
        '''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Name of your s3 bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#bucket LogsArchive#bucket}
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Path where the archive will be stored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#path LogsArchive#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_name(self) -> builtins.str:
        '''Your AWS role name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_archive#role_name LogsArchive#role_name}
        '''
        result = self._values.get("role_name")
        assert result is not None, "Required property 'role_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsArchiveS3Archive(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsArchiveS3ArchiveOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsArchive.LogsArchiveS3ArchiveOutputReference",
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
            type_hints = typing.get_type_hints(LogsArchiveS3ArchiveOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="roleNameInput")
    def role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveS3ArchiveOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveS3ArchiveOutputReference, "bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveS3ArchiveOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleName"))

    @role_name.setter
    def role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveS3ArchiveOutputReference, "role_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LogsArchiveS3Archive]:
        return typing.cast(typing.Optional[LogsArchiveS3Archive], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LogsArchiveS3Archive]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsArchiveS3ArchiveOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LogsArchive",
    "LogsArchiveAzureArchive",
    "LogsArchiveAzureArchiveOutputReference",
    "LogsArchiveConfig",
    "LogsArchiveGcsArchive",
    "LogsArchiveGcsArchiveOutputReference",
    "LogsArchiveS3Archive",
    "LogsArchiveS3ArchiveOutputReference",
]

publication.publish()
