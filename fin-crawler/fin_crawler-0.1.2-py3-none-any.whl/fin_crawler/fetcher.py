
import requests

class Fetcher:
    """
    Handling requests action including sending request and parse response object

    fetch_params:
        url: requests url
        method: requests method
        headers: requests headers
        data: data send with requests
        response_type: response parsing type (json/text/content)
        accept_codes: accepted response code, code usually will be 200 if not will raise ConnectionError
    """

    def __init__(self,fetch_params):
        self.url = fetch_params['url']
        self.method = fetch_params['method'].lower()
        self.headers = fetch_params.get('headers')
        self.data = fetch_params.get('data')
        self.response_type = fetch_params.get('response_type') or 'json'
        self.accept_codes = fetch_params.get('accept_codes') or [200]
    def fetch(self):
        response = eval(f"self.{self.method}()")
        if response.status_code in self.accept_codes:
            response_data = self.parse_response(response)
            return response_data
        else:
            raise ConnectionError(f"Response Error:{response.content}")
    def get(self):
        return requests.get(self.url,headers=self.headers)
    
    def parse_response(self,response):
        if self.response_type=='json':
            return response.json()
        elif self.response_type=='text':
            return response.text
        else:
            return response.content