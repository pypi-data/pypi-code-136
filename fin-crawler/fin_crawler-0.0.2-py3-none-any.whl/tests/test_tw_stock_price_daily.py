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
            ]
        }
        result = parse(test_data,**{'date':'20220920'})
        self.assertEqual(
            result,
            {
                "stock_id":['0050'],
                "stock_name":['元大台灣50'],
                "vol":[5999746],
                "trade_num":[7093],
                "trade_amount":[675492164],
                "open":[112.55],
                "close":[113.05],
                "high":[113.15],
                "low":[112.25],
                "spread":[1],
                "date":['20220920']
            }
        )


        test_data = {
            'stat':'OK',
            'data8':[
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
            ]
        }
        result = parse(test_data,**{'date':'20220920'})
        self.assertEqual(
            result,
            {
                "stock_id":['0050'],
                "stock_name":['元大台灣50'],
                "vol":[5999746],
                "trade_num":[7093],
                "trade_amount":[675492164],
                "open":[112.55],
                "close":[113.05],
                "high":[113.15],
                "low":[112.25],
                "spread":[1],
                "date":['20220920']
            }
        )



        empty_result =  {
            "stock_id":[],
            "stock_name":[],
            "vol":[],
            "trade_num":[],
            "trade_amount":[],
            "open":[],
            "close":[],
            "high":[],
            "low":[],
            "spread":[],
            "date":[]
        }
        
        # stat is not 'OK'
        test_data = {
            'stat':'123',
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
            ]
        }
        result = parse(test_data,**{'date':'20220922'})
        self.assertEqual(result,empty_result)

        #without key 'data'
        test_data = {
            'stat':'OK',
            'data7':[
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
            ]
        }
        result = parse(test_data,**{'date':'20220922','stock_id':'2330'})
        self.assertEqual(result,empty_result)

        #empty test ata
        test_data = {}
        result = parse(test_data,**{'date':'20220922','stock_id':'2330'})
        self.assertEqual(result,empty_result)