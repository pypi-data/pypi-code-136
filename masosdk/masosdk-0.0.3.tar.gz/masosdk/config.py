import requests

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


class Config:
    base_url = 'https://maso.isibrno.cz/api'