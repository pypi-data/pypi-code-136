import logging
from itertools import chain

import numpy as np
from graphdb import Node, Relationship
from pandas import DataFrame, concat

from ingestor.common import (
    USER_LABEL,
    CUSTOMER_ID,
    EDGE,
    CONTENT_ID,
    USER_CONTENT_RELATIONSHIP_LABEL,
    CONTENT_LABEL,
    VIDEO_ID1,
    STATUS,
    LABEL,
    PROPERTIES,
    PAY_TV_CONTENT,
    IS_PAY_TV,
    NO_PAY_TV_CONTENT,
    RELATIONSHIP,
    VIEW_COUNT,
    VIEW_HISTORY,
    HAS_PAYTV_PROVIDER,
    ID,
)
from ingestor.repository.graph_db_connection import ANGraphDb
from ingestor.utils import custom_exception


class ViewedUtils:
    @staticmethod
    @custom_exception()
    def fetch_edge_id(data: DataFrame):
        """
        Function to fetch edge id's from graph
        :param data: Dataframe object pandas
        :return: Dataframe object pandas
        """
        graph = ANGraphDb.new_connection_config().graph
        tmp = []
        for index in range(len(data)):
            try:
                query = f"""g.V().has('{USER_LABEL}', '{CUSTOMER_ID}', '{data.loc[index, CUSTOMER_ID]}').
                                outE("{USER_CONTENT_RELATIONSHIP_LABEL}").project('{EDGE}','{CUSTOMER_ID}','{CONTENT_ID}').
                                by(id).
                                by(outV().values('{CUSTOMER_ID}')).
                                by(inV().values('{CONTENT_ID}'))"""
                response = graph.custom_query(
                    query=query,
                    payload={
                        USER_LABEL: USER_LABEL,
                        CUSTOMER_ID: CUSTOMER_ID,
                        USER_CONTENT_RELATIONSHIP_LABEL: USER_CONTENT_RELATIONSHIP_LABEL,
                        CONTENT_ID: CONTENT_ID,
                        EDGE: EDGE,
                    },
                )
                tmp.append(response[0])
            except Exception as e:
                logging.error(f"Error while fetching edge id from graphdb, Error: {e}")
        graph.connection.close()
        df = DataFrame(list(chain.from_iterable(tmp)))
        data = data.merge(df, on=[CUSTOMER_ID, CONTENT_ID], how="left")
        return data

    @staticmethod
    @custom_exception()
    def fetch_status(data: DataFrame):
        """
        Function to fetch content status from graphdb
        :param data: Dataframe object pandas
        :return: Dataframe object pandas
        """
        graph = ANGraphDb.new_connection_config().graph
        tmp = []
        for index in range(len(data)):
            print("Fetching content status for record ", index + 1, " of ", len(data))
            try:
                query = f"""g.V().
                 has('{data.loc[index, CONTENT_LABEL]}', '{CONTENT_ID}', {int(data.loc[index, VIDEO_ID1])}).
                 project('{CONTENT_ID}', '{STATUS}').by(values('{CONTENT_ID}')).by(values('{STATUS}'))"""
                response = graph.custom_query(
                    query=query,
                    payload={
                        CONTENT_ID: CONTENT_ID,
                        STATUS: STATUS,
                        CONTENT_LABEL: CONTENT_LABEL,
                    },
                )
                if len(response) > 0:
                    tmp.append(response[0][0])
            except Exception as e:
                logging.error(f"Error while fetching record from graphdb, Error: {e}")
        graph.connection.close()
        tmp_df = DataFrame(tmp)
        return tmp_df

    @staticmethod
    @custom_exception()
    def dump_relations(
        data: DataFrame,
    ):
        """
        Dump newly created VIEWED relations in graphdb
        :param data: Created_df of ubd data
        :return: None
        """
        graph = ANGraphDb.new_connection_config().graph
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
                    RELATIONSHIP: USER_CONTENT_RELATIONSHIP_LABEL,
                    PROPERTIES: {
                        VIEW_COUNT: int(data.loc[index, VIEW_COUNT]),
                        VIEW_HISTORY: str(data.loc[index, VIEW_HISTORY]),
                    },
                }
            )
            try:
                graph.create_multi_relationship_without_upsert(
                    node_from=user_node, node_to=content_node, rel=rel
                )
            except Exception as e:
                logging.error(
                    f"Error while creating VIEWED relation in graphdb, Error: {e}"
                )
        graph.connection.close()

    @staticmethod
    @custom_exception()
    def get_is_paytv(data: DataFrame) -> DataFrame:
        """
        This function updates the ubd dataframe
        with is_paytv column containing Yes or
        No according to user's relation with
        paytv_provider static network
        :param data: Dataframe object pandas
        :return: Updated User Behaviour Dataframe
        object pandas
        """
        user_list = data[CUSTOMER_ID].unique().tolist()
        users = DataFrame()
        graph = ANGraphDb.new_connection_config().graph
        for user in user_list:
            try:
                response = graph.custom_query(
                    query=f"""g.V().has('{USER_LABEL}','{CUSTOMER_ID}', '{user}').
                            outE('{HAS_PAYTV_PROVIDER}').project('{CUSTOMER_ID}','{IS_PAY_TV}').
                            by(outV().values('{CUSTOMER_ID}')).
                            by(outV().values('{IS_PAY_TV}'))""",
                    payload={
                        USER_LABEL: USER_LABEL,
                        CUSTOMER_ID: CUSTOMER_ID,
                        IS_PAY_TV: IS_PAY_TV,
                        HAS_PAYTV_PROVIDER: HAS_PAYTV_PROVIDER,
                    },
                )
                if len(response) > 0:
                    row_to_add = response[0][0]
                    users = concat([users, DataFrame([row_to_add])], ignore_index=True)
            except Exception as e:
                logging.error(
                    f"Error while fetching paytv users from graph, Error: {e}"
                )
        data = data.merge(users, on=CUSTOMER_ID, how="left")
        data[IS_PAY_TV] = data[IS_PAY_TV].fillna(False)
        data[CONTENT_LABEL] = np.where(
            (data[IS_PAY_TV] == True), PAY_TV_CONTENT, NO_PAY_TV_CONTENT
        )
        return data

    @staticmethod
    @custom_exception()
    def update_existing_relations(
        data: DataFrame,
    ):
        """
        Updates the existing set of relations with
        new respective property values
        :param data: dataframe object pandas
        :return: None, Updates the relationships
        in graphDB
        """
        record_count = len(data)
        graph = ANGraphDb.new_connection_config().graph
        for index in range(record_count):
            print(
                "Updating existing relationship record ",
                index + 1,
                " of ",
                record_count,
            )
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
            try:
                graph.replace_relationship_property(
                    rel=Relationship(
                        **{
                            RELATIONSHIP: USER_CONTENT_RELATIONSHIP_LABEL,
                            ID: data.loc[index, EDGE],
                        }
                    ),
                    update_query={
                        VIEW_COUNT: int(data.loc[index, VIEW_COUNT]),
                        VIEW_HISTORY: str(data.loc[index, VIEW_HISTORY]),
                    },
                    node_from=user_node,
                    node_to=content_node,
                )
            except Exception as e:
                logging.error(
                    f"Error while updating relation {USER_CONTENT_RELATIONSHIP_LABEL} on graph, Error: {e}"
                )
        graph.connection.close()

    @staticmethod
    @custom_exception()
    def get_viewed_relation_count(
        customer_id: str, content_key: str, content_id: int, graph=None
    ):
        """
        Use custom query to retrieve information regarding
        user-content VIEWED relationship for the considered
        customer_id and content_id
        :param graph: graph connection object
        :param customer_id: string customer_id
        :param content_key: paytv status of content
        :param content_id: string content_id
        :return: list of values
        """
        try:
            response = graph.custom_query(
                query=f"""g.V().hasLabel('{USER_LABEL}')
                .has('{CUSTOMER_ID}','{customer_id}').outE()
                .hasLabel('{USER_CONTENT_RELATIONSHIP_LABEL}')
                .inV().hasLabel('{content_key}')
                .has('{CONTENT_ID}',{content_id})
                .path().by(elementMap())""",
                payload={
                    USER_LABEL: USER_LABEL,
                    CUSTOMER_ID: CUSTOMER_ID,
                    USER_CONTENT_RELATIONSHIP_LABEL: USER_CONTENT_RELATIONSHIP_LABEL,
                    content_key: content_key,
                    CONTENT_ID: CONTENT_ID,
                },
            )
        except Exception as e:
            logging.error(f"Error while fetching record from graphdb, Error: {e}")
        if len(response) == 0:
            return 0, []
        try:
            view_history = list(eval(response[0][0][1][VIEW_HISTORY]))
        except KeyError:
            node_from = Node.parse_obj(
                {LABEL: USER_LABEL, PROPERTIES: {CUSTOMER_ID: str(customer_id)}}
            )
            node_to = Node.parse_obj(
                {LABEL: content_key, PROPERTIES: {CONTENT_ID: int(content_id)}}
            )
            relationship = Relationship.parse_obj({RELATIONSHIP: "VIEWED"})
            try:
                graph.delete_relationship(
                    node_from=node_from, node_to=node_to, rel=relationship
                )
            except StopIteration:
                logging.warning(
                    f"No VIEWED relation found on graph between {node_from} to {node_to}"
                )
            except Exception as e:
                logging.error(
                    f"Unable to drop VIEWED relation between {node_from} to {node_to}, Error: {e}"
                )
            finally:
                return 0, []
        return response[0][0][1][VIEW_COUNT], view_history
