from __future__ import annotations

import json
from datetime import datetime
from enum import Enum
from typing import Any, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class BaseADTModel(BaseModel):
    def dump(self) -> dict:
        return json.loads(
            self.json(by_alias=True, exclude_none=True, exclude_unset=True)
        )

    class Config:
        use_enum_values = True
        anystr_strip_whitespace = True


class Granularity(str, Enum):
    # https://rwes-gitlab01.internal.imsglobal.com/e360/analytic-dataset-tools-api/-/blob/master/src/Models/Enums/Granularity.cs
    EVENT = "event"  # -1
    PATIENT = "patient"  # 0
    OTHER = "other"  # 1


class CharacteristicReportColumnType(str, Enum):
    # https://rwes-gitlab01.internal.imsglobal.com/e360/analytic-dataset-tools-api/-/blob/master/src/Models/Enums/CharacteristicReportColumnType.cs
    PAT_ID = "patId"
    EVENT_COUNT = "eventCount"
    EVENT_COUNT_BEFORE_INDEX_DATE = "eventCountBeforeIndexDate"
    EVENT_COUNT_ON_OR_AFTER_INDEX_DATE = "eventCountOnOrAfterIndexDate"
    DAYS_DIFFERENCE_BETWEEN_EARLIEST_EVENT_ON_OR_AFTER_INDEX_DATE = (
        "daysDifferenceBetweenEarliestEventOnOrAfterIndexDate"
    )
    DAYS_DIFFERENCE_BETWEEN_LATEST_EVENT_BEFORE_INDEX_DATE = (
        "daysDifferenceBetweenLatestEventBeforeIndexDate"
    )
    GENDER = "gender"
    AGE_GROUP = "ageGroup"
    AGEAT_INDEX_DATE = "ageatIndexDate"
    YEAROF_INDEX_DATE = "yearofIndexDate"
    MONTHOF_INDEX_DATE = "monthofIndexDate"
    FUP_PERIOD = "fupPeriod"
    INDEX_DATE = "indexDate"
    EVENT_OCCURRENCE_BEFORE_INDEX_DATE = "eventOccurrenceBeforeIndexDate"
    EVENT_OCCURRENCE_ON_OR_AFTER_INDEX_DATE = "eventOccurrenceOnOrAfterIndexDate"
    ETHNICITY = "ethnicity"
    SITE_KEY = "siteKey"
    SITE_LOCATION = "siteLocation"
    PATIENT_LINKAGE = "patientLinkage"
    EMR_VALUE = "emrValue"
    DAYS_TO_EVENT_FROM_INDEX_DATE = "daysToEventFromIndexDate"
    EVENT_DATE = "eventDate"
    AGE_AT_EVENT_DATE = "ageAtEventDate"
    EVENT_OCCURRENCE = "eventOccurrence"
    EMR_LOOKUP_VALUE = "emrLookupValue"
    CODELIST_GROUP = "codelistGroup"
    INDEPENDENT_CODELIST_GROUP_NAMES = "independentCodelistGroupNames"
    PAYER_TYPE = "payerType"
    SPECIALITY = "speciality"
    GEOGRAPHIC_REGION = "geographicRegion"
    HEALTH_PLAN_TYPE = "healthPlanType"
    DEMOGRAPHIC_GROUP_DESCRIPTION = "demographicGroupDescription"
    YEAR_OF_BIRTH = "yearOfBirth"
    DATABASE_ENTRY_DATE = "databaseEntryDate"
    FIRST_EVENT_DATE = "firstEventDate"
    DATABASE_EXIT_DATE = "databaseExitDate"
    DEMOGRAPHIC_GROUP_ORDINAL = "demographicGroupOrdinal"
    EARLIEST_EVENT_INSTANCE = "earliestEventInstance"
    LATEST_EVENT_INSTANCE = "latestEventInstance"
    EARLIEST_EVENT_LOOKUP_INSTANCE = "earliestEventLookupInstance"
    LATEST_EVENT_LOOKUP_INSTANCE = "latestEventLookupInstance"
    TOTAL_COST_OF_CARE_AFTER_INDEX = "totalCostOfCareAfterIndex"
    COMPOUND_PAT_ID = "compoundPatId"
    GENOMIC_PATIENT_SEQUENCE_NUMBER = "genomicPatientSequenceNumber"
    GENOMIC_PATIENT_SEQUENCE_DATE = "genomicPatientSequenceDate"
    DAYS_DIFFERENCE_BETWEEN_EARLIEST_EVENT_START_DATE_AFTER_INDEX_DATE = (
        "daysDifferenceBetweenEarliestEventStartDateAfterIndexDate"
    )
    DAYS_DIFFERENCE_BETWEEN_LATEST_EVENT_START_DATE_BEFORE_INDEX_DATE = (
        "daysDifferenceBetweenLatestEventStartDateBeforeIndexDate"
    )
    EMPHASIS = "emphasis"
    PRACTICE = "practice"
    PRACTICE_PHYSICIAN_COUNT = "practicePhysicianCount"
    EMR_VALUE_AGGREGATE_SUM = "emrValueAggregateSum"
    EMR_VALUE_AGGREGATE_LOOKUP_SUM = "emrValueAggregateLookupSum"
    EMR_VALUE_AGGREGATE_MIN = "emrValueAggregateMin"
    EMR_VALUE_AGGREGATE_LOOKUP_MIN = "emrValueAggregateLookupMin"
    EMR_VALUE_AGGREGATE_MAX = "emrValueAggregateMax"
    EMR_VALUE_AGGREGATE_LOOKUP_MAX = "emrValueAggregateLookupMax"
    EMR_VALUE_AGGREGATE_MEAN = "emrValueAggregateMean"
    EMR_VALUE_AGGREGATE_LOOKUP_MEAN = "emrValueAggregateLookupMean"
    EMR_VALUE_AGGREGATE_COUNT_DISTINCT = "emrValueAggregateCountDistinct"
    EMR_VALUE_AGGREGATE_LOOKUP_COUNT_DISTINCT = "emrValueAggregateLookupCountDistinct"
    EMR_VALUE_AGGREGATE_STANDARD_DEVIATION = "emrValueAggregateStandardDeviation"
    EMR_VALUE_AGGREGATE_LOOKUP_STANDARD_DEVIATION = (
        "emrValueAggregateLookupStandardDeviation"
    )
    EMR_VALUE_AGGREGATE_VARIANCE = "emrValueAggregateVariance"
    EMR_VALUE_AGGREGATE_LOOKUP_VARIANCE = "emrValueAggregateLookupVariance"
    HIGH_DIMENSIONAL_RESULT = "highDimensionalResult"
    PATIENT_AGE = "patientAge"
    PATIENT_BMI = "patientBmi"
    PATIENT_WEIGHT = "patientWeight"
    PATIENT_HEIGHT = "patientHeight"
    FEE_SCHEDULE = "feeSchedule"
    INSURANCE = "insurance"
    INSURANCE_STATUS = "insuranceStatus"
    SMOKER_STATUS = "smokerStatus"
    DOCTOR_ID = "doctorId"
    DOCTOR_AGE_GROUP = "doctorAgeGroup"
    DIABETOLOGY = "diabetology"
    REGION = "region"
    UP_TO_DATE = "upToDate"
    PATIENT_LOCATION = "patientLocation"
    MERGED_DATASET = "mergedDataset"
    PATIENT_STATE = "patientState"
    PATIENT_REGION = "patientRegion"
    DEATH_DATE = "deathDate"


class CharacteristicReportColumnModel(BaseADTModel):
    reportColumnTypeId: Optional[CharacteristicReportColumnType] = None
    characteristicTypeId: Optional[int] = None
    characteristicId: Optional[int] = None
    order: Optional[int] = None
    name: Optional[str] = None
    emrColumnName: Optional[str] = None
    emrEventFilter: Optional[int] = None
    codelistGroupName: Optional[str] = None
    codelistId: Optional[int] = None
    mergedDatasetId: Optional[UUID] = None
    originalName: Optional[str] = None


class AnalyticDatasetStatus(str, Enum):
    # https://rwes-gitlab01.internal.imsglobal.com/e360/analytic-dataset-tools-api/-/blob/master/src/Models/Enums/AnalyticDatasetStatus.cs
    NOT_STARTED = "notStarted"  # 1
    IN_PROGRESS = "inProgress"  # 2
    COMPRESSING = "compressing"  # 3
    COMPLETED = "completed"  # 4
    FAILED = "failed"  # 5
    CANCELLED = "cancelled"  # 6
    CANCELLATION_PENDING = "cancellationPending"  # 7


class AnalyticDatasetSource(str, Enum):
    # https://rwes-gitlab01.internal.imsglobal.com/e360/analytic-dataset-tools-api/-/blob/master/src/Models/Enums/AnalyticDatasetSource.cs
    STANDARD = "standard"  # 1
    UPLOAD = "upload"  # 2


class OutputType(str, Enum):
    # https://rwes-gitlab01.internal.imsglobal.com/e360/analytic-dataset-tools-api/-/blob/master/src/Models/Enums/OutputType.cs
    CSV = "csv"  # 1
    ZIP = "zip"  # 2
    PARQUET = "parquet"  # 3
    MULTIPARTPARQUETZIP = "multipartparquetzip"  # 4


class AnalyticDatasetResultModel(BaseADTModel):
    completedDate: Optional[datetime] = None
    downloadUrl: Optional[str] = None
    fileSize: Optional[int] = None
    rowCount: Optional[int] = None
    reason: Optional[str] = None


class EmailAddressModel(BaseADTModel):
    name: Optional[str] = None
    address: Optional[str] = None


class AnalyticDatasetModel(BaseADTModel):
    analyticDatasetDefinitionId: Optional[UUID] = None
    assetId: Optional[UUID] = None
    createdByUserId: Optional[UUID] = None
    granularity: Optional[Granularity] = Granularity.PATIENT
    cohortOfInterestId: Optional[int] = None
    cohortOfInterestAssetId: Optional[UUID] = None
    combineEventsOnSameDay: Optional[bool] = None
    columns: Optional[List[CharacteristicReportColumnModel]] = None
    randomPatientCount: Optional[int] = None
    status: Optional[AnalyticDatasetStatus] = None
    source: Optional[AnalyticDatasetSource] = None
    outputType: Optional[OutputType] = OutputType.ZIP
    result: Optional[AnalyticDatasetResultModel] = None
    emailAddresses: Optional[List[EmailAddressModel]] = None
    generateAsset: Optional[bool] = None
    datasetReleaseIdentifier: Optional[str] = None
    hashSecret: Optional[str] = None
    id: Optional[UUID] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None


class ErrorMessageModel(BaseADTModel):
    message: Optional[str] = None
    errorCode: Optional[str] = None
    details: Optional[List[str]] = None


class AnalyticDatasetColumnsModel(BaseADTModel):
    granularity: Optional[Granularity] = None
    patient: Optional[List[CharacteristicReportColumnModel]] = None
    event: Optional[List[CharacteristicReportColumnModel]] = None
    other: Optional[List[CharacteristicReportColumnModel]] = None


class AnalyticDatasetRowsModel(BaseADTModel):
    header: Optional[List[str]] = None
    values: Optional[List[List[str]]] = None


class CharacteristicType(str, Enum):
    # https://rwes-gitlab01.internal.imsglobal.com/e360/analytic-dataset-tools-api/-/blob/master/src/Models/Enums/CharacteristicType.cs
    DEMOGRAPHIC = "demographic"  # 1
    CHARACTERISTIC = "characteristic"  # 2
    HIGH_DIMENSIONAL = "highDimensional"  # 3
    ANALYTIC_DATASET = "analyticDataset"  # 4


class AssetType(str, Enum):
    COHORT = "cohort"  # 1
    CARD = "card"  # 3


class PatientLevelEventInstanceType(str, Enum):
    # https://rwes-gitlab01.internal.imsglobal.com/e360/analytic-dataset-tools-api/-/blob/master/src/Models/Enums/PatientLevelEventInstanceType.cs
    EARLIEST = "earliest"  # 0
    LATEST = "latest"  # 1


class AggregateType(str, Enum):
    # https://rwes-gitlab01.internal.imsglobal.com/e360/analytic-dataset-tools-api/-/blob/master/src/Models/Enums/AggregateType.cs
    EARLIEST = "earliest"  # 1
    LATEST = "latest"  # 2
    SUM = "sum"  # 3
    MIN = "min"  # 4
    MAX = "max"  # 5
    MEAN = "mean"  # 6
    COUNT_DISTINCT = "countDistinct"  # 7
    STANDARD_DEVIATION = "standardDeviation"  # 8
    VARIANCE = "variance"  # 9


class PatientLevelAggregateModel(BaseADTModel):
    aggregateType: Optional[AggregateType] = None
    description: Optional[str] = None
    selected: Optional[bool] = None
    disabled: Optional[bool] = None


class EmrCharacteristicModel(BaseADTModel):
    columnName: Optional[str] = None
    description: Optional[str] = None
    selected: Optional[bool] = None
    patientLevelAggregates: Optional[List[PatientLevelAggregateModel]] = None
    inaccessibleForUser: Optional[bool] = None


class EmrEventFilterModel(BaseADTModel):
    columnName: Optional[str] = None
    description: Optional[str] = None
    filterId: Optional[int] = None
    selected: Optional[bool] = None
    inaccessibleForUser: Optional[bool] = None
    patientLevelAggregates: Optional[List[PatientLevelAggregateModel]] = None


class DatePeriod(str, Enum):
    # https://rwes-gitlab01.internal.imsglobal.com/e360/analytic-dataset-tools-api/-/blob/master/src/Models/Enums/DatePeriod.cs
    DAYS = "days"  # 1
    WEEKS = "weeks"  # 2
    MONTHS = "months"  # 3
    YEARS = "years"  # 4


class CharacteristicModel(BaseADTModel):
    type: Optional[CharacteristicType] = None
    assetType: Optional[AssetType] = None
    assetId: Optional[UUID] = None
    codelistCharacteristic: Optional[bool] = None
    isGroupedCodelist: Optional[bool] = None
    isErrorLoading: Optional[bool] = None
    errorLoadingMessage: Optional[str] = None
    eventCount: Optional[bool] = None
    eventCountBeforeIndexDate: Optional[bool] = None
    eventCountOnOrAfterIndexDate: Optional[bool] = None
    daysDifferenceBetweenLatestEventBeforeIndexDate: Optional[bool] = None
    daysDifferenceBetweenEarliestEventAfterIndexDate: Optional[bool] = None
    daysDifferenceBetweenLatestEventStartDateBeforeIndexDate: Optional[bool] = None
    daysDifferenceBetweenEarliestEventStartDateAfterIndexDate: Optional[bool] = None
    eventOccurrenceBeforeIndexDate: Optional[bool] = None
    eventOccurrenceOnOrAfterIndexDate: Optional[bool] = None
    eventOccurrence: Optional[bool] = None
    codelistGroup: Optional[bool] = None
    demographicGroupDescription: Optional[bool] = None
    demographicGroupOrdinal: Optional[bool] = None
    firstEventDate: Optional[bool] = None
    patientLevelEventInstanceType: Optional[PatientLevelEventInstanceType] = None
    costOfCareDays: Optional[int] = None
    emrCharacteristics: Optional[List[EmrCharacteristicModel]] = None
    emrLookupCharacteristics: Optional[List[EmrCharacteristicModel]] = None
    emrEventFilters: Optional[List[EmrEventFilterModel]] = None
    emrExtraCharacteristics: Optional[List[EmrCharacteristicModel]] = None
    lowerBound: Optional[int] = None
    upperBound: Optional[int] = None
    lowerDatePeriod: Optional[DatePeriod] = None
    upperDatePeriod: Optional[DatePeriod] = None
    exportAsEvent: Optional[bool] = None
    id: Optional[int] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None


class DemographicCharacteristicType(str, Enum):
    # https://rwes-gitlab01.internal.imsglobal.com/e360/analytic-dataset-tools-api/-/blob/master/src/Models/Enums/DemographicCharacteristicType.cs
    GENDER = "gender"  # 1
    AGE_GROUP = "ageGroup"  # 2
    AGE_AT_INDEX_DATE = "ageAtIndexDate"  # 3
    YEAR_OF_INDEX_DATE = "yearOfIndexDate"  # 4
    MONTH_OF_INDEX_DATE = "monthOfIndexDate"  # 5
    FOLLOW_UP_PERIOD = "followUpPeriod"  # 6
    INDEX_DATE = "indexDate"  # 7
    DAYS_TO_EVENT_FROM_INDEX_DATE = "daysToEventFromIndexDate"  # 8
    AGE_AT_EVENT_DATE = "ageAtEventDate"  # 9
    ETHNICITY = "ethnicity"  # 10
    SITE_KEY = "siteKey"  # 11
    SITE_LOCATION = "siteLocation"  # 12
    PATIENT_LINKAGE = "patientLinkage"  # 13
    PAYER_TYPE = "payerType"  # 14
    SPECIALITY = "speciality"  # 15
    GEOGRAPHIC_REGION = "geographicRegion"  # 16
    HEALTH_PLAN_TYPE = "healthPlanType"  # 17
    YEAR_OF_BIRTH = "yearOfBirth"  # 18
    DATABASE_ENTRY_DATE = "databaseEntryDate"  # 19
    DATABASE_EXIT_DATE = "databaseExitDate"  # 20
    TOTAL_COST_OF_CARE_AFTER_INDEX = "totalCostOfCareAfterIndex"  # 21
    EMPHASIS = "emphasis"  # 22
    COMPOUND_PAT_ID = "compoundPatID"  # 23
    PRACTICE_ID = "practiceID"  # 24
    PRACTICE_PHYSICIAN_COUNT = "practicePhysicianCount"  # 25
    PATIENT_AGE = "patientAge"  # 26
    PATIENT_B_M_I = "patientBMI"  # 27
    PATIENT_WEIGHT = "patientWeight"  # 28
    PATIENT_HEIGHT = "patientHeight"  # 29
    FEE_SCHEDULE = "feeSchedule"  # 30
    INSURANCE = "insurance"  # 31
    INSURANCE_STATUS = "insuranceStatus"  # 32
    SMOKER_STATUS = "smokerStatus"  # 33
    DOCTOR_ID = "doctorID"  # 34
    DOCTOR_AGE_GROUP = "doctorAgeGroup"  # 35
    DIABETOLOGY = "diabetology"  # 36
    REGION = "region"  # 37
    UP_TO_DATE = "upToDate"  # 38
    PATIENT_LOCATION = "patientLocation"  # 39
    PATIENT_STATE = "patientState"  # 40
    PATIENT_REGION = "patientRegion"  # 41
    DEATH_DATE = "deathDate"  # 42


class DemographicCharacteristicGroupModel(BaseADTModel):
    description: Optional[str] = None
    from_: Optional[int] = Field(None, alias="from")
    to_: Optional[int] = Field(None, alias="to")
    option: Optional[str] = None
    symbol: Optional[str] = None


class DemographicCharacteristicModel(BaseADTModel):
    typeId: Optional[DemographicCharacteristicType] = None
    title: Optional[str] = None
    columnName: Optional[str] = None
    rawValueDescription: Optional[str] = None
    useRawValue: Optional[bool] = None
    rangeGrouping: Optional[bool] = None
    options: Optional[List[str]] = None
    groups: Optional[List[DemographicCharacteristicGroupModel]] = None
    doesSupportGroupDescription: Optional[bool] = None
    useGroupDescription: Optional[bool] = None
    doesSupportGroupOrdinal: Optional[bool] = None
    useGroupOrdinal: Optional[bool] = None
    costOfCareDays: Optional[int] = None
    exportAsEvent: Optional[bool] = None
    granularitiesSupported: Optional[
        List[Any]
    ] = None  # 'Granularity' replaced to Any due to int/str usage by the service
    id: Optional[int] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None


class CountType(str, Enum):
    PATIENT = "patient"
    EVENT = "event"


class EventDateFilterType(str, Enum):
    ALL = "all"
    ABSOLUTE_DATE_RANGE = "absoluteDateRange"
    BEFORE_INDEX_DATE = "beforeIndexDate"
    ON_OR_AFTER_INDEX_DATE = "onOrAfterIndexDate"
    RELATIVE_TO_INDEX_DATE = "relativeToIndexDate"


class VisitType(str, Enum):
    ALL = "all"
    IN_PATIENT = "inPatient"
    OUT_PATIENT = "outPatient"
    EMERGENCY = "emergency"


class HighDimensionalCharacteristicPostRequestModel(BaseADTModel):
    domain: str
    vocabulary: str
    topCount: int
    countType: Optional[CountType] = None
    leftAnchor: Optional[int] = None
    eventDateFilterType: Optional[EventDateFilterType] = None
    absoluteDateFromDate: Optional[datetime] = None
    absoluteDateToDate: Optional[datetime] = None
    relativeToIndexDatePrePeriod: Optional[int] = None
    relativeToIndexDatePrePeriodType: Optional[int] = None
    relativeToIndexDatePostPeriod: Optional[int] = None
    relativeToIndexDatePostPeriodType: Optional[int] = None
    visitType: Optional[VisitType] = None
    eventOccurrence: Optional[bool] = None
    eventCount: Optional[bool] = None
    descriptionInColumnName: Optional[bool] = None


class JoinType(Enum):
    # https://rwes-gitlab01.internal.imsglobal.com/e360/analytic-dataset-tools-api/-/blob/master/src/Models/Enums/JoinType.cs
    INNER = 1
    LEFT_OUTER = 2
    RIGHT_OUTER = 3


class ColumnSelectionType(Enum):
    # https://rwes-gitlab01.internal.imsglobal.com/e360/analytic-dataset-tools-api/-/blob/master/src/Models/Enums/ColumnSelectionType.cs
    ALL = 1
    CUSTOM = 2


class AnalyticDatasetMergeRequestModel(BaseADTModel):
    analyticDatasetAssetId: Optional[UUID] = None
    sourceJoinColumn: Optional[str] = None
    destJoinColumn: Optional[str] = None
    joinType: Optional[JoinType] = None
    columnSelectionType: Optional[ColumnSelectionType] = None
    selectedColumns: Optional[List[str]] = None


class CohortAssetOptions(BaseADTModel):
    createAllCohortAssets: Optional[bool] = None


class AnalyticDatasetDefinitionCreateModel(BaseADTModel):
    datasetSchemaId: Optional[str] = None
    originalCohortId: Optional[int] = None
    originalCohortAssetId: Optional[UUID] = None
    studyPeriodFrom: Optional[datetime] = None
    studyPeriodTo: Optional[datetime] = None
    containerId: Optional[UUID] = None
    defaultGranularity: Optional[Granularity] = None
    assetName: Optional[str] = None
    isAssetHidden: Optional[bool] = None
    characteristics: Optional[List[CharacteristicModel]] = None
    demographicCharacteristics: Optional[List[DemographicCharacteristicModel]] = None
    highDimensionalCharacteristics: Optional[
        List[HighDimensionalCharacteristicPostRequestModel]
    ] = None
    analyticDatasetMergeCharacteristics: Optional[
        List[AnalyticDatasetMergeRequestModel]
    ] = None
    cohortAssetOptions: Optional[CohortAssetOptions] = None
    id: Optional[UUID] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None


class CohortOfInterestCopyStatus(str, Enum):
    # https://rwes-gitlab01.internal.imsglobal.com/e360/analytic-dataset-tools-api/-/blob/master/src/Models/Enums/CohortOfInterestCopyStatus.cs
    PENDING = "pending"  # 1
    COPYING = "copying"  # 2
    COMPLETE = "complete"  # 3
    FAILED = "failed"  # 4


class CohortOfInterestCopyModel(BaseADTModel):
    status: Optional[CohortOfInterestCopyStatus] = None
    errorMessage: Optional[str] = None


class TopNExecutionStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETE = "complete"
    ERROR = "error"


class HighDimensionalCharacteristicTopNExecutionResponseModel(BaseADTModel):
    id: Optional[int] = None
    executionId: Optional[UUID] = None
    status: Optional[TopNExecutionStatus] = None
    message: Optional[str] = None
    dateLastTouched: Optional[datetime] = None


class HighDimensionalCharacteristicColumnsResponseModel(BaseADTModel):
    code: Optional[str] = None
    description: Optional[str] = None
    usageCount: Optional[int] = None


class HighDimensionalCharacteristicResponseModel(BaseADTModel):
    id: Optional[UUID] = None
    domain: Optional[str] = None
    vocabulary: Optional[str] = None
    topCount: Optional[int] = None
    countType: Optional[CountType] = None
    leftAnchor: Optional[int] = None
    eventDateFilterType: Optional[EventDateFilterType] = None
    absoluteDateFromDate: Optional[datetime] = None
    absoluteDateToDate: Optional[datetime] = None
    relativeToIndexDatePrePeriod: Optional[int] = None
    relativeToIndexDatePrePeriodType: Optional[int] = None
    relativeToIndexDatePostPeriod: Optional[int] = None
    relativeToIndexDatePostPeriodType: Optional[int] = None
    visitType: Optional[VisitType] = None
    eventOccurrence: Optional[bool] = None
    eventCount: Optional[bool] = None
    descriptionInColumnName: Optional[bool] = None
    topNExecution: Optional[
        HighDimensionalCharacteristicTopNExecutionResponseModel
    ] = None
    columns: Optional[List[HighDimensionalCharacteristicColumnsResponseModel]] = None


class AnalyticDatasetMergeResponseModel(BaseADTModel):
    id: Optional[UUID] = None
    analyticDatasetId: Optional[UUID] = None
    analyticDatasetAssetId: Optional[UUID] = None
    outputType: Optional[OutputType] = None
    sourceJoinColumn: Optional[str] = None
    destJoinColumn: Optional[str] = None
    joinType: Optional[JoinType] = None
    columnSelectionType: Optional[ColumnSelectionType] = None
    selectedColumns: Optional[List[str]] = None
    isErrorLoading: Optional[bool] = None
    errorLoadingMessage: Optional[str] = None


class AnalyticDatasetDefinitionRightsModel(BaseADTModel):
    canCreateAnalyticDatasets: Optional[bool] = None
    canDownloadAnalyticDatasets: Optional[bool] = None
    canAccessNetworkExecution: Optional[bool] = None
    canSeePythonAnalyticsWorkbench: Optional[bool] = None
    canAccessPythonAnalyticsWorkbench: Optional[bool] = None
    canSeeSOSExists: Optional[bool] = None
    canAccessSOS: Optional[bool] = None


class AnalyticDatasetDefinitionCapabilitiesModel(BaseADTModel):
    hasPatientAges: Optional[bool] = None
    hasPatientAgeBandingsData: Optional[bool] = None
    hasNetworkFeatureExecutionSupport: Optional[bool] = None
    hasPatientAgeRawValue: Optional[bool] = None


class IndexDateType(str, Enum):
    EARLIEST = "earliest"
    LATEST = "latest"
    ALL = "all"


class AnalyticDatasetDefinitionModel(BaseADTModel):
    datasetSchemaId: Optional[str] = None
    createdByUserId: Optional[UUID] = None
    isErrorLoading: Optional[bool] = None
    originalCohortId: Optional[int] = None
    originalCohortAssetId: Optional[UUID] = None
    studyPeriodFrom: Optional[datetime] = None
    studyPeriodTo: Optional[datetime] = None
    containerId: Optional[UUID] = None
    workspaceAssetId: Optional[UUID] = None
    patientCount: Optional[int] = None
    cohortOfInterestCopyModel: Optional[CohortOfInterestCopyModel] = None
    characteristics: Optional[List[CharacteristicModel]] = None
    demographicCharacteristics: Optional[List[DemographicCharacteristicModel]] = None
    highDimensionalCharacteristics: Optional[
        List[HighDimensionalCharacteristicResponseModel]
    ] = None
    analyticDatasetMergeCharacteristics: Optional[
        List[AnalyticDatasetMergeResponseModel]
    ] = None
    rights: Optional[AnalyticDatasetDefinitionRightsModel] = None
    capabilities: Optional[AnalyticDatasetDefinitionCapabilitiesModel] = None
    cohortOfInterestIndexDateType: Optional[IndexDateType] = None
    source: Optional[AnalyticDatasetSource] = None
    defaultGranularity: Optional[Granularity] = None
    id: Optional[UUID] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None


class AnalyticDatasetAction(Enum):
    DELETE = "delete"
    DOWNLOAD = "download"
    CANCEL = "cancel"


class AnalyticDatasetInfoResponseModel(BaseADTModel):
    id: Optional[UUID] = None
    name: Optional[str] = None
    assetId: Optional[UUID] = None
    status: Optional[AnalyticDatasetStatus] = None
    percentageComplete: Optional[int] = None
    createdAt: Optional[datetime] = None
    completedAt: Optional[datetime] = None
    outputType: Optional[OutputType] = None
    granularity: Optional[Granularity] = None
    rowCount: Optional[int] = None
    allowedActions: Optional[List[AnalyticDatasetAction]] = None
    fileSize: Optional[int] = None


class TopNVisitType(Enum):
    ALL = "All"
    INPATIENT = "InPatient"
    OUTPATIENT = "OutPatient"
    EMERGENCY = "Emergency "


class TopNVocabularyMetadataVisitType(BaseADTModel):
    id: Optional[int] = None
    name: Optional[TopNVisitType] = None


class TopNVocabularyMetadata(BaseADTModel):
    isLeftAnchoringAllowed: Optional[bool] = None
    leftAnchoringOptions: Optional[List[int]] = None
    codelistTypeId: Optional[int] = None
    standardCodeColumn: Optional[str] = None
    cardTypeId: Optional[int] = None
    hasDescription: Optional[bool] = None
    visitTypes: Optional[List[TopNVocabularyMetadataVisitType]] = None


class TopNVocabulary(BaseADTModel):
    name: Optional[str] = None
    metadata: Optional[TopNVocabularyMetadata] = None


class TopNMetadata(BaseADTModel):
    id: Optional[int] = None
    name: Optional[str] = None
    vocabularies: Optional[List[TopNVocabulary]] = None


class TopNMetadataResourceModel(BaseADTModel):
    metadata: Optional[List[TopNMetadata]] = None


class PatientLevelAggregateResponseModel(BaseADTModel):
    aggregateType: Optional[AggregateType] = None
    description: Optional[str] = None
    disabled: Optional[bool] = None


class EmrCharacteristicResponseModel(BaseADTModel):
    columnName: Optional[str] = None
    description: Optional[str] = None
    inaccessibleForUser: Optional[bool] = None
    patientLevelAggregates: Optional[List[PatientLevelAggregateResponseModel]] = None


class EmrEventFilterResponseModel(BaseADTModel):
    columnName: Optional[str] = None
    description: Optional[str] = None
    filterId: Optional[int] = None
    patientLevelAggregates: Optional[List[PatientLevelAggregateResponseModel]] = None


class SimpleCharacteristicResponseModel(BaseADTModel):
    type: Optional[CharacteristicType] = None
    assetType: Optional[AssetType] = None
    assetId: Optional[UUID] = None
    codelistCharacteristic: Optional[bool] = None
    isGroupedCodelist: Optional[bool] = None
    emrCharacteristics: Optional[List[EmrCharacteristicResponseModel]] = None
    emrLookupCharacteristics: Optional[List[EmrCharacteristicResponseModel]] = None
    emrEventFilters: Optional[List[EmrEventFilterResponseModel]] = None
    emrExtraCharacteristics: Optional[List[EmrCharacteristicResponseModel]] = None
    id: Optional[int] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None


class CharacteristicReportSettingModel(BaseADTModel):
    name: Optional[str] = None
    onlyAvailableForCodelistCharacteristics: Optional[bool] = None
    onlyAvailableForGroupedCodelistCharacteristics: Optional[bool] = None
    indexDateTypesSupported: Optional[List[IndexDateType]] = None
    granularitiesSupported: Optional[List[Granularity]] = None
    description: Optional[str] = None
    id: Optional[str] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None


class DemographicCharacteristicTypeModel(BaseADTModel):
    name: Optional[str] = None
    characterLength: Optional[int] = None
    indexDateTypesSupported: Optional[List[IndexDateType]] = None
    schemasSupported: Optional[List[str]] = None
    datasetsSupported: Optional[List[str]] = None
    granularitiesSupported: Optional[List[Granularity]] = None
    doesSupportGroupDescription: Optional[bool] = None
    doesSupportGroupOrdinal: Optional[bool] = None
    id: Optional[str] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None


# Backwards compatibility mapper

AnalyticDatasetFormat = OutputType
