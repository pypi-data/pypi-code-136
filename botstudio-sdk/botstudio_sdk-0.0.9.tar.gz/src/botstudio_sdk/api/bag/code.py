"""
More info:
    https://github.com/lvbag/BAG-API/blob/master/Features/paginering.feature
    https://www.kadaster.nl/documents/1953498/2762071/Productbeschrijving+BAG+API+Individuele+Bevragingen.pdf/cf35e5fd-ddb0-bc82-ffc5-6e7877a58ffa?t=1638438344305
    https://lvbag.github.io/BAG-API/Technische%20specificatie/#/Adres%20uitgebreid/zoekAdresUitgebreid
    https://lvbag.github.io/BAG-API/Technische%20specificatie/
"""

import requests


URL_PRODUCTIE = "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/"


def _adres_uitgebreid(
    api_key: str,
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
        "X-Api-Key": api_key,
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

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise ConnectionError(
            f"There was not a good api connection established. Status code: {response.status_code}"
        )


def _change_keys(dict_to_change: dict) -> dict:

    old_new_keys = {
        "oorspronkelijkBouwjaar": "bouwjaar",
        "typeAdresseerbaarObject": "type_object",
        "openbareRuimteNaam": "woonplaats",
        "adresregel6": "adresregel_2",
        "adresregel5": "adresregel_1",
    }

    for old_key, new_key in old_new_keys.items():
        dict_to_change = _change_key(dict_to_change, old_key, new_key)

    return dict_to_change


def _change_key(dict_with_keys, old_key, new_key):

    if old_key in dict_with_keys.keys():
        dict_with_keys[new_key] = dict_with_keys.pop(old_key)
    return dict_with_keys


def get_zip_code_info(
    api_key: str,
    zip_code: str,
    house_number: str,
) -> dict:

    adress_info = _adres_uitgebreid(
        api_key=api_key,
        postcode=zip_code,
        huisnummer=house_number,
    )

    item_list = [
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
    ]

    zip_code_info = dict()
    zip_code_info["adressen"] = list()

    for item in adress_info["_embedded"]["adressen"]:
        adres_dict = dict()

        for key in item_list:
            if key in item.keys():
                adres_dict[key] = item[key]
            else:
                adres_dict[key] = "nvt"

        adres_dict = _change_keys(dict_to_change=adres_dict)

        zip_code_info["adressen"].append(adres_dict)

    return zip_code_info


if __name__ == "__main__":
    key_productie = "l73550f472b0e943ceb15e8071e7bb1462"

    # postcode = "3011DD"
    # huisnummer = "142"

    postcode = "3039SG"
    huisnummer = "53"

    # postcode = "3011BH"
    # huisnummer = "154"

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

    info = get_zip_code_info(key_productie, postcode, huisnummer)

    import pprint
    pprint.pprint(info)
