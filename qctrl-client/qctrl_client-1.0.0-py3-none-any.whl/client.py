# Copyright 2022 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.

from typing import (
    Any,
    Callable,
    Dict,
    Optional,
    Type,
    Union,
)

import gql
from gql.transport import Transport
from graphql import (
    DocumentNode,
    print_schema,
)
from qctrlcommons.exceptions import QctrlGqlException

from .auth import BaseAuthHandler
from .transports import RequestsTransport


def _default_handle_document_error(data: Dict[str, Any]):
    """Handles document level errors.

    Parameters
    ----------
    data : dict
        The document result returned from gql.Client.

    Raises
    ------
    QctrlGqlException
        If there are any errors.
    """
    raise QctrlGqlException(data["errors"])


def _default_handle_query_error(key: str, data: Dict[str, Any]):
    """Handles query level errors.

    Parameters
    ----------
    key : str
        The query name or alias key.
    data : dict
        The query result returned from gql.Client.

    Raises
    ------
    QctrlGqlException
        If there are any errors.
    """
    raise QctrlGqlException(data["errors"])


def _prepare_kwargs(
    user_options: Dict[str, Any], **mandatory_kwargs: Any
) -> Dict[str, Any]:
    """Combines mandatory keyword arguments with options
    provided by the user.

    Parameters
    ----------
    user_options : Dict[str,Any]
        Keyword arguments requested by the user.
    mandatory_kwargs : Any
        Keyword arguments that must be included in the
        result.

    Returns
    -------
    Dict[str,Any]

    Raises
    ------
    RuntimeError
        If any keyword arguments requested by the user
        conflict with any mandatory keyword arguments.
    """
    kwargs = mandatory_kwargs.copy()

    for name, value in user_options.items():
        if name in kwargs:
            raise RuntimeError(f"Unable to specify keyword argument: {name}")

        kwargs[name] = value

    return kwargs


class GraphQLClient:  # pylint: disable=too-few-public-methods
    """
    GraphQL Client.
    """

    def __init__(
        self,
        url: str,
        auth: Optional[BaseAuthHandler] = None,
        headers: Optional[Dict[str, Any]] = None,
        schema: Optional[str] = None,
        transport_cls: Optional[Type[Transport]] = RequestsTransport,
        transport_options: Optional[Dict[str, Any]] = None,
        client_options: Optional[Dict[str, Any]] = None,
        handle_document_error: Callable = _default_handle_document_error,
        handle_query_error: Callable = _default_handle_query_error,
    ):
        """
        Parameters
        ----------
        url : str
            The endpoint for the graphql request.
        headers : dict
            The dictionary of http headers.
        auth : BaseAuthHandler, optional
            An instance of an authentication object. (Default value = None)
        schema : list of str, Optional
            The string version of the GQL schema. (Default value = None)
        transport_cls : Optional[Type[Transport]]
            The transport class to be used by the gql.Client instance.
        transport_options : dict
            Custom arguments to the used transport instance. (Default value = None)
        client_options : dict
            Custom arguments to the created gql.Client instance. (Default value = None)
        handle_document_error : Callable
            Hook function called if a document level error is found. The callable
            should accept a single argument which is the document result. Default
            behaviour is to raise a QctrlGqlException.
        handle_query_error : Callable
            Hook function called if any query level errors are found. The callable
            should accept two arguments - the query key and the query result. Default
            behaviour is to raise a QctrlGqlException.
        """

        self._auth = auth
        self._handle_document_error = handle_document_error
        self._handle_query_error = handle_query_error

        transport_options = transport_options or {}
        transport_kwargs = _prepare_kwargs(
            transport_options,
            url=url,
            headers=headers or {},
            auth=auth,
        )

        transport = transport_cls(**transport_kwargs)

        client_options = client_options or {}
        client_kwargs = _prepare_kwargs(
            client_options,
            schema=schema,
            transport=transport,
            fetch_schema_from_transport=not schema,
        )

        self._client = gql.Client(**client_kwargs)

    def get_access_token(self) -> str:
        """
        Returns an access token.
        """
        if self._auth is None:
            raise RuntimeError("Client is not authenticated.")

        return self._auth.access_token

    def execute(
        self, query: Union[DocumentNode, str], variable_values: Optional[Dict] = None
    ):
        """
        Executes a GraphQL query/mutation.
        """
        if variable_values is None:
            variable_values = {}

        if isinstance(query, DocumentNode):
            document = query
        else:
            document = gql.gql(query)

        result = self._client.execute(document, variable_values=variable_values)
        self._check_errors(document, result)
        return result

    def _check_errors(
        self,
        document: DocumentNode,
        result: Dict,
    ):
        """Checks for any errors, including query-level errors, returned
         from the query request.

        Parameters
        ----------
        document: DocumentNode
            The GraphQL document which was executed.
        result: dict
            The result of the query execution, as returned from
            gql.Client.execute
        """

        # check document level errors
        if result.get("errors"):
            self._handle_document_error(result)

        # search result for query errors
        for definition_node in document.definitions:
            for node in definition_node.selection_set.selections:
                if node.alias:
                    query_key = node.alias.value
                else:
                    query_key = node.name.value

                if result.get(query_key, {}).get("errors"):
                    self._handle_query_error(query_key, result[query_key])

    def get_schema(self) -> str:
        """
        Get Schema from gql.Client.
        """
        with self._client as session:
            session.fetch_schema()

        if not self._client.schema:
            raise ValueError("Schema cannot be empty")

        return print_schema(self._client.schema)
