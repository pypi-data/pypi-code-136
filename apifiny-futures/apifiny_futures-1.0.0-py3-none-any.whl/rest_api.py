#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  rest_api.py
@Time    :  2022/07/07 15:25:07
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

import json
import time

import requests

from .lib.utils import gen_signature, prepare_params, rest_url


class API:
    def __init__(self, venue="BINANCE", key=None, secret=None, recv_window=None):
        self.secret_key_id = key
        self.secret_key = secret
        self.venue = venue
        self.test = False
        self.recv_window = recv_window
        self.session = requests.Session()

    def http_request(self, method, path, params=None, unified_url=True):
        base_url = rest_url(unified_url, self.venue)
        url = base_url + path
        rep = None
        header = {}
        if method.lower() == 'get':
            if params:
                params["timestamp"] = int(time.time() * 1000)
                params["recvWindow"] = self.recv_window
                params_string = prepare_params(params)
                header["apiKey"] = self.secret_key_id
                header["signature"] = gen_signature(self.secret_key, params_string)
            rep = self.session.get(url, params=params, headers=header)
            # print(rep.url)

        if method.lower() == 'post':
            params["timestamp"] = int(time.time() * 1000)
            params["recvWindow"] = self.recv_window
            params_json_string = json.dumps(params)
            header["Content-Type"] = "application/json; charset=utf-8"
            header["apiKey"] = self.secret_key_id
            header["signature"] = gen_signature(self.secret_key, params_json_string)
            rep = self.session.post(url, data=params_json_string, headers=header)
            # print(rep.url)
        try:
            data = rep.json()
        except ValueError:
            data = rep.text
        return data
    
    ######################################################################
    # Base Information
    # unified_url
    def list_venue(self):
        return self.http_request("get", "/utils/futures/exchange-list")

    # unified_url
    def list_currency(self, venue):
        return self.http_request("get", f"/utils/futures/currency-list/{venue}")

    # unified_url
    def list_symbol(self, venue):
        return self.http_request("get", f"/utils/futures/symbol-list/{venue}")

    ######################################################################
    # Account API
    # unified_url
    def create_account(self, **kwargs):
        return self.http_request("get", "/account/futures/enable", kwargs)

    # unified_url
    def transfer(self, **kwargs):
        return self.http_request("post", "/futures/asset/transfer", kwargs)

    # unified_url
    def transfer_record(self, **kwargs):
        return self.http_request("get", "/futures/transfer/list", kwargs)
        
    # unified_url
    def get_fund_list(self, **kwargs):
        return self.http_request("get", "/futures/fund/list", kwargs)

    # unified_url
    def get_account_info(self, **kwargs):
        return self.http_request("get", "/account/futures/info", kwargs)

    def list_balance(self, **kwargs):
        return self.http_request("get", "/futures/list-balance", kwargs)
    
    def get_position(self, **kwargs):
        return self.http_request("get", "/futures/position", kwargs)

    # unified_url
    def get_position_type(self, **kwargs):
        return self.http_request("get", "/futures/positionType", kwargs)

    # unified_url
    def update_position_type(self, **kwargs):
        return self.http_request("post", "/futures/updatePositionType", kwargs)

    # unified_url
    def update_margin_type(self, **kwargs):
        return self.http_request("post", "/futures/updateMarginType", kwargs)

    # unified_url=
    def update_leverage(self, **kwargs):
        return self.http_request("post", "/futures/updateLeverage", kwargs)

    # unified_url
    def update_position_margin(self, **kwargs):
        return self.http_request("post", "/futures/updatePositionMargin", kwargs)
    
    # unified_url
    def get_user_rate(self, **kwargs):
        return self.http_request("get", "/futures/getCommissionRate", kwargs)

    ######################################################################
    # Trading API
    def new_order(self, **kwargs):
        return self.http_request("post", "/fac/v1/order/newOrder", kwargs, unified_url=False)

    def cancel_order(self, **kwargs):
        return self.http_request("post", "/fac/v1/order/cancelOrder", kwargs, unified_url=False)

    def get_order(self, **kwargs):
        return self.http_request("get", "/order/futures/orderInfo", kwargs)

    def get_open_orders(self, **kwargs):
        return self.http_request("post", "/fac/v1/order/listOpenOrder", kwargs, unified_url=False)
    
    def get_all_orders(self, **kwargs):
        return self.http_request("get", "/order/futures/allOrders", kwargs)
    
    def get_fills(self, **kwargs):
        return self.http_request("get", "/order/futures/fills", kwargs)
