import unittest

from fin_crawler.plugins.tw_institutional_investors_daily import gen_params_example,gen_params,parse

class Test_tw_stock_price(unittest.TestCase):
    def setUp(self):
        self.date = '20221012'
        self.empty_result = {
                "stock_id":[],
                "stock_name":[],
                "IIFI_buy_amount_woIIFD":[],
                "IIFI_sell_amount_woIIFD":[],
                "IIFI_net_amount_woIIFD":[],
                "IIFD_buy_amount":[],
                "IIFD_sell_amount":[],
                "IIFD_net_amount":[],
                "IIIT_buy_amount":[],
                "IIIT_sell_amount":[],
                "IIIT_net_amount":[],
                "IID_net_amount":[],
                "IID_buy_amount_self":[],
                "IID_sell_amount_self":[],
                "IID_net_amount_self":[],
                "IID_buy_amount_hedging":[],
                "IID_sell_amount_hedging":[],
                "IID_net_amount_hedging":[],
                "II_net_amount":[],
                "date":[]
            }
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
            ]
        }
        result = parse(test_data,**{'date':self.date})
        self.assertEqual(
            result,
            {
                "stock_id":['00632R'],
                "stock_name":['元大台灣50反1'],
                "IIFI_buy_amount_woIIFD":[9475000],
                "IIFI_sell_amount_woIIFD":[10531000],
                "IIFI_net_amount_woIIFD":[-1056000],
                "IIFD_buy_amount":[0],
                "IIFD_sell_amount":[0],
                "IIFD_net_amount":[0],
                "IIIT_buy_amount":[0],
                "IIIT_sell_amount":[0],
                "IIIT_net_amount":[0],
                "IID_net_amount":[33113360],
                "IID_buy_amount_self":[3589000],
                "IID_sell_amount_self":[2837000],
                "IID_net_amount_self":[752000],
                "IID_buy_amount_hedging":[78438681],
                "IID_sell_amount_hedging":[46077321],
                "IID_net_amount_hedging":[32361360],
                "II_net_amount":[32057360],
                "date":[self.date]
            }
        )


    def test_parse_stat_not_ok(self):
        # stat is not 'OK'
        test_data = {
            'stat':'123',
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
            ]
        }
        result = parse(test_data,**{'date':self.date})
        self.assertEqual(result,self.empty_result)
    def test_parse_no_key(self):
        #without key 'data'
        test_data = {
            'stat':'123',
            'data1':[
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
            ]
        }
        result = parse(test_data,**{'date':self.date})
        self.assertEqual(result,self.empty_result)
    def test_parse_no_data(self):
        #empty test ata
        test_data = {}
        result = parse(test_data,**{'date':self.date})
        self.assertEqual(result,self.empty_result)