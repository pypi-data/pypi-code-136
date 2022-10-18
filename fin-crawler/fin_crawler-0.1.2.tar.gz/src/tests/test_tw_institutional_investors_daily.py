import unittest

from fin_crawler.plugins.tw_institutional_investors_daily import gen_params_example,gen_params,parse

class Test_tw_stock_price(unittest.TestCase):
    def setUp(self):
        self.date = '20221012'
    def test_gen_params_example(self):
        self.assertEqual({'date':self.date},gen_params_example())

    def test_gen_params(self):

        # test normal case
        params = gen_params(**{'date':self.date})
        self.assertEqual(
            params['fetch']['url_template'],
            'https://www.twse.com.tw/fund/T86?response=json&date=**date**&selectType=ALL&_=**time_stamp**'
            )
        self.assertEqual(params['fetch']['url_params']['**date**'],self.date)
        self.assertEqual(params['parse']['kwargs']['date'],self.date)
        # test date with -
        params = gen_params(**{'date':'2022-10-12'})
        self.assertEqual(params['fetch']['url_params']['**date**'],self.date)
        self.assertEqual(params['parse']['kwargs']['date'],self.date)
        #test invalid date
        with self.assertRaises(ValueError):
            gen_params(**{'date':'2022-09-88'})


    def test_parse(self):
        test_data = {
            'stat':'OK',
            'data':[
                ['00632R',
                '元大台灣50反1   ',
                '9,475,000',
                '10,531,000',
                '-1,056,000',
                '0',
                '0',
                '0',
                '0',
                '0',
                '0',
                '33,113,360',
                '3,589,000',
                '2,837,000',
                '752,000',
                '78,438,681',
                '46,077,321',
                '32,361,360',
                '32,057,360']
            ],
            'fields':[
                "證券代號",
                "證券名稱",
                "外陸資買進股數(不含外資自營商)",
                "外陸資賣出股數(不含外資自營商)",
                "外陸資買賣超股數(不含外資自營商)",
                "外資自營商買進股數",
                "外資自營商賣出股數",
                "外資自營商買賣超股數",
                "投信買進股數",
                "投信賣出股數",
                "投信買賣超股數",
                "自營商買賣超股數",
                "自營商買進股數(自行買賣)",
                "自營商賣出股數(自行買賣)",
                "自營商買賣超股數(自行買賣)",
                "自營商買進股數(避險)",
                "自營商賣出股數(避險)",
                "自營商買賣超股數(避險)",
                "三大法人買賣超股數"
            ]
        }
        result = parse(test_data,**{'date':self.date})
        self.assertEqual(
            result[0],
            {'stock_id': '00632R',
            'stock_name': '元大台灣50反1',
            'IIFI_buy_amount_woIIFD': 9475000.0,
            'IIFI_sell_amount_woIIFD': 10531000.0,
            'IIFI_net_amount_woIIFD': -1056000.0,
            'IIFD_buy_amount': 0.0,
            'IIFD_sell_amount': 0.0,
            'IIFD_net_amount': 0.0,
            'IIIT_buy_amount': 0.0,
            'IIIT_sell_amount': 0.0,
            'IIIT_net_amount': 0.0,
            'IID_net_amount': 33113360.0,
            'IID_buy_amount_self': 3589000.0,
            'IID_sell_amount_self': 2837000.0,
            'IID_net_amount_self': 752000.0,
            'IID_buy_amount_hedging': 78438681.0,
            'IID_sell_amount_hedging': 46077321.0,
            'IID_net_amount_hedging': 32361360.0,
            'II_net_amount': 32057360.0,
            'date': '20221012'}
        )
