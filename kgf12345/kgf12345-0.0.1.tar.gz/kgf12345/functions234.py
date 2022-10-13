import requests
import pandas as pd 
import json 
import hashlib 
import time
import datetime
import string 
from pandas import json_normalize
timestamp = datetime.datetime.now()
limit = 100
import argparse
parser = argparse.ArgumentParser(description="provide the private_key and public_key")
private_key = parser.add_argument('private_key',type=str,help='provide the private_key')
public_key = parser.add_argument('public_key',type=str,help='provide the public_key')


def hash_params():
    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{private_key}{public_key}'.encode('utf-8'))
    hashe_params = hash_md5.hexdigest()
    return hashe_params

#activity 3 function 

from asyncio.windows_events import NULL
import time
import datetime
import requests
import pandas as pd 
import json
from pandas import json_normalize
import hashlib


timestamp=datetime.datetime.now()
def gen_dataframe (nameStartsWith,APIKEY=NULL, HASH=NULL):
    if(APIKEY==NULL and HASH==NULL):
        raise Exception("NULL values not allowed")
    else:
        REQ_URL = "http://gateway.marvel.com/v1/public/characters"
       
        parameters = { "ts": timestamp, "apikey": APIKEY, "hash": HASH,
        "nameStartsWith": nameStartsWith}
        response = requests.get(REQ_URL,params=parameters)
        data_7 = response.json()
        df_7 = pd.json_normalize(data_7,record_path=['data','results'])
        df_new = df_7[['id','name','comics.available','stories.available','events.available']]
        return df_new

# activity 4 function

def gen_filter(df_63,column_name,filter):
    if filter[0]== '>':
        res_obt_df = df_63[df_63[column_name]>filter[1]]
    if filter[0]== '<':
        res_obt_df= df_63[df_63[column_name]<filter[1]]
    return res_obt_df