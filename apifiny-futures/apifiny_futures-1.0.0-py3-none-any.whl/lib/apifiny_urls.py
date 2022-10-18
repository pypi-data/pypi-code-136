#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  apifiny_urls.py
@Time    :  2022/07/06 19:12:07
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

urls = {
    'REST': {
        'BINANCE': 'https://apibn.apifiny.com', 'BINANCEUS': 'https://apibnu.apifiny.com',
        'COINBASEPRO': 'https://apicb.apifiny.com', 'FTX': 'https://apiftx.apifiny.com',
        'HUOBI': 'https://apihb.apifiny.com', 'KUCOIN': 'https://apikc.apifiny.com',
        'OKCOIN': 'https://apiokc.apifiny.com', 'OKX': 'https://apiok.apifiny.com', 'MAIN': 'https://api.apifiny.com'},
    'WS': {
        'BINANCE': 'wss://apibn.apifiny.com', 'BINANCEUS': 'wss://apibnu.apifiny.com',
        'COINBASEPRO': 'wss://apicb.apifiny.com', 'FTX': 'wss://apiftx.apifiny.com', 'HUOBI': 'wss://apihb.apifiny.com',
        'KUCOIN': 'wss://apikc.apifiny.com', 'OKCOIN': 'wss://apiokc.apifiny.com', 'OKX': 'wss://apiok.apifiny.com',
        'MAIN': 'wss://api.apifiny.com'},
    'FIX': {
        'BINANCE': 'fixapibn.apifiny.com:1443', 'BINANCEUS': 'fixapibnu.apifiny.com:1443',
        'COINBASEPRO': 'fixapicb.apifiny.com:1443', 'FTX': 'fixapiftx.apifiny.com:1443',
        'HUOBI': 'fixapihb.apifiny.com:1443', 'KUCOIN': 'fixapikc.apifiny.com:1443',
        'OKCOIN': 'fixapiokc.apifiny.com:1443', 'OKEX': 'fixapiok.apifiny.com:1443', 'MAIN': 'fix.api.apifiny.com:1443'}
}
