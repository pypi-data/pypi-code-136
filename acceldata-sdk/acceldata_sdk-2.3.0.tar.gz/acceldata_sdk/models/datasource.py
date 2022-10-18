from dataclasses import dataclass, asdict
from typing import List, Dict
from enum import Enum, auto

from acceldata_sdk.errors import TorchSdkException
from acceldata_sdk.models.snapshot import SnapshotData, AssociatedItemType
from acceldata_sdk.models.create_asset import CreateAsset, CreateAssetRelation, RelationType, AssetMetadata
from acceldata_sdk.models.connection import Connection


@dataclass
class ConfigProperty:
    key=None
    value = None

    def __init__(self,
                 key=None,
                 value=None):
        self.key = key
        self.value = value


@dataclass
class Crawler:
    name = None

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return f"Crawler({self.__dict__})"


@dataclass
class DatasourceType:
    id = None
    name = None

    def __init__(self,
                 id = None,
                 name=None):
        self.name = name
        self.id = id


class CreateDataSource:

    def __init__(self,
                 name: str,
                 sourceType: DatasourceType,
                 description: str = None,
                 isVirtual: bool = None,
                 connectionId: int = None,
                 configProperties: List[ConfigProperty] = []
                 ):
        self.name = name
        self.description = description
        self.sourceType = DatasourceType(sourceType.id, sourceType.name)
        if isVirtual is None and connectionId is None:
            raise TorchSdkException('Either provide connection configuration for the assembly or enable isVirtual flag')
        if isVirtual is None:
            self.connectionId = connectionId
            self.configProperties = configProperties
            self.isVirtual = False
        if connectionId is None:
            self.isVirtual = isVirtual

    def __eq__(self, other):
        return self.name == other.name and self.connectionId == other.connectionId

    def __repr__(self):
        return f"DataSource({self.name!r})"


@dataclass
class DatasourceSourceModel:
    id = None
    name = None

    def __init__(self,
                 id = None,
                 name=None):
        self.name = name
        self.id = id


@dataclass
class DatasourceSourceType:

    def __init__(self, id, name, sourceModel=None, connectionTypeId=None, **kwargs):
        """
            Description:
                Datasource source type
        :param id: id of the source type
        :param name: name of the source type
        :param sourceModel: source model
        :param connectionTypeId: (int) connection type id for the given source type
        """
        self.id = id
        self.name = name
        self.connectionTypeId = connectionTypeId
        if isinstance(sourceModel, dict):
            self.sourceModel = DatasourceSourceModel(**sourceModel)
        else:
            self.sourceModel = sourceModel

    def __repr__(self):
        return f"DatasourceSourceType({self.__dict__})"


class ChildType:

    def __init__(self, canProfile, canSample, id, name):
        self.canProfile = canProfile
        self.canSample = canSample
        self.id = id
        self.name = name

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return f"ChildType({self.__dict__})"


class RootAsset:

    def __init__(self, assetId=None, alias=None, isCustom=False, childType=None, name=None, parentId=None):
        self.assetId = assetId
        self.alias = alias
        self.isCustom = isCustom
        if isinstance(childType, dict):
            self.datasource = ChildType(**childType)
        else:
            self.datasource = childType
        self.name = name
        self.parentId = parentId

    def __repr__(self):
        return f"DataSourceRootAsset({self.__dict__})"


class PropertyType(Enum):
    INT = auto()
    FLOAT = auto()
    STRING = auto()
    BOOLEAN = auto()
    JSON = auto()
    DURATION = auto()
    OBJECT = auto()
    OPTIONS = auto()
    URL = auto()
    URI = auto()
    PASSWORD = auto()
    EMAIL = auto()
    CRONEXPRESSION = auto()
    FILE = auto()
    ARRAY = auto()

    class SubPropertyType(Enum):
        STRING = auto()
        INT = auto()
        FLOAT = auto()
        BOOLEAN = auto()


class OptionTypes(Enum):

    CSV = auto()
    PARQUET = auto()
    ORC = auto()
    JSON = auto()
    AVRO = auto()
    CONFLUENT_AVRO = auto()

    PLAINTEXT = auto()
    SASL_PLAINTEXT = auto()
    SASL_SSL = auto()
    SSL = auto()
    BASIC_AUTH = auto()

    STANDALONE = auto()
    ORACLE_CLOUD_AUTONOMOUS_DB = auto()

    # Postgresql Environments
    ON_PREMISE = auto()
    AMAZON_RDS = auto()

    # Analysis Service Data Processor types
    HADOOP = auto()
    KUBERNETES = auto()
    DATABRICKS = auto()

    # Kafka Schema Naming Strategies
    TOPIC_NAME = auto()
    RECORD_NAME = auto()
    TOPIC_RECORD_NAME = auto()
    KEY = auto()
    VALUE = auto()

    # Torch Result Location Types
    HDFS = auto()
    S3 = auto()

@dataclass
class PropertyTemplate:
    key: str = None
    description: str = None
    displayLabel: str = None
    type: PropertyType = None
    options: List[OptionTypes] = None
    subType: PropertyType.SubPropertyType = None
    required: bool = None
    children: object = None
    visibility: str = None
    value: str = None
    replacementFor: str = None
    hidden: bool = None
    readOnly: bool = None
    configKey: str = None
    configValue: str = None
    multiSelect: bool = None


@dataclass
class PropertyTemplates:
    connections: Dict[str, List[PropertyTemplate]] = None
    assemblies: Dict[str, List[PropertyTemplate]] = None



@dataclass
class SourceModel:
    id = None,
    name = None

    def __init__(self,
                 id = None,
                 name=None):
        self.name = name
        self.id = id


@dataclass
class SourceType:
    id: str = None
    name: str = None
    sourceModel: SourceModel = None
    connectionTypeId: str = None
    miniProfiling: bool = None
    propertyTemplates: PropertyTemplates = None


@dataclass
class SecurityConfig:
    type = None
    config = None

    def __init__(self,
                 type = None,
                 config=None):
        self.type = type
        self.config = config


class DataSource:

    def __init__(self,
                 name: str = None,
                 isSecured: bool = None,
                 isVirtual: bool = None,
                 id: int = None,
                 createdAt: str = None,
                 updatedAt: str = None,
                 assemblyProperties = None,
                 conn: Connection = None,
                 connectionId: int = None,
                 crawler: Crawler = None,
                 currentSnapshot: str = None,
                 description: str = None,
                 sourceType: SourceType = None,
                 securityConfig: SecurityConfig = None,
                 schedule: str=None,
                 configuration=None,
                 client=None,
                 autoProfile: bool = None,
                 tenantId: str = None,
                 integrationId: str = None,
                 subIntegrationId: str = None,
                 isProtectedResource: bool = None,
                 createdBy: str = None,
                 **kwargs
                 ):
        """
            Description:
                datasource class.
        :param name: name of the datasource
        :param isSecured: is secured or not
        :param isVirtual: is virtual datasource or not
        :param id: id of the datasource
        :param createdAt: creation time of the datasource
        :param updatedAt: updated time of the datasource
        :param assemblyProperties: datasource properties
        :param conn: connection details for the ds
        :param connectionId: connection id of the datasource
        :param crawler: crawler details of the datasource
        :param currentSnapshot: current version of the datasource
        :param description: desc of the datasource
        :param sourceType: (DatasourceSourceModel) source type details
        :param securityConfig: security configuration for the given ds
        :param schedule: scheduled exp
        :param configuration: configurations
        """
        self.name = name
        self.isSecured = isSecured
        self.isVirtual = isVirtual
        self.id = id
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.assemblyProperties = assemblyProperties
        if isinstance(conn, dict):
            self.conn = Connection(**conn)
        else:
            self.conn = conn
        self.connectionId = connectionId
        if isinstance(crawler, dict):
            self.crawler = Crawler(**crawler)
        else:
            self.crawler = crawler
        self.currentSnapshot = currentSnapshot
        self.description = description
        if isinstance(securityConfig, dict):
            self.securityConfig = SecurityConfig(**securityConfig)
        else:
            self.securityConfig = securityConfig
        self.schedule = schedule
        self.configuration = configuration
        if isinstance(sourceType, dict):
            self.sourceType = SourceType(**sourceType)
        else:
            self.sourceType = sourceType
        self. autoProfile = autoProfile
        self.tenantId = tenantId
        self.integrationId = integrationId
        self.subIntegrationId = subIntegrationId
        self.isProtectedResource = isProtectedResource
        self.createdBy = createdBy

        self.client = client

    def __repr__(self):
        return f"DataSource({self.__dict__})"

    def update_datasource(self, create_datasource=CreateDataSource):
        return self.client.update_datasource(datasource_id=self.id, datasource=create_datasource)

    def get_root_assets(self):
        return self.client.get_root_asset(self.id)

    # convert asset to dict type
    def _convert_asset_to_dict(self, asset: CreateAsset):
        """
            Description:
                Convert CreateAsset class instance to dict type
            :param asset: CreateAsset class instance
            :return: dict form of CreateAsset class instance
        """
        payload = asset.__dict__
        metadata = []
        for md in asset.metadata:
            metadata.append(asdict(md))
        payload['metadata'] = metadata
        asset_payload = {'data': payload}
        return asset_payload

    # to create an asset
    def create_asset(self, name: str, uid: str, asset_type_id: int, parent_id: int = None, description: str = None,
                     snapshots=None, metadata: List[AssetMetadata] = None):
        """
        Description:
            used to create asset in datasource
        :return: asset created
        """
        if snapshots is None:
            snapshots = [self.currentSnapshot]
        asset = CreateAsset(
            name=name,
            description=description,
            assemblyId=self.id,
            uid=uid,
            assetTypeId=asset_type_id,
            sourceTypeId=self.sourceType.id,
            isCustom=False,
            parentId=parent_id,
            currentSnapshot=self.currentSnapshot,
            snapshots=snapshots,
            metadata=metadata
        )
        payload = self._convert_asset_to_dict(asset)
        return self.client.create_asset(payload)

    # convert snapshot data to dict type
    def _convert_snapshot_data_to_dict(self, snapshot_data: SnapshotData):
        """
            Description:
                Convert SnapshotData class instance to dict type
            :param snapshotData: SnapshotData class instance
            :return: dict form of SnapshotData class instance
        """
        payload = snapshot_data.__dict__
        payload['associatedItemType'] = snapshot_data.associatedItemType.name
        snaoshot_payload = {'data': payload}
        return snaoshot_payload

    # initialise new version of snapshot for a datasource
    def initialise_snapshot(self, uid: str):
        """
        Description:
            Used to initialise new version of snapshot for a datasource
        :param uid: uid of new snapshot version
        :return: created snapshotData class instance
        """
        if uid is None:
            raise TorchSdkException('uid for new snapshot version is required')
        snapshot_data = SnapshotData(
            uuid=uid,
            associatedItemType=AssociatedItemType.ASSEMBLY,
            associatedItemId=self.id
        )

        payload = self._convert_snapshot_data_to_dict(snapshot_data)
        snapshot = self.client.initialise_snapshot(payload)
        self.currentSnapshot = snapshot.uuid
        return snapshot

    # get current version of datasource
    def get_current_snapshot(self):
        """
        Description:
            If you want to get current version of a datasource
        :return: SnapshotData class instance of datasource
        """
        snapshot = self.client.get_current_snapshot(self.id)
        if self.currentSnapshot is None:
            self.currentSnapshot = snapshot.uuid
        return snapshot

    def get_asset(self, identifier):
        """"
            Description:
                Find an asset of the datasource
            :param identifier: uid or id of the asset
        """
        return self.client.get_asset(identifier)

    def delete_asset(self, id: int = None):
        if id is None:
            raise TorchSdkException('Id of the asset is required to delete an asset')
        return self.client.delete_asset(id)

    def list_all_snapshots(self):
        return self.client.list_datasource_snapshots(self.id)

    def start_crawler(self):
        return self.client.start_crawler(self.name)

    def get_crawler_status(self):
        return self.client.get_crawler_status(self.name)

    def restart_crawler(self):
        return self.client.restart_crawler(self.name)

    def remove_crawler(self):
        return self.client.remove_crawler(self.name)

    def get_auto_profile_configuration(self):
        return self.client.get_auto_profile_configuration(self.id)

    def remove_auto_profile_configuration(self):
        return self.client.remove_auto_profile_configuration(self.id)


class CrawlerStatus:
    def __init__(self, assemblyName, isSuccess=None, status=None):
        self.assemblyName = assemblyName
        if status is not None:
            self.status = status
        if isSuccess is not None:
            self.isSuccess = isSuccess

    def __repr__(self):
        return f"CrawlerStatus({self.__dict__})"
