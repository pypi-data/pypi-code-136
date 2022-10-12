'''
# `databricks_mws_workspaces`

Refer to the Terraform Registory for docs: [`databricks_mws_workspaces`](https://www.terraform.io/docs/providers/databricks/r/mws_workspaces).
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


class MwsWorkspaces(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspaces",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces databricks_mws_workspaces}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        account_id: builtins.str,
        workspace_name: builtins.str,
        aws_region: typing.Optional[builtins.str] = None,
        cloud: typing.Optional[builtins.str] = None,
        cloud_resource_bucket: typing.Optional[typing.Union["MwsWorkspacesCloudResourceBucket", typing.Dict[str, typing.Any]]] = None,
        creation_time: typing.Optional[jsii.Number] = None,
        credentials_id: typing.Optional[builtins.str] = None,
        customer_managed_key_id: typing.Optional[builtins.str] = None,
        deployment_name: typing.Optional[builtins.str] = None,
        external_customer_info: typing.Optional[typing.Union["MwsWorkspacesExternalCustomerInfo", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        is_no_public_ip_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        managed_services_customer_managed_key_id: typing.Optional[builtins.str] = None,
        network: typing.Optional[typing.Union["MwsWorkspacesNetwork", typing.Dict[str, typing.Any]]] = None,
        network_id: typing.Optional[builtins.str] = None,
        pricing_tier: typing.Optional[builtins.str] = None,
        private_access_settings_id: typing.Optional[builtins.str] = None,
        storage_configuration_id: typing.Optional[builtins.str] = None,
        storage_customer_managed_key_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MwsWorkspacesTimeouts", typing.Dict[str, typing.Any]]] = None,
        token: typing.Optional[typing.Union["MwsWorkspacesToken", typing.Dict[str, typing.Any]]] = None,
        workspace_id: typing.Optional[jsii.Number] = None,
        workspace_status: typing.Optional[builtins.str] = None,
        workspace_status_message: typing.Optional[builtins.str] = None,
        workspace_url: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces databricks_mws_workspaces} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#account_id MwsWorkspaces#account_id}.
        :param workspace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_name MwsWorkspaces#workspace_name}.
        :param aws_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#aws_region MwsWorkspaces#aws_region}.
        :param cloud: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#cloud MwsWorkspaces#cloud}.
        :param cloud_resource_bucket: cloud_resource_bucket block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#cloud_resource_bucket MwsWorkspaces#cloud_resource_bucket}
        :param creation_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#creation_time MwsWorkspaces#creation_time}.
        :param credentials_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#credentials_id MwsWorkspaces#credentials_id}.
        :param customer_managed_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#customer_managed_key_id MwsWorkspaces#customer_managed_key_id}.
        :param deployment_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#deployment_name MwsWorkspaces#deployment_name}.
        :param external_customer_info: external_customer_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#external_customer_info MwsWorkspaces#external_customer_info}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#id MwsWorkspaces#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_no_public_ip_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#is_no_public_ip_enabled MwsWorkspaces#is_no_public_ip_enabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#location MwsWorkspaces#location}.
        :param managed_services_customer_managed_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#managed_services_customer_managed_key_id MwsWorkspaces#managed_services_customer_managed_key_id}.
        :param network: network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#network MwsWorkspaces#network}
        :param network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#network_id MwsWorkspaces#network_id}.
        :param pricing_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#pricing_tier MwsWorkspaces#pricing_tier}.
        :param private_access_settings_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#private_access_settings_id MwsWorkspaces#private_access_settings_id}.
        :param storage_configuration_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#storage_configuration_id MwsWorkspaces#storage_configuration_id}.
        :param storage_customer_managed_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#storage_customer_managed_key_id MwsWorkspaces#storage_customer_managed_key_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#timeouts MwsWorkspaces#timeouts}
        :param token: token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token MwsWorkspaces#token}
        :param workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_id MwsWorkspaces#workspace_id}.
        :param workspace_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_status MwsWorkspaces#workspace_status}.
        :param workspace_status_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_status_message MwsWorkspaces#workspace_status_message}.
        :param workspace_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_url MwsWorkspaces#workspace_url}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MwsWorkspaces.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MwsWorkspacesConfig(
            account_id=account_id,
            workspace_name=workspace_name,
            aws_region=aws_region,
            cloud=cloud,
            cloud_resource_bucket=cloud_resource_bucket,
            creation_time=creation_time,
            credentials_id=credentials_id,
            customer_managed_key_id=customer_managed_key_id,
            deployment_name=deployment_name,
            external_customer_info=external_customer_info,
            id=id,
            is_no_public_ip_enabled=is_no_public_ip_enabled,
            location=location,
            managed_services_customer_managed_key_id=managed_services_customer_managed_key_id,
            network=network,
            network_id=network_id,
            pricing_tier=pricing_tier,
            private_access_settings_id=private_access_settings_id,
            storage_configuration_id=storage_configuration_id,
            storage_customer_managed_key_id=storage_customer_managed_key_id,
            timeouts=timeouts,
            token=token,
            workspace_id=workspace_id,
            workspace_status=workspace_status,
            workspace_status_message=workspace_status_message,
            workspace_url=workspace_url,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCloudResourceBucket")
    def put_cloud_resource_bucket(
        self,
        *,
        gcp: typing.Union["MwsWorkspacesCloudResourceBucketGcp", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param gcp: gcp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gcp MwsWorkspaces#gcp}
        '''
        value = MwsWorkspacesCloudResourceBucket(gcp=gcp)

        return typing.cast(None, jsii.invoke(self, "putCloudResourceBucket", [value]))

    @jsii.member(jsii_name="putExternalCustomerInfo")
    def put_external_customer_info(
        self,
        *,
        authoritative_user_email: builtins.str,
        authoritative_user_full_name: builtins.str,
        customer_name: builtins.str,
    ) -> None:
        '''
        :param authoritative_user_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#authoritative_user_email MwsWorkspaces#authoritative_user_email}.
        :param authoritative_user_full_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#authoritative_user_full_name MwsWorkspaces#authoritative_user_full_name}.
        :param customer_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#customer_name MwsWorkspaces#customer_name}.
        '''
        value = MwsWorkspacesExternalCustomerInfo(
            authoritative_user_email=authoritative_user_email,
            authoritative_user_full_name=authoritative_user_full_name,
            customer_name=customer_name,
        )

        return typing.cast(None, jsii.invoke(self, "putExternalCustomerInfo", [value]))

    @jsii.member(jsii_name="putNetwork")
    def put_network(
        self,
        *,
        gcp_common_network_config: typing.Union["MwsWorkspacesNetworkGcpCommonNetworkConfig", typing.Dict[str, typing.Any]],
        gcp_managed_network_config: typing.Optional[typing.Union["MwsWorkspacesNetworkGcpManagedNetworkConfig", typing.Dict[str, typing.Any]]] = None,
        network_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param gcp_common_network_config: gcp_common_network_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gcp_common_network_config MwsWorkspaces#gcp_common_network_config}
        :param gcp_managed_network_config: gcp_managed_network_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gcp_managed_network_config MwsWorkspaces#gcp_managed_network_config}
        :param network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#network_id MwsWorkspaces#network_id}.
        '''
        value = MwsWorkspacesNetwork(
            gcp_common_network_config=gcp_common_network_config,
            gcp_managed_network_config=gcp_managed_network_config,
            network_id=network_id,
        )

        return typing.cast(None, jsii.invoke(self, "putNetwork", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#create MwsWorkspaces#create}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#read MwsWorkspaces#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#update MwsWorkspaces#update}.
        '''
        value = MwsWorkspacesTimeouts(create=create, read=read, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putToken")
    def put_token(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        lifetime_seconds: typing.Optional[jsii.Number] = None,
        token_id: typing.Optional[builtins.str] = None,
        token_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#comment MwsWorkspaces#comment}.
        :param lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#lifetime_seconds MwsWorkspaces#lifetime_seconds}.
        :param token_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token_id MwsWorkspaces#token_id}.
        :param token_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token_value MwsWorkspaces#token_value}.
        '''
        value = MwsWorkspacesToken(
            comment=comment,
            lifetime_seconds=lifetime_seconds,
            token_id=token_id,
            token_value=token_value,
        )

        return typing.cast(None, jsii.invoke(self, "putToken", [value]))

    @jsii.member(jsii_name="resetAwsRegion")
    def reset_aws_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegion", []))

    @jsii.member(jsii_name="resetCloud")
    def reset_cloud(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloud", []))

    @jsii.member(jsii_name="resetCloudResourceBucket")
    def reset_cloud_resource_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudResourceBucket", []))

    @jsii.member(jsii_name="resetCreationTime")
    def reset_creation_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreationTime", []))

    @jsii.member(jsii_name="resetCredentialsId")
    def reset_credentials_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentialsId", []))

    @jsii.member(jsii_name="resetCustomerManagedKeyId")
    def reset_customer_managed_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerManagedKeyId", []))

    @jsii.member(jsii_name="resetDeploymentName")
    def reset_deployment_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentName", []))

    @jsii.member(jsii_name="resetExternalCustomerInfo")
    def reset_external_customer_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalCustomerInfo", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsNoPublicIpEnabled")
    def reset_is_no_public_ip_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsNoPublicIpEnabled", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetManagedServicesCustomerManagedKeyId")
    def reset_managed_services_customer_managed_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedServicesCustomerManagedKeyId", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetNetworkId")
    def reset_network_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkId", []))

    @jsii.member(jsii_name="resetPricingTier")
    def reset_pricing_tier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPricingTier", []))

    @jsii.member(jsii_name="resetPrivateAccessSettingsId")
    def reset_private_access_settings_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateAccessSettingsId", []))

    @jsii.member(jsii_name="resetStorageConfigurationId")
    def reset_storage_configuration_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageConfigurationId", []))

    @jsii.member(jsii_name="resetStorageCustomerManagedKeyId")
    def reset_storage_customer_managed_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageCustomerManagedKeyId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="resetWorkspaceId")
    def reset_workspace_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceId", []))

    @jsii.member(jsii_name="resetWorkspaceStatus")
    def reset_workspace_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceStatus", []))

    @jsii.member(jsii_name="resetWorkspaceStatusMessage")
    def reset_workspace_status_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceStatusMessage", []))

    @jsii.member(jsii_name="resetWorkspaceUrl")
    def reset_workspace_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceUrl", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cloudResourceBucket")
    def cloud_resource_bucket(
        self,
    ) -> "MwsWorkspacesCloudResourceBucketOutputReference":
        return typing.cast("MwsWorkspacesCloudResourceBucketOutputReference", jsii.get(self, "cloudResourceBucket"))

    @builtins.property
    @jsii.member(jsii_name="externalCustomerInfo")
    def external_customer_info(
        self,
    ) -> "MwsWorkspacesExternalCustomerInfoOutputReference":
        return typing.cast("MwsWorkspacesExternalCustomerInfoOutputReference", jsii.get(self, "externalCustomerInfo"))

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> "MwsWorkspacesNetworkOutputReference":
        return typing.cast("MwsWorkspacesNetworkOutputReference", jsii.get(self, "network"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MwsWorkspacesTimeoutsOutputReference":
        return typing.cast("MwsWorkspacesTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> "MwsWorkspacesTokenOutputReference":
        return typing.cast("MwsWorkspacesTokenOutputReference", jsii.get(self, "token"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegionInput")
    def aws_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudInput")
    def cloud_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudResourceBucketInput")
    def cloud_resource_bucket_input(
        self,
    ) -> typing.Optional["MwsWorkspacesCloudResourceBucket"]:
        return typing.cast(typing.Optional["MwsWorkspacesCloudResourceBucket"], jsii.get(self, "cloudResourceBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="creationTimeInput")
    def creation_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "creationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsIdInput")
    def credentials_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsIdInput"))

    @builtins.property
    @jsii.member(jsii_name="customerManagedKeyIdInput")
    def customer_managed_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerManagedKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentNameInput")
    def deployment_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentNameInput"))

    @builtins.property
    @jsii.member(jsii_name="externalCustomerInfoInput")
    def external_customer_info_input(
        self,
    ) -> typing.Optional["MwsWorkspacesExternalCustomerInfo"]:
        return typing.cast(typing.Optional["MwsWorkspacesExternalCustomerInfo"], jsii.get(self, "externalCustomerInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isNoPublicIpEnabledInput")
    def is_no_public_ip_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isNoPublicIpEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="managedServicesCustomerManagedKeyIdInput")
    def managed_services_customer_managed_key_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedServicesCustomerManagedKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="networkIdInput")
    def network_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional["MwsWorkspacesNetwork"]:
        return typing.cast(typing.Optional["MwsWorkspacesNetwork"], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="pricingTierInput")
    def pricing_tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pricingTierInput"))

    @builtins.property
    @jsii.member(jsii_name="privateAccessSettingsIdInput")
    def private_access_settings_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateAccessSettingsIdInput"))

    @builtins.property
    @jsii.member(jsii_name="storageConfigurationIdInput")
    def storage_configuration_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageConfigurationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="storageCustomerManagedKeyIdInput")
    def storage_customer_managed_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageCustomerManagedKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MwsWorkspacesTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MwsWorkspacesTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional["MwsWorkspacesToken"]:
        return typing.cast(typing.Optional["MwsWorkspacesToken"], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceIdInput")
    def workspace_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "workspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceNameInput")
    def workspace_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceStatusInput")
    def workspace_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceStatusMessageInput")
    def workspace_status_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceStatusMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceUrlInput")
    def workspace_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="awsRegion")
    def aws_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsRegion"))

    @aws_region.setter
    def aws_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "aws_region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegion", value)

    @builtins.property
    @jsii.member(jsii_name="cloud")
    def cloud(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloud"))

    @cloud.setter
    def cloud(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "cloud").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloud", value)

    @builtins.property
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "creationTime"))

    @creation_time.setter
    def creation_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "creation_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creationTime", value)

    @builtins.property
    @jsii.member(jsii_name="credentialsId")
    def credentials_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentialsId"))

    @credentials_id.setter
    def credentials_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "credentials_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialsId", value)

    @builtins.property
    @jsii.member(jsii_name="customerManagedKeyId")
    def customer_managed_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerManagedKeyId"))

    @customer_managed_key_id.setter
    def customer_managed_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "customer_managed_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerManagedKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentName")
    def deployment_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentName"))

    @deployment_name.setter
    def deployment_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "deployment_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isNoPublicIpEnabled")
    def is_no_public_ip_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isNoPublicIpEnabled"))

    @is_no_public_ip_enabled.setter
    def is_no_public_ip_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "is_no_public_ip_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isNoPublicIpEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="managedServicesCustomerManagedKeyId")
    def managed_services_customer_managed_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedServicesCustomerManagedKeyId"))

    @managed_services_customer_managed_key_id.setter
    def managed_services_customer_managed_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "managed_services_customer_managed_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedServicesCustomerManagedKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="networkId")
    def network_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkId"))

    @network_id.setter
    def network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkId", value)

    @builtins.property
    @jsii.member(jsii_name="pricingTier")
    def pricing_tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pricingTier"))

    @pricing_tier.setter
    def pricing_tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "pricing_tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pricingTier", value)

    @builtins.property
    @jsii.member(jsii_name="privateAccessSettingsId")
    def private_access_settings_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateAccessSettingsId"))

    @private_access_settings_id.setter
    def private_access_settings_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "private_access_settings_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateAccessSettingsId", value)

    @builtins.property
    @jsii.member(jsii_name="storageConfigurationId")
    def storage_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageConfigurationId"))

    @storage_configuration_id.setter
    def storage_configuration_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "storage_configuration_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageConfigurationId", value)

    @builtins.property
    @jsii.member(jsii_name="storageCustomerManagedKeyId")
    def storage_customer_managed_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageCustomerManagedKeyId"))

    @storage_customer_managed_key_id.setter
    def storage_customer_managed_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "storage_customer_managed_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCustomerManagedKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceId")
    def workspace_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "workspaceId"))

    @workspace_id.setter
    def workspace_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "workspace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceId", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceName")
    def workspace_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceName"))

    @workspace_name.setter
    def workspace_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "workspace_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceName", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceStatus")
    def workspace_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceStatus"))

    @workspace_status.setter
    def workspace_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "workspace_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceStatus", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceStatusMessage")
    def workspace_status_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceStatusMessage"))

    @workspace_status_message.setter
    def workspace_status_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "workspace_status_message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceStatusMessage", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceUrl")
    def workspace_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceUrl"))

    @workspace_url.setter
    def workspace_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspaces, "workspace_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceUrl", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesCloudResourceBucket",
    jsii_struct_bases=[],
    name_mapping={"gcp": "gcp"},
)
class MwsWorkspacesCloudResourceBucket:
    def __init__(
        self,
        *,
        gcp: typing.Union["MwsWorkspacesCloudResourceBucketGcp", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param gcp: gcp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gcp MwsWorkspaces#gcp}
        '''
        if isinstance(gcp, dict):
            gcp = MwsWorkspacesCloudResourceBucketGcp(**gcp)
        if __debug__:
            type_hints = typing.get_type_hints(MwsWorkspacesCloudResourceBucket.__init__)
            check_type(argname="argument gcp", value=gcp, expected_type=type_hints["gcp"])
        self._values: typing.Dict[str, typing.Any] = {
            "gcp": gcp,
        }

    @builtins.property
    def gcp(self) -> "MwsWorkspacesCloudResourceBucketGcp":
        '''gcp block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gcp MwsWorkspaces#gcp}
        '''
        result = self._values.get("gcp")
        assert result is not None, "Required property 'gcp' is missing"
        return typing.cast("MwsWorkspacesCloudResourceBucketGcp", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesCloudResourceBucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesCloudResourceBucketGcp",
    jsii_struct_bases=[],
    name_mapping={"project_id": "projectId"},
)
class MwsWorkspacesCloudResourceBucketGcp:
    def __init__(self, *, project_id: builtins.str) -> None:
        '''
        :param project_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#project_id MwsWorkspaces#project_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MwsWorkspacesCloudResourceBucketGcp.__init__)
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "project_id": project_id,
        }

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#project_id MwsWorkspaces#project_id}.'''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesCloudResourceBucketGcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsWorkspacesCloudResourceBucketGcpOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesCloudResourceBucketGcpOutputReference",
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
            type_hints = typing.get_type_hints(MwsWorkspacesCloudResourceBucketGcpOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesCloudResourceBucketGcpOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsWorkspacesCloudResourceBucketGcp]:
        return typing.cast(typing.Optional[MwsWorkspacesCloudResourceBucketGcp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwsWorkspacesCloudResourceBucketGcp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesCloudResourceBucketGcpOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MwsWorkspacesCloudResourceBucketOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesCloudResourceBucketOutputReference",
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
            type_hints = typing.get_type_hints(MwsWorkspacesCloudResourceBucketOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGcp")
    def put_gcp(self, *, project_id: builtins.str) -> None:
        '''
        :param project_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#project_id MwsWorkspaces#project_id}.
        '''
        value = MwsWorkspacesCloudResourceBucketGcp(project_id=project_id)

        return typing.cast(None, jsii.invoke(self, "putGcp", [value]))

    @builtins.property
    @jsii.member(jsii_name="gcp")
    def gcp(self) -> MwsWorkspacesCloudResourceBucketGcpOutputReference:
        return typing.cast(MwsWorkspacesCloudResourceBucketGcpOutputReference, jsii.get(self, "gcp"))

    @builtins.property
    @jsii.member(jsii_name="gcpInput")
    def gcp_input(self) -> typing.Optional[MwsWorkspacesCloudResourceBucketGcp]:
        return typing.cast(typing.Optional[MwsWorkspacesCloudResourceBucketGcp], jsii.get(self, "gcpInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsWorkspacesCloudResourceBucket]:
        return typing.cast(typing.Optional[MwsWorkspacesCloudResourceBucket], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwsWorkspacesCloudResourceBucket],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesCloudResourceBucketOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_id": "accountId",
        "workspace_name": "workspaceName",
        "aws_region": "awsRegion",
        "cloud": "cloud",
        "cloud_resource_bucket": "cloudResourceBucket",
        "creation_time": "creationTime",
        "credentials_id": "credentialsId",
        "customer_managed_key_id": "customerManagedKeyId",
        "deployment_name": "deploymentName",
        "external_customer_info": "externalCustomerInfo",
        "id": "id",
        "is_no_public_ip_enabled": "isNoPublicIpEnabled",
        "location": "location",
        "managed_services_customer_managed_key_id": "managedServicesCustomerManagedKeyId",
        "network": "network",
        "network_id": "networkId",
        "pricing_tier": "pricingTier",
        "private_access_settings_id": "privateAccessSettingsId",
        "storage_configuration_id": "storageConfigurationId",
        "storage_customer_managed_key_id": "storageCustomerManagedKeyId",
        "timeouts": "timeouts",
        "token": "token",
        "workspace_id": "workspaceId",
        "workspace_status": "workspaceStatus",
        "workspace_status_message": "workspaceStatusMessage",
        "workspace_url": "workspaceUrl",
    },
)
class MwsWorkspacesConfig(cdktf.TerraformMetaArguments):
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
        account_id: builtins.str,
        workspace_name: builtins.str,
        aws_region: typing.Optional[builtins.str] = None,
        cloud: typing.Optional[builtins.str] = None,
        cloud_resource_bucket: typing.Optional[typing.Union[MwsWorkspacesCloudResourceBucket, typing.Dict[str, typing.Any]]] = None,
        creation_time: typing.Optional[jsii.Number] = None,
        credentials_id: typing.Optional[builtins.str] = None,
        customer_managed_key_id: typing.Optional[builtins.str] = None,
        deployment_name: typing.Optional[builtins.str] = None,
        external_customer_info: typing.Optional[typing.Union["MwsWorkspacesExternalCustomerInfo", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        is_no_public_ip_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        managed_services_customer_managed_key_id: typing.Optional[builtins.str] = None,
        network: typing.Optional[typing.Union["MwsWorkspacesNetwork", typing.Dict[str, typing.Any]]] = None,
        network_id: typing.Optional[builtins.str] = None,
        pricing_tier: typing.Optional[builtins.str] = None,
        private_access_settings_id: typing.Optional[builtins.str] = None,
        storage_configuration_id: typing.Optional[builtins.str] = None,
        storage_customer_managed_key_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MwsWorkspacesTimeouts", typing.Dict[str, typing.Any]]] = None,
        token: typing.Optional[typing.Union["MwsWorkspacesToken", typing.Dict[str, typing.Any]]] = None,
        workspace_id: typing.Optional[jsii.Number] = None,
        workspace_status: typing.Optional[builtins.str] = None,
        workspace_status_message: typing.Optional[builtins.str] = None,
        workspace_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#account_id MwsWorkspaces#account_id}.
        :param workspace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_name MwsWorkspaces#workspace_name}.
        :param aws_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#aws_region MwsWorkspaces#aws_region}.
        :param cloud: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#cloud MwsWorkspaces#cloud}.
        :param cloud_resource_bucket: cloud_resource_bucket block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#cloud_resource_bucket MwsWorkspaces#cloud_resource_bucket}
        :param creation_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#creation_time MwsWorkspaces#creation_time}.
        :param credentials_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#credentials_id MwsWorkspaces#credentials_id}.
        :param customer_managed_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#customer_managed_key_id MwsWorkspaces#customer_managed_key_id}.
        :param deployment_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#deployment_name MwsWorkspaces#deployment_name}.
        :param external_customer_info: external_customer_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#external_customer_info MwsWorkspaces#external_customer_info}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#id MwsWorkspaces#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_no_public_ip_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#is_no_public_ip_enabled MwsWorkspaces#is_no_public_ip_enabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#location MwsWorkspaces#location}.
        :param managed_services_customer_managed_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#managed_services_customer_managed_key_id MwsWorkspaces#managed_services_customer_managed_key_id}.
        :param network: network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#network MwsWorkspaces#network}
        :param network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#network_id MwsWorkspaces#network_id}.
        :param pricing_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#pricing_tier MwsWorkspaces#pricing_tier}.
        :param private_access_settings_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#private_access_settings_id MwsWorkspaces#private_access_settings_id}.
        :param storage_configuration_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#storage_configuration_id MwsWorkspaces#storage_configuration_id}.
        :param storage_customer_managed_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#storage_customer_managed_key_id MwsWorkspaces#storage_customer_managed_key_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#timeouts MwsWorkspaces#timeouts}
        :param token: token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token MwsWorkspaces#token}
        :param workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_id MwsWorkspaces#workspace_id}.
        :param workspace_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_status MwsWorkspaces#workspace_status}.
        :param workspace_status_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_status_message MwsWorkspaces#workspace_status_message}.
        :param workspace_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_url MwsWorkspaces#workspace_url}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cloud_resource_bucket, dict):
            cloud_resource_bucket = MwsWorkspacesCloudResourceBucket(**cloud_resource_bucket)
        if isinstance(external_customer_info, dict):
            external_customer_info = MwsWorkspacesExternalCustomerInfo(**external_customer_info)
        if isinstance(network, dict):
            network = MwsWorkspacesNetwork(**network)
        if isinstance(timeouts, dict):
            timeouts = MwsWorkspacesTimeouts(**timeouts)
        if isinstance(token, dict):
            token = MwsWorkspacesToken(**token)
        if __debug__:
            type_hints = typing.get_type_hints(MwsWorkspacesConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument workspace_name", value=workspace_name, expected_type=type_hints["workspace_name"])
            check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
            check_type(argname="argument cloud", value=cloud, expected_type=type_hints["cloud"])
            check_type(argname="argument cloud_resource_bucket", value=cloud_resource_bucket, expected_type=type_hints["cloud_resource_bucket"])
            check_type(argname="argument creation_time", value=creation_time, expected_type=type_hints["creation_time"])
            check_type(argname="argument credentials_id", value=credentials_id, expected_type=type_hints["credentials_id"])
            check_type(argname="argument customer_managed_key_id", value=customer_managed_key_id, expected_type=type_hints["customer_managed_key_id"])
            check_type(argname="argument deployment_name", value=deployment_name, expected_type=type_hints["deployment_name"])
            check_type(argname="argument external_customer_info", value=external_customer_info, expected_type=type_hints["external_customer_info"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_no_public_ip_enabled", value=is_no_public_ip_enabled, expected_type=type_hints["is_no_public_ip_enabled"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument managed_services_customer_managed_key_id", value=managed_services_customer_managed_key_id, expected_type=type_hints["managed_services_customer_managed_key_id"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument network_id", value=network_id, expected_type=type_hints["network_id"])
            check_type(argname="argument pricing_tier", value=pricing_tier, expected_type=type_hints["pricing_tier"])
            check_type(argname="argument private_access_settings_id", value=private_access_settings_id, expected_type=type_hints["private_access_settings_id"])
            check_type(argname="argument storage_configuration_id", value=storage_configuration_id, expected_type=type_hints["storage_configuration_id"])
            check_type(argname="argument storage_customer_managed_key_id", value=storage_customer_managed_key_id, expected_type=type_hints["storage_customer_managed_key_id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument workspace_id", value=workspace_id, expected_type=type_hints["workspace_id"])
            check_type(argname="argument workspace_status", value=workspace_status, expected_type=type_hints["workspace_status"])
            check_type(argname="argument workspace_status_message", value=workspace_status_message, expected_type=type_hints["workspace_status_message"])
            check_type(argname="argument workspace_url", value=workspace_url, expected_type=type_hints["workspace_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
            "workspace_name": workspace_name,
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
        if aws_region is not None:
            self._values["aws_region"] = aws_region
        if cloud is not None:
            self._values["cloud"] = cloud
        if cloud_resource_bucket is not None:
            self._values["cloud_resource_bucket"] = cloud_resource_bucket
        if creation_time is not None:
            self._values["creation_time"] = creation_time
        if credentials_id is not None:
            self._values["credentials_id"] = credentials_id
        if customer_managed_key_id is not None:
            self._values["customer_managed_key_id"] = customer_managed_key_id
        if deployment_name is not None:
            self._values["deployment_name"] = deployment_name
        if external_customer_info is not None:
            self._values["external_customer_info"] = external_customer_info
        if id is not None:
            self._values["id"] = id
        if is_no_public_ip_enabled is not None:
            self._values["is_no_public_ip_enabled"] = is_no_public_ip_enabled
        if location is not None:
            self._values["location"] = location
        if managed_services_customer_managed_key_id is not None:
            self._values["managed_services_customer_managed_key_id"] = managed_services_customer_managed_key_id
        if network is not None:
            self._values["network"] = network
        if network_id is not None:
            self._values["network_id"] = network_id
        if pricing_tier is not None:
            self._values["pricing_tier"] = pricing_tier
        if private_access_settings_id is not None:
            self._values["private_access_settings_id"] = private_access_settings_id
        if storage_configuration_id is not None:
            self._values["storage_configuration_id"] = storage_configuration_id
        if storage_customer_managed_key_id is not None:
            self._values["storage_customer_managed_key_id"] = storage_customer_managed_key_id
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if token is not None:
            self._values["token"] = token
        if workspace_id is not None:
            self._values["workspace_id"] = workspace_id
        if workspace_status is not None:
            self._values["workspace_status"] = workspace_status
        if workspace_status_message is not None:
            self._values["workspace_status_message"] = workspace_status_message
        if workspace_url is not None:
            self._values["workspace_url"] = workspace_url

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
    def account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#account_id MwsWorkspaces#account_id}.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_name MwsWorkspaces#workspace_name}.'''
        result = self._values.get("workspace_name")
        assert result is not None, "Required property 'workspace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#aws_region MwsWorkspaces#aws_region}.'''
        result = self._values.get("aws_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#cloud MwsWorkspaces#cloud}.'''
        result = self._values.get("cloud")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_resource_bucket(
        self,
    ) -> typing.Optional[MwsWorkspacesCloudResourceBucket]:
        '''cloud_resource_bucket block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#cloud_resource_bucket MwsWorkspaces#cloud_resource_bucket}
        '''
        result = self._values.get("cloud_resource_bucket")
        return typing.cast(typing.Optional[MwsWorkspacesCloudResourceBucket], result)

    @builtins.property
    def creation_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#creation_time MwsWorkspaces#creation_time}.'''
        result = self._values.get("creation_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def credentials_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#credentials_id MwsWorkspaces#credentials_id}.'''
        result = self._values.get("credentials_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def customer_managed_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#customer_managed_key_id MwsWorkspaces#customer_managed_key_id}.'''
        result = self._values.get("customer_managed_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#deployment_name MwsWorkspaces#deployment_name}.'''
        result = self._values.get("deployment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_customer_info(
        self,
    ) -> typing.Optional["MwsWorkspacesExternalCustomerInfo"]:
        '''external_customer_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#external_customer_info MwsWorkspaces#external_customer_info}
        '''
        result = self._values.get("external_customer_info")
        return typing.cast(typing.Optional["MwsWorkspacesExternalCustomerInfo"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#id MwsWorkspaces#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_no_public_ip_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#is_no_public_ip_enabled MwsWorkspaces#is_no_public_ip_enabled}.'''
        result = self._values.get("is_no_public_ip_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#location MwsWorkspaces#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_services_customer_managed_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#managed_services_customer_managed_key_id MwsWorkspaces#managed_services_customer_managed_key_id}.'''
        result = self._values.get("managed_services_customer_managed_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network(self) -> typing.Optional["MwsWorkspacesNetwork"]:
        '''network block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#network MwsWorkspaces#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional["MwsWorkspacesNetwork"], result)

    @builtins.property
    def network_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#network_id MwsWorkspaces#network_id}.'''
        result = self._values.get("network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pricing_tier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#pricing_tier MwsWorkspaces#pricing_tier}.'''
        result = self._values.get("pricing_tier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_access_settings_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#private_access_settings_id MwsWorkspaces#private_access_settings_id}.'''
        result = self._values.get("private_access_settings_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_configuration_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#storage_configuration_id MwsWorkspaces#storage_configuration_id}.'''
        result = self._values.get("storage_configuration_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_customer_managed_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#storage_customer_managed_key_id MwsWorkspaces#storage_customer_managed_key_id}.'''
        result = self._values.get("storage_customer_managed_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MwsWorkspacesTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#timeouts MwsWorkspaces#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MwsWorkspacesTimeouts"], result)

    @builtins.property
    def token(self) -> typing.Optional["MwsWorkspacesToken"]:
        '''token block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token MwsWorkspaces#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional["MwsWorkspacesToken"], result)

    @builtins.property
    def workspace_id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_id MwsWorkspaces#workspace_id}.'''
        result = self._values.get("workspace_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def workspace_status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_status MwsWorkspaces#workspace_status}.'''
        result = self._values.get("workspace_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspace_status_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_status_message MwsWorkspaces#workspace_status_message}.'''
        result = self._values.get("workspace_status_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspace_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_url MwsWorkspaces#workspace_url}.'''
        result = self._values.get("workspace_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesExternalCustomerInfo",
    jsii_struct_bases=[],
    name_mapping={
        "authoritative_user_email": "authoritativeUserEmail",
        "authoritative_user_full_name": "authoritativeUserFullName",
        "customer_name": "customerName",
    },
)
class MwsWorkspacesExternalCustomerInfo:
    def __init__(
        self,
        *,
        authoritative_user_email: builtins.str,
        authoritative_user_full_name: builtins.str,
        customer_name: builtins.str,
    ) -> None:
        '''
        :param authoritative_user_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#authoritative_user_email MwsWorkspaces#authoritative_user_email}.
        :param authoritative_user_full_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#authoritative_user_full_name MwsWorkspaces#authoritative_user_full_name}.
        :param customer_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#customer_name MwsWorkspaces#customer_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MwsWorkspacesExternalCustomerInfo.__init__)
            check_type(argname="argument authoritative_user_email", value=authoritative_user_email, expected_type=type_hints["authoritative_user_email"])
            check_type(argname="argument authoritative_user_full_name", value=authoritative_user_full_name, expected_type=type_hints["authoritative_user_full_name"])
            check_type(argname="argument customer_name", value=customer_name, expected_type=type_hints["customer_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "authoritative_user_email": authoritative_user_email,
            "authoritative_user_full_name": authoritative_user_full_name,
            "customer_name": customer_name,
        }

    @builtins.property
    def authoritative_user_email(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#authoritative_user_email MwsWorkspaces#authoritative_user_email}.'''
        result = self._values.get("authoritative_user_email")
        assert result is not None, "Required property 'authoritative_user_email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authoritative_user_full_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#authoritative_user_full_name MwsWorkspaces#authoritative_user_full_name}.'''
        result = self._values.get("authoritative_user_full_name")
        assert result is not None, "Required property 'authoritative_user_full_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def customer_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#customer_name MwsWorkspaces#customer_name}.'''
        result = self._values.get("customer_name")
        assert result is not None, "Required property 'customer_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesExternalCustomerInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsWorkspacesExternalCustomerInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesExternalCustomerInfoOutputReference",
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
            type_hints = typing.get_type_hints(MwsWorkspacesExternalCustomerInfoOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="authoritativeUserEmailInput")
    def authoritative_user_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authoritativeUserEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="authoritativeUserFullNameInput")
    def authoritative_user_full_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authoritativeUserFullNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customerNameInput")
    def customer_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="authoritativeUserEmail")
    def authoritative_user_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authoritativeUserEmail"))

    @authoritative_user_email.setter
    def authoritative_user_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesExternalCustomerInfoOutputReference, "authoritative_user_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authoritativeUserEmail", value)

    @builtins.property
    @jsii.member(jsii_name="authoritativeUserFullName")
    def authoritative_user_full_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authoritativeUserFullName"))

    @authoritative_user_full_name.setter
    def authoritative_user_full_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesExternalCustomerInfoOutputReference, "authoritative_user_full_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authoritativeUserFullName", value)

    @builtins.property
    @jsii.member(jsii_name="customerName")
    def customer_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerName"))

    @customer_name.setter
    def customer_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesExternalCustomerInfoOutputReference, "customer_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsWorkspacesExternalCustomerInfo]:
        return typing.cast(typing.Optional[MwsWorkspacesExternalCustomerInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwsWorkspacesExternalCustomerInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesExternalCustomerInfoOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesNetwork",
    jsii_struct_bases=[],
    name_mapping={
        "gcp_common_network_config": "gcpCommonNetworkConfig",
        "gcp_managed_network_config": "gcpManagedNetworkConfig",
        "network_id": "networkId",
    },
)
class MwsWorkspacesNetwork:
    def __init__(
        self,
        *,
        gcp_common_network_config: typing.Union["MwsWorkspacesNetworkGcpCommonNetworkConfig", typing.Dict[str, typing.Any]],
        gcp_managed_network_config: typing.Optional[typing.Union["MwsWorkspacesNetworkGcpManagedNetworkConfig", typing.Dict[str, typing.Any]]] = None,
        network_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param gcp_common_network_config: gcp_common_network_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gcp_common_network_config MwsWorkspaces#gcp_common_network_config}
        :param gcp_managed_network_config: gcp_managed_network_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gcp_managed_network_config MwsWorkspaces#gcp_managed_network_config}
        :param network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#network_id MwsWorkspaces#network_id}.
        '''
        if isinstance(gcp_common_network_config, dict):
            gcp_common_network_config = MwsWorkspacesNetworkGcpCommonNetworkConfig(**gcp_common_network_config)
        if isinstance(gcp_managed_network_config, dict):
            gcp_managed_network_config = MwsWorkspacesNetworkGcpManagedNetworkConfig(**gcp_managed_network_config)
        if __debug__:
            type_hints = typing.get_type_hints(MwsWorkspacesNetwork.__init__)
            check_type(argname="argument gcp_common_network_config", value=gcp_common_network_config, expected_type=type_hints["gcp_common_network_config"])
            check_type(argname="argument gcp_managed_network_config", value=gcp_managed_network_config, expected_type=type_hints["gcp_managed_network_config"])
            check_type(argname="argument network_id", value=network_id, expected_type=type_hints["network_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "gcp_common_network_config": gcp_common_network_config,
        }
        if gcp_managed_network_config is not None:
            self._values["gcp_managed_network_config"] = gcp_managed_network_config
        if network_id is not None:
            self._values["network_id"] = network_id

    @builtins.property
    def gcp_common_network_config(self) -> "MwsWorkspacesNetworkGcpCommonNetworkConfig":
        '''gcp_common_network_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gcp_common_network_config MwsWorkspaces#gcp_common_network_config}
        '''
        result = self._values.get("gcp_common_network_config")
        assert result is not None, "Required property 'gcp_common_network_config' is missing"
        return typing.cast("MwsWorkspacesNetworkGcpCommonNetworkConfig", result)

    @builtins.property
    def gcp_managed_network_config(
        self,
    ) -> typing.Optional["MwsWorkspacesNetworkGcpManagedNetworkConfig"]:
        '''gcp_managed_network_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gcp_managed_network_config MwsWorkspaces#gcp_managed_network_config}
        '''
        result = self._values.get("gcp_managed_network_config")
        return typing.cast(typing.Optional["MwsWorkspacesNetworkGcpManagedNetworkConfig"], result)

    @builtins.property
    def network_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#network_id MwsWorkspaces#network_id}.'''
        result = self._values.get("network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesNetwork(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesNetworkGcpCommonNetworkConfig",
    jsii_struct_bases=[],
    name_mapping={
        "gke_cluster_master_ip_range": "gkeClusterMasterIpRange",
        "gke_connectivity_type": "gkeConnectivityType",
    },
)
class MwsWorkspacesNetworkGcpCommonNetworkConfig:
    def __init__(
        self,
        *,
        gke_cluster_master_ip_range: builtins.str,
        gke_connectivity_type: builtins.str,
    ) -> None:
        '''
        :param gke_cluster_master_ip_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_cluster_master_ip_range MwsWorkspaces#gke_cluster_master_ip_range}.
        :param gke_connectivity_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_connectivity_type MwsWorkspaces#gke_connectivity_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MwsWorkspacesNetworkGcpCommonNetworkConfig.__init__)
            check_type(argname="argument gke_cluster_master_ip_range", value=gke_cluster_master_ip_range, expected_type=type_hints["gke_cluster_master_ip_range"])
            check_type(argname="argument gke_connectivity_type", value=gke_connectivity_type, expected_type=type_hints["gke_connectivity_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "gke_cluster_master_ip_range": gke_cluster_master_ip_range,
            "gke_connectivity_type": gke_connectivity_type,
        }

    @builtins.property
    def gke_cluster_master_ip_range(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_cluster_master_ip_range MwsWorkspaces#gke_cluster_master_ip_range}.'''
        result = self._values.get("gke_cluster_master_ip_range")
        assert result is not None, "Required property 'gke_cluster_master_ip_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def gke_connectivity_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_connectivity_type MwsWorkspaces#gke_connectivity_type}.'''
        result = self._values.get("gke_connectivity_type")
        assert result is not None, "Required property 'gke_connectivity_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesNetworkGcpCommonNetworkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsWorkspacesNetworkGcpCommonNetworkConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesNetworkGcpCommonNetworkConfigOutputReference",
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
            type_hints = typing.get_type_hints(MwsWorkspacesNetworkGcpCommonNetworkConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="gkeClusterMasterIpRangeInput")
    def gke_cluster_master_ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gkeClusterMasterIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="gkeConnectivityTypeInput")
    def gke_connectivity_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gkeConnectivityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="gkeClusterMasterIpRange")
    def gke_cluster_master_ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gkeClusterMasterIpRange"))

    @gke_cluster_master_ip_range.setter
    def gke_cluster_master_ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesNetworkGcpCommonNetworkConfigOutputReference, "gke_cluster_master_ip_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gkeClusterMasterIpRange", value)

    @builtins.property
    @jsii.member(jsii_name="gkeConnectivityType")
    def gke_connectivity_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gkeConnectivityType"))

    @gke_connectivity_type.setter
    def gke_connectivity_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesNetworkGcpCommonNetworkConfigOutputReference, "gke_connectivity_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gkeConnectivityType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MwsWorkspacesNetworkGcpCommonNetworkConfig]:
        return typing.cast(typing.Optional[MwsWorkspacesNetworkGcpCommonNetworkConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwsWorkspacesNetworkGcpCommonNetworkConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesNetworkGcpCommonNetworkConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesNetworkGcpManagedNetworkConfig",
    jsii_struct_bases=[],
    name_mapping={
        "gke_cluster_pod_ip_range": "gkeClusterPodIpRange",
        "gke_cluster_service_ip_range": "gkeClusterServiceIpRange",
        "subnet_cidr": "subnetCidr",
    },
)
class MwsWorkspacesNetworkGcpManagedNetworkConfig:
    def __init__(
        self,
        *,
        gke_cluster_pod_ip_range: builtins.str,
        gke_cluster_service_ip_range: builtins.str,
        subnet_cidr: builtins.str,
    ) -> None:
        '''
        :param gke_cluster_pod_ip_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_cluster_pod_ip_range MwsWorkspaces#gke_cluster_pod_ip_range}.
        :param gke_cluster_service_ip_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_cluster_service_ip_range MwsWorkspaces#gke_cluster_service_ip_range}.
        :param subnet_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#subnet_cidr MwsWorkspaces#subnet_cidr}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MwsWorkspacesNetworkGcpManagedNetworkConfig.__init__)
            check_type(argname="argument gke_cluster_pod_ip_range", value=gke_cluster_pod_ip_range, expected_type=type_hints["gke_cluster_pod_ip_range"])
            check_type(argname="argument gke_cluster_service_ip_range", value=gke_cluster_service_ip_range, expected_type=type_hints["gke_cluster_service_ip_range"])
            check_type(argname="argument subnet_cidr", value=subnet_cidr, expected_type=type_hints["subnet_cidr"])
        self._values: typing.Dict[str, typing.Any] = {
            "gke_cluster_pod_ip_range": gke_cluster_pod_ip_range,
            "gke_cluster_service_ip_range": gke_cluster_service_ip_range,
            "subnet_cidr": subnet_cidr,
        }

    @builtins.property
    def gke_cluster_pod_ip_range(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_cluster_pod_ip_range MwsWorkspaces#gke_cluster_pod_ip_range}.'''
        result = self._values.get("gke_cluster_pod_ip_range")
        assert result is not None, "Required property 'gke_cluster_pod_ip_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def gke_cluster_service_ip_range(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_cluster_service_ip_range MwsWorkspaces#gke_cluster_service_ip_range}.'''
        result = self._values.get("gke_cluster_service_ip_range")
        assert result is not None, "Required property 'gke_cluster_service_ip_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_cidr(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#subnet_cidr MwsWorkspaces#subnet_cidr}.'''
        result = self._values.get("subnet_cidr")
        assert result is not None, "Required property 'subnet_cidr' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesNetworkGcpManagedNetworkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsWorkspacesNetworkGcpManagedNetworkConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesNetworkGcpManagedNetworkConfigOutputReference",
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
            type_hints = typing.get_type_hints(MwsWorkspacesNetworkGcpManagedNetworkConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="gkeClusterPodIpRangeInput")
    def gke_cluster_pod_ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gkeClusterPodIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="gkeClusterServiceIpRangeInput")
    def gke_cluster_service_ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gkeClusterServiceIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetCidrInput")
    def subnet_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="gkeClusterPodIpRange")
    def gke_cluster_pod_ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gkeClusterPodIpRange"))

    @gke_cluster_pod_ip_range.setter
    def gke_cluster_pod_ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesNetworkGcpManagedNetworkConfigOutputReference, "gke_cluster_pod_ip_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gkeClusterPodIpRange", value)

    @builtins.property
    @jsii.member(jsii_name="gkeClusterServiceIpRange")
    def gke_cluster_service_ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gkeClusterServiceIpRange"))

    @gke_cluster_service_ip_range.setter
    def gke_cluster_service_ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesNetworkGcpManagedNetworkConfigOutputReference, "gke_cluster_service_ip_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gkeClusterServiceIpRange", value)

    @builtins.property
    @jsii.member(jsii_name="subnetCidr")
    def subnet_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetCidr"))

    @subnet_cidr.setter
    def subnet_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesNetworkGcpManagedNetworkConfigOutputReference, "subnet_cidr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetCidr", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MwsWorkspacesNetworkGcpManagedNetworkConfig]:
        return typing.cast(typing.Optional[MwsWorkspacesNetworkGcpManagedNetworkConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwsWorkspacesNetworkGcpManagedNetworkConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesNetworkGcpManagedNetworkConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MwsWorkspacesNetworkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesNetworkOutputReference",
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
            type_hints = typing.get_type_hints(MwsWorkspacesNetworkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGcpCommonNetworkConfig")
    def put_gcp_common_network_config(
        self,
        *,
        gke_cluster_master_ip_range: builtins.str,
        gke_connectivity_type: builtins.str,
    ) -> None:
        '''
        :param gke_cluster_master_ip_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_cluster_master_ip_range MwsWorkspaces#gke_cluster_master_ip_range}.
        :param gke_connectivity_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_connectivity_type MwsWorkspaces#gke_connectivity_type}.
        '''
        value = MwsWorkspacesNetworkGcpCommonNetworkConfig(
            gke_cluster_master_ip_range=gke_cluster_master_ip_range,
            gke_connectivity_type=gke_connectivity_type,
        )

        return typing.cast(None, jsii.invoke(self, "putGcpCommonNetworkConfig", [value]))

    @jsii.member(jsii_name="putGcpManagedNetworkConfig")
    def put_gcp_managed_network_config(
        self,
        *,
        gke_cluster_pod_ip_range: builtins.str,
        gke_cluster_service_ip_range: builtins.str,
        subnet_cidr: builtins.str,
    ) -> None:
        '''
        :param gke_cluster_pod_ip_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_cluster_pod_ip_range MwsWorkspaces#gke_cluster_pod_ip_range}.
        :param gke_cluster_service_ip_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_cluster_service_ip_range MwsWorkspaces#gke_cluster_service_ip_range}.
        :param subnet_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#subnet_cidr MwsWorkspaces#subnet_cidr}.
        '''
        value = MwsWorkspacesNetworkGcpManagedNetworkConfig(
            gke_cluster_pod_ip_range=gke_cluster_pod_ip_range,
            gke_cluster_service_ip_range=gke_cluster_service_ip_range,
            subnet_cidr=subnet_cidr,
        )

        return typing.cast(None, jsii.invoke(self, "putGcpManagedNetworkConfig", [value]))

    @jsii.member(jsii_name="resetGcpManagedNetworkConfig")
    def reset_gcp_managed_network_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpManagedNetworkConfig", []))

    @jsii.member(jsii_name="resetNetworkId")
    def reset_network_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkId", []))

    @builtins.property
    @jsii.member(jsii_name="gcpCommonNetworkConfig")
    def gcp_common_network_config(
        self,
    ) -> MwsWorkspacesNetworkGcpCommonNetworkConfigOutputReference:
        return typing.cast(MwsWorkspacesNetworkGcpCommonNetworkConfigOutputReference, jsii.get(self, "gcpCommonNetworkConfig"))

    @builtins.property
    @jsii.member(jsii_name="gcpManagedNetworkConfig")
    def gcp_managed_network_config(
        self,
    ) -> MwsWorkspacesNetworkGcpManagedNetworkConfigOutputReference:
        return typing.cast(MwsWorkspacesNetworkGcpManagedNetworkConfigOutputReference, jsii.get(self, "gcpManagedNetworkConfig"))

    @builtins.property
    @jsii.member(jsii_name="gcpCommonNetworkConfigInput")
    def gcp_common_network_config_input(
        self,
    ) -> typing.Optional[MwsWorkspacesNetworkGcpCommonNetworkConfig]:
        return typing.cast(typing.Optional[MwsWorkspacesNetworkGcpCommonNetworkConfig], jsii.get(self, "gcpCommonNetworkConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpManagedNetworkConfigInput")
    def gcp_managed_network_config_input(
        self,
    ) -> typing.Optional[MwsWorkspacesNetworkGcpManagedNetworkConfig]:
        return typing.cast(typing.Optional[MwsWorkspacesNetworkGcpManagedNetworkConfig], jsii.get(self, "gcpManagedNetworkConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="networkIdInput")
    def network_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="networkId")
    def network_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkId"))

    @network_id.setter
    def network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesNetworkOutputReference, "network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsWorkspacesNetwork]:
        return typing.cast(typing.Optional[MwsWorkspacesNetwork], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MwsWorkspacesNetwork]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesNetworkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "read": "read", "update": "update"},
)
class MwsWorkspacesTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#create MwsWorkspaces#create}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#read MwsWorkspaces#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#update MwsWorkspaces#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MwsWorkspacesTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#create MwsWorkspaces#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#read MwsWorkspaces#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#update MwsWorkspaces#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsWorkspacesTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MwsWorkspacesTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

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
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MwsWorkspacesTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MwsWorkspacesTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MwsWorkspacesTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesToken",
    jsii_struct_bases=[],
    name_mapping={
        "comment": "comment",
        "lifetime_seconds": "lifetimeSeconds",
        "token_id": "tokenId",
        "token_value": "tokenValue",
    },
)
class MwsWorkspacesToken:
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        lifetime_seconds: typing.Optional[jsii.Number] = None,
        token_id: typing.Optional[builtins.str] = None,
        token_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#comment MwsWorkspaces#comment}.
        :param lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#lifetime_seconds MwsWorkspaces#lifetime_seconds}.
        :param token_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token_id MwsWorkspaces#token_id}.
        :param token_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token_value MwsWorkspaces#token_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MwsWorkspacesToken.__init__)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument lifetime_seconds", value=lifetime_seconds, expected_type=type_hints["lifetime_seconds"])
            check_type(argname="argument token_id", value=token_id, expected_type=type_hints["token_id"])
            check_type(argname="argument token_value", value=token_value, expected_type=type_hints["token_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if lifetime_seconds is not None:
            self._values["lifetime_seconds"] = lifetime_seconds
        if token_id is not None:
            self._values["token_id"] = token_id
        if token_value is not None:
            self._values["token_value"] = token_value

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#comment MwsWorkspaces#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifetime_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#lifetime_seconds MwsWorkspaces#lifetime_seconds}.'''
        result = self._values.get("lifetime_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token_id MwsWorkspaces#token_id}.'''
        result = self._values.get("token_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token_value MwsWorkspaces#token_value}.'''
        result = self._values.get("token_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsWorkspacesTokenOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mwsWorkspaces.MwsWorkspacesTokenOutputReference",
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
            type_hints = typing.get_type_hints(MwsWorkspacesTokenOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetLifetimeSeconds")
    def reset_lifetime_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifetimeSeconds", []))

    @jsii.member(jsii_name="resetTokenId")
    def reset_token_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenId", []))

    @jsii.member(jsii_name="resetTokenValue")
    def reset_token_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenValue", []))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="lifetimeSecondsInput")
    def lifetime_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lifetimeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenIdInput")
    def token_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenValueInput")
    def token_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenValueInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesTokenOutputReference, "comment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="lifetimeSeconds")
    def lifetime_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lifetimeSeconds"))

    @lifetime_seconds.setter
    def lifetime_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesTokenOutputReference, "lifetime_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifetimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tokenId")
    def token_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenId"))

    @token_id.setter
    def token_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesTokenOutputReference, "token_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenId", value)

    @builtins.property
    @jsii.member(jsii_name="tokenValue")
    def token_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenValue"))

    @token_value.setter
    def token_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesTokenOutputReference, "token_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsWorkspacesToken]:
        return typing.cast(typing.Optional[MwsWorkspacesToken], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MwsWorkspacesToken]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsWorkspacesTokenOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MwsWorkspaces",
    "MwsWorkspacesCloudResourceBucket",
    "MwsWorkspacesCloudResourceBucketGcp",
    "MwsWorkspacesCloudResourceBucketGcpOutputReference",
    "MwsWorkspacesCloudResourceBucketOutputReference",
    "MwsWorkspacesConfig",
    "MwsWorkspacesExternalCustomerInfo",
    "MwsWorkspacesExternalCustomerInfoOutputReference",
    "MwsWorkspacesNetwork",
    "MwsWorkspacesNetworkGcpCommonNetworkConfig",
    "MwsWorkspacesNetworkGcpCommonNetworkConfigOutputReference",
    "MwsWorkspacesNetworkGcpManagedNetworkConfig",
    "MwsWorkspacesNetworkGcpManagedNetworkConfigOutputReference",
    "MwsWorkspacesNetworkOutputReference",
    "MwsWorkspacesTimeouts",
    "MwsWorkspacesTimeoutsOutputReference",
    "MwsWorkspacesToken",
    "MwsWorkspacesTokenOutputReference",
]

publication.publish()
