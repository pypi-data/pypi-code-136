import unittest
from fin_crawler import FinCrawler
import time
class Test_tw_stock_price_all_real(unittest.TestCase):
    def setUp(self):
        self.date = '20221007'
    def test_request(self):
        time.sleep(4)
        result_idx10={
            'stock_id': '2915',
            'stock_name': '潤泰全',
            'IIFI_buy_amount_woIIFD': 4154000.0,
            'IIFI_sell_amount_woIIFD': 781000.0,
            'IIFI_net_amount_woIIFD': 3373000.0,
            'IIFD_buy_amount': 0.0,
            'IIFD_sell_amount': 0.0,
            'IIFD_net_amount': 0.0,
            'IIIT_buy_amount': 0.0,
            'IIIT_sell_amount': 1000.0,
            'IIIT_net_amount': -1000.0,
            'IID_net_amount': -26000.0,
            'IID_buy_amount_self': 70000.0,
            'IID_sell_amount_self': 108000.0,
            'IID_net_amount_self': -38000.0,
            'IID_buy_amount_hedging': 18000.0,
            'IID_sell_amount_hedging': 6000.0,
            'IID_net_amount_hedging': 12000.0,
            'II_net_amount': 3346000.0,
            'date': '20221007'
        }
        result_idx500={
            'stock_id': '067464',
            'stock_name': 'T50正2元大1C購03',
            'IIFI_buy_amount_woIIFD': 0.0,
            'IIFI_sell_amount_woIIFD': 0.0,
            'IIFI_net_amount_woIIFD': 0.0,
            'IIFD_buy_amount': 0.0,
            'IIFD_sell_amount': 0.0,
            'IIFD_net_amount': 0.0,
            'IIIT_buy_amount': 0.0,
            'IIIT_sell_amount': 0.0,
            'IIIT_net_amount': 0.0,
            'IID_net_amount': 301000.0,
            'IID_buy_amount_self': 0.0,
            'IID_sell_amount_self': 0.0,
            'IID_net_amount_self': 0.0,
            'IID_buy_amount_hedging': 301000.0,
            'IID_sell_amount_hedging': 0.0,
            'IID_net_amount_hedging': 301000.0,
            'II_net_amount': 301000.0,
            'date': '20221007'
        }
        data = FinCrawler.get('tw_institutional_investors_daily',{'date':self.date})
        self.assertEqual(data[10],result_idx10)
        self.assertEqual(data[500],result_idx500)
    
    def test_request_no_data(self):
        time.sleep(4)
        data = FinCrawler.get('tw_institutional_investors_daily',{'date':'20221010'})
        self.assertEqual(data,[])
