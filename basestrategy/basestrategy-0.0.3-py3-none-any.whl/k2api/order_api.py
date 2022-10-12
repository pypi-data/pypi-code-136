import json
import requests
from config import settings
import datamodel as dm


class K2OrderApi:
    INTERNAL_API_BASE_URL = settings["INTERNAL_API_BASE_URL"]

    @staticmethod
    def api_wrapper_order_post(order_data):
        try:
            url = f"{K2OrderApi.INTERNAL_API_BASE_URL}/order"
            headers = {"Content-Type": "application/json"}
            order_data = json.dumps(order_data)
            response = requests.post(url, order_data, headers=headers)
            if (response.status_code == 200):
                response = json.loads(response.text)
                order = dm.PydanticOrder(**(response))
                return order
            return False
        except Exception as error:
            raise error

    @staticmethod
    def api_wrapper_order_put(order_data):
        try:
            url = f"{K2OrderApi.INTERNAL_API_BASE_URL}/order"
            headers = {"Content-Type": "application/json"}
            order_data = json.dumps(order_data)
            response = requests.put(url, order_data, headers=headers)
            if (response.status_code == 200):
                return response
            else:
                return False
        except Exception as error:
            raise error

    @staticmethod
    def api_wrapper_order_get(order_id):
        try:
            url = f"{K2OrderApi.INTERNAL_API_BASE_URL}/order/{order_id}"
            headers = {"Content-Type": "application/json"}
            response = requests.get(url, headers=headers)
            if (response.status_code == 200):
                response = json.loads(response.text)
                return dm.PydanticOrder(**response)
            return False
        except Exception as error:
            raise error

    @staticmethod
    def api_wrapper_order_cancel_patch(order_id):
        try:
            url = f"{K2OrderApi.INTERNAL_API_BASE_URL}/cancel_order/{order_id}"
            headers = {"Content-Type": "application/json"}
            response = requests.patch(
                url, headers=headers)
            if (response.status_code == 200):
                return response
            else:
                return False
        except Exception as error:
            raise error

    @staticmethod
    def api_wrapper_modify_sl_order_price_patch(order_id, order_modify_data):
        try:
            url = f"{K2OrderApi.INTERNAL_API_BASE_URL}/modify_sl_order_price/{order_id}"
            headers = {"Content-Type": "application/json"}
            order_modify_data = json.dumps(order_modify_data)
            response = requests.patch(
                url, data=order_modify_data, headers=headers)
            if (response.status_code == 200):
                response = json.loads(response.text)
                return dm.PydanticOrder(**response)
            return False
        except Exception as error:
            raise error
