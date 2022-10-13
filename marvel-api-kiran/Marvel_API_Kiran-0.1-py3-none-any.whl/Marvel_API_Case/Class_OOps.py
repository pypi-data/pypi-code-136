from asyncio.windows_events import NULL
import requests
import pandas as pd
from time import time
import hashlib
import pandas as pd
import string
import datetime


class marvel_kia:
    
    def _init_(self, public_key, private_key, address, hash):
        self.public_key = public_key
        self.private_key = private_key
        self.address = address
        self.hash = hash
    
    def get_data_with(self, name_starts_with):
        
        """
        returns a dataframe where character name starts with a specific string
        """
        try:
            params = {"apikey": self.public_key, "ts": datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S'), 
                    "hash": self.hash, "nameStartsWith": name_starts_with,
                    "limit" : 100}

            response = requests.get(self.address, params)
            print(response.json)
            df = pd.json_normalize(response.json(), record_path=['data','results'])

            df.drop(['modified', "resourceURI", "urls", "thumbnail.path", "thumbnail.extension", "comics.collectionURI", 
                        "series.items", "stories.collectionURI", "stories.items", "events.collectionURI", "events.items",
                        "comics.items", "series.collectionURI", "comics.returned", "series.returned", "stories.returned", 
                        "events.returned"], 
                    axis=1, inplace=True)
            return df
        except:
            print("Hash and/or API key is not provided")

    def filtered_data(self, data, column, condition,value):
        if column=='name' and condition=='name_starts_with':
            required_data = data[data[column.capitalize()][0]==value]  
        elif condition=='>':
            required_data = data[data[column.capitalize()]>value]
        elif condition=='<':
            required_data = data[data[column.capitalize()]<value]
        elif condition =='=':
            required_data = data[data[column.capitalize()]==value]
        elif condition == ('<=' or '=<'):
            required_data = data[data[column.capitalize()]<=value]
        elif condition == ('>=' or '=>'):
            required_data = data[data[column.capitalize()]<=value]
        
        return required_data

    
    def authorization(self):
        """
        arguments: web service endpoint, public key, private key
        computes hash and returns the complete address and parameter dictionary
        # """
        # api_url = url
        # api_url_2 = resource
        # address = api_url + api_url_2
        # address = self.address

        limit = 100 

        ts = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
        hash_param = ts + self.private_key + self.public_key
        hash_result = hashlib.md5(hash_param.encode())

        params = {"apikey": self.public_key, 
                    "ts": datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S'),
                    "hash": hash_result.hexdigest(),
                    "limit": limit}

        return params

    def dataframe(self, params):
        """
        arguments: parameters dictionary, web api address
        returns a dataframe
        """
        start_char = list(string.ascii_lowercase + string.digits)
        start_char.remove('0')

        df = pd.DataFrame()

        for letter in start_char :
            params["nameStartsWith"] = letter
            response = requests.get(self.address, params)
            temp_df = pd.json_normalize(response.json(), record_path=['data', 'results'])
            df = pd.concat([df, temp_df], ignore_index=True)
            del params["nameStartsWith"]
        
        df.drop(['modified', "resourceURI", "urls", "thumbnail.path", "thumbnail.extension", "comics.collectionURI", 
                        "series.items", "stories.collectionURI", "stories.items", "events.collectionURI", "events.items",
                        "comics.items", "series.collectionURI", "comics.returned", "series.returned", "stories.returned", 
                        "events.returned"], 
                    axis=1, inplace=True)
        return df