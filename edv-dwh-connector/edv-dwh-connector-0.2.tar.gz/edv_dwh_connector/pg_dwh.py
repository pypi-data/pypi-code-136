"""
This module implement a PostgreSQL data warehouse.
.. since: 0.1
"""

# -*- coding: utf-8 -*-
# Copyright (c) 2022 Endeavour Mining
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to read
# the Software only. Permissions is hereby NOT GRANTED to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pygrametl import ConnectionWrapper  # type: ignore
import psycopg2  # type: ignore
from edv_dwh_connector.dwh import Dwh


# pylint: disable=too-many-arguments,too-few-public-methods
class PgDwh(Dwh):
    """
    PostgreSQL data warehouse.
    .. since: 0.1
    """

    def __init__(
        self, name: str, host: str, user: str, password: str, port: int
    ) -> None:
        """
        Ctor.
        :param name: Database name
        :param host: Hostname or IP address
        :param user: Username
        :param password: Password
        :param port: Port
        """

        self.__connection_string = \
            f"host={host} \
            dbname={name} \
            user={user} \
            password={password} \
            port={port}"

    def connection(self) -> ConnectionWrapper:
        return ConnectionWrapper(
            connection=psycopg2.connect(self.__connection_string)
        )
