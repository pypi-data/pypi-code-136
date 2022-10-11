"""
SteamaCo API client
"""
# pylint: disable=too-few-public-methods

import os
import logging
from typing import List, Optional
from datetime import timedelta
import requests
from requests import Timeout
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from pydantic import parse_raw_as
from icecommercialpower.utils import CachedValue
from .errors import CreateTransactionError, ObtainTokenError
from .meter_record import MeterRecord
from .customer_record import CustomerRecord
from .transaction import Transaction

DEFAULT_REQUEST_TIMEOUT = 60


# pylint: disable=too-many-instance-attributes
class SteamaCoClient:
    """
    SteamaCo REST API client
    Handles authentication
    """

    DEFAULT_PAGE_SIZE = 200
    PAGE_SIZE_PARAM_NAME = "page_size"

    _cached_token = CachedValue(ttl=timedelta(minutes=5))

    def __init__(self):
        """
        Initalize environment Steamaco variables
        """
        self._api_url = os.getenv("STEAMACO_API_URL", "https://api.steama.co/")
        self._get_token_path = os.getenv("STEAMACO_AUTH_URL", "get-token/")
        self._get_customers_path = os.getenv("STEAMACO_CUSTOMERS_URL", "customers/")
        self._get_meters_path = os.getenv("STEAMACO_METERS_URL", "meters/")
        self._retry_count = int(os.getenv("STEAMACO_RETRY_COUNT", "5"))
        self._username = os.environ["STEAMACO_USERNAME"]
        self._password = os.environ["STEAMACO_PASSWORD"]
        self._get_all_page_size = int(
            os.getenv("STEAMACO_GET_ALL_PAGE_SIZE", str(self.DEFAULT_PAGE_SIZE))
        )
        self.timeout_sec = int(
            os.getenv("FLUTTERWAVE_TIMEOUT", str(DEFAULT_REQUEST_TIMEOUT))
        )

    def __get_token(self):
        """
        Send request to SteamaCo authentication API
        The token is cached for 5 minutes
        """
        token = SteamaCoClient._cached_token.get_value()
        if token:
            return token

        logging.debug("Getting auth token from SteamaCo API.")
        session = self._get_session()

        try:
            response = session.post(
                self._api_url + self._get_token_path,
                timeout=self.timeout_sec,
                json={"username": self._username, "password": self._password},
            )
        except Exception as ex:
            if isinstance(ex, Timeout):
                logging.exception("Request to SteamaCo API timed out")
                raise

            logging.exception("Unable to communicate with SteamaCo")
            raise ObtainTokenError from ex

        body = response.json()
        if response.status_code != 200:
            error_message = (
                f"Unable to get token from {self._api_url}. "
                "Username: {self.username}, "
                "Status code: {response.status_code}, "
                "Body: {body}"
            )
            logging.error(error_message)
            raise ObtainTokenError(error_message)

        token = "Token " + body["token"]
        SteamaCoClient._cached_token.set_value(token)
        return token

    def _get_session(self) -> requests.Session:
        retry_strategy = Retry(
            total=int(self._retry_count),
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["POST", "GET", "HEAD"],
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()
        session.mount("https://", adapter)
        return session

    def get_customer_by_phone_number(self, phone_number) -> Optional[CustomerRecord]:
        """
        Returns a single customer data identified by phone number
        """
        logging.debug("Sending request to SteamaCo API.")

        matching_customers = self.get_all(
            self._get_customers_path, {"telephone": phone_number}
        )

        if len(matching_customers) == 1:
            return CustomerRecord(**matching_customers[0])

        logging.error("SteamaCo invalid response %s", matching_customers)
        return None

    def get_all(self, path: str, query_params: dict = None) -> List:
        """
        Gets all data from SteamaCo API
        If the result is paged, continues until all data is retrieved

        Args:
            path: Path to the resource
            query_params: (Optional) Query parameters to be added to the request
        """
        logging.debug("Sending request to SteamaCo API.")

        session = self._get_session()
        headers = {"Authorization": self.__get_token()}

        if self._get_all_page_size:
            query_params = query_params or {}
            query_params[self.PAGE_SIZE_PARAM_NAME] = self._get_all_page_size

        try:
            response = session.get(
                f"{self._api_url}{path}",
                timeout=self.timeout_sec,
                headers=headers,
                params=query_params,
            )
        except Timeout:
            logging.exception("Request to SteamaCo API timed out")
            raise

        if response.status_code != 200:
            response.raise_for_status()

        data = []
        response_json = response.json()

        # Steamaco API returns paged data
        # data array is in "results"
        # next page is in "next"
        while response_json:
            if not isinstance(response_json, dict):
                break

            results = response_json.get("results")
            if not results:
                break

            data.extend(results)

            next_url = response_json.get("next")
            if not next_url:
                break

            response = session.get(
                next_url,
                headers=headers,
            )

            if response.status_code != 200:
                response.raise_for_status()

            response_json = response.json()

        return data

    def get_meters(self) -> List[MeterRecord]:
        """
        Gets all meters from SteamaCo API
        """
        return [MeterRecord(**m) for m in self.get_all(self._get_meters_path)]

    def get_customers(self) -> List[CustomerRecord]:
        """
        Gets all customers from SteamaCo API
        """
        return [CustomerRecord(**m) for m in self.get_all(self._get_customers_path)]

    def get_customer_by_id(self, customer_id: int) -> Optional[CustomerRecord]:
        """
        Gets a single customer from SteamaCo API.
        Return None when not found.
        """
        res = self._get(path=f"{self._get_customers_path}{customer_id}")

        if res.status_code == 404:
            return None

        res.raise_for_status()

        json_response = res.json()
        return CustomerRecord(**json_response)

    def get_customer_transactions(
        self, customer_id: int, reference: str = None
    ) -> List[Transaction]:
        """
        Gets transactions for a customer

        Args:
            customer_id: ID of the customer
            reference: Reference of the transaction
        """

        query_params = {}
        if reference:
            query_params["reference"] = reference

        return [
            Transaction(**t)
            for t in self.get_all(
                f"{self._get_customers_path}{customer_id}/transactions/", query_params
            )
        ]

    def _post(
        self, path: str, json: str, query_params: dict = None
    ) -> requests.Response:
        """
        Sends a POST request to SteamaCo API
        """

        full_url = f"{self._api_url}{path}"
        logging.debug("Sending POST request to SteamaCo API at %s.", full_url)

        session = self._get_session()
        headers = {
            "Authorization": self.__get_token(),
            "Content-Type": "application/json",
        }

        try:
            response = session.post(
                full_url,
                timeout=self.timeout_sec,
                headers=headers,
                params=query_params,
                data=json,
            )
        except Timeout:
            logging.exception("Request to SteamaCo API timed out")
            raise

        return response

    def _get(self, path: str, query_params: dict = None) -> requests.Response:
        """
        Sends a GET request to SteamaCo API
        """

        full_url = f"{self._api_url}{path}"
        logging.debug("Sending GET request to SteamaCo API at %s.", full_url)

        session = self._get_session()
        headers = {
            "Authorization": self.__get_token(),
            "Content-Type": "application/json",
        }

        try:
            response = session.get(
                full_url, timeout=self.timeout_sec, headers=headers, params=query_params
            )
        except Timeout:
            logging.exception("Request to SteamaCo API timed out")
            raise

        return response

    def create_customer_transaction(
        self, customer_id: int, transaction: Transaction
    ) -> Transaction:
        """
        Creates a transaction for a customer
        """

        response = self._post(
            f"{self._get_customers_path}{customer_id}/transactions/",
            transaction.json(exclude_defaults=True),
        )

        if response.status_code != 201:
            raise CreateTransactionError(
                f"Failed to create transaction for customer {customer_id}"
                f"with status code {response.status_code} and response {response.text}"
            )

        return parse_raw_as(Transaction, response.text)
