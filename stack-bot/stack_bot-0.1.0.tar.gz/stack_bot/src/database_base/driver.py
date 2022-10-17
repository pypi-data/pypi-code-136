import ydb
import requests


class Driver(object):
    
    def __init__(self, database: str, endpoint: str, iamToken: str="", oauth: str=""):
        self.database = database
        self.endpoint = endpoint
        self.iamToken = iamToken
        self.oauth = oauth

        self.update_credentials(get_new_token=True)
    
    def update_pool_and_driver(self):
        self.actual_driver = ydb.Driver(
            database=self.database, 
            endpoint=self.endpoint,
            credentials=ydb.AccessTokenCredentials(self.iamToken)
        )

        self.actual_driver.wait(fail_fast=True, timeout=5)
        self.pool = ydb.SessionPool(self.actual_driver)
    
    def update_credentials(self, get_new_token=False):
        if get_new_token:

            response = requests.post(
                url="https://iam.api.cloud.yandex.net/iam/v1/tokens",
                data="{\"yandexPassportOauthToken\":\"" + self.oauth + "\"}"
            )

            if response.status_code == 200:
                self.iamToken = response.json()['iamToken']
        
        self.update_pool_and_driver()
