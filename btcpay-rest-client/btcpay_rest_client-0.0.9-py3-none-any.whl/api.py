import os
import sys
import base64
import pprint
import code
import logging
import json
from datetime import datetime, timedelta

# Module Imports
import requests
from requests.auth import HTTPBasicAuth


class BTCPayServerAPIClient(object):
    def __init__(self, btcpay_url):
        self.base_url = btcpay_url

        # Store auth header
        self.auth_header = None
        self.active_store_id = None

    @classmethod
    def login_basic(cls, btcpay_url, username, password):
        uname = os.getenv("BTCPayUser")
        upass = os.getenv("BTCPayPass")

        # Exit if any creds missing
        if not any([uname, upass]):
            print("No Credentials Available!")
            print("Must export BTCPayUser and BTCPayPass before running this script.")
            sys.exit(-1)

        acode = f"{uname}:{upass}".encode()
        header_key = base64.b64encode(acode).decode()
        headers = {
            "Authorization": f"Basic {header_key}",
            "Content-Type": "application/json",
        }

        cls.auth_header = headers

        btcpay = cls.whoami(cls.auth_header)
        print(btcpay)
        return cls

    @classmethod
    def login_token(cls, btcpay_url, token):
        instance = cls(btcpay_url=btcpay_url)
        headers = {
            "Authorization": f"token {token}",
            "Content-Type": "application/json",
        }
        instance.auth_header = headers
        return instance

    def set_store_id(self, store_id):
        self.active_store_id = store_id

    def get_token(self, label, plist=["unrestricted"]):
        if plist != None:
            permissions = plist

        payload = {
            "label": label,
            "permissions": permissions,
        }

        # Obtain the API Key
        url = f"{self.base_url}/api/v1/api-keys"
        r = requests.post(url, headers=self.basic_header, json=payload)
        print(r.text)
        print(f"API Key Status Code: {r.status_code}")
        new_token = r.json()["apiKey"]

        # Test API Key
        header = {"Authorization": f"token {new_token}"}
        url = f"{self.base_url}/api/v1/api-keys/current"
        r = requests.get(url, headers=header)

        self.token_header = header
        if self.token_header == None:
            return False
        return True

    def get_current_key(self):
        url = f"{self.base_url}/api/v1/api-keys/current"
        r = requests.get(url, headers=self.token_header)
        try:
            key = r.json()
            return key
        except Exception as e:
            print(e)
            return None

    # ***** STORES APIs *****
    def create_new_store(self, store_name):
        # Create New Store
        payload = {
            "name": store_name,
            "website": "https://test.io",
            "invoiceExpiration": 900,
            "monitoringExpiration": 3600,
            "speedPolicy": "HighSpeed",
            "lightningDescriptionTemplate": "pay me really fast",
            "paymentTolerance": 0,
            "anyoneCanCreateInvoice": False,
            "requiresRefundEmail": False,
            "lightningAmountInSatoshi": False,
            "lightningPrivateRouteHints": False,
            "onChainWithLnInvoiceFallback": False,
            "redirectAutomatically": False,
            "showRecommendedFee": True,
            "recommendedFeeBlockTarget": 1,
            "defaultLang": "en",
            "htmlTitle": "Test!",
            "networkFeeMode": "MultiplePaymentsOnly",
            "payJoinEnabled": False,
            "defaultPaymentMethod": "BTC",
        }

        url = f"{self.base_url}/api/v1/stores"
        r = requests.post(url, headers=self.auth_header, json=payload)

        sc = r.status_code
        print(f"STATUS CODE: {sc}")
        return r.json()

    def list_stores(self):
        # List Stores
        url = f"{self.base_url}/api/v1/stores"
        r = requests.get(url, headers=self.auth_header)
        return r.json()

    # ***** INVOICE APIs *****
    def get_invoice_url(self, invoice_id):
        return f"{self.base_url}/i/{invoice_id}"

    def create_invoice(self, request_data):
        required_fields = {'currency', 'metadata', 'checkout', 'amount'}
        optional_fields = set()
        allowed_fields = required_fields | optional_fields
        if required_fields <= request_data.keys() <= allowed_fields:
            pass
        else:
            print("Missing fields")
            print(f"Required: {required_fields}")
            print(f"Optional: {optional_fields}")
            raise ValueError("Input fields missing or too many included")
        url = f"{self.base_url}/api/v1/stores/{self.active_store_id}/invoices"
        print(url)
        create_invoice = requests.post(
            url=url,
            data=json.dumps(request_data),
            headers=self.auth_header,
        )
        print(create_invoice.status_code)
        if create_invoice.status_code != 200:
            print("There was a problem creating invoice")
            print(create_invoice.status_code)
            print(create_invoice.text)
            raise ValueError(create_invoice.text)

        request_result = create_invoice.json()
        return request_result    

    def get_invoice(self, invoice_id):
        url = f"{self.base_url}/api/v1/stores/{self.active_store_id}/invoices/{invoice_id}"
        req = requests.get(
            url=url,
            headers=self.auth_header,
        )
        if req.status_code != 200:
            print(req.status_code)
            print(req.content)
            raise ValueError("Didn't get a good response from btcpay. Can't process.")
        return req.json()

    def get_invoice_payment_methods(self, payment_id):
        url = f"{self.base_url}/api/v1/stores/{self.active_store_id}/invoices/{payment_id}/payment-methods"
        print(url)
        get_invoice_methods = requests.get(
            url=url,
            headers=self.auth_header,
        )
        return get_invoice_methods.json()

    # ***** PAYMENT REQUEST APIs *****
    def get_pay_request_url(self, payment_request_id):
        return f"{self.base_url}/payment-requests/{payment_request_id}"

    def create_payment_request(self, request_data):
        """
        """
        required_fields = {'amount'}
        optional_fields = {'title', 'currency', 'email', 'description', 'expiryDate', 'allowCustomPaymentAmounts'}
        allowed_fields = required_fields | optional_fields
        if required_fields <= request_data.keys() <= allowed_fields:
            pass
        else:
            print("Missing fields")
            print(f"Required: {required_fields}")
            print(f"Optional: {optional_fields}")
            raise ValueError("Input fields missing or too many included")

        url = f"{self.base_url}/api/v1/stores/{self.active_store_id}/payment-requests"
        print(url)
        req = requests.post(
            url=url,
            data=json.dumps(request_data),
            headers=self.auth_header,
        )
        if req.status_code != 200:
            print("There was a problem creating payment request")
            print(req.status_code)
            print(req.text)
            raise ValueError(req.text)

        request_result = req.json()
        return request_result

    def get_payment_request(self, payment_request_id):
        url = f"{self.base_url}/api/v1/stores/{self.active_store_id}/payment-requests/{payment_request_id}"
        req = requests.get(
            url=url,
            headers=self.auth_header,
        )
        if req.status_code != 200:
            print(req.status_code)
            print(req.content)
            raise ValueError("Didn't get a good response from btcpay. Can't process.")
        return req.json()


    # ***** WEBHOOK APIs *****
    def webhooks_get(self):
        url = f"{self.base_url}/api/v1/stores/{self.active_store_id}/webhooks"
        print(url)
        req = requests.get(
            url=url,
            headers=self.auth_header,
        )
        return req.json()

    def webhooks_get_by_id(self, webhook_id):
        url = f"{self.base_url}/api/v1/stores/{self.active_store_id}/webhooks/{webhook_id}"
        print(url)
        req = requests.get(
            url=url,
            headers=self.auth_header,
        )
        return req.json()

    def webhooks_create(self, url):
        url = f"{self.base_url}/api/v1/stores/{self.active_store_id}/webhooks"
        print(url)
        events = [
            "InvoiceCreated", "InvoiceReceivedPayment", "InvoiceProcessing",
            "InvoiceExpired", "InvoiceSettled", "InvoiceInvalid"
        ]
        payload = {
            "enabled": True,
            "automaticRedelivery": True,
            "url": url,
            "authorizedEvents": {
                "everything": False,
                "specificEvents": events
            },
            # "secret": 
        }
        req = requests.post(
            url=url,
            headers=self.auth_header,
            json=payload
        )
        return req.json()


    def webhooks_update(self):
        pass

    def webhooks_delete(self, webhook_id):
        url = f"{self.base_url}/api/v1/stores/{self.active_store_id}/webhooks/{webhook_id}"
        print(url)
        req = requests.delete(
            url=url,
            headers=self.auth_header,
        )
        return req.json()

   # ***** HEALTH APIs *****
    def health(self):
        url = f"{self.base_url}/api/v1/health"
        print(url)
        req = requests.get(
            url=url,
            headers=self.auth_header,
        )
        return req.json()

   # ***** ServerInfo APIs *****
    def server_info(self):
        url = f"{self.base_url}/api/v1/server/info"
        print(url)
        req = requests.get(
            url=url,
            headers=self.auth_header,
        )
        return req.json()

    # ***** User APIs *****
    def current_user(self):
        # Get ME
        url = f"{self.base_url}/api/v1/users/me"
        r = requests.get(url, headers=self.auth_header)

        if r.status_code == 200:
            return r.json()
        sc = r.status_code
        print(f"STATUS CODE: {sc}")
        return r.text

    def create_new_user(self, uname, upass, isAdmin=False):
        # Create New Account
        payload = {"email": uname, "password": upass, "isAdministrator": isAdmin}
        url = f"{self.base_url}/api/v1/users"
        r = requests.post(url, headers=self.auth_header, json=payload)

        sc = r.status_code
        print(f"STATUS CODE: {sc}")
        if sc == 403:
            print("Error: Permissions Issue")
            return
        return r.json()

    def delete_user(self, user_id):
        url = f"{self.base_url}/v1/users/{user_id}"
        print(url)
        response = requests.delete(
            url=url,
            headers=self.auth_header,
        )
        if response.status_code != 200:
            print(response.status_code)
            print(response.text)
            return False
        return True


    def internal_node_info(self, header=None):
        if header is None:
            header = self.token_header

        # Get Lightning Node Info
        cryptoCode = "BTC"
        url = f"{self.base_url}/api/v1/server/lightning/{cryptoCode}/info"
        r = requests.get(url, headers=header)

        sc = r.status_code
        print(f"STATUS CODE: {sc}")
        return r.text

    def internal_node_connect(self, node_uri, header=None):
        if header is None:
            header = self.token_header

        # Connect Lightning Node
        cryptoCode = "BTC"
        url = f"{self.base_url}/api/v1/server/lightning/{cryptoCode}/connect"
        payload = {"nodeURI": node_uri}
        r = requests.post(url, headers=header, json=payload)

        sc = r.status_code
        print(f"STATUS CODE: {sc}")
        return r.text

    def internal_node_address(self, header=None):
        if header is None:
            header = self.token_header

        # Get Lightning Node On-Chain Address
        cryptoCode = "BTC"
        url = f"{self.base_url}/api/v1/server/lightning/{cryptoCode}/address"
        r = requests.post(url, headers=header)

        sc = r.status_code
        print(f"STATUS CODE: {sc}")
        return r.text


if __name__ == "__main__":
    a = BTCPayServerAPIClient()
    a.login()
    code.interact(local=locals())
