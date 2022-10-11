"""
FlutterWave API client.

We aren't using the official FlutterWave API SDK rave-python
because it's not available for v3 version of the API.
"""
import logging
import json
from datetime import datetime
from enum import Enum
from typing import NamedTuple, Optional
import os

import requests
from requests import Timeout
from requests.sessions import HTTPAdapter, Session

from urllib3.util import Retry


class FwTransactionStatus(str, Enum):
    """FlutterWave transaction status"""

    SUCCESSFUL = "successful"  # terminal state
    ABANDONED = "abandoned"  # terminal state
    PENDING = "pending"  # may change
    CANCELLED = "cancelled"  # terminal state
    VOIDED = "voided"  # terminal state
    FAILED = "failed"  # terminal state


class FwPaymentType(str, Enum):
    """FlutterWave payment type"""

    USSD = "ussd"


class FwTransaction(NamedTuple):
    """FlutterWave transaction"""

    transaction_id: int
    flw_ref: str
    status: FwTransactionStatus
    tx_ref: str
    currency: str
    amount: float
    customer_id: int
    customer_email: str
    customer_phone: str
    customer_name: str
    created_at: datetime
    payment_type: FwPaymentType
    charged_amount: Optional[
        float
    ] = None  # Amount charged by Flutterwave (amount + fees)
    app_fee: Optional[float] = None  # Fee charged by Flutterwave
    merchant_fee: Optional[
        float
    ] = None  # Uncertain what this is. Awaiting clarification from Flutterwave
    """
    amount_settled: Depends on Flutterwave fee settings (charged to customer or to ICE).
    If charged to customer fees are not included, else fees are.
    """
    amount_settled: Optional[float] = None


class FwStartUssdPaymentRequest(NamedTuple):
    """FlutterWave start ussd payment request"""

    tx_ref: str
    account_bank: str
    amount: float
    customer_id: int
    currency: str
    customer_email: str
    customer_phone: str
    customer_name: str


class FwStartUssdPaymentResponse(NamedTuple):
    """FlutterWave start ussd payment response"""

    transaction: FwTransaction
    ussd_code: str
    payment_code: str


class FlutterWaveResponseError(Exception):
    """Raised when FlutterWave API returns an error in message body"""


HTTP_REQUESTS_RETRY_COUNT = 3
DEFAULT_REQUEST_TIMEOUT = 60


def _create_http(retry_on_status_400: bool = False) -> Session:
    """Create HTTP client with retry policy"""
    status_list = [429, 500, 502, 503]
    if retry_on_status_400:
        status_list.append(400)

    retry_strat = Retry(
        total=HTTP_REQUESTS_RETRY_COUNT,
        allowed_methods=["GET", "POST", "HEAD"],
        backoff_factor=1,
        status_forcelist=status_list,
    )
    adapter = HTTPAdapter(max_retries=retry_strat)
    http = requests.Session()
    http.mount("http://", adapter)
    http.mount("https://", adapter)
    return http


class FlutterWaveClient:
    """FlutterWave API client"""

    def __init__(self, secret_key: str):
        self._token = "Bearer " + secret_key
        self._api_endpoint = os.getenv(
            "FLUTTERWAVE_API_ENDPOINT", "https://api.flutterwave.com/v3"
        )

        self.timeout_sec = int(
            os.getenv("FLUTTERWAVE_TIMEOUT", str(DEFAULT_REQUEST_TIMEOUT))
        )

    @classmethod
    def from_env(cls):
        """Construct with the secret key from environment variables"""
        return cls(os.environ["FLUTTERWAVE_SECRET_KEY"])

    def get_transaction_status(self, transaction_id: int) -> FwTransaction:
        """
        Get full transaction information along with the current status.
        https://developer.flutterwave.com/docs/transaction-verification
        """

        resp = _create_http().get(
            f"{self._api_endpoint}/transactions/{transaction_id}/verify",
            timeout=self.timeout_sec,
            headers={"Authorization": self._token},
        )
        resp.raise_for_status()

        body = resp.json()

        if body["status"] != "success":
            raise Exception(body["message"])

        data = body["data"]
        return self._create_fl_transaction_from_response(data)

    def start_ussd_payment(
        self, request: FwStartUssdPaymentRequest
    ) -> FwStartUssdPaymentResponse:
        """
        Starts USSD payment in FlutterWave
        It returns the USSD code and the transaction details
        """

        create_request = json.dumps(
            {
                "tx_ref": request.tx_ref,
                "account_bank": request.account_bank,
                "amount": request.amount,
                "currency": request.currency,
                "email": request.customer_email,
                "phone_number": request.customer_phone,
                "fullname": request.customer_name,
                "meta": {
                    "customer_id": request.customer_id,
                },
            }
        )

        logging.info(
            "Starting USSD payment transaction for tx_ref '%s' with bank '%s', amount '%s', currency '%s', customer_id '%s'",  # pylint: disable=line-too-long
            request.tx_ref,
            request.account_bank,
            request.amount,
            request.currency,
            request.customer_id,
        )

        try:
            resp = _create_http(retry_on_status_400=True).post(
                f"{self._api_endpoint}/charges?type=ussd",
                timeout=self.timeout_sec,
                headers={
                    "Authorization": self._token,
                    "Content-type": "application/json",
                },
                data=create_request,
            )
        except Timeout:
            logging.exception("USSD transaction timed out")
            raise

        body = resp.json()
        logging.info(
            "Response for USSD payment transaction with tx_ref '%s' has status: '%s'",
            request.tx_ref,
            body["status"] if hasattr(body, "status") else "",
        )

        resp.raise_for_status()

        if body["status"] != "success":
            raise FlutterWaveResponseError(body["message"])

        data = body["data"]
        ussd_code = body["meta"]["authorization"]["note"]
        payment_code = data["payment_code"]
        fw_transaction = self._create_fl_transaction_from_response(
            data, customer_id=request.customer_id
        )

        return FwStartUssdPaymentResponse(
            transaction=fw_transaction,
            ussd_code=ussd_code,
            payment_code=payment_code,
        )

    @staticmethod
    def _create_fl_transaction_from_response(
        data: dict, customer_id: int = None
    ) -> FwTransaction:
        customer_id = customer_id or int(data["meta"]["customer_id"])
        customer = data["customer"]

        return FwTransaction(
            transaction_id=int(data["id"]),
            flw_ref=data["flw_ref"],
            amount=float(data["amount"]),
            charged_amount=float(data["charged_amount"]),
            amount_settled=data.get("amount_settled"),
            app_fee=float(data.get("app_fee", 0.0)),
            merchant_fee=float(data.get("merchant_fee", 0.0)),
            currency=data["currency"],
            status=FwTransactionStatus(data["status"]),
            tx_ref=data["tx_ref"],
            customer_id=customer_id,
            customer_email=customer["email"],
            customer_phone=customer["phone_number"],
            customer_name=customer["name"],
            created_at=datetime.strptime(data["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z"),
            payment_type=FwPaymentType(data["payment_type"]),
        )
