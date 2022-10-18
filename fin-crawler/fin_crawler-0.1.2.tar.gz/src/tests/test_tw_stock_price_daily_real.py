import unittest
from fin_crawler import FinCrawler
import time
from math import nan
class Test_tw_stock_price_daily_real(unittest.TestCase):

    def test_request(self):
        time.sleep(4)
        result_idx1 = {
            'stock_id': '0051',
            'stock_name': '元大中型100',
            'volume': 72013.0,
            'trade_num': 148.0,
            'trade_amount': 4072517.0,
            'open': 56.5,
            'high': 56.8,
            'low': 56.4,
            'close': 56.55,
            'last_buy_price': 56.55,
            'last_buy_volume': 1.0,
            'last_sell_price': 56.6,
            'last_sell_volume': 35.0,
            'PE': 0.0,
            'spread': -1,
            'date': '20210922'
            }
        result_idx500 = {
            'stock_id': '030325',
            'stock_name': '長榮麥證0C購01',
            'volume': 0.0,
            'trade_num': 0.0,
            'trade_amount': 0.0,
            'open': nan,
            'high': nan,
            'low': nan,
            'close': nan,
            'last_buy_price': 15.6,
            'last_buy_volume': 10.0,
            'last_sell_price': nan,
            'last_sell_volume': 0.0,
            'PE': 0.0,
            'spread': -1,
            'date': '20210922'
            }

        data = FinCrawler.get('tw_stock_price_daily',{'date':'20210922'})

        self.assertEqual(data[1],result_idx1)
        self.assertEqual(data[500],result_idx500)
    
    def test_request_no_result(self):
        time.sleep(4)
        data = FinCrawler.get('tw_stock_price_daily',{'date':'20221010'})

        self.assertEqual(data,[])
