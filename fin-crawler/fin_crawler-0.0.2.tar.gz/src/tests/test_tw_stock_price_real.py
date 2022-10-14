import unittest
from fin_crawler import FinCrawler
import time
class Test_tw_stock_price_real(unittest.TestCase):

    def test_reuqest(self):
        time.sleep(4)
        result = {
            'date':['20210901', '20210902', '20210903', '20210906', '20210907', '20210908', '20210909', '20210910', '20210913', '20210914', '20210915', '20210916', '20210917', '20210922', '20210923', '20210924', '20210927', '20210928', '20210929', '20210930'],
            'open':[614.0, 613.0, 610.0, 623.0, 634.0, 622.0, 612.0, 615.0, 619.0, 618.0, 610.0, 603.0, 600.0, 586.0, 588.0, 591.0, 600.0, 595.0, 580.0, 580.0],
            'close':[613.0, 607.0, 620.0, 631.0, 623.0, 619.0, 619.0, 622.0, 615.0, 613.0, 607.0, 600.0, 600.0, 586.0, 588.0, 598.0, 602.0, 594.0, 580.0, 580.0]
        }
        data = FinCrawler.get('tw_stock_price',{'date':'20210920','stock_id':'2330'})
        self.assertEqual(data['open'],result['open'])
        self.assertEqual(data['date'],result['date'])
        self.assertEqual(data['close'],result['close'])
