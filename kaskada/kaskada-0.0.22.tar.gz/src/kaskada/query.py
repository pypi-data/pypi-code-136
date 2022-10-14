"""
Copyright (C) 2022 Kaskada Inc. All rights reserved.

This package cannot be used, copied or distributed without the express
written permission of Kaskada Inc.

For licensing inquiries, please contact us at info@kaskada.com.
"""

from kaskada.client import Client
import kaskada
import kaskada.compute
import kaskada.api.v1alpha.query_pb2 as query_pb
import kaskada.api.v1alpha.compute_pb2 as pb

import grpc


class QueryResource(object):
    CURRENT_DATA_TOKEN = ""

    def __init__(self, query: query_pb.Query):
        self.query = query

    def to_query_request(self):
        return {
            "query_id": self.query.query_id,
            "expression": self.query.expression,
            "data_token_id": self.query.data_token_id,
            "changed_since_time": self.query.changed_since_time,
            "final_result_time": self.query.final_result_time,
            "limits": self.query.limits,
            "parquet": self.query.parquet,
            "result_behavior": self.query.result_behavior,
        }

    def run(self, data_token=None, dry_run=False, experimental_features=False):
        try:
            query_options = {
                "dry_run": dry_run,
                "experimental_features": experimental_features,
                "stream_metrics": False,
            }
            query_request = self.to_query_request()
            in_ipython = kaskada.formatters.in_ipython()
            if in_ipython:
                query_options["stream_metrics"] = True
            if data_token is not None:
                query_request["data_token_id"] = {"value": data_token}
            request_args = {
                "query_request": query_request,
                "query_options": query_options,
            }
            request = pb.StreamQueryV2Request(**request_args)
            return kaskada.compute.executeQuery(request, kaskada.KASKADA_DEFAULT_CLIENT)
        except grpc.RpcError as e:
            kaskada.handleGrpcError(e)
        except Exception as e:
            kaskada.handleException(e)

    def run_with_latest(self, dry_run=False, experimental_features=False):
        return self.run(
            data_token=QueryResource.CURRENT_DATA_TOKEN,
            dry_run=dry_run,
            experimental_features=experimental_features,
        )


def get_query(query_id: str, client: Client = None):
    """
    Gets a query by query ID
    Args:
        query_id (str): The target query ID
        client (Client, optional): The Kaskada Client. Defaults to kaskada.KASKADA_DEFAULT_CLIENT.

    Raises:
        NotImplementedError
    """
    if client is None:
        client = kaskada.KASKADA_DEFAULT_CLIENT

    try:
        kaskada.validate_client(client)
        req = query_pb.GetQueryRequest(
            query_id=query_id,
        )
        resp = client.queryStub.GetQuery(req, metadata=client.get_metadata())
        return QueryResource(resp.query)
    except grpc.RpcError as e:
        kaskada.handleGrpcError(e)
    except Exception as e:
        kaskada.handleException(e)


def list_queries(search: str = None, client: Client = None):
    """
    Lists all queries the user has previously performed

    Args:
        search (str): The search parameter to filter queries by. Defaults to None.
        client (Client, optional): The Kaskada Client. Defaults to kaskada.KASKADA_DEFAULT_CLIENT.

    Raises:
        NotImplementedError
    """
    if client is None:
        client = kaskada.KASKADA_DEFAULT_CLIENT

    try:
        kaskada.validate_client(client)
        req = query_pb.ListQueriesRequest(
            search=search,
        )
        return client.queryStub.ListQueries(req, metadata=client.get_metadata())

    except grpc.RpcError as e:
        kaskada.handleGrpcError(e)
    except Exception as e:
        kaskada.handleException(e)
