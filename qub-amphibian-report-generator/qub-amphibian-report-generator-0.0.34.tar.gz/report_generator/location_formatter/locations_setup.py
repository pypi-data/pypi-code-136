"""# Locations setup.

Initial set up file that creates a json file with countries continents and regions

"""

import json
import os
import sqlite3
from sqlite3 import Error

import pandas
from loguru import logger

# Read Csvs
continents = [
    "africa",
    "asia",
    "europe",
    "antarctica",
    "north america",
    "south america",
    "central america",
]
countries = pandas.read_csv(
    os.path.join(os.getcwd(), "csv_files", "country-and-continent-codes.csv"),
    dtype=object,
    na_filter=False,
)
countries_2 = pandas.read_csv(
    os.path.join(os.getcwd(), "csv_files", "country_and_area_data.csv"),
    dtype=object,
    na_filter=False,
)
countries_3 = pandas.read_csv(
    os.path.join(os.getcwd(), "csv_files", "countrys_lat_long.csv"),
    dtype=object,
    na_filter=False,
)
states = pandas.read_csv(
    os.path.join(os.getcwd(), "csv_files", "states.csv"), encoding="iso8859_15"
)

# Get database connection


# Initialise location data object
location_data = {"continent": {}, "country": {}, "region": {}}


# Set up sqlite connection
conn = None

try:
    conn = sqlite3.connect("location_database/location.db")
except Error as e:
    logger.error(e)

cursor = conn.cursor()


# Iterate through continents:
logger.debug("Iterating continents")
for continent in continents:

    # SQL query

    sql = f"""
    select place_name, latitude, longitude FROM geocode
    WHERE place_name="{continent.title()}" AND country_code is NULL limit 1;
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    continent = {
        "continent": rows[0][0],
        "latitude": rows[0][1],
        "longitude": rows[0][2],
    }

    location_data["continent"][rows[0][0].lower()] = continent

# Iterate through countries
country_results = []
logger.debug("Iterating countries")

for row in countries.iterrows():
    vals = []
    for value in row:
        if isinstance(value, int):
            vals.append(value)
        else:
            vals = [*vals, *value.values]
    try:
        name = vals[3].split(",")[0].split("(")[0]
        ccode = vals[4]
    except TypeError:
        name = vals[3]
        ccode = vals[4]

    sql_1 = f"""
    select latitude, longitude FROM geocode
    WHERE country_code='{ccode}' limit 1;
    """

    sql_2 = f"""
    select continent_name, country_name from country_codes
    where Two_Letter_Country_Code='{ccode}';
    """

    cursor.execute(sql_1)
    rows_1 = cursor.fetchall()

    cursor.execute(sql_2)
    rows_2 = cursor.fetchall()
    country_results.append([rows_1, rows_2])

    lat = None
    lon = None
    continent_name = None
    full_country_name = None

    if rows_1 != []:
        lat = rows_1[0][0]
        lon = rows_1[0][1]
    if rows_2 != []:
        continent_name = rows_2[0][0]
        full_country_name = rows_2[0][1]

    country = {
        "country": name,
        "country_code": ccode,
        "latitude": lat,
        "longitude": lon,
        "continent": continent_name,
        "country_full_name": full_country_name,
    }

    location_data["country"][name.lower()] = country


# Iterate through regions
logger.debug("Iterating regions")

for row in states.iterrows():
    vals = []
    for value in row:
        if isinstance(value, int):
            vals.append(value)
        else:
            vals = [*vals, *value.values]

    ccode = vals[4]

    sql_1 = f"""
    select continent_name, country_name from country_codes
    where Two_Letter_Country_Code='{ccode}'LIMIT 1;
    """

    cursor.execute(sql_1)
    resps = cursor.fetchall()

    if len(resps) > 0:
        continent = resps[0][0]
        country_full_name = resps[0][1]
    else:
        continent = None
        country_full_name = None

    region_name = (
        vals[2]
        .lower()
        .replace("parish", "")
        .replace("county", "")
        .replace("province", "")
        .replace("district", "")
        .replace("territory", "")
        .replace("governorate", "")
        .replace("region", "")
        .replace("department", "")
        .replace("prefecture", "")
        .replace("municipality", "")
        .replace("regional unit", "")
        .strip()
    )

    region = {
        "region": region_name,
        "country": vals[5],
        "country_code": ccode,
        "continent": continent,
        "latitude": vals[8],
        "longitude": vals[9],
        "country_full_name": country_full_name,
    }

    location_data["region"][region_name.lower()] = region


# dump to json
location_json = json.dumps(location_data, ensure_ascii=False)
logger.debug("Writing to Json")

# write to file
with open("location.json", "w", encoding="utf-8") as file:
    file.write(location_json)

cursor.close()
conn.close()
