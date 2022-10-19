import logging
from ast import literal_eval
from datetime import datetime
from math import ceil
from operator import itemgetter

from graphdb import Relationship, Node
from pandas import DataFrame, concat

from ingestor.common.constants import (
    CUSTOMER_ID,
    VIEW_COUNT,
    VIEW_HISTORY,
    CREATED_ON,
    DURATION,
    RELATIONSHIP,
    PROPERTIES,
    CONTENT_ID,
    CONTENT_LABEL,
    LABEL,
    USER_LABEL,
)
from ingestor.common.read_write_from_s3 import ConnectS3
from ingestor.repository.graph_db_connection import ANGraphDb
from ingestor.user_rating.config import (
    MILLISECONDS_IN_ONE_MINUTE,
    VISIONPLUS_DEV,
    VIEWED_DATA_PATH,
    S3_RESOURCE,
    HAS_RATING,
)
from ingestor.user_rating.constants import (
    RECENT_DURATION,
    IMPLICIT_RATING_SHIFTED,
    MAX_RATING,
    IMPLICIT_RATING_VALUE,
    RECENT_DATE,
    CONTENT_STATUS,
    ACTIVE,
    IMPLICIT_RATING,
)


class RatingUtils:
    @staticmethod
    def get_queried_log_data_for_user() -> DataFrame:
        s3_cls = ConnectS3()

        viewed = s3_cls.read_compress_pickles_from_S3(
            bucket_name=VISIONPLUS_DEV,
            object_name=VIEWED_DATA_PATH,
            resource=S3_RESOURCE,
        )
        return viewed[viewed[CONTENT_STATUS] == ACTIVE]

    @staticmethod
    def get_recent_viewed_date(data) -> DataFrame:
        recent_date_list = []
        for idx, val in data.iterrows():
            recent_date_dict = {}
            history_data = val[VIEW_HISTORY]
            list_history_data = literal_eval(str(history_data))
            list_history_data = sorted(
                list_history_data, key=itemgetter(CREATED_ON), reverse=True
            )
            recent_date = list_history_data[0][CREATED_ON]
            recent_date = datetime.fromisoformat(str(recent_date)).date()
            recent_date_dict[RECENT_DATE] = recent_date
            recent_date_list.append(recent_date_dict)
        recent_date_df = DataFrame(recent_date_list)
        df = concat([data, recent_date_df], axis=1)
        return df

    @staticmethod
    def get_recent_duration(data) -> DataFrame:
        recent_duration_list = []
        for idx, val in data.iterrows():
            recent_duration_dict = {}
            history_data = val[VIEW_HISTORY]
            list_history_data = literal_eval(str(history_data))
            list_history_data = sorted(
                list_history_data, key=itemgetter(CREATED_ON), reverse=True
            )
            recent_duration = list_history_data[0][DURATION]
            recent_duration_dict[RECENT_DURATION] = recent_duration
            recent_duration_list.append(recent_duration_dict)
        recent_duration_df = DataFrame(recent_duration_list)
        df = concat([data, recent_duration_df], axis=1)
        return df

    @staticmethod
    def get_number_of_users(data) -> int:
        number_of_users = len(set(data[CUSTOMER_ID]))
        return number_of_users

    @staticmethod
    def milliseconds_to_minutes(data) -> DataFrame:
        data[RECENT_DURATION] = data[RECENT_DURATION] / MILLISECONDS_IN_ONE_MINUTE
        return data

    @staticmethod
    def get_maximum_of_two_implicit_ratings(data) -> DataFrame:
        data[IMPLICIT_RATING_SHIFTED] = data[IMPLICIT_RATING_VALUE].shift()
        data[MAX_RATING] = data[[IMPLICIT_RATING_VALUE, IMPLICIT_RATING_SHIFTED]].max(
            axis=1
        )
        data.drop(columns=[IMPLICIT_RATING_SHIFTED], inplace=True)

        return data

    @staticmethod
    def round_partial(value, resolution):
        return round(value / resolution) * resolution

    @staticmethod
    def cap_ubd_data(data) -> DataFrame:
        quantile1, quantile3 = data[VIEW_COUNT].quantile([0.25, 0.75])
        IQR = quantile3 - quantile1
        upper_view_threshold = ceil(quantile3 + 1.5 * IQR)
        data.loc[
            data[VIEW_COUNT] > upper_view_threshold, VIEW_COUNT
        ] = upper_view_threshold
        return data

    @staticmethod
    def drop_relations(data: DataFrame):
        """
        Drop existing Has_Rating relations
        :param data: Dataframe object pandas
        :return: None, updates graphdb
        """
        graph = ANGraphDb.new_connection_config().graph
        print("Starting dropping HAS_RATING relationships".center(100, "*"))
        for index in range(len(data)):
            node_from = Node.parse_obj(
                {
                    LABEL: USER_LABEL,
                    PROPERTIES: {CUSTOMER_ID: str(data.loc[index, CUSTOMER_ID])},
                }
            )
            node_to = Node.parse_obj(
                {
                    LABEL: data.loc[index, CONTENT_LABEL],
                    PROPERTIES: {CONTENT_ID: int(data.loc[index, CONTENT_ID])},
                }
            )
            relationship = Relationship.parse_obj({RELATIONSHIP: HAS_RATING})
            try:
                graph.delete_relationship(
                    node_from=node_from, node_to=node_to, rel=relationship
                )
            except StopIteration:
                logging.warning(
                    f"No HAS_RATING relation found on graph between {node_from} to {node_to}"
                )
            except Exception as e:
                logging.error(
                    f"Unable to drop HAS_RATING relation between {node_from} to {node_to}, Error: {e}"
                )
            finally:
                continue
        graph.connection.close()

    @staticmethod
    def dump_relation(data: DataFrame):
        """
        Plot has rating relation in graphdb
        :param data: Dataframe object pandas
        :return: None, updates graphdb
        """
        graph = ANGraphDb.new_connection_config().graph
        print("Starting dumping HAS_RATING relationships".center(100, "*"))
        for index in range(len(data)):
            user_node = Node.parse_obj(
                {
                    LABEL: USER_LABEL,
                    PROPERTIES: {CUSTOMER_ID: str(data.loc[index, CUSTOMER_ID])},
                }
            )
            content_node = Node.parse_obj(
                {
                    LABEL: str(data.loc[index, CONTENT_LABEL]),
                    PROPERTIES: {CONTENT_ID: int(data.loc[index, CONTENT_ID])},
                }
            )
            rel = Relationship.parse_obj(
                {
                    RELATIONSHIP: HAS_RATING,
                    PROPERTIES: {IMPLICIT_RATING: data.loc[index, IMPLICIT_RATING]},
                }
            )
            try:
                graph.create_multi_relationship_without_upsert(
                    node_from=user_node, node_to=content_node, rel=rel
                )
            except Exception as e:
                logging.error(
                    f"Error while creating HAS_RATING relation {user_node} to {content_node} in graphdb, Error: {e}"
                )
        graph.connection.close()
