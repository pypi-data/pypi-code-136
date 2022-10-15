"""
arthub_api.api
~~~~~~~~~~~~~~

This module encapsulates the ArtHub OpenAPI.
For detailed interface doc: "https://arthub.aa.com/user_manual/index.html"
"""
import logging
import requests
from . import utils
from . import models
from . import _internal_utils
from xml.etree import ElementTree


def _node_query_metas(simplified_meta=True):
    metas = [
        "name",
        "file_format",
        "node_type",
        "permission_mask",
        "direct_child_count",
        "capacity",
        "parent_id"
    ]
    if not simplified_meta:
        metas += [
            "full_path_id",
            "full_path_name",
            "confirmed_asset_id",
            "preview_url",
            "status",
            "crc64",
            "updated_date"
        ]
    return metas


class APIResponse(object):
    def __init__(self, http_response, network_connection_failed=False):
        self._http_response = http_response
        self._network_connection_failed = network_connection_failed
        self._direct_result = None

        self.api_result_code = -9999
        self.api_item_result_code = -9999
        self.api_error_message = "Unknown"
        self.results = {}
        self.errors = {}

        self._preprocess()

    def _preprocess(self):
        if self._network_connection_failed:
            return
        if self._http_response is None:
            return
        if not self._http_response.ok:
            logging.error("[API] request \"%s\" failed, code: %d" % (
                self._http_response.url, self._http_response.status_code))
            return
        try:
            # parse api response
            _data = self._http_response.json()
            # parse result code
            self.api_result_code = _data["code"]
            # parse result
            self.parse_items(_data.get("result"), self.results)
            # parse error
            self.parse_items(_data.get("error"), self.errors)
            # parse error message
            self._parse_error()

        except Exception:
            logging.error("[API] parsing response exception, \"%s\"" % self._http_response.text)

    def _parse_error(self):
        if not self.errors:
            return
        e = self.errors.get(next(iter(self.errors)))
        if e is None:
            return
        if type(e) is not dict:
            self.api_error_message = e
        else:
            item_message = e.get("message")
            item_error_code = e.get("error_code")
            if item_message is not None:
                self.api_error_message = item_message
            if item_error_code is not None:
                self.api_item_result_code = item_error_code

    @property
    def url(self):
        if self._http_response is None:
            return ""
        return self._http_response.url

    @property
    def direct_result(self):
        return self._direct_result

    def first_result(self, key=None):
        if key:
            return self.results.get(0).get(key)
        else:
            return self.results.get(0)

    def set_direct_result_by_key(self, direct_result_key):
        if self.is_succeeded():
            self._direct_result = self.first_result(direct_result_key)

    def set_direct_result(self, direct_result):
        self._direct_result = direct_result

    @staticmethod
    def parse_items(items_in, items_out):
        if items_in is None:
            return
        t = type(items_in)
        # example: "result": 123
        if t != list and t != dict:
            items_out[0] = items_in
            return

        items_list = []
        if t == list:
            # example: "result": []
            items_list = items_in
        else:
            items_ = items_in.get("items")
            if type(items_) == list:
                # example: "result": {"items": []}
                items_list = items_
            else:
                # example: "result": {}
                items_out[0] = items_in
                return

        for i, item in enumerate(items_list):
            if type(item) != dict:
                items_out[i] = item
                continue
            param_index = item.get("param_index")
            if type(param_index) == int:
                items_out[param_index] = item
            else:
                items_out[i] = item

    def is_http_request_succeeded(self):
        if not self._http_response:
            return False
        return True

    def is_succeeded(self):
        r"""Batch call, all return success.
        """

        if not self.is_http_request_succeeded():
            return False
        return self.api_result_code == 0

    def is_partial_succeeded(self):
        r"""Batch call, partial success.
        """

        if not self.is_http_request_succeeded():
            return False
        return self.api_result_code == 1

    def is_api_authentication_failed(self):
        r"""Authentication failed.
        """

        if not self.is_http_request_succeeded():
            return False
        return self.api_result_code == -1

    def is_no_permission(self):
        r"""No access to target node, please contact the administrator.
        """

        if not self.is_http_request_succeeded():
            return False
        return self.api_result_code == -19 or self.api_item_result_code == -19

    def is_node_not_exist(self):
        r"""Node does not exist.
        """

        if not self.is_http_request_succeeded():
            return False
        return self.api_result_code == -10 or self.api_item_result_code == -10

    def error_message(self):
        if self._network_connection_failed:
            return "network connection failed"
        if not self._http_response.ok:
            return "http request failed, code: %d" % self._http_response.status_code
        if self.is_succeeded():
            return "no error"
        if self.is_api_authentication_failed():
            return "authentication failed"
        if self.is_no_permission():
            return "no permission"
        if self.is_node_not_exist():
            return "node not exist"

        return self.api_error_message


class OpenAPI(object):
    def __init__(self, config):
        r"""Used to call ArtHub openapi.
        for detailed interface doc: "https://arthub.qq.com/user_manual/index.html"

        :param config: from arthub_api.config.
        """

        self._config = config
        self._token_type = 'arthubtoken'
        self._token = ""
        self._cookies = None
        self._api_version_depot = "v2"
        self._api_version_gateway = "v2"
        self._api_version_account = "v3"
        self._cached_account_name = ""
        self._cached_password = ""
        self._auto_login = False

    @property
    def is_login(self):
        return self._token

    @property
    def config(self):
        return self._config

    def set_token(self, token):
        r"""Optional pre-action for calling api.

        :param token: str, a token obtained by API:login.
        """

        self._token_type = "arthubtoken"
        self._token = token

    def set_public_token(self, token):
        r"""Optional pre-action for calling api.

        :param token: str, a public token issued by the administrator.
        """

        self._token_type = "publictoken"
        self._token = token

    def set_cookies(self, cookie):
        r"""Optional pre-action for calling api.

        :param cookie: str or dict, cookie from browser.
        """

        if type(cookie) is str:
            self._cookies = utils.parse_cookies(cookie)
        elif type(cookie) is dict:
            self._cookies = cookie

    def _depot_url(self, asset_hub, api_method):
        return "%s//%s/%s/data/openapi/%s/core/%s" % (
            self.config["http_scheme"], self.config["host"], asset_hub, self._api_version_depot, api_method)

    def _gateway_url(self, api_method):
        return "%s//%s/gateway/gateway/openapi/%s/core/%s" % (
            self.config["http_scheme"], self.config["host"], self._api_version_gateway, api_method)

    def _account_url(self, api_method):
        return "%s//%s/account/account/openapi/%s/core/%s" % (
            self.config["http_scheme"], self.config["host"], self._api_version_account, api_method)

    def _try_auto_login(self):
        # Use the cached account password to log in again to get the token
        if not self._auto_login:
            return False
        if len(self._cached_password) == 0 or len(self._cached_account_name) == 0:
            return False
        return self.login(self._cached_account_name, self._cached_password).is_succeeded()

    def _make_api_request(self, url, data=None, method='POST', content_type='application/json',
                          try_login_on_expired=True):
        # set token to headers
        headers = {}
        if self._token:
            headers[self._token_type] = self._token
        headers["content-type"] = content_type

        # send request
        try:
            res = requests.request(method=method, url=url, headers=headers, json=data, cookies=self._cookies)
        except Exception as e:
            logging.error("[API] send request \"%s\" exception: %s" % (url, e))
            response = APIResponse(None, True)
            return response

        response = APIResponse(res)
        if response.is_api_authentication_failed() and try_login_on_expired:
            # Try to log in again due to authentication failure
            if self._try_auto_login():
                response = self._make_api_request(url, data, method, content_type, try_login_on_expired=False)

        return response

    def login(self, account_name, password, set_auto_login=True):
        r"""Login by email/mobile and password. You can visit https://arthub.qq.com to register.

        :param account_name: str. email or mobile.
        :param password: str. If you forget, visit https://arthub.qq.com/reset-password to reset
        :param set_auto_login: (optional) bool. After successful login, save the account and password,
               and login automatically after the login status expires
        :rtype: arthub_api.APIResponse
        """

        url = self._account_url("login")
        req_payload = {
            "account_name": account_name,
            "account_type": "mobile" if account_name.isdigit() else "email",
            "password": password,
            "current_time": utils.current_milli_time(),
            "nounce": utils.get_random_string(8),
            "oauth_type": "password",
            "login_type": "arthub_token"
        }
        res = self._make_api_request(url, req_payload, try_login_on_expired=False)
        if res.is_succeeded():
            r = res.results.get(0)
            token = r["arthub_token"]
            self.set_token(token)

            self._auto_login = set_auto_login
            # save account and password for auto login
            if set_auto_login:
                self._cached_account_name = account_name
                self._cached_password = password

        return res

    def get_account_detail(self):
        r"""Get the detail of user's account.

        :rtype: arthub_api.APIResponse
        """

        url = self._account_url("get-account-detail-by-account-name")
        return self._make_api_request(url, method="GET")

    def get_ticket(self):
        r"""Get the ticket to request websocket.

        :rtype: arthub_api.APIResponse
        """

        url = self._account_url("get-ticket")
        return self._make_api_request(url, method="GET")

    def get_last_access_location_by_account(self):
        r"""Get the user's last access location.

        :rtype: arthub_api.APIResponse
        """

        url = self._account_url("get-last-access-location-by-account")
        return self._make_api_request(url, method="GET")

    def depot_get_node_brief_by_ids(self, asset_hub, ids, simplified_meta=False):
        r"""Get the brief of node by id in depot.

        :param asset_hub: str. Example: "trial".
        :param ids: list<int>. Example: [1234].
        :param simplified_meta: (optional) bool. Just basic meta, lower bandwidth consumption.
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "get-node-brief-by-id")
        req_payload = {
            "ids": ids,
            "meta": _node_query_metas(simplified_meta)
        }
        return self._make_api_request(url, req_payload)

    def depot_get_download_signature(self, asset_hub, nodes):
        r"""Get the download url of asset in depot.

        :param asset_hub: str. Example: "trial".
        :param nodes: list<node (dict) >. Example: [{"object_id": 110347249345024, "object_meta": "origin_url"}].
                {
                    "object_id": int, node id,
                    "object_meta": str, Example: "origin_url"|"preview_url"
                }
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "get-download-signature")
        req_payload = {
            "items": nodes
        }
        res = self._make_api_request(url, req_payload)
        signed_url = "%s%s" % (self.config["http_scheme"], res.first_result("signed_url"))
        res.set_direct_result(signed_url)
        return res

    def depot_get_upload_signature(self, asset_hub, nodes):
        r"""Get the upload url of asset in depot.

        :param asset_hub: str. Example: "trial".
        :param nodes: list<node (dict) >. Example: [{"object_id": 110347249345024, "object_meta": "origin_url"}].
                {
                    "object_id": int, node id,
                    "object_meta": str, Example: "origin_url"|"preview_url",
                    "file_name": file name to upload
                }
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "get-upload-signature")
        req_payload = {
            "items": nodes
        }
        res = self._make_api_request(url, req_payload)
        signed_url = "%s%s" % (self.config["http_scheme"], res.first_result("signed_url"))
        res.set_direct_result(signed_url)
        return res

    def depot_create_empty_file(self, asset_hub, asset_id, file_name):
        r"""Create the empty file on storage of asset in depot.

        :param asset_hub: str. Example: "trial".
        :param asset_id: int. Example: 1234.
        :param file_name: str. Example: "1.jpg".
        :rtype: arthub_api.Result::data: {"origin_url": str}
        """

        api_res = self.depot_get_upload_signature(asset_hub, [{
            "object_id": asset_id,
            "object_meta": "origin_url",
            "file_name": file_name
        }])
        if not api_res.is_succeeded():
            return models.failure_result("get upload signature url of %d to create empty file failed, %s" % (
                asset_id, api_res.error_message()))
        signed_upload_url = api_res.direct_result
        origin_url = api_res.first_result()["origin_url"]

        # send signature url
        try:
            upload_res = requests.put(url=signed_upload_url, headers={"content-length": str(0)})
        except Exception as e:
            return models.failure_result("request \"%s\" exception, %s" % (
                signed_upload_url, e))
        if not upload_res.ok:
            return models.failure_result("upload to \"%s\" failed, status code: %d" % (
                signed_upload_url, upload_res.status_code))

        return models.success_result({
            "origin_url": origin_url
        })

    def depot_get_create_multipart_upload_signature(self, asset_hub, nodes):
        r"""Get the multipart upload url to visit S3 in depot.

        :param asset_hub: str. Example: "trial".
        :param nodes: list<node (dict) >. Example: [{"object_id": 110347249345024, "object_meta": "origin_url"}].
                {
                    "object_id": int, node id,
                    "object_meta": str, Example: "origin_url"|"preview_url",
                    "file_name": file name to upload
                }
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "create-multipart-upload-signature")
        req_payload = {
            "items": nodes
        }
        res = self._make_api_request(url, req_payload)
        signed_url = "%s%s" % (self.config["http_scheme"], res.first_result("signed_url"))
        res.set_direct_result(signed_url)
        return res

    def depot_get_multipart_upload_id(self, asset_hub, asset_id, file_name):
        r"""Get the multipart upload id to in depot.

        :param asset_hub: str. Example: "trial".
        :param asset_id: int. Example: 1234.
        :param file_name: str. Example: "1.jpg".

        :rtype: arthub_api.Result::data: {"upload_id": str, "origin_url": str}
        """

        # create multipart upload task
        api_res = self.depot_get_create_multipart_upload_signature(asset_hub, [{
            "object_id": asset_id,
            "object_meta": "origin_url",
            "file_name": file_name
        }])
        if not api_res.is_succeeded():
            return models.failure_result("get create multipart upload signature url of %d failed, %s" % (
                asset_id, api_res.error_message()))
        signed_url = api_res.direct_result
        origin_url = api_res.first_result()["origin_url"]

        # send signature url
        res = requests.post(signed_url,
                            headers={"content-type": _internal_utils.get_content_type_from_file_name(file_name)})
        if not res or not res.ok:
            error_message = "request S3 multipart upload id failed, url: %s, code: %d" % (signed_url, res.status_code)
            logging.error("[API] %s" % error_message)
            return models.failure_result(error_message)

        try:
            xml_tree = ElementTree.fromstring(res.content)
            upload_id = xml_tree.find("UploadId").text
        except Exception as e:
            error_message = "parsing S3 multipart upload id from \"%s\" exception, %s" % (res.text, e)
            logging.error("[API] %s" % error_message)
            return models.failure_result(error_message)
        return models.success_result({
            "origin_url": origin_url,
            "upload_id": upload_id
        })

    def depot_get_part_upload_signature(self, asset_hub, nodes):
        r"""Get the S3 part upload url.

        :param asset_hub: str. Example: "trial".
        :param nodes: list<node (dict) >. Example: [{"object_id": 110347249345024, "object_meta": "origin_url"}].
                {
                    "object_id": int, node id,
                    "object_meta": str, Example: "origin_url"|"preview_url",
                    "file_name": file name to upload,
                    "upload_id": str, upload id of S3 multipart upload task,
                    "part_number": int, upload part number, begin with 1
                }
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "upload-part-signature")
        req_payload = {
            "items": nodes
        }
        res = self._make_api_request(url, req_payload)
        signed_url = "%s%s" % (self.config["http_scheme"], res.first_result("signed_url"))
        res.set_direct_result(signed_url)
        return res

    def depot_get_complete_multipart_upload_signature(self, asset_hub, nodes):
        r"""Get the multipart upload url to visit S3 in depot.

        :param asset_hub: str. Example: "trial".
        :param nodes: list<node (dict) >. Example: [{"object_id": 110347249345024, "object_meta": "origin_url"}].
                {
                    "object_id": int, node id,
                    "object_meta": str, Example: "origin_url"|"preview_url",
                    "file_name": file name to upload,
                    "upload_id": str, upload id of S3 multipart upload task
                }
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "complete-multipart-upload-signature")
        req_payload = {
            "items": nodes
        }
        res = self._make_api_request(url, req_payload)
        signed_url = "%s%s" % (self.config["http_scheme"], res.first_result("signed_url"))
        res.set_direct_result(signed_url)
        return res

    def depot_complete_multipart_upload(self, asset_hub, asset_id, file_name, upload_id, etag_data):
        r"""Get the multipart upload id to in depot.

        :param asset_hub: str. Example: "trial".
        :param asset_id: int. Example: 1234.
        :param file_name: str. Example: "1.jpg".
        :param upload_id: str. upload id of S3 multipart upload task

        :rtype: arthub_api.Result::data: {"upload_id": str, "origin_url": str}
        """

        # complete multipart upload task
        api_res = self.depot_get_complete_multipart_upload_signature(asset_hub, [{
            "object_id": asset_id,
            "object_meta": "origin_url",
            "file_name": file_name,
            "upload_id": upload_id
        }])
        if not api_res.is_succeeded():
            return models.failure_result("get complete multipart upload signature url of %d failed, %s" % (
                asset_id, api_res.error_message()))
        signed_url = api_res.direct_result

        # send signature url
        res = requests.post(signed_url,
                            headers={"content-type": "application/xml"}, data=etag_data)
        if not res or not res.ok:
            error_message = "request complete S3 multipart upload failed, url: %s, code: %d" % (
                signed_url, res.status_code)
            logging.error("[API] %s" % error_message)
            return models.failure_result(error_message)
        return models.success_result(None)

    def depot_get_child_node_count(self, asset_hub, ids, query_filters=[], is_recursive=False):
        r"""Get the child node count of node in depot.

        :param asset_hub: str. Example: "trial".
        :param ids: list<int>. Example: [1234].
        :param query_filters: (optional) list<query_filter (dict) >. Example: [{"meta": "type", "condition": "x != project"}].
                {
                    "meta": filters meta,
                    "condition": filters condition
                }
        :param is_recursive: (optional) bool, Whether to query recursively
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "get-child-node-count")
        req_payload = {
            "ids": ids,
            "filter": query_filters,
            "is_recursive": is_recursive
        }
        res = self._make_api_request(url, req_payload)
        res.set_direct_result_by_key("count")
        return res

    def depot_get_child_node_id_in_range(self, asset_hub, parent_id, offset, count, query_filters=[],
                                         is_recursive=False):
        r"""Get the child node count of node in depot.

        :param asset_hub: str. Example: "trial".
        :param parent_id: int. Example: 1234.
        :param offset: int. range offset: 0.
        :param count: int. range count: 100.
        :param query_filters: list<query_filter (dict) >. Example: [{"meta": "type", "condition": "x != project"}].
                {
                    "meta": filters meta,
                    "condition": filters condition
                }
        :param is_recursive: (optional) bool, Whether to query recursively
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "get-child-node-id-in-range")
        req_payload = {
            "parent_id": parent_id,
            "offset": offset,
            "count": count,
            "filter": query_filters,
            "is_recursive": is_recursive
        }
        res = self._make_api_request(url, req_payload)
        res.set_direct_result_by_key("nodes")
        return res

    def depot_get_node_brief_by_path(self, asset_hub, root_id, path, simplified_meta=False):
        r"""Get the brief of node by path in depot.

        :param asset_hub: str. Example: "trial".
        :param root_id: int. Example: 1234.
        :param path: str. Example: "1/2.jpg".
        :param simplified_meta: (optional) bool. Just basic meta, lower bandwidth consumption.
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "get-node-brief-by-path")

        path = path.replace('\\', '/')
        req_payload = {
            "root_id": root_id,
            "path": [path],
            "meta": _node_query_metas(simplified_meta)
        }
        return self._make_api_request(url, req_payload)

    def depot_delete_node_by_ids(self, asset_hub, ids):
        r"""delete the node in depot.

        :param asset_hub: str. Example: "trial".
        :param ids: list<int>. Example: [1234].
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "delete-node-by-id")
        req_payload = {
            "ids": ids
        }
        return self._make_api_request(url, req_payload)

    def depot_move_node(self, asset_hub, ids, other_parent_id):
        r"""move the node in depot.

        :param asset_hub: str. Example: "trial".
        :param ids: list<int>. Example: [1234, 3456].
        :param other_parent_id: int.
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "move-node")
        req_payload = {
            "ids": ids,
            "other_parent_id": other_parent_id
        }
        return self._make_api_request(url, req_payload)

    def depot_create_project(self, asset_hub, name, parent_id, return_existing_id=True, show_detail_column=True,
                             show_version_column=True,
                             watermark=False):
        r"""create project in depot.

        :param asset_hub: str. Example: "trial".
        :param name: str. project name. Example: "test".
        :param parent_id: int. depot root id. Example: 304942678017.
        :param return_existing_id: (optional) bool.
        :param show_detail_column: (optional) bool.
        :param show_version_column: (optional) bool.
        :param watermark: (optional) bool.
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "create-project")
        req_payload = [{
            "name": name,
            "parent_id": parent_id,
            "return_existing_id": return_existing_id,
            "show_detail_column": show_detail_column,
            "show_version_column": show_version_column,
            "watermark": watermark,
        }]

        res = self._make_api_request(url, req_payload)
        res.set_direct_result_by_key("id")
        return res

    def depot_create_directory(self, asset_hub, payloads):
        r"""create dirs in depot.

        :param asset_hub: str. Example: "trial".
        :param payloads: list<payload (dict) >.
                {
                    "parent_id": parent dir id,
                    "name": name of new dir to create,
                    "allowed_rename": allow renaming new dir to "name(<index>)" when a dir with the same name exists,
                    "return_existing_id": returns the id of an existing dir with the same name
                }
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "create-directory")
        req_payload = {
            "items": payloads
        }

        res = self._make_api_request(url, req_payload)
        res.set_direct_result_by_key("id")
        return res

    def depot_create_asset(self, asset_hub, payloads):
        r"""create assets in depot.

        :param asset_hub: str. Example: "trial".
        :param payloads: list<payload (dict) >.
                {
                    "parent_id": parent dir id,
                    "name": name of new asset to create,
                    "add_new_version": add a version when an asset with the same name exists,
                }
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "create-asset")
        req_payload = {
            "items": payloads
        }
        res = self._make_api_request(url, req_payload)
        res.set_direct_result_by_key("id")
        return res

    def depot_create_multi_asset(self, asset_hub, payloads):
        r"""create multi asset (version container) in depot.

        :param asset_hub: str. Example: "trial".
        :param payloads: list<payload (dict) >.
                {
                    "parent_id": parent dir id,
                    "name": name of new multi asset to create,
                }
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "create-multi-asset")
        req_payload = {
            "items": payloads
        }
        return self._make_api_request(url, req_payload)

    def depot_update_asset_by_id(self, asset_hub, payloads):
        r"""update metas of asset in depot.

        :param asset_hub: str. Example: "trial".
        :param payloads: list<payload (dict) >.
                {
                    "id": int, node id,
                    "name": str, node name,
                    "origin_url": origin url,
                    "description": description of node
                }
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "update-asset-by-id")
        req_payload = {
            "items": payloads
        }
        return self._make_api_request(url, req_payload)

    def depot_convert_asset(self, asset_hub, asset_files, asset_ids):
        r"""convert asset in depot.

        :param asset_hub: str. Example: "trial".
        :param asset_files: list<str>. Example: ["//ahs_cos_guangzhou_1/assethub-trial-1258344700/cospri/download/110347249345/110347249345067/1.png"].
        :param asset_ids: list<int>. Example: [110347249345067].
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "convert-asset")
        req_payload = {
            "asset_files": asset_files,
            "asset_ids": asset_ids
        }
        return self._make_api_request(url, req_payload)

    def depot_create_tsa(self, asset_hub, asset_id, company, description, title, tsa_info):
        r"""convert asset in depot.

        :param asset_hub: str. Example: "trial".
        :param asset_id: int. Example: 110347249345071.
        :param company: str. Example: "Tencent".
        :param description: str. Example: "New weapon".
        :param title: str. Example: "Christmas".
        :param tsa_info: str. Example: "Characters; Web design".
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "create-tsa")
        req_payload = {
            "asset_id": asset_id,
            "company": company,
            "description": description,
            "title": title,
            "tsa_info": tsa_info
        }
        return self._make_api_request(url, req_payload)

    def depot_add_asset_tag(self, asset_hub, asset_id, tag_name):
        r"""add tags to asset node in depot.

        :param asset_hub: str. Example: "trial".
        :param asset_id: int. Example: 110347249345071.
        :param tag_name: list<str>. Example: ["tag_1", "tag_2"].
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "add-asset-tag")
        req_payload = {
            "asset_id": asset_id,
            "tag_name": tag_name
        }
        return self._make_api_request(url, req_payload)

    def depot_update_directory_by_id(self, asset_hub, payloads):
        r"""update metas of directory in depot .

        :param asset_hub: str. Example: "trial".
        :param payloads: list<payload (dict) >.
                {
                    "id": int, node id,
                    "name": str, node name,
                    "origin_url": origin url,
                    "description": description of node
                }
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "update-directory-by-id")
        req_payload = {
            "items": payloads
        }
        return self._make_api_request(url, req_payload)

    def depot_update_project_by_id(self, asset_hub, payloads):
        r"""update metas of project in depot .

        :param asset_hub: str. Example: "trial".
        :param payloads: list<payload (dict) >.
                {
                    "id": int, node id,
                    "name": str, node name,
                    "origin_url": origin url,
                    "description": description of node
                }
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "update-project-by-id")
        req_payload = {
            "items": payloads
        }
        return self._make_api_request(url, req_payload)

    def depot_update_multi_asset_by_id(self, asset_hub, payloads):
        r"""update metas of multi asset in depot .

        :param asset_hub: str. Example: "trial".
        :param payloads: list<payload (dict) >.
                {
                    "id": int, node id,
                    "name": str, node name,
                    "origin_url": origin url,
                    "description": description of node
                }
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "update-multi-asset-by-id")
        req_payload = {
            "items": payloads
        }
        return self._make_api_request(url, req_payload)

    def depot_get_root_id(self, asset_hub):
        r"""get the depot root id of asset hub.

        :param asset_hub: str. Example: "trial".
        :rtype: arthub_api.APIResponse
        """

        url = self._depot_url(asset_hub, "get-depot-id")
        return self._make_api_request(url)

    def reset_config(self, config):
        self._config = config
