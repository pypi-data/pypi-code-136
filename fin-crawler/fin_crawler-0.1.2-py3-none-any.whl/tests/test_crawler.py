import unittest

from unittest.mock import MagicMock, patch

from fin_crawler.crawler import Crawler,FinCrawler
from fin_crawler.fetcher import Fetcher

class TestCrawler(unittest.TestCase):

    def test_crawler_url(self):
        parameters = {
            "fetch":{
                "url_template":"http://test.com/?date=**date**&stockNo=**stock_id**",
                'method':'GET',
                "url_params":{
                    "**date**":"20220922",
                    "**stock_id**":"2330"
                }
            },
            'parse':{
                'parse_data':{},
                'kwargs':{}
            }
        }

        crawler = Crawler(parameters)
        self.assertEqual(crawler.fetch_params['url'],'http://test.com/?date=20220922&stockNo=2330')



#     @patch('fin_crawler.crawler.Fetcher')
#     def test_fetch(self,mock_fetcher):
#         def parse_data_function(data,**kwargs):
#             return int(data['test'])+int(kwargs['value'])
#         parameters = {
#             "fetch":{
#                 "url_template":"http://test.com/?date=**date**&stockNo=**stock_id**",
#                 "url_params":{
#                     "**date**":"20220922",
#                     "**stock_id**":"2330"
#                 }
#             },
#             'parse':{
#                 'parse_data':parse_data_function,
#                 'kwargs':{'value':'234'}
#             }
#         }


#         mock_fetcher().fetch.return_value = {'test':'123'}

#         crawler = Crawler(parameters)
        
#         self.assertEqual(crawler.fetch(),357)


# class Test_FinCrawler(unittest.TestCase):
    
#     @patch('fin_crawler.plugins.test_module.gen_params')
#     def test_get(self,mock_gen_params):

#         fetch_params = {
#             "fetch":{
#                 "url_template":"http://test.com/?date=**date**&stockNo=**stock_id**",
#                 'method':'GET',
#                 "url_params":{
#                     "**date**":"20220922",
#                     "**stock_id**":"2330"
#                 }
#             },
#             'parse':{
#                 'parse_data':{},
#                 'kwargs':{}
#             }
#         }
#         mock_gen_params.return_value = fetch_params

#         result = FinCrawler.get('test_module',{})
#         fetcher = Fetcher(fetch_params)
#         self.assertEqual(result,fetch_params)