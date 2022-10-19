"""
Test case for PITag.
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

from sqlalchemy.engine import Connection, Engine  # type: ignore
from sqlalchemy import text  # type: ignore
from testcontainers.postgres import PostgresContainer  # type: ignore
from edv_dwh_connector.dwh import Dwh
from edv_dwh_connector.pg_dwh import PgDwh


class AdaptedPostreSQL(PostgresContainer):
    """
    Adapted PostgreSQL container to fix host.
    .. since: 0.2
    """

    def __init__(self) -> None:
        """
        Ctor.
        """
        super().__init__('postgres:14.5')

    def get_connection_url(self, host: str = None):
        """
        Connection url.
        :param host: Hostname
        :return: Url
        """
        return super().get_connection_url(host) \
            .replace('localnpipe', 'localhost')


# flake8: noqa
SCHEMA = """
    CREATE TABLE IF NOT EXISTS Dim_PItag (
        tag_PK serial NOT NULL,
        tag_code CHARACTER VARYING (225) NOT NULL,
        tag_name CHARACTER VARYING (225) NOT NULL,
        tag_units CHARACTER(10),
        CONSTRAINT dim_tag_pk PRIMARY KEY (tag_PK)
    );
    CREATE TABLE IF NOT EXISTS Dim_Time(
        time_PK INTEGER NOT NULL,
        time_value CHARACTER(8) NOT NULL,
        hours_24 INTEGER NOT NULL,
        hours_12 INTEGER NOT NULL,
        hour_minutes INTEGER  NOT NULL,
        minutes_second INTEGER  NOT NULL,
        day_minutes INTEGER NOT NULL,
        hour_second INTEGER NOT NULL,
        day_second INTEGER NOT NULL,
        day_time_name CHARACTER VARYING (20) NOT NULL,
        day_night CHARACTER VARYING (20) NOT NULL,
        CONSTRAINT dim_time_pk PRIMARY KEY (time_PK)
    );
    CREATE TABLE IF NOT EXISTS Dim_Date(
        date_PK NUMERIC NOT NULL,
        date_value date NOT NULL,
        year INTEGER NOT NULL,
        month INTEGER NOT NULL,
        monthname CHARACTER (12)  NOT NULL,
        day INTEGER NOT NULL,
        dayofyear INTEGER NOT NULL,
        weekdayname CHARACTER (12) NOT NULL,
        calendarweek INTEGER NOT NULL,
        formatteddate CHARACTER (10) NOT NULL,
        quartal CHARACTER (2) NOT NULL,
        yearquartal CHARACTER (7) NOT NULL,
        yearmonth CHARACTER (7) NOT NULL,
        yearcalendarweek CHARACTER (7) NOT NULL,
        weekend CHARACTER (10) NOT NULL,
        cwstart date NOT NULL,
        cwend date NOT NULL,
        monthstart date NOT NULL,
        monthend date NOT NULL,
        CONSTRAINT dim_date_pk PRIMARY KEY (date_PK)
    );
    CREATE TABLE IF NOT EXISTS Fact_PImesure (
        tag_PK INTEGER NOT NULL,
        date_PK INTEGER NOT NULL,
        time_PK INTEGER NOT NULL,
        millisecond NUMERIC DEFAULT 0 NOT NULL,
        mesure NUMERIC(8,3) NOT NULL,
        CONSTRAINT fk_pimesure_dim_pitag FOREIGN KEY (tag_PK) REFERENCES dim_pitag (tag_PK) ON DELETE RESTRICT ON UPDATE CASCADE,
        CONSTRAINT fk_pimesure_dim_date FOREIGN KEY (date_PK) REFERENCES dim_date (date_PK) ON DELETE RESTRICT ON UPDATE CASCADE,
        CONSTRAINT fk_pimesure_dim_time FOREIGN KEY (time_PK) REFERENCES dim_time (time_PK) ON DELETE RESTRICT ON UPDATE CASCADE,
        CONSTRAINT fact_pimesure_pk PRIMARY KEY (date_PK, time_PK, tag_PK,millisecond)
    );
    CREATE  VIEW v_pimesure AS
      SELECT CAST(dd.date_value AS TEXT)||' '||dt.time_value datetime, dtg.tag_code, dtg.tag_name, dtg.tag_units, fp.mesure
      FROM dim_date dd,dim_time dt,dim_pitag dtg,fact_pimesure fp
      WHERE fp.date_pk = dd.date_pk
      AND fp.time_pk = dt.time_pk
      AND fp.tag_pk = dtg.tag_pk;
    INSERT INTO  Dim_Time
    SELECT  CAST(TO_CHAR(second, 'hh24miss') AS numeric) time_PK,
        TO_CHAR(second, 'hh24:mi:ss') AS time_value,
        -- Hour of the day (0 - 23)
        EXTRACT (hour FROM  second) AS hour_24,
        -- Hour of the day (0 - 11)
        TO_NUMBER(TO_CHAR(second, 'hh12'),'99') hour_12,
        -- Hour minute (0 - 59)
        EXTRACT(minute FROM second) hour_minutes,
        -- minute second (0 - 59)
        EXTRACT(second FROM second) minutes_second,
        -- Minute of the day (0 - 1439)
        EXTRACT(hour FROM second)*60 + EXTRACT(minute FROM second) day_minutes,
        -- second of the hour (0 - 3599)
        EXTRACT(minute FROM second)*60 + EXTRACT(second FROM second) hour_second,
        -- second of the day (0 - 86399)
        EXTRACT(hour FROM second)*3600 + EXTRACT(minute FROM second)*60 + EXTRACT(second FROM second) day_second,
        -- Names of day periods
        CASE WHEN TO_CHAR(second, 'hh24:mi') BETWEEN '06:00' AND '08:29'
        THEN 'Morning'
        WHEN TO_CHAR(second, 'hh24:mi') BETWEEN '08:30' AND '11:59'
        THEN 'AM'
        WHEN TO_CHAR(second, 'hh24:mi') BETWEEN '12:00' AND '17:59'
        THEN 'PM'
        WHEN TO_CHAR(second, 'hh24:mi') BETWEEN '18:00' AND '22:29'
        THEN 'Evening'
        ELSE 'Night'
        END AS day_time_name,
        -- Indicator of day or night
        CASE WHEN TO_CHAR(second, 'hh24:mi') BETWEEN '07:00' AND '19:59' THEN 'Day'
        ELSE 'Night'
        END AS day_night
    FROM (SELECT '0:00:00'::time + (sequence.second || ' seconds')::interval AS second
        FROM generate_series(0,86399) AS sequence(second)
        GROUP BY sequence.second
        ) DQ
    ORDER BY 1;
    INSERT INTO  Dim_Date
    SELECT
        CAST(TO_CHAR(datum, 'yyyymmdd') as numeric) date_PK,
        datum as Date,
        EXTRACT(year FROM datum) AS Year,
        EXTRACT(month FROM datum) AS Month,
        -- Localized month name
        TO_CHAR(datum, 'TMMonth') AS MonthName,
        EXTRACT(day FROM datum) AS Day,
        EXTRACT(doy FROM datum) AS DayOfYear,
        -- Localized weekday
        TO_CHAR(datum, 'TMDay') AS WeekdayName,
        -- ISO calendar week
        EXTRACT(week FROM datum) AS CalendarWeek,
        TO_CHAR(datum, 'dd-mm-yyyy') AS FormattedDate,
        'Q' || TO_CHAR(datum, 'Q') AS Quartal,
        TO_CHAR(datum, 'yyyy/"Q"Q') AS YearQuartal,
        TO_CHAR(datum, 'yyyy/mm') AS YearMonth,
        -- ISO calendar year and week
        TO_CHAR(datum, 'iyyy/IW') AS YearCalendarWeek,
        -- Weekend
        CASE WHEN EXTRACT(isodow FROM datum) in (6, 7) THEN 'Weekend' ELSE 'Weekday' END AS Weekend,
        -- ISO start and end of the week of this date
        datum + (1 - EXTRACT(isodow FROM datum))::integer AS CWStart,
        datum + (7 - EXTRACT(isodow FROM datum))::integer AS CWEnd,
        -- Start and end of the month of this date
        datum + (1 - EXTRACT(day FROM datum))::integer AS MonthStart,
        (datum + (1 - EXTRACT(day FROM datum))::integer + '1 month'::interval)::date - '1 day'::interval AS MonthEnd
    FROM (
        -- There are 3 leap years in this range, so calculate 365 * 10 + 3 records
        SELECT '2022-01-01'::DATE + sequence.day AS datum
        FROM generate_series(0,30) AS sequence(day)
        GROUP BY sequence.day
         ) DQ
    ORDER BY 1;
    INSERT INTO Dim_PITag (tag_code, tag_name, tag_units)
    VALUES
        ('AI162003_SCLD', 'Carbon Scout Tank 1 Carbon Concentration Scaled Value', 'g/l'),
        ('AI162007_SCLD', 'Carbon Scout Tank 3 pH Scaled Value', 'pH'),
        ('AI162014_SCLD', 'Carbon Scout Tank 5 DO Scaled Value', 'ppm');
    """


# pylint: disable=too-few-public-methods
class PgDwhForTests(Dwh):
    """PostgreSQL data warehouse for tests"""

    def __init__(self, engine: Engine):
        self.__dwh = PgDwh(engine)
        with self.__dwh.connection() as conn:
            conn.execute(
                text(SCHEMA)
            )

    def connection(self) -> Connection:
        return self.__dwh.connection()
