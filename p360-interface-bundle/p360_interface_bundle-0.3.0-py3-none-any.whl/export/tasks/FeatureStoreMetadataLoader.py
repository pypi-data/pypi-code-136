import json
from logging import Logger
from featurestorebundle.entity.EntityGetter import EntityGetter
from featurestorebundle.feature.FeatureStore import FeatureStore
from p360_interface_bundle.export.ExportTaskInterface import ExportTaskInterface
from daipecore.widgets.Widgets import Widgets


class FeatureStoreMetadataLoader(ExportTaskInterface):
    def __init__(self, feature_store: FeatureStore, entity_getter: EntityGetter, logger: Logger, widgets: Widgets):
        self.__feature_store = feature_store
        self.__entity_getter = entity_getter
        self.__logger = logger
        self.__widgets = widgets

    def run(self):
        self.__logger.info("Loading Feature Store metadata")

        attributes = json.loads(self.__widgets.get_value("config"))

        entity = self.__entity_getter.get()

        feature_store_metadata = self.__feature_store.get_metadata(entity.name, features=attributes["attributes"], exclude_tags=["private"])

        feature_store_metadata.createOrReplaceTempView("feature_store_metadata")

        self.__logger.info("Loading Feature Store metadata done")
