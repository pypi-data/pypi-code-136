from src.botstudio_sdk.api.bag.code import _change_keys_from_dict, _clean_bag_api_output


def test__change_keys():
    dict_to_change = {
        "adresregel_1": "Stationsplein 15",
        "adresregel_2": "1012 AB  AMSTERDAM",
        "bouwjaar": ["1889"],
        "gebruiksdoelen": ["bijeenkomstfunctie"],
        "huisletter": "nvt",
        "huisnummer": 15,
        "huisnummertoevoeging": "nvt",
        "oppervlakte": 56725,
        "type_object": "Verblijfsobject",
        "woonplaats": "Stationsplein",
    }

    new_dict = _change_keys_from_dict(dictonary=dict_to_change)
    assert new_dict == {
        "adresregel_1": "Stationsplein 15",
        "adresregel_2": "1012 AB  AMSTERDAM",
        "bouwjaar": ["1889"],
        "gebruiksdoelen": ["bijeenkomstfunctie"],
        "huisletter": "nvt",
        "huisnummer": 15,
        "huisnummertoevoeging": "nvt",
        "oppervlakte": 56725,
        "type_object": "Verblijfsobject",
        "woonplaats": "Stationsplein",
    }
    assert dict_to_change == {
        "adresregel_1": "Stationsplein 15",
        "adresregel_2": "1012 AB  AMSTERDAM",
        "bouwjaar": ["1889"],
        "gebruiksdoelen": ["bijeenkomstfunctie"],
        "huisletter": "nvt",
        "huisnummer": 15,
        "huisnummertoevoeging": "nvt",
        "oppervlakte": 56725,
        "type_object": "Verblijfsobject",
        "woonplaats": "Stationsplein",
    }

    assert new_dict["type_object"] == "Verblijfsobject"
    assert new_dict["type_object"] == dict_to_change["type_object"]

    assert new_dict["adresregel_1"] == "Stationsplein 15"
    assert new_dict["adresregel_1"] == dict_to_change["adresregel_1"]

    assert new_dict["adresregel_2"] == "1012 AB  AMSTERDAM"
    assert new_dict["adresregel_2"] == dict_to_change["adresregel_2"]

    assert new_dict["bouwjaar"] == ["1889"]
    assert new_dict["bouwjaar"] == dict_to_change["bouwjaar"]

    assert new_dict["gebruiksdoelen"] == ["bijeenkomstfunctie"]
    assert new_dict["gebruiksdoelen"] == dict_to_change["gebruiksdoelen"]

    assert new_dict["huisletter"] == "nvt"


def test__clean_api_output():
    api_output = {
        "_embedded": {
            "adressen": [
                {
                    "_links": {
                        "adresseerbaarObject": {
                            "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/verblijfsobjecten/0363010012072677"
                        },
                        "nummeraanduiding": {
                            "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/nummeraanduidingen/0363200012072975"
                        },
                        "openbareRuimte": {
                            "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/openbareruimten/0363300000005036"
                        },
                        "panden": [
                            {
                                "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/panden/0363100012185598"
                            }
                        ],
                        "self": {
                            "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/adressenuitgebreid/0363200012072975"
                        },
                        "woonplaats": {
                            "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/woonplaatsen/3594"
                        },
                    },
                    "adresregel5": "Stationsplein 15",
                    "adresregel6": "1012 AB  AMSTERDAM",
                    "adresseerbaarObjectGeometrie": {
                        "punt": {
                            "coordinates": [121838.439, 487951.782, 0.0],
                            "type": "Point",
                        }
                    },
                    "adresseerbaarObjectIdentificatie": "0363010012072677",
                    "adresseerbaarObjectStatus": "Verblijfsobject in " "gebruik",
                    "gebruiksdoelen": ["bijeenkomstfunctie"],
                    "huisnummer": 15,
                    "korteNaam": "Stationsplein",
                    "nummeraanduidingIdentificatie": "0363200012072975",
                    "oorspronkelijkBouwjaar": ["1889", 0],
                    "openbareRuimteIdentificatie": "0363300000005036",
                    "openbareRuimteNaam": "Stationsplein",
                    "oppervlakte": 56725,
                    "pandIdentificaties": ["0363100012185598"],
                    "postcode": "1012AB",
                    "typeAdresseerbaarObject": "Verblijfsobject",
                    "woonplaatsIdentificatie": "3594",
                    "woonplaatsNaam": "Amsterdam",
                }
            ]
        },
        "_links": {
            "self": {
                "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/adressenuitgebreid?postcode=1012+AB&huisnummer=15&exacteMatch=False&pageSize=100"
            }
        },
    }

    clean_output = _clean_bag_api_output(api_output=api_output)
    assert clean_output == [
        {
            "adresregel_1": "Stationsplein 15",
            "adresregel_2": "1012 AB  AMSTERDAM",
            "bouwjaar": "1889, 0",
            "gebruiksdoelen": "bijeenkomstfunctie",
            "huisletter": "",
            "huisnummer": "15",
            "huisnummertoevoeging": "",
            "oppervlakte": "56725",
            "straatnaam": "Stationsplein",
            "type_object": "Verblijfsobject",
            "woonplaats": "Amsterdam",
        }
    ]

    api_output = {
        "_embedded": {
            "adressen": [
                {
                    "_links": {
                        "adresseerbaarObject": {
                            "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/verblijfsobjecten/0611010000508342"
                        },
                        "nummeraanduiding": {
                            "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/nummeraanduidingen/0611200000608342"
                        },
                        "openbareRuimte": {
                            "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/openbareruimten/0611300000312876"
                        },
                        "panden": [
                            {
                                "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/panden/0611100000408245"
                            }
                        ],
                        "self": {
                            "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/adressenuitgebreid/0611200000608342"
                        },
                        "woonplaats": {
                            "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/woonplaatsen/2371"
                        },
                    },
                    "adresregel5": "Schenkeldijk 37",
                    "adresregel6": "3286 LT  KLAASWAAL",
                    "adresseerbaarObjectGeometrie": {
                        "punt": {
                            "coordinates": [89652.0, 419507.0, 0.0],
                            "type": "Point",
                        }
                    },
                    "adresseerbaarObjectIdentificatie": "0611010000508342",
                    "adresseerbaarObjectStatus": "Verblijfsobject in " "gebruik",
                    "gebruiksdoelen": ["woonfunctie"],
                    "huisnummer": 37,
                    "korteNaam": "Schenkeldijk",
                    "nummeraanduidingIdentificatie": "0611200000608342",
                    "oorspronkelijkBouwjaar": ["1920"],
                    "openbareRuimteIdentificatie": "0611300000312876",
                    "openbareRuimteNaam": "Schenkeldijk",
                    "oppervlakte": 84,
                    "pandIdentificaties": ["0611100000408245"],
                    "postcode": "3286LT",
                    "typeAdresseerbaarObject": "Verblijfsobject",
                    "woonplaatsIdentificatie": "2371",
                    "woonplaatsNaam": "Klaaswaal",
                },
                {
                    "_links": {
                        "adresseerbaarObject": {
                            "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/verblijfsobjecten/0611010000513311"
                        },
                        "nummeraanduiding": {
                            "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/nummeraanduidingen/0611200000613311"
                        },
                        "openbareRuimte": {
                            "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/openbareruimten/0611300000312876"
                        },
                        "panden": [
                            {
                                "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/panden/0611100000408309"
                            }
                        ],
                        "self": {
                            "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/adressenuitgebreid/0611200000613311"
                        },
                        "woonplaats": {
                            "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/woonplaatsen/2371"
                        },
                    },
                    "adresregel5": "Schenkeldijk 37 a",
                    "adresregel6": "3286 LT  KLAASWAAL",
                    "adresseerbaarObjectGeometrie": {
                        "punt": {
                            "coordinates": [89666.0, 419473.0, 0.0],
                            "type": "Point",
                        }
                    },
                    "adresseerbaarObjectIdentificatie": "0611010000513311",
                    "adresseerbaarObjectStatus": "Verblijfsobject in " "gebruik",
                    "gebruiksdoelen": ["woonfunctie"],
                    "huisletter": "a",
                    "huisnummer": 37,
                    "korteNaam": "Schenkeldijk",
                    "nummeraanduidingIdentificatie": "0611200000613311",
                    "oorspronkelijkBouwjaar": ["1954"],
                    "openbareRuimteIdentificatie": "0611300000312876",
                    "openbareRuimteNaam": "Schenkeldijk",
                    "oppervlakte": 43,
                    "pandIdentificaties": ["0611100000408309"],
                    "postcode": "3286LT",
                    "typeAdresseerbaarObject": "Verblijfsobject",
                    "woonplaatsIdentificatie": "2371",
                    "woonplaatsNaam": "Klaaswaal",
                },
            ]
        },
        "_links": {
            "self": {
                "href": "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/adressenuitgebreid?postcode=3286LT&huisnummer=37&exacteMatch=False&pageSize=100"
            }
        },
    }
    clean_output = _clean_bag_api_output(api_output=api_output)
    assert clean_output == [
        {
            "adresregel_1": "Schenkeldijk 37",
            "adresregel_2": "3286 LT  KLAASWAAL",
            "bouwjaar": "1920",
            "gebruiksdoelen": "woonfunctie",
            "huisletter": "",
            "huisnummer": "37",
            "huisnummertoevoeging": "",
            "oppervlakte": "84",
            "straatnaam": "Schenkeldijk",
            "type_object": "Verblijfsobject",
            "woonplaats": "Klaaswaal",
        },
        {
            "adresregel_1": "Schenkeldijk 37 a",
            "adresregel_2": "3286 LT  KLAASWAAL",
            "bouwjaar": "1954",
            "gebruiksdoelen": "woonfunctie",
            "huisletter": "a",
            "huisnummer": "37",
            "huisnummertoevoeging": "",
            "oppervlakte": "43",
            "straatnaam": "Schenkeldijk",
            "type_object": "Verblijfsobject",
            "woonplaats": "Klaaswaal",
        },
    ]
