# Github page: https://github.com/googlemaps/google-maps-services-python
# info about parameters https://developers.google.com/maps/documentation/distance-matrix/distance-matrix

import requests
from typing import Tuple


def get_distance(
    api_key: str,
    place_id_origin: str,
    place_id_destination: str,
) -> Tuple[int, int]:
    """Returns the distance between points in meters and seconds.
    More info: https://developers.google.com/maps/documentation/distance-matrix/distance-matrix

    :param api_key: google api key
    :type api_key: str
    :param place_id_origin: textual identifier that uniquely identifies the place of origin
    :type place_id_origin: str
    :param place_id_destination: textual identifier that uniquely identifies the place of destination
    :type place_id_destination: str
    :return: distance in meters and seconds
    :rtype: tuple(int, int)
    """

    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": f"place_id:{place_id_origin}",
        "destinations": f"place_id:{place_id_destination}",
        "key": api_key,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        dist_meters = response.json()["rows"][0]["elements"][0]["distance"]["value"]
        dist_seconds = response.json()["rows"][0]["elements"][0]["duration"]["value"]
        return dist_meters, dist_seconds


def get_place_id(
    api_key: str,
    query: str,
) -> str:
    """Returns a place id based on a query string.
    More info: https://developers.google.com/maps/documentation/places/web-service/search-text

    :param api_key: google api key
    :type api_key: str
    :param query: text string on which to search
    :type query: str
    :return: place_id: textual identifier that uniquely identifies a place
    :rtype: str
    """

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "key": api_key,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        place_id = response.json()["results"][0]["place_id"]
        return place_id


if __name__ == "__main__":
    import os

    api_key = os.getenv("GOOGLE_MAPS_API_KEY")

    # stuc concurrent
    place_id_sc = "ChIJaWwAIWjkxUcR_qs0D7yXQSA"
    query_sc = "Venenweg 17I, 1161 AK Zwanenburg"

    # workspace 42
    place_id_ws = "ChIJYx0GM14zxEcRLzueyePISpY"
    query_ws = "Schiedamse vest 154 rotterdam"

    dist_meters, dist_seconds = get_distance(
        api_key=api_key,
        place_id_origin=place_id_sc,
        place_id_destination=place_id_ws,
    )
    print(dist_meters)
    print(dist_seconds)
