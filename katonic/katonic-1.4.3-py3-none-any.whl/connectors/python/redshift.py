#!/usr/bin/env python
#
# Copyright (c) 2022 Katonic Pty Ltd. All rights reserved.
#
from pathlib import Path
from time import gmtime
from time import strftime
from typing import Optional

import redshift_connector
from colorama import Fore
from colorama import Style


class RedshiftConnector:
    """Provides Redshift Connector to extracts data from Amazon Redshift."""

    _conn: Optional[redshift_connector.connect] = None

    def __init__(
        self,
        host: str,
        database: str,
        user: str,
        password: str,
        table_name: str,
        query: str,
        port: int = 5439,
        output: str = "local",
        file_name: Optional[str] = "",
        file_path: Optional[str] = "",
    ):
        """
        Connect with redshift database, fetch data from redshift and store into your output path.

        Args:
            host (str): database host address for eg: examplecluster.abc123xyz789.us-west-1.redshift.amazonaws.com
            database (str): database name
            user (str): redshift user name used to authenticate
            password (str): password used to authenticate
            table_name (str): table name from where you want retrieve data
            query (str): custom query to retrieve data
            port (int): connection port number (default: 5439 if not provided)
            output (Optional[str]): output type, it can be `local` or `katonic` (default: `local` if not provided)
            file_name (Optional[str]): output file name on which retrieved data will be stored
            file_path (Optional[str]): output path where you want to store data

        Returns:
            None

        """
        self._host = host
        self._port = port
        self._db_name = database
        self._user = user
        self._password = password
        self._table_name = table_name
        self._custom_query = query
        self._output = output
        self._file_name = file_name
        self._file_path = file_path

        if self._output.lower() == "local":
            Path(self._file_path).mkdir(
                parents=True, exist_ok=True
            ) if self._file_path else ""
            self._dst_path = (
                Path(self._file_path).absolute()
                if self._file_path
                else Path().absolute()
            )
        elif self._output.lower() == "katonic":
            if self._file_path:
                Path(f"/kfs_private/{self._file_path}").mkdir(
                    parents=True, exist_ok=True
                )
                self._dst_path = Path(f"/kfs_private/{self._file_path}").absolute()
            else:
                self._dst_path = Path("/kfs_private/").absolute()
        else:
            raise ValueError(
                f"invalid literal for variable output: '{self._output}', it must be one from 'local' or 'katonic'."
            )

    def _get_redshift_reg_conn(self):
        """Creates a connection to the amazon redshift database."""

        if not self._conn:
            self._conn = redshift_connector.connect(
                host=self._host,
                port=self._port,
                database=self._db_name,
                user=self._user,
                password=self._password,
            )

        return self._conn

    def get_data(self) -> None:
        """
        This function will extracts data from amazon redshift database.

        Returns:
            None

        Raises:
            ValueError: if output type provided other than `local` or `katonic`.
        """
        fname = f"redshift_{self._db_name}_{self._file_name or self._table_name}_{strftime('%Y_%m_%d_%H_%M_%S', gmtime())}.csv"
        self._dstn_path = f"{self._dst_path}/{fname}"

        try:
            _conn = self._get_redshift_reg_conn()
            _cursor = _conn.cursor()
            print("Connection to Amazon redshift stablished Successfully.")
        except redshift_connector.OperationalError as e:
            print(f"Unable to connect!\n{e}")
        else:
            try:
                _cursor.execute(self._custom_query)
                _data = _cursor.fetch_dataframe()
                _data.to_csv(self._dstn_path, index=False)
                print(
                    f"File saved to your {Style.BRIGHT + Fore.GREEN}'{self._output}'{Style.RESET_ALL}"
                    f"file system with name {Style.BRIGHT + Fore.GREEN}'{fname}'{Style.RESET_ALL} Successfully."
                )

            except Exception as e:
                raise ValueError(
                    f"Failed to save data to your {Style.BRIGHT + Fore.RED}'{self._output}'{Style.RESET_ALL} file system path."
                ) from e

            else:
                _conn.close()
                _cursor.close()
