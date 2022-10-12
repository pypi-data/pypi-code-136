from pprint import pprint
from pathlib import Path

from tradebot.configs import TradebotConfigs
from tradebot.requests import auth_get_request, auth_post_request


class Tradebot:

    def __init__(self, configs:TradebotConfigs):
        self.__configs = configs


    def __request_new_access_token(self, ):

        consumer_key, refresh_token = self.__configs["consumer_key"], self.__configs["refresh_token"]
        auth_url = "https://api.tdameritrade.com/v1/oauth2/token"
        
        req_body = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": consumer_key + "@AMER.OAUTHAP",
        }

        res = auth_post_request(auth_url, data=req_body)
        if not res.ok:
            raise Exception("Response was not ok; could not get new access token")

        return res.json()


    def update_access_token(self, ):
        new_data = self.__request_new_access_token()
        self.__configs.update(new_data)


    def fundamentals(self, ticker:str):

        url = "https://api.tdameritrade.com/v1/instruments"
        url_params = {"apikey": self.__configs["consumer_key"], "symbol": ticker, "projection": "fundamental"}
        
        res = auth_get_request(url, params=url_params)
        if not res.ok:
            print("Response was not ok for the url:")
            print("URL: " + url)
            return res

        return res.json()
        

    def quote(self, ticker:str):
        
        url = f"https://api.tdameritrade.com/v1/marketdata/{ticker}/quotes"
        res = auth_get_request(url)
        assert res.ok

        return res.json()
