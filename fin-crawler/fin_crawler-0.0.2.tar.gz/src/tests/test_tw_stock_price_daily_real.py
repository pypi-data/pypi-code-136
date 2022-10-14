import unittest
from fin_crawler import FinCrawler
import time
class Test_tw_stock_price_daily_real(unittest.TestCase):

    def test_request(self):
        time.sleep(4)
        result = {
            'date':['20210922', '20210922', '20210922', '20210922', '20210922', '20210922', '20210922', '20210922', '20210922', '20210922'],
            'open':[137.1, 56.5, 123.6, 65.5, 31.02, 23.48, 32.9, 93.65, 21.5, 65.45],
            'close':[137.2, 56.55, 123.45, 65.95, 31.13, 23.5, 32.9, 93.65, 22.1, 65.2],
            'stock_id':['0050', '0051', '0052', '0053', '0054', '0055', '0056', '0057', '0061', '006203']
        }
        data = FinCrawler.get('tw_stock_price_daily',{'date':'20210922'})
        self.assertEqual(data['open'][:10],result['open'])
        self.assertEqual(data['date'][:10],result['date'])
        self.assertEqual(data['close'][:10],result['close'])
        self.assertEqual(data['stock_id'][:10],result['stock_id'])
