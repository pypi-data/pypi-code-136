import psycopg2 as pg

from prefect import Task
from prefect.utilities.tasks import defaults_from_attrs
from urllib.parse import urlparse

from typing import *

__all__ = ["PostgresExecute"]


class PostgresExecute(Task):
    """
    Task for executing a query against a Postgres database.

    Args:
        - db_name (str): name of Postgres database
        - user (str): user name used to authenticate
        - host (str): database host address
        - port (int, optional): port used to connect to Postgres database, defaults to 5432 if
            not provided
        - query (str, optional): query to execute against database
        - data (tuple, optional): values to use in query, must be specified using placeholder
            is query string
        - commit (bool, optional): set to True to commit transaction, defaults to false
        - **kwargs (dict, optional): additional keyword arguments to pass to the
            Task constructor
    """

    def __init__(
        self,
        db_name: Optional[str] = None,
        user: Optional[str] = None,
        host: Optional[str] = None,
        port: int = 5432,
        query: Optional[str] = None,
        data: Optional[Any] = None,
        commit: bool = False,
        **kwargs
    ):
        self.db_name = db_name
        self.user = user
        self.host = host
        self.port = port
        self.query = query
        self.data = data
        self.commit = commit
        super().__init__(**kwargs)

    @defaults_from_attrs("db_name", "user", "host", "port", "query", "data", "commit")
    def run(
        self,
        db_name: Optional[str],
        user: Optional[str],
        host: Optional[str],
        port: Optional[int],
        query: Optional[str],
        data: Optional[Any],
        commit: bool,
        password: Optional[str],
        connection_string: Optional[str],
    ):
        """
        Task run method. Executes a query against Postgres database.

        Args:
            - query (str, optional): query to execute against database
            - data (tuple, optional): values to use in query, must be specified using
                placeholder is query string
            - commit (bool, optional): set to True to commit transaction, defaults to false
            - password (str): password used to authenticate; should be provided from a `Secret` task

        Returns:
            - None

        Raises:
            - ValueError: if query parameter is None or a blank string
            - DatabaseError: if exception occurs when executing the query
        """
        if not query:
            raise ValueError("A query string must be provided")

        if connection_string:
            if host:
                raise ValueError(
                    "Connection string and hostname cannot be set at the same time"
                )
            parsed = urlparse(connection_string)

            db_name = parsed.path[1:] or db_name
            user = parsed.username or user
            password = parsed.password or password
            host = parsed.hostname
            port = parsed.port or port

        if not isinstance(data, list) or isinstance(data, tuple):
            data = (data,)

        # connect to database, open cursor
        # allow psycopg2 to pass through any exceptions raised
        conn = pg.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port,
        )

        # try to execute query
        # context manager automatically rolls back failed transactions
        try:
            with conn, conn.cursor() as cursor:
                executed = cursor.execute(query=query, vars=data)
                if commit:
                    conn.commit()
                else:
                    conn.rollback()

            return executed

        # ensure connection is closed
        finally:
            conn.close()
