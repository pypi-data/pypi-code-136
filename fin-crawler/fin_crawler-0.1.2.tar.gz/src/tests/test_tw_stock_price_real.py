import unittest
from fin_crawler import FinCrawler
import time
class Test_tw_stock_price_real(unittest.TestCase):

    def test_reuqest(self):
        time.sleep(4)
        result_idx1 = {
            'date': '20220902',
            'volume': 33877655.0,
            'trade_amount': 16486942365.0,
            'open': 488.0,
            'high': 489.5,
            'low': 485.0,
            'close': 485.0,
            'spread_value': -5.5,
            'trade_num': 71175.0,
            'stock_id': '2330'
            }
        result_idx5 = {
            'date': '20220908',
            'volume': 35355467.0,
            'trade_amount': 16755699888.0,
            'open': 473.0,
            'high': 475.0,
            'low': 472.0,
            'close': 475.0,
            'spread_value': 2.5,
            'trade_num': 37943.0,
            'stock_id': '2330'
            }
        data = FinCrawler.get('tw_stock_price',{'date':'20220920','stock_id':'2330'})

        self.assertEqual(data[1],result_idx1)
        self.assertEqual(data[5],result_idx5)