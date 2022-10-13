from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import requests
from dateutil import parser


class ICE():
    @staticmethod
    def commodity_prices(products):
        with ThreadPoolExecutor(max_workers=16) as executor:
            indata_list = ICE._flatten_list(list(executor.map(ICE._get_product_prices, products)))
        return indata_list

    @staticmethod
    def commodity_prices_df(products):
        import pandas as pd
        indata_list = ICE.commodity_prices(products)
        df = pd.DataFrame(indata_list)
        df = df.pivot_table(index='date', columns='product', values='value')
        df = df.resample('D').ffill()
        return df

    @classmethod
    def _get_product_prices(cls, product):
        product_dict = cls._product_data()
        product = product_dict[product]
        contracts_url = product['contracts_url']
        contracts = requests.get(contracts_url).json()
        if product['mth'] == 'next':
            market_strip_month = datetime(datetime.today().year, datetime.today().month + 1, 1).strftime('%b')
        elif product['mth'] == 'nextnext':
            market_strip_month = datetime(datetime.today().year, datetime.today().month + 2, 1).strftime('%b')
        else:
            market_strip_month = product['mth']
        market_id = [obs for obs in contracts if
                     obs['marketStrip'] == f'{market_strip_month}{str(datetime.today().year)[2:]}'][0]['marketId']
        data_url = f'https://www.theice.com/marketdata/DelayedMarkets.shtml?' \
                   f'getHistoricalChartDataAsJson=&marketId={market_id}&historicalSpan=3'
        data_list = [{'product': product['name'], 'date': parser.parse(x[0]), 'value': x[1]} for x in
                     requests.get(data_url).json()['bars']]
        return data_list

    @classmethod
    def _flatten_list(cls, list):
        return [item for sublist in list for item in sublist]

    @classmethod
    def _product_data(cls):
        product_dict = {
            "Coal": {"name": "Coal price",
                     "contracts_url": "https://www.theice.com/marketdata/DelayedMarkets.shtml?getContractsAsJson=&productId=517&hubId=681",
                     "mth": "next"},
            "CO2": {"name": "CO2 price",
                    "contracts_url": "https://www.theice.com/marketdata/DelayedMarkets.shtml?getContractsAsJson=&productId=390&hubId=564",
                    "mth": "Dec"},
            "Gas": {"name": "Gas price",
                    "contracts_url": "https://www.theice.com/marketdata/DelayedMarkets.shtml?getContractsAsJson=&productId=4331&hubId=7979",
                    "mth": "next"},
            "Oil": {"name": "Oil price",
                    "contracts_url": "https://www.theice.com/marketdata/DelayedMarkets.shtml?getContractsAsJson=&productId=254&hubId=403",
                    "mth": "nextnext"}
        }
        return product_dict
