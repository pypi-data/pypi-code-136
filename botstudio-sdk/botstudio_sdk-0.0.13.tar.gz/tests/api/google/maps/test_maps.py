import os
from src.botstudio_sdk.api.google.maps import get_distance, get_place_id


def test_get_distance():
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")

    # Stuc-Concurrent
    place_id_sc = "ChIJaWwAIWjkxUcR_qs0D7yXQSA"

    # workspace 42
    place_id_ws = "ChIJYx0GM14zxEcRLzueyePISpY"

    dist_meters, dist_seconds = get_distance(
        api_key=api_key,
        place_id_origin=place_id_sc,
        place_id_destination=place_id_ws,
    )

    assert dist_meters == 71368
    assert dist_seconds == 3443


def test_get_place_id():
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")

    # workspace 42
    query_ws = "Schiedamse vest 154 rotterdam"

    place_id = get_place_id(
        api_key=api_key,
        query=query_ws,
    )

    assert place_id == "ChIJYx0GM14zxEcRLzueyePISpY"
