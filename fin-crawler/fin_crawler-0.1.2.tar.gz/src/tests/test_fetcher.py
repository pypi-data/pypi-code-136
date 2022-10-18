import unittest
from unittest.mock import MagicMock, patch

from fin_crawler.fetcher import Fetcher


class TestFetcher(unittest.TestCase):

    @patch('fin_crawler.fetcher.requests')
    def test_text_response(self,mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '123'

        mock_requests.get.return_value = mock_response

        fetch_params = {
            'url':'http://test.com/test',
            'method':'GET',
            'response_type':'text'
            }
        fetcher = Fetcher(fetch_params=fetch_params)
        self.assertEqual(fetcher.accept_codes,[200])
        self.assertEqual(fetcher.method,'get')
        self.assertEqual(fetcher.headers,None)
        self.assertEqual(fetcher.data,None)
        self.assertEqual(fetcher.response_type,'text')
        data = fetcher.fetch()

        self.assertEqual(data,'123')

    @patch('fin_crawler.fetcher.requests')
    def test_error500(self,mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 500

        mock_requests.get.return_value = mock_response

        fetch_params = {
            'url':'http://test.com/test',
            'method':'GET',
            'response_type':'text'
            }
        fetcher = Fetcher(fetch_params=fetch_params)
        with self.assertRaises(ConnectionError):
            fetcher.fetch()

    @patch('fin_crawler.fetcher.requests')
    def test_json_response(self,mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'test':'123'
        }
        mock_requests.get.return_value = mock_response
        fetch_params = {
            'url':'http://test.com/test',
            'method':'GET',
            }
        fetcher = Fetcher(fetch_params=fetch_params)
        self.assertEqual(fetcher.response_type,'json')
        data = fetcher.fetch()
        self.assertEqual(data,{'test':'123'})


    @patch('fin_crawler.fetcher.requests')
    def test_content_response(self,mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'123'
        mock_requests.get.return_value = mock_response
        fetch_params = {
            'url':'http://test.com/test',
            'method':'GET',
            'response_type':'content'
            }
        fetcher = Fetcher(fetch_params=fetch_params)
        self.assertEqual(fetcher.response_type,'content')
        data = fetcher.fetch()
        self.assertEqual(data,b'123')

    