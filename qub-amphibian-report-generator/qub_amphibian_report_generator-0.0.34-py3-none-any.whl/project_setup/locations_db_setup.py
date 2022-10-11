"""# Database setup.

Setup file to create a locations SQLITE database and load location information
into the database to allow for queries.

"""

import os
import sqlite3
import time
from sqlite3 import Error

import pandas
import tqdm
from loguru import logger


def locations_database_setup(location_path: str) -> None:
    """Location database setup.

    Sets up database for locations data. Creates database,
    loads data from csv. Creates tables in database. Inserts
    csv data into the database.

    Args:
        location_path (str): Path string to project location.

    """
    db_path = os.path.join(location_path, "location_database")
    csv_path = os.path.join(location_path, "csv_files")
    conn = create_connection(db_path)
    logger.info("Location Database Created")
    create_tables(conn)
    time.sleep(1)
    logger.info("Tables Created")
    insert_country_data(conn, csv_path)
    logger.info("Country Data Populated")
    time.sleep(1)
    logger.info("Populating Geocode data:")
    insert_geocode_data(conn, csv_path)
    logger.info("Geocode Data Populated")
    time.sleep(1)
    logger.info("Location database set up complete.")
    conn.close()


def create_connection(db_path: str) -> sqlite3.Connection:
    """Create connection.

    Create a SQLite3 connection object and return it.

    Args:
        db_path (str): Path string to db directory location.

    Returns:
        conn: SQLite3 connection object

    """
    conn = None
    try:
        conn = sqlite3.connect(os.path.join(db_path, "location.db"))
    except Error as e:
        logger.error(e)

    return conn


def create_tables(conn: sqlite3.Connection) -> None:
    """Create SQL table strings.

    Create SQL table strings for the locations database.

    Use SQLite3 connection object to create tables in locations
    database with table strings.

    Tables:
        country_codes: table representing country data
        geocode: table representing geocode data

    Args:
        conn: SQLite3 connection object

    """
    country_table = """CREATE TABLE IF NOT EXISTS country_codes (
        country_code_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        continent_name VARCHAR(50) NOT NULL,
        continent_code VARCHAR(4) NOT NULL,
        country_name VARCHAR(50) NOT NULL,
        two_letter_country_code VARCHAR(2),
        three_letter_country_code VARCHAR(3),
        country_number integer NOT NULL
    )
    """

    geocode_table = """CREATE TABLE IF NOT EXISTS geocode (
            geoname_id INT NOT NULL PRIMARY KEY,
            place_name VARCHAR(50),
            ascii_name TEXT,
            alternate_names TEXT,
            latitude REAL,
            longitude REAL,
            feature_class TEXT,
            feature_code TEXT,
            country_code TEXT,
            cc2 TEXT,
            admin1_code TEXT,
            admin2_code TEXT,
            admin3_code TEXT,
            admin4_code TEXT,
            population_info integer,
            elevation integer,
            dem integer,
            timezone TEXT,
            modification TEXT
        )
    """

    try:
        cursor = conn.cursor()
        cursor.execute(country_table)
        logger.debug("Country Table Created")
        cursor.execute(geocode_table)
        logger.debug("Geocode Table Created")
    except Error as e:
        logger.error(e)


def insert_country_data(conn: sqlite3.Connection, csv_path: str) -> None:
    """Insert country data.

    Inserts country data into the country_codes table

    Args:
        conn: SQLite3 connection object

    """
    # Open Country data in pandas
    file_path = os.path.join(csv_path, "country-and-continent-codes.csv")
    data_frame = pandas.read_csv(file_path)

    data_frame.to_sql("country_codes", conn, if_exists="replace", index=False)


def insert_country_data_row(conn: object, row_values: list) -> None:
    """Insert country data row.

    Inserts row of country data into country table in locations database.

    Args:
        conn: SQLite3 connection object
        row_values: List of values from the Pandas dataframe row.

    """
    sql = """ INSERT INTO country_codes
    (
        continent_name,
        continent_code,
        country_name,
        two_letter_country_code,
        three_letter_country_code,
        country_number
    )
    VALUES(?,?,?,?,?,?)"""

    try:
        cursor = conn.cursor()
        cursor.execute(sql, row_values)
        conn.commit()
    except Error as e:
        logger.error(row_values)
        logger.error(e)


def insert_geocode_data(conn: object, csv_path: str) -> None:
    """Insert geocode data.

    Inserts geocode data into locations database.

    Opens the csv files that contain the geocode data directory
    and iterates through to insert the geocode data by section.


    Args:
        conn:       SQLite3 connection object

        csv_path:   Path string to csv directory

    """
    dir_path = os.path.join(csv_path, "split_csv")

    files = os.listdir(dir_path)
    progress_bar = tqdm.tqdm(total=len(files), desc="Inserting Data")
    for i in range(len(files)):
        file = files[i]
        file_path = os.path.join(dir_path, file)
        insert_geocode_data_section(conn, file_path)
        progress_bar.update(1)


def insert_geocode_data_section(conn: object, file_path: str) -> None:
    """Insert geocode data section.

    Opens ands processes geocode data section csv file and
    then inserts it into the geocode_data table in the locations
    database.

    Args:
        conn: SQLite3 connection object
        file_path: string of filepath to section csv

    """
    data_frame = pandas.read_csv(file_path, sep="\t")
    data_frame.to_sql("geocode", conn, if_exists="append", index=False)


def main():
    """Locations db main method."""
    locations_database_setup()


if __name__ == "__main__":
    main()
