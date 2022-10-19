"""
This module implements PI tag API coming from PostgreSQL.
.. since: 0.2
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

import math
from datetime import datetime
from sqlalchemy import text  # type: ignore
from edv_dwh_connector.pi.pi_measure import PImeasure, PImeasures
from edv_dwh_connector.pi.pi_tag import PITag
from edv_dwh_connector.dwh import Dwh
from edv_dwh_connector.exceptions import ValueNotFoundError,\
    ValueAlreadyExistsError


class PgPImeasure(PImeasure):
    """
    PI measure from PostgreSQL.
    .. since: 0.2
    """

    def __init__(self, tag: PITag, date: datetime, dwh: Dwh) -> None:
        """
        Ctor.
        :param tag: PI tag
        :param date: Datetime
        :param dwh: Data warehouse
        :raises ValueNotFoundError: If not found
        """
        self.__tag = tag
        self.__date = date
        with dwh.connection() as conn:
            self.__value, = conn.execute(
                text(
                    "SELECT mesure "
                    "FROM v_pimesure "
                    "WHERE tag_code = :code and datetime = CAST(:date AS TEXT)"
                ),
                ({"code": self.__tag.code(), "date": self.__date})
            ).fetchone()
            if self.__value is None:
                raise ValueNotFoundError("PI measure not found")

    def tag(self) -> PITag:
        return self.__tag

    def date(self) -> datetime:
        return self.__date

    def value(self) -> float:
        return float(self.__value)


class PgPImeasures(PImeasures):
    """
    PI measures from PostgreSQL.
    .. since: 0.2
    """

    def __init__(self, tag: PITag, dwh: Dwh):
        """
        Ctor.
        :param tag: Tag
        :param dwh: Data warehouse
        """
        self.__tag = tag
        self.__dwh = dwh

    def items(self, start: datetime, end: datetime) -> list:
        result = []
        with self.__dwh.connection() as conn:
            for row in conn.execute(
                text(
                    "SELECT datetime FROM v_pimesure "
                    "WHERE TO_TIMESTAMP(datetime, 'YYYY-MM-DD HH24:MI:SS') "
                    "BETWEEN :start AND :end "
                    "AND tag_code = :code"
                ),
                ({"start": start, "end": end, "code": self.__tag.code()})
            ).fetchall():
                result.append(
                    PgPImeasure(self.__tag, row[0], self.__dwh)
                )
        return result

    def add(self, date: datetime, measure: float) -> PImeasure:
        with self.__dwh.connection() as conn:
            count, = conn.execute(
                text(
                    "SELECT count(*) FROM v_pimesure "
                    "WHERE tag_code = :code AND datetime = CAST(:date AS TEXT)"
                ),
                ({"code": self.__tag.code(), "date": date})
            ).fetchone()
            if count == 0:
                conn.execute(
                    text(
                        "INSERT INTO fact_pimesure "
                        "(tag_pk, date_pk, time_pk, mesure, millisecond) "
                        "VALUES"
                        "(:tag_pk, :date_pk, :time_pk, :mesure, :millis) "
                    ),
                    (
                        {
                            "tag_pk": self.__tag.uid(),
                            "date_pk": self.__date_pk(date),
                            "time_pk": self.__time_pk(date),
                            "mesure": measure,
                            "millis": math.floor(date.microsecond / 1000)
                        }
                    )
                )
                return PgPImeasure(self.__tag, date, self.__dwh)
            raise ValueAlreadyExistsError(
                "A measure already exists at "
                f"{date} for tag {self.__tag.code()}"
            )

    def __date_pk(self, date: datetime) -> int:
        """
        Date key.
        :param date: Datetime
        :return: UID
        :raises ValueNotFoundError: If key not found
        """
        with self.__dwh.connection() as conn:
            uid, = conn.execute(
                text(
                    "SELECT date_pk FROM dim_date "
                    "WHERE date_value = :date "
                ),
                ({"date": date.date()})
            ).fetchone()
            if uid is None:
                raise ValueNotFoundError("Saving PI measure: Date not found")
            return uid

    def __time_pk(self, date: datetime) -> int:
        """
        Time key.
        :param date: Datetime
        :return: UID
        :raises ValueNotFoundError: If key not found
        """
        with self.__dwh.connection() as conn:
            uid, = conn.execute(
                text(
                    "SELECT time_pk FROM dim_time "
                    "WHERE time_value = CAST(:time AS TEXT)"
                ),
                ({"time": date.time()})
            ).fetchone()
            if uid is None:
                raise ValueNotFoundError("Saving PI measure: Time not found")
            return uid
