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

import aws_cdk
import constructs
from ..ec2 import FlowLogFormat as _FlowLogFormat_b7c2ba34
from ..glue import Database as _Database_5971ae38
from ..s3_buckets import (
    AlbLogsBucket as _AlbLogsBucket_93df9b00,
    CloudfrontLogsBucket as _CloudfrontLogsBucket_34407447,
    CloudtrailBucket as _CloudtrailBucket_aa5784e2,
    FlowLogsBucket as _FlowLogsBucket_2af17beb,
    S3AccessLogsBucket as _S3AccessLogsBucket_c740f099,
    SesLogsBucket as _SesLogsBucket_bc9a3d3a,
    WafLogsBucket as _WafLogsBucket_0ad870de,
)


class AwsLoggingStack(
    aws_cdk.Stack,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-extensions.stacks.AwsLoggingStack",
):
    '''Creates a demo web service running in Fargate that is accessible through an application load balancer.

    The demo service serves a generic "Welcome to nginx" page.

    The service can be accessed remotely using ECS Exec. For details see the documentation at:
    https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html#ecs-exec-running-commands
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        alb_logs_bucket: typing.Optional[_AlbLogsBucket_93df9b00] = None,
        cloudfront_logs_bucket: typing.Optional[_CloudfrontLogsBucket_34407447] = None,
        cloudtrail_logs_bucket: typing.Optional[_CloudtrailBucket_aa5784e2] = None,
        database_name: typing.Optional[builtins.str] = None,
        flow_logs_bucket: typing.Optional[_FlowLogsBucket_2af17beb] = None,
        flow_logs_format: typing.Optional[_FlowLogFormat_b7c2ba34] = None,
        friendly_query_names: typing.Optional[builtins.bool] = None,
        ses_logs_bucket: typing.Optional[_SesLogsBucket_bc9a3d3a] = None,
        standardize_names: typing.Optional[builtins.bool] = None,
        waf_logs_bucket: typing.Optional[_WafLogsBucket_0ad870de] = None,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Union[aws_cdk.Environment, typing.Dict[str, typing.Any]]] = None,
        stack_name: typing.Optional[builtins.str] = None,
        synthesizer: typing.Optional[aws_cdk.IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param alb_logs_bucket: 
        :param cloudfront_logs_bucket: 
        :param cloudtrail_logs_bucket: 
        :param database_name: 
        :param flow_logs_bucket: 
        :param flow_logs_format: 
        :param friendly_query_names: 
        :param ses_logs_bucket: 
        :param standardize_names: 
        :param waf_logs_bucket: 
        :param analytics_reporting: Include runtime versioning information in this Stack. Default: ``analyticsReporting`` setting of containing ``App``, or value of 'aws:cdk:version-reporting' context key
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param synthesizer: Synthesis method to use while deploying this stack. Default: - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag is set, ``LegacyStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AwsLoggingStack.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AwsLoggingStackProps(
            alb_logs_bucket=alb_logs_bucket,
            cloudfront_logs_bucket=cloudfront_logs_bucket,
            cloudtrail_logs_bucket=cloudtrail_logs_bucket,
            database_name=database_name,
            flow_logs_bucket=flow_logs_bucket,
            flow_logs_format=flow_logs_format,
            friendly_query_names=friendly_query_names,
            ses_logs_bucket=ses_logs_bucket,
            standardize_names=standardize_names,
            waf_logs_bucket=waf_logs_bucket,
            analytics_reporting=analytics_reporting,
            description=description,
            env=env,
            stack_name=stack_name,
            synthesizer=synthesizer,
            tags=tags,
            termination_protection=termination_protection,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="albLogsBucket")
    def alb_logs_bucket(self) -> _AlbLogsBucket_93df9b00:
        return typing.cast(_AlbLogsBucket_93df9b00, jsii.get(self, "albLogsBucket"))

    @builtins.property
    @jsii.member(jsii_name="cloudfrontLogsBucket")
    def cloudfront_logs_bucket(self) -> _CloudfrontLogsBucket_34407447:
        return typing.cast(_CloudfrontLogsBucket_34407447, jsii.get(self, "cloudfrontLogsBucket"))

    @builtins.property
    @jsii.member(jsii_name="cloudtrailLogsBucket")
    def cloudtrail_logs_bucket(self) -> _CloudtrailBucket_aa5784e2:
        return typing.cast(_CloudtrailBucket_aa5784e2, jsii.get(self, "cloudtrailLogsBucket"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> _Database_5971ae38:
        return typing.cast(_Database_5971ae38, jsii.get(self, "database"))

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @builtins.property
    @jsii.member(jsii_name="flowLogsBucket")
    def flow_logs_bucket(self) -> _FlowLogsBucket_2af17beb:
        return typing.cast(_FlowLogsBucket_2af17beb, jsii.get(self, "flowLogsBucket"))

    @builtins.property
    @jsii.member(jsii_name="flowLogsFormat")
    def flow_logs_format(self) -> _FlowLogFormat_b7c2ba34:
        return typing.cast(_FlowLogFormat_b7c2ba34, jsii.get(self, "flowLogsFormat"))

    @builtins.property
    @jsii.member(jsii_name="s3AccessLogsBucket")
    def s3_access_logs_bucket(self) -> _S3AccessLogsBucket_c740f099:
        return typing.cast(_S3AccessLogsBucket_c740f099, jsii.get(self, "s3AccessLogsBucket"))

    @builtins.property
    @jsii.member(jsii_name="sesLogsBucket")
    def ses_logs_bucket(self) -> _SesLogsBucket_bc9a3d3a:
        return typing.cast(_SesLogsBucket_bc9a3d3a, jsii.get(self, "sesLogsBucket"))

    @builtins.property
    @jsii.member(jsii_name="standardizeNames")
    def standardize_names(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "standardizeNames"))

    @builtins.property
    @jsii.member(jsii_name="wafLogsBucket")
    def waf_logs_bucket(self) -> _WafLogsBucket_0ad870de:
        return typing.cast(_WafLogsBucket_0ad870de, jsii.get(self, "wafLogsBucket"))

    @builtins.property
    @jsii.member(jsii_name="friendlyQueryNames")
    def friendly_query_names(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "friendlyQueryNames"))


@jsii.data_type(
    jsii_type="cdk-extensions.stacks.AwsLoggingStackProps",
    jsii_struct_bases=[aws_cdk.StackProps],
    name_mapping={
        "analytics_reporting": "analyticsReporting",
        "description": "description",
        "env": "env",
        "stack_name": "stackName",
        "synthesizer": "synthesizer",
        "tags": "tags",
        "termination_protection": "terminationProtection",
        "alb_logs_bucket": "albLogsBucket",
        "cloudfront_logs_bucket": "cloudfrontLogsBucket",
        "cloudtrail_logs_bucket": "cloudtrailLogsBucket",
        "database_name": "databaseName",
        "flow_logs_bucket": "flowLogsBucket",
        "flow_logs_format": "flowLogsFormat",
        "friendly_query_names": "friendlyQueryNames",
        "ses_logs_bucket": "sesLogsBucket",
        "standardize_names": "standardizeNames",
        "waf_logs_bucket": "wafLogsBucket",
    },
)
class AwsLoggingStackProps(aws_cdk.StackProps):
    def __init__(
        self,
        *,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Union[aws_cdk.Environment, typing.Dict[str, typing.Any]]] = None,
        stack_name: typing.Optional[builtins.str] = None,
        synthesizer: typing.Optional[aws_cdk.IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
        alb_logs_bucket: typing.Optional[_AlbLogsBucket_93df9b00] = None,
        cloudfront_logs_bucket: typing.Optional[_CloudfrontLogsBucket_34407447] = None,
        cloudtrail_logs_bucket: typing.Optional[_CloudtrailBucket_aa5784e2] = None,
        database_name: typing.Optional[builtins.str] = None,
        flow_logs_bucket: typing.Optional[_FlowLogsBucket_2af17beb] = None,
        flow_logs_format: typing.Optional[_FlowLogFormat_b7c2ba34] = None,
        friendly_query_names: typing.Optional[builtins.bool] = None,
        ses_logs_bucket: typing.Optional[_SesLogsBucket_bc9a3d3a] = None,
        standardize_names: typing.Optional[builtins.bool] = None,
        waf_logs_bucket: typing.Optional[_WafLogsBucket_0ad870de] = None,
    ) -> None:
        '''Configuration for the demo service stack.

        :param analytics_reporting: Include runtime versioning information in this Stack. Default: ``analyticsReporting`` setting of containing ``App``, or value of 'aws:cdk:version-reporting' context key
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param synthesizer: Synthesis method to use while deploying this stack. Default: - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag is set, ``LegacyStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false
        :param alb_logs_bucket: 
        :param cloudfront_logs_bucket: 
        :param cloudtrail_logs_bucket: 
        :param database_name: 
        :param flow_logs_bucket: 
        :param flow_logs_format: 
        :param friendly_query_names: 
        :param ses_logs_bucket: 
        :param standardize_names: 
        :param waf_logs_bucket: 
        '''
        if isinstance(env, dict):
            env = aws_cdk.Environment(**env)
        if __debug__:
            type_hints = typing.get_type_hints(AwsLoggingStackProps.__init__)
            check_type(argname="argument analytics_reporting", value=analytics_reporting, expected_type=type_hints["analytics_reporting"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument stack_name", value=stack_name, expected_type=type_hints["stack_name"])
            check_type(argname="argument synthesizer", value=synthesizer, expected_type=type_hints["synthesizer"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument termination_protection", value=termination_protection, expected_type=type_hints["termination_protection"])
            check_type(argname="argument alb_logs_bucket", value=alb_logs_bucket, expected_type=type_hints["alb_logs_bucket"])
            check_type(argname="argument cloudfront_logs_bucket", value=cloudfront_logs_bucket, expected_type=type_hints["cloudfront_logs_bucket"])
            check_type(argname="argument cloudtrail_logs_bucket", value=cloudtrail_logs_bucket, expected_type=type_hints["cloudtrail_logs_bucket"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument flow_logs_bucket", value=flow_logs_bucket, expected_type=type_hints["flow_logs_bucket"])
            check_type(argname="argument flow_logs_format", value=flow_logs_format, expected_type=type_hints["flow_logs_format"])
            check_type(argname="argument friendly_query_names", value=friendly_query_names, expected_type=type_hints["friendly_query_names"])
            check_type(argname="argument ses_logs_bucket", value=ses_logs_bucket, expected_type=type_hints["ses_logs_bucket"])
            check_type(argname="argument standardize_names", value=standardize_names, expected_type=type_hints["standardize_names"])
            check_type(argname="argument waf_logs_bucket", value=waf_logs_bucket, expected_type=type_hints["waf_logs_bucket"])
        self._values: typing.Dict[str, typing.Any] = {}
        if analytics_reporting is not None:
            self._values["analytics_reporting"] = analytics_reporting
        if description is not None:
            self._values["description"] = description
        if env is not None:
            self._values["env"] = env
        if stack_name is not None:
            self._values["stack_name"] = stack_name
        if synthesizer is not None:
            self._values["synthesizer"] = synthesizer
        if tags is not None:
            self._values["tags"] = tags
        if termination_protection is not None:
            self._values["termination_protection"] = termination_protection
        if alb_logs_bucket is not None:
            self._values["alb_logs_bucket"] = alb_logs_bucket
        if cloudfront_logs_bucket is not None:
            self._values["cloudfront_logs_bucket"] = cloudfront_logs_bucket
        if cloudtrail_logs_bucket is not None:
            self._values["cloudtrail_logs_bucket"] = cloudtrail_logs_bucket
        if database_name is not None:
            self._values["database_name"] = database_name
        if flow_logs_bucket is not None:
            self._values["flow_logs_bucket"] = flow_logs_bucket
        if flow_logs_format is not None:
            self._values["flow_logs_format"] = flow_logs_format
        if friendly_query_names is not None:
            self._values["friendly_query_names"] = friendly_query_names
        if ses_logs_bucket is not None:
            self._values["ses_logs_bucket"] = ses_logs_bucket
        if standardize_names is not None:
            self._values["standardize_names"] = standardize_names
        if waf_logs_bucket is not None:
            self._values["waf_logs_bucket"] = waf_logs_bucket

    @builtins.property
    def analytics_reporting(self) -> typing.Optional[builtins.bool]:
        '''Include runtime versioning information in this Stack.

        :default:

        ``analyticsReporting`` setting of containing ``App``, or value of
        'aws:cdk:version-reporting' context key
        '''
        result = self._values.get("analytics_reporting")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the stack.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def env(self) -> typing.Optional[aws_cdk.Environment]:
        '''The AWS environment (account/region) where this stack will be deployed.

        Set the ``region``/``account`` fields of ``env`` to either a concrete value to
        select the indicated environment (recommended for production stacks), or to
        the values of environment variables
        ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment
        depend on the AWS credentials/configuration that the CDK CLI is executed
        under (recommended for development stacks).

        If the ``Stack`` is instantiated inside a ``Stage``, any undefined
        ``region``/``account`` fields from ``env`` will default to the same field on the
        encompassing ``Stage``, if configured there.

        If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the
        Stack will be considered "*environment-agnostic*"". Environment-agnostic
        stacks can be deployed to any environment but may not be able to take
        advantage of all features of the CDK. For example, they will not be able to
        use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not
        automatically translate Service Principals to the right format based on the
        environment's AWS partition, and other such enhancements.

        :default:

        - The environment of the containing ``Stage`` if available,
        otherwise create the stack will be environment-agnostic.

        Example::

            // Use a concrete account and region to deploy this stack to:
            // `.account` and `.region` will simply return these values.
            new Stack(app, 'Stack1', {
              env: {
                account: '123456789012',
                region: 'us-east-1'
              },
            });
            
            // Use the CLI's current credentials to determine the target environment:
            // `.account` and `.region` will reflect the account+region the CLI
            // is configured to use (based on the user CLI credentials)
            new Stack(app, 'Stack2', {
              env: {
                account: process.env.CDK_DEFAULT_ACCOUNT,
                region: process.env.CDK_DEFAULT_REGION
              },
            });
            
            // Define multiple stacks stage associated with an environment
            const myStage = new Stage(app, 'MyStage', {
              env: {
                account: '123456789012',
                region: 'us-east-1'
              }
            });
            
            // both of these stacks will use the stage's account/region:
            // `.account` and `.region` will resolve to the concrete values as above
            new MyStack(myStage, 'Stack1');
            new YourStack(myStage, 'Stack2');
            
            // Define an environment-agnostic stack:
            // `.account` and `.region` will resolve to `{ "Ref": "AWS::AccountId" }` and `{ "Ref": "AWS::Region" }` respectively.
            // which will only resolve to actual values by CloudFormation during deployment.
            new MyStack(app, 'Stack1');
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[aws_cdk.Environment], result)

    @builtins.property
    def stack_name(self) -> typing.Optional[builtins.str]:
        '''Name to deploy the stack with.

        :default: - Derived from construct path.
        '''
        result = self._values.get("stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def synthesizer(self) -> typing.Optional[aws_cdk.IStackSynthesizer]:
        '''Synthesis method to use while deploying this stack.

        :default:

        - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag
        is set, ``LegacyStackSynthesizer`` otherwise.
        '''
        result = self._values.get("synthesizer")
        return typing.cast(typing.Optional[aws_cdk.IStackSynthesizer], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Stack tags that will be applied to all the taggable resources and the stack itself.

        :default: {}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def termination_protection(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable termination protection for this stack.

        :default: false
        '''
        result = self._values.get("termination_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def alb_logs_bucket(self) -> typing.Optional[_AlbLogsBucket_93df9b00]:
        result = self._values.get("alb_logs_bucket")
        return typing.cast(typing.Optional[_AlbLogsBucket_93df9b00], result)

    @builtins.property
    def cloudfront_logs_bucket(self) -> typing.Optional[_CloudfrontLogsBucket_34407447]:
        result = self._values.get("cloudfront_logs_bucket")
        return typing.cast(typing.Optional[_CloudfrontLogsBucket_34407447], result)

    @builtins.property
    def cloudtrail_logs_bucket(self) -> typing.Optional[_CloudtrailBucket_aa5784e2]:
        result = self._values.get("cloudtrail_logs_bucket")
        return typing.cast(typing.Optional[_CloudtrailBucket_aa5784e2], result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_logs_bucket(self) -> typing.Optional[_FlowLogsBucket_2af17beb]:
        result = self._values.get("flow_logs_bucket")
        return typing.cast(typing.Optional[_FlowLogsBucket_2af17beb], result)

    @builtins.property
    def flow_logs_format(self) -> typing.Optional[_FlowLogFormat_b7c2ba34]:
        result = self._values.get("flow_logs_format")
        return typing.cast(typing.Optional[_FlowLogFormat_b7c2ba34], result)

    @builtins.property
    def friendly_query_names(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("friendly_query_names")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ses_logs_bucket(self) -> typing.Optional[_SesLogsBucket_bc9a3d3a]:
        result = self._values.get("ses_logs_bucket")
        return typing.cast(typing.Optional[_SesLogsBucket_bc9a3d3a], result)

    @builtins.property
    def standardize_names(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("standardize_names")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def waf_logs_bucket(self) -> typing.Optional[_WafLogsBucket_0ad870de]:
        result = self._values.get("waf_logs_bucket")
        return typing.cast(typing.Optional[_WafLogsBucket_0ad870de], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsLoggingStackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AwsLoggingStack",
    "AwsLoggingStackProps",
]

publication.publish()
