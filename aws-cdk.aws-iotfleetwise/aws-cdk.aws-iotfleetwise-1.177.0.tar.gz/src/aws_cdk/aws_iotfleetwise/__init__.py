'''
# AWS::IoTFleetWise Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_iotfleetwise as iotfleetwise
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IoTFleetWise construct libraries](https://constructs.dev/search?q=iotfleetwise)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IoTFleetWise resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTFleetWise.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IoTFleetWise](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTFleetWise.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/master/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
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

import aws_cdk.core


@jsii.implements(aws_cdk.core.IInspectable)
class CfnCampaign(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotfleetwise.CfnCampaign",
):
    '''A CloudFormation ``AWS::IoTFleetWise::Campaign``.

    :cloudformationResource: AWS::IoTFleetWise::Campaign
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotfleetwise as iotfleetwise
        
        cfn_campaign = iotfleetwise.CfnCampaign(self, "MyCfnCampaign",
            action="action",
            collection_scheme=iotfleetwise.CfnCampaign.CollectionSchemeProperty(
                condition_based_collection_scheme=iotfleetwise.CfnCampaign.ConditionBasedCollectionSchemeProperty(
                    expression="expression",
        
                    # the properties below are optional
                    condition_language_version=123,
                    minimum_trigger_interval_ms=123,
                    trigger_mode="triggerMode"
                ),
                time_based_collection_scheme=iotfleetwise.CfnCampaign.TimeBasedCollectionSchemeProperty(
                    period_ms=123
                )
            ),
            name="name",
            signal_catalog_arn="signalCatalogArn",
            target_arn="targetArn",
        
            # the properties below are optional
            compression="compression",
            data_extra_dimensions=["dataExtraDimensions"],
            description="description",
            diagnostics_mode="diagnosticsMode",
            expiry_time="expiryTime",
            post_trigger_collection_duration=123,
            priority=123,
            signals_to_collect=[iotfleetwise.CfnCampaign.SignalInformationProperty(
                name="name",
        
                # the properties below are optional
                max_sample_count=123,
                minimum_sampling_interval_ms=123
            )],
            spooling_mode="spoolingMode",
            start_time="startTime",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        action: builtins.str,
        collection_scheme: typing.Union[typing.Union["CfnCampaign.CollectionSchemeProperty", typing.Dict[str, typing.Any]], aws_cdk.core.IResolvable],
        name: builtins.str,
        signal_catalog_arn: builtins.str,
        target_arn: builtins.str,
        compression: typing.Optional[builtins.str] = None,
        data_extra_dimensions: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        diagnostics_mode: typing.Optional[builtins.str] = None,
        expiry_time: typing.Optional[builtins.str] = None,
        post_trigger_collection_duration: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
        signals_to_collect: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCampaign.SignalInformationProperty", typing.Dict[str, typing.Any]]]]]] = None,
        spooling_mode: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[aws_cdk.core.CfnTag, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTFleetWise::Campaign``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param action: ``AWS::IoTFleetWise::Campaign.Action``.
        :param collection_scheme: ``AWS::IoTFleetWise::Campaign.CollectionScheme``.
        :param name: ``AWS::IoTFleetWise::Campaign.Name``.
        :param signal_catalog_arn: ``AWS::IoTFleetWise::Campaign.SignalCatalogArn``.
        :param target_arn: ``AWS::IoTFleetWise::Campaign.TargetArn``.
        :param compression: ``AWS::IoTFleetWise::Campaign.Compression``.
        :param data_extra_dimensions: ``AWS::IoTFleetWise::Campaign.DataExtraDimensions``.
        :param description: ``AWS::IoTFleetWise::Campaign.Description``.
        :param diagnostics_mode: ``AWS::IoTFleetWise::Campaign.DiagnosticsMode``.
        :param expiry_time: ``AWS::IoTFleetWise::Campaign.ExpiryTime``.
        :param post_trigger_collection_duration: ``AWS::IoTFleetWise::Campaign.PostTriggerCollectionDuration``.
        :param priority: ``AWS::IoTFleetWise::Campaign.Priority``.
        :param signals_to_collect: ``AWS::IoTFleetWise::Campaign.SignalsToCollect``.
        :param spooling_mode: ``AWS::IoTFleetWise::Campaign.SpoolingMode``.
        :param start_time: ``AWS::IoTFleetWise::Campaign.StartTime``.
        :param tags: ``AWS::IoTFleetWise::Campaign.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCampaign.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCampaignProps(
            action=action,
            collection_scheme=collection_scheme,
            name=name,
            signal_catalog_arn=signal_catalog_arn,
            target_arn=target_arn,
            compression=compression,
            data_extra_dimensions=data_extra_dimensions,
            description=description,
            diagnostics_mode=diagnostics_mode,
            expiry_time=expiry_time,
            post_trigger_collection_duration=post_trigger_collection_duration,
            priority=priority,
            signals_to_collect=signals_to_collect,
            spooling_mode=spooling_mode,
            start_time=start_time,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCampaign.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCampaign._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTFleetWise::Campaign.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.Action``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-action
        '''
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCampaign, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="collectionScheme")
    def collection_scheme(
        self,
    ) -> typing.Union["CfnCampaign.CollectionSchemeProperty", aws_cdk.core.IResolvable]:
        '''``AWS::IoTFleetWise::Campaign.CollectionScheme``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-collectionscheme
        '''
        return typing.cast(typing.Union["CfnCampaign.CollectionSchemeProperty", aws_cdk.core.IResolvable], jsii.get(self, "collectionScheme"))

    @collection_scheme.setter
    def collection_scheme(
        self,
        value: typing.Union["CfnCampaign.CollectionSchemeProperty", aws_cdk.core.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCampaign, "collection_scheme").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collectionScheme", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCampaign, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="signalCatalogArn")
    def signal_catalog_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.SignalCatalogArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-signalcatalogarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "signalCatalogArn"))

    @signal_catalog_arn.setter
    def signal_catalog_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCampaign, "signal_catalog_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalCatalogArn", value)

    @builtins.property
    @jsii.member(jsii_name="targetArn")
    def target_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.TargetArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-targetarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetArn"))

    @target_arn.setter
    def target_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCampaign, "target_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetArn", value)

    @builtins.property
    @jsii.member(jsii_name="compression")
    def compression(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.Compression``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-compression
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compression"))

    @compression.setter
    def compression(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCampaign, "compression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compression", value)

    @builtins.property
    @jsii.member(jsii_name="dataExtraDimensions")
    def data_extra_dimensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::IoTFleetWise::Campaign.DataExtraDimensions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-dataextradimensions
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dataExtraDimensions"))

    @data_extra_dimensions.setter
    def data_extra_dimensions(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCampaign, "data_extra_dimensions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataExtraDimensions", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCampaign, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="diagnosticsMode")
    def diagnostics_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.DiagnosticsMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-diagnosticsmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diagnosticsMode"))

    @diagnostics_mode.setter
    def diagnostics_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCampaign, "diagnostics_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diagnosticsMode", value)

    @builtins.property
    @jsii.member(jsii_name="expiryTime")
    def expiry_time(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.ExpiryTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-expirytime
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expiryTime"))

    @expiry_time.setter
    def expiry_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCampaign, "expiry_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiryTime", value)

    @builtins.property
    @jsii.member(jsii_name="postTriggerCollectionDuration")
    def post_trigger_collection_duration(self) -> typing.Optional[jsii.Number]:
        '''``AWS::IoTFleetWise::Campaign.PostTriggerCollectionDuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-posttriggercollectionduration
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "postTriggerCollectionDuration"))

    @post_trigger_collection_duration.setter
    def post_trigger_collection_duration(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCampaign, "post_trigger_collection_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postTriggerCollectionDuration", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> typing.Optional[jsii.Number]:
        '''``AWS::IoTFleetWise::Campaign.Priority``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-priority
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCampaign, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="signalsToCollect")
    def signals_to_collect(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.SignalInformationProperty"]]]]:
        '''``AWS::IoTFleetWise::Campaign.SignalsToCollect``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-signalstocollect
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.SignalInformationProperty"]]]], jsii.get(self, "signalsToCollect"))

    @signals_to_collect.setter
    def signals_to_collect(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.SignalInformationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCampaign, "signals_to_collect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalsToCollect", value)

    @builtins.property
    @jsii.member(jsii_name="spoolingMode")
    def spooling_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.SpoolingMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-spoolingmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spoolingMode"))

    @spooling_mode.setter
    def spooling_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCampaign, "spooling_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spoolingMode", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.StartTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-starttime
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCampaign, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnCampaign.CollectionSchemeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "condition_based_collection_scheme": "conditionBasedCollectionScheme",
            "time_based_collection_scheme": "timeBasedCollectionScheme",
        },
    )
    class CollectionSchemeProperty:
        def __init__(
            self,
            *,
            condition_based_collection_scheme: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCampaign.ConditionBasedCollectionSchemeProperty", typing.Dict[str, typing.Any]]]] = None,
            time_based_collection_scheme: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCampaign.TimeBasedCollectionSchemeProperty", typing.Dict[str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param condition_based_collection_scheme: ``CfnCampaign.CollectionSchemeProperty.ConditionBasedCollectionScheme``.
            :param time_based_collection_scheme: ``CfnCampaign.CollectionSchemeProperty.TimeBasedCollectionScheme``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-collectionscheme.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                collection_scheme_property = iotfleetwise.CfnCampaign.CollectionSchemeProperty(
                    condition_based_collection_scheme=iotfleetwise.CfnCampaign.ConditionBasedCollectionSchemeProperty(
                        expression="expression",
                
                        # the properties below are optional
                        condition_language_version=123,
                        minimum_trigger_interval_ms=123,
                        trigger_mode="triggerMode"
                    ),
                    time_based_collection_scheme=iotfleetwise.CfnCampaign.TimeBasedCollectionSchemeProperty(
                        period_ms=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCampaign.CollectionSchemeProperty.__init__)
                check_type(argname="argument condition_based_collection_scheme", value=condition_based_collection_scheme, expected_type=type_hints["condition_based_collection_scheme"])
                check_type(argname="argument time_based_collection_scheme", value=time_based_collection_scheme, expected_type=type_hints["time_based_collection_scheme"])
            self._values: typing.Dict[str, typing.Any] = {}
            if condition_based_collection_scheme is not None:
                self._values["condition_based_collection_scheme"] = condition_based_collection_scheme
            if time_based_collection_scheme is not None:
                self._values["time_based_collection_scheme"] = time_based_collection_scheme

        @builtins.property
        def condition_based_collection_scheme(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.ConditionBasedCollectionSchemeProperty"]]:
            '''``CfnCampaign.CollectionSchemeProperty.ConditionBasedCollectionScheme``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-collectionscheme.html#cfn-iotfleetwise-campaign-collectionscheme-conditionbasedcollectionscheme
            '''
            result = self._values.get("condition_based_collection_scheme")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.ConditionBasedCollectionSchemeProperty"]], result)

        @builtins.property
        def time_based_collection_scheme(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.TimeBasedCollectionSchemeProperty"]]:
            '''``CfnCampaign.CollectionSchemeProperty.TimeBasedCollectionScheme``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-collectionscheme.html#cfn-iotfleetwise-campaign-collectionscheme-timebasedcollectionscheme
            '''
            result = self._values.get("time_based_collection_scheme")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.TimeBasedCollectionSchemeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CollectionSchemeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnCampaign.ConditionBasedCollectionSchemeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "expression": "expression",
            "condition_language_version": "conditionLanguageVersion",
            "minimum_trigger_interval_ms": "minimumTriggerIntervalMs",
            "trigger_mode": "triggerMode",
        },
    )
    class ConditionBasedCollectionSchemeProperty:
        def __init__(
            self,
            *,
            expression: builtins.str,
            condition_language_version: typing.Optional[jsii.Number] = None,
            minimum_trigger_interval_ms: typing.Optional[jsii.Number] = None,
            trigger_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param expression: ``CfnCampaign.ConditionBasedCollectionSchemeProperty.Expression``.
            :param condition_language_version: ``CfnCampaign.ConditionBasedCollectionSchemeProperty.ConditionLanguageVersion``.
            :param minimum_trigger_interval_ms: ``CfnCampaign.ConditionBasedCollectionSchemeProperty.MinimumTriggerIntervalMs``.
            :param trigger_mode: ``CfnCampaign.ConditionBasedCollectionSchemeProperty.TriggerMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                condition_based_collection_scheme_property = iotfleetwise.CfnCampaign.ConditionBasedCollectionSchemeProperty(
                    expression="expression",
                
                    # the properties below are optional
                    condition_language_version=123,
                    minimum_trigger_interval_ms=123,
                    trigger_mode="triggerMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCampaign.ConditionBasedCollectionSchemeProperty.__init__)
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument condition_language_version", value=condition_language_version, expected_type=type_hints["condition_language_version"])
                check_type(argname="argument minimum_trigger_interval_ms", value=minimum_trigger_interval_ms, expected_type=type_hints["minimum_trigger_interval_ms"])
                check_type(argname="argument trigger_mode", value=trigger_mode, expected_type=type_hints["trigger_mode"])
            self._values: typing.Dict[str, typing.Any] = {
                "expression": expression,
            }
            if condition_language_version is not None:
                self._values["condition_language_version"] = condition_language_version
            if minimum_trigger_interval_ms is not None:
                self._values["minimum_trigger_interval_ms"] = minimum_trigger_interval_ms
            if trigger_mode is not None:
                self._values["trigger_mode"] = trigger_mode

        @builtins.property
        def expression(self) -> builtins.str:
            '''``CfnCampaign.ConditionBasedCollectionSchemeProperty.Expression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def condition_language_version(self) -> typing.Optional[jsii.Number]:
            '''``CfnCampaign.ConditionBasedCollectionSchemeProperty.ConditionLanguageVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-conditionlanguageversion
            '''
            result = self._values.get("condition_language_version")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def minimum_trigger_interval_ms(self) -> typing.Optional[jsii.Number]:
            '''``CfnCampaign.ConditionBasedCollectionSchemeProperty.MinimumTriggerIntervalMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-minimumtriggerintervalms
            '''
            result = self._values.get("minimum_trigger_interval_ms")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def trigger_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.ConditionBasedCollectionSchemeProperty.TriggerMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-triggermode
            '''
            result = self._values.get("trigger_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionBasedCollectionSchemeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnCampaign.SignalInformationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "max_sample_count": "maxSampleCount",
            "minimum_sampling_interval_ms": "minimumSamplingIntervalMs",
        },
    )
    class SignalInformationProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            max_sample_count: typing.Optional[jsii.Number] = None,
            minimum_sampling_interval_ms: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param name: ``CfnCampaign.SignalInformationProperty.Name``.
            :param max_sample_count: ``CfnCampaign.SignalInformationProperty.MaxSampleCount``.
            :param minimum_sampling_interval_ms: ``CfnCampaign.SignalInformationProperty.MinimumSamplingIntervalMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                signal_information_property = iotfleetwise.CfnCampaign.SignalInformationProperty(
                    name="name",
                
                    # the properties below are optional
                    max_sample_count=123,
                    minimum_sampling_interval_ms=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCampaign.SignalInformationProperty.__init__)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument max_sample_count", value=max_sample_count, expected_type=type_hints["max_sample_count"])
                check_type(argname="argument minimum_sampling_interval_ms", value=minimum_sampling_interval_ms, expected_type=type_hints["minimum_sampling_interval_ms"])
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }
            if max_sample_count is not None:
                self._values["max_sample_count"] = max_sample_count
            if minimum_sampling_interval_ms is not None:
                self._values["minimum_sampling_interval_ms"] = minimum_sampling_interval_ms

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnCampaign.SignalInformationProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html#cfn-iotfleetwise-campaign-signalinformation-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def max_sample_count(self) -> typing.Optional[jsii.Number]:
            '''``CfnCampaign.SignalInformationProperty.MaxSampleCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html#cfn-iotfleetwise-campaign-signalinformation-maxsamplecount
            '''
            result = self._values.get("max_sample_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def minimum_sampling_interval_ms(self) -> typing.Optional[jsii.Number]:
            '''``CfnCampaign.SignalInformationProperty.MinimumSamplingIntervalMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html#cfn-iotfleetwise-campaign-signalinformation-minimumsamplingintervalms
            '''
            result = self._values.get("minimum_sampling_interval_ms")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SignalInformationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnCampaign.TimeBasedCollectionSchemeProperty",
        jsii_struct_bases=[],
        name_mapping={"period_ms": "periodMs"},
    )
    class TimeBasedCollectionSchemeProperty:
        def __init__(self, *, period_ms: jsii.Number) -> None:
            '''
            :param period_ms: ``CfnCampaign.TimeBasedCollectionSchemeProperty.PeriodMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timebasedcollectionscheme.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                time_based_collection_scheme_property = iotfleetwise.CfnCampaign.TimeBasedCollectionSchemeProperty(
                    period_ms=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCampaign.TimeBasedCollectionSchemeProperty.__init__)
                check_type(argname="argument period_ms", value=period_ms, expected_type=type_hints["period_ms"])
            self._values: typing.Dict[str, typing.Any] = {
                "period_ms": period_ms,
            }

        @builtins.property
        def period_ms(self) -> jsii.Number:
            '''``CfnCampaign.TimeBasedCollectionSchemeProperty.PeriodMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timebasedcollectionscheme.html#cfn-iotfleetwise-campaign-timebasedcollectionscheme-periodms
            '''
            result = self._values.get("period_ms")
            assert result is not None, "Required property 'period_ms' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeBasedCollectionSchemeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotfleetwise.CfnCampaignProps",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "collection_scheme": "collectionScheme",
        "name": "name",
        "signal_catalog_arn": "signalCatalogArn",
        "target_arn": "targetArn",
        "compression": "compression",
        "data_extra_dimensions": "dataExtraDimensions",
        "description": "description",
        "diagnostics_mode": "diagnosticsMode",
        "expiry_time": "expiryTime",
        "post_trigger_collection_duration": "postTriggerCollectionDuration",
        "priority": "priority",
        "signals_to_collect": "signalsToCollect",
        "spooling_mode": "spoolingMode",
        "start_time": "startTime",
        "tags": "tags",
    },
)
class CfnCampaignProps:
    def __init__(
        self,
        *,
        action: builtins.str,
        collection_scheme: typing.Union[typing.Union[CfnCampaign.CollectionSchemeProperty, typing.Dict[str, typing.Any]], aws_cdk.core.IResolvable],
        name: builtins.str,
        signal_catalog_arn: builtins.str,
        target_arn: builtins.str,
        compression: typing.Optional[builtins.str] = None,
        data_extra_dimensions: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        diagnostics_mode: typing.Optional[builtins.str] = None,
        expiry_time: typing.Optional[builtins.str] = None,
        post_trigger_collection_duration: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
        signals_to_collect: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCampaign.SignalInformationProperty, typing.Dict[str, typing.Any]]]]]] = None,
        spooling_mode: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[aws_cdk.core.CfnTag, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCampaign``.

        :param action: ``AWS::IoTFleetWise::Campaign.Action``.
        :param collection_scheme: ``AWS::IoTFleetWise::Campaign.CollectionScheme``.
        :param name: ``AWS::IoTFleetWise::Campaign.Name``.
        :param signal_catalog_arn: ``AWS::IoTFleetWise::Campaign.SignalCatalogArn``.
        :param target_arn: ``AWS::IoTFleetWise::Campaign.TargetArn``.
        :param compression: ``AWS::IoTFleetWise::Campaign.Compression``.
        :param data_extra_dimensions: ``AWS::IoTFleetWise::Campaign.DataExtraDimensions``.
        :param description: ``AWS::IoTFleetWise::Campaign.Description``.
        :param diagnostics_mode: ``AWS::IoTFleetWise::Campaign.DiagnosticsMode``.
        :param expiry_time: ``AWS::IoTFleetWise::Campaign.ExpiryTime``.
        :param post_trigger_collection_duration: ``AWS::IoTFleetWise::Campaign.PostTriggerCollectionDuration``.
        :param priority: ``AWS::IoTFleetWise::Campaign.Priority``.
        :param signals_to_collect: ``AWS::IoTFleetWise::Campaign.SignalsToCollect``.
        :param spooling_mode: ``AWS::IoTFleetWise::Campaign.SpoolingMode``.
        :param start_time: ``AWS::IoTFleetWise::Campaign.StartTime``.
        :param tags: ``AWS::IoTFleetWise::Campaign.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotfleetwise as iotfleetwise
            
            cfn_campaign_props = iotfleetwise.CfnCampaignProps(
                action="action",
                collection_scheme=iotfleetwise.CfnCampaign.CollectionSchemeProperty(
                    condition_based_collection_scheme=iotfleetwise.CfnCampaign.ConditionBasedCollectionSchemeProperty(
                        expression="expression",
            
                        # the properties below are optional
                        condition_language_version=123,
                        minimum_trigger_interval_ms=123,
                        trigger_mode="triggerMode"
                    ),
                    time_based_collection_scheme=iotfleetwise.CfnCampaign.TimeBasedCollectionSchemeProperty(
                        period_ms=123
                    )
                ),
                name="name",
                signal_catalog_arn="signalCatalogArn",
                target_arn="targetArn",
            
                # the properties below are optional
                compression="compression",
                data_extra_dimensions=["dataExtraDimensions"],
                description="description",
                diagnostics_mode="diagnosticsMode",
                expiry_time="expiryTime",
                post_trigger_collection_duration=123,
                priority=123,
                signals_to_collect=[iotfleetwise.CfnCampaign.SignalInformationProperty(
                    name="name",
            
                    # the properties below are optional
                    max_sample_count=123,
                    minimum_sampling_interval_ms=123
                )],
                spooling_mode="spoolingMode",
                start_time="startTime",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCampaignProps.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument collection_scheme", value=collection_scheme, expected_type=type_hints["collection_scheme"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument signal_catalog_arn", value=signal_catalog_arn, expected_type=type_hints["signal_catalog_arn"])
            check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument data_extra_dimensions", value=data_extra_dimensions, expected_type=type_hints["data_extra_dimensions"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument diagnostics_mode", value=diagnostics_mode, expected_type=type_hints["diagnostics_mode"])
            check_type(argname="argument expiry_time", value=expiry_time, expected_type=type_hints["expiry_time"])
            check_type(argname="argument post_trigger_collection_duration", value=post_trigger_collection_duration, expected_type=type_hints["post_trigger_collection_duration"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument signals_to_collect", value=signals_to_collect, expected_type=type_hints["signals_to_collect"])
            check_type(argname="argument spooling_mode", value=spooling_mode, expected_type=type_hints["spooling_mode"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "collection_scheme": collection_scheme,
            "name": name,
            "signal_catalog_arn": signal_catalog_arn,
            "target_arn": target_arn,
        }
        if compression is not None:
            self._values["compression"] = compression
        if data_extra_dimensions is not None:
            self._values["data_extra_dimensions"] = data_extra_dimensions
        if description is not None:
            self._values["description"] = description
        if diagnostics_mode is not None:
            self._values["diagnostics_mode"] = diagnostics_mode
        if expiry_time is not None:
            self._values["expiry_time"] = expiry_time
        if post_trigger_collection_duration is not None:
            self._values["post_trigger_collection_duration"] = post_trigger_collection_duration
        if priority is not None:
            self._values["priority"] = priority
        if signals_to_collect is not None:
            self._values["signals_to_collect"] = signals_to_collect
        if spooling_mode is not None:
            self._values["spooling_mode"] = spooling_mode
        if start_time is not None:
            self._values["start_time"] = start_time
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def action(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.Action``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-action
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def collection_scheme(
        self,
    ) -> typing.Union[CfnCampaign.CollectionSchemeProperty, aws_cdk.core.IResolvable]:
        '''``AWS::IoTFleetWise::Campaign.CollectionScheme``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-collectionscheme
        '''
        result = self._values.get("collection_scheme")
        assert result is not None, "Required property 'collection_scheme' is missing"
        return typing.cast(typing.Union[CfnCampaign.CollectionSchemeProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signal_catalog_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.SignalCatalogArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-signalcatalogarn
        '''
        result = self._values.get("signal_catalog_arn")
        assert result is not None, "Required property 'signal_catalog_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.TargetArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-targetarn
        '''
        result = self._values.get("target_arn")
        assert result is not None, "Required property 'target_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compression(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.Compression``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-compression
        '''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_extra_dimensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::IoTFleetWise::Campaign.DataExtraDimensions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-dataextradimensions
        '''
        result = self._values.get("data_extra_dimensions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def diagnostics_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.DiagnosticsMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-diagnosticsmode
        '''
        result = self._values.get("diagnostics_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiry_time(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.ExpiryTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-expirytime
        '''
        result = self._values.get("expiry_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def post_trigger_collection_duration(self) -> typing.Optional[jsii.Number]:
        '''``AWS::IoTFleetWise::Campaign.PostTriggerCollectionDuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-posttriggercollectionduration
        '''
        result = self._values.get("post_trigger_collection_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''``AWS::IoTFleetWise::Campaign.Priority``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def signals_to_collect(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCampaign.SignalInformationProperty]]]]:
        '''``AWS::IoTFleetWise::Campaign.SignalsToCollect``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-signalstocollect
        '''
        result = self._values.get("signals_to_collect")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCampaign.SignalInformationProperty]]]], result)

    @builtins.property
    def spooling_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.SpoolingMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-spoolingmode
        '''
        result = self._values.get("spooling_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.StartTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-starttime
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTFleetWise::Campaign.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCampaignProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDecoderManifest(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotfleetwise.CfnDecoderManifest",
):
    '''A CloudFormation ``AWS::IoTFleetWise::DecoderManifest``.

    :cloudformationResource: AWS::IoTFleetWise::DecoderManifest
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotfleetwise as iotfleetwise
        
        # network_interfaces: Any
        # signal_decoders: Any
        
        cfn_decoder_manifest = iotfleetwise.CfnDecoderManifest(self, "MyCfnDecoderManifest",
            model_manifest_arn="modelManifestArn",
            name="name",
        
            # the properties below are optional
            description="description",
            network_interfaces=[network_interfaces],
            signal_decoders=[signal_decoders],
            status="status",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        model_manifest_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        network_interfaces: typing.Optional[typing.Union[typing.Sequence[typing.Any], aws_cdk.core.IResolvable]] = None,
        signal_decoders: typing.Optional[typing.Union[typing.Sequence[typing.Any], aws_cdk.core.IResolvable]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[aws_cdk.core.CfnTag, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTFleetWise::DecoderManifest``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param model_manifest_arn: ``AWS::IoTFleetWise::DecoderManifest.ModelManifestArn``.
        :param name: ``AWS::IoTFleetWise::DecoderManifest.Name``.
        :param description: ``AWS::IoTFleetWise::DecoderManifest.Description``.
        :param network_interfaces: ``AWS::IoTFleetWise::DecoderManifest.NetworkInterfaces``.
        :param signal_decoders: ``AWS::IoTFleetWise::DecoderManifest.SignalDecoders``.
        :param status: ``AWS::IoTFleetWise::DecoderManifest.Status``.
        :param tags: ``AWS::IoTFleetWise::DecoderManifest.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDecoderManifest.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDecoderManifestProps(
            model_manifest_arn=model_manifest_arn,
            name=name,
            description=description,
            network_interfaces=network_interfaces,
            signal_decoders=signal_decoders,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDecoderManifest.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDecoderManifest._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTFleetWise::DecoderManifest.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="modelManifestArn")
    def model_manifest_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::DecoderManifest.ModelManifestArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-modelmanifestarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "modelManifestArn"))

    @model_manifest_arn.setter
    def model_manifest_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDecoderManifest, "model_manifest_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelManifestArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::DecoderManifest.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDecoderManifest, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::DecoderManifest.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDecoderManifest, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> typing.Optional[typing.Union[typing.List[typing.Any], aws_cdk.core.IResolvable]]:
        '''``AWS::IoTFleetWise::DecoderManifest.NetworkInterfaces``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-networkinterfaces
        '''
        return typing.cast(typing.Optional[typing.Union[typing.List[typing.Any], aws_cdk.core.IResolvable]], jsii.get(self, "networkInterfaces"))

    @network_interfaces.setter
    def network_interfaces(
        self,
        value: typing.Optional[typing.Union[typing.List[typing.Any], aws_cdk.core.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDecoderManifest, "network_interfaces").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkInterfaces", value)

    @builtins.property
    @jsii.member(jsii_name="signalDecoders")
    def signal_decoders(
        self,
    ) -> typing.Optional[typing.Union[typing.List[typing.Any], aws_cdk.core.IResolvable]]:
        '''``AWS::IoTFleetWise::DecoderManifest.SignalDecoders``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-signaldecoders
        '''
        return typing.cast(typing.Optional[typing.Union[typing.List[typing.Any], aws_cdk.core.IResolvable]], jsii.get(self, "signalDecoders"))

    @signal_decoders.setter
    def signal_decoders(
        self,
        value: typing.Optional[typing.Union[typing.List[typing.Any], aws_cdk.core.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDecoderManifest, "signal_decoders").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalDecoders", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::DecoderManifest.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDecoderManifest, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnDecoderManifest.CanInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "protocol_name": "protocolName",
            "protocol_version": "protocolVersion",
        },
    )
    class CanInterfaceProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            protocol_name: typing.Optional[builtins.str] = None,
            protocol_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: ``CfnDecoderManifest.CanInterfaceProperty.Name``.
            :param protocol_name: ``CfnDecoderManifest.CanInterfaceProperty.ProtocolName``.
            :param protocol_version: ``CfnDecoderManifest.CanInterfaceProperty.ProtocolVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                can_interface_property = iotfleetwise.CfnDecoderManifest.CanInterfaceProperty(
                    name="name",
                
                    # the properties below are optional
                    protocol_name="protocolName",
                    protocol_version="protocolVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDecoderManifest.CanInterfaceProperty.__init__)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument protocol_name", value=protocol_name, expected_type=type_hints["protocol_name"])
                check_type(argname="argument protocol_version", value=protocol_version, expected_type=type_hints["protocol_version"])
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }
            if protocol_name is not None:
                self._values["protocol_name"] = protocol_name
            if protocol_version is not None:
                self._values["protocol_version"] = protocol_version

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnDecoderManifest.CanInterfaceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html#cfn-iotfleetwise-decodermanifest-caninterface-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def protocol_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDecoderManifest.CanInterfaceProperty.ProtocolName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html#cfn-iotfleetwise-decodermanifest-caninterface-protocolname
            '''
            result = self._values.get("protocol_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def protocol_version(self) -> typing.Optional[builtins.str]:
            '''``CfnDecoderManifest.CanInterfaceProperty.ProtocolVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html#cfn-iotfleetwise-decodermanifest-caninterface-protocolversion
            '''
            result = self._values.get("protocol_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CanInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnDecoderManifest.CanNetworkInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "can_interface": "canInterface",
            "interface_id": "interfaceId",
            "type": "type",
        },
    )
    class CanNetworkInterfaceProperty:
        def __init__(
            self,
            *,
            can_interface: typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnDecoderManifest.CanInterfaceProperty", typing.Dict[str, typing.Any]]],
            interface_id: builtins.str,
            type: builtins.str,
        ) -> None:
            '''
            :param can_interface: ``CfnDecoderManifest.CanNetworkInterfaceProperty.CanInterface``.
            :param interface_id: ``CfnDecoderManifest.CanNetworkInterfaceProperty.InterfaceId``.
            :param type: ``CfnDecoderManifest.CanNetworkInterfaceProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cannetworkinterface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                can_network_interface_property = iotfleetwise.CfnDecoderManifest.CanNetworkInterfaceProperty(
                    can_interface=iotfleetwise.CfnDecoderManifest.CanInterfaceProperty(
                        name="name",
                
                        # the properties below are optional
                        protocol_name="protocolName",
                        protocol_version="protocolVersion"
                    ),
                    interface_id="interfaceId",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDecoderManifest.CanNetworkInterfaceProperty.__init__)
                check_type(argname="argument can_interface", value=can_interface, expected_type=type_hints["can_interface"])
                check_type(argname="argument interface_id", value=interface_id, expected_type=type_hints["interface_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[str, typing.Any] = {
                "can_interface": can_interface,
                "interface_id": interface_id,
                "type": type,
            }

        @builtins.property
        def can_interface(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDecoderManifest.CanInterfaceProperty"]:
            '''``CfnDecoderManifest.CanNetworkInterfaceProperty.CanInterface``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cannetworkinterface.html#cfn-iotfleetwise-decodermanifest-cannetworkinterface-caninterface
            '''
            result = self._values.get("can_interface")
            assert result is not None, "Required property 'can_interface' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDecoderManifest.CanInterfaceProperty"], result)

        @builtins.property
        def interface_id(self) -> builtins.str:
            '''``CfnDecoderManifest.CanNetworkInterfaceProperty.InterfaceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cannetworkinterface.html#cfn-iotfleetwise-decodermanifest-cannetworkinterface-interfaceid
            '''
            result = self._values.get("interface_id")
            assert result is not None, "Required property 'interface_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnDecoderManifest.CanNetworkInterfaceProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cannetworkinterface.html#cfn-iotfleetwise-decodermanifest-cannetworkinterface-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CanNetworkInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnDecoderManifest.CanSignalDecoderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "can_signal": "canSignal",
            "fully_qualified_name": "fullyQualifiedName",
            "interface_id": "interfaceId",
            "type": "type",
        },
    )
    class CanSignalDecoderProperty:
        def __init__(
            self,
            *,
            can_signal: typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnDecoderManifest.CanSignalProperty", typing.Dict[str, typing.Any]]],
            fully_qualified_name: builtins.str,
            interface_id: builtins.str,
            type: builtins.str,
        ) -> None:
            '''
            :param can_signal: ``CfnDecoderManifest.CanSignalDecoderProperty.CanSignal``.
            :param fully_qualified_name: ``CfnDecoderManifest.CanSignalDecoderProperty.FullyQualifiedName``.
            :param interface_id: ``CfnDecoderManifest.CanSignalDecoderProperty.InterfaceId``.
            :param type: ``CfnDecoderManifest.CanSignalDecoderProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignaldecoder.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                # factor: Any
                # is_big_endian: Any
                # is_signed: Any
                # length: Any
                # message_id: Any
                # offset: Any
                # start_bit: Any
                
                can_signal_decoder_property = iotfleetwise.CfnDecoderManifest.CanSignalDecoderProperty(
                    can_signal=iotfleetwise.CfnDecoderManifest.CanSignalProperty(
                        factor=factor,
                        is_big_endian=is_big_endian,
                        is_signed=is_signed,
                        length=length,
                        message_id=message_id,
                        offset=offset,
                        start_bit=start_bit,
                
                        # the properties below are optional
                        name="name"
                    ),
                    fully_qualified_name="fullyQualifiedName",
                    interface_id="interfaceId",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDecoderManifest.CanSignalDecoderProperty.__init__)
                check_type(argname="argument can_signal", value=can_signal, expected_type=type_hints["can_signal"])
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument interface_id", value=interface_id, expected_type=type_hints["interface_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[str, typing.Any] = {
                "can_signal": can_signal,
                "fully_qualified_name": fully_qualified_name,
                "interface_id": interface_id,
                "type": type,
            }

        @builtins.property
        def can_signal(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDecoderManifest.CanSignalProperty"]:
            '''``CfnDecoderManifest.CanSignalDecoderProperty.CanSignal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignaldecoder.html#cfn-iotfleetwise-decodermanifest-cansignaldecoder-cansignal
            '''
            result = self._values.get("can_signal")
            assert result is not None, "Required property 'can_signal' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDecoderManifest.CanSignalProperty"], result)

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''``CfnDecoderManifest.CanSignalDecoderProperty.FullyQualifiedName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignaldecoder.html#cfn-iotfleetwise-decodermanifest-cansignaldecoder-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def interface_id(self) -> builtins.str:
            '''``CfnDecoderManifest.CanSignalDecoderProperty.InterfaceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignaldecoder.html#cfn-iotfleetwise-decodermanifest-cansignaldecoder-interfaceid
            '''
            result = self._values.get("interface_id")
            assert result is not None, "Required property 'interface_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnDecoderManifest.CanSignalDecoderProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignaldecoder.html#cfn-iotfleetwise-decodermanifest-cansignaldecoder-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CanSignalDecoderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnDecoderManifest.CanSignalProperty",
        jsii_struct_bases=[],
        name_mapping={
            "factor": "factor",
            "is_big_endian": "isBigEndian",
            "is_signed": "isSigned",
            "length": "length",
            "message_id": "messageId",
            "offset": "offset",
            "start_bit": "startBit",
            "name": "name",
        },
    )
    class CanSignalProperty:
        def __init__(
            self,
            *,
            factor: typing.Any,
            is_big_endian: typing.Any,
            is_signed: typing.Any,
            length: typing.Any,
            message_id: typing.Any,
            offset: typing.Any,
            start_bit: typing.Any,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param factor: ``CfnDecoderManifest.CanSignalProperty.Factor``.
            :param is_big_endian: ``CfnDecoderManifest.CanSignalProperty.IsBigEndian``.
            :param is_signed: ``CfnDecoderManifest.CanSignalProperty.IsSigned``.
            :param length: ``CfnDecoderManifest.CanSignalProperty.Length``.
            :param message_id: ``CfnDecoderManifest.CanSignalProperty.MessageId``.
            :param offset: ``CfnDecoderManifest.CanSignalProperty.Offset``.
            :param start_bit: ``CfnDecoderManifest.CanSignalProperty.StartBit``.
            :param name: ``CfnDecoderManifest.CanSignalProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                # factor: Any
                # is_big_endian: Any
                # is_signed: Any
                # length: Any
                # message_id: Any
                # offset: Any
                # start_bit: Any
                
                can_signal_property = iotfleetwise.CfnDecoderManifest.CanSignalProperty(
                    factor=factor,
                    is_big_endian=is_big_endian,
                    is_signed=is_signed,
                    length=length,
                    message_id=message_id,
                    offset=offset,
                    start_bit=start_bit,
                
                    # the properties below are optional
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDecoderManifest.CanSignalProperty.__init__)
                check_type(argname="argument factor", value=factor, expected_type=type_hints["factor"])
                check_type(argname="argument is_big_endian", value=is_big_endian, expected_type=type_hints["is_big_endian"])
                check_type(argname="argument is_signed", value=is_signed, expected_type=type_hints["is_signed"])
                check_type(argname="argument length", value=length, expected_type=type_hints["length"])
                check_type(argname="argument message_id", value=message_id, expected_type=type_hints["message_id"])
                check_type(argname="argument offset", value=offset, expected_type=type_hints["offset"])
                check_type(argname="argument start_bit", value=start_bit, expected_type=type_hints["start_bit"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {
                "factor": factor,
                "is_big_endian": is_big_endian,
                "is_signed": is_signed,
                "length": length,
                "message_id": message_id,
                "offset": offset,
                "start_bit": start_bit,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def factor(self) -> typing.Any:
            '''``CfnDecoderManifest.CanSignalProperty.Factor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-factor
            '''
            result = self._values.get("factor")
            assert result is not None, "Required property 'factor' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def is_big_endian(self) -> typing.Any:
            '''``CfnDecoderManifest.CanSignalProperty.IsBigEndian``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-isbigendian
            '''
            result = self._values.get("is_big_endian")
            assert result is not None, "Required property 'is_big_endian' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def is_signed(self) -> typing.Any:
            '''``CfnDecoderManifest.CanSignalProperty.IsSigned``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-issigned
            '''
            result = self._values.get("is_signed")
            assert result is not None, "Required property 'is_signed' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def length(self) -> typing.Any:
            '''``CfnDecoderManifest.CanSignalProperty.Length``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-length
            '''
            result = self._values.get("length")
            assert result is not None, "Required property 'length' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def message_id(self) -> typing.Any:
            '''``CfnDecoderManifest.CanSignalProperty.MessageId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-messageid
            '''
            result = self._values.get("message_id")
            assert result is not None, "Required property 'message_id' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def offset(self) -> typing.Any:
            '''``CfnDecoderManifest.CanSignalProperty.Offset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-offset
            '''
            result = self._values.get("offset")
            assert result is not None, "Required property 'offset' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def start_bit(self) -> typing.Any:
            '''``CfnDecoderManifest.CanSignalProperty.StartBit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-startbit
            '''
            result = self._values.get("start_bit")
            assert result is not None, "Required property 'start_bit' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnDecoderManifest.CanSignalProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CanSignalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnDecoderManifest.ObdInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "request_message_id": "requestMessageId",
            "dtc_request_interval_seconds": "dtcRequestIntervalSeconds",
            "has_transmission_ecu": "hasTransmissionEcu",
            "obd_standard": "obdStandard",
            "pid_request_interval_seconds": "pidRequestIntervalSeconds",
            "use_extended_ids": "useExtendedIds",
        },
    )
    class ObdInterfaceProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            request_message_id: typing.Any,
            dtc_request_interval_seconds: typing.Any = None,
            has_transmission_ecu: typing.Any = None,
            obd_standard: typing.Optional[builtins.str] = None,
            pid_request_interval_seconds: typing.Any = None,
            use_extended_ids: typing.Any = None,
        ) -> None:
            '''
            :param name: ``CfnDecoderManifest.ObdInterfaceProperty.Name``.
            :param request_message_id: ``CfnDecoderManifest.ObdInterfaceProperty.RequestMessageId``.
            :param dtc_request_interval_seconds: ``CfnDecoderManifest.ObdInterfaceProperty.DtcRequestIntervalSeconds``.
            :param has_transmission_ecu: ``CfnDecoderManifest.ObdInterfaceProperty.HasTransmissionEcu``.
            :param obd_standard: ``CfnDecoderManifest.ObdInterfaceProperty.ObdStandard``.
            :param pid_request_interval_seconds: ``CfnDecoderManifest.ObdInterfaceProperty.PidRequestIntervalSeconds``.
            :param use_extended_ids: ``CfnDecoderManifest.ObdInterfaceProperty.UseExtendedIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                # dtc_request_interval_seconds: Any
                # has_transmission_ecu: Any
                # pid_request_interval_seconds: Any
                # request_message_id: Any
                # use_extended_ids: Any
                
                obd_interface_property = iotfleetwise.CfnDecoderManifest.ObdInterfaceProperty(
                    name="name",
                    request_message_id=request_message_id,
                
                    # the properties below are optional
                    dtc_request_interval_seconds=dtc_request_interval_seconds,
                    has_transmission_ecu=has_transmission_ecu,
                    obd_standard="obdStandard",
                    pid_request_interval_seconds=pid_request_interval_seconds,
                    use_extended_ids=use_extended_ids
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDecoderManifest.ObdInterfaceProperty.__init__)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument request_message_id", value=request_message_id, expected_type=type_hints["request_message_id"])
                check_type(argname="argument dtc_request_interval_seconds", value=dtc_request_interval_seconds, expected_type=type_hints["dtc_request_interval_seconds"])
                check_type(argname="argument has_transmission_ecu", value=has_transmission_ecu, expected_type=type_hints["has_transmission_ecu"])
                check_type(argname="argument obd_standard", value=obd_standard, expected_type=type_hints["obd_standard"])
                check_type(argname="argument pid_request_interval_seconds", value=pid_request_interval_seconds, expected_type=type_hints["pid_request_interval_seconds"])
                check_type(argname="argument use_extended_ids", value=use_extended_ids, expected_type=type_hints["use_extended_ids"])
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "request_message_id": request_message_id,
            }
            if dtc_request_interval_seconds is not None:
                self._values["dtc_request_interval_seconds"] = dtc_request_interval_seconds
            if has_transmission_ecu is not None:
                self._values["has_transmission_ecu"] = has_transmission_ecu
            if obd_standard is not None:
                self._values["obd_standard"] = obd_standard
            if pid_request_interval_seconds is not None:
                self._values["pid_request_interval_seconds"] = pid_request_interval_seconds
            if use_extended_ids is not None:
                self._values["use_extended_ids"] = use_extended_ids

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnDecoderManifest.ObdInterfaceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def request_message_id(self) -> typing.Any:
            '''``CfnDecoderManifest.ObdInterfaceProperty.RequestMessageId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-requestmessageid
            '''
            result = self._values.get("request_message_id")
            assert result is not None, "Required property 'request_message_id' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def dtc_request_interval_seconds(self) -> typing.Any:
            '''``CfnDecoderManifest.ObdInterfaceProperty.DtcRequestIntervalSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-dtcrequestintervalseconds
            '''
            result = self._values.get("dtc_request_interval_seconds")
            return typing.cast(typing.Any, result)

        @builtins.property
        def has_transmission_ecu(self) -> typing.Any:
            '''``CfnDecoderManifest.ObdInterfaceProperty.HasTransmissionEcu``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-hastransmissionecu
            '''
            result = self._values.get("has_transmission_ecu")
            return typing.cast(typing.Any, result)

        @builtins.property
        def obd_standard(self) -> typing.Optional[builtins.str]:
            '''``CfnDecoderManifest.ObdInterfaceProperty.ObdStandard``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-obdstandard
            '''
            result = self._values.get("obd_standard")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pid_request_interval_seconds(self) -> typing.Any:
            '''``CfnDecoderManifest.ObdInterfaceProperty.PidRequestIntervalSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-pidrequestintervalseconds
            '''
            result = self._values.get("pid_request_interval_seconds")
            return typing.cast(typing.Any, result)

        @builtins.property
        def use_extended_ids(self) -> typing.Any:
            '''``CfnDecoderManifest.ObdInterfaceProperty.UseExtendedIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-useextendedids
            '''
            result = self._values.get("use_extended_ids")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObdInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnDecoderManifest.ObdNetworkInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interface_id": "interfaceId",
            "obd_interface": "obdInterface",
            "type": "type",
        },
    )
    class ObdNetworkInterfaceProperty:
        def __init__(
            self,
            *,
            interface_id: builtins.str,
            obd_interface: typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnDecoderManifest.ObdInterfaceProperty", typing.Dict[str, typing.Any]]],
            type: builtins.str,
        ) -> None:
            '''
            :param interface_id: ``CfnDecoderManifest.ObdNetworkInterfaceProperty.InterfaceId``.
            :param obd_interface: ``CfnDecoderManifest.ObdNetworkInterfaceProperty.ObdInterface``.
            :param type: ``CfnDecoderManifest.ObdNetworkInterfaceProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdnetworkinterface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                # dtc_request_interval_seconds: Any
                # has_transmission_ecu: Any
                # pid_request_interval_seconds: Any
                # request_message_id: Any
                # use_extended_ids: Any
                
                obd_network_interface_property = iotfleetwise.CfnDecoderManifest.ObdNetworkInterfaceProperty(
                    interface_id="interfaceId",
                    obd_interface=iotfleetwise.CfnDecoderManifest.ObdInterfaceProperty(
                        name="name",
                        request_message_id=request_message_id,
                
                        # the properties below are optional
                        dtc_request_interval_seconds=dtc_request_interval_seconds,
                        has_transmission_ecu=has_transmission_ecu,
                        obd_standard="obdStandard",
                        pid_request_interval_seconds=pid_request_interval_seconds,
                        use_extended_ids=use_extended_ids
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDecoderManifest.ObdNetworkInterfaceProperty.__init__)
                check_type(argname="argument interface_id", value=interface_id, expected_type=type_hints["interface_id"])
                check_type(argname="argument obd_interface", value=obd_interface, expected_type=type_hints["obd_interface"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[str, typing.Any] = {
                "interface_id": interface_id,
                "obd_interface": obd_interface,
                "type": type,
            }

        @builtins.property
        def interface_id(self) -> builtins.str:
            '''``CfnDecoderManifest.ObdNetworkInterfaceProperty.InterfaceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdnetworkinterface.html#cfn-iotfleetwise-decodermanifest-obdnetworkinterface-interfaceid
            '''
            result = self._values.get("interface_id")
            assert result is not None, "Required property 'interface_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def obd_interface(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDecoderManifest.ObdInterfaceProperty"]:
            '''``CfnDecoderManifest.ObdNetworkInterfaceProperty.ObdInterface``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdnetworkinterface.html#cfn-iotfleetwise-decodermanifest-obdnetworkinterface-obdinterface
            '''
            result = self._values.get("obd_interface")
            assert result is not None, "Required property 'obd_interface' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDecoderManifest.ObdInterfaceProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnDecoderManifest.ObdNetworkInterfaceProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdnetworkinterface.html#cfn-iotfleetwise-decodermanifest-obdnetworkinterface-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObdNetworkInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnDecoderManifest.ObdSignalDecoderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "fully_qualified_name": "fullyQualifiedName",
            "interface_id": "interfaceId",
            "obd_signal": "obdSignal",
            "type": "type",
        },
    )
    class ObdSignalDecoderProperty:
        def __init__(
            self,
            *,
            fully_qualified_name: builtins.str,
            interface_id: builtins.str,
            obd_signal: typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnDecoderManifest.ObdSignalProperty", typing.Dict[str, typing.Any]]],
            type: builtins.str,
        ) -> None:
            '''
            :param fully_qualified_name: ``CfnDecoderManifest.ObdSignalDecoderProperty.FullyQualifiedName``.
            :param interface_id: ``CfnDecoderManifest.ObdSignalDecoderProperty.InterfaceId``.
            :param obd_signal: ``CfnDecoderManifest.ObdSignalDecoderProperty.ObdSignal``.
            :param type: ``CfnDecoderManifest.ObdSignalDecoderProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                # bit_mask_length: Any
                # bit_right_shift: Any
                # byte_length: Any
                # offset: Any
                # pid: Any
                # pid_response_length: Any
                # scaling: Any
                # service_mode: Any
                # start_byte: Any
                
                obd_signal_decoder_property = iotfleetwise.CfnDecoderManifest.ObdSignalDecoderProperty(
                    fully_qualified_name="fullyQualifiedName",
                    interface_id="interfaceId",
                    obd_signal=iotfleetwise.CfnDecoderManifest.ObdSignalProperty(
                        byte_length=byte_length,
                        offset=offset,
                        pid=pid,
                        pid_response_length=pid_response_length,
                        scaling=scaling,
                        service_mode=service_mode,
                        start_byte=start_byte,
                
                        # the properties below are optional
                        bit_mask_length=bit_mask_length,
                        bit_right_shift=bit_right_shift
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDecoderManifest.ObdSignalDecoderProperty.__init__)
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument interface_id", value=interface_id, expected_type=type_hints["interface_id"])
                check_type(argname="argument obd_signal", value=obd_signal, expected_type=type_hints["obd_signal"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[str, typing.Any] = {
                "fully_qualified_name": fully_qualified_name,
                "interface_id": interface_id,
                "obd_signal": obd_signal,
                "type": type,
            }

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''``CfnDecoderManifest.ObdSignalDecoderProperty.FullyQualifiedName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder.html#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def interface_id(self) -> builtins.str:
            '''``CfnDecoderManifest.ObdSignalDecoderProperty.InterfaceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder.html#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-interfaceid
            '''
            result = self._values.get("interface_id")
            assert result is not None, "Required property 'interface_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def obd_signal(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDecoderManifest.ObdSignalProperty"]:
            '''``CfnDecoderManifest.ObdSignalDecoderProperty.ObdSignal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder.html#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-obdsignal
            '''
            result = self._values.get("obd_signal")
            assert result is not None, "Required property 'obd_signal' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDecoderManifest.ObdSignalProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnDecoderManifest.ObdSignalDecoderProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder.html#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObdSignalDecoderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnDecoderManifest.ObdSignalProperty",
        jsii_struct_bases=[],
        name_mapping={
            "byte_length": "byteLength",
            "offset": "offset",
            "pid": "pid",
            "pid_response_length": "pidResponseLength",
            "scaling": "scaling",
            "service_mode": "serviceMode",
            "start_byte": "startByte",
            "bit_mask_length": "bitMaskLength",
            "bit_right_shift": "bitRightShift",
        },
    )
    class ObdSignalProperty:
        def __init__(
            self,
            *,
            byte_length: typing.Any,
            offset: typing.Any,
            pid: typing.Any,
            pid_response_length: typing.Any,
            scaling: typing.Any,
            service_mode: typing.Any,
            start_byte: typing.Any,
            bit_mask_length: typing.Any = None,
            bit_right_shift: typing.Any = None,
        ) -> None:
            '''
            :param byte_length: ``CfnDecoderManifest.ObdSignalProperty.ByteLength``.
            :param offset: ``CfnDecoderManifest.ObdSignalProperty.Offset``.
            :param pid: ``CfnDecoderManifest.ObdSignalProperty.Pid``.
            :param pid_response_length: ``CfnDecoderManifest.ObdSignalProperty.PidResponseLength``.
            :param scaling: ``CfnDecoderManifest.ObdSignalProperty.Scaling``.
            :param service_mode: ``CfnDecoderManifest.ObdSignalProperty.ServiceMode``.
            :param start_byte: ``CfnDecoderManifest.ObdSignalProperty.StartByte``.
            :param bit_mask_length: ``CfnDecoderManifest.ObdSignalProperty.BitMaskLength``.
            :param bit_right_shift: ``CfnDecoderManifest.ObdSignalProperty.BitRightShift``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                # bit_mask_length: Any
                # bit_right_shift: Any
                # byte_length: Any
                # offset: Any
                # pid: Any
                # pid_response_length: Any
                # scaling: Any
                # service_mode: Any
                # start_byte: Any
                
                obd_signal_property = iotfleetwise.CfnDecoderManifest.ObdSignalProperty(
                    byte_length=byte_length,
                    offset=offset,
                    pid=pid,
                    pid_response_length=pid_response_length,
                    scaling=scaling,
                    service_mode=service_mode,
                    start_byte=start_byte,
                
                    # the properties below are optional
                    bit_mask_length=bit_mask_length,
                    bit_right_shift=bit_right_shift
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDecoderManifest.ObdSignalProperty.__init__)
                check_type(argname="argument byte_length", value=byte_length, expected_type=type_hints["byte_length"])
                check_type(argname="argument offset", value=offset, expected_type=type_hints["offset"])
                check_type(argname="argument pid", value=pid, expected_type=type_hints["pid"])
                check_type(argname="argument pid_response_length", value=pid_response_length, expected_type=type_hints["pid_response_length"])
                check_type(argname="argument scaling", value=scaling, expected_type=type_hints["scaling"])
                check_type(argname="argument service_mode", value=service_mode, expected_type=type_hints["service_mode"])
                check_type(argname="argument start_byte", value=start_byte, expected_type=type_hints["start_byte"])
                check_type(argname="argument bit_mask_length", value=bit_mask_length, expected_type=type_hints["bit_mask_length"])
                check_type(argname="argument bit_right_shift", value=bit_right_shift, expected_type=type_hints["bit_right_shift"])
            self._values: typing.Dict[str, typing.Any] = {
                "byte_length": byte_length,
                "offset": offset,
                "pid": pid,
                "pid_response_length": pid_response_length,
                "scaling": scaling,
                "service_mode": service_mode,
                "start_byte": start_byte,
            }
            if bit_mask_length is not None:
                self._values["bit_mask_length"] = bit_mask_length
            if bit_right_shift is not None:
                self._values["bit_right_shift"] = bit_right_shift

        @builtins.property
        def byte_length(self) -> typing.Any:
            '''``CfnDecoderManifest.ObdSignalProperty.ByteLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-bytelength
            '''
            result = self._values.get("byte_length")
            assert result is not None, "Required property 'byte_length' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def offset(self) -> typing.Any:
            '''``CfnDecoderManifest.ObdSignalProperty.Offset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-offset
            '''
            result = self._values.get("offset")
            assert result is not None, "Required property 'offset' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def pid(self) -> typing.Any:
            '''``CfnDecoderManifest.ObdSignalProperty.Pid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-pid
            '''
            result = self._values.get("pid")
            assert result is not None, "Required property 'pid' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def pid_response_length(self) -> typing.Any:
            '''``CfnDecoderManifest.ObdSignalProperty.PidResponseLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-pidresponselength
            '''
            result = self._values.get("pid_response_length")
            assert result is not None, "Required property 'pid_response_length' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def scaling(self) -> typing.Any:
            '''``CfnDecoderManifest.ObdSignalProperty.Scaling``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-scaling
            '''
            result = self._values.get("scaling")
            assert result is not None, "Required property 'scaling' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def service_mode(self) -> typing.Any:
            '''``CfnDecoderManifest.ObdSignalProperty.ServiceMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-servicemode
            '''
            result = self._values.get("service_mode")
            assert result is not None, "Required property 'service_mode' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def start_byte(self) -> typing.Any:
            '''``CfnDecoderManifest.ObdSignalProperty.StartByte``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-startbyte
            '''
            result = self._values.get("start_byte")
            assert result is not None, "Required property 'start_byte' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def bit_mask_length(self) -> typing.Any:
            '''``CfnDecoderManifest.ObdSignalProperty.BitMaskLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-bitmasklength
            '''
            result = self._values.get("bit_mask_length")
            return typing.cast(typing.Any, result)

        @builtins.property
        def bit_right_shift(self) -> typing.Any:
            '''``CfnDecoderManifest.ObdSignalProperty.BitRightShift``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-bitrightshift
            '''
            result = self._values.get("bit_right_shift")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObdSignalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotfleetwise.CfnDecoderManifestProps",
    jsii_struct_bases=[],
    name_mapping={
        "model_manifest_arn": "modelManifestArn",
        "name": "name",
        "description": "description",
        "network_interfaces": "networkInterfaces",
        "signal_decoders": "signalDecoders",
        "status": "status",
        "tags": "tags",
    },
)
class CfnDecoderManifestProps:
    def __init__(
        self,
        *,
        model_manifest_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        network_interfaces: typing.Optional[typing.Union[typing.Sequence[typing.Any], aws_cdk.core.IResolvable]] = None,
        signal_decoders: typing.Optional[typing.Union[typing.Sequence[typing.Any], aws_cdk.core.IResolvable]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[aws_cdk.core.CfnTag, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDecoderManifest``.

        :param model_manifest_arn: ``AWS::IoTFleetWise::DecoderManifest.ModelManifestArn``.
        :param name: ``AWS::IoTFleetWise::DecoderManifest.Name``.
        :param description: ``AWS::IoTFleetWise::DecoderManifest.Description``.
        :param network_interfaces: ``AWS::IoTFleetWise::DecoderManifest.NetworkInterfaces``.
        :param signal_decoders: ``AWS::IoTFleetWise::DecoderManifest.SignalDecoders``.
        :param status: ``AWS::IoTFleetWise::DecoderManifest.Status``.
        :param tags: ``AWS::IoTFleetWise::DecoderManifest.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotfleetwise as iotfleetwise
            
            # network_interfaces: Any
            # signal_decoders: Any
            
            cfn_decoder_manifest_props = iotfleetwise.CfnDecoderManifestProps(
                model_manifest_arn="modelManifestArn",
                name="name",
            
                # the properties below are optional
                description="description",
                network_interfaces=[network_interfaces],
                signal_decoders=[signal_decoders],
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDecoderManifestProps.__init__)
            check_type(argname="argument model_manifest_arn", value=model_manifest_arn, expected_type=type_hints["model_manifest_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument network_interfaces", value=network_interfaces, expected_type=type_hints["network_interfaces"])
            check_type(argname="argument signal_decoders", value=signal_decoders, expected_type=type_hints["signal_decoders"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "model_manifest_arn": model_manifest_arn,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if network_interfaces is not None:
            self._values["network_interfaces"] = network_interfaces
        if signal_decoders is not None:
            self._values["signal_decoders"] = signal_decoders
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def model_manifest_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::DecoderManifest.ModelManifestArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-modelmanifestarn
        '''
        result = self._values.get("model_manifest_arn")
        assert result is not None, "Required property 'model_manifest_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::DecoderManifest.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::DecoderManifest.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_interfaces(
        self,
    ) -> typing.Optional[typing.Union[typing.List[typing.Any], aws_cdk.core.IResolvable]]:
        '''``AWS::IoTFleetWise::DecoderManifest.NetworkInterfaces``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-networkinterfaces
        '''
        result = self._values.get("network_interfaces")
        return typing.cast(typing.Optional[typing.Union[typing.List[typing.Any], aws_cdk.core.IResolvable]], result)

    @builtins.property
    def signal_decoders(
        self,
    ) -> typing.Optional[typing.Union[typing.List[typing.Any], aws_cdk.core.IResolvable]]:
        '''``AWS::IoTFleetWise::DecoderManifest.SignalDecoders``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-signaldecoders
        '''
        result = self._values.get("signal_decoders")
        return typing.cast(typing.Optional[typing.Union[typing.List[typing.Any], aws_cdk.core.IResolvable]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::DecoderManifest.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTFleetWise::DecoderManifest.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDecoderManifestProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFleet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotfleetwise.CfnFleet",
):
    '''A CloudFormation ``AWS::IoTFleetWise::Fleet``.

    :cloudformationResource: AWS::IoTFleetWise::Fleet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotfleetwise as iotfleetwise
        
        cfn_fleet = iotfleetwise.CfnFleet(self, "MyCfnFleet",
            id="id",
            signal_catalog_arn="signalCatalogArn",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id_: builtins.str,
        *,
        id: builtins.str,
        signal_catalog_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[aws_cdk.core.CfnTag, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTFleetWise::Fleet``.

        :param scope: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param id: ``AWS::IoTFleetWise::Fleet.Id``.
        :param signal_catalog_arn: ``AWS::IoTFleetWise::Fleet.SignalCatalogArn``.
        :param description: ``AWS::IoTFleetWise::Fleet.Description``.
        :param tags: ``AWS::IoTFleetWise::Fleet.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFleet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = CfnFleetProps(
            id=id,
            signal_catalog_arn=signal_catalog_arn,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFleet.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFleet._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTFleetWise::Fleet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Fleet.Id``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-id
        '''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFleet, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="signalCatalogArn")
    def signal_catalog_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Fleet.SignalCatalogArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-signalcatalogarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "signalCatalogArn"))

    @signal_catalog_arn.setter
    def signal_catalog_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFleet, "signal_catalog_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalCatalogArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Fleet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFleet, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotfleetwise.CfnFleetProps",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "signal_catalog_arn": "signalCatalogArn",
        "description": "description",
        "tags": "tags",
    },
)
class CfnFleetProps:
    def __init__(
        self,
        *,
        id: builtins.str,
        signal_catalog_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[aws_cdk.core.CfnTag, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFleet``.

        :param id: ``AWS::IoTFleetWise::Fleet.Id``.
        :param signal_catalog_arn: ``AWS::IoTFleetWise::Fleet.SignalCatalogArn``.
        :param description: ``AWS::IoTFleetWise::Fleet.Description``.
        :param tags: ``AWS::IoTFleetWise::Fleet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotfleetwise as iotfleetwise
            
            cfn_fleet_props = iotfleetwise.CfnFleetProps(
                id="id",
                signal_catalog_arn="signalCatalogArn",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFleetProps.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument signal_catalog_arn", value=signal_catalog_arn, expected_type=type_hints["signal_catalog_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
            "signal_catalog_arn": signal_catalog_arn,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def id(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Fleet.Id``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signal_catalog_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Fleet.SignalCatalogArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-signalcatalogarn
        '''
        result = self._values.get("signal_catalog_arn")
        assert result is not None, "Required property 'signal_catalog_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Fleet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTFleetWise::Fleet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFleetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModelManifest(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotfleetwise.CfnModelManifest",
):
    '''A CloudFormation ``AWS::IoTFleetWise::ModelManifest``.

    :cloudformationResource: AWS::IoTFleetWise::ModelManifest
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotfleetwise as iotfleetwise
        
        cfn_model_manifest = iotfleetwise.CfnModelManifest(self, "MyCfnModelManifest",
            name="name",
            signal_catalog_arn="signalCatalogArn",
        
            # the properties below are optional
            description="description",
            nodes=["nodes"],
            status="status",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        signal_catalog_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        nodes: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[aws_cdk.core.CfnTag, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTFleetWise::ModelManifest``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::IoTFleetWise::ModelManifest.Name``.
        :param signal_catalog_arn: ``AWS::IoTFleetWise::ModelManifest.SignalCatalogArn``.
        :param description: ``AWS::IoTFleetWise::ModelManifest.Description``.
        :param nodes: ``AWS::IoTFleetWise::ModelManifest.Nodes``.
        :param status: ``AWS::IoTFleetWise::ModelManifest.Status``.
        :param tags: ``AWS::IoTFleetWise::ModelManifest.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnModelManifest.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnModelManifestProps(
            name=name,
            signal_catalog_arn=signal_catalog_arn,
            description=description,
            nodes=nodes,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnModelManifest.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnModelManifest._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTFleetWise::ModelManifest.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::ModelManifest.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnModelManifest, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="signalCatalogArn")
    def signal_catalog_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::ModelManifest.SignalCatalogArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-signalcatalogarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "signalCatalogArn"))

    @signal_catalog_arn.setter
    def signal_catalog_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnModelManifest, "signal_catalog_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalCatalogArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::ModelManifest.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnModelManifest, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="nodes")
    def nodes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::IoTFleetWise::ModelManifest.Nodes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-nodes
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nodes"))

    @nodes.setter
    def nodes(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnModelManifest, "nodes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodes", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::ModelManifest.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnModelManifest, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotfleetwise.CfnModelManifestProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "signal_catalog_arn": "signalCatalogArn",
        "description": "description",
        "nodes": "nodes",
        "status": "status",
        "tags": "tags",
    },
)
class CfnModelManifestProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        signal_catalog_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        nodes: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[aws_cdk.core.CfnTag, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnModelManifest``.

        :param name: ``AWS::IoTFleetWise::ModelManifest.Name``.
        :param signal_catalog_arn: ``AWS::IoTFleetWise::ModelManifest.SignalCatalogArn``.
        :param description: ``AWS::IoTFleetWise::ModelManifest.Description``.
        :param nodes: ``AWS::IoTFleetWise::ModelManifest.Nodes``.
        :param status: ``AWS::IoTFleetWise::ModelManifest.Status``.
        :param tags: ``AWS::IoTFleetWise::ModelManifest.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotfleetwise as iotfleetwise
            
            cfn_model_manifest_props = iotfleetwise.CfnModelManifestProps(
                name="name",
                signal_catalog_arn="signalCatalogArn",
            
                # the properties below are optional
                description="description",
                nodes=["nodes"],
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnModelManifestProps.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument signal_catalog_arn", value=signal_catalog_arn, expected_type=type_hints["signal_catalog_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument nodes", value=nodes, expected_type=type_hints["nodes"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "signal_catalog_arn": signal_catalog_arn,
        }
        if description is not None:
            self._values["description"] = description
        if nodes is not None:
            self._values["nodes"] = nodes
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::ModelManifest.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signal_catalog_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::ModelManifest.SignalCatalogArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-signalcatalogarn
        '''
        result = self._values.get("signal_catalog_arn")
        assert result is not None, "Required property 'signal_catalog_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::ModelManifest.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nodes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::IoTFleetWise::ModelManifest.Nodes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-nodes
        '''
        result = self._values.get("nodes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::ModelManifest.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTFleetWise::ModelManifest.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelManifestProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSignalCatalog(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotfleetwise.CfnSignalCatalog",
):
    '''A CloudFormation ``AWS::IoTFleetWise::SignalCatalog``.

    :cloudformationResource: AWS::IoTFleetWise::SignalCatalog
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotfleetwise as iotfleetwise
        
        cfn_signal_catalog = iotfleetwise.CfnSignalCatalog(self, "MyCfnSignalCatalog",
            description="description",
            name="name",
            nodes=[iotfleetwise.CfnSignalCatalog.NodeProperty(
                actuator=iotfleetwise.CfnSignalCatalog.ActuatorProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
        
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    assigned_value="assignedValue",
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                ),
                attribute=iotfleetwise.CfnSignalCatalog.AttributeProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
        
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    assigned_value="assignedValue",
                    default_value="defaultValue",
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                ),
                branch=iotfleetwise.CfnSignalCatalog.BranchProperty(
                    fully_qualified_name="fullyQualifiedName",
        
                    # the properties below are optional
                    description="description"
                ),
                sensor=iotfleetwise.CfnSignalCatalog.SensorProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
        
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                )
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        nodes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnSignalCatalog.NodeProperty", typing.Dict[str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[aws_cdk.core.CfnTag, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTFleetWise::SignalCatalog``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::IoTFleetWise::SignalCatalog.Description``.
        :param name: ``AWS::IoTFleetWise::SignalCatalog.Name``.
        :param nodes: ``AWS::IoTFleetWise::SignalCatalog.Nodes``.
        :param tags: ``AWS::IoTFleetWise::SignalCatalog.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSignalCatalog.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSignalCatalogProps(
            description=description, name=name, nodes=nodes, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSignalCatalog.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSignalCatalog._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCountsTotalActuators")
    def attr_node_counts_total_actuators(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: NodeCounts.TotalActuators
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrNodeCountsTotalActuators"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCountsTotalAttributes")
    def attr_node_counts_total_attributes(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: NodeCounts.TotalAttributes
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrNodeCountsTotalAttributes"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCountsTotalBranches")
    def attr_node_counts_total_branches(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: NodeCounts.TotalBranches
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrNodeCountsTotalBranches"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCountsTotalNodes")
    def attr_node_counts_total_nodes(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: NodeCounts.TotalNodes
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrNodeCountsTotalNodes"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCountsTotalSensors")
    def attr_node_counts_total_sensors(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: NodeCounts.TotalSensors
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrNodeCountsTotalSensors"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTFleetWise::SignalCatalog.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::SignalCatalog.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSignalCatalog, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::SignalCatalog.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSignalCatalog, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nodes")
    def nodes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSignalCatalog.NodeProperty"]]]]:
        '''``AWS::IoTFleetWise::SignalCatalog.Nodes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-nodes
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSignalCatalog.NodeProperty"]]]], jsii.get(self, "nodes"))

    @nodes.setter
    def nodes(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSignalCatalog.NodeProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSignalCatalog, "nodes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodes", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnSignalCatalog.ActuatorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_type": "dataType",
            "fully_qualified_name": "fullyQualifiedName",
            "allowed_values": "allowedValues",
            "assigned_value": "assignedValue",
            "description": "description",
            "max": "max",
            "min": "min",
            "unit": "unit",
        },
    )
    class ActuatorProperty:
        def __init__(
            self,
            *,
            data_type: builtins.str,
            fully_qualified_name: builtins.str,
            allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
            assigned_value: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            max: typing.Optional[jsii.Number] = None,
            min: typing.Optional[jsii.Number] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param data_type: ``CfnSignalCatalog.ActuatorProperty.DataType``.
            :param fully_qualified_name: ``CfnSignalCatalog.ActuatorProperty.FullyQualifiedName``.
            :param allowed_values: ``CfnSignalCatalog.ActuatorProperty.AllowedValues``.
            :param assigned_value: ``CfnSignalCatalog.ActuatorProperty.AssignedValue``.
            :param description: ``CfnSignalCatalog.ActuatorProperty.Description``.
            :param max: ``CfnSignalCatalog.ActuatorProperty.Max``.
            :param min: ``CfnSignalCatalog.ActuatorProperty.Min``.
            :param unit: ``CfnSignalCatalog.ActuatorProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                actuator_property = iotfleetwise.CfnSignalCatalog.ActuatorProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
                
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    assigned_value="assignedValue",
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSignalCatalog.ActuatorProperty.__init__)
                check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument allowed_values", value=allowed_values, expected_type=type_hints["allowed_values"])
                check_type(argname="argument assigned_value", value=assigned_value, expected_type=type_hints["assigned_value"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument max", value=max, expected_type=type_hints["max"])
                check_type(argname="argument min", value=min, expected_type=type_hints["min"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[str, typing.Any] = {
                "data_type": data_type,
                "fully_qualified_name": fully_qualified_name,
            }
            if allowed_values is not None:
                self._values["allowed_values"] = allowed_values
            if assigned_value is not None:
                self._values["assigned_value"] = assigned_value
            if description is not None:
                self._values["description"] = description
            if max is not None:
                self._values["max"] = max
            if min is not None:
                self._values["min"] = min
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def data_type(self) -> builtins.str:
            '''``CfnSignalCatalog.ActuatorProperty.DataType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-datatype
            '''
            result = self._values.get("data_type")
            assert result is not None, "Required property 'data_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''``CfnSignalCatalog.ActuatorProperty.FullyQualifiedName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allowed_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnSignalCatalog.ActuatorProperty.AllowedValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-allowedvalues
            '''
            result = self._values.get("allowed_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def assigned_value(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.ActuatorProperty.AssignedValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-assignedvalue
            '''
            result = self._values.get("assigned_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.ActuatorProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.ActuatorProperty.Max``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-max
            '''
            result = self._values.get("max")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.ActuatorProperty.Min``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-min
            '''
            result = self._values.get("min")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.ActuatorProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActuatorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnSignalCatalog.AttributeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_type": "dataType",
            "fully_qualified_name": "fullyQualifiedName",
            "allowed_values": "allowedValues",
            "assigned_value": "assignedValue",
            "default_value": "defaultValue",
            "description": "description",
            "max": "max",
            "min": "min",
            "unit": "unit",
        },
    )
    class AttributeProperty:
        def __init__(
            self,
            *,
            data_type: builtins.str,
            fully_qualified_name: builtins.str,
            allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
            assigned_value: typing.Optional[builtins.str] = None,
            default_value: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            max: typing.Optional[jsii.Number] = None,
            min: typing.Optional[jsii.Number] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param data_type: ``CfnSignalCatalog.AttributeProperty.DataType``.
            :param fully_qualified_name: ``CfnSignalCatalog.AttributeProperty.FullyQualifiedName``.
            :param allowed_values: ``CfnSignalCatalog.AttributeProperty.AllowedValues``.
            :param assigned_value: ``CfnSignalCatalog.AttributeProperty.AssignedValue``.
            :param default_value: ``CfnSignalCatalog.AttributeProperty.DefaultValue``.
            :param description: ``CfnSignalCatalog.AttributeProperty.Description``.
            :param max: ``CfnSignalCatalog.AttributeProperty.Max``.
            :param min: ``CfnSignalCatalog.AttributeProperty.Min``.
            :param unit: ``CfnSignalCatalog.AttributeProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                attribute_property = iotfleetwise.CfnSignalCatalog.AttributeProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
                
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    assigned_value="assignedValue",
                    default_value="defaultValue",
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSignalCatalog.AttributeProperty.__init__)
                check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument allowed_values", value=allowed_values, expected_type=type_hints["allowed_values"])
                check_type(argname="argument assigned_value", value=assigned_value, expected_type=type_hints["assigned_value"])
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument max", value=max, expected_type=type_hints["max"])
                check_type(argname="argument min", value=min, expected_type=type_hints["min"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[str, typing.Any] = {
                "data_type": data_type,
                "fully_qualified_name": fully_qualified_name,
            }
            if allowed_values is not None:
                self._values["allowed_values"] = allowed_values
            if assigned_value is not None:
                self._values["assigned_value"] = assigned_value
            if default_value is not None:
                self._values["default_value"] = default_value
            if description is not None:
                self._values["description"] = description
            if max is not None:
                self._values["max"] = max
            if min is not None:
                self._values["min"] = min
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def data_type(self) -> builtins.str:
            '''``CfnSignalCatalog.AttributeProperty.DataType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-datatype
            '''
            result = self._values.get("data_type")
            assert result is not None, "Required property 'data_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''``CfnSignalCatalog.AttributeProperty.FullyQualifiedName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allowed_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnSignalCatalog.AttributeProperty.AllowedValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-allowedvalues
            '''
            result = self._values.get("allowed_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def assigned_value(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.AttributeProperty.AssignedValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-assignedvalue
            '''
            result = self._values.get("assigned_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def default_value(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.AttributeProperty.DefaultValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.AttributeProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.AttributeProperty.Max``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-max
            '''
            result = self._values.get("max")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.AttributeProperty.Min``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-min
            '''
            result = self._values.get("min")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.AttributeProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnSignalCatalog.BranchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "fully_qualified_name": "fullyQualifiedName",
            "description": "description",
        },
    )
    class BranchProperty:
        def __init__(
            self,
            *,
            fully_qualified_name: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param fully_qualified_name: ``CfnSignalCatalog.BranchProperty.FullyQualifiedName``.
            :param description: ``CfnSignalCatalog.BranchProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-branch.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                branch_property = iotfleetwise.CfnSignalCatalog.BranchProperty(
                    fully_qualified_name="fullyQualifiedName",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSignalCatalog.BranchProperty.__init__)
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[str, typing.Any] = {
                "fully_qualified_name": fully_qualified_name,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''``CfnSignalCatalog.BranchProperty.FullyQualifiedName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-branch.html#cfn-iotfleetwise-signalcatalog-branch-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.BranchProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-branch.html#cfn-iotfleetwise-signalcatalog-branch-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BranchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnSignalCatalog.NodeCountsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "total_actuators": "totalActuators",
            "total_attributes": "totalAttributes",
            "total_branches": "totalBranches",
            "total_nodes": "totalNodes",
            "total_sensors": "totalSensors",
        },
    )
    class NodeCountsProperty:
        def __init__(
            self,
            *,
            total_actuators: typing.Optional[jsii.Number] = None,
            total_attributes: typing.Optional[jsii.Number] = None,
            total_branches: typing.Optional[jsii.Number] = None,
            total_nodes: typing.Optional[jsii.Number] = None,
            total_sensors: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param total_actuators: ``CfnSignalCatalog.NodeCountsProperty.TotalActuators``.
            :param total_attributes: ``CfnSignalCatalog.NodeCountsProperty.TotalAttributes``.
            :param total_branches: ``CfnSignalCatalog.NodeCountsProperty.TotalBranches``.
            :param total_nodes: ``CfnSignalCatalog.NodeCountsProperty.TotalNodes``.
            :param total_sensors: ``CfnSignalCatalog.NodeCountsProperty.TotalSensors``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                node_counts_property = iotfleetwise.CfnSignalCatalog.NodeCountsProperty(
                    total_actuators=123,
                    total_attributes=123,
                    total_branches=123,
                    total_nodes=123,
                    total_sensors=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSignalCatalog.NodeCountsProperty.__init__)
                check_type(argname="argument total_actuators", value=total_actuators, expected_type=type_hints["total_actuators"])
                check_type(argname="argument total_attributes", value=total_attributes, expected_type=type_hints["total_attributes"])
                check_type(argname="argument total_branches", value=total_branches, expected_type=type_hints["total_branches"])
                check_type(argname="argument total_nodes", value=total_nodes, expected_type=type_hints["total_nodes"])
                check_type(argname="argument total_sensors", value=total_sensors, expected_type=type_hints["total_sensors"])
            self._values: typing.Dict[str, typing.Any] = {}
            if total_actuators is not None:
                self._values["total_actuators"] = total_actuators
            if total_attributes is not None:
                self._values["total_attributes"] = total_attributes
            if total_branches is not None:
                self._values["total_branches"] = total_branches
            if total_nodes is not None:
                self._values["total_nodes"] = total_nodes
            if total_sensors is not None:
                self._values["total_sensors"] = total_sensors

        @builtins.property
        def total_actuators(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.NodeCountsProperty.TotalActuators``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalactuators
            '''
            result = self._values.get("total_actuators")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total_attributes(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.NodeCountsProperty.TotalAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalattributes
            '''
            result = self._values.get("total_attributes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total_branches(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.NodeCountsProperty.TotalBranches``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalbranches
            '''
            result = self._values.get("total_branches")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total_nodes(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.NodeCountsProperty.TotalNodes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalnodes
            '''
            result = self._values.get("total_nodes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total_sensors(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.NodeCountsProperty.TotalSensors``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalsensors
            '''
            result = self._values.get("total_sensors")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodeCountsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnSignalCatalog.NodeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "actuator": "actuator",
            "attribute": "attribute",
            "branch": "branch",
            "sensor": "sensor",
        },
    )
    class NodeProperty:
        def __init__(
            self,
            *,
            actuator: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnSignalCatalog.ActuatorProperty", typing.Dict[str, typing.Any]]]] = None,
            attribute: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnSignalCatalog.AttributeProperty", typing.Dict[str, typing.Any]]]] = None,
            branch: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnSignalCatalog.BranchProperty", typing.Dict[str, typing.Any]]]] = None,
            sensor: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnSignalCatalog.SensorProperty", typing.Dict[str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param actuator: ``CfnSignalCatalog.NodeProperty.Actuator``.
            :param attribute: ``CfnSignalCatalog.NodeProperty.Attribute``.
            :param branch: ``CfnSignalCatalog.NodeProperty.Branch``.
            :param sensor: ``CfnSignalCatalog.NodeProperty.Sensor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                node_property = iotfleetwise.CfnSignalCatalog.NodeProperty(
                    actuator=iotfleetwise.CfnSignalCatalog.ActuatorProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
                
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        assigned_value="assignedValue",
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    ),
                    attribute=iotfleetwise.CfnSignalCatalog.AttributeProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
                
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        assigned_value="assignedValue",
                        default_value="defaultValue",
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    ),
                    branch=iotfleetwise.CfnSignalCatalog.BranchProperty(
                        fully_qualified_name="fullyQualifiedName",
                
                        # the properties below are optional
                        description="description"
                    ),
                    sensor=iotfleetwise.CfnSignalCatalog.SensorProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
                
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSignalCatalog.NodeProperty.__init__)
                check_type(argname="argument actuator", value=actuator, expected_type=type_hints["actuator"])
                check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
                check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
                check_type(argname="argument sensor", value=sensor, expected_type=type_hints["sensor"])
            self._values: typing.Dict[str, typing.Any] = {}
            if actuator is not None:
                self._values["actuator"] = actuator
            if attribute is not None:
                self._values["attribute"] = attribute
            if branch is not None:
                self._values["branch"] = branch
            if sensor is not None:
                self._values["sensor"] = sensor

        @builtins.property
        def actuator(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSignalCatalog.ActuatorProperty"]]:
            '''``CfnSignalCatalog.NodeProperty.Actuator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-actuator
            '''
            result = self._values.get("actuator")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSignalCatalog.ActuatorProperty"]], result)

        @builtins.property
        def attribute(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSignalCatalog.AttributeProperty"]]:
            '''``CfnSignalCatalog.NodeProperty.Attribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-attribute
            '''
            result = self._values.get("attribute")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSignalCatalog.AttributeProperty"]], result)

        @builtins.property
        def branch(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSignalCatalog.BranchProperty"]]:
            '''``CfnSignalCatalog.NodeProperty.Branch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-branch
            '''
            result = self._values.get("branch")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSignalCatalog.BranchProperty"]], result)

        @builtins.property
        def sensor(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSignalCatalog.SensorProperty"]]:
            '''``CfnSignalCatalog.NodeProperty.Sensor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-sensor
            '''
            result = self._values.get("sensor")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSignalCatalog.SensorProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotfleetwise.CfnSignalCatalog.SensorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_type": "dataType",
            "fully_qualified_name": "fullyQualifiedName",
            "allowed_values": "allowedValues",
            "description": "description",
            "max": "max",
            "min": "min",
            "unit": "unit",
        },
    )
    class SensorProperty:
        def __init__(
            self,
            *,
            data_type: builtins.str,
            fully_qualified_name: builtins.str,
            allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
            description: typing.Optional[builtins.str] = None,
            max: typing.Optional[jsii.Number] = None,
            min: typing.Optional[jsii.Number] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param data_type: ``CfnSignalCatalog.SensorProperty.DataType``.
            :param fully_qualified_name: ``CfnSignalCatalog.SensorProperty.FullyQualifiedName``.
            :param allowed_values: ``CfnSignalCatalog.SensorProperty.AllowedValues``.
            :param description: ``CfnSignalCatalog.SensorProperty.Description``.
            :param max: ``CfnSignalCatalog.SensorProperty.Max``.
            :param min: ``CfnSignalCatalog.SensorProperty.Min``.
            :param unit: ``CfnSignalCatalog.SensorProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotfleetwise as iotfleetwise
                
                sensor_property = iotfleetwise.CfnSignalCatalog.SensorProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
                
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSignalCatalog.SensorProperty.__init__)
                check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument allowed_values", value=allowed_values, expected_type=type_hints["allowed_values"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument max", value=max, expected_type=type_hints["max"])
                check_type(argname="argument min", value=min, expected_type=type_hints["min"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[str, typing.Any] = {
                "data_type": data_type,
                "fully_qualified_name": fully_qualified_name,
            }
            if allowed_values is not None:
                self._values["allowed_values"] = allowed_values
            if description is not None:
                self._values["description"] = description
            if max is not None:
                self._values["max"] = max
            if min is not None:
                self._values["min"] = min
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def data_type(self) -> builtins.str:
            '''``CfnSignalCatalog.SensorProperty.DataType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-datatype
            '''
            result = self._values.get("data_type")
            assert result is not None, "Required property 'data_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''``CfnSignalCatalog.SensorProperty.FullyQualifiedName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allowed_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnSignalCatalog.SensorProperty.AllowedValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-allowedvalues
            '''
            result = self._values.get("allowed_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.SensorProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.SensorProperty.Max``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-max
            '''
            result = self._values.get("max")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.SensorProperty.Min``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-min
            '''
            result = self._values.get("min")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.SensorProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SensorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotfleetwise.CfnSignalCatalogProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "name": "name",
        "nodes": "nodes",
        "tags": "tags",
    },
)
class CfnSignalCatalogProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        nodes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnSignalCatalog.NodeProperty, typing.Dict[str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[aws_cdk.core.CfnTag, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSignalCatalog``.

        :param description: ``AWS::IoTFleetWise::SignalCatalog.Description``.
        :param name: ``AWS::IoTFleetWise::SignalCatalog.Name``.
        :param nodes: ``AWS::IoTFleetWise::SignalCatalog.Nodes``.
        :param tags: ``AWS::IoTFleetWise::SignalCatalog.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotfleetwise as iotfleetwise
            
            cfn_signal_catalog_props = iotfleetwise.CfnSignalCatalogProps(
                description="description",
                name="name",
                nodes=[iotfleetwise.CfnSignalCatalog.NodeProperty(
                    actuator=iotfleetwise.CfnSignalCatalog.ActuatorProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
            
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        assigned_value="assignedValue",
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    ),
                    attribute=iotfleetwise.CfnSignalCatalog.AttributeProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
            
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        assigned_value="assignedValue",
                        default_value="defaultValue",
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    ),
                    branch=iotfleetwise.CfnSignalCatalog.BranchProperty(
                        fully_qualified_name="fullyQualifiedName",
            
                        # the properties below are optional
                        description="description"
                    ),
                    sensor=iotfleetwise.CfnSignalCatalog.SensorProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
            
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    )
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSignalCatalogProps.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument nodes", value=nodes, expected_type=type_hints["nodes"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if nodes is not None:
            self._values["nodes"] = nodes
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::SignalCatalog.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::SignalCatalog.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nodes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnSignalCatalog.NodeProperty]]]]:
        '''``AWS::IoTFleetWise::SignalCatalog.Nodes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-nodes
        '''
        result = self._values.get("nodes")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnSignalCatalog.NodeProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTFleetWise::SignalCatalog.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSignalCatalogProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnVehicle(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotfleetwise.CfnVehicle",
):
    '''A CloudFormation ``AWS::IoTFleetWise::Vehicle``.

    :cloudformationResource: AWS::IoTFleetWise::Vehicle
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotfleetwise as iotfleetwise
        
        cfn_vehicle = iotfleetwise.CfnVehicle(self, "MyCfnVehicle",
            decoder_manifest_arn="decoderManifestArn",
            model_manifest_arn="modelManifestArn",
            name="name",
        
            # the properties below are optional
            association_behavior="associationBehavior",
            attributes={
                "attributes_key": "attributes"
            },
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        decoder_manifest_arn: builtins.str,
        model_manifest_arn: builtins.str,
        name: builtins.str,
        association_behavior: typing.Optional[builtins.str] = None,
        attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[aws_cdk.core.CfnTag, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTFleetWise::Vehicle``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param decoder_manifest_arn: ``AWS::IoTFleetWise::Vehicle.DecoderManifestArn``.
        :param model_manifest_arn: ``AWS::IoTFleetWise::Vehicle.ModelManifestArn``.
        :param name: ``AWS::IoTFleetWise::Vehicle.Name``.
        :param association_behavior: ``AWS::IoTFleetWise::Vehicle.AssociationBehavior``.
        :param attributes: ``AWS::IoTFleetWise::Vehicle.Attributes``.
        :param tags: ``AWS::IoTFleetWise::Vehicle.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnVehicle.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVehicleProps(
            decoder_manifest_arn=decoder_manifest_arn,
            model_manifest_arn=model_manifest_arn,
            name=name,
            association_behavior=association_behavior,
            attributes=attributes,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnVehicle.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnVehicle._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTFleetWise::Vehicle.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="decoderManifestArn")
    def decoder_manifest_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Vehicle.DecoderManifestArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-decodermanifestarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "decoderManifestArn"))

    @decoder_manifest_arn.setter
    def decoder_manifest_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVehicle, "decoder_manifest_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "decoderManifestArn", value)

    @builtins.property
    @jsii.member(jsii_name="modelManifestArn")
    def model_manifest_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Vehicle.ModelManifestArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-modelmanifestarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "modelManifestArn"))

    @model_manifest_arn.setter
    def model_manifest_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVehicle, "model_manifest_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelManifestArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Vehicle.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVehicle, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="associationBehavior")
    def association_behavior(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Vehicle.AssociationBehavior``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-associationbehavior
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associationBehavior"))

    @association_behavior.setter
    def association_behavior(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVehicle, "association_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associationBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::IoTFleetWise::Vehicle.Attributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-attributes
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVehicle, "attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributes", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotfleetwise.CfnVehicleProps",
    jsii_struct_bases=[],
    name_mapping={
        "decoder_manifest_arn": "decoderManifestArn",
        "model_manifest_arn": "modelManifestArn",
        "name": "name",
        "association_behavior": "associationBehavior",
        "attributes": "attributes",
        "tags": "tags",
    },
)
class CfnVehicleProps:
    def __init__(
        self,
        *,
        decoder_manifest_arn: builtins.str,
        model_manifest_arn: builtins.str,
        name: builtins.str,
        association_behavior: typing.Optional[builtins.str] = None,
        attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[aws_cdk.core.CfnTag, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVehicle``.

        :param decoder_manifest_arn: ``AWS::IoTFleetWise::Vehicle.DecoderManifestArn``.
        :param model_manifest_arn: ``AWS::IoTFleetWise::Vehicle.ModelManifestArn``.
        :param name: ``AWS::IoTFleetWise::Vehicle.Name``.
        :param association_behavior: ``AWS::IoTFleetWise::Vehicle.AssociationBehavior``.
        :param attributes: ``AWS::IoTFleetWise::Vehicle.Attributes``.
        :param tags: ``AWS::IoTFleetWise::Vehicle.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotfleetwise as iotfleetwise
            
            cfn_vehicle_props = iotfleetwise.CfnVehicleProps(
                decoder_manifest_arn="decoderManifestArn",
                model_manifest_arn="modelManifestArn",
                name="name",
            
                # the properties below are optional
                association_behavior="associationBehavior",
                attributes={
                    "attributes_key": "attributes"
                },
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnVehicleProps.__init__)
            check_type(argname="argument decoder_manifest_arn", value=decoder_manifest_arn, expected_type=type_hints["decoder_manifest_arn"])
            check_type(argname="argument model_manifest_arn", value=model_manifest_arn, expected_type=type_hints["model_manifest_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument association_behavior", value=association_behavior, expected_type=type_hints["association_behavior"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "decoder_manifest_arn": decoder_manifest_arn,
            "model_manifest_arn": model_manifest_arn,
            "name": name,
        }
        if association_behavior is not None:
            self._values["association_behavior"] = association_behavior
        if attributes is not None:
            self._values["attributes"] = attributes
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def decoder_manifest_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Vehicle.DecoderManifestArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-decodermanifestarn
        '''
        result = self._values.get("decoder_manifest_arn")
        assert result is not None, "Required property 'decoder_manifest_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model_manifest_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Vehicle.ModelManifestArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-modelmanifestarn
        '''
        result = self._values.get("model_manifest_arn")
        assert result is not None, "Required property 'model_manifest_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Vehicle.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def association_behavior(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Vehicle.AssociationBehavior``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-associationbehavior
        '''
        result = self._values.get("association_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::IoTFleetWise::Vehicle.Attributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-attributes
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTFleetWise::Vehicle.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVehicleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCampaign",
    "CfnCampaignProps",
    "CfnDecoderManifest",
    "CfnDecoderManifestProps",
    "CfnFleet",
    "CfnFleetProps",
    "CfnModelManifest",
    "CfnModelManifestProps",
    "CfnSignalCatalog",
    "CfnSignalCatalogProps",
    "CfnVehicle",
    "CfnVehicleProps",
]

publication.publish()
