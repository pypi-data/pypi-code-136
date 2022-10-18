import unittest

from fin_crawler.plugins.tw_stock_price_daily import gen_params_example,gen_params,parse

class Test_tw_stock_price_dialy(unittest.TestCase):
    
    def test_gen_params_example(self):
        self.assertEqual({'date':'20220920'},gen_params_example())

    def test_gen_params(self):

        # test normal case
        params = gen_params(**{'date':'20220922'})
        self.assertEqual(params['fetch']['url_template'],'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=**date**&type=ALL&_=**time_stamp**')
        self.assertEqual(params['fetch']['url_params']['**date**'],'20220922')
        self.assertEqual(params['parse']['kwargs']['date'],'20220922')
        # test date with -
        params = gen_params(**{'date':'2022-09-22','stock_id':'2330'})
        self.assertEqual(params['fetch']['url_params']['**date**'],'20220922')
        self.assertEqual(params['parse']['kwargs']['date'],'20220922')
        #test invalid date
        with self.assertRaises(ValueError):
            gen_params(**{'date':'2022-09-88'})


    def test_parse(self):
        test_data = {
            'stat':'OK',
            'data9':[
                ['0050',
                '元大台灣50',
                '5,999,746',
                '7,093',
                '675,492,164',
                '112.55',
                '113.15',
                '112.25',
                '113.05',
                '<p style= color:red>+</p>',
                '1.00',
                '113.00',
                '205',
                '113.05',
                '9',
                '0.00'],
            ],
            'fields9':[
                "證券代號",
                "證券名稱",
                "成交股數",
                "成交筆數",
                "成交金額",
                "開盤價",
                "最高價",
                "最低價",
                "收盤價",
                "漲跌(+/-)",
                "漲跌價差",
                "最後揭示買價",
                "最後揭示買量",
                "最後揭示賣價",
                "最後揭示賣量",
                "本益比"
            ]
        }
        result = parse(test_data)[0]
        self.assertEqual(result['spread'],1.0)
        self.assertEqual(result['stock_id'],'0050')
        self.assertEqual(result['high'],113.15)

