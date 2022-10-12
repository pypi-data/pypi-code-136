import json
import requests
from config import settings
import datamodel as dm
import app 

log = app.Logger()

class K2HolidayApi:
    EXTERNAL_API_BASE_URL = settings["EXTERNAL_API_BASE_URL"]

    @staticmethod
    def api_wrapper_holiday_get(exchange, year):
        try:
            url = f"{K2HolidayApi.EXTERNAL_API_BASE_URL}/holidays/{exchange}/{year}"
            headers = {"Content-Type": "application/json"}
            response = requests.get(url, headers=headers)
            if (response.status_code == 200):
                return response.json()
            else:
                return False
        except Exception as error:
            raise error