import logging
import http.client
import json
from enum import Enum
from json import JSONDecodeError
from socket import error as socket_error
from pyGuardPoint.guardpoint_utils import Stopwatch, ConvertBase64
import time


class GuardPointAuthType(Enum):
    BASIC = 1
    BEARER_TOKEN = 2


log = logging.getLogger(__name__)


class GuardPointConnection:

    def __init__(self, host, port, auth, user, pwd, key):
        self.host = host
        self.port = port
        if not isinstance(auth, GuardPointAuthType):
            raise ValueError("Parameter authType must be instance of GuardPointAuthType")
        self.authType = auth
        self.user = user
        self.pwd = pwd
        self.key = key
        self.baseurl = f"http://{host}:{port}"
        self.token = None
        self.token_issued = 0
        self.token_expiry = 0
        log.info(f"GP10 server connection: {host}:{port}")
        self.connection = http.client.HTTPConnection(self.host, self.port)

    def gp_json_query(self, method, url, json_body: dict = '', headers=None):
        if self.authType == GuardPointAuthType.BASIC:
            auth_str = "Basic " + ConvertBase64.encode(f"{self.user}:{self.key}")
        elif self.authType == GuardPointAuthType.BEARER_TOKEN:
            if self.token is None:
                code, auth_body = self._new_token()
                if code != 200:
                    return code, auth_body
            if self.token_expiry < (time.time() - (30 * 60)):  # If Token will expire within 30 minutes
                code, auth_body = self._renew_token()
                if code != 200:
                    return code, auth_body
            if self.token_expiry < time.time():
                code, auth_body = self._new_token()
                if code != 200:
                    return code, auth_body

            auth_str = f"Bearer {self.token}"
        else:
            raise NotImplementedError("Selected authentication mechanism not available.")

        return self._query(method, url, json_body, headers, auth_str)

    def _query(self, method, url, json_body: dict = None, headers=None, auth_str=None):
        raw_body = ''
        if json_body:
            if not isinstance(json_body, dict):
                raise ValueError("Variable 'json_body' must be of type dict.")
            else:
                raw_body = json.dumps(json_body)

        headers = headers or {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        if auth_str:
            headers['Authorization'] = auth_str

        log.debug(f"Request data: host={self.host}:{self.port}, {method}, {url}, {headers}, {raw_body}")
        timer = Stopwatch().start()

        self.connection.request(method, url, raw_body, headers)

        timer.stop()
        response = self.connection.getresponse()
        body = response.read().decode("utf-8")
        # log.debug("Response hdrs: " + str(response.headers))
        # log.debug("Response data: " + response.read().decode("utf-8"))
        # log.debug(f"Response \'{response.getcode()}\' received in {timer.print()}")

        # Try to convert body into json
        try:
            json_body = json.loads(body)
        except JSONDecodeError:
            json_body = None
        except Exception as e:
            log.error(e)
            json_body = None

        return response.getcode(), json_body

    def _new_token(self):
        log.info("Requesting new token")
        payload = {"username": self.user,
                   "password": self.pwd}
        url = self.baseurl + "/api/Token/"
        return self._query_token(url, payload)

    def _renew_token(self):
        log.info("Renewing token")
        payload = {"oldToken": self.token}
        url = self.baseurl + "/api/Token/RenewToken"
        return self._query_token(url, payload)

    def _query_token(self, url, json_payload):
        code, json_body = self._query("POST", url, json_payload)

        if code == 200:
            try:
                self.token = json_body['token']
                token_dict = json.loads(ConvertBase64.decode(self.token.split(".")[1]))
                self.token_issued = token_dict['iat']
                self.token_expiry = token_dict['exp']
            except JSONDecodeError:
                json_body = None
            except Exception as e:
                log.error(e)
                json_body = None

        return code, json_body
