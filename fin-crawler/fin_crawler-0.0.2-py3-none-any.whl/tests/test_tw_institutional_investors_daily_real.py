import unittest
from fin_crawler import FinCrawler
import time
class Test_tw_stock_price_all_real(unittest.TestCase):
    def setUp(self):
        self.date = '20220922'
    def test_request(self):
        time.sleep(4)
        result = {
            'date':[self.date]*10,
            'IIFI_net_amount_woIIFD':[-84000.0,
                29006711.0,
                11132000.0,
                -871000.0,
                0.0,
                0.0,
                -132000.0,
                0.0,
                0.0,
                0.0],
            'IIIT_sell_amount':[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            'II_net_amount':[131158773.0,
                            28480928.0,
                            24199022.0,
                            13604146.0,
                            9001692.0,
                            7395000.0,
                            7192000.0,
                            6473377.0,
                            4662000.0,
                            4490000.0],
            'stock_id':['00632R',
                        '2834',
                        '00673R',
                        '00671R',
                        '00676R',
                        '06809P',
                        '00664R',
                        '00669R',
                        '078432',
                        '07060P']
        }
        data = FinCrawler.get('tw_institutional_investors_daily',{'date':self.date})
        self.assertEqual(data['IIFI_net_amount_woIIFD'][:10],result['IIFI_net_amount_woIIFD'])
        self.assertEqual(data['IIIT_sell_amount'][:10],result['IIIT_sell_amount'])
        self.assertEqual(data['II_net_amount'][:10],result['II_net_amount'])
        self.assertEqual(data['stock_id'][:10],result['stock_id'])
