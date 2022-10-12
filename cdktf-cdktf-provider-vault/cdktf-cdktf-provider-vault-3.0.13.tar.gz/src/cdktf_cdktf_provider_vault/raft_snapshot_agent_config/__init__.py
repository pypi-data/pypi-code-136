'''
# `vault_raft_snapshot_agent_config`

Refer to the Terraform Registory for docs: [`vault_raft_snapshot_agent_config`](https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config).
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


class RaftSnapshotAgentConfig(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.raftSnapshotAgentConfig.RaftSnapshotAgentConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config vault_raft_snapshot_agent_config}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        interval_seconds: jsii.Number,
        name: builtins.str,
        path_prefix: builtins.str,
        storage_type: builtins.str,
        aws_access_key_id: typing.Optional[builtins.str] = None,
        aws_s3_bucket: typing.Optional[builtins.str] = None,
        aws_s3_disable_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        aws_s3_enable_kms: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        aws_s3_endpoint: typing.Optional[builtins.str] = None,
        aws_s3_force_path_style: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        aws_s3_kms_key: typing.Optional[builtins.str] = None,
        aws_s3_region: typing.Optional[builtins.str] = None,
        aws_s3_server_side_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        aws_secret_access_key: typing.Optional[builtins.str] = None,
        aws_session_token: typing.Optional[builtins.str] = None,
        azure_account_key: typing.Optional[builtins.str] = None,
        azure_account_name: typing.Optional[builtins.str] = None,
        azure_blob_environment: typing.Optional[builtins.str] = None,
        azure_container_name: typing.Optional[builtins.str] = None,
        azure_endpoint: typing.Optional[builtins.str] = None,
        file_prefix: typing.Optional[builtins.str] = None,
        google_disable_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        google_endpoint: typing.Optional[builtins.str] = None,
        google_gcs_bucket: typing.Optional[builtins.str] = None,
        google_service_account_key: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        local_max_space: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        retain: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config vault_raft_snapshot_agent_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param interval_seconds: Number of seconds between snapshots. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#interval_seconds RaftSnapshotAgentConfig#interval_seconds}
        :param name: Name of the snapshot agent configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#name RaftSnapshotAgentConfig#name}
        :param path_prefix: The directory or bucket prefix to to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#path_prefix RaftSnapshotAgentConfig#path_prefix}
        :param storage_type: What storage service to send snapshots to. One of "local", "azure-blob", "aws-s3", or "google-gcs". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#storage_type RaftSnapshotAgentConfig#storage_type}
        :param aws_access_key_id: AWS access key ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_access_key_id RaftSnapshotAgentConfig#aws_access_key_id}
        :param aws_s3_bucket: S3 bucket to write snapshots to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_bucket RaftSnapshotAgentConfig#aws_s3_bucket}
        :param aws_s3_disable_tls: Disable TLS for the S3 endpoint. This should only be used for testing purposes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_disable_tls RaftSnapshotAgentConfig#aws_s3_disable_tls}
        :param aws_s3_enable_kms: Use KMS to encrypt bucket contents. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_enable_kms RaftSnapshotAgentConfig#aws_s3_enable_kms}
        :param aws_s3_endpoint: AWS endpoint. This is typically only set when using a non-AWS S3 implementation like Minio. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_endpoint RaftSnapshotAgentConfig#aws_s3_endpoint}
        :param aws_s3_force_path_style: Use the endpoint/bucket URL style instead of bucket.endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_force_path_style RaftSnapshotAgentConfig#aws_s3_force_path_style}
        :param aws_s3_kms_key: Use named KMS key, when aws_s3_enable_kms=true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_kms_key RaftSnapshotAgentConfig#aws_s3_kms_key}
        :param aws_s3_region: AWS region bucket is in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_region RaftSnapshotAgentConfig#aws_s3_region}
        :param aws_s3_server_side_encryption: Use AES256 to encrypt bucket contents. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_server_side_encryption RaftSnapshotAgentConfig#aws_s3_server_side_encryption}
        :param aws_secret_access_key: AWS secret access key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_secret_access_key RaftSnapshotAgentConfig#aws_secret_access_key}
        :param aws_session_token: AWS session token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_session_token RaftSnapshotAgentConfig#aws_session_token}
        :param azure_account_key: Azure account key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#azure_account_key RaftSnapshotAgentConfig#azure_account_key}
        :param azure_account_name: Azure account name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#azure_account_name RaftSnapshotAgentConfig#azure_account_name}
        :param azure_blob_environment: Azure blob environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#azure_blob_environment RaftSnapshotAgentConfig#azure_blob_environment}
        :param azure_container_name: Azure container name to write snapshots to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#azure_container_name RaftSnapshotAgentConfig#azure_container_name}
        :param azure_endpoint: Azure blob storage endpoint. This is typically only set when using a non-Azure implementation like Azurite. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#azure_endpoint RaftSnapshotAgentConfig#azure_endpoint}
        :param file_prefix: The file or object name of snapshot files will start with this string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#file_prefix RaftSnapshotAgentConfig#file_prefix}
        :param google_disable_tls: Disable TLS for the GCS endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#google_disable_tls RaftSnapshotAgentConfig#google_disable_tls}
        :param google_endpoint: GCS endpoint. This is typically only set when using a non-Google GCS implementation like fake-gcs-server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#google_endpoint RaftSnapshotAgentConfig#google_endpoint}
        :param google_gcs_bucket: GCS bucket to write snapshots to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#google_gcs_bucket RaftSnapshotAgentConfig#google_gcs_bucket}
        :param google_service_account_key: Google service account key in JSON format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#google_service_account_key RaftSnapshotAgentConfig#google_service_account_key}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#id RaftSnapshotAgentConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local_max_space: The maximum space, in bytes, to use for snapshots. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#local_max_space RaftSnapshotAgentConfig#local_max_space}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#namespace RaftSnapshotAgentConfig#namespace}
        :param retain: How many snapshots are to be kept. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#retain RaftSnapshotAgentConfig#retain}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RaftSnapshotAgentConfig.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RaftSnapshotAgentConfigConfig(
            interval_seconds=interval_seconds,
            name=name,
            path_prefix=path_prefix,
            storage_type=storage_type,
            aws_access_key_id=aws_access_key_id,
            aws_s3_bucket=aws_s3_bucket,
            aws_s3_disable_tls=aws_s3_disable_tls,
            aws_s3_enable_kms=aws_s3_enable_kms,
            aws_s3_endpoint=aws_s3_endpoint,
            aws_s3_force_path_style=aws_s3_force_path_style,
            aws_s3_kms_key=aws_s3_kms_key,
            aws_s3_region=aws_s3_region,
            aws_s3_server_side_encryption=aws_s3_server_side_encryption,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
            azure_account_key=azure_account_key,
            azure_account_name=azure_account_name,
            azure_blob_environment=azure_blob_environment,
            azure_container_name=azure_container_name,
            azure_endpoint=azure_endpoint,
            file_prefix=file_prefix,
            google_disable_tls=google_disable_tls,
            google_endpoint=google_endpoint,
            google_gcs_bucket=google_gcs_bucket,
            google_service_account_key=google_service_account_key,
            id=id,
            local_max_space=local_max_space,
            namespace=namespace,
            retain=retain,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAwsAccessKeyId")
    def reset_aws_access_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsAccessKeyId", []))

    @jsii.member(jsii_name="resetAwsS3Bucket")
    def reset_aws_s3_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsS3Bucket", []))

    @jsii.member(jsii_name="resetAwsS3DisableTls")
    def reset_aws_s3_disable_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsS3DisableTls", []))

    @jsii.member(jsii_name="resetAwsS3EnableKms")
    def reset_aws_s3_enable_kms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsS3EnableKms", []))

    @jsii.member(jsii_name="resetAwsS3Endpoint")
    def reset_aws_s3_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsS3Endpoint", []))

    @jsii.member(jsii_name="resetAwsS3ForcePathStyle")
    def reset_aws_s3_force_path_style(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsS3ForcePathStyle", []))

    @jsii.member(jsii_name="resetAwsS3KmsKey")
    def reset_aws_s3_kms_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsS3KmsKey", []))

    @jsii.member(jsii_name="resetAwsS3Region")
    def reset_aws_s3_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsS3Region", []))

    @jsii.member(jsii_name="resetAwsS3ServerSideEncryption")
    def reset_aws_s3_server_side_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsS3ServerSideEncryption", []))

    @jsii.member(jsii_name="resetAwsSecretAccessKey")
    def reset_aws_secret_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsSecretAccessKey", []))

    @jsii.member(jsii_name="resetAwsSessionToken")
    def reset_aws_session_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsSessionToken", []))

    @jsii.member(jsii_name="resetAzureAccountKey")
    def reset_azure_account_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureAccountKey", []))

    @jsii.member(jsii_name="resetAzureAccountName")
    def reset_azure_account_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureAccountName", []))

    @jsii.member(jsii_name="resetAzureBlobEnvironment")
    def reset_azure_blob_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureBlobEnvironment", []))

    @jsii.member(jsii_name="resetAzureContainerName")
    def reset_azure_container_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureContainerName", []))

    @jsii.member(jsii_name="resetAzureEndpoint")
    def reset_azure_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureEndpoint", []))

    @jsii.member(jsii_name="resetFilePrefix")
    def reset_file_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilePrefix", []))

    @jsii.member(jsii_name="resetGoogleDisableTls")
    def reset_google_disable_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleDisableTls", []))

    @jsii.member(jsii_name="resetGoogleEndpoint")
    def reset_google_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleEndpoint", []))

    @jsii.member(jsii_name="resetGoogleGcsBucket")
    def reset_google_gcs_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleGcsBucket", []))

    @jsii.member(jsii_name="resetGoogleServiceAccountKey")
    def reset_google_service_account_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleServiceAccountKey", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocalMaxSpace")
    def reset_local_max_space(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalMaxSpace", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetRetain")
    def reset_retain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetain", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="awsAccessKeyIdInput")
    def aws_access_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsAccessKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="awsS3BucketInput")
    def aws_s3_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsS3BucketInput"))

    @builtins.property
    @jsii.member(jsii_name="awsS3DisableTlsInput")
    def aws_s3_disable_tls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "awsS3DisableTlsInput"))

    @builtins.property
    @jsii.member(jsii_name="awsS3EnableKmsInput")
    def aws_s3_enable_kms_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "awsS3EnableKmsInput"))

    @builtins.property
    @jsii.member(jsii_name="awsS3EndpointInput")
    def aws_s3_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsS3EndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="awsS3ForcePathStyleInput")
    def aws_s3_force_path_style_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "awsS3ForcePathStyleInput"))

    @builtins.property
    @jsii.member(jsii_name="awsS3KmsKeyInput")
    def aws_s3_kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsS3KmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="awsS3RegionInput")
    def aws_s3_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsS3RegionInput"))

    @builtins.property
    @jsii.member(jsii_name="awsS3ServerSideEncryptionInput")
    def aws_s3_server_side_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "awsS3ServerSideEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="awsSecretAccessKeyInput")
    def aws_secret_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsSecretAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="awsSessionTokenInput")
    def aws_session_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsSessionTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="azureAccountKeyInput")
    def azure_account_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureAccountKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="azureAccountNameInput")
    def azure_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="azureBlobEnvironmentInput")
    def azure_blob_environment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureBlobEnvironmentInput"))

    @builtins.property
    @jsii.member(jsii_name="azureContainerNameInput")
    def azure_container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureContainerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="azureEndpointInput")
    def azure_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="filePrefixInput")
    def file_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="googleDisableTlsInput")
    def google_disable_tls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "googleDisableTlsInput"))

    @builtins.property
    @jsii.member(jsii_name="googleEndpointInput")
    def google_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="googleGcsBucketInput")
    def google_gcs_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleGcsBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccountKeyInput")
    def google_service_account_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleServiceAccountKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalSecondsInput")
    def interval_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="localMaxSpaceInput")
    def local_max_space_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "localMaxSpaceInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="pathPrefixInput")
    def path_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="retainInput")
    def retain_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retainInput"))

    @builtins.property
    @jsii.member(jsii_name="storageTypeInput")
    def storage_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="awsAccessKeyId")
    def aws_access_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsAccessKeyId"))

    @aws_access_key_id.setter
    def aws_access_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "aws_access_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsAccessKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="awsS3Bucket")
    def aws_s3_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsS3Bucket"))

    @aws_s3_bucket.setter
    def aws_s3_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "aws_s3_bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsS3Bucket", value)

    @builtins.property
    @jsii.member(jsii_name="awsS3DisableTls")
    def aws_s3_disable_tls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "awsS3DisableTls"))

    @aws_s3_disable_tls.setter
    def aws_s3_disable_tls(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "aws_s3_disable_tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsS3DisableTls", value)

    @builtins.property
    @jsii.member(jsii_name="awsS3EnableKms")
    def aws_s3_enable_kms(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "awsS3EnableKms"))

    @aws_s3_enable_kms.setter
    def aws_s3_enable_kms(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "aws_s3_enable_kms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsS3EnableKms", value)

    @builtins.property
    @jsii.member(jsii_name="awsS3Endpoint")
    def aws_s3_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsS3Endpoint"))

    @aws_s3_endpoint.setter
    def aws_s3_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "aws_s3_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsS3Endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="awsS3ForcePathStyle")
    def aws_s3_force_path_style(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "awsS3ForcePathStyle"))

    @aws_s3_force_path_style.setter
    def aws_s3_force_path_style(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "aws_s3_force_path_style").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsS3ForcePathStyle", value)

    @builtins.property
    @jsii.member(jsii_name="awsS3KmsKey")
    def aws_s3_kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsS3KmsKey"))

    @aws_s3_kms_key.setter
    def aws_s3_kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "aws_s3_kms_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsS3KmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="awsS3Region")
    def aws_s3_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsS3Region"))

    @aws_s3_region.setter
    def aws_s3_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "aws_s3_region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsS3Region", value)

    @builtins.property
    @jsii.member(jsii_name="awsS3ServerSideEncryption")
    def aws_s3_server_side_encryption(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "awsS3ServerSideEncryption"))

    @aws_s3_server_side_encryption.setter
    def aws_s3_server_side_encryption(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "aws_s3_server_side_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsS3ServerSideEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="awsSecretAccessKey")
    def aws_secret_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsSecretAccessKey"))

    @aws_secret_access_key.setter
    def aws_secret_access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "aws_secret_access_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsSecretAccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="awsSessionToken")
    def aws_session_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsSessionToken"))

    @aws_session_token.setter
    def aws_session_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "aws_session_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsSessionToken", value)

    @builtins.property
    @jsii.member(jsii_name="azureAccountKey")
    def azure_account_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureAccountKey"))

    @azure_account_key.setter
    def azure_account_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "azure_account_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureAccountKey", value)

    @builtins.property
    @jsii.member(jsii_name="azureAccountName")
    def azure_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureAccountName"))

    @azure_account_name.setter
    def azure_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "azure_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="azureBlobEnvironment")
    def azure_blob_environment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureBlobEnvironment"))

    @azure_blob_environment.setter
    def azure_blob_environment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "azure_blob_environment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureBlobEnvironment", value)

    @builtins.property
    @jsii.member(jsii_name="azureContainerName")
    def azure_container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureContainerName"))

    @azure_container_name.setter
    def azure_container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "azure_container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureContainerName", value)

    @builtins.property
    @jsii.member(jsii_name="azureEndpoint")
    def azure_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureEndpoint"))

    @azure_endpoint.setter
    def azure_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "azure_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="filePrefix")
    def file_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filePrefix"))

    @file_prefix.setter
    def file_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "file_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="googleDisableTls")
    def google_disable_tls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "googleDisableTls"))

    @google_disable_tls.setter
    def google_disable_tls(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "google_disable_tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "googleDisableTls", value)

    @builtins.property
    @jsii.member(jsii_name="googleEndpoint")
    def google_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "googleEndpoint"))

    @google_endpoint.setter
    def google_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "google_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "googleEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="googleGcsBucket")
    def google_gcs_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "googleGcsBucket"))

    @google_gcs_bucket.setter
    def google_gcs_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "google_gcs_bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "googleGcsBucket", value)

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccountKey")
    def google_service_account_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "googleServiceAccountKey"))

    @google_service_account_key.setter
    def google_service_account_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "google_service_account_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "googleServiceAccountKey", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="intervalSeconds")
    def interval_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalSeconds"))

    @interval_seconds.setter
    def interval_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "interval_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="localMaxSpace")
    def local_max_space(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "localMaxSpace"))

    @local_max_space.setter
    def local_max_space(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "local_max_space").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localMaxSpace", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="pathPrefix")
    def path_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathPrefix"))

    @path_prefix.setter
    def path_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "path_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="retain")
    def retain(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retain"))

    @retain.setter
    def retain(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "retain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retain", value)

    @builtins.property
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftSnapshotAgentConfig, "storage_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.raftSnapshotAgentConfig.RaftSnapshotAgentConfigConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "interval_seconds": "intervalSeconds",
        "name": "name",
        "path_prefix": "pathPrefix",
        "storage_type": "storageType",
        "aws_access_key_id": "awsAccessKeyId",
        "aws_s3_bucket": "awsS3Bucket",
        "aws_s3_disable_tls": "awsS3DisableTls",
        "aws_s3_enable_kms": "awsS3EnableKms",
        "aws_s3_endpoint": "awsS3Endpoint",
        "aws_s3_force_path_style": "awsS3ForcePathStyle",
        "aws_s3_kms_key": "awsS3KmsKey",
        "aws_s3_region": "awsS3Region",
        "aws_s3_server_side_encryption": "awsS3ServerSideEncryption",
        "aws_secret_access_key": "awsSecretAccessKey",
        "aws_session_token": "awsSessionToken",
        "azure_account_key": "azureAccountKey",
        "azure_account_name": "azureAccountName",
        "azure_blob_environment": "azureBlobEnvironment",
        "azure_container_name": "azureContainerName",
        "azure_endpoint": "azureEndpoint",
        "file_prefix": "filePrefix",
        "google_disable_tls": "googleDisableTls",
        "google_endpoint": "googleEndpoint",
        "google_gcs_bucket": "googleGcsBucket",
        "google_service_account_key": "googleServiceAccountKey",
        "id": "id",
        "local_max_space": "localMaxSpace",
        "namespace": "namespace",
        "retain": "retain",
    },
)
class RaftSnapshotAgentConfigConfig(cdktf.TerraformMetaArguments):
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
        interval_seconds: jsii.Number,
        name: builtins.str,
        path_prefix: builtins.str,
        storage_type: builtins.str,
        aws_access_key_id: typing.Optional[builtins.str] = None,
        aws_s3_bucket: typing.Optional[builtins.str] = None,
        aws_s3_disable_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        aws_s3_enable_kms: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        aws_s3_endpoint: typing.Optional[builtins.str] = None,
        aws_s3_force_path_style: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        aws_s3_kms_key: typing.Optional[builtins.str] = None,
        aws_s3_region: typing.Optional[builtins.str] = None,
        aws_s3_server_side_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        aws_secret_access_key: typing.Optional[builtins.str] = None,
        aws_session_token: typing.Optional[builtins.str] = None,
        azure_account_key: typing.Optional[builtins.str] = None,
        azure_account_name: typing.Optional[builtins.str] = None,
        azure_blob_environment: typing.Optional[builtins.str] = None,
        azure_container_name: typing.Optional[builtins.str] = None,
        azure_endpoint: typing.Optional[builtins.str] = None,
        file_prefix: typing.Optional[builtins.str] = None,
        google_disable_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        google_endpoint: typing.Optional[builtins.str] = None,
        google_gcs_bucket: typing.Optional[builtins.str] = None,
        google_service_account_key: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        local_max_space: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        retain: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param interval_seconds: Number of seconds between snapshots. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#interval_seconds RaftSnapshotAgentConfig#interval_seconds}
        :param name: Name of the snapshot agent configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#name RaftSnapshotAgentConfig#name}
        :param path_prefix: The directory or bucket prefix to to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#path_prefix RaftSnapshotAgentConfig#path_prefix}
        :param storage_type: What storage service to send snapshots to. One of "local", "azure-blob", "aws-s3", or "google-gcs". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#storage_type RaftSnapshotAgentConfig#storage_type}
        :param aws_access_key_id: AWS access key ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_access_key_id RaftSnapshotAgentConfig#aws_access_key_id}
        :param aws_s3_bucket: S3 bucket to write snapshots to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_bucket RaftSnapshotAgentConfig#aws_s3_bucket}
        :param aws_s3_disable_tls: Disable TLS for the S3 endpoint. This should only be used for testing purposes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_disable_tls RaftSnapshotAgentConfig#aws_s3_disable_tls}
        :param aws_s3_enable_kms: Use KMS to encrypt bucket contents. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_enable_kms RaftSnapshotAgentConfig#aws_s3_enable_kms}
        :param aws_s3_endpoint: AWS endpoint. This is typically only set when using a non-AWS S3 implementation like Minio. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_endpoint RaftSnapshotAgentConfig#aws_s3_endpoint}
        :param aws_s3_force_path_style: Use the endpoint/bucket URL style instead of bucket.endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_force_path_style RaftSnapshotAgentConfig#aws_s3_force_path_style}
        :param aws_s3_kms_key: Use named KMS key, when aws_s3_enable_kms=true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_kms_key RaftSnapshotAgentConfig#aws_s3_kms_key}
        :param aws_s3_region: AWS region bucket is in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_region RaftSnapshotAgentConfig#aws_s3_region}
        :param aws_s3_server_side_encryption: Use AES256 to encrypt bucket contents. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_server_side_encryption RaftSnapshotAgentConfig#aws_s3_server_side_encryption}
        :param aws_secret_access_key: AWS secret access key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_secret_access_key RaftSnapshotAgentConfig#aws_secret_access_key}
        :param aws_session_token: AWS session token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_session_token RaftSnapshotAgentConfig#aws_session_token}
        :param azure_account_key: Azure account key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#azure_account_key RaftSnapshotAgentConfig#azure_account_key}
        :param azure_account_name: Azure account name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#azure_account_name RaftSnapshotAgentConfig#azure_account_name}
        :param azure_blob_environment: Azure blob environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#azure_blob_environment RaftSnapshotAgentConfig#azure_blob_environment}
        :param azure_container_name: Azure container name to write snapshots to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#azure_container_name RaftSnapshotAgentConfig#azure_container_name}
        :param azure_endpoint: Azure blob storage endpoint. This is typically only set when using a non-Azure implementation like Azurite. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#azure_endpoint RaftSnapshotAgentConfig#azure_endpoint}
        :param file_prefix: The file or object name of snapshot files will start with this string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#file_prefix RaftSnapshotAgentConfig#file_prefix}
        :param google_disable_tls: Disable TLS for the GCS endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#google_disable_tls RaftSnapshotAgentConfig#google_disable_tls}
        :param google_endpoint: GCS endpoint. This is typically only set when using a non-Google GCS implementation like fake-gcs-server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#google_endpoint RaftSnapshotAgentConfig#google_endpoint}
        :param google_gcs_bucket: GCS bucket to write snapshots to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#google_gcs_bucket RaftSnapshotAgentConfig#google_gcs_bucket}
        :param google_service_account_key: Google service account key in JSON format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#google_service_account_key RaftSnapshotAgentConfig#google_service_account_key}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#id RaftSnapshotAgentConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local_max_space: The maximum space, in bytes, to use for snapshots. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#local_max_space RaftSnapshotAgentConfig#local_max_space}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#namespace RaftSnapshotAgentConfig#namespace}
        :param retain: How many snapshots are to be kept. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#retain RaftSnapshotAgentConfig#retain}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(RaftSnapshotAgentConfigConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument interval_seconds", value=interval_seconds, expected_type=type_hints["interval_seconds"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument path_prefix", value=path_prefix, expected_type=type_hints["path_prefix"])
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
            check_type(argname="argument aws_access_key_id", value=aws_access_key_id, expected_type=type_hints["aws_access_key_id"])
            check_type(argname="argument aws_s3_bucket", value=aws_s3_bucket, expected_type=type_hints["aws_s3_bucket"])
            check_type(argname="argument aws_s3_disable_tls", value=aws_s3_disable_tls, expected_type=type_hints["aws_s3_disable_tls"])
            check_type(argname="argument aws_s3_enable_kms", value=aws_s3_enable_kms, expected_type=type_hints["aws_s3_enable_kms"])
            check_type(argname="argument aws_s3_endpoint", value=aws_s3_endpoint, expected_type=type_hints["aws_s3_endpoint"])
            check_type(argname="argument aws_s3_force_path_style", value=aws_s3_force_path_style, expected_type=type_hints["aws_s3_force_path_style"])
            check_type(argname="argument aws_s3_kms_key", value=aws_s3_kms_key, expected_type=type_hints["aws_s3_kms_key"])
            check_type(argname="argument aws_s3_region", value=aws_s3_region, expected_type=type_hints["aws_s3_region"])
            check_type(argname="argument aws_s3_server_side_encryption", value=aws_s3_server_side_encryption, expected_type=type_hints["aws_s3_server_side_encryption"])
            check_type(argname="argument aws_secret_access_key", value=aws_secret_access_key, expected_type=type_hints["aws_secret_access_key"])
            check_type(argname="argument aws_session_token", value=aws_session_token, expected_type=type_hints["aws_session_token"])
            check_type(argname="argument azure_account_key", value=azure_account_key, expected_type=type_hints["azure_account_key"])
            check_type(argname="argument azure_account_name", value=azure_account_name, expected_type=type_hints["azure_account_name"])
            check_type(argname="argument azure_blob_environment", value=azure_blob_environment, expected_type=type_hints["azure_blob_environment"])
            check_type(argname="argument azure_container_name", value=azure_container_name, expected_type=type_hints["azure_container_name"])
            check_type(argname="argument azure_endpoint", value=azure_endpoint, expected_type=type_hints["azure_endpoint"])
            check_type(argname="argument file_prefix", value=file_prefix, expected_type=type_hints["file_prefix"])
            check_type(argname="argument google_disable_tls", value=google_disable_tls, expected_type=type_hints["google_disable_tls"])
            check_type(argname="argument google_endpoint", value=google_endpoint, expected_type=type_hints["google_endpoint"])
            check_type(argname="argument google_gcs_bucket", value=google_gcs_bucket, expected_type=type_hints["google_gcs_bucket"])
            check_type(argname="argument google_service_account_key", value=google_service_account_key, expected_type=type_hints["google_service_account_key"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument local_max_space", value=local_max_space, expected_type=type_hints["local_max_space"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument retain", value=retain, expected_type=type_hints["retain"])
        self._values: typing.Dict[str, typing.Any] = {
            "interval_seconds": interval_seconds,
            "name": name,
            "path_prefix": path_prefix,
            "storage_type": storage_type,
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
        if aws_access_key_id is not None:
            self._values["aws_access_key_id"] = aws_access_key_id
        if aws_s3_bucket is not None:
            self._values["aws_s3_bucket"] = aws_s3_bucket
        if aws_s3_disable_tls is not None:
            self._values["aws_s3_disable_tls"] = aws_s3_disable_tls
        if aws_s3_enable_kms is not None:
            self._values["aws_s3_enable_kms"] = aws_s3_enable_kms
        if aws_s3_endpoint is not None:
            self._values["aws_s3_endpoint"] = aws_s3_endpoint
        if aws_s3_force_path_style is not None:
            self._values["aws_s3_force_path_style"] = aws_s3_force_path_style
        if aws_s3_kms_key is not None:
            self._values["aws_s3_kms_key"] = aws_s3_kms_key
        if aws_s3_region is not None:
            self._values["aws_s3_region"] = aws_s3_region
        if aws_s3_server_side_encryption is not None:
            self._values["aws_s3_server_side_encryption"] = aws_s3_server_side_encryption
        if aws_secret_access_key is not None:
            self._values["aws_secret_access_key"] = aws_secret_access_key
        if aws_session_token is not None:
            self._values["aws_session_token"] = aws_session_token
        if azure_account_key is not None:
            self._values["azure_account_key"] = azure_account_key
        if azure_account_name is not None:
            self._values["azure_account_name"] = azure_account_name
        if azure_blob_environment is not None:
            self._values["azure_blob_environment"] = azure_blob_environment
        if azure_container_name is not None:
            self._values["azure_container_name"] = azure_container_name
        if azure_endpoint is not None:
            self._values["azure_endpoint"] = azure_endpoint
        if file_prefix is not None:
            self._values["file_prefix"] = file_prefix
        if google_disable_tls is not None:
            self._values["google_disable_tls"] = google_disable_tls
        if google_endpoint is not None:
            self._values["google_endpoint"] = google_endpoint
        if google_gcs_bucket is not None:
            self._values["google_gcs_bucket"] = google_gcs_bucket
        if google_service_account_key is not None:
            self._values["google_service_account_key"] = google_service_account_key
        if id is not None:
            self._values["id"] = id
        if local_max_space is not None:
            self._values["local_max_space"] = local_max_space
        if namespace is not None:
            self._values["namespace"] = namespace
        if retain is not None:
            self._values["retain"] = retain

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
    def interval_seconds(self) -> jsii.Number:
        '''Number of seconds between snapshots.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#interval_seconds RaftSnapshotAgentConfig#interval_seconds}
        '''
        result = self._values.get("interval_seconds")
        assert result is not None, "Required property 'interval_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the snapshot agent configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#name RaftSnapshotAgentConfig#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path_prefix(self) -> builtins.str:
        '''The directory or bucket prefix to to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#path_prefix RaftSnapshotAgentConfig#path_prefix}
        '''
        result = self._values.get("path_prefix")
        assert result is not None, "Required property 'path_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_type(self) -> builtins.str:
        '''What storage service to send snapshots to. One of "local", "azure-blob", "aws-s3", or "google-gcs".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#storage_type RaftSnapshotAgentConfig#storage_type}
        '''
        result = self._values.get("storage_type")
        assert result is not None, "Required property 'storage_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_access_key_id(self) -> typing.Optional[builtins.str]:
        '''AWS access key ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_access_key_id RaftSnapshotAgentConfig#aws_access_key_id}
        '''
        result = self._values.get("aws_access_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_s3_bucket(self) -> typing.Optional[builtins.str]:
        '''S3 bucket to write snapshots to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_bucket RaftSnapshotAgentConfig#aws_s3_bucket}
        '''
        result = self._values.get("aws_s3_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_s3_disable_tls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disable TLS for the S3 endpoint. This should only be used for testing purposes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_disable_tls RaftSnapshotAgentConfig#aws_s3_disable_tls}
        '''
        result = self._values.get("aws_s3_disable_tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def aws_s3_enable_kms(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Use KMS to encrypt bucket contents.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_enable_kms RaftSnapshotAgentConfig#aws_s3_enable_kms}
        '''
        result = self._values.get("aws_s3_enable_kms")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def aws_s3_endpoint(self) -> typing.Optional[builtins.str]:
        '''AWS endpoint. This is typically only set when using a non-AWS S3 implementation like Minio.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_endpoint RaftSnapshotAgentConfig#aws_s3_endpoint}
        '''
        result = self._values.get("aws_s3_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_s3_force_path_style(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Use the endpoint/bucket URL style instead of bucket.endpoint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_force_path_style RaftSnapshotAgentConfig#aws_s3_force_path_style}
        '''
        result = self._values.get("aws_s3_force_path_style")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def aws_s3_kms_key(self) -> typing.Optional[builtins.str]:
        '''Use named KMS key, when aws_s3_enable_kms=true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_kms_key RaftSnapshotAgentConfig#aws_s3_kms_key}
        '''
        result = self._values.get("aws_s3_kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_s3_region(self) -> typing.Optional[builtins.str]:
        '''AWS region bucket is in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_region RaftSnapshotAgentConfig#aws_s3_region}
        '''
        result = self._values.get("aws_s3_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_s3_server_side_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Use AES256 to encrypt bucket contents.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_s3_server_side_encryption RaftSnapshotAgentConfig#aws_s3_server_side_encryption}
        '''
        result = self._values.get("aws_s3_server_side_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def aws_secret_access_key(self) -> typing.Optional[builtins.str]:
        '''AWS secret access key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_secret_access_key RaftSnapshotAgentConfig#aws_secret_access_key}
        '''
        result = self._values.get("aws_secret_access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_session_token(self) -> typing.Optional[builtins.str]:
        '''AWS session token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#aws_session_token RaftSnapshotAgentConfig#aws_session_token}
        '''
        result = self._values.get("aws_session_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_account_key(self) -> typing.Optional[builtins.str]:
        '''Azure account key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#azure_account_key RaftSnapshotAgentConfig#azure_account_key}
        '''
        result = self._values.get("azure_account_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_account_name(self) -> typing.Optional[builtins.str]:
        '''Azure account name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#azure_account_name RaftSnapshotAgentConfig#azure_account_name}
        '''
        result = self._values.get("azure_account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_blob_environment(self) -> typing.Optional[builtins.str]:
        '''Azure blob environment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#azure_blob_environment RaftSnapshotAgentConfig#azure_blob_environment}
        '''
        result = self._values.get("azure_blob_environment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_container_name(self) -> typing.Optional[builtins.str]:
        '''Azure container name to write snapshots to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#azure_container_name RaftSnapshotAgentConfig#azure_container_name}
        '''
        result = self._values.get("azure_container_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_endpoint(self) -> typing.Optional[builtins.str]:
        '''Azure blob storage endpoint. This is typically only set when using a non-Azure implementation like Azurite.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#azure_endpoint RaftSnapshotAgentConfig#azure_endpoint}
        '''
        result = self._values.get("azure_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_prefix(self) -> typing.Optional[builtins.str]:
        '''The file or object name of snapshot files will start with this string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#file_prefix RaftSnapshotAgentConfig#file_prefix}
        '''
        result = self._values.get("file_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def google_disable_tls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disable TLS for the GCS endpoint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#google_disable_tls RaftSnapshotAgentConfig#google_disable_tls}
        '''
        result = self._values.get("google_disable_tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def google_endpoint(self) -> typing.Optional[builtins.str]:
        '''GCS endpoint. This is typically only set when using a non-Google GCS implementation like fake-gcs-server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#google_endpoint RaftSnapshotAgentConfig#google_endpoint}
        '''
        result = self._values.get("google_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def google_gcs_bucket(self) -> typing.Optional[builtins.str]:
        '''GCS bucket to write snapshots to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#google_gcs_bucket RaftSnapshotAgentConfig#google_gcs_bucket}
        '''
        result = self._values.get("google_gcs_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def google_service_account_key(self) -> typing.Optional[builtins.str]:
        '''Google service account key in JSON format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#google_service_account_key RaftSnapshotAgentConfig#google_service_account_key}
        '''
        result = self._values.get("google_service_account_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#id RaftSnapshotAgentConfig#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_max_space(self) -> typing.Optional[jsii.Number]:
        '''The maximum space, in bytes, to use for snapshots.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#local_max_space RaftSnapshotAgentConfig#local_max_space}
        '''
        result = self._values.get("local_max_space")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#namespace RaftSnapshotAgentConfig#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retain(self) -> typing.Optional[jsii.Number]:
        '''How many snapshots are to be kept.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_snapshot_agent_config#retain RaftSnapshotAgentConfig#retain}
        '''
        result = self._values.get("retain")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RaftSnapshotAgentConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "RaftSnapshotAgentConfig",
    "RaftSnapshotAgentConfigConfig",
]

publication.publish()
