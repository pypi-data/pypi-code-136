"""
Type annotations for chime-sdk-messaging service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/type_defs/)

Usage::

    ```python
    from mypy_boto3_chime_sdk_messaging.type_defs import AppInstanceUserMembershipSummaryTypeDef

    data: AppInstanceUserMembershipSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AllowNotificationsType,
    ChannelMembershipTypeType,
    ChannelMessagePersistenceTypeType,
    ChannelMessageStatusType,
    ChannelMessageTypeType,
    ChannelModeType,
    ChannelPrivacyType,
    ErrorCodeType,
    FallbackActionType,
    PushNotificationTypeType,
    SearchFieldOperatorType,
    SortOrderType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AppInstanceUserMembershipSummaryTypeDef",
    "AssociateChannelFlowRequestRequestTypeDef",
    "IdentityTypeDef",
    "BatchCreateChannelMembershipErrorTypeDef",
    "BatchCreateChannelMembershipRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ChannelAssociatedWithFlowSummaryTypeDef",
    "ChannelSummaryTypeDef",
    "PushNotificationPreferencesTypeDef",
    "MessageAttributeValueTypeDef",
    "PushNotificationConfigurationTypeDef",
    "ChannelMessageStatusStructureTypeDef",
    "ElasticChannelConfigurationTypeDef",
    "CreateChannelBanRequestRequestTypeDef",
    "TagTypeDef",
    "CreateChannelMembershipRequestRequestTypeDef",
    "CreateChannelModeratorRequestRequestTypeDef",
    "DeleteChannelBanRequestRequestTypeDef",
    "DeleteChannelFlowRequestRequestTypeDef",
    "DeleteChannelMembershipRequestRequestTypeDef",
    "DeleteChannelMessageRequestRequestTypeDef",
    "DeleteChannelModeratorRequestRequestTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DescribeChannelBanRequestRequestTypeDef",
    "DescribeChannelFlowRequestRequestTypeDef",
    "DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef",
    "DescribeChannelMembershipRequestRequestTypeDef",
    "DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef",
    "DescribeChannelModeratorRequestRequestTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DisassociateChannelFlowRequestRequestTypeDef",
    "GetChannelMembershipPreferencesRequestRequestTypeDef",
    "GetChannelMessageRequestRequestTypeDef",
    "GetChannelMessageStatusRequestRequestTypeDef",
    "MessagingSessionEndpointTypeDef",
    "LambdaConfigurationTypeDef",
    "ListChannelBansRequestRequestTypeDef",
    "ListChannelFlowsRequestRequestTypeDef",
    "ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    "ListChannelMembershipsRequestRequestTypeDef",
    "ListChannelMessagesRequestRequestTypeDef",
    "ListChannelModeratorsRequestRequestTypeDef",
    "ListChannelsAssociatedWithChannelFlowRequestRequestTypeDef",
    "ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListSubChannelsRequestRequestTypeDef",
    "SubChannelSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RedactChannelMessageRequestRequestTypeDef",
    "SearchFieldTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateChannelMessageRequestRequestTypeDef",
    "UpdateChannelReadMarkerRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "BatchChannelMembershipsTypeDef",
    "ChannelBanSummaryTypeDef",
    "ChannelBanTypeDef",
    "ChannelMembershipSummaryTypeDef",
    "ChannelMembershipTypeDef",
    "ChannelModeratorSummaryTypeDef",
    "ChannelModeratorTypeDef",
    "ChannelFlowCallbackResponseTypeDef",
    "CreateChannelBanResponseTypeDef",
    "CreateChannelFlowResponseTypeDef",
    "CreateChannelMembershipResponseTypeDef",
    "CreateChannelModeratorResponseTypeDef",
    "CreateChannelResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "RedactChannelMessageResponseTypeDef",
    "UpdateChannelFlowResponseTypeDef",
    "UpdateChannelReadMarkerResponseTypeDef",
    "UpdateChannelResponseTypeDef",
    "ListChannelsAssociatedWithChannelFlowResponseTypeDef",
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    "ListChannelsResponseTypeDef",
    "SearchChannelsResponseTypeDef",
    "ChannelMembershipPreferencesTypeDef",
    "ChannelMessageCallbackTypeDef",
    "SendChannelMessageRequestRequestTypeDef",
    "ChannelMessageSummaryTypeDef",
    "ChannelMessageTypeDef",
    "GetChannelMessageStatusResponseTypeDef",
    "SendChannelMessageResponseTypeDef",
    "UpdateChannelMessageResponseTypeDef",
    "ChannelTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "GetMessagingSessionEndpointResponseTypeDef",
    "ProcessorConfigurationTypeDef",
    "ListSubChannelsResponseTypeDef",
    "SearchChannelsRequestRequestTypeDef",
    "BatchCreateChannelMembershipResponseTypeDef",
    "ListChannelBansResponseTypeDef",
    "DescribeChannelBanResponseTypeDef",
    "ListChannelMembershipsResponseTypeDef",
    "DescribeChannelMembershipResponseTypeDef",
    "ListChannelModeratorsResponseTypeDef",
    "DescribeChannelModeratorResponseTypeDef",
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    "GetChannelMembershipPreferencesResponseTypeDef",
    "PutChannelMembershipPreferencesRequestRequestTypeDef",
    "PutChannelMembershipPreferencesResponseTypeDef",
    "ChannelFlowCallbackRequestRequestTypeDef",
    "ListChannelMessagesResponseTypeDef",
    "GetChannelMessageResponseTypeDef",
    "DescribeChannelResponseTypeDef",
    "ProcessorTypeDef",
    "ChannelFlowSummaryTypeDef",
    "ChannelFlowTypeDef",
    "CreateChannelFlowRequestRequestTypeDef",
    "UpdateChannelFlowRequestRequestTypeDef",
    "ListChannelFlowsResponseTypeDef",
    "DescribeChannelFlowResponseTypeDef",
)

AppInstanceUserMembershipSummaryTypeDef = TypedDict(
    "AppInstanceUserMembershipSummaryTypeDef",
    {
        "Type": ChannelMembershipTypeType,
        "ReadMarkerTimestamp": datetime,
        "SubChannelId": str,
    },
    total=False,
)

AssociateChannelFlowRequestRequestTypeDef = TypedDict(
    "AssociateChannelFlowRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelFlowArn": str,
        "ChimeBearer": str,
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

BatchCreateChannelMembershipErrorTypeDef = TypedDict(
    "BatchCreateChannelMembershipErrorTypeDef",
    {
        "MemberArn": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredBatchCreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "_RequiredBatchCreateChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArns": Sequence[str],
        "ChimeBearer": str,
    },
)
_OptionalBatchCreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "_OptionalBatchCreateChannelMembershipRequestRequestTypeDef",
    {
        "Type": ChannelMembershipTypeType,
        "SubChannelId": str,
    },
    total=False,
)


class BatchCreateChannelMembershipRequestRequestTypeDef(
    _RequiredBatchCreateChannelMembershipRequestRequestTypeDef,
    _OptionalBatchCreateChannelMembershipRequestRequestTypeDef,
):
    pass


ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

ChannelAssociatedWithFlowSummaryTypeDef = TypedDict(
    "ChannelAssociatedWithFlowSummaryTypeDef",
    {
        "Name": str,
        "ChannelArn": str,
        "Mode": ChannelModeType,
        "Privacy": ChannelPrivacyType,
        "Metadata": str,
    },
    total=False,
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "Name": str,
        "ChannelArn": str,
        "Mode": ChannelModeType,
        "Privacy": ChannelPrivacyType,
        "Metadata": str,
        "LastMessageTimestamp": datetime,
    },
    total=False,
)

_RequiredPushNotificationPreferencesTypeDef = TypedDict(
    "_RequiredPushNotificationPreferencesTypeDef",
    {
        "AllowNotifications": AllowNotificationsType,
    },
)
_OptionalPushNotificationPreferencesTypeDef = TypedDict(
    "_OptionalPushNotificationPreferencesTypeDef",
    {
        "FilterRule": str,
    },
    total=False,
)


class PushNotificationPreferencesTypeDef(
    _RequiredPushNotificationPreferencesTypeDef, _OptionalPushNotificationPreferencesTypeDef
):
    pass


MessageAttributeValueTypeDef = TypedDict(
    "MessageAttributeValueTypeDef",
    {
        "StringValues": Sequence[str],
    },
    total=False,
)

PushNotificationConfigurationTypeDef = TypedDict(
    "PushNotificationConfigurationTypeDef",
    {
        "Title": str,
        "Body": str,
        "Type": PushNotificationTypeType,
    },
    total=False,
)

ChannelMessageStatusStructureTypeDef = TypedDict(
    "ChannelMessageStatusStructureTypeDef",
    {
        "Value": ChannelMessageStatusType,
        "Detail": str,
    },
    total=False,
)

ElasticChannelConfigurationTypeDef = TypedDict(
    "ElasticChannelConfigurationTypeDef",
    {
        "MaximumSubChannels": int,
        "TargetMembershipsPerSubChannel": int,
        "MinimumMembershipPercentage": int,
    },
)

CreateChannelBanRequestRequestTypeDef = TypedDict(
    "CreateChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredCreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "Type": ChannelMembershipTypeType,
        "ChimeBearer": str,
    },
)
_OptionalCreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelMembershipRequestRequestTypeDef",
    {
        "SubChannelId": str,
    },
    total=False,
)


class CreateChannelMembershipRequestRequestTypeDef(
    _RequiredCreateChannelMembershipRequestRequestTypeDef,
    _OptionalCreateChannelMembershipRequestRequestTypeDef,
):
    pass


CreateChannelModeratorRequestRequestTypeDef = TypedDict(
    "CreateChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": str,
    },
)

DeleteChannelBanRequestRequestTypeDef = TypedDict(
    "DeleteChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

DeleteChannelFlowRequestRequestTypeDef = TypedDict(
    "DeleteChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
    },
)

_RequiredDeleteChannelMembershipRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)
_OptionalDeleteChannelMembershipRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteChannelMembershipRequestRequestTypeDef",
    {
        "SubChannelId": str,
    },
    total=False,
)


class DeleteChannelMembershipRequestRequestTypeDef(
    _RequiredDeleteChannelMembershipRequestRequestTypeDef,
    _OptionalDeleteChannelMembershipRequestRequestTypeDef,
):
    pass


_RequiredDeleteChannelMessageRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
    },
)
_OptionalDeleteChannelMessageRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteChannelMessageRequestRequestTypeDef",
    {
        "SubChannelId": str,
    },
    total=False,
)


class DeleteChannelMessageRequestRequestTypeDef(
    _RequiredDeleteChannelMessageRequestRequestTypeDef,
    _OptionalDeleteChannelMessageRequestRequestTypeDef,
):
    pass


DeleteChannelModeratorRequestRequestTypeDef = TypedDict(
    "DeleteChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": str,
    },
)

_RequiredDeleteChannelRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
_OptionalDeleteChannelRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteChannelRequestRequestTypeDef",
    {
        "SubChannelId": str,
    },
    total=False,
)


class DeleteChannelRequestRequestTypeDef(
    _RequiredDeleteChannelRequestRequestTypeDef, _OptionalDeleteChannelRequestRequestTypeDef
):
    pass


DescribeChannelBanRequestRequestTypeDef = TypedDict(
    "DescribeChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelFlowRequestRequestTypeDef = TypedDict(
    "DescribeChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
    },
)

DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
        "ChimeBearer": str,
    },
)

_RequiredDescribeChannelMembershipRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)
_OptionalDescribeChannelMembershipRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelMembershipRequestRequestTypeDef",
    {
        "SubChannelId": str,
    },
    total=False,
)


class DescribeChannelMembershipRequestRequestTypeDef(
    _RequiredDescribeChannelMembershipRequestRequestTypeDef,
    _OptionalDescribeChannelMembershipRequestRequestTypeDef,
):
    pass


DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelModeratorRequestRequestTypeDef = TypedDict(
    "DescribeChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)

DisassociateChannelFlowRequestRequestTypeDef = TypedDict(
    "DisassociateChannelFlowRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelFlowArn": str,
        "ChimeBearer": str,
    },
)

GetChannelMembershipPreferencesRequestRequestTypeDef = TypedDict(
    "GetChannelMembershipPreferencesRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

_RequiredGetChannelMessageRequestRequestTypeDef = TypedDict(
    "_RequiredGetChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
    },
)
_OptionalGetChannelMessageRequestRequestTypeDef = TypedDict(
    "_OptionalGetChannelMessageRequestRequestTypeDef",
    {
        "SubChannelId": str,
    },
    total=False,
)


class GetChannelMessageRequestRequestTypeDef(
    _RequiredGetChannelMessageRequestRequestTypeDef, _OptionalGetChannelMessageRequestRequestTypeDef
):
    pass


_RequiredGetChannelMessageStatusRequestRequestTypeDef = TypedDict(
    "_RequiredGetChannelMessageStatusRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
    },
)
_OptionalGetChannelMessageStatusRequestRequestTypeDef = TypedDict(
    "_OptionalGetChannelMessageStatusRequestRequestTypeDef",
    {
        "SubChannelId": str,
    },
    total=False,
)


class GetChannelMessageStatusRequestRequestTypeDef(
    _RequiredGetChannelMessageStatusRequestRequestTypeDef,
    _OptionalGetChannelMessageStatusRequestRequestTypeDef,
):
    pass


MessagingSessionEndpointTypeDef = TypedDict(
    "MessagingSessionEndpointTypeDef",
    {
        "Url": str,
    },
    total=False,
)

LambdaConfigurationTypeDef = TypedDict(
    "LambdaConfigurationTypeDef",
    {
        "ResourceArn": str,
        "InvocationType": Literal["ASYNC"],
    },
)

_RequiredListChannelBansRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelBansRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
_OptionalListChannelBansRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelBansRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListChannelBansRequestRequestTypeDef(
    _RequiredListChannelBansRequestRequestTypeDef, _OptionalListChannelBansRequestRequestTypeDef
):
    pass


_RequiredListChannelFlowsRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelFlowsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
_OptionalListChannelFlowsRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelFlowsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListChannelFlowsRequestRequestTypeDef(
    _RequiredListChannelFlowsRequestRequestTypeDef, _OptionalListChannelFlowsRequestRequestTypeDef
):
    pass


_RequiredListChannelMembershipsForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
)
_OptionalListChannelMembershipsForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef(
    _RequiredListChannelMembershipsForAppInstanceUserRequestRequestTypeDef,
    _OptionalListChannelMembershipsForAppInstanceUserRequestRequestTypeDef,
):
    pass


_RequiredListChannelMembershipsRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelMembershipsRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
_OptionalListChannelMembershipsRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelMembershipsRequestRequestTypeDef",
    {
        "Type": ChannelMembershipTypeType,
        "MaxResults": int,
        "NextToken": str,
        "SubChannelId": str,
    },
    total=False,
)


class ListChannelMembershipsRequestRequestTypeDef(
    _RequiredListChannelMembershipsRequestRequestTypeDef,
    _OptionalListChannelMembershipsRequestRequestTypeDef,
):
    pass


_RequiredListChannelMessagesRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelMessagesRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
_OptionalListChannelMessagesRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelMessagesRequestRequestTypeDef",
    {
        "SortOrder": SortOrderType,
        "NotBefore": Union[datetime, str],
        "NotAfter": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
        "SubChannelId": str,
    },
    total=False,
)


class ListChannelMessagesRequestRequestTypeDef(
    _RequiredListChannelMessagesRequestRequestTypeDef,
    _OptionalListChannelMessagesRequestRequestTypeDef,
):
    pass


_RequiredListChannelModeratorsRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelModeratorsRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
_OptionalListChannelModeratorsRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelModeratorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListChannelModeratorsRequestRequestTypeDef(
    _RequiredListChannelModeratorsRequestRequestTypeDef,
    _OptionalListChannelModeratorsRequestRequestTypeDef,
):
    pass


_RequiredListChannelsAssociatedWithChannelFlowRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelsAssociatedWithChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
    },
)
_OptionalListChannelsAssociatedWithChannelFlowRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelsAssociatedWithChannelFlowRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListChannelsAssociatedWithChannelFlowRequestRequestTypeDef(
    _RequiredListChannelsAssociatedWithChannelFlowRequestRequestTypeDef,
    _OptionalListChannelsAssociatedWithChannelFlowRequestRequestTypeDef,
):
    pass


_RequiredListChannelsModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
)
_OptionalListChannelsModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef(
    _RequiredListChannelsModeratedByAppInstanceUserRequestRequestTypeDef,
    _OptionalListChannelsModeratedByAppInstanceUserRequestRequestTypeDef,
):
    pass


_RequiredListChannelsRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "ChimeBearer": str,
    },
)
_OptionalListChannelsRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelsRequestRequestTypeDef",
    {
        "Privacy": ChannelPrivacyType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListChannelsRequestRequestTypeDef(
    _RequiredListChannelsRequestRequestTypeDef, _OptionalListChannelsRequestRequestTypeDef
):
    pass


_RequiredListSubChannelsRequestRequestTypeDef = TypedDict(
    "_RequiredListSubChannelsRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
_OptionalListSubChannelsRequestRequestTypeDef = TypedDict(
    "_OptionalListSubChannelsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListSubChannelsRequestRequestTypeDef(
    _RequiredListSubChannelsRequestRequestTypeDef, _OptionalListSubChannelsRequestRequestTypeDef
):
    pass


SubChannelSummaryTypeDef = TypedDict(
    "SubChannelSummaryTypeDef",
    {
        "SubChannelId": str,
        "MembershipCount": int,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

_RequiredRedactChannelMessageRequestRequestTypeDef = TypedDict(
    "_RequiredRedactChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
    },
)
_OptionalRedactChannelMessageRequestRequestTypeDef = TypedDict(
    "_OptionalRedactChannelMessageRequestRequestTypeDef",
    {
        "SubChannelId": str,
    },
    total=False,
)


class RedactChannelMessageRequestRequestTypeDef(
    _RequiredRedactChannelMessageRequestRequestTypeDef,
    _OptionalRedactChannelMessageRequestRequestTypeDef,
):
    pass


SearchFieldTypeDef = TypedDict(
    "SearchFieldTypeDef",
    {
        "Key": Literal["MEMBERS"],
        "Values": Sequence[str],
        "Operator": SearchFieldOperatorType,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredUpdateChannelMessageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
    },
)
_OptionalUpdateChannelMessageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelMessageRequestRequestTypeDef",
    {
        "Content": str,
        "Metadata": str,
        "SubChannelId": str,
    },
    total=False,
)


class UpdateChannelMessageRequestRequestTypeDef(
    _RequiredUpdateChannelMessageRequestRequestTypeDef,
    _OptionalUpdateChannelMessageRequestRequestTypeDef,
):
    pass


_RequiredUpdateChannelReadMarkerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelReadMarkerRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
_OptionalUpdateChannelReadMarkerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelReadMarkerRequestRequestTypeDef",
    {
        "SubChannelId": str,
    },
    total=False,
)


class UpdateChannelReadMarkerRequestRequestTypeDef(
    _RequiredUpdateChannelReadMarkerRequestRequestTypeDef,
    _OptionalUpdateChannelReadMarkerRequestRequestTypeDef,
):
    pass


_RequiredUpdateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
_OptionalUpdateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelRequestRequestTypeDef",
    {
        "Name": str,
        "Mode": ChannelModeType,
        "Metadata": str,
    },
    total=False,
)


class UpdateChannelRequestRequestTypeDef(
    _RequiredUpdateChannelRequestRequestTypeDef, _OptionalUpdateChannelRequestRequestTypeDef
):
    pass


BatchChannelMembershipsTypeDef = TypedDict(
    "BatchChannelMembershipsTypeDef",
    {
        "InvitedBy": IdentityTypeDef,
        "Type": ChannelMembershipTypeType,
        "Members": List[IdentityTypeDef],
        "ChannelArn": str,
        "SubChannelId": str,
    },
    total=False,
)

ChannelBanSummaryTypeDef = TypedDict(
    "ChannelBanSummaryTypeDef",
    {
        "Member": IdentityTypeDef,
    },
    total=False,
)

ChannelBanTypeDef = TypedDict(
    "ChannelBanTypeDef",
    {
        "Member": IdentityTypeDef,
        "ChannelArn": str,
        "CreatedTimestamp": datetime,
        "CreatedBy": IdentityTypeDef,
    },
    total=False,
)

ChannelMembershipSummaryTypeDef = TypedDict(
    "ChannelMembershipSummaryTypeDef",
    {
        "Member": IdentityTypeDef,
    },
    total=False,
)

ChannelMembershipTypeDef = TypedDict(
    "ChannelMembershipTypeDef",
    {
        "InvitedBy": IdentityTypeDef,
        "Type": ChannelMembershipTypeType,
        "Member": IdentityTypeDef,
        "ChannelArn": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "SubChannelId": str,
    },
    total=False,
)

ChannelModeratorSummaryTypeDef = TypedDict(
    "ChannelModeratorSummaryTypeDef",
    {
        "Moderator": IdentityTypeDef,
    },
    total=False,
)

ChannelModeratorTypeDef = TypedDict(
    "ChannelModeratorTypeDef",
    {
        "Moderator": IdentityTypeDef,
        "ChannelArn": str,
        "CreatedTimestamp": datetime,
        "CreatedBy": IdentityTypeDef,
    },
    total=False,
)

ChannelFlowCallbackResponseTypeDef = TypedDict(
    "ChannelFlowCallbackResponseTypeDef",
    {
        "ChannelArn": str,
        "CallbackId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateChannelBanResponseTypeDef = TypedDict(
    "CreateChannelBanResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": IdentityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateChannelFlowResponseTypeDef = TypedDict(
    "CreateChannelFlowResponseTypeDef",
    {
        "ChannelFlowArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateChannelMembershipResponseTypeDef = TypedDict(
    "CreateChannelMembershipResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": IdentityTypeDef,
        "SubChannelId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateChannelModeratorResponseTypeDef = TypedDict(
    "CreateChannelModeratorResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelModerator": IdentityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RedactChannelMessageResponseTypeDef = TypedDict(
    "RedactChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "SubChannelId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateChannelFlowResponseTypeDef = TypedDict(
    "UpdateChannelFlowResponseTypeDef",
    {
        "ChannelFlowArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateChannelReadMarkerResponseTypeDef = TypedDict(
    "UpdateChannelReadMarkerResponseTypeDef",
    {
        "ChannelArn": str,
        "SubChannelId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListChannelsAssociatedWithChannelFlowResponseTypeDef = TypedDict(
    "ListChannelsAssociatedWithChannelFlowResponseTypeDef",
    {
        "Channels": List[ChannelAssociatedWithFlowSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ChannelMembershipForAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": ChannelSummaryTypeDef,
        "AppInstanceUserMembershipSummary": AppInstanceUserMembershipSummaryTypeDef,
    },
    total=False,
)

ChannelModeratedByAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": ChannelSummaryTypeDef,
    },
    total=False,
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Channels": List[ChannelSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SearchChannelsResponseTypeDef = TypedDict(
    "SearchChannelsResponseTypeDef",
    {
        "Channels": List[ChannelSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ChannelMembershipPreferencesTypeDef = TypedDict(
    "ChannelMembershipPreferencesTypeDef",
    {
        "PushNotifications": PushNotificationPreferencesTypeDef,
    },
    total=False,
)

_RequiredChannelMessageCallbackTypeDef = TypedDict(
    "_RequiredChannelMessageCallbackTypeDef",
    {
        "MessageId": str,
    },
)
_OptionalChannelMessageCallbackTypeDef = TypedDict(
    "_OptionalChannelMessageCallbackTypeDef",
    {
        "Content": str,
        "Metadata": str,
        "PushNotification": PushNotificationConfigurationTypeDef,
        "MessageAttributes": Mapping[str, MessageAttributeValueTypeDef],
        "SubChannelId": str,
    },
    total=False,
)


class ChannelMessageCallbackTypeDef(
    _RequiredChannelMessageCallbackTypeDef, _OptionalChannelMessageCallbackTypeDef
):
    pass


_RequiredSendChannelMessageRequestRequestTypeDef = TypedDict(
    "_RequiredSendChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "Content": str,
        "Type": ChannelMessageTypeType,
        "Persistence": ChannelMessagePersistenceTypeType,
        "ClientRequestToken": str,
        "ChimeBearer": str,
    },
)
_OptionalSendChannelMessageRequestRequestTypeDef = TypedDict(
    "_OptionalSendChannelMessageRequestRequestTypeDef",
    {
        "Metadata": str,
        "PushNotification": PushNotificationConfigurationTypeDef,
        "MessageAttributes": Mapping[str, MessageAttributeValueTypeDef],
        "SubChannelId": str,
    },
    total=False,
)


class SendChannelMessageRequestRequestTypeDef(
    _RequiredSendChannelMessageRequestRequestTypeDef,
    _OptionalSendChannelMessageRequestRequestTypeDef,
):
    pass


ChannelMessageSummaryTypeDef = TypedDict(
    "ChannelMessageSummaryTypeDef",
    {
        "MessageId": str,
        "Content": str,
        "Metadata": str,
        "Type": ChannelMessageTypeType,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "LastEditedTimestamp": datetime,
        "Sender": IdentityTypeDef,
        "Redacted": bool,
        "Status": ChannelMessageStatusStructureTypeDef,
        "MessageAttributes": Dict[str, MessageAttributeValueTypeDef],
    },
    total=False,
)

ChannelMessageTypeDef = TypedDict(
    "ChannelMessageTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "Content": str,
        "Metadata": str,
        "Type": ChannelMessageTypeType,
        "CreatedTimestamp": datetime,
        "LastEditedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Sender": IdentityTypeDef,
        "Redacted": bool,
        "Persistence": ChannelMessagePersistenceTypeType,
        "Status": ChannelMessageStatusStructureTypeDef,
        "MessageAttributes": Dict[str, MessageAttributeValueTypeDef],
        "SubChannelId": str,
    },
    total=False,
)

GetChannelMessageStatusResponseTypeDef = TypedDict(
    "GetChannelMessageStatusResponseTypeDef",
    {
        "Status": ChannelMessageStatusStructureTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SendChannelMessageResponseTypeDef = TypedDict(
    "SendChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "Status": ChannelMessageStatusStructureTypeDef,
        "SubChannelId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateChannelMessageResponseTypeDef = TypedDict(
    "UpdateChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "Status": ChannelMessageStatusStructureTypeDef,
        "SubChannelId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Name": str,
        "ChannelArn": str,
        "Mode": ChannelModeType,
        "Privacy": ChannelPrivacyType,
        "Metadata": str,
        "CreatedBy": IdentityTypeDef,
        "CreatedTimestamp": datetime,
        "LastMessageTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "ChannelFlowArn": str,
        "ElasticChannelConfiguration": ElasticChannelConfigurationTypeDef,
    },
    total=False,
)

_RequiredCreateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChannelRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "ClientRequestToken": str,
        "ChimeBearer": str,
    },
)
_OptionalCreateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelRequestRequestTypeDef",
    {
        "Mode": ChannelModeType,
        "Privacy": ChannelPrivacyType,
        "Metadata": str,
        "Tags": Sequence[TagTypeDef],
        "ChannelId": str,
        "MemberArns": Sequence[str],
        "ModeratorArns": Sequence[str],
        "ElasticChannelConfiguration": ElasticChannelConfigurationTypeDef,
    },
    total=False,
)


class CreateChannelRequestRequestTypeDef(
    _RequiredCreateChannelRequestRequestTypeDef, _OptionalCreateChannelRequestRequestTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

GetMessagingSessionEndpointResponseTypeDef = TypedDict(
    "GetMessagingSessionEndpointResponseTypeDef",
    {
        "Endpoint": MessagingSessionEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ProcessorConfigurationTypeDef = TypedDict(
    "ProcessorConfigurationTypeDef",
    {
        "Lambda": LambdaConfigurationTypeDef,
    },
)

ListSubChannelsResponseTypeDef = TypedDict(
    "ListSubChannelsResponseTypeDef",
    {
        "ChannelArn": str,
        "SubChannels": List[SubChannelSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredSearchChannelsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchChannelsRequestRequestTypeDef",
    {
        "Fields": Sequence[SearchFieldTypeDef],
    },
)
_OptionalSearchChannelsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchChannelsRequestRequestTypeDef",
    {
        "ChimeBearer": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class SearchChannelsRequestRequestTypeDef(
    _RequiredSearchChannelsRequestRequestTypeDef, _OptionalSearchChannelsRequestRequestTypeDef
):
    pass


BatchCreateChannelMembershipResponseTypeDef = TypedDict(
    "BatchCreateChannelMembershipResponseTypeDef",
    {
        "BatchChannelMemberships": BatchChannelMembershipsTypeDef,
        "Errors": List[BatchCreateChannelMembershipErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListChannelBansResponseTypeDef = TypedDict(
    "ListChannelBansResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelBans": List[ChannelBanSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeChannelBanResponseTypeDef = TypedDict(
    "DescribeChannelBanResponseTypeDef",
    {
        "ChannelBan": ChannelBanTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListChannelMembershipsResponseTypeDef = TypedDict(
    "ListChannelMembershipsResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelMemberships": List[ChannelMembershipSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeChannelMembershipResponseTypeDef = TypedDict(
    "DescribeChannelMembershipResponseTypeDef",
    {
        "ChannelMembership": ChannelMembershipTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListChannelModeratorsResponseTypeDef = TypedDict(
    "ListChannelModeratorsResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelModerators": List[ChannelModeratorSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeChannelModeratorResponseTypeDef = TypedDict(
    "DescribeChannelModeratorResponseTypeDef",
    {
        "ChannelModerator": ChannelModeratorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeChannelMembershipForAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    {
        "ChannelMembership": ChannelMembershipForAppInstanceUserSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListChannelMembershipsForAppInstanceUserResponseTypeDef = TypedDict(
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    {
        "ChannelMemberships": List[ChannelMembershipForAppInstanceUserSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeChannelModeratedByAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    {
        "Channel": ChannelModeratedByAppInstanceUserSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListChannelsModeratedByAppInstanceUserResponseTypeDef = TypedDict(
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    {
        "Channels": List[ChannelModeratedByAppInstanceUserSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetChannelMembershipPreferencesResponseTypeDef = TypedDict(
    "GetChannelMembershipPreferencesResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": IdentityTypeDef,
        "Preferences": ChannelMembershipPreferencesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutChannelMembershipPreferencesRequestRequestTypeDef = TypedDict(
    "PutChannelMembershipPreferencesRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
        "Preferences": ChannelMembershipPreferencesTypeDef,
    },
)

PutChannelMembershipPreferencesResponseTypeDef = TypedDict(
    "PutChannelMembershipPreferencesResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": IdentityTypeDef,
        "Preferences": ChannelMembershipPreferencesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredChannelFlowCallbackRequestRequestTypeDef = TypedDict(
    "_RequiredChannelFlowCallbackRequestRequestTypeDef",
    {
        "CallbackId": str,
        "ChannelArn": str,
        "ChannelMessage": ChannelMessageCallbackTypeDef,
    },
)
_OptionalChannelFlowCallbackRequestRequestTypeDef = TypedDict(
    "_OptionalChannelFlowCallbackRequestRequestTypeDef",
    {
        "DeleteResource": bool,
    },
    total=False,
)


class ChannelFlowCallbackRequestRequestTypeDef(
    _RequiredChannelFlowCallbackRequestRequestTypeDef,
    _OptionalChannelFlowCallbackRequestRequestTypeDef,
):
    pass


ListChannelMessagesResponseTypeDef = TypedDict(
    "ListChannelMessagesResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelMessages": List[ChannelMessageSummaryTypeDef],
        "SubChannelId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetChannelMessageResponseTypeDef = TypedDict(
    "GetChannelMessageResponseTypeDef",
    {
        "ChannelMessage": ChannelMessageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Channel": ChannelTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ProcessorTypeDef = TypedDict(
    "ProcessorTypeDef",
    {
        "Name": str,
        "Configuration": ProcessorConfigurationTypeDef,
        "ExecutionOrder": int,
        "FallbackAction": FallbackActionType,
    },
)

ChannelFlowSummaryTypeDef = TypedDict(
    "ChannelFlowSummaryTypeDef",
    {
        "ChannelFlowArn": str,
        "Name": str,
        "Processors": List[ProcessorTypeDef],
    },
    total=False,
)

ChannelFlowTypeDef = TypedDict(
    "ChannelFlowTypeDef",
    {
        "ChannelFlowArn": str,
        "Processors": List[ProcessorTypeDef],
        "Name": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

_RequiredCreateChannelFlowRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChannelFlowRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Processors": Sequence[ProcessorTypeDef],
        "Name": str,
        "ClientRequestToken": str,
    },
)
_OptionalCreateChannelFlowRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelFlowRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateChannelFlowRequestRequestTypeDef(
    _RequiredCreateChannelFlowRequestRequestTypeDef, _OptionalCreateChannelFlowRequestRequestTypeDef
):
    pass


UpdateChannelFlowRequestRequestTypeDef = TypedDict(
    "UpdateChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
        "Processors": Sequence[ProcessorTypeDef],
        "Name": str,
    },
)

ListChannelFlowsResponseTypeDef = TypedDict(
    "ListChannelFlowsResponseTypeDef",
    {
        "ChannelFlows": List[ChannelFlowSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeChannelFlowResponseTypeDef = TypedDict(
    "DescribeChannelFlowResponseTypeDef",
    {
        "ChannelFlow": ChannelFlowTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
