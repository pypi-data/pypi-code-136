import importlib
from fin_crawler.fetcher import Fetcher


class Crawler:

    """
    Handling crawl actions
    Will generate Crawler needed parameters and send to fetch to fetch data
    
    """

    def __init__(self,parameters: dict):

        self.parameters = parameters
        self.fetch_params = self.parameters['fetch']
        self.fetch_params['url'] = self.gen_url(self.fetch_params)
        # self.fetch_params['headers'] = self.gen_headers(self.fetch_params)
        # self.fetch_params['data'] = self.gen_data(self.fetch_params)
        self.fetcher = Fetcher(self.fetch_params)
        self.parse = self.parameters['parse']['parse_data']
        self.parse_kwargs = self.parameters['parse']['kwargs']

    def gen_url(self,fetch_params):
        url = fetch_params['url_template']
        for param_name,param_value in fetch_params['url_params'].items():
            url = url.replace(param_name,param_value)
        return url
    # def gen_headers(self,fetch_params):
    #     headers = fetch_params.get('headers_template') or {}
    #     headers_params = fetch_params.get('headers_params') or {}
    #     for name,value in headers_params.items():
    #         headers.replace(name,value)
    #     return headers
    # def gen_data(self,fetch_params):
    #     return {}
    def fetch(self)->dict:
        response_data = self.fetcher.fetch()
        return self.parse(response_data,**self.parse_kwargs)




class FinCrawler:
    plugin_path = 'fin_crawler.plugins'
    @classmethod
    def get(cls,data_type,params={}):
        gen_params = getattr(
            importlib.import_module(f'{cls.plugin_path}.{data_type}'),
            'gen_params'
            )
        crawler = Crawler(gen_params(**params))
        return crawler.fetch()
    
    @classmethod
    @property
    def crawler_list(cls):
        return getattr(importlib.import_module(cls.plugin_path),'crawler_list')
    
    @classmethod
    def params_example(cls,data_type):
        gen_params_example = getattr(
            importlib.import_module(f'{cls.plugin_path}.{data_type}'),
            'gen_params_example'
            )
        return gen_params_example()
    @classmethod
    def col_names(cls,data_type):
        gen_col_names = getattr(
            importlib.import_module(f'{cls.plugin_path}.{data_type}'),
            'gen_col_names'
            )
        return gen_col_names()