"""
Type annotations for iotfleetwise service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/type_defs/)

Usage::

    ```python
    from mypy_boto3_iotfleetwise.type_defs import ActuatorTypeDef

    data: ActuatorTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    CampaignStatusType,
    CompressionType,
    DiagnosticsModeType,
    LogTypeType,
    ManifestStatusType,
    NetworkInterfaceTypeType,
    NodeDataTypeType,
    RegistrationStatusType,
    SignalDecoderTypeType,
    SpoolingModeType,
    TriggerModeType,
    UpdateCampaignActionType,
    UpdateModeType,
    VehicleAssociationBehaviorType,
    VehicleStateType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActuatorTypeDef",
    "AssociateVehicleFleetRequestRequestTypeDef",
    "AttributeTypeDef",
    "CreateVehicleErrorTypeDef",
    "CreateVehicleResponseItemTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateVehicleRequestItemTypeDef",
    "UpdateVehicleErrorTypeDef",
    "UpdateVehicleResponseItemTypeDef",
    "BranchTypeDef",
    "CampaignSummaryTypeDef",
    "CanDbcDefinitionTypeDef",
    "CanInterfaceTypeDef",
    "CanSignalTypeDef",
    "CloudWatchLogDeliveryOptionsTypeDef",
    "ConditionBasedCollectionSchemeTypeDef",
    "TimeBasedCollectionSchemeTypeDef",
    "SignalInformationTypeDef",
    "TagTypeDef",
    "DecoderManifestSummaryTypeDef",
    "DeleteCampaignRequestRequestTypeDef",
    "DeleteDecoderManifestRequestRequestTypeDef",
    "DeleteFleetRequestRequestTypeDef",
    "DeleteModelManifestRequestRequestTypeDef",
    "DeleteSignalCatalogRequestRequestTypeDef",
    "DeleteVehicleRequestRequestTypeDef",
    "DisassociateVehicleFleetRequestRequestTypeDef",
    "FleetSummaryTypeDef",
    "FormattedVssTypeDef",
    "GetCampaignRequestRequestTypeDef",
    "GetDecoderManifestRequestRequestTypeDef",
    "GetFleetRequestRequestTypeDef",
    "GetModelManifestRequestRequestTypeDef",
    "IamRegistrationResponseTypeDef",
    "TimestreamRegistrationResponseTypeDef",
    "GetSignalCatalogRequestRequestTypeDef",
    "NodeCountsTypeDef",
    "GetVehicleRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetVehicleStatusRequestRequestTypeDef",
    "VehicleStatusTypeDef",
    "IamResourcesTypeDef",
    "ListCampaignsRequestRequestTypeDef",
    "ListDecoderManifestNetworkInterfacesRequestRequestTypeDef",
    "ListDecoderManifestSignalsRequestRequestTypeDef",
    "ListDecoderManifestsRequestRequestTypeDef",
    "ListFleetsForVehicleRequestRequestTypeDef",
    "ListFleetsRequestRequestTypeDef",
    "ListModelManifestNodesRequestRequestTypeDef",
    "ListModelManifestsRequestRequestTypeDef",
    "ModelManifestSummaryTypeDef",
    "ListSignalCatalogNodesRequestRequestTypeDef",
    "ListSignalCatalogsRequestRequestTypeDef",
    "SignalCatalogSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListVehiclesInFleetRequestRequestTypeDef",
    "ListVehiclesRequestRequestTypeDef",
    "VehicleSummaryTypeDef",
    "ObdInterfaceTypeDef",
    "SensorTypeDef",
    "ObdSignalTypeDef",
    "TimestreamResourcesTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCampaignRequestRequestTypeDef",
    "UpdateFleetRequestRequestTypeDef",
    "UpdateModelManifestRequestRequestTypeDef",
    "UpdateVehicleRequestRequestTypeDef",
    "BatchCreateVehicleResponseTypeDef",
    "CreateCampaignResponseTypeDef",
    "CreateDecoderManifestResponseTypeDef",
    "CreateFleetResponseTypeDef",
    "CreateModelManifestResponseTypeDef",
    "CreateSignalCatalogResponseTypeDef",
    "CreateVehicleResponseTypeDef",
    "DeleteCampaignResponseTypeDef",
    "DeleteDecoderManifestResponseTypeDef",
    "DeleteFleetResponseTypeDef",
    "DeleteModelManifestResponseTypeDef",
    "DeleteSignalCatalogResponseTypeDef",
    "DeleteVehicleResponseTypeDef",
    "GetDecoderManifestResponseTypeDef",
    "GetFleetResponseTypeDef",
    "GetModelManifestResponseTypeDef",
    "GetVehicleResponseTypeDef",
    "ImportDecoderManifestResponseTypeDef",
    "ImportSignalCatalogResponseTypeDef",
    "ListFleetsForVehicleResponseTypeDef",
    "ListVehiclesInFleetResponseTypeDef",
    "UpdateCampaignResponseTypeDef",
    "UpdateDecoderManifestResponseTypeDef",
    "UpdateFleetResponseTypeDef",
    "UpdateModelManifestResponseTypeDef",
    "UpdateSignalCatalogResponseTypeDef",
    "UpdateVehicleResponseTypeDef",
    "BatchUpdateVehicleRequestRequestTypeDef",
    "BatchUpdateVehicleResponseTypeDef",
    "ListCampaignsResponseTypeDef",
    "NetworkFileDefinitionTypeDef",
    "GetLoggingOptionsResponseTypeDef",
    "PutLoggingOptionsRequestRequestTypeDef",
    "CollectionSchemeTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "CreateModelManifestRequestRequestTypeDef",
    "CreateVehicleRequestItemTypeDef",
    "CreateVehicleRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ListDecoderManifestsResponseTypeDef",
    "ListFleetsResponseTypeDef",
    "ImportSignalCatalogRequestRequestTypeDef",
    "GetRegisterAccountStatusResponseTypeDef",
    "GetSignalCatalogResponseTypeDef",
    "GetVehicleStatusRequestGetVehicleStatusPaginateTypeDef",
    "ListCampaignsRequestListCampaignsPaginateTypeDef",
    "ListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef",
    "ListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef",
    "ListDecoderManifestsRequestListDecoderManifestsPaginateTypeDef",
    "ListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef",
    "ListFleetsRequestListFleetsPaginateTypeDef",
    "ListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef",
    "ListModelManifestsRequestListModelManifestsPaginateTypeDef",
    "ListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef",
    "ListSignalCatalogsRequestListSignalCatalogsPaginateTypeDef",
    "ListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef",
    "ListVehiclesRequestListVehiclesPaginateTypeDef",
    "GetVehicleStatusResponseTypeDef",
    "ListModelManifestsResponseTypeDef",
    "ListSignalCatalogsResponseTypeDef",
    "ListVehiclesResponseTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeTypeDef",
    "SignalDecoderTypeDef",
    "RegisterAccountRequestRequestTypeDef",
    "RegisterAccountResponseTypeDef",
    "ImportDecoderManifestRequestRequestTypeDef",
    "CreateCampaignRequestRequestTypeDef",
    "GetCampaignResponseTypeDef",
    "BatchCreateVehicleRequestRequestTypeDef",
    "ListDecoderManifestNetworkInterfacesResponseTypeDef",
    "CreateSignalCatalogRequestRequestTypeDef",
    "ListModelManifestNodesResponseTypeDef",
    "ListSignalCatalogNodesResponseTypeDef",
    "UpdateSignalCatalogRequestRequestTypeDef",
    "CreateDecoderManifestRequestRequestTypeDef",
    "ListDecoderManifestSignalsResponseTypeDef",
    "UpdateDecoderManifestRequestRequestTypeDef",
)

_RequiredActuatorTypeDef = TypedDict(
    "_RequiredActuatorTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
    },
)
_OptionalActuatorTypeDef = TypedDict(
    "_OptionalActuatorTypeDef",
    {
        "description": str,
        "unit": str,
        "allowedValues": Sequence[str],
        "min": float,
        "max": float,
        "assignedValue": str,
    },
    total=False,
)


class ActuatorTypeDef(_RequiredActuatorTypeDef, _OptionalActuatorTypeDef):
    pass


AssociateVehicleFleetRequestRequestTypeDef = TypedDict(
    "AssociateVehicleFleetRequestRequestTypeDef",
    {
        "vehicleName": str,
        "fleetId": str,
    },
)

_RequiredAttributeTypeDef = TypedDict(
    "_RequiredAttributeTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
    },
)
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {
        "description": str,
        "unit": str,
        "allowedValues": Sequence[str],
        "min": float,
        "max": float,
        "assignedValue": str,
        "defaultValue": str,
    },
    total=False,
)


class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass


CreateVehicleErrorTypeDef = TypedDict(
    "CreateVehicleErrorTypeDef",
    {
        "vehicleName": str,
        "code": str,
        "message": str,
    },
    total=False,
)

CreateVehicleResponseItemTypeDef = TypedDict(
    "CreateVehicleResponseItemTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "thingArn": str,
    },
    total=False,
)

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

_RequiredUpdateVehicleRequestItemTypeDef = TypedDict(
    "_RequiredUpdateVehicleRequestItemTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalUpdateVehicleRequestItemTypeDef = TypedDict(
    "_OptionalUpdateVehicleRequestItemTypeDef",
    {
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "attributes": Mapping[str, str],
        "attributeUpdateMode": UpdateModeType,
    },
    total=False,
)


class UpdateVehicleRequestItemTypeDef(
    _RequiredUpdateVehicleRequestItemTypeDef, _OptionalUpdateVehicleRequestItemTypeDef
):
    pass


UpdateVehicleErrorTypeDef = TypedDict(
    "UpdateVehicleErrorTypeDef",
    {
        "vehicleName": str,
        "code": int,
        "message": str,
    },
    total=False,
)

UpdateVehicleResponseItemTypeDef = TypedDict(
    "UpdateVehicleResponseItemTypeDef",
    {
        "vehicleName": str,
        "arn": str,
    },
    total=False,
)

_RequiredBranchTypeDef = TypedDict(
    "_RequiredBranchTypeDef",
    {
        "fullyQualifiedName": str,
    },
)
_OptionalBranchTypeDef = TypedDict(
    "_OptionalBranchTypeDef",
    {
        "description": str,
    },
    total=False,
)


class BranchTypeDef(_RequiredBranchTypeDef, _OptionalBranchTypeDef):
    pass


_RequiredCampaignSummaryTypeDef = TypedDict(
    "_RequiredCampaignSummaryTypeDef",
    {
        "creationTime": datetime,
        "lastModificationTime": datetime,
    },
)
_OptionalCampaignSummaryTypeDef = TypedDict(
    "_OptionalCampaignSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "signalCatalogArn": str,
        "targetArn": str,
        "status": CampaignStatusType,
    },
    total=False,
)


class CampaignSummaryTypeDef(_RequiredCampaignSummaryTypeDef, _OptionalCampaignSummaryTypeDef):
    pass


_RequiredCanDbcDefinitionTypeDef = TypedDict(
    "_RequiredCanDbcDefinitionTypeDef",
    {
        "networkInterface": str,
        "canDbcFiles": Sequence[Union[str, bytes, IO[Any], StreamingBody]],
    },
)
_OptionalCanDbcDefinitionTypeDef = TypedDict(
    "_OptionalCanDbcDefinitionTypeDef",
    {
        "signalsMap": Mapping[str, str],
    },
    total=False,
)


class CanDbcDefinitionTypeDef(_RequiredCanDbcDefinitionTypeDef, _OptionalCanDbcDefinitionTypeDef):
    pass


_RequiredCanInterfaceTypeDef = TypedDict(
    "_RequiredCanInterfaceTypeDef",
    {
        "name": str,
    },
)
_OptionalCanInterfaceTypeDef = TypedDict(
    "_OptionalCanInterfaceTypeDef",
    {
        "protocolName": str,
        "protocolVersion": str,
    },
    total=False,
)


class CanInterfaceTypeDef(_RequiredCanInterfaceTypeDef, _OptionalCanInterfaceTypeDef):
    pass


_RequiredCanSignalTypeDef = TypedDict(
    "_RequiredCanSignalTypeDef",
    {
        "messageId": int,
        "isBigEndian": bool,
        "isSigned": bool,
        "startBit": int,
        "offset": float,
        "factor": float,
        "length": int,
    },
)
_OptionalCanSignalTypeDef = TypedDict(
    "_OptionalCanSignalTypeDef",
    {
        "name": str,
    },
    total=False,
)


class CanSignalTypeDef(_RequiredCanSignalTypeDef, _OptionalCanSignalTypeDef):
    pass


_RequiredCloudWatchLogDeliveryOptionsTypeDef = TypedDict(
    "_RequiredCloudWatchLogDeliveryOptionsTypeDef",
    {
        "logType": LogTypeType,
    },
)
_OptionalCloudWatchLogDeliveryOptionsTypeDef = TypedDict(
    "_OptionalCloudWatchLogDeliveryOptionsTypeDef",
    {
        "logGroupName": str,
    },
    total=False,
)


class CloudWatchLogDeliveryOptionsTypeDef(
    _RequiredCloudWatchLogDeliveryOptionsTypeDef, _OptionalCloudWatchLogDeliveryOptionsTypeDef
):
    pass


_RequiredConditionBasedCollectionSchemeTypeDef = TypedDict(
    "_RequiredConditionBasedCollectionSchemeTypeDef",
    {
        "expression": str,
    },
)
_OptionalConditionBasedCollectionSchemeTypeDef = TypedDict(
    "_OptionalConditionBasedCollectionSchemeTypeDef",
    {
        "minimumTriggerIntervalMs": int,
        "triggerMode": TriggerModeType,
        "conditionLanguageVersion": int,
    },
    total=False,
)


class ConditionBasedCollectionSchemeTypeDef(
    _RequiredConditionBasedCollectionSchemeTypeDef, _OptionalConditionBasedCollectionSchemeTypeDef
):
    pass


TimeBasedCollectionSchemeTypeDef = TypedDict(
    "TimeBasedCollectionSchemeTypeDef",
    {
        "periodMs": int,
    },
)

_RequiredSignalInformationTypeDef = TypedDict(
    "_RequiredSignalInformationTypeDef",
    {
        "name": str,
    },
)
_OptionalSignalInformationTypeDef = TypedDict(
    "_OptionalSignalInformationTypeDef",
    {
        "maxSampleCount": int,
        "minimumSamplingIntervalMs": int,
    },
    total=False,
)


class SignalInformationTypeDef(
    _RequiredSignalInformationTypeDef, _OptionalSignalInformationTypeDef
):
    pass


TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredDecoderManifestSummaryTypeDef = TypedDict(
    "_RequiredDecoderManifestSummaryTypeDef",
    {
        "creationTime": datetime,
        "lastModificationTime": datetime,
    },
)
_OptionalDecoderManifestSummaryTypeDef = TypedDict(
    "_OptionalDecoderManifestSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "modelManifestArn": str,
        "description": str,
        "status": ManifestStatusType,
    },
    total=False,
)


class DecoderManifestSummaryTypeDef(
    _RequiredDecoderManifestSummaryTypeDef, _OptionalDecoderManifestSummaryTypeDef
):
    pass


DeleteCampaignRequestRequestTypeDef = TypedDict(
    "DeleteCampaignRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteDecoderManifestRequestRequestTypeDef = TypedDict(
    "DeleteDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteFleetRequestRequestTypeDef = TypedDict(
    "DeleteFleetRequestRequestTypeDef",
    {
        "fleetId": str,
    },
)

DeleteModelManifestRequestRequestTypeDef = TypedDict(
    "DeleteModelManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteSignalCatalogRequestRequestTypeDef = TypedDict(
    "DeleteSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteVehicleRequestRequestTypeDef = TypedDict(
    "DeleteVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)

DisassociateVehicleFleetRequestRequestTypeDef = TypedDict(
    "DisassociateVehicleFleetRequestRequestTypeDef",
    {
        "vehicleName": str,
        "fleetId": str,
    },
)

_RequiredFleetSummaryTypeDef = TypedDict(
    "_RequiredFleetSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "signalCatalogArn": str,
        "creationTime": datetime,
    },
)
_OptionalFleetSummaryTypeDef = TypedDict(
    "_OptionalFleetSummaryTypeDef",
    {
        "description": str,
        "lastModificationTime": datetime,
    },
    total=False,
)


class FleetSummaryTypeDef(_RequiredFleetSummaryTypeDef, _OptionalFleetSummaryTypeDef):
    pass


FormattedVssTypeDef = TypedDict(
    "FormattedVssTypeDef",
    {
        "vssJson": str,
    },
    total=False,
)

GetCampaignRequestRequestTypeDef = TypedDict(
    "GetCampaignRequestRequestTypeDef",
    {
        "name": str,
    },
)

GetDecoderManifestRequestRequestTypeDef = TypedDict(
    "GetDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)

GetFleetRequestRequestTypeDef = TypedDict(
    "GetFleetRequestRequestTypeDef",
    {
        "fleetId": str,
    },
)

GetModelManifestRequestRequestTypeDef = TypedDict(
    "GetModelManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)

_RequiredIamRegistrationResponseTypeDef = TypedDict(
    "_RequiredIamRegistrationResponseTypeDef",
    {
        "roleArn": str,
        "registrationStatus": RegistrationStatusType,
    },
)
_OptionalIamRegistrationResponseTypeDef = TypedDict(
    "_OptionalIamRegistrationResponseTypeDef",
    {
        "errorMessage": str,
    },
    total=False,
)


class IamRegistrationResponseTypeDef(
    _RequiredIamRegistrationResponseTypeDef, _OptionalIamRegistrationResponseTypeDef
):
    pass


_RequiredTimestreamRegistrationResponseTypeDef = TypedDict(
    "_RequiredTimestreamRegistrationResponseTypeDef",
    {
        "timestreamDatabaseName": str,
        "timestreamTableName": str,
        "registrationStatus": RegistrationStatusType,
    },
)
_OptionalTimestreamRegistrationResponseTypeDef = TypedDict(
    "_OptionalTimestreamRegistrationResponseTypeDef",
    {
        "timestreamDatabaseArn": str,
        "timestreamTableArn": str,
        "errorMessage": str,
    },
    total=False,
)


class TimestreamRegistrationResponseTypeDef(
    _RequiredTimestreamRegistrationResponseTypeDef, _OptionalTimestreamRegistrationResponseTypeDef
):
    pass


GetSignalCatalogRequestRequestTypeDef = TypedDict(
    "GetSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)

NodeCountsTypeDef = TypedDict(
    "NodeCountsTypeDef",
    {
        "totalNodes": int,
        "totalBranches": int,
        "totalSensors": int,
        "totalAttributes": int,
        "totalActuators": int,
    },
    total=False,
)

GetVehicleRequestRequestTypeDef = TypedDict(
    "GetVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredGetVehicleStatusRequestRequestTypeDef = TypedDict(
    "_RequiredGetVehicleStatusRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalGetVehicleStatusRequestRequestTypeDef = TypedDict(
    "_OptionalGetVehicleStatusRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetVehicleStatusRequestRequestTypeDef(
    _RequiredGetVehicleStatusRequestRequestTypeDef, _OptionalGetVehicleStatusRequestRequestTypeDef
):
    pass


VehicleStatusTypeDef = TypedDict(
    "VehicleStatusTypeDef",
    {
        "campaignName": str,
        "vehicleName": str,
        "status": VehicleStateType,
    },
    total=False,
)

IamResourcesTypeDef = TypedDict(
    "IamResourcesTypeDef",
    {
        "roleArn": str,
    },
)

ListCampaignsRequestRequestTypeDef = TypedDict(
    "ListCampaignsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "status": str,
    },
    total=False,
)

_RequiredListDecoderManifestNetworkInterfacesRequestRequestTypeDef = TypedDict(
    "_RequiredListDecoderManifestNetworkInterfacesRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalListDecoderManifestNetworkInterfacesRequestRequestTypeDef = TypedDict(
    "_OptionalListDecoderManifestNetworkInterfacesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListDecoderManifestNetworkInterfacesRequestRequestTypeDef(
    _RequiredListDecoderManifestNetworkInterfacesRequestRequestTypeDef,
    _OptionalListDecoderManifestNetworkInterfacesRequestRequestTypeDef,
):
    pass


_RequiredListDecoderManifestSignalsRequestRequestTypeDef = TypedDict(
    "_RequiredListDecoderManifestSignalsRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalListDecoderManifestSignalsRequestRequestTypeDef = TypedDict(
    "_OptionalListDecoderManifestSignalsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListDecoderManifestSignalsRequestRequestTypeDef(
    _RequiredListDecoderManifestSignalsRequestRequestTypeDef,
    _OptionalListDecoderManifestSignalsRequestRequestTypeDef,
):
    pass


ListDecoderManifestsRequestRequestTypeDef = TypedDict(
    "ListDecoderManifestsRequestRequestTypeDef",
    {
        "modelManifestArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredListFleetsForVehicleRequestRequestTypeDef = TypedDict(
    "_RequiredListFleetsForVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalListFleetsForVehicleRequestRequestTypeDef = TypedDict(
    "_OptionalListFleetsForVehicleRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListFleetsForVehicleRequestRequestTypeDef(
    _RequiredListFleetsForVehicleRequestRequestTypeDef,
    _OptionalListFleetsForVehicleRequestRequestTypeDef,
):
    pass


ListFleetsRequestRequestTypeDef = TypedDict(
    "ListFleetsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredListModelManifestNodesRequestRequestTypeDef = TypedDict(
    "_RequiredListModelManifestNodesRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalListModelManifestNodesRequestRequestTypeDef = TypedDict(
    "_OptionalListModelManifestNodesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListModelManifestNodesRequestRequestTypeDef(
    _RequiredListModelManifestNodesRequestRequestTypeDef,
    _OptionalListModelManifestNodesRequestRequestTypeDef,
):
    pass


ListModelManifestsRequestRequestTypeDef = TypedDict(
    "ListModelManifestsRequestRequestTypeDef",
    {
        "signalCatalogArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredModelManifestSummaryTypeDef = TypedDict(
    "_RequiredModelManifestSummaryTypeDef",
    {
        "creationTime": datetime,
        "lastModificationTime": datetime,
    },
)
_OptionalModelManifestSummaryTypeDef = TypedDict(
    "_OptionalModelManifestSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "signalCatalogArn": str,
        "description": str,
        "status": ManifestStatusType,
    },
    total=False,
)


class ModelManifestSummaryTypeDef(
    _RequiredModelManifestSummaryTypeDef, _OptionalModelManifestSummaryTypeDef
):
    pass


_RequiredListSignalCatalogNodesRequestRequestTypeDef = TypedDict(
    "_RequiredListSignalCatalogNodesRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalListSignalCatalogNodesRequestRequestTypeDef = TypedDict(
    "_OptionalListSignalCatalogNodesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListSignalCatalogNodesRequestRequestTypeDef(
    _RequiredListSignalCatalogNodesRequestRequestTypeDef,
    _OptionalListSignalCatalogNodesRequestRequestTypeDef,
):
    pass


ListSignalCatalogsRequestRequestTypeDef = TypedDict(
    "ListSignalCatalogsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

SignalCatalogSummaryTypeDef = TypedDict(
    "SignalCatalogSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "creationTime": datetime,
        "lastModificationTime": datetime,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

_RequiredListVehiclesInFleetRequestRequestTypeDef = TypedDict(
    "_RequiredListVehiclesInFleetRequestRequestTypeDef",
    {
        "fleetId": str,
    },
)
_OptionalListVehiclesInFleetRequestRequestTypeDef = TypedDict(
    "_OptionalListVehiclesInFleetRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListVehiclesInFleetRequestRequestTypeDef(
    _RequiredListVehiclesInFleetRequestRequestTypeDef,
    _OptionalListVehiclesInFleetRequestRequestTypeDef,
):
    pass


ListVehiclesRequestRequestTypeDef = TypedDict(
    "ListVehiclesRequestRequestTypeDef",
    {
        "modelManifestArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

VehicleSummaryTypeDef = TypedDict(
    "VehicleSummaryTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "creationTime": datetime,
        "lastModificationTime": datetime,
    },
)

_RequiredObdInterfaceTypeDef = TypedDict(
    "_RequiredObdInterfaceTypeDef",
    {
        "name": str,
        "requestMessageId": int,
    },
)
_OptionalObdInterfaceTypeDef = TypedDict(
    "_OptionalObdInterfaceTypeDef",
    {
        "obdStandard": str,
        "pidRequestIntervalSeconds": int,
        "dtcRequestIntervalSeconds": int,
        "useExtendedIds": bool,
        "hasTransmissionEcu": bool,
    },
    total=False,
)


class ObdInterfaceTypeDef(_RequiredObdInterfaceTypeDef, _OptionalObdInterfaceTypeDef):
    pass


_RequiredSensorTypeDef = TypedDict(
    "_RequiredSensorTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
    },
)
_OptionalSensorTypeDef = TypedDict(
    "_OptionalSensorTypeDef",
    {
        "description": str,
        "unit": str,
        "allowedValues": Sequence[str],
        "min": float,
        "max": float,
    },
    total=False,
)


class SensorTypeDef(_RequiredSensorTypeDef, _OptionalSensorTypeDef):
    pass


_RequiredObdSignalTypeDef = TypedDict(
    "_RequiredObdSignalTypeDef",
    {
        "pidResponseLength": int,
        "serviceMode": int,
        "pid": int,
        "scaling": float,
        "offset": float,
        "startByte": int,
        "byteLength": int,
    },
)
_OptionalObdSignalTypeDef = TypedDict(
    "_OptionalObdSignalTypeDef",
    {
        "bitRightShift": int,
        "bitMaskLength": int,
    },
    total=False,
)


class ObdSignalTypeDef(_RequiredObdSignalTypeDef, _OptionalObdSignalTypeDef):
    pass


TimestreamResourcesTypeDef = TypedDict(
    "TimestreamResourcesTypeDef",
    {
        "timestreamDatabaseName": str,
        "timestreamTableName": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredUpdateCampaignRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCampaignRequestRequestTypeDef",
    {
        "name": str,
        "action": UpdateCampaignActionType,
    },
)
_OptionalUpdateCampaignRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCampaignRequestRequestTypeDef",
    {
        "description": str,
        "dataExtraDimensions": Sequence[str],
    },
    total=False,
)


class UpdateCampaignRequestRequestTypeDef(
    _RequiredUpdateCampaignRequestRequestTypeDef, _OptionalUpdateCampaignRequestRequestTypeDef
):
    pass


_RequiredUpdateFleetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFleetRequestRequestTypeDef",
    {
        "fleetId": str,
    },
)
_OptionalUpdateFleetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFleetRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)


class UpdateFleetRequestRequestTypeDef(
    _RequiredUpdateFleetRequestRequestTypeDef, _OptionalUpdateFleetRequestRequestTypeDef
):
    pass


_RequiredUpdateModelManifestRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateModelManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateModelManifestRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateModelManifestRequestRequestTypeDef",
    {
        "description": str,
        "nodesToAdd": Sequence[str],
        "nodesToRemove": Sequence[str],
        "status": ManifestStatusType,
    },
    total=False,
)


class UpdateModelManifestRequestRequestTypeDef(
    _RequiredUpdateModelManifestRequestRequestTypeDef,
    _OptionalUpdateModelManifestRequestRequestTypeDef,
):
    pass


_RequiredUpdateVehicleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalUpdateVehicleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVehicleRequestRequestTypeDef",
    {
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "attributes": Mapping[str, str],
        "attributeUpdateMode": UpdateModeType,
    },
    total=False,
)


class UpdateVehicleRequestRequestTypeDef(
    _RequiredUpdateVehicleRequestRequestTypeDef, _OptionalUpdateVehicleRequestRequestTypeDef
):
    pass


BatchCreateVehicleResponseTypeDef = TypedDict(
    "BatchCreateVehicleResponseTypeDef",
    {
        "vehicles": List[CreateVehicleResponseItemTypeDef],
        "errors": List[CreateVehicleErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateCampaignResponseTypeDef = TypedDict(
    "CreateCampaignResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateDecoderManifestResponseTypeDef = TypedDict(
    "CreateDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateFleetResponseTypeDef = TypedDict(
    "CreateFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateModelManifestResponseTypeDef = TypedDict(
    "CreateModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateSignalCatalogResponseTypeDef = TypedDict(
    "CreateSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateVehicleResponseTypeDef = TypedDict(
    "CreateVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "thingArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteCampaignResponseTypeDef = TypedDict(
    "DeleteCampaignResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteDecoderManifestResponseTypeDef = TypedDict(
    "DeleteDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteFleetResponseTypeDef = TypedDict(
    "DeleteFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteModelManifestResponseTypeDef = TypedDict(
    "DeleteModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteSignalCatalogResponseTypeDef = TypedDict(
    "DeleteSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteVehicleResponseTypeDef = TypedDict(
    "DeleteVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDecoderManifestResponseTypeDef = TypedDict(
    "GetDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "modelManifestArn": str,
        "status": ManifestStatusType,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetFleetResponseTypeDef = TypedDict(
    "GetFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "description": str,
        "signalCatalogArn": str,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetModelManifestResponseTypeDef = TypedDict(
    "GetModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "signalCatalogArn": str,
        "status": ManifestStatusType,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetVehicleResponseTypeDef = TypedDict(
    "GetVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "attributes": Dict[str, str],
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ImportDecoderManifestResponseTypeDef = TypedDict(
    "ImportDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ImportSignalCatalogResponseTypeDef = TypedDict(
    "ImportSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListFleetsForVehicleResponseTypeDef = TypedDict(
    "ListFleetsForVehicleResponseTypeDef",
    {
        "fleets": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListVehiclesInFleetResponseTypeDef = TypedDict(
    "ListVehiclesInFleetResponseTypeDef",
    {
        "vehicles": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateCampaignResponseTypeDef = TypedDict(
    "UpdateCampaignResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": CampaignStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateDecoderManifestResponseTypeDef = TypedDict(
    "UpdateDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateFleetResponseTypeDef = TypedDict(
    "UpdateFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateModelManifestResponseTypeDef = TypedDict(
    "UpdateModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateSignalCatalogResponseTypeDef = TypedDict(
    "UpdateSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateVehicleResponseTypeDef = TypedDict(
    "UpdateVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchUpdateVehicleRequestRequestTypeDef = TypedDict(
    "BatchUpdateVehicleRequestRequestTypeDef",
    {
        "vehicles": Sequence[UpdateVehicleRequestItemTypeDef],
    },
)

BatchUpdateVehicleResponseTypeDef = TypedDict(
    "BatchUpdateVehicleResponseTypeDef",
    {
        "vehicles": List[UpdateVehicleResponseItemTypeDef],
        "errors": List[UpdateVehicleErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListCampaignsResponseTypeDef = TypedDict(
    "ListCampaignsResponseTypeDef",
    {
        "campaignSummaries": List[CampaignSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

NetworkFileDefinitionTypeDef = TypedDict(
    "NetworkFileDefinitionTypeDef",
    {
        "canDbc": CanDbcDefinitionTypeDef,
    },
    total=False,
)

GetLoggingOptionsResponseTypeDef = TypedDict(
    "GetLoggingOptionsResponseTypeDef",
    {
        "cloudWatchLogDelivery": CloudWatchLogDeliveryOptionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutLoggingOptionsRequestRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestRequestTypeDef",
    {
        "cloudWatchLogDelivery": CloudWatchLogDeliveryOptionsTypeDef,
    },
)

CollectionSchemeTypeDef = TypedDict(
    "CollectionSchemeTypeDef",
    {
        "timeBasedCollectionScheme": TimeBasedCollectionSchemeTypeDef,
        "conditionBasedCollectionScheme": ConditionBasedCollectionSchemeTypeDef,
    },
    total=False,
)

_RequiredCreateFleetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFleetRequestRequestTypeDef",
    {
        "fleetId": str,
        "signalCatalogArn": str,
    },
)
_OptionalCreateFleetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFleetRequestRequestTypeDef",
    {
        "description": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateFleetRequestRequestTypeDef(
    _RequiredCreateFleetRequestRequestTypeDef, _OptionalCreateFleetRequestRequestTypeDef
):
    pass


_RequiredCreateModelManifestRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelManifestRequestRequestTypeDef",
    {
        "name": str,
        "nodes": Sequence[str],
        "signalCatalogArn": str,
    },
)
_OptionalCreateModelManifestRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelManifestRequestRequestTypeDef",
    {
        "description": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateModelManifestRequestRequestTypeDef(
    _RequiredCreateModelManifestRequestRequestTypeDef,
    _OptionalCreateModelManifestRequestRequestTypeDef,
):
    pass


_RequiredCreateVehicleRequestItemTypeDef = TypedDict(
    "_RequiredCreateVehicleRequestItemTypeDef",
    {
        "vehicleName": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
    },
)
_OptionalCreateVehicleRequestItemTypeDef = TypedDict(
    "_OptionalCreateVehicleRequestItemTypeDef",
    {
        "attributes": Mapping[str, str],
        "associationBehavior": VehicleAssociationBehaviorType,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateVehicleRequestItemTypeDef(
    _RequiredCreateVehicleRequestItemTypeDef, _OptionalCreateVehicleRequestItemTypeDef
):
    pass


_RequiredCreateVehicleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
    },
)
_OptionalCreateVehicleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVehicleRequestRequestTypeDef",
    {
        "attributes": Mapping[str, str],
        "associationBehavior": VehicleAssociationBehaviorType,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateVehicleRequestRequestTypeDef(
    _RequiredCreateVehicleRequestRequestTypeDef, _OptionalCreateVehicleRequestRequestTypeDef
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

ListDecoderManifestsResponseTypeDef = TypedDict(
    "ListDecoderManifestsResponseTypeDef",
    {
        "summaries": List[DecoderManifestSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListFleetsResponseTypeDef = TypedDict(
    "ListFleetsResponseTypeDef",
    {
        "fleetSummaries": List[FleetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredImportSignalCatalogRequestRequestTypeDef = TypedDict(
    "_RequiredImportSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalImportSignalCatalogRequestRequestTypeDef = TypedDict(
    "_OptionalImportSignalCatalogRequestRequestTypeDef",
    {
        "description": str,
        "vss": FormattedVssTypeDef,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class ImportSignalCatalogRequestRequestTypeDef(
    _RequiredImportSignalCatalogRequestRequestTypeDef,
    _OptionalImportSignalCatalogRequestRequestTypeDef,
):
    pass


GetRegisterAccountStatusResponseTypeDef = TypedDict(
    "GetRegisterAccountStatusResponseTypeDef",
    {
        "customerAccountId": str,
        "accountStatus": RegistrationStatusType,
        "timestreamRegistrationResponse": TimestreamRegistrationResponseTypeDef,
        "iamRegistrationResponse": IamRegistrationResponseTypeDef,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSignalCatalogResponseTypeDef = TypedDict(
    "GetSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "nodeCounts": NodeCountsTypeDef,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredGetVehicleStatusRequestGetVehicleStatusPaginateTypeDef = TypedDict(
    "_RequiredGetVehicleStatusRequestGetVehicleStatusPaginateTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalGetVehicleStatusRequestGetVehicleStatusPaginateTypeDef = TypedDict(
    "_OptionalGetVehicleStatusRequestGetVehicleStatusPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class GetVehicleStatusRequestGetVehicleStatusPaginateTypeDef(
    _RequiredGetVehicleStatusRequestGetVehicleStatusPaginateTypeDef,
    _OptionalGetVehicleStatusRequestGetVehicleStatusPaginateTypeDef,
):
    pass


ListCampaignsRequestListCampaignsPaginateTypeDef = TypedDict(
    "ListCampaignsRequestListCampaignsPaginateTypeDef",
    {
        "status": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef = TypedDict(
    "_RequiredListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef",
    {
        "name": str,
    },
)
_OptionalListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef = TypedDict(
    "_OptionalListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef(
    _RequiredListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef,
    _OptionalListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef,
):
    pass


_RequiredListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef = TypedDict(
    "_RequiredListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef",
    {
        "name": str,
    },
)
_OptionalListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef = TypedDict(
    "_OptionalListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef(
    _RequiredListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef,
    _OptionalListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef,
):
    pass


ListDecoderManifestsRequestListDecoderManifestsPaginateTypeDef = TypedDict(
    "ListDecoderManifestsRequestListDecoderManifestsPaginateTypeDef",
    {
        "modelManifestArn": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef = TypedDict(
    "_RequiredListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef = TypedDict(
    "_OptionalListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef(
    _RequiredListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef,
    _OptionalListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef,
):
    pass


ListFleetsRequestListFleetsPaginateTypeDef = TypedDict(
    "ListFleetsRequestListFleetsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef = TypedDict(
    "_RequiredListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef",
    {
        "name": str,
    },
)
_OptionalListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef = TypedDict(
    "_OptionalListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef(
    _RequiredListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef,
    _OptionalListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef,
):
    pass


ListModelManifestsRequestListModelManifestsPaginateTypeDef = TypedDict(
    "ListModelManifestsRequestListModelManifestsPaginateTypeDef",
    {
        "signalCatalogArn": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef = TypedDict(
    "_RequiredListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef",
    {
        "name": str,
    },
)
_OptionalListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef = TypedDict(
    "_OptionalListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef(
    _RequiredListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef,
    _OptionalListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef,
):
    pass


ListSignalCatalogsRequestListSignalCatalogsPaginateTypeDef = TypedDict(
    "ListSignalCatalogsRequestListSignalCatalogsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef = TypedDict(
    "_RequiredListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef",
    {
        "fleetId": str,
    },
)
_OptionalListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef = TypedDict(
    "_OptionalListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef(
    _RequiredListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef,
    _OptionalListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef,
):
    pass


ListVehiclesRequestListVehiclesPaginateTypeDef = TypedDict(
    "ListVehiclesRequestListVehiclesPaginateTypeDef",
    {
        "modelManifestArn": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

GetVehicleStatusResponseTypeDef = TypedDict(
    "GetVehicleStatusResponseTypeDef",
    {
        "campaigns": List[VehicleStatusTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListModelManifestsResponseTypeDef = TypedDict(
    "ListModelManifestsResponseTypeDef",
    {
        "summaries": List[ModelManifestSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListSignalCatalogsResponseTypeDef = TypedDict(
    "ListSignalCatalogsResponseTypeDef",
    {
        "summaries": List[SignalCatalogSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListVehiclesResponseTypeDef = TypedDict(
    "ListVehiclesResponseTypeDef",
    {
        "vehicleSummaries": List[VehicleSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredNetworkInterfaceTypeDef = TypedDict(
    "_RequiredNetworkInterfaceTypeDef",
    {
        "interfaceId": str,
        "type": NetworkInterfaceTypeType,
    },
)
_OptionalNetworkInterfaceTypeDef = TypedDict(
    "_OptionalNetworkInterfaceTypeDef",
    {
        "canInterface": CanInterfaceTypeDef,
        "obdInterface": ObdInterfaceTypeDef,
    },
    total=False,
)


class NetworkInterfaceTypeDef(_RequiredNetworkInterfaceTypeDef, _OptionalNetworkInterfaceTypeDef):
    pass


NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "branch": BranchTypeDef,
        "sensor": SensorTypeDef,
        "actuator": ActuatorTypeDef,
        "attribute": AttributeTypeDef,
    },
    total=False,
)

_RequiredSignalDecoderTypeDef = TypedDict(
    "_RequiredSignalDecoderTypeDef",
    {
        "fullyQualifiedName": str,
        "type": SignalDecoderTypeType,
        "interfaceId": str,
    },
)
_OptionalSignalDecoderTypeDef = TypedDict(
    "_OptionalSignalDecoderTypeDef",
    {
        "canSignal": CanSignalTypeDef,
        "obdSignal": ObdSignalTypeDef,
    },
    total=False,
)


class SignalDecoderTypeDef(_RequiredSignalDecoderTypeDef, _OptionalSignalDecoderTypeDef):
    pass


_RequiredRegisterAccountRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterAccountRequestRequestTypeDef",
    {
        "timestreamResources": TimestreamResourcesTypeDef,
    },
)
_OptionalRegisterAccountRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterAccountRequestRequestTypeDef",
    {
        "iamResources": IamResourcesTypeDef,
    },
    total=False,
)


class RegisterAccountRequestRequestTypeDef(
    _RequiredRegisterAccountRequestRequestTypeDef, _OptionalRegisterAccountRequestRequestTypeDef
):
    pass


RegisterAccountResponseTypeDef = TypedDict(
    "RegisterAccountResponseTypeDef",
    {
        "registerAccountStatus": RegistrationStatusType,
        "timestreamResources": TimestreamResourcesTypeDef,
        "iamResources": IamResourcesTypeDef,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ImportDecoderManifestRequestRequestTypeDef = TypedDict(
    "ImportDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
        "networkFileDefinitions": Sequence[NetworkFileDefinitionTypeDef],
    },
)

_RequiredCreateCampaignRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCampaignRequestRequestTypeDef",
    {
        "name": str,
        "signalCatalogArn": str,
        "targetArn": str,
        "collectionScheme": CollectionSchemeTypeDef,
    },
)
_OptionalCreateCampaignRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCampaignRequestRequestTypeDef",
    {
        "description": str,
        "startTime": Union[datetime, str],
        "expiryTime": Union[datetime, str],
        "postTriggerCollectionDuration": int,
        "diagnosticsMode": DiagnosticsModeType,
        "spoolingMode": SpoolingModeType,
        "compression": CompressionType,
        "priority": int,
        "signalsToCollect": Sequence[SignalInformationTypeDef],
        "dataExtraDimensions": Sequence[str],
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateCampaignRequestRequestTypeDef(
    _RequiredCreateCampaignRequestRequestTypeDef, _OptionalCreateCampaignRequestRequestTypeDef
):
    pass


GetCampaignResponseTypeDef = TypedDict(
    "GetCampaignResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "signalCatalogArn": str,
        "targetArn": str,
        "status": CampaignStatusType,
        "startTime": datetime,
        "expiryTime": datetime,
        "postTriggerCollectionDuration": int,
        "diagnosticsMode": DiagnosticsModeType,
        "spoolingMode": SpoolingModeType,
        "compression": CompressionType,
        "priority": int,
        "signalsToCollect": List[SignalInformationTypeDef],
        "collectionScheme": CollectionSchemeTypeDef,
        "dataExtraDimensions": List[str],
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchCreateVehicleRequestRequestTypeDef = TypedDict(
    "BatchCreateVehicleRequestRequestTypeDef",
    {
        "vehicles": Sequence[CreateVehicleRequestItemTypeDef],
    },
)

ListDecoderManifestNetworkInterfacesResponseTypeDef = TypedDict(
    "ListDecoderManifestNetworkInterfacesResponseTypeDef",
    {
        "networkInterfaces": List[NetworkInterfaceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateSignalCatalogRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateSignalCatalogRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSignalCatalogRequestRequestTypeDef",
    {
        "description": str,
        "nodes": Sequence[NodeTypeDef],
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateSignalCatalogRequestRequestTypeDef(
    _RequiredCreateSignalCatalogRequestRequestTypeDef,
    _OptionalCreateSignalCatalogRequestRequestTypeDef,
):
    pass


ListModelManifestNodesResponseTypeDef = TypedDict(
    "ListModelManifestNodesResponseTypeDef",
    {
        "nodes": List[NodeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListSignalCatalogNodesResponseTypeDef = TypedDict(
    "ListSignalCatalogNodesResponseTypeDef",
    {
        "nodes": List[NodeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdateSignalCatalogRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateSignalCatalogRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSignalCatalogRequestRequestTypeDef",
    {
        "description": str,
        "nodesToAdd": Sequence[NodeTypeDef],
        "nodesToUpdate": Sequence[NodeTypeDef],
        "nodesToRemove": Sequence[str],
    },
    total=False,
)


class UpdateSignalCatalogRequestRequestTypeDef(
    _RequiredUpdateSignalCatalogRequestRequestTypeDef,
    _OptionalUpdateSignalCatalogRequestRequestTypeDef,
):
    pass


_RequiredCreateDecoderManifestRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
        "modelManifestArn": str,
    },
)
_OptionalCreateDecoderManifestRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDecoderManifestRequestRequestTypeDef",
    {
        "description": str,
        "signalDecoders": Sequence[SignalDecoderTypeDef],
        "networkInterfaces": Sequence[NetworkInterfaceTypeDef],
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateDecoderManifestRequestRequestTypeDef(
    _RequiredCreateDecoderManifestRequestRequestTypeDef,
    _OptionalCreateDecoderManifestRequestRequestTypeDef,
):
    pass


ListDecoderManifestSignalsResponseTypeDef = TypedDict(
    "ListDecoderManifestSignalsResponseTypeDef",
    {
        "signalDecoders": List[SignalDecoderTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdateDecoderManifestRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateDecoderManifestRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDecoderManifestRequestRequestTypeDef",
    {
        "description": str,
        "signalDecodersToAdd": Sequence[SignalDecoderTypeDef],
        "signalDecodersToUpdate": Sequence[SignalDecoderTypeDef],
        "signalDecodersToRemove": Sequence[str],
        "networkInterfacesToAdd": Sequence[NetworkInterfaceTypeDef],
        "networkInterfacesToUpdate": Sequence[NetworkInterfaceTypeDef],
        "networkInterfacesToRemove": Sequence[str],
        "status": ManifestStatusType,
    },
    total=False,
)


class UpdateDecoderManifestRequestRequestTypeDef(
    _RequiredUpdateDecoderManifestRequestRequestTypeDef,
    _OptionalUpdateDecoderManifestRequestRequestTypeDef,
):
    pass
