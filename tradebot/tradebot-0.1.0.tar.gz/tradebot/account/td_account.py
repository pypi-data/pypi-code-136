from tradebot.requests import TradebotRequests
from tradebot.configs import TradebotConfigs

def get_account_info(configs:TradebotConfigs, fields:str=None):
    acct_number = configs["account_number"]
    url = f"https://api.tdameritrade.com/v1/accounts/{acct_number}"
    url_params = {"fields": fields} if fields else ''
    requests = TradebotRequests(configs)
    res = requests.get(url, params=url_params)
    assert res.ok

    return res.json()