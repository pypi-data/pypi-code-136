import requests
import socket
import logging
import json
from .models import GTJAVintexQytResult
from .models import SecuritiesSummary
from .models import Securities
from urllib.parse import urlunparse

formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')

logger = logging.getLogger()
logging_level = logging.DEBUG

logger.setLevel(logging_level)

ch = logging.StreamHandler()
ch.setFormatter(formatter)
ch.setLevel(logging.DEBUG)

logger.addHandler(ch)

fh = logging.FileHandler('gtja_qyt.log', 'a', encoding="utf-8")
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


class GTJAVintexQyt:
    SYSTEM_ID = 79
    PROTOCOL = ""
    HOSTNAME = ""
    PORT = 9129

    HEADERS = {
        "Content-Type": "application/json"
    }

    @staticmethod
    def _get_ip():
        try:
            logger.debug("Trying to get external ip from ipify.org...")
            r = requests.get("https://api.ipify.org?format=json")
            return r.json()["ip"]
        except Exception:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(0)
            try:
                s.connect(('10.254.254.254', 1))
                return s.getsockname()[0]
            except Exception:
                return '127.0.0.1'
            finally:
                s.close()

    def __init__(self, custid: str, auth: str):
        logger.debug("Initializing GTJA Qyt Python lib...")

        self.ip = GTJAVintexQyt._get_ip()
        logger.debug(f"Client ip: {self.ip}.")

        self.customer_id = custid
        self.auth_code = auth

    def qc0020(
            self,
            pag: int = 1,
            rownum: int = 10,
            custid: str = None,
            qc_id: str = None,
            stkcodes: list[str] = None,
            locktype: str = None,
            vc_type: str = None
    ) -> GTJAVintexQytResult:

        path = "/qyt/QC/QC0020"

        payload = {
            "systemInfo": {
                "systemid": GTJAVintexQyt.SYSTEM_ID,
                "ip": self.ip
            },
            "businessInfo": {
                "pag": pag,
                "rownum": rownum
            },
            "auth": self.auth_code
        }

        if custid:
            payload["businessInfo"]["custid"] = custid

        if qc_id:
            payload["businessInfo"]["qc_id"] = qc_id

        if stkcodes:
            payload["businessInfo"]["stkcodes"] = stkcodes

        if locktype:
            payload["businessInfo"]["locktype"] = locktype

        if vc_type:
            payload["businessInfo"]["vc_type"] = vc_type

        url = urlunparse(("http", f"10.184.36.42:9129", path, None, None, None))

        try:
            r = requests.post(url, data=json.dumps(payload), headers=GTJAVintexQyt.HEADERS)
            if r.status_code == 200:
                response = GTJAVintexQytResult(r.content)

                for security_pool in response.json["data"]:
                    response.data.append(
                        Securities(
                            security_pool["firstdroptype"],
                            security_pool["vc_type"],
                            security_pool["qcid"],
                            security_pool["qcname"],
                            security_pool["dropid"],
                            security_pool["market"],
                            security_pool["stkcode"],
                            security_pool["stkname"],
                            security_pool["totalleftqty"],
                            security_pool["totallockqty"],
                            security_pool["startdate"],
                            security_pool["limitdate"],
                            security_pool["reslimit"],
                            security_pool["floorrate"],
                            security_pool["upperrate"],
                            security_pool["relatedcustid"],
                            security_pool["contractid"],
                            security_pool["applyid"]
                        )
                    )

                return response
            else:
                raise
        except Exception as e:
            logger.error("Exception while calling QC0020: " + str(e))

    def qc0021(
            self,
            custid: str,
            pag: int = 1,
            rownum: int = 10,
            market: str = None,
            stkcode: str = None,
            locktype: str = None,
            vctype: str = None
    ) -> GTJAVintexQytResult:
        path = "/qyt/QC/QC0021"

        payload = {
            "systemInfo": {
                "systemid": GTJAVintexQyt.SYSTEM_ID,
                "ip": self.ip
            },
            "businessInfo": {
                "pag": pag,
                "rownum": rownum,
                "custid": custid,
            },
            "auth": self.auth_code
        }

        if market:
            payload["businessInfo"]["market"] = market

        if stkcode:
            payload["businessInfo"]["stkcode"] = stkcode

        if vctype:
            payload["businessInfo"]["vc_type"] = vctype

        if locktype:
            payload["businessInfo"]["locktype"] = locktype

        url = urlunparse(("http", f"10.184.36.23:8080", path, None, None, None))

        try:
            r = requests.post(url, data=json.dumps(payload), headers=GTJAVintexQyt.HEADERS)
            if r.status_code == 200:
                response = GTJAVintexQytResult(r.content)

                for security in response.json["data"]:
                    response.data.append(
                        SecuritiesSummary(
                            security["stkcode"],
                            security["stkname"],
                            security["market"],
                            security["actualleftqty"],
                            security["floorrate"],
                            security["startdate"]
                        )
                    )

                return response
            else:
                raise
        except Exception as e:
            logger.error("Exception while calling QC0021: " + str(e))

