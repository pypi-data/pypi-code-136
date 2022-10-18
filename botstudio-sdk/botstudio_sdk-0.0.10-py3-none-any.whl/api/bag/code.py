# More info:
# https://github.com/lvbag/BAG-API/blob/master/Features/paginering.feature
# https://www.kadaster.nl/documents/1953498/2762071/Productbeschrijving+BAG+API+Individuele+Bevragingen.pdf/cf35e5fd-ddb0-bc82-ffc5-6e7877a58ffa?t=1638438344305
# https://lvbag.github.io/BAG-API/Technische%20specificatie/#/Adres%20uitgebreid/zoekAdresUitgebreid
# https://lvbag.github.io/BAG-API/Technische%20specificatie/
import os
from typing import List

import requests

URL_PRODUCTIE = "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/"
API_KEY = os.getenv("API_KEY_BAG")


def _get_extended_address_info(
    postcode: str,
    huisnummer: str,
    huisnummertoevoeging: str = None,
    huisletter: str = None,
    exacte_match: bool = False,
    adresseerbaar_object_identificatie: str = None,
    woonplaats_naam: str = None,
    openbare_ruimte_naam: str = None,
    page: int = None,
    page_size: int = 100,
    q: str = None,
) -> dict:
    """Query extensive information an address based on different combinations of parameters."""

    headers = {
        "X-Api-Key": API_KEY,
        "Accept-Crs": "epsg:28992",
        "accept": "application/hal+json",
    }

    params = {
        "postcode": postcode,
        "huisnummer": huisnummer,
        "huisnummertoevoeging": huisnummertoevoeging,
        "huisletter": huisletter,
        "exacteMatch": exacte_match,
        "adresseerbaarObjectIdentificatie": adresseerbaar_object_identificatie,
        "woonplaatsNaam": woonplaats_naam,
        "openbareRuimteNaam": openbare_ruimte_naam,
        "page": page,
        "pageSize": page_size,
        "q": q,
    }

    url = f"{URL_PRODUCTIE}adressenuitgebreid"

    # Get the response from the API
    response = requests.get(url, headers=headers, params=params)

    # Check if the response is valid
    if response.status_code == 200:
        return response.json()
    else:
        raise ConnectionError(f"Error: {response.status_code} {response.reason}")


def _clean_bag_api_output(api_output: dict) -> List[dict]:
    """Clean the api output to a more user friendly version."""

    items_to_keep = [
        "adresregel5",
        "adresregel6",
        "openbareRuimteNaam",
        "huisnummer",
        "huisletter",
        "huisnummertoevoeging",
        "oorspronkelijkBouwjaar",
        "oppervlakte",
        "gebruiksdoelen",
        "typeAdresseerbaarObject",
        "woonplaatsNaam",
    ]

    items_to_rename = {
        "oorspronkelijkBouwjaar": "bouwjaar",
        "typeAdresseerbaarObject": "type_object",
        "woonplaatsNaam": "woonplaats",
        "adresregel6": "adresregel_2",
        "adresregel5": "adresregel_1",
        "openbareRuimteNaam": "straatnaam",
    }

    # Create a new list with dictionaries with adress information
    adressen = []
    for item in api_output["_embedded"]["adressen"]:

        # Create a new dictionary with only the items we want to keep and if item is not present, set it to None
        new_dict = {key: item.get(key, None) for key in items_to_keep}

        # Rename all items to a more user friendly version
        for old_key, new_key in items_to_rename.items():
            if old_key in new_dict.keys():
                new_dict[new_key] = new_dict.pop(old_key)

        # Change values to a more user friendly version
        for key, value in new_dict.items():
            # if value is an integer or float, convert to string
            if isinstance(value, int) or isinstance(value, float):
                new_dict[key] = str(value)
            # if value is a list, with strings, integers and/or floats, convert to string
            elif isinstance(value, list):
                new_dict[key] = ", ".join([str(x) for x in value])
            # if value is a dictionary, convert key and value to string
            elif isinstance(value, dict):
                new_dict[key] = ", ".join([f"{k}: {v}" for k, v in value.items()])
            # if value is None, convert to empty string
            elif value is None:
                new_dict[key] = ""

        # Add the new dictionary to the list
        adressen.append(new_dict)

    return adressen


def get_zip_code_info(
    zip_code: str,
    house_number: str,
) -> List[dict]:
    """Get extensive information about an address based on zip code and house number.

    returns a list of dictionaries with the following keys:
        - adresregel_1
        - adresregel_2
        - straatnaam
        - huisnummer
        - huisletter
        - huisnummertoevoeging
        - woonplaats
        - bouwjaar
        - oppervlakte
        - gebruiksdoelen
        - type_object
    """

    # Get the response from the API
    address_info = _get_extended_address_info(
        postcode=zip_code,
        huisnummer=house_number,
    )

    # Clean the output
    clean_output = _clean_bag_api_output(api_output=address_info)

    return clean_output


if __name__ == "__main__":
    # postcode = "3011DD"
    # huisnummer = "142"

    # postcode = "3039SG"
    # huisnummer = "53"

    # postcode = "3286LT"
    # huisnummer = "37"

    # postcode = "1012 AB"
    # huisnummer = "15"

    # postcode = "3198 NA"
    # huisnummer = "76"

    # postcode = "3198LK"
    # huisnummer = "21"

    # postcode = "3198LB"
    # huisnummer = "87"

    postcode = "3011BH"
    huisnummer = "154"

    info = get_zip_code_info(postcode, huisnummer)

    import pprint

    pprint.pprint(info)
