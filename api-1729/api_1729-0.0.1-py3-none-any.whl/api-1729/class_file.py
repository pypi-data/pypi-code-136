import requests
import json
import hashlib
import pandas as pd
import datetime
import string
from pprint import pprint as pp
import time
from pandas import json_normalize
import os
import argparse
ts=datetime.datetime.now()

class API_CALL:
    def __init__(self,public_key,private_key,address,hash):
        self.public_key = public_key
        self.private_key = private_key
        self.address = address
        self.hash = hash
    
    def dataframe_generator(self,nameStartsWith):
        global df
        APIKEY=self.public_key
        Hash=self.hash
        if APIKEY is None or Hash is None:
            raise Exception("Expected arguments!!!")
        else:
            request_url = 'http://gateway.marvel.com/v1/public/characters'
            params ={'ts':ts,'apikey':APIKEY,'hash':Hash,
          'nameStartsWith':nameStartsWith,'limit':100}
            response = requests.get(request_url,params=params)
            data_1 =response.json()
            df = pd.json_normalize(data_1,record_path=['data','results'])
            df_new=df[['name','id','comics.available','stories.available',
                       'events.available','series.available']]
            return df_new
    
    
    def filter_character(self,dataframe,column,filter):
        if filter[0]=='>':
            filt_df=dataframe[dataframe[column]>filter[1]]
        if filter[0]=='<':
            filt_df=dataframe[dataframe[column]<filter[1]]
        if filter[0]=='=':
            filt_df=dataframe[dataframe[column]==filter[1]]
        return filt_df

    
    def params(self):
        limit = 100 
        hash_md5 = hashlib.md5()
        hash_md5.update(f'{ts}{self.private_key}{self.public_key}'.encode('utf-8'))
        hash_params = hash_md5.hexdigest()

        params = {"apikey": self.public_key, 
                    "ts": ts, 
                    "hash": hash_params,
                    "limit": limit}

        return params

    def dataframe(self,params):
        appended_data=[]  
        for i in string.ascii_uppercase:  
            nameStartsWith = i
            response = requests.get(self.address,params=params)
            data_1 =response.json()
            df_1 = pd.json_normalize(data_1,record_path=['data','results'])
            appended_data.append(df_1)
        df=pd.concat(appended_data)
        df_new=df[['name','id','comics.available','stories.available',
                            'events.available','series.available']]
        return df_new

                
