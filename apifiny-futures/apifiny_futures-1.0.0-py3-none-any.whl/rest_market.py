#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  rest_market.py
@Time    :  2022/07/07 15:25:54
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

import requests


class MarketData:
    def __init__(self):
        self.base_url = "https://api.apifiny.com"
        self.session = requests.Session()

    def http_request(self, path):
        url = self.base_url + path
        rep = self.session.get(url)

        try:
            data = rep.json()
        except ValueError:
            data = rep.text
        return data

    # Market Data
    def get_mark(self, venue, symbol):
        return self.http_request(f"/fapi/md/mark/v1/{symbol}/{venue}")

    def get_order_book(self, venue, symbol):
        return self.http_request(f"/fapi/md/orderbook/v1/{symbol}/{venue}")

    def get_ticker(self, venue, symbol):
        return self.http_request(f"/fapi/md/ticker/v1/{symbol}/{venue}")

    def get_trade(self, venue, symbol):
        return self.http_request(f"/fapi/md/trade/v1/{symbol}/{venue}")

    def get_kline(self, venue, base, quote, period):
        return self.http_request(f"/fapi/md/kline/v1/{venue}/{base}/{quote}/{period}")
