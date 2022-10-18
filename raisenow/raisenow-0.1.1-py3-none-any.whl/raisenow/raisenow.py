import datetime
import json
from pprint import pprint
from typing import List

import urllib3

# API documentation : https://developer.raisenow.com/docs/api/

API_BASE_URL = "https://api.raisenow.com"
UTF8 = "utf-8"
YMD = "%Y-%m-%d"
YMDHMS = "%Y-%m-%d %H:%M:%S"

# Commission fee Fairgive 2.5%* no VAT 10.40
# Commission fee RaiseNow 2.5%** incl. 7.7% VAT CHF 0.74 10.40
# Commission fee RaiseNow CHF 0.25 per transaction** incl. 7.7% VAT CHF 0.05 0.75


class RaiseNowConnector:
    """This class represents a connection to the RaiseNow API."""

    def __init__(self, merchant_config: str, merchant_id: str, username: str, password: str) -> None:
        self.TRANSACTION_SEARCH_URL = f"{API_BASE_URL}/epayment/api/{merchant_id}/transactions/search"
        self.TRANSACTION_STATUS_URL = f"{API_BASE_URL}/epayment/api/transaction/status"
        self.MERCHANT_PARAMETERS_URL = f"{API_BASE_URL}/epayment/api/transaction/merchant-params"
        self.merchant_config = merchant_config
        self.merchant_id = merchant_id
        self.username = username
        self.password = password
        self.poolmanager = urllib3.PoolManager()
        self.auth_header = urllib3.make_headers(basic_auth=f"{self.username}:{self.password}")

    def get(self, url: str, fields: dict = {}) -> urllib3.response.HTTPResponse:
        return self.poolmanager.request("GET", url=url, headers=self.auth_header, fields=fields)


class Transaction:
    def __init__(self, data: dict) -> None:
        self.id = str(data.get("epp_transaction_id")).upper()
        self.amount = data.get("amount") / 100
        self.currency = str(data.get("currency_identifier")).upper()
        self.status = str(data.get("last_status")).upper()
        self.created = datetime.datetime.fromtimestamp(int(data.get("created")))
        self.payment_method = str(data.get("payment_method_identifier")).upper()

    def __repr__(self) -> str:
        return f"Transaction: {self.id} {self.created} {self.currency} {self.amount:.2f} {self.status} {self.created} {self.payment_method}"


class Customer:
    def __init__(self, data: dict) -> None:
        self.firstname = str(data.get("stored_customer_firstname", "")).strip().title()
        self.lastname = str(data.get("stored_customer_lastname", "")).strip().title()
        self.civility = data.get("stored_customer_salutation", "").lower()
        self.email = data.get("stored_customer_email", "")
        self.street = str(data.get("stored_customer_street", "")).strip()
        self.street_no = str(data.get("stored_customer_street_number", "")).strip()
        self.street_no = "" if self.street_no in self.street else self.street_no
        self.city = str(data.get("stored_customer_city", "")).strip()
        self.postal_code = str(data.get("stored_customer_zip_code", "")).strip()
        self.country = data.get("stored_customer_country", "")
        self.need_donation_receipt = data.get("stored_customer_donation_receipt", "") == "true"
        self.message = data.get("stored_customer_message", "")

    @property
    def address(self) -> str:
        return f"{self.street} {self.street_no}\n{self.country} {self.postal_code} {self.city}"

    @property
    def salutation(self):
        if self.civility == "ms":
            return "Madame"
        elif self.civility == "mr":
            return "Monsieur"
        return ""

    def __repr__(self) -> str:
        return f"{self.salutation}\n{self._firstname} {self.lastname} ({self.email})\n{self.address}\n{self.message}\n{self.need_donation_receipt} | {self.token}"

    def as_xls_row(self) -> str:
        return f"{self.salutation}\t{self._firstname}\t{self.lastname}\t{self.email}\t{self.street} {self.street_no}\t" + f"{self.country}\t" + f"{self.postal_code} {self.city}\t{self.message}\t{self.need_donation_receipt}"


class TransactionDetails:
    def __init__(self, data: dict) -> None:
        self.id = str(data.get("epp_transaction_id")).upper()
        self.amount = data.get("amount") / 100
        self.currency = str(data.get("currency")).upper()
        self.created = datetime.datetime.strptime(data.get("created"), YMDHMS)
        self.creditable = str(data.get("creditable", "false")) == "true"
        self.credited_at = datetime.datetime.strptime(data.get("credited_at"), YMDHMS) if self.creditable else ""
        self.payment_method = data.get("payment_method", "")

        self.customer = Customer(data)
        self.history = [Status(_) for _ in data.get("status")]

    @property
    def paid_via(self) -> str:
        if self.payment_method == "ECA":
            return "MasterCard"
        elif self.payment_method == "PEF":
            return "Postfinance"
        elif self.payment_method == "TWI":
            return "Twint"
        return "???"

    @staticmethod
    def xls_header() -> str:
        header = [
            "Transaction ID",
            "Montant",
            "Monnaie",
            "Date",
            "Date valeur",
            "Creditable",
            "Méthode",
            "Salutation",
            "Prénom",
            "Nom",
            "Email",
            "Adresse",
            "Localité",
            "Pays",
            "Remerciement souhaité",
            "Message",
        ]
        return ";".join(header)

    @property
    def xls_row(self) -> str:
        data = [
            self.id,
            f"{self.amount:.2f}",
            self.currency,
            str(self.created),
            str(self.credited_at),
            "Oui" if self.creditable else "Non",
            self.paid_via,
            self.customer.salutation,
            self.customer.firstname,
            self.customer.lastname,
            self.customer.email,
            f"{self.customer.street} {self.customer.street_no}",
            f"{self.customer.postal_code} {self.customer.city}",
            self.customer.country,
            "Oui" if self.customer.need_donation_receipt == True else "Non",
            self.customer.message,
        ]
        result = ";".join(data)
        return result


class Status:
    def __init__(self, data: dict) -> None:
        self.status = str(data.get("statusName")).upper()
        self.stamp = datetime.datetime.fromtimestamp(int(data.get("timestamp")))

    def __repr__(self) -> str:
        return f"Status: {self.stamp} {self.status} "


class RaiseNowRequest:
    def __init__(self, connector: RaiseNowConnector) -> None:
        self.connector = connector

    def get_transactions(self, date_from: datetime.date = None, date_to: datetime.date = None, status: str = None) -> List[Transaction]:
        fields = {
            "filters[0][field_name]": "test_mode",
            "filters[0][type]": "term",
            "filters[0][value]": "false",
        }
        if date_from:
            fields.update(
                {
                    "filters[1][field_name]": "created",
                    "filters[1][type]": "date_range",
                    "filters[1][from]": date_from.strftime(YMD),
                    "filters[1][to]": date_to.strftime(YMD) if date_to else date_from.strftime(YMD),
                }
            )

        if status:
            fields.update(
                {
                    "filters[2][field_name]": "last_status",
                    "filters[2][type]": "term",
                    "filters[2][value]": status,
                }
            )

        response = self.connector.get(self.connector.TRANSACTION_SEARCH_URL, fields=fields)

        if response.status != 200:
            return []

        try:
            data = json.loads(response.data.decode(UTF8)).get("result").get("transactions")
            return [Transaction(_) for _ in data]
        except:
            return []

    def get_transaction_details(self, transaction_id: str) -> TransactionDetails:
        fields = {
            "transaction-id": transaction_id,
            "merchant-config": self.connector.merchant_config,
        }

        response = self.connector.get(self.connector.TRANSACTION_STATUS_URL, fields=fields)

        if response.status != 200:
            return None

        data: dict = json.loads(response.data.decode(UTF8))
        return TransactionDetails(data)

    def get_merchant_parameters(self, transaction_id: str):
        fields = {
            "transaction-id": transaction_id,
            "merchant-config": self.connector.merchant_config,
        }
        response = self.connector.get(self.connector.MERCHANT_PARAMETERS_URL, fields=fields)

        if response.status != 200:
            return None

        pprint(json.loads(response.data.decode(UTF8)))


