'''
# `snowflake_notification_integration`

Refer to the Terraform Registory for docs: [`snowflake_notification_integration`](https://www.terraform.io/docs/providers/snowflake/r/notification_integration).
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


class NotificationIntegration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.notificationIntegration.NotificationIntegration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration snowflake_notification_integration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        aws_sns_role_arn: typing.Optional[builtins.str] = None,
        aws_sns_topic_arn: typing.Optional[builtins.str] = None,
        aws_sqs_arn: typing.Optional[builtins.str] = None,
        aws_sqs_role_arn: typing.Optional[builtins.str] = None,
        azure_storage_queue_primary_uri: typing.Optional[builtins.str] = None,
        azure_tenant_id: typing.Optional[builtins.str] = None,
        comment: typing.Optional[builtins.str] = None,
        direction: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        gcp_pubsub_subscription_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        notification_provider: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration snowflake_notification_integration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#name NotificationIntegration#name}.
        :param aws_sns_role_arn: AWS IAM role ARN for notification integration to assume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#aws_sns_role_arn NotificationIntegration#aws_sns_role_arn}
        :param aws_sns_topic_arn: AWS SNS Topic ARN for notification integration to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#aws_sns_topic_arn NotificationIntegration#aws_sns_topic_arn}
        :param aws_sqs_arn: AWS SQS queue ARN for notification integration to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#aws_sqs_arn NotificationIntegration#aws_sqs_arn}
        :param aws_sqs_role_arn: AWS IAM role ARN for notification integration to assume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#aws_sqs_role_arn NotificationIntegration#aws_sqs_role_arn}
        :param azure_storage_queue_primary_uri: The queue ID for the Azure Queue Storage queue created for Event Grid notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#azure_storage_queue_primary_uri NotificationIntegration#azure_storage_queue_primary_uri}
        :param azure_tenant_id: The ID of the Azure Active Directory tenant used for identity management. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#azure_tenant_id NotificationIntegration#azure_tenant_id}
        :param comment: A comment for the integration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#comment NotificationIntegration#comment}
        :param direction: Direction of the cloud messaging with respect to Snowflake (required only for error notifications). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#direction NotificationIntegration#direction}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#enabled NotificationIntegration#enabled}.
        :param gcp_pubsub_subscription_name: The subscription id that Snowflake will listen to when using the GCP_PUBSUB provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#gcp_pubsub_subscription_name NotificationIntegration#gcp_pubsub_subscription_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#id NotificationIntegration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_provider: The third-party cloud message queuing service (e.g. AZURE_STORAGE_QUEUE, AWS_SQS, AWS_SNS). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#notification_provider NotificationIntegration#notification_provider}
        :param type: A type of integration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#type NotificationIntegration#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NotificationIntegration.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NotificationIntegrationConfig(
            name=name,
            aws_sns_role_arn=aws_sns_role_arn,
            aws_sns_topic_arn=aws_sns_topic_arn,
            aws_sqs_arn=aws_sqs_arn,
            aws_sqs_role_arn=aws_sqs_role_arn,
            azure_storage_queue_primary_uri=azure_storage_queue_primary_uri,
            azure_tenant_id=azure_tenant_id,
            comment=comment,
            direction=direction,
            enabled=enabled,
            gcp_pubsub_subscription_name=gcp_pubsub_subscription_name,
            id=id,
            notification_provider=notification_provider,
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

    @jsii.member(jsii_name="resetAwsSnsRoleArn")
    def reset_aws_sns_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsSnsRoleArn", []))

    @jsii.member(jsii_name="resetAwsSnsTopicArn")
    def reset_aws_sns_topic_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsSnsTopicArn", []))

    @jsii.member(jsii_name="resetAwsSqsArn")
    def reset_aws_sqs_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsSqsArn", []))

    @jsii.member(jsii_name="resetAwsSqsRoleArn")
    def reset_aws_sqs_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsSqsRoleArn", []))

    @jsii.member(jsii_name="resetAzureStorageQueuePrimaryUri")
    def reset_azure_storage_queue_primary_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureStorageQueuePrimaryUri", []))

    @jsii.member(jsii_name="resetAzureTenantId")
    def reset_azure_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureTenantId", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetDirection")
    def reset_direction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirection", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetGcpPubsubSubscriptionName")
    def reset_gcp_pubsub_subscription_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpPubsubSubscriptionName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNotificationProvider")
    def reset_notification_provider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationProvider", []))

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
    @jsii.member(jsii_name="awsSnsExternalId")
    def aws_sns_external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsSnsExternalId"))

    @builtins.property
    @jsii.member(jsii_name="awsSnsIamUserArn")
    def aws_sns_iam_user_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsSnsIamUserArn"))

    @builtins.property
    @jsii.member(jsii_name="awsSqsExternalId")
    def aws_sqs_external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsSqsExternalId"))

    @builtins.property
    @jsii.member(jsii_name="awsSqsIamUserArn")
    def aws_sqs_iam_user_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsSqsIamUserArn"))

    @builtins.property
    @jsii.member(jsii_name="createdOn")
    def created_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdOn"))

    @builtins.property
    @jsii.member(jsii_name="gcpPubsubServiceAccount")
    def gcp_pubsub_service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gcpPubsubServiceAccount"))

    @builtins.property
    @jsii.member(jsii_name="awsSnsRoleArnInput")
    def aws_sns_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsSnsRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="awsSnsTopicArnInput")
    def aws_sns_topic_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsSnsTopicArnInput"))

    @builtins.property
    @jsii.member(jsii_name="awsSqsArnInput")
    def aws_sqs_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsSqsArnInput"))

    @builtins.property
    @jsii.member(jsii_name="awsSqsRoleArnInput")
    def aws_sqs_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsSqsRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="azureStorageQueuePrimaryUriInput")
    def azure_storage_queue_primary_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureStorageQueuePrimaryUriInput"))

    @builtins.property
    @jsii.member(jsii_name="azureTenantIdInput")
    def azure_tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureTenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="directionInput")
    def direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpPubsubSubscriptionNameInput")
    def gcp_pubsub_subscription_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gcpPubsubSubscriptionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationProviderInput")
    def notification_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="awsSnsRoleArn")
    def aws_sns_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsSnsRoleArn"))

    @aws_sns_role_arn.setter
    def aws_sns_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationIntegration, "aws_sns_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsSnsRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="awsSnsTopicArn")
    def aws_sns_topic_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsSnsTopicArn"))

    @aws_sns_topic_arn.setter
    def aws_sns_topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationIntegration, "aws_sns_topic_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsSnsTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="awsSqsArn")
    def aws_sqs_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsSqsArn"))

    @aws_sqs_arn.setter
    def aws_sqs_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationIntegration, "aws_sqs_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsSqsArn", value)

    @builtins.property
    @jsii.member(jsii_name="awsSqsRoleArn")
    def aws_sqs_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsSqsRoleArn"))

    @aws_sqs_role_arn.setter
    def aws_sqs_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationIntegration, "aws_sqs_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsSqsRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="azureStorageQueuePrimaryUri")
    def azure_storage_queue_primary_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureStorageQueuePrimaryUri"))

    @azure_storage_queue_primary_uri.setter
    def azure_storage_queue_primary_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationIntegration, "azure_storage_queue_primary_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureStorageQueuePrimaryUri", value)

    @builtins.property
    @jsii.member(jsii_name="azureTenantId")
    def azure_tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureTenantId"))

    @azure_tenant_id.setter
    def azure_tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationIntegration, "azure_tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureTenantId", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationIntegration, "comment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "direction"))

    @direction.setter
    def direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationIntegration, "direction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "direction", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationIntegration, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="gcpPubsubSubscriptionName")
    def gcp_pubsub_subscription_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gcpPubsubSubscriptionName"))

    @gcp_pubsub_subscription_name.setter
    def gcp_pubsub_subscription_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationIntegration, "gcp_pubsub_subscription_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gcpPubsubSubscriptionName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationIntegration, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationIntegration, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notificationProvider")
    def notification_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationProvider"))

    @notification_provider.setter
    def notification_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationIntegration, "notification_provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationProvider", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationIntegration, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.notificationIntegration.NotificationIntegrationConfig",
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
        "aws_sns_role_arn": "awsSnsRoleArn",
        "aws_sns_topic_arn": "awsSnsTopicArn",
        "aws_sqs_arn": "awsSqsArn",
        "aws_sqs_role_arn": "awsSqsRoleArn",
        "azure_storage_queue_primary_uri": "azureStorageQueuePrimaryUri",
        "azure_tenant_id": "azureTenantId",
        "comment": "comment",
        "direction": "direction",
        "enabled": "enabled",
        "gcp_pubsub_subscription_name": "gcpPubsubSubscriptionName",
        "id": "id",
        "notification_provider": "notificationProvider",
        "type": "type",
    },
)
class NotificationIntegrationConfig(cdktf.TerraformMetaArguments):
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
        aws_sns_role_arn: typing.Optional[builtins.str] = None,
        aws_sns_topic_arn: typing.Optional[builtins.str] = None,
        aws_sqs_arn: typing.Optional[builtins.str] = None,
        aws_sqs_role_arn: typing.Optional[builtins.str] = None,
        azure_storage_queue_primary_uri: typing.Optional[builtins.str] = None,
        azure_tenant_id: typing.Optional[builtins.str] = None,
        comment: typing.Optional[builtins.str] = None,
        direction: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        gcp_pubsub_subscription_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        notification_provider: typing.Optional[builtins.str] = None,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#name NotificationIntegration#name}.
        :param aws_sns_role_arn: AWS IAM role ARN for notification integration to assume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#aws_sns_role_arn NotificationIntegration#aws_sns_role_arn}
        :param aws_sns_topic_arn: AWS SNS Topic ARN for notification integration to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#aws_sns_topic_arn NotificationIntegration#aws_sns_topic_arn}
        :param aws_sqs_arn: AWS SQS queue ARN for notification integration to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#aws_sqs_arn NotificationIntegration#aws_sqs_arn}
        :param aws_sqs_role_arn: AWS IAM role ARN for notification integration to assume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#aws_sqs_role_arn NotificationIntegration#aws_sqs_role_arn}
        :param azure_storage_queue_primary_uri: The queue ID for the Azure Queue Storage queue created for Event Grid notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#azure_storage_queue_primary_uri NotificationIntegration#azure_storage_queue_primary_uri}
        :param azure_tenant_id: The ID of the Azure Active Directory tenant used for identity management. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#azure_tenant_id NotificationIntegration#azure_tenant_id}
        :param comment: A comment for the integration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#comment NotificationIntegration#comment}
        :param direction: Direction of the cloud messaging with respect to Snowflake (required only for error notifications). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#direction NotificationIntegration#direction}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#enabled NotificationIntegration#enabled}.
        :param gcp_pubsub_subscription_name: The subscription id that Snowflake will listen to when using the GCP_PUBSUB provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#gcp_pubsub_subscription_name NotificationIntegration#gcp_pubsub_subscription_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#id NotificationIntegration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_provider: The third-party cloud message queuing service (e.g. AZURE_STORAGE_QUEUE, AWS_SQS, AWS_SNS). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#notification_provider NotificationIntegration#notification_provider}
        :param type: A type of integration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#type NotificationIntegration#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(NotificationIntegrationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument aws_sns_role_arn", value=aws_sns_role_arn, expected_type=type_hints["aws_sns_role_arn"])
            check_type(argname="argument aws_sns_topic_arn", value=aws_sns_topic_arn, expected_type=type_hints["aws_sns_topic_arn"])
            check_type(argname="argument aws_sqs_arn", value=aws_sqs_arn, expected_type=type_hints["aws_sqs_arn"])
            check_type(argname="argument aws_sqs_role_arn", value=aws_sqs_role_arn, expected_type=type_hints["aws_sqs_role_arn"])
            check_type(argname="argument azure_storage_queue_primary_uri", value=azure_storage_queue_primary_uri, expected_type=type_hints["azure_storage_queue_primary_uri"])
            check_type(argname="argument azure_tenant_id", value=azure_tenant_id, expected_type=type_hints["azure_tenant_id"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument direction", value=direction, expected_type=type_hints["direction"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument gcp_pubsub_subscription_name", value=gcp_pubsub_subscription_name, expected_type=type_hints["gcp_pubsub_subscription_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument notification_provider", value=notification_provider, expected_type=type_hints["notification_provider"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if aws_sns_role_arn is not None:
            self._values["aws_sns_role_arn"] = aws_sns_role_arn
        if aws_sns_topic_arn is not None:
            self._values["aws_sns_topic_arn"] = aws_sns_topic_arn
        if aws_sqs_arn is not None:
            self._values["aws_sqs_arn"] = aws_sqs_arn
        if aws_sqs_role_arn is not None:
            self._values["aws_sqs_role_arn"] = aws_sqs_role_arn
        if azure_storage_queue_primary_uri is not None:
            self._values["azure_storage_queue_primary_uri"] = azure_storage_queue_primary_uri
        if azure_tenant_id is not None:
            self._values["azure_tenant_id"] = azure_tenant_id
        if comment is not None:
            self._values["comment"] = comment
        if direction is not None:
            self._values["direction"] = direction
        if enabled is not None:
            self._values["enabled"] = enabled
        if gcp_pubsub_subscription_name is not None:
            self._values["gcp_pubsub_subscription_name"] = gcp_pubsub_subscription_name
        if id is not None:
            self._values["id"] = id
        if notification_provider is not None:
            self._values["notification_provider"] = notification_provider
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#name NotificationIntegration#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_sns_role_arn(self) -> typing.Optional[builtins.str]:
        '''AWS IAM role ARN for notification integration to assume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#aws_sns_role_arn NotificationIntegration#aws_sns_role_arn}
        '''
        result = self._values.get("aws_sns_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''AWS SNS Topic ARN for notification integration to connect to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#aws_sns_topic_arn NotificationIntegration#aws_sns_topic_arn}
        '''
        result = self._values.get("aws_sns_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_sqs_arn(self) -> typing.Optional[builtins.str]:
        '''AWS SQS queue ARN for notification integration to connect to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#aws_sqs_arn NotificationIntegration#aws_sqs_arn}
        '''
        result = self._values.get("aws_sqs_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_sqs_role_arn(self) -> typing.Optional[builtins.str]:
        '''AWS IAM role ARN for notification integration to assume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#aws_sqs_role_arn NotificationIntegration#aws_sqs_role_arn}
        '''
        result = self._values.get("aws_sqs_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_storage_queue_primary_uri(self) -> typing.Optional[builtins.str]:
        '''The queue ID for the Azure Queue Storage queue created for Event Grid notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#azure_storage_queue_primary_uri NotificationIntegration#azure_storage_queue_primary_uri}
        '''
        result = self._values.get("azure_storage_queue_primary_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_tenant_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the Azure Active Directory tenant used for identity management.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#azure_tenant_id NotificationIntegration#azure_tenant_id}
        '''
        result = self._values.get("azure_tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment for the integration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#comment NotificationIntegration#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def direction(self) -> typing.Optional[builtins.str]:
        '''Direction of the cloud messaging with respect to Snowflake (required only for error notifications).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#direction NotificationIntegration#direction}
        '''
        result = self._values.get("direction")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#enabled NotificationIntegration#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def gcp_pubsub_subscription_name(self) -> typing.Optional[builtins.str]:
        '''The subscription id that Snowflake will listen to when using the GCP_PUBSUB provider.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#gcp_pubsub_subscription_name NotificationIntegration#gcp_pubsub_subscription_name}
        '''
        result = self._values.get("gcp_pubsub_subscription_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#id NotificationIntegration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_provider(self) -> typing.Optional[builtins.str]:
        '''The third-party cloud message queuing service (e.g. AZURE_STORAGE_QUEUE, AWS_SQS, AWS_SNS).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#notification_provider NotificationIntegration#notification_provider}
        '''
        result = self._values.get("notification_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''A type of integration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/notification_integration#type NotificationIntegration#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationIntegrationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "NotificationIntegration",
    "NotificationIntegrationConfig",
]

publication.publish()
