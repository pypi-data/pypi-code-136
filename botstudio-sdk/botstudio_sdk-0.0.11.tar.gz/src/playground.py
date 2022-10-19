from botstudio_sdk import get_zip_code_info, get_place_id, get_distance

if __name__ == "__main__":
    import os
    import pprint
    from botstudio_sdk import get_zip_code_info

    api_key = os.getenv("API_KEY_BAG")
    postcode = "3011BH"
    huisnummer = "154"

    info = get_zip_code_info(api_key, postcode, huisnummer)

    pprint.pprint(info)

    ###

    adres = (
        f"{info['adressen'][0]['adresregel_1']}, {info['adressen'][0]['adresregel_2']}"
    )
    print(adres)

    ###

    import os
    from botstudio_sdk import get_place_id

    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    adres = "Schiedamse Vest 154, 3011 BH  ROTTERDAM"

    place_id = get_place_id(
        api_key=api_key,
        query=adres,
    )

    print(place_id)

    ###

    import os
    from botstudio_sdk import get_distance

    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    place_id_origin = "ChIJYx0GM14zxEcRLzueyePISpY"
    place_id_destination = "ChIJaWwAIWjkxUcR_qs0D7yXQSA"

    dist_meters, dist_seconds = get_distance(
        api_key=api_key,
        place_id_origin=place_id_origin,
        place_id_destination=place_id_destination,
    )

    print(dist_meters)
    print(dist_seconds)
