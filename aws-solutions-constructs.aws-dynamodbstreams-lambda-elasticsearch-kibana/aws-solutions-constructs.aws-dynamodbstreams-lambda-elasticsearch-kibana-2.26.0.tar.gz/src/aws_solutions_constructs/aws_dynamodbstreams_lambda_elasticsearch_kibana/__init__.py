'''
# aws-dynamodbstreams-lambda-elasticsearch-kibana module

<!--BEGIN STABILITY BANNER-->---


![Stability: Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

> All classes are under active development and subject to non-backward compatible changes or removal in any
> future version. These are not subject to the [Semantic Versioning](https://semver.org/) model.
> This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

| **Reference Documentation**:| <span style="font-weight: normal">https://docs.aws.amazon.com/solutions/latest/constructs/</span>|
|:-------------|:-------------|

<div style="height:8px"></div>

| **Language**     | **Package**        |
|:-------------|-----------------|
|![Python Logo](https://docs.aws.amazon.com/cdk/api/latest/img/python32.png) Python|`aws_solutions_constructs.aws_dynamodbstreams_elasticsearch_kibana`|
|![Typescript Logo](https://docs.aws.amazon.com/cdk/api/latest/img/typescript32.png) Typescript|`@aws-solutions-constructs/aws-dynamodbstreams-lambda-elasticsearch-kibana`|
|![Java Logo](https://docs.aws.amazon.com/cdk/api/latest/img/java32.png) Java|`software.amazon.awsconstructs.services.dynamodbstreamslambdaelasticsearchkibana`|

## Overview

This AWS Solutions Construct implements Amazon DynamoDB table with stream, AWS Lambda function and Amazon Elasticsearch Service with the least privileged permissions.

**Some cluster configurations (e.g VPC access) require the existence of the `AWSServiceRoleForAmazonElasticsearchService` Service-Linked Role in your account.**

**You will need to create the service-linked role using the AWS CLI once in any account using this construct (it may have already been run to support other stacks):**

```
aws iam create-service-linked-role --aws-service-name es.amazonaws.com
```

Here is a minimal deployable pattern definition:

Typescript

```python
import { Construct } from 'constructs';
import { Stack, StackProps, Aws } from 'aws-cdk-lib';
import { DynamoDBStreamsToLambdaToElasticSearchAndKibana, DynamoDBStreamsToLambdaToElasticSearchAndKibanaProps } from '@aws-solutions-constructs/aws-dynamodbstreams-lambda-elasticsearch-kibana';
import * as lambda from 'aws-cdk-lib/aws-lambda';

const constructProps: DynamoDBStreamsToLambdaToElasticSearchAndKibanaProps = {
  lambdaFunctionProps: {
    code: lambda.Code.fromAsset(`lambda`),
    runtime: lambda.Runtime.NODEJS_14_X,
    handler: 'index.handler'
  },
  domainName: 'test-domain',
  // TODO: Ensure the Cognito domain name is globally unique
  cognitoDomainName: 'globallyuniquedomain' + Aws.ACCOUNT_ID
};

new DynamoDBStreamsToLambdaToElasticSearchAndKibana(this, 'test-dynamodbstreams-lambda-elasticsearch-kibana', constructProps);
```

Python

```Python
from aws_solutions_constructs.aws_dynamodbstreams_lambda_elasticsearch_kibana import DynamoDBStreamsToLambdaToElasticSearchAndKibana, DynamoDBStreamsToLambdaToElasticSearchAndKibanaProps
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    Aws,
)
from constructs import Construct

DynamoDBStreamsToLambdaToElasticSearchAndKibana(
    self, 'test-dynamodbstreams-lambda-elasticsearch-kibana',
    lambda_function_props=_lambda.FunctionProps(
        code=_lambda.Code.from_asset('lambda'),
        runtime=_lambda.Runtime.PYTHON_3_9,
        handler='index.handler'
    ),
    domain_name='test-domain',
    # TODO: Ensure the Cognito domain name is globally unique
    cognito_domain_name='globallyuniquedomain' + Aws.ACCOUNT_ID)
```

Java

```java
import software.constructs.Construct;

import software.amazon.awscdk.Aws;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awsconstructs.services.dynamodbstreamslambdaelasticsearchkibana.*;

new DynamoDBStreamsToLambdaToElasticSearchAndKibana(this, "test-dynamodb-stream-lambda-elasticsearch-kibana",
        new DynamoDBStreamsToLambdaToElasticSearchAndKibanaProps.Builder()
                .lambdaFunctionProps(new FunctionProps.Builder()
                        .runtime(Runtime.NODEJS_14_X)
                        .code(Code.fromAsset("lambda"))
                        .handler("index.handler")
                        .build())
                .domainName("test-domain")
                .cognitoDomainName("globallyuniquedomain" + Aws.ACCOUNT_ID)
                .build());
```

## Pattern Construct Props

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|existingLambdaObj?|[`lambda.Function`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)|Existing instance of Lambda Function object, providing both this and `lambdaFunctionProps` will cause an error.|
|lambdaFunctionProps?|[`lambda.FunctionProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.FunctionProps.html)|User provided props to override the default props for the Lambda function.|
|dynamoTableProps?|[`dynamodb.TableProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_dynamodb.TableProps.html)|Optional user provided props to override the default props for DynamoDB Table|
|existingTableInterface?|[`dynamodb.ITable`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_dynamodb.ITable.html)|Existing instance of DynamoDB table object or interface, providing both this and `dynamoTableProps` will cause an error.|
|dynamoEventSourceProps?|[`aws-lambda-event-sources.DynamoEventSourceProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda_event_sources.DynamoEventSourceProps.html)|Optional user provided props to override the default props for DynamoDB Event Source|
|esDomainProps?|[`elasticsearch.CfnDomainProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_elasticsearch.CfnDomainProps.html)|Optional user provided props to override the default props for the Elasticsearch Service|
|domainName|`string`|Domain name for the Cognito and the Elasticsearch Service|
|cognitoDomainName?|`string`|Optional Cognito Domain Name, if provided it will be used for Cognito Domain, and domainName will be used for the Elasticsearch Domain.|
|deploySqsDlqQueue?|`boolean`|Whether to deploy a SQS dead letter queue when a data record reaches the Maximum Retry Attempts or Maximum Record Age, its metadata like shard ID and stream ARN will be sent to an SQS queue.|
|sqsDlqQueueProps?|[`sqs.QueueProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.QueueProps.html)|Optional user provided properties for the SQS dead letter queue|
|createCloudWatchAlarms?|`boolean`|Whether to create recommended CloudWatch alarms|
| existingVpc? | [`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)|An existing VPC in which to deploy the construct. Providing both this and `vpcProps` is an error.|
| deployVpc? |`boolean`|Whether to create a new VPC based on `vpcProps` into which to deploy this pattern. Setting this to true will deploy the minimal, most private VPC to run the pattern:<ul><li> One isolated subnet in each Availability Zone used by the CDK program</li><li>`enableDnsHostnames` and `enableDnsSupport` will both be set to true</li></ul>If this property is `true` then `existingVpc` cannot be specified. Defaults to `false`.|
| vpcProps? |[`ec2.VpcProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.VpcProps.html)|Optional user-provided properties to override the default properties for the new VPC. `enableDnsHostnames`, `enableDnsSupport`, `natGateways` and `subnetConfiguration` are set by the Construct, so any values for those properties supplied here will be overrriden. If `deployVpc?` is not `true` then this property will be ignored. |

## Pattern Properties

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|dynamoTableInterface|[`dynamodb.ITable`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_dynamodb.ITable.html)|Returns an instance of dynamodb.ITable created by the construct|
|dynamoTable?|[`dynamodb.Table`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_dynamodb.Table.html)|Returns an instance of dynamodb.Table created by the construct. IMPORTANT: If existingTableInterface was provided in Pattern Construct Props, this property will be `undefined`|
|lambdaFunction|[`lambda.Function`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)|Returns an instance of lambda.Function created by the construct|
|userPool|[`cognito.UserPool`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cognito.UserPool.html)|Returns an instance of cognito.UserPool created by the construct|
|userPoolClient|[`cognito.UserPoolClient`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cognito.UserPoolClient.html)|Returns an instance of cognito.UserPoolClient created by the construct|
|identityPool|[`cognito.CfnIdentityPool`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cognito.CfnIdentityPool.html)|Returns an instance of cognito.CfnIdentityPool created by the construct|
|elasticsearchDomain|[`elasticsearch.CfnDomain`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_elasticsearch.CfnDomain.html)|Returns an instance of elasticsearch.CfnDomain created by the construct|
|elasticsearchDomain|[`iam.Role`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)|Returns an instance of iam.Role created by the construct for elasticsearch.CfnDomain|
|cloudwatchAlarms?|[`cloudwatch.Alarm[]`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html)|Returns a list of cloudwatch.Alarm created by the construct|
| vpc? |[`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)| Returns an instance of the VPC created by the pattern, if `deployVpc?` is `true`, or `existingVpc?` is provided.                 |

## Lambda Function

This pattern requires a lambda function that can post data into the Elasticsearch from DynamoDB stream. A sample function is provided [here](https://github.com/awslabs/aws-solutions-constructs/blob/master/source/patterns/%40aws-solutions-constructs/aws-dynamodbstreams-lambda-elasticsearch-kibana/test/lambda/index.js).

## Default settings

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon DynamoDB Table

* Set the billing mode for DynamoDB Table to On-Demand (Pay per request)
* Enable server-side encryption for DynamoDB Table using AWS managed KMS Key
* Creates a partition key called 'id' for DynamoDB Table
* Retain the Table when deleting the CloudFormation stack
* Enable continuous backups and point-in-time recovery

### AWS Lambda Function

* Configure limited privilege access IAM role for Lambda function
* Enable reusing connections with Keep-Alive for NodeJs Lambda function
* Enable X-Ray Tracing
* Enable Failure-Handling features like enable bisect on function Error, set defaults for Maximum Record Age (24 hours) & Maximum Retry Attempts (500) and deploy SQS dead-letter queue as destination on failure
* Set Environment Variables

  * AWS_NODEJS_CONNECTION_REUSE_ENABLED (for Node 10.x and higher functions)

### Amazon Cognito

* Set password policy for User Pools
* Enforce the advanced security mode for User Pools

### Amazon Elasticsearch Service

* Deploy best practices CloudWatch Alarms for the Elasticsearch Domain
* Secure the Kibana dashboard access with Cognito User Pools
* Enable server-side encryption for Elasticsearch Domain using AWS managed KMS Key
* Enable node-to-node encryption for Elasticsearch Domain
* Configure the cluster for the Amazon ES domain

## Architecture

![Architecture Diagram](architecture.png)

---


© Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

from ._jsii import *

import aws_cdk.aws_cloudwatch
import aws_cdk.aws_cognito
import aws_cdk.aws_dynamodb
import aws_cdk.aws_ec2
import aws_cdk.aws_elasticsearch
import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.aws_lambda_event_sources
import aws_cdk.aws_sqs
import constructs


class DynamoDBStreamsToLambdaToElasticSearchAndKibana(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-solutions-constructs/aws-dynamodbstreams-lambda-elasticsearch-kibana.DynamoDBStreamsToLambdaToElasticSearchAndKibana",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        cognito_domain_name: typing.Optional[builtins.str] = None,
        create_cloud_watch_alarms: typing.Optional[builtins.bool] = None,
        deploy_sqs_dlq_queue: typing.Optional[builtins.bool] = None,
        deploy_vpc: typing.Optional[builtins.bool] = None,
        dynamo_event_source_props: typing.Optional[typing.Union[aws_cdk.aws_lambda_event_sources.DynamoEventSourceProps, typing.Dict[str, typing.Any]]] = None,
        dynamo_table_props: typing.Optional[typing.Union[aws_cdk.aws_dynamodb.TableProps, typing.Dict[str, typing.Any]]] = None,
        es_domain_props: typing.Optional[typing.Union[aws_cdk.aws_elasticsearch.CfnDomainProps, typing.Dict[str, typing.Any]]] = None,
        existing_lambda_obj: typing.Optional[aws_cdk.aws_lambda.Function] = None,
        existing_table_interface: typing.Optional[aws_cdk.aws_dynamodb.ITable] = None,
        existing_vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        lambda_function_props: typing.Optional[typing.Union[aws_cdk.aws_lambda.FunctionProps, typing.Dict[str, typing.Any]]] = None,
        sqs_dlq_queue_props: typing.Optional[typing.Union[aws_cdk.aws_sqs.QueueProps, typing.Dict[str, typing.Any]]] = None,
        vpc_props: typing.Optional[typing.Union[aws_cdk.aws_ec2.VpcProps, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: - represents the scope for all the resources.
        :param id: - this is a a scope-unique id.
        :param domain_name: Cognito & ES Domain Name. Default: - None
        :param cognito_domain_name: Optional Cognito Domain Name, if provided it will be used for Cognito Domain, and domainName will be used for the Elasticsearch Domain. Default: - None
        :param create_cloud_watch_alarms: Whether to create recommended CloudWatch alarms. Default: - Alarms are created
        :param deploy_sqs_dlq_queue: Whether to deploy a SQS dead letter queue when a data record reaches the Maximum Retry Attempts or Maximum Record Age, its metadata like shard ID and stream ARN will be sent to an SQS queue. Default: - true.
        :param deploy_vpc: Whether to deploy a new VPC. Default: - false
        :param dynamo_event_source_props: Optional user provided props to override the default props. Default: - Default props are used
        :param dynamo_table_props: Optional user provided props to override the default props. Default: - Default props are used
        :param es_domain_props: Optional user provided props to override the default props for the API Gateway. Default: - Default props are used
        :param existing_lambda_obj: Existing instance of Lambda Function object, providing both this and ``lambdaFunctionProps`` will cause an error. Default: - None
        :param existing_table_interface: Existing instance of DynamoDB table object, providing both this and ``dynamoTableProps`` will cause an error. Default: - None
        :param existing_vpc: An existing VPC for the construct to use (construct will NOT create a new VPC in this case). Default: - None
        :param lambda_function_props: User provided props to override the default props for the Lambda function. Default: - Default props are used
        :param sqs_dlq_queue_props: Optional user provided properties for the SQS dead letter queue. Default: - Default props are used
        :param vpc_props: Properties to override default properties if deployVpc is true. Default: - DefaultIsolatedVpcProps() in vpc-defaults.ts

        :access: public
        :summary: Constructs a new instance of the LambdaToDynamoDB class.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DynamoDBStreamsToLambdaToElasticSearchAndKibana.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DynamoDBStreamsToLambdaToElasticSearchAndKibanaProps(
            domain_name=domain_name,
            cognito_domain_name=cognito_domain_name,
            create_cloud_watch_alarms=create_cloud_watch_alarms,
            deploy_sqs_dlq_queue=deploy_sqs_dlq_queue,
            deploy_vpc=deploy_vpc,
            dynamo_event_source_props=dynamo_event_source_props,
            dynamo_table_props=dynamo_table_props,
            es_domain_props=es_domain_props,
            existing_lambda_obj=existing_lambda_obj,
            existing_table_interface=existing_table_interface,
            existing_vpc=existing_vpc,
            lambda_function_props=lambda_function_props,
            sqs_dlq_queue_props=sqs_dlq_queue_props,
            vpc_props=vpc_props,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="dynamoTableInterface")
    def dynamo_table_interface(self) -> aws_cdk.aws_dynamodb.ITable:
        return typing.cast(aws_cdk.aws_dynamodb.ITable, jsii.get(self, "dynamoTableInterface"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchDomain")
    def elasticsearch_domain(self) -> aws_cdk.aws_elasticsearch.CfnDomain:
        return typing.cast(aws_cdk.aws_elasticsearch.CfnDomain, jsii.get(self, "elasticsearchDomain"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchRole")
    def elasticsearch_role(self) -> aws_cdk.aws_iam.Role:
        return typing.cast(aws_cdk.aws_iam.Role, jsii.get(self, "elasticsearchRole"))

    @builtins.property
    @jsii.member(jsii_name="identityPool")
    def identity_pool(self) -> aws_cdk.aws_cognito.CfnIdentityPool:
        return typing.cast(aws_cdk.aws_cognito.CfnIdentityPool, jsii.get(self, "identityPool"))

    @builtins.property
    @jsii.member(jsii_name="lambdaFunction")
    def lambda_function(self) -> aws_cdk.aws_lambda.Function:
        return typing.cast(aws_cdk.aws_lambda.Function, jsii.get(self, "lambdaFunction"))

    @builtins.property
    @jsii.member(jsii_name="userPool")
    def user_pool(self) -> aws_cdk.aws_cognito.UserPool:
        return typing.cast(aws_cdk.aws_cognito.UserPool, jsii.get(self, "userPool"))

    @builtins.property
    @jsii.member(jsii_name="userPoolClient")
    def user_pool_client(self) -> aws_cdk.aws_cognito.UserPoolClient:
        return typing.cast(aws_cdk.aws_cognito.UserPoolClient, jsii.get(self, "userPoolClient"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchAlarms")
    def cloudwatch_alarms(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_cloudwatch.Alarm]]:
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_cloudwatch.Alarm]], jsii.get(self, "cloudwatchAlarms"))

    @builtins.property
    @jsii.member(jsii_name="dynamoTable")
    def dynamo_table(self) -> typing.Optional[aws_cdk.aws_dynamodb.Table]:
        return typing.cast(typing.Optional[aws_cdk.aws_dynamodb.Table], jsii.get(self, "dynamoTable"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], jsii.get(self, "vpc"))


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/aws-dynamodbstreams-lambda-elasticsearch-kibana.DynamoDBStreamsToLambdaToElasticSearchAndKibanaProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "cognito_domain_name": "cognitoDomainName",
        "create_cloud_watch_alarms": "createCloudWatchAlarms",
        "deploy_sqs_dlq_queue": "deploySqsDlqQueue",
        "deploy_vpc": "deployVpc",
        "dynamo_event_source_props": "dynamoEventSourceProps",
        "dynamo_table_props": "dynamoTableProps",
        "es_domain_props": "esDomainProps",
        "existing_lambda_obj": "existingLambdaObj",
        "existing_table_interface": "existingTableInterface",
        "existing_vpc": "existingVpc",
        "lambda_function_props": "lambdaFunctionProps",
        "sqs_dlq_queue_props": "sqsDlqQueueProps",
        "vpc_props": "vpcProps",
    },
)
class DynamoDBStreamsToLambdaToElasticSearchAndKibanaProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        cognito_domain_name: typing.Optional[builtins.str] = None,
        create_cloud_watch_alarms: typing.Optional[builtins.bool] = None,
        deploy_sqs_dlq_queue: typing.Optional[builtins.bool] = None,
        deploy_vpc: typing.Optional[builtins.bool] = None,
        dynamo_event_source_props: typing.Optional[typing.Union[aws_cdk.aws_lambda_event_sources.DynamoEventSourceProps, typing.Dict[str, typing.Any]]] = None,
        dynamo_table_props: typing.Optional[typing.Union[aws_cdk.aws_dynamodb.TableProps, typing.Dict[str, typing.Any]]] = None,
        es_domain_props: typing.Optional[typing.Union[aws_cdk.aws_elasticsearch.CfnDomainProps, typing.Dict[str, typing.Any]]] = None,
        existing_lambda_obj: typing.Optional[aws_cdk.aws_lambda.Function] = None,
        existing_table_interface: typing.Optional[aws_cdk.aws_dynamodb.ITable] = None,
        existing_vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        lambda_function_props: typing.Optional[typing.Union[aws_cdk.aws_lambda.FunctionProps, typing.Dict[str, typing.Any]]] = None,
        sqs_dlq_queue_props: typing.Optional[typing.Union[aws_cdk.aws_sqs.QueueProps, typing.Dict[str, typing.Any]]] = None,
        vpc_props: typing.Optional[typing.Union[aws_cdk.aws_ec2.VpcProps, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param domain_name: Cognito & ES Domain Name. Default: - None
        :param cognito_domain_name: Optional Cognito Domain Name, if provided it will be used for Cognito Domain, and domainName will be used for the Elasticsearch Domain. Default: - None
        :param create_cloud_watch_alarms: Whether to create recommended CloudWatch alarms. Default: - Alarms are created
        :param deploy_sqs_dlq_queue: Whether to deploy a SQS dead letter queue when a data record reaches the Maximum Retry Attempts or Maximum Record Age, its metadata like shard ID and stream ARN will be sent to an SQS queue. Default: - true.
        :param deploy_vpc: Whether to deploy a new VPC. Default: - false
        :param dynamo_event_source_props: Optional user provided props to override the default props. Default: - Default props are used
        :param dynamo_table_props: Optional user provided props to override the default props. Default: - Default props are used
        :param es_domain_props: Optional user provided props to override the default props for the API Gateway. Default: - Default props are used
        :param existing_lambda_obj: Existing instance of Lambda Function object, providing both this and ``lambdaFunctionProps`` will cause an error. Default: - None
        :param existing_table_interface: Existing instance of DynamoDB table object, providing both this and ``dynamoTableProps`` will cause an error. Default: - None
        :param existing_vpc: An existing VPC for the construct to use (construct will NOT create a new VPC in this case). Default: - None
        :param lambda_function_props: User provided props to override the default props for the Lambda function. Default: - Default props are used
        :param sqs_dlq_queue_props: Optional user provided properties for the SQS dead letter queue. Default: - Default props are used
        :param vpc_props: Properties to override default properties if deployVpc is true. Default: - DefaultIsolatedVpcProps() in vpc-defaults.ts

        :summary: The properties for the DynamoDBStreamsToLambdaToElastciSearchAndKibana Construct
        '''
        if isinstance(dynamo_event_source_props, dict):
            dynamo_event_source_props = aws_cdk.aws_lambda_event_sources.DynamoEventSourceProps(**dynamo_event_source_props)
        if isinstance(dynamo_table_props, dict):
            dynamo_table_props = aws_cdk.aws_dynamodb.TableProps(**dynamo_table_props)
        if isinstance(es_domain_props, dict):
            es_domain_props = aws_cdk.aws_elasticsearch.CfnDomainProps(**es_domain_props)
        if isinstance(lambda_function_props, dict):
            lambda_function_props = aws_cdk.aws_lambda.FunctionProps(**lambda_function_props)
        if isinstance(sqs_dlq_queue_props, dict):
            sqs_dlq_queue_props = aws_cdk.aws_sqs.QueueProps(**sqs_dlq_queue_props)
        if isinstance(vpc_props, dict):
            vpc_props = aws_cdk.aws_ec2.VpcProps(**vpc_props)
        if __debug__:
            type_hints = typing.get_type_hints(DynamoDBStreamsToLambdaToElasticSearchAndKibanaProps.__init__)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument cognito_domain_name", value=cognito_domain_name, expected_type=type_hints["cognito_domain_name"])
            check_type(argname="argument create_cloud_watch_alarms", value=create_cloud_watch_alarms, expected_type=type_hints["create_cloud_watch_alarms"])
            check_type(argname="argument deploy_sqs_dlq_queue", value=deploy_sqs_dlq_queue, expected_type=type_hints["deploy_sqs_dlq_queue"])
            check_type(argname="argument deploy_vpc", value=deploy_vpc, expected_type=type_hints["deploy_vpc"])
            check_type(argname="argument dynamo_event_source_props", value=dynamo_event_source_props, expected_type=type_hints["dynamo_event_source_props"])
            check_type(argname="argument dynamo_table_props", value=dynamo_table_props, expected_type=type_hints["dynamo_table_props"])
            check_type(argname="argument es_domain_props", value=es_domain_props, expected_type=type_hints["es_domain_props"])
            check_type(argname="argument existing_lambda_obj", value=existing_lambda_obj, expected_type=type_hints["existing_lambda_obj"])
            check_type(argname="argument existing_table_interface", value=existing_table_interface, expected_type=type_hints["existing_table_interface"])
            check_type(argname="argument existing_vpc", value=existing_vpc, expected_type=type_hints["existing_vpc"])
            check_type(argname="argument lambda_function_props", value=lambda_function_props, expected_type=type_hints["lambda_function_props"])
            check_type(argname="argument sqs_dlq_queue_props", value=sqs_dlq_queue_props, expected_type=type_hints["sqs_dlq_queue_props"])
            check_type(argname="argument vpc_props", value=vpc_props, expected_type=type_hints["vpc_props"])
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
        }
        if cognito_domain_name is not None:
            self._values["cognito_domain_name"] = cognito_domain_name
        if create_cloud_watch_alarms is not None:
            self._values["create_cloud_watch_alarms"] = create_cloud_watch_alarms
        if deploy_sqs_dlq_queue is not None:
            self._values["deploy_sqs_dlq_queue"] = deploy_sqs_dlq_queue
        if deploy_vpc is not None:
            self._values["deploy_vpc"] = deploy_vpc
        if dynamo_event_source_props is not None:
            self._values["dynamo_event_source_props"] = dynamo_event_source_props
        if dynamo_table_props is not None:
            self._values["dynamo_table_props"] = dynamo_table_props
        if es_domain_props is not None:
            self._values["es_domain_props"] = es_domain_props
        if existing_lambda_obj is not None:
            self._values["existing_lambda_obj"] = existing_lambda_obj
        if existing_table_interface is not None:
            self._values["existing_table_interface"] = existing_table_interface
        if existing_vpc is not None:
            self._values["existing_vpc"] = existing_vpc
        if lambda_function_props is not None:
            self._values["lambda_function_props"] = lambda_function_props
        if sqs_dlq_queue_props is not None:
            self._values["sqs_dlq_queue_props"] = sqs_dlq_queue_props
        if vpc_props is not None:
            self._values["vpc_props"] = vpc_props

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Cognito & ES Domain Name.

        :default: - None
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cognito_domain_name(self) -> typing.Optional[builtins.str]:
        '''Optional Cognito Domain Name, if provided it will be used for Cognito Domain, and domainName will be used for the Elasticsearch Domain.

        :default: - None
        '''
        result = self._values.get("cognito_domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def create_cloud_watch_alarms(self) -> typing.Optional[builtins.bool]:
        '''Whether to create recommended CloudWatch alarms.

        :default: - Alarms are created
        '''
        result = self._values.get("create_cloud_watch_alarms")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def deploy_sqs_dlq_queue(self) -> typing.Optional[builtins.bool]:
        '''Whether to deploy a SQS dead letter queue when a data record reaches the Maximum Retry Attempts or Maximum Record Age, its metadata like shard ID and stream ARN will be sent to an SQS queue.

        :default: - true.
        '''
        result = self._values.get("deploy_sqs_dlq_queue")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def deploy_vpc(self) -> typing.Optional[builtins.bool]:
        '''Whether to deploy a new VPC.

        :default: - false
        '''
        result = self._values.get("deploy_vpc")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def dynamo_event_source_props(
        self,
    ) -> typing.Optional[aws_cdk.aws_lambda_event_sources.DynamoEventSourceProps]:
        '''Optional user provided props to override the default props.

        :default: - Default props are used
        '''
        result = self._values.get("dynamo_event_source_props")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda_event_sources.DynamoEventSourceProps], result)

    @builtins.property
    def dynamo_table_props(self) -> typing.Optional[aws_cdk.aws_dynamodb.TableProps]:
        '''Optional user provided props to override the default props.

        :default: - Default props are used
        '''
        result = self._values.get("dynamo_table_props")
        return typing.cast(typing.Optional[aws_cdk.aws_dynamodb.TableProps], result)

    @builtins.property
    def es_domain_props(
        self,
    ) -> typing.Optional[aws_cdk.aws_elasticsearch.CfnDomainProps]:
        '''Optional user provided props to override the default props for the API Gateway.

        :default: - Default props are used
        '''
        result = self._values.get("es_domain_props")
        return typing.cast(typing.Optional[aws_cdk.aws_elasticsearch.CfnDomainProps], result)

    @builtins.property
    def existing_lambda_obj(self) -> typing.Optional[aws_cdk.aws_lambda.Function]:
        '''Existing instance of Lambda Function object, providing both this and ``lambdaFunctionProps`` will cause an error.

        :default: - None
        '''
        result = self._values.get("existing_lambda_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.Function], result)

    @builtins.property
    def existing_table_interface(self) -> typing.Optional[aws_cdk.aws_dynamodb.ITable]:
        '''Existing instance of DynamoDB table object, providing both this and ``dynamoTableProps`` will cause an error.

        :default: - None
        '''
        result = self._values.get("existing_table_interface")
        return typing.cast(typing.Optional[aws_cdk.aws_dynamodb.ITable], result)

    @builtins.property
    def existing_vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''An existing VPC for the construct to use (construct will NOT create a new VPC in this case).

        :default: - None
        '''
        result = self._values.get("existing_vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    @builtins.property
    def lambda_function_props(
        self,
    ) -> typing.Optional[aws_cdk.aws_lambda.FunctionProps]:
        '''User provided props to override the default props for the Lambda function.

        :default: - Default props are used
        '''
        result = self._values.get("lambda_function_props")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.FunctionProps], result)

    @builtins.property
    def sqs_dlq_queue_props(self) -> typing.Optional[aws_cdk.aws_sqs.QueueProps]:
        '''Optional user provided properties for the SQS dead letter queue.

        :default: - Default props are used
        '''
        result = self._values.get("sqs_dlq_queue_props")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.QueueProps], result)

    @builtins.property
    def vpc_props(self) -> typing.Optional[aws_cdk.aws_ec2.VpcProps]:
        '''Properties to override default properties if deployVpc is true.

        :default: - DefaultIsolatedVpcProps() in vpc-defaults.ts
        '''
        result = self._values.get("vpc_props")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.VpcProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamoDBStreamsToLambdaToElasticSearchAndKibanaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DynamoDBStreamsToLambdaToElasticSearchAndKibana",
    "DynamoDBStreamsToLambdaToElasticSearchAndKibanaProps",
]

publication.publish()
