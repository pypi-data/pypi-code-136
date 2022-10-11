"""# Location updater.

Module used to take locations data from a DataFrame object and
update that data to provide better information.

"""

# Python imports
import json
import os
import sqlite3
import time
from sqlite3 import Error

import pandas
from loguru import logger

import report_generator.config
from report_generator.location_formatter.location_finder import (
    find_location,
    find_unknown,
)


def update_location(data_frame: pandas.DataFrame) -> pandas.DataFrame:
    """Update location.

    Takes a pandas data frame object and runs the location finder on each cell of the
    Location column/series

    Updates the data frames values for the Location column then returns the updated
    data frame.

    Args:
        data_frame (pandas.DataFrame): Pandas DataFrame object

    Returns:
        updated_data_frame (pandas.DataFrame): Pandas DataFrame object

    """
    # Load Locations Data
    LOCATIONS_DATA = load_locations_data()

    logger.info("Update Location entries Start")
    process_start_time = time.time()

    updated_data_frame = update_location_entries(data_frame, LOCATIONS_DATA)

    process_time_taken = time.time() - process_start_time
    logger.info(f"Update Location entries end: {process_time_taken}s")

    return updated_data_frame


def update_location_entries(
    data_frame: pandas.DataFrame, LOCATIONS_DATA: object
) -> pandas.DataFrame:
    """Update location entries.

    Takes pandas data frame object and calls lambda function on each entry in
    'GeographicRegion' to update the entry. Then returns updated data frame object.

    Args:
        data_frame (pandas.DataFrame): Pandas DataFrame object
        LOCATIONS_DATA (object) : location data

    Returns:
        data_frame (pandas.DataFrame): Pandas DataFrame object

    """
    locations = data_frame["GeographicRegion"].values.tolist()
    LOCATIONS_DATA = update_locations_unknowns(locations, LOCATIONS_DATA)

    data_frame["FormattedGeographicRegion"] = data_frame["GeographicRegion"].apply(
        lambda x: update_location_entry(x, LOCATIONS_DATA)
    )

    return data_frame


def update_location_entry(location_str: str, LOCATIONS_DATA: object) -> str:
    """Update location entry.

    Takes the 'GeographicRegion' cell string value. Splits it into sections.
    Attempts to transform into a more robust location value

        'continent-country-region/continent-country-region/etc'

    Args:
        location_str (str): string location value
        LOCATIONS_DATA (object) : location data


    Returns:
        updated_location_str (str): string updated location value

    """
    # location_strs = location_str.split("/")
    # updated_location_strings = []

    # for location in location_strs:
    #     location_obj = create_location_obj(location)
    #     updated_location_strings.append(location_obj.__str__())

    locations = find_location(location_str, LOCATIONS_DATA)

    updated_location_strings = []

    for location in locations:
        updated_location_strings.append(location.__str__())

    return "/".join(updated_location_strings)


def load_location_json(file_path: str) -> object:
    """Load location json.

    Opens and returns location object from json file

    Args:
        file_path (str): file path string

    Returns:
        location_data (object): location data python object

    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_locations_data() -> dict:
    """Load locations data.

    Opens json file and loads locations data from json
    and returns locations object.

    Returns:
        locations_data (dict): Python dict containing location info

    """
    # load location object
    logger.info("Read location json Start")
    process_start_time = time.time()
    config = report_generator.config.load_config()
    file_path = os.path.join(
        config["dir_path"], "data", "locations", "location_json", "location.json"
    )
    locations_data = load_location_json(file_path)

    process_time_taken = time.time() - process_start_time
    logger.info(f"Read location json end: {process_time_taken}s")

    return locations_data


def update_locations_unknowns(locs: list, locations_data: object) -> object:
    """Update unknown locations.

    Takes list of unknown locations and passes to the find unknown method.
    If data is still unknown passes to the search for unknowns method.
    Takes these results and passes to the update locations data method to
    update the location data.

    Args:
        locs: list of locations
        locations data: Object containing location data

    Returns:
        locations_data: Object containing location data

    """
    unknowns = [find_unknown(loc, locations_data) for loc in locs]
    unknowns = [*{item for sublist in unknowns for item in sublist}]
    results = search_for_unknowns(unknowns)
    return update_locations_data(results, locations_data)


def update_locations_data(results: list, locations_data: object) -> None:
    """Update locations data.

    Updates the locations data with results of unknown location search.

    Args:
        results: list of results from unknown locaiton search
        locations_data: Object containing locations data

    """
    for region in results:
        logger.debug(region[0])
        region_data = {
            "region": region[0],
            "country": str(region[1]).split(",")[0],
            "continent": region[2],
            "latitude": region[3],
            "longitude": region[4],
            "country_code": region[5],
            "country_full_name": region[1],
        }
        locations_data["region"][region[0].lower()] = region_data

    save_locations_data(locations_data)
    return locations_data


def search_for_unknowns(unknowns: list):
    """Search for unknowns.

    Takes list of unidentified locations and searches locations database for
    results matching the unknown location string.

    Args:
        unknowns: list of unknown location strings.

    Returns:
        results: list of results from searching locations database

    """
    # define search func
    def unknown_sql_query(unknown: str):
        # Timing query
        logger.info("Location unknown value sql query start")
        process_start_time = time.time()

        time.sleep(0.01)
        # Sql connection/cursor
        conn = sqlite3.connect("location_database/location.db")
        cursor = conn.cursor()

        # Sql query
        sql = f"""
        select Country_Name, Continent_Name, latitude, longitude, country_code
        from geocode
        join country_codes on geocode.country_code=country_codes.Two_Letter_Country_Code
        where place_name like '{unknown.title()}'
        or alternate_names like '{unknown.title}%' limit 1
        """

        # Execute
        cursor.execute(sql)
        rows = cursor.fetchall()
        logger.debug(unknown)

        # Check if result
        if rows != []:
            results.append([unknown, *list(rows[0])])
        else:
            logger.debug("no match")

        # End logging time
        process_time_taken = time.time() - process_start_time
        logger.info(f"Location unknown value sql query end: {process_time_taken}s")

    logger.info("Search for unknowns Start")
    process_start_time = time.time()
    results = []
    try:
        for unknown in unknowns:
            unknown_sql_query(unknown)

    except Error as e:
        logger.error(e)

    process_time_taken = time.time() - process_start_time
    logger.info(f"Search for unknowns end: {process_time_taken}s")

    return results


def save_locations_data(locations_data: object) -> None:
    """Save locations data.

    Takes the locations data object and uses json.dumps to
    write the data to a json file.

    Args:
        locations_data - object containing locations data

    """
    logger.debug("Saving locations data")
    dumped = json.dumps(locations_data)
    config = report_generator.config.load_config()
    file_path = os.path.join(
        config["dir_path"], "data", "locations", "location_json", "location.json"
    )
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(dumped)
