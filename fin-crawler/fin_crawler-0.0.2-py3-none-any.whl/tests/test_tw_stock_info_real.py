import unittest
from fin_crawler import FinCrawler
import time
class Test_tw_stock_info_real(unittest.TestCase):

    def test_request(self):
        time.sleep(4)
        result = {
            'website':['http://www.taiwancement.com',
                        'www.acc.com.tw',
                        'www.chcgroup.com.tw',
                        'www.ucctw.com',
                        'www.luckygrp.com.tw',
                        'www.hsingta.com.tw',
                        'www.southeastcement.com.tw',
                        'http://www.weichuan.com.tw',
                        'http://www.vewong.com',
                        'http://www.dachan.com'],

            'company_name':['台灣水泥股份有限公司',
                        '亞洲水泥股份有限公司',
                        '嘉新水泥股份有限公司',
                        '環球水泥股份有限公司',
                        '幸福水泥股份有限公司',
                        '信大水泥股份有限公司',
                        '東南水泥股份有限公司',
                        '味全食品工業股份有限公司',
                        '味王股份有限公司',
                        '大成長城企業股份有限公司'],

            'stock_id':['1101',
                        '1102',
                        '1103',
                        '1104',
                        '1108',
                        '1109',
                        '1110',
                        '1201',
                        '1203',
                        '1210'],

            'tax_id':['11913502',
                    '03244509',
                    '11892801',
                    '07568009',
                    '40601248',
                    '03279507',
                    '83078600',
                    '11347802',
                    '07067309',
                    '73008303']
        }
        data = FinCrawler.get('tw_stock_info',{})
        self.assertEqual(data['website'][:10],result['website'])
        self.assertEqual(data['company_name'][:10],result['company_name'])
        self.assertEqual(data['stock_id'][:10],result['stock_id'])
        self.assertEqual(data['tax_id'][:10],result['tax_id'])
