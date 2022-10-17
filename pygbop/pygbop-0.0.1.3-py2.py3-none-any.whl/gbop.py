# @Time : 2022-07-08 11:18
# @Author  : Huang.XiaoGang
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# ======================================================
# @Project : python_test
# @FileName: PyGbop
# @Software: PyCharm
import time
import enum
import hmac
import base64
import datetime
import requests
from hashlib import sha256


class BasicAuth(object):
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key


class Method(enum.Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'
    OPTIONS = 'OPTIONS'
    HEAD = 'HEAD'


class GbopApiClient(object):
    LN = "\n"

    def __init__(self, auth: BasicAuth, base_url='', protocol='http://'):
        self.auth = auth
        self.base_url = base_url
        self.protocol = protocol

    def _generate_signature(self, path, method, headers, params):
        query_string = self._get_query_str(params)
        content_array = [method, path, query_string]
        if headers:
            if headers.__contains__("X-Gapi-Ca-Access-Key"):
                content_array.append(headers["X-Gapi-Ca-Access-Key"])
            if headers.__contains__("Date"):
                content_array.append(headers["Date"])
            if headers.__contains__("X-Gapi-Ca-Signed-Headers"):
                custom_headers = headers["X-Gapi-Ca-Signed-Headers"].split(";")
                for custom_header in custom_headers:
                    content_array.append(custom_header + ":" + headers[custom_header])
        content = self.LN.join(content_array) + self.LN
        content = content.encode("utf-8")
        secret_key = self.auth.secret_key.encode("utf-8")
        signature = base64.b64encode(hmac.new(secret_key, content, digestmod=sha256).digest())
        return signature

    def _get_header(self, path, method, params):
        gmt_format = '%a, %d %b %Y %H:%M:%S GMT'
        headers = {
            "X-Gapi-Ca-Timestamp": str(int(round(time.time() * 1000))),
            "X-Gapi-Ca-Algorithm": "hmac-sha256",
            "X-Gapi-Ca-Access-Key": self.auth.access_key,
            "X-Gapi-Ca-Signed-Headers": 'X-Gapi-Ca-Timestamp',
            "Date": datetime.datetime.utcnow().strftime(gmt_format),
            "Host": self.base_url,
        }
        headers["X-Gapi-Ca-Signature"] = self._generate_signature(path, method, headers, params)
        return headers

    def _get_query_str(self, params):
        if not params:
            return ''
        queries_dic = sorted(params)
        queries = []
        for k in queries_dic:
            if isinstance(params[k], list):
                params[k].sort()
                for i in params[k]:
                    queries.append(f'{k}={i}')
            else:
                queries.append(f'{k}={params[k]}')
        return "&".join(queries)

    def _get_url_str(self, path, params):
        query_str = self._get_query_str(params)
        format_string = f"{self.base_url}{path}?{query_str}" if query_str else f"{self.base_url}{path}"
        url = self.protocol + format_string
        return url

    def execute(self, method=Method.GET, path='', params={}, data={}):
        url = self._get_url_str(path, params)
        headers = self._get_header(path, method.value, params)
        res = requests.request(method.value, url, headers=headers, data=data)
        return res.content
