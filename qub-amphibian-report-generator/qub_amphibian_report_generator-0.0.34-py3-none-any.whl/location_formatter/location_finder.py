"""# Locations finder.

Methods used to break down locations strings and categorise the locations
into continents, countries, regions and unknown locations.

"""

import re
import time

from loguru import logger

from report_generator.location_formatter.location import Location


def find_location(location_str: str, locations_data: object) -> list:
    """Find location.

    Takes a location string splits it into sections. Attempts
    to determine what kind of location (continent, country, region) the section is.

    Creates list of Location objects based on results.

    Args:
        location_str(str): string value of GeographicRegion cell
        LOCATIONS_DATA(object) : location data

    Returns:
        location_objs(list): list of Location objects

    """
    # logger
    logger.debug("Location finder func Start")
    process_start_time = time.time()

    if locations_data is None:
        logger.error("Locations data is None")
        raise Exception

    logger.debug(f"Sections: {location_str}")

    # Handling nan/null dataset error
    if str(location_str) == "nan":
        location_str = ""

    # Split location string into component sections

    # location_str = re.sub("island|islands", "", location_str.lower()).strip()
    sections = re.split("[,/()-+]", location_str.lower().strip())

    # lists for each section
    locations = []
    continents_list = []
    countries_list = []
    regions_list = []
    unknown_list = []

    # Iterate through the sections to try and determine what kind of location they are

    for section in sections:
        # logger.debug(f"Section: {section}")

        # Data Cleaning
        # section = re.sub(" s$| is$", "", section)
        section = section.lower().strip().strip(".").strip('"').strip()

        # Handle common America issue
        if section == "central":
            section = "central america"
        if section == "north":
            section = "north america"
        if section == "south":
            section = "south america"

        # Iterate through sections check if string is in continents list
        # or countries list

        if section in locations_data["continent"].keys():
            continents_list.append(locations_data["continent"][section])
        elif section in locations_data["country"].keys():
            country = locations_data["country"][section]
            countries_list.append(country)
        elif section in locations_data["region"].keys():
            region = locations_data["region"][section]
            regions_list.append(locations_data["region"][section])
        else:
            # logger.debug(f"Region Found: {section}")
            unknown_list.append(section)

    # Try to create a location object based on results

    for continent in continents_list:
        loc = Location(
            continent=continent["continent"],
            latitude=continent["latitude"],
            longitude=continent["longitude"],
        )
        locations.append(loc)

    for country in countries_list:
        loc = Location(
            country["continent"],
            country["country"],
            latitude=country["latitude"],
            longitude=country["longitude"],
            country_code=country["country_code"],
        )
        locations.append(loc)

    for region in regions_list:
        loc = Location(
            region["continent"],
            region["country"],
            region["region"],
            latitude=region["latitude"],
            longitude=region["longitude"],
            country_code=region["country_code"],
        )
        locations.append(loc)

    for unknown in unknown_list:
        loc = Location(region=unknown)
        locations.append(loc)

    # Log time taken
    process_time_taken = time.time() - process_start_time
    logger.debug(f"Location finder func end: {process_time_taken}s")

    return locations


def find_unknown(location_str: str, locations_data: object) -> object:
    """Find unknown location.

    Takes a location string splits it into sections. Finds unknown regions.

    Creates list based on results.

    Args:
        location_str(str): string value of GeographicRegion cell
        LOCATIONS_DATA(object) : location data

    Returns:
        location_objs(list): list of Location objects

    """
    if locations_data is None:
        raise Exception
    # logger
    logger.debug("unknown finder func Start")
    process_start_time = time.time()

    # Handling nan/null dataset error
    if str(location_str) == "nan":
        location_str = ""

    # Split location string into component sections
    # location_str = re.sub("island|islands", "", location_str.lower()).strip()
    sections = re.split("[,/()-+]", location_str.lower().strip())

    # Unknown list
    unknown_list = []

    # Iterate through the sections to try and determine what kind of location they are

    for section in sections:
        # logger.debug("Section: {section}")

        # Data Cleaning
        # section = re.sub(r"\ss$", "", section)
        section = section.lower().strip().strip(".")

        # Handle common America issue
        if section == "central":
            section = "central america"
        if section == "north":
            section = "north america"
        if section == "south":
            section = "south america"

        # Iterate to check if string is in continents, countries or regions

        conditions = [
            (section not in locations_data["continent"]),
            (section not in locations_data["country"].keys()),
            (section not in locations_data["region"].keys()),
        ]

        if all(conditions):
            unknown_list.append(section)

    # Log time taken
    process_time_taken = time.time() - process_start_time
    logger.debug(f"Location finder func end: {process_time_taken}s")

    return unknown_list
