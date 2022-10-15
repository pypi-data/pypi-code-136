from typing import Iterable

import requests


class PyTranslo:
    def __init__(self, token: str, api_domain: str = "translo.p.rapidapi.com"):
        self._token = token
        self._api_domain = api_domain
        self._api_url = f"https://{self._api_domain}/api/v3/"

    def translate(self,
                  text: str | Iterable,
                  to_lang: str,
                  from_lang: str = "",
                  fast: bool = False) -> str | dict:
        """
        Translate function

        :param text: text of translate
        :param from_lang: from the language of the text
        :param to_lang: to language of the text
        :param fast: fast mode translate
        :return:
        """
        if not isinstance(text, str):
            # Text can prompt multiple sentences to translate
            text = "".join([f"&text={line}" for line in text])

        response = requests.post(
            f"{self._api_url}translate?{text}",
            data=f"text={text}&from={from_lang}&to={to_lang}"
                 f"&fast={str(fast).lower()}".encode('utf-8'),

            headers={"content-type": "application/x-www-form-urlencoded",
                     "X-RapidAPI-Host": self._api_domain,
                     "X-RapidAPI-Key": self._token})

        json = response.json()

        try:
            return json["translated_text"]
        except KeyError:
            raise Exception(json["error"])

    def detect(self, text: str) -> str:
        response = requests.get(
            f"{self._api_url}detect",
            headers={
                "content-type": "application/x-www-form-urlencoded",
                "X-RapidAPI-Host": self._api_domain,
                "X-RapidAPI-Key": self._token},
            params={"text": text})

        json = response.json()

        try:
            return json["lang"]
        except KeyError:
            raise Exception(json["message"])
