'''
[![NPM version](https://badge.fury.io/js/cdk-slack-chatbot.svg)](https://badge.fury.io/js/cdk-slack-chatbot)
[![PyPI version](https://badge.fury.io/py/cdk-slack-chatbot.svg)](https://badge.fury.io/py/cdk-slack-chatbot)
![Release](https://github.com/lvthillo/cdk-slack-chatbot/workflows/release/badge.svg)

# cdk-slack-chatbot

A CDK construct which creates an SNS AWS ChatBot (Slack) integration for CloudWatch alarms, AWS Config rules, ...

# Example

Example use of construct

```python
import * as cdk from 'aws-cdk-lib';
import * as cloudwatch from 'aws-cdk-lib/aws-cloudwatch';
import * as cloudwatch_actions from 'aws-cdk-lib/aws-cloudwatch-actions';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import { CdkSlackChatBot } from 'cdk-slack-chatbot';
import { Construct } from 'constructs';

export class CdkDemoStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const queue = new sqs.Queue(this, 'HelloCdkQueue', {
      visibilityTimeout: cdk.Duration.seconds(300)
    });

    const qMetric = queue.metric('ApproximateNumberOfMessagesVisible');

    const alarm = new cloudwatch.Alarm(this, 'Alarm', {
      metric: qMetric,
      threshold: 100,
      evaluationPeriods: 3,
      datapointsToAlarm: 2
    });

    const slackAlarmIntegration = new CdkSlackChatBot(this, 'SlackIntegration', {
      topicName: 'slack-alarm',
      slackChannelId: 'xxx',
      slackWorkSpaceId: 'yyy',
      slackChannelConfigName: 'slack',
    });

    alarm.addAlarmAction(new cloudwatch_actions.SnsAction(slackAlarmIntegration.topic));

  }
}
```

Test Alarm:

```
$ aws cloudwatch set-alarm-state --alarm-name "xxx" --state-value ALARM --state-reason "testing purposes"
```
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

import aws_cdk.aws_sns
import constructs


class CdkSlackChatBot(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-slack-chatbot.CdkSlackChatBot",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        slack_channel_config_name: builtins.str,
        slack_channel_id: builtins.str,
        slack_work_space_id: builtins.str,
        topic_name: builtins.str,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param slack_channel_config_name: 
        :param slack_channel_id: 
        :param slack_work_space_id: 
        :param topic_name: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdkSlackChatBot.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CdkSlackChatBotProps(
            slack_channel_config_name=slack_channel_config_name,
            slack_channel_id=slack_channel_id,
            slack_work_space_id=slack_work_space_id,
            topic_name=topic_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> aws_cdk.aws_sns.Topic:
        '''
        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_sns.Topic, jsii.get(self, "topic"))


@jsii.data_type(
    jsii_type="cdk-slack-chatbot.CdkSlackChatBotProps",
    jsii_struct_bases=[],
    name_mapping={
        "slack_channel_config_name": "slackChannelConfigName",
        "slack_channel_id": "slackChannelId",
        "slack_work_space_id": "slackWorkSpaceId",
        "topic_name": "topicName",
    },
)
class CdkSlackChatBotProps:
    def __init__(
        self,
        *,
        slack_channel_config_name: builtins.str,
        slack_channel_id: builtins.str,
        slack_work_space_id: builtins.str,
        topic_name: builtins.str,
    ) -> None:
        '''
        :param slack_channel_config_name: 
        :param slack_channel_id: 
        :param slack_work_space_id: 
        :param topic_name: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdkSlackChatBotProps.__init__)
            check_type(argname="argument slack_channel_config_name", value=slack_channel_config_name, expected_type=type_hints["slack_channel_config_name"])
            check_type(argname="argument slack_channel_id", value=slack_channel_id, expected_type=type_hints["slack_channel_id"])
            check_type(argname="argument slack_work_space_id", value=slack_work_space_id, expected_type=type_hints["slack_work_space_id"])
            check_type(argname="argument topic_name", value=topic_name, expected_type=type_hints["topic_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "slack_channel_config_name": slack_channel_config_name,
            "slack_channel_id": slack_channel_id,
            "slack_work_space_id": slack_work_space_id,
            "topic_name": topic_name,
        }

    @builtins.property
    def slack_channel_config_name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("slack_channel_config_name")
        assert result is not None, "Required property 'slack_channel_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slack_channel_id(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("slack_channel_id")
        assert result is not None, "Required property 'slack_channel_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slack_work_space_id(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("slack_work_space_id")
        assert result is not None, "Required property 'slack_work_space_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("topic_name")
        assert result is not None, "Required property 'topic_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdkSlackChatBotProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CdkSlackChatBot",
    "CdkSlackChatBotProps",
]

publication.publish()
