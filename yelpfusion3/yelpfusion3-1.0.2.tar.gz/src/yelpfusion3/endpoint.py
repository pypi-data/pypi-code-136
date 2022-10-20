from abc import abstractmethod
from typing import Dict, List
from urllib.parse import quote, urlencode

import requests
from pydantic import BaseModel, validator
from requests import Response

from yelpfusion3.model import Model
from yelpfusion3.settings import Settings


class SupportedLocales:
    """
    A collection of locales supported by the Yelp Fusion API.
    """

    locales: List[Dict] = [
        {
            "code": "cs_CZ",
            "country": "Czech Republic",
            "language": "Czech",
        },
        {
            "code": "da_DK",
            "country": "Denmark",
            "language": "Danish",
        },
        {
            "code": "de_AT",
            "country": "Austria",
            "language": "German",
        },
        {
            "code": "de_CH",
            "country": "Switzerland",
            "language": "German",
        },
        {
            "code": "de_DE",
            "country": "Germany",
            "language": "German",
        },
        {
            "code": "en_AU",
            "country": "Australia",
            "language": "English",
        },
        {
            "code": "en_BE",
            "country": "Belgium",
            "language": "English",
        },
        {
            "code": "en_CA",
            "country": "Canada",
            "language": "English",
        },
        {
            "code": "en_CH",
            "country": "Switzerland",
            "language": "English",
        },
        {
            "code": "en_GB",
            "country": "United Kingdom",
            "language": "English",
        },
        {
            "code": "en_HK",
            "country": "Hong Kong",
            "language": "English",
        },
        {
            "code": "en_IE",
            "country": "Republic of Ireland",
            "language": "English",
        },
        {
            "code": "en_MY",
            "country": "Malaysia",
            "language": "English",
        },
        {
            "code": "en_NZ",
            "country": "New Zealand",
            "language": "English",
        },
        {
            "code": "en_PH",
            "country": "Philippines",
            "language": "English",
        },
        {
            "code": "en_SG",
            "country": "Singapore",
            "language": "English",
        },
        {
            "code": "en_US",
            "country": "United States",
            "language": "English",
        },
        {
            "code": "es_AR",
            "country": "Argentina",
            "language": "Spanish",
        },
        {
            "code": "es_CL",
            "country": "Chile",
            "language": "Spanish",
        },
        {
            "code": "es_ES",
            "country": "Spain",
            "language": "Spanish",
        },
        {
            "code": "es_MX",
            "country": "Mexico",
            "language": "Spanish",
        },
        {
            "code": "fi_FI",
            "country": "Finland",
            "language": "Finnish",
        },
        {
            "code": "fil_PH",
            "country": "Philippines",
            "language": "Filipino",
        },
        {
            "code": "fr_BE",
            "country": "Belgium",
            "language": "French",
        },
        {
            "code": "fr_CA",
            "country": "Canada",
            "language": "French",
        },
        {
            "code": "fr_CH",
            "country": "Switzerland",
            "language": "French",
        },
        {
            "code": "fr_FR",
            "country": "France",
            "language": "French",
        },
        {
            "code": "it_CH",
            "country": "Switzerland",
            "language": "Italian",
        },
        {
            "code": "it_IT",
            "country": "Italy",
            "language": "Italian",
        },
        {
            "code": "ja_JP",
            "country": "Japan",
            "language": "Japanese",
        },
        {
            "code": "ms_MY",
            "country": "Malaysia",
            "language": "Malay",
        },
        {
            "code": "nb_NO",
            "country": "Norway",
            "language": "Norwegian",
        },
        {
            "code": "nl_BE",
            "country": "Belgium",
            "language": "Dutch",
        },
        {
            "code": "nl_NL",
            "country": "The Netherlands",
            "language": "Dutch",
        },
        {
            "code": "pl_PL",
            "country": "Poland",
            "language": "Polish",
        },
        {
            "code": "pt_BR",
            "country": "Brazil",
            "language": "Portuguese",
        },
        {
            "code": "pt_PT",
            "country": "Portugal",
            "language": "Portuguese",
        },
        {
            "code": "sv_FI",
            "country": "Finland",
            "language": "Swedish",
        },
        {
            "code": "sv_SE",
            "country": "Sweden",
            "language": "Swedish",
        },
        {
            "code": "tr_TR",
            "country": "Turkey",
            "language": "Turkish",
        },
        {
            "code": "zh_HK",
            "country": "Hong Kong",
            "language": "Chinese",
        },
        {
            "code": "zh_TW",
            "country": "Taiwan",
            "language": "Chinese",
        },
    ]

    @staticmethod
    def codes() -> List[str]:
        """
        Returns a list of all supported locale codes.

        :return: A list containing just the supported locale codes.
        :rtype: List[str]
        """
        return [locale["code"] for locale in SupportedLocales.locales]


class Endpoint(BaseModel):
    """
    Basic base class for all endpoint implementations.
    """

    class Config:
        anystr_strip_whitespace = True
        min_anystr_length = 1
        validate_assignment = True

    _path: str

    @property
    def url(self) -> str:
        """
        Constructs a URL to the business search endpoint with the given query parameters.

        :return: Yelp Fusion API 3 endpoint URL.
        :rtype: str
        """
        non_none_fields = {key: value for key, value in self.dict().items() if value is not None}
        parameters = urlencode(query=non_none_fields, quote_via=quote)
        settings = Settings()
        if parameters:
            return f"{settings.base_url}{self._path}?{parameters}"
        return f"{settings.base_url}{self._path}"

    @abstractmethod
    def get(self) -> Model:
        pass  # pragma: no cover

    def _get(self) -> Response:
        return requests.get(url=self.url, headers=Settings().headers)

    @validator("locale", check_fields=False)
    def _check_locale(cls, v: str) -> str:
        """
        Validates that the locale is supported by Yelp Fusion API 3.
        See https://www.yelp.com/developers/documentation/v3/supported_locales

        :param v: Locale of the response body.
        :type v: str
        :raise ValueError: "v" is an unsupported locale value.
        :return: "v" if it's a supported locale.
        :rtype: str
        """
        if v not in SupportedLocales.codes():
            raise ValueError("Unsupported 'locale' value.")
        return v
