import hashlib
import requests
import json


class Motilal:
    url = "https://uatopenapi.motilaloswal.com/rest/login/v3/authdirectapi"
    headers = {
        "Accept": "application/json",
        "User-Agent": "MOSL/V.1.1.0",
        "ApiKey": "ypdJRIbZkCTHV5Tp",
        "vendorinfo": "T0240",
        "SourceId": "WEB",
        "MacAddress": "00:50:56:BD:F4:0B",
        "ClientLocalIp": "192.168.165.165",
        "ClientPublicIp": "106.193.137.95",
        "osname": "Ubuntu",
        "osversion": "10.0.19041",
        "devicemodel": "AHV",
        "manufacturer": "DELL",
        "productname": "Your Product Name",
        "productversion": "Your Product Version",
        "installedappid": "AppID",
        "browsername": "Chrome",
        "browserversion": "105.0"
    }

    def __init__(self):
        pass

    def generate_token(self):
        # initializing string
        str = "Quant@123ypdJRIbZkCTHV5Tp"

        # encoding GeeksforGeeks using encode()
        # then sending to SHA256()
        result = hashlib.sha256(str.encode())

        data = {
            "userid": "EMUM755714",
            "password": result.hexdigest(),
            "2FA": "25/03/1993"
        }
        response = requests.post(Motilal.url, headers=Motilal.headers, data=json.dumps(data))
        print(response.json())

Motilal().generate_token()